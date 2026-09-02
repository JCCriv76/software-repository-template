# Secure development standard

This baseline follows secure-development outcomes: prepare the organization, protect the software
and development environment, produce well-secured software, and respond to vulnerabilities.

## Design

- Classify data and complete the threat model before implementation crosses a new trust boundary.
- Default deny authentication, authorization, network access, and cloud permissions.
- Minimize data collection, privilege, retention, and exposed surface.
- Define abuse cases, failure behavior, logging, recovery, and deletion—not only the happy path.
- Require review for public contracts, auth, cryptography, secrets, migrations, and deployment.

## Implementation

- Validate at trust boundaries and encode output for its destination.
- Use maintained platform cryptography; do not design custom algorithms.
- Keep secrets in approved secret managers and use short-lived workload identity where possible.
- Prevent sensitive data from entering logs, telemetry, fixtures, crash reports, or model prompts.
- Keep dependencies locked, reviewed, scanned, and attributable.
- Use memory-safe and framework-safe APIs where practical.

## Build and delivery

- Pin Actions and reusable workflows to immutable commits.
- Give CI the minimum token permissions and isolate untrusted pull-request code.
- Protect deployment environments and use OIDC rather than stored cloud credentials.
- Scan source, dependencies, secrets, containers, and infrastructure according to project risk.
- Generate an SBOM and provenance for released artifacts where supported.
- Make rollback tested, documented, and independent of the failing release.

## Vulnerability response

Maintain private reporting, severity-based response targets, ownership, coordinated disclosure, and
post-incident root-cause work. Track exceptions with expiry and verify fixes with regression tests.
