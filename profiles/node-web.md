# Node web profile

Supports Vue, React, Angular, or another browser framework without making one universal.

## Required decisions

- Framework and rendering model: SPA, SSR, SSG, or library.
- Node major version and package manager; pin both in developer and CI configuration.
- Browser support, accessibility target, localization, and performance budgets.
- API boundary, authentication model, client-visible configuration, and CSP.
- Deployment target and whether artifacts are static or server-executed.

## Baseline tooling

- Framework-supported project generator using a reviewed, recorded version.
- Lockfile installation (`npm ci`, `pnpm --frozen-lockfile`, or equivalent).
- ESLint or framework linter, formatter, and TypeScript where appropriate.
- Vitest/Jest and DOM testing library; Playwright for critical browser journeys.
- Dependency audit and bundle/artifact-size reporting.
- Source maps and telemetry reviewed for data exposure before production.

## Verification contract example

Record the project's actual equivalents in `repository-profile.json`:

```text
npm run lint
npm run typecheck
npm test
npm run test:coverage
npm run build
npm run test:e2e
```

Do not copy these names unless the generated package actually defines them. CI should install from
the lockfile and use the same commands contributors run locally.
