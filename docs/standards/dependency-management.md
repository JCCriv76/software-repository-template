# Dependency management standard

## Admission

A new direct dependency requires approval from a human other than the author. Record:

- required capability and alternatives considered;
- owner, upstream source, release cadence, and maintenance signals;
- license and organization-policy compatibility;
- direct and transitive dependency surface;
- install/build hooks and native binaries;
- known vulnerabilities and security posture;
- runtime, artifact-size, startup, and operational cost;
- removal or replacement strategy.

Prefer platform or standard-library capabilities when they are adequate. Do not adopt two libraries
for the same purpose without an explicit decision.

## Integrity and updates

- Commit the ecosystem's lockfile and regenerate it with the package manager.
- Use trusted registries and prevent dependency confusion with explicit scopes/namespaces.
- Automate version and security updates for every ecosystem in `.github/dependabot.yml` or the
  organization-approved equivalent.
- Review dependency-update tests and release notes; automation does not make an update trustworthy.
- Pin CI actions and reusable workflows to full commit SHAs and keep the release name in a comment.
- Inventory vendored or locally referenced packages separately because normal audit tools may not
  see them.

## Exceptions and removal

Vulnerability, license, staleness, or provenance exceptions require an owner, approver, business
reason, compensating control, creation date, and expiry/review date. Revalidate the upstream facts
at every review. Remove stale packages and expired exceptions promptly.

Released artifacts should produce an SBOM and provenance attestation when the hosting plan and
artifact type support them.
