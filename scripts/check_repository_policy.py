#!/usr/bin/env python3
"""Dependency-free checks for repository governance and workflow hardening."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = (
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    "AGENTS.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE",
    "MAINTAINERS.md",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "docs/README.md",
    "docs/THREAT_MODEL.md",
    "repository-profile.json",
)

ESSENTIAL_PROJECT_FILES = (
    ".github/CODEOWNERS",
    "LICENSE",
    "MAINTAINERS.md",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "docs/THREAT_MODEL.md",
    "repository-profile.json",
)

PLACEHOLDER_PATTERNS = (
    "YOUR-ORG",
    "YOUR-TEAM",
    "YOUR-ORGANIZATION",
    "example.invalid",
    "security@example.invalid",
    "{{",
    "TEMPLATE LICENSE PLACEHOLDER",
)

SECRET_PATTERNS = (
    ("private key material", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
)

MAX_TRACKED_FILE_BYTES = 10 * 1024 * 1024
MAX_AGENTS_BYTES = 32 * 1024
FULL_SHA = re.compile(r"[0-9a-fA-F]{40}")
USES_LINE = re.compile(r"^\s*(?:-\s*)?uses:\s*['\"]?([^'\"\s#]+)", re.MULTILINE)


def tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, check=False
    )
    if result.returncode == 0:
        return [root / Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]
    return [path for path in root.rglob("*") if path.is_file() and ".git" not in path.parts]


def is_environment_file(relative: str) -> bool:
    name = Path(relative).name
    if name == ".env.example" or (name.startswith(".env.") and name.endswith(".example")):
        return False
    return name == ".env" or name.startswith(".env.")


def action_reference_failures(text: str, workflow_name: str) -> list[str]:
    failures: list[str] = []
    for reference in USES_LINE.findall(text):
        if reference.startswith("./") or reference.startswith("docker://"):
            continue
        if "@" not in reference:
            failures.append(f"{workflow_name}: action reference has no immutable ref: {reference}")
            continue
        _, ref = reference.rsplit("@", 1)
        if not FULL_SHA.fullmatch(ref):
            failures.append(
                f"{workflow_name}: action/reusable workflow is not pinned to a full SHA: {reference}"
            )
    return failures


def load_profile(root: Path, failures: list[str]) -> dict:
    try:
        profile = json.loads((root / "repository-profile.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"repository-profile.json is unreadable or invalid JSON: {exc}")
        return {}
    if profile.get("schemaVersion") != 1:
        failures.append("repository-profile.json schemaVersion must be 1.")
    return profile


def validate_profile(
    root: Path, profile: dict, repository_name: str | None, failures: list[str], warnings: list[str]
) -> None:
    template = profile.get("template", {})
    project = profile.get("project", {})
    ownership = profile.get("ownership", {})
    legal = profile.get("legal", {})
    stack = profile.get("stack", {})
    verification = profile.get("verification", {})
    is_template = template.get("isTemplate") is True

    if is_template:
        expected_name = template.get("repositoryName")
        if repository_name and repository_name != expected_name:
            failures.append(
                "This repository was created from the template but was not bootstrapped: "
                f"expected template repository name {expected_name!r}, got {repository_name!r}."
            )
        if project.get("lifecycle") != "template":
            failures.append("A template repository must use project.lifecycle 'template'.")
        return

    required_values = {
        "project.name": project.get("name"),
        "project.description": project.get("description"),
        "project.type": project.get("type"),
        "project.lifecycle": project.get("lifecycle"),
        "ownership.primaryTeam": ownership.get("primaryTeam"),
        "ownership.securityContact": ownership.get("securityContact"),
        "ownership.supportUrl": ownership.get("supportUrl"),
        "legal.license": legal.get("license"),
        "legal.licenseHolder": legal.get("licenseHolder"),
        "stack.profile": stack.get("profile"),
    }
    for label, value in required_values.items():
        if value in (None, "", "none", "template", "unselected"):
            failures.append(f"repository-profile.json requires a real {label} value.")

    if repository_name and project.get("name") != repository_name:
        failures.append(
            f"project.name {project.get('name')!r} does not match repository name {repository_name!r}."
        )

    lifecycle = project.get("lifecycle")
    if lifecycle not in {"bootstrapping", "active", "maintenance", "deprecated", "archived"}:
        failures.append(f"Unsupported project.lifecycle: {lifecycle!r}.")
    if lifecycle == "bootstrapping":
        warnings.append("Project remains in bootstrapping state; application merge gates are not complete.")
    if lifecycle == "active" and not verification.get("commands"):
        failures.append("Active projects must declare verification.commands.")
    if lifecycle == "active":
        architecture = (root / "docs/architecture/README.md").read_text(encoding="utf-8")
        threat_model = (root / "docs/THREAT_MODEL.md").read_text(encoding="utf-8")
        if "_To be defined_" in architecture:
            failures.append("Active projects must replace the architecture template content.")
        if "Status: incomplete template" in threat_model:
            failures.append("Active projects must complete the threat model status.")


def check_placeholders(root: Path, failures: list[str]) -> None:
    for relative in ESSENTIAL_PROJECT_FILES:
        path = root / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for placeholder in PLACEHOLDER_PATTERNS:
            if placeholder in text:
                failures.append(f"{relative}: unresolved template placeholder {placeholder!r}.")


def check_workflows(root: Path, failures: list[str]) -> None:
    workflow_dir = root / ".github/workflows"
    if not workflow_dir.exists():
        failures.append(".github/workflows is missing.")
        return
    workflows = sorted([*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")])
    if not workflows:
        failures.append("No active GitHub workflow exists.")
        return
    for workflow in workflows:
        relative = workflow.relative_to(root).as_posix()
        text = workflow.read_text(encoding="utf-8")
        failures.extend(action_reference_failures(text, relative))
        if re.search(r"^\s*permissions:\s*write-all\s*$", text, re.MULTILINE):
            failures.append(f"{relative}: permissions write-all is forbidden.")
        if re.search(r"^\s*pull_request_target\s*:", text, re.MULTILINE):
            failures.append(
                f"{relative}: pull_request_target requires a separately approved threat model."
            )
        if not re.search(r"^permissions:\s*$", text, re.MULTILINE):
            failures.append(f"{relative}: top-level permissions block is required.")


def check_tracked_files(root: Path, files: list[Path], failures: list[str]) -> None:
    for path in files:
        try:
            relative = path.relative_to(root).as_posix()
        except ValueError:
            continue
        if is_environment_file(relative):
            failures.append(f"Tracked environment file is forbidden: {relative}.")
        if path.is_symlink():
            failures.append(f"Tracked symlink is not portable across supported environments: {relative}.")
        try:
            size = path.stat().st_size
        except OSError as exc:
            failures.append(f"Cannot stat tracked file {relative}: {exc}")
            continue
        if size > MAX_TRACKED_FILE_BYTES:
            failures.append(f"Tracked file exceeds 10 MiB baseline: {relative} ({size} bytes).")

        if relative.startswith(".template/") or path.suffix.lower() in {
            ".gif",
            ".ico",
            ".jpg",
            ".jpeg",
            ".pdf",
            ".png",
            ".webp",
            ".woff",
            ".woff2",
            ".zip",
        }:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                failures.append(f"Possible {label} in tracked file: {relative}.")
        if re.search(r"curl\b[^\n|]*\|\s*(?:ba)?sh\b", text):
            failures.append(f"Unpinned network installer pipeline found in {relative}.")


def run(root: Path, repository_name: str | None = None) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).exists():
            failures.append(f"Required file is missing: {relative}.")

    profile = load_profile(root, failures)
    if profile:
        validate_profile(root, profile, repository_name, failures, warnings)
        if not profile.get("template", {}).get("isTemplate"):
            check_placeholders(root, failures)

    agents = root / "AGENTS.md"
    if agents.exists() and agents.stat().st_size > MAX_AGENTS_BYTES:
        failures.append(
            f"AGENTS.md exceeds the 32 KiB baseline ({agents.stat().st_size} bytes); "
            "move subsystem detail closer to the code."
        )

    check_workflows(root, failures)
    check_tracked_files(root, tracked_files(root), failures)
    return failures, warnings


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures, warnings = run(root, os.environ.get("REPOSITORY_NAME"))

    for warning in warnings:
        print(f"WARNING: {warning}")
    if failures:
        print("Repository policy failed:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print(f"Repository policy passed ({len(REQUIRED_FILES)} required files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
