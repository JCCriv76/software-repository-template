# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## Status

This repository is in **bootstrapping** state. Complete the application profile, architecture,
threat model, GitHub settings, and verification contract before changing
`repository-profile.json.project.lifecycle` to `active`.

## Getting started

Add the exact environment setup and local run commands selected by the project. State runtime
version floors and package-manager requirements explicitly.

## How it works

Describe the core components and data flow. Keep detailed boundaries in
`docs/architecture/README.md` and durable decisions in `docs/adr/`.

## What is load-bearing

List the small number of constraints that shape distant behavior. Each should have an automated
check or explicit review boundary.

## Verification

The authoritative command list is `repository-profile.json.verification.commands`. Every pull
request also runs:

```bash
python scripts/check_repository_policy.py
python -m unittest discover -s tests -p "test_*.py"
```

## Project structure

Update this section after the selected profile creates application source and tests.

## Documentation

Start at `docs/README.md`.

## Ownership and support

- Primary owner: `{{ORG}}/{{TEAM}}`
- Support: {{SUPPORT_URL}}
- Security reports: follow `SECURITY.md`
