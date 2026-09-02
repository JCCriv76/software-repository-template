# Python service profile

## Required decisions

- Supported Python version and packaging tool.
- Application framework, process model, interfaces, and compatibility policy.
- Database/migrations, authentication, secrets, retention, and background jobs.
- Deployment artifact and runtime ownership.

## Baseline tooling

- `pyproject.toml` as the central project configuration.
- A locked, hash-verifiable dependency workflow approved by the organization.
- Ruff or equivalent lint/format, a type checker, pytest, and coverage.
- Integration tests using disposable services or isolated test resources.
- Dependency vulnerability/license review, SBOM, and provenance for artifacts.

Record exact commands in `repository-profile.json`; do not make Node a policy dependency for a
Python-only project.
