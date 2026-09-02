# Node service profile

## Required decisions

- Supported Node major and package manager.
- HTTP, queue, scheduled-job, or worker interfaces and compatibility policy.
- Authentication/authorization, secret store, database, migrations, and retention.
- Runtime platform, health checks, observability, scaling, and shutdown behavior.
- Container, serverless, or process artifact and rollback model.

## Baseline tooling

- TypeScript for service contracts where practical.
- Lint, format, type checking, unit and contract tests.
- Integration tests against real disposable dependencies or test containers.
- Schema/migration compatibility checks.
- Dependency audit, container scan when applicable, SBOM, and provenance.
- Structured logs with explicit sensitive-field redaction.

Example verification categories: lint, typecheck, unit tests, coverage, integration tests, build,
migration validation, and a health/readiness probe.
