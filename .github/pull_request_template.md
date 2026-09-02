## Outcome

<!-- One sentence describing the user, operator, or developer outcome. -->

Closes #

## Why

<!-- Explain the problem and evidence, not just the patch. -->

## What changed

<!-- Keep this to one logical boundary. Link an ADR for durable structural decisions. -->

## Risk and rollout

- Risk level: low / medium / high
- Data, security, compatibility, migration, or operational impact:
- Rollout and rollback plan, or `not applicable`:

## Verification

Paste real, concise output. A check not run says **skipped** and why.

| Contract | Command or probe | Result |
|---|---|---|
| Repository policy | `python scripts/check_repository_policy.py` | |
| Policy tests | `python -m unittest discover -s tests -p "test_*.py"` | |
| Application lint/type checks | From `repository-profile.json` | |
| Application tests/coverage | From `repository-profile.json` | |
| Build/package | From `repository-profile.json` | |
| Integration, UI, migration, or deployment probe | Describe, or `not applicable` | |

## Review boundaries

- [ ] This does not change architecture, public contracts, authentication, sensitive data,
      dependencies, CI, deployment, infrastructure, ownership, or licensing; **or**
- [ ] The planned file list and approach were explicitly authorized before implementation.
- [ ] New direct dependencies were approved by a human other than the author, with purpose,
      alternatives, license, maintenance, transitive surface, install behavior, and cost recorded.
- [ ] Security and policy exceptions have an owner, approver, reason, compensating control, and
      expiry or review date.

## Documentation and operations

- [ ] User, operator, API, and architecture documentation is updated where behavior changed.
- [ ] Durable decisions have an ADR.
- [ ] Monitoring, runbooks, migration, and rollback instructions are updated where applicable.
- [ ] No secrets, production data, personal data, or restricted content were added to code,
      fixtures, logs, prompts, or artifacts.

## AI assistance

- Tools used, or `none`:
- [ ] Model/tool access complied with the project's data-classification policy.
- [ ] Generated code was reviewed for correctness, security, provenance, licensing, tests, and
      operational consequences exactly as human-written code would be.
- [ ] A human reviewer remains accountable for this change.
