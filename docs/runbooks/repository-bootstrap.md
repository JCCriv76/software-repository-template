# Repository bootstrap runbook

This runbook turns a repository copied from the template into an owned project. Template creation
does not carry GitHub rulesets, teams, labels, environments, variables, secrets, or security
configuration; apply those separately.

## 1. Collect decisions

Before running bootstrap, identify:

- repository name and plain-language purpose;
- primary and backup owning teams;
- private security contact and normal support URL;
- approved license and license holder;
- project type and stack profile;
- visibility, risk tier, and highest data classification;
- release model, artifact type, deployment target, and environments;
- required verification commands and supported developer operating systems;
- approved AI tools, connectors, and data boundary.

## 2. Render project metadata

Run from the repository root:

```bash
python scripts/bootstrap_repository.py \
  --name example-service \
  --description "What the service does." \
  --org YOUR-ORG \
  --team YOUR-TEAM \
  --security-email security@example.com \
  --support-url https://example.com/support \
  --profile node-service \
  --license proprietary \
  --license-holder "Example Organization"
```

This sets the repository to `bootstrapping`, replaces ownership/contact/license placeholders, and
creates a project README. Review every generated value; the script cannot make legal, security, or
ownership decisions.

## 3. Add the application profile

Follow the selected guide in `profiles/`. Add runtime files, a lockfile, formatter/linter, tests,
build/package command, and a thin CI caller. Record the real commands in
`repository-profile.json.verification.commands`.

When the application scaffold and CI are green, change `project.type`, stack and delivery fields as
needed and set `template.isTemplate` to `false` with the project in an active state.

## 4. Complete project documents

- Replace `docs/architecture/README.md` template sections.
- Complete `docs/THREAT_MODEL.md` before external input, credentials, sensitive data, networking,
  or production deployment.
- Create ADR-0001 for the stack and deployment decision.
- Set supported versions and response targets in `SECURITY.md`.
- Assign the backup owner for production or business-critical systems.
- Remove template-only profile guides if the team does not want to retain them.

## 5. Configure GitHub

Follow `github-configuration.md`. Create required labels, apply organization rulesets and security
configuration, restrict Actions, configure environments, and test that controls block prohibited
operations.

## 6. Verify

```bash
python scripts/check_repository_policy.py
python -m unittest discover -s tests -p "test_*.py"
```

Then run every application command in `repository-profile.json`. Open the first pull request only
after policy, ownership, security contact, license, and required checks are real.
