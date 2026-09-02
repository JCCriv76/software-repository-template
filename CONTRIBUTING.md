# Contributing

Thank you for improving this project. `AGENTS.md` is the complete working agreement; this document
summarizes the human contribution flow.

## Before work begins

1. Start from an issue with a clear problem statement and acceptance criteria.
2. Search open and recently closed work for overlap or rejected approaches.
3. Branch from the protected default branch using `<type>/<issue>-<short-description>`, such as
   `feature/123-export-report` or `fix/456-null-owner`.
4. For architecture, security, data, CI, dependency, or deployment changes, obtain the approval
   required by `AGENTS.md` before editing.

## Development

- Keep pull requests focused on one logical outcome.
- Add tests at the same boundary as the behavior being changed.
- Preserve unrelated working-tree changes.
- Regenerate dependency lockfiles with the package manager.
- Do not introduce secrets or production data into fixtures.
- Record durable design decisions in `docs/adr/`.

## Verification

Run the stack-neutral repository checks:

```bash
python scripts/check_repository_policy.py
python -m unittest discover -s tests -p "test_*.py"
```

Then run every application command listed under `verification.commands` in
`repository-profile.json`. Paste concise, real results into the pull request. Mark anything not run
as `skipped` with the reason.

## Commits and pull requests

Commits should be atomic logical changes—not artificially split by file. Use Conventional Commit
types where practical: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `perf`, and `chore`.

The pull request must explain the problem, the change, risk, testing, rollout or migration needs,
and any AI assistance. A human reviewer remains accountable for the merged result.

## Dependencies

A new direct dependency requires approval from a human reviewer other than the author. Document its
purpose, alternatives considered, license, maintenance health, transitive and install-script
surface, and effect on runtime or artifact size.

## Security reports

Do not disclose a vulnerability in a public issue. Follow `SECURITY.md`.
