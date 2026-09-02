# Stack profiles

Profiles add application conventions after the repository baseline is owned and configured. They
are guides rather than copied dependency manifests so a new repository can select current,
organization-approved tool versions at creation time.

| Profile | Use when | Guide |
|---|---|---|
| `node-web` | Browser applications using Vue, React, Angular, or another Node-built frontend | `node-web.md` |
| `node-service` | Node.js APIs, workers, or backend-for-frontend services | `node-service.md` |
| `static-web` | HTML/CSS/JavaScript without a package-manager requirement | `static-web.md` |
| `python-service` | Python APIs, workers, jobs, or libraries | `python-service.md` |
| `spring-service` | Java/Kotlin Spring Boot services | `spring-service.md` |

Every profile must define locked dependencies, lint/format, static analysis, unit tests, coverage,
build/package, integration tests, vulnerability scanning, and real verification commands. It may
add nested `AGENTS.md` files only after stable subsystem constraints exist.
