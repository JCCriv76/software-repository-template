# Software Repository Template

A hardened, stack-neutral starting point for organization software repositories. It provides
repository governance, GitHub automation, security policy, AI-agent instructions, architectural
decision records, and an enforceable repository-policy check without committing the project to a
frontend or backend framework.

This repository intentionally contains no application dependencies. Select a profile only after a
new repository has been created from the template.

## Create a project from this template

1. Mark this repository as a GitHub template.
2. Create a new repository from its default branch only.
3. Clone the new repository.
4. Run the bootstrap command below, replacing every example value:

   ```bash
   python scripts/bootstrap_repository.py \
     --name example-service \
     --description "What the service does." \
     --org YOUR-ORG \
     --team YOUR-TEAM \
     --security-email security@example.com \
     --support-url https://example.com/support \
     --profile node-web \
     --license proprietary \
     --license-holder "Example Organization"
   ```

5. Follow the generated checklist in `docs/runbooks/repository-bootstrap.md`.
6. Apply organization rulesets and security settings before the first production change.
7. Add the chosen stack through a setup pull request; do not mix application behavior into the
   repository-initialization commit.

Until bootstrap is complete, CI deliberately reports a failure in repositories whose name differs
from this template's name.

## Design principles

- **Policy is stack-neutral.** Node, Python, Java, and static-web details live in profiles.
- **Settings are a separate control plane.** GitHub templates copy files, not the organization
  rulesets, security configuration, teams, environments, or secrets that enforce them.
- **Checks must bite.** A documented control that is not executed is treated as a defect.
- **One source for each contract.** CI calls the repository's verification contract rather than
  reproducing command lists in several documents.
- **Human accountability remains.** AI tools may assist, but cannot approve their own dependency,
  security, architecture, or deployment changes.
- **Controls scale by risk.** The baseline is mandatory; internet-facing, sensitive-data, and
  released-artifact projects add stronger profiles.

## Repository contents

| Path | Purpose |
|---|---|
| `AGENTS.md` | Tool-neutral instructions for humans and AI coding agents |
| `.github/` | Issue forms, PR template, Dependabot, CODEOWNERS, and policy CI |
| `docs/` | Architecture, ADRs, standards, threat model, and operating runbooks |
| `profiles/` | Guidance for adding Node/Vue, Node services, Python, Spring, or static HTML |
| `scripts/` | Dependency-free bootstrap and repository-policy checks |
| `tests/` | Tests for the policy checker and bootstrap metadata |
| `repository-profile.json` | Machine-readable ownership, risk, stack, and delivery decisions |

## What the template does not decide

The new repository owner must choose its license, real owning team, security contact, runtime,
deployment target, data classification, verification commands, and release model. Placeholder
values are allowed only while this repository remains the template.

## Where to read next

| Need | Document |
|---|---|
| Instantiate the template | `docs/runbooks/repository-bootstrap.md` |
| Apply GitHub controls | `docs/runbooks/github-configuration.md` |
| Understand AI boundaries | `docs/standards/ai-development.md` |
| Define secure development | `docs/standards/secure-development.md` |
| Set quality gates | `docs/standards/quality.md` |
| Choose a stack | `profiles/README.md` |
