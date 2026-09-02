# Spring service profile

## Required decisions

- Java/Kotlin and Spring Boot versions, Maven or Gradle, and wrapper policy.
- Public API compatibility, authentication/authorization, persistence, and migrations.
- JVM/container runtime, resource budgets, health checks, observability, and shutdown.
- Deployment, rollback, secret injection, and environment promotion.

## Baseline tooling

- Committed Maven or Gradle wrapper with verified distribution integrity.
- Compiler warnings/static analysis, formatter, JUnit 5, and JaCoCo.
- Spring integration tests and Testcontainers where real infrastructure behavior matters.
- ArchUnit for enforceable package/layer boundaries.
- Dependency and container scanning, SBOM, provenance, and immutable image digests.

Tests follow Maven/Gradle conventions; the stack-neutral template does not force a top-level
`tests/` directory for application tests.
