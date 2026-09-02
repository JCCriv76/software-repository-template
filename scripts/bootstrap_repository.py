#!/usr/bin/env python3
"""Render project identity into a repository created from this template."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path


PROFILE_METADATA = {
    "node-web": {
        "projectType": "web-application",
        "languages": ["JavaScript", "TypeScript", "HTML", "CSS"],
        "packageManagers": ["npm-or-approved-alternative"],
        "deployable": True,
        "producesArtifacts": True,
    },
    "node-service": {
        "projectType": "service",
        "languages": ["JavaScript", "TypeScript"],
        "packageManagers": ["npm-or-approved-alternative"],
        "deployable": True,
        "producesArtifacts": True,
    },
    "static-web": {
        "projectType": "web-application",
        "languages": ["HTML", "CSS", "JavaScript"],
        "packageManagers": [],
        "deployable": True,
        "producesArtifacts": True,
    },
    "python-service": {
        "projectType": "service",
        "languages": ["Python"],
        "packageManagers": ["select-during-stack-setup"],
        "deployable": True,
        "producesArtifacts": True,
    },
    "spring-service": {
        "projectType": "service",
        "languages": ["Java-or-Kotlin"],
        "packageManagers": ["Maven-or-Gradle"],
        "deployable": True,
        "producesArtifacts": True,
    },
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--org", required=True)
    parser.add_argument("--team", required=True)
    parser.add_argument("--backup-team", default="")
    parser.add_argument("--security-email", required=True)
    parser.add_argument("--support-url", required=True)
    parser.add_argument("--profile", choices=sorted(PROFILE_METADATA), required=True)
    parser.add_argument("--license", choices=("mit", "proprietary"), required=True)
    parser.add_argument("--license-holder", required=True)
    parser.add_argument("--visibility", choices=("private", "internal", "public"), default="private")
    parser.add_argument("--risk-tier", choices=("baseline", "moderate", "high"), default="baseline")
    parser.add_argument(
        "--data-classification",
        choices=("public", "internal", "confidential", "restricted"),
        default="internal",
    )
    parser.add_argument("--allow-dirty", action="store_true")
    return parser.parse_args(argv)


def validate_identifier(value: str, label: str) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", value):
        raise ValueError(f"{label} must contain only letters, digits, '.', '_' or '-'.")


def require_clean_tree(root: Path, allow_dirty: bool) -> None:
    if allow_dirty:
        return
    result = subprocess.run(
        ["git", "status", "--porcelain"], cwd=root, text=True, capture_output=True, check=False
    )
    if result.returncode != 0:
        raise RuntimeError("Run bootstrap inside a Git repository, or pass --allow-dirty for testing.")
    if result.stdout.strip():
        raise RuntimeError("Bootstrap requires a clean working tree. Commit or stash changes first.")


def replace_in_file(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8", newline="\n")


def render(text: str, values: dict[str, str]) -> str:
    for name, value in values.items():
        text = text.replace("{{" + name + "}}", value)
    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", text)))
    if unresolved:
        raise ValueError(f"Unresolved template values: {', '.join(unresolved)}")
    return text


def build_profile(base: dict, args: argparse.Namespace) -> dict:
    profile = json.loads(json.dumps(base))
    metadata = PROFILE_METADATA[args.profile]
    profile["template"]["isTemplate"] = False
    profile["project"].update(
        {
            "name": args.name,
            "description": args.description,
            "type": metadata["projectType"],
            "lifecycle": "bootstrapping",
            "visibility": args.visibility,
            "riskTier": args.risk_tier,
            "dataClassification": args.data_classification,
        }
    )
    profile["ownership"].update(
        {
            "primaryTeam": f"{args.org}/{args.team}",
            "backupTeam": f"{args.org}/{args.backup_team}" if args.backup_team else "",
            "securityContact": args.security_email,
            "supportUrl": args.support_url,
        }
    )
    stack_metadata = {key: value for key, value in metadata.items() if key != "projectType"}
    profile["stack"].update({"profile": args.profile, **stack_metadata})
    profile["legal"] = {
        "license": args.license,
        "licenseHolder": args.license_holder,
    }
    profile["verification"]["commands"] = []
    return profile


def bootstrap(root: Path, args: argparse.Namespace) -> None:
    validate_identifier(args.name, "name")
    validate_identifier(args.org, "org")
    validate_identifier(args.team, "team")
    if args.backup_team:
        validate_identifier(args.backup_team, "backup-team")
    if "@" not in args.security_email:
        raise ValueError("security-email must be an email address.")
    if not re.match(r"^https://", args.support_url):
        raise ValueError("support-url must use HTTPS.")

    require_clean_tree(root, args.allow_dirty)
    profile_path = root / "repository-profile.json"
    base_profile = json.loads(profile_path.read_text(encoding="utf-8"))
    if not base_profile.get("template", {}).get("isTemplate"):
        raise RuntimeError("This repository has already been bootstrapped.")

    year = str(dt.date.today().year)
    owner = f"{args.org}/{args.team}"
    replacements = {
        "YOUR-ORG/YOUR-TEAM": owner,
        "security@example.invalid": args.security_email,
        "https://example.invalid/support": args.support_url,
    }

    for relative in (
        ".github/CODEOWNERS",
        "MAINTAINERS.md",
        "SECURITY.md",
        "SUPPORT.md",
        "docs/THREAT_MODEL.md",
    ):
        replace_in_file(root / relative, replacements)

    readme_template = (root / ".template/README.project.md").read_text(encoding="utf-8")
    readme = render(
        readme_template,
        {
            "PROJECT_NAME": args.name,
            "PROJECT_DESCRIPTION": args.description,
            "ORG": args.org,
            "TEAM": args.team,
            "SUPPORT_URL": args.support_url,
        },
    )
    (root / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    license_name = "MIT.txt" if args.license == "mit" else "PROPRIETARY.txt"
    license_template = (root / ".template/licenses" / license_name).read_text(encoding="utf-8")
    license_text = render(
        license_template,
        {"YEAR": year, "LICENSE_HOLDER": args.license_holder},
    )
    (root / "LICENSE").write_text(license_text, encoding="utf-8", newline="\n")

    profile = build_profile(base_profile, args)
    profile_path.write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8", newline="\n")

    changelog = root / "CHANGELOG.md"
    replace_in_file(
        changelog,
        {
            "https://example.invalid/software-repository-template": (
                f"https://github.com/{args.org}/{args.name}"
            )
        },
    )

    print(f"Bootstrapped {args.name} with profile {args.profile}.")
    print("State: bootstrapping (intentional). Next:")
    print(f"  1. Follow profiles/{args.profile}.md and add the application scaffold.")
    print("  2. Complete architecture and threat-model documents.")
    print("  3. Record real verification commands in repository-profile.json.")
    print("  4. Apply and drill GitHub controls from docs/runbooks/github-configuration.md.")
    print("  5. Set project.lifecycle to active after every gate is real and green.")


def main(argv: list[str] | None = None) -> int:
    try:
        args = parse_args(argv)
        root = Path(__file__).resolve().parents[1]
        bootstrap(root, args)
        return 0
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"bootstrap failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
