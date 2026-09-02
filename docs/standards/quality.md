# Quality standard

## Verification contract

`repository-profile.json` lists the project-specific commands for linting, types/static analysis,
tests, coverage, build/package, and integration checks. CI and contributors use that same list; do
not maintain competing command lists in several files.

Every repository also runs:

```bash
python scripts/check_repository_policy.py
python -m unittest discover -s tests -p "test_*.py"
```

## Baselines

Set a numeric threshold only after measuring representative code. Record the metric, tool/version,
date, commit, scope, exclusions, owner, and rationale. A floor may tighten as quality improves; a
reduction requires an explicit, time-bound exception rather than a silent config edit.

Coverage is evidence, not the objective. Risky authorization, parsing, money movement, migrations,
and destructive operations may require complete scenario coverage even when the repository-wide
percentage is lower.

## Test layers

Choose layers proportional to the system:

- unit tests for pure behavior;
- component or contract tests at interfaces;
- integration tests for real storage, queues, APIs, and framework wiring;
- end-to-end tests for critical user or operator journeys;
- architecture/guard tests for dependency direction and forbidden behavior;
- manual or automated accessibility, visual, migration, performance, and disaster-recovery probes
  where applicable.

Golden files and snapshots require intentional review. Regenerating them to make a failure disappear
is not verification.

## CI design

- Use stable, clearly named required checks.
- Keep blocking and advisory checks visibly distinct.
- Pin workflow dependencies and grant minimal permissions.
- Cancel superseded pull-request runs where safe.
- Run untrusted pull-request code without production secrets or deployment authority.
- A documented check that is not executed is a defect.
