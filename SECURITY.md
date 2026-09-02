# Security Policy

## Reporting a vulnerability

Report suspected vulnerabilities privately to **security@example.invalid**. Do not open a public
issue, paste sensitive evidence into an AI tool, or publish a proof of concept before the security
contact confirms a disclosure plan.

Include, when safe:

- affected version, branch, or commit;
- impact and prerequisites;
- minimal reproduction steps;
- relevant logs with secrets and personal data removed;
- a suggested remediation, if known.

The project will acknowledge a report within two business days, triage severity within five
business days, and coordinate remediation and disclosure based on risk. These targets must be
replaced if the owning organization uses a different incident-response SLA.

## Supported versions

Until the project defines a release model, only the protected default branch is supported. Update
this section before publishing a versioned artifact or operating a production service.

## Security model

The project-specific trust boundaries, assets, actors, abuse cases, and mitigations live in
`docs/THREAT_MODEL.md`. It must be completed before the project handles external input, credentials,
personal or regulated data, network traffic, or production deployment.

## Baseline controls

- Branch rulesets and required human review.
- Least-privilege GitHub Actions permissions.
- Full-SHA-pinned Actions and reusable workflows.
- Secret scanning and push protection where the GitHub plan supports them.
- Dependency graph, automated security updates, and ecosystem-specific vulnerability review.
- Code scanning for supported languages.
- Protected deployment environments and OIDC instead of long-lived cloud credentials.
- SBOM and build provenance for released artifacts where supported.
- Dated, owned, expiring risk exceptions.

Repository files document these controls; organization settings must enforce them. Follow
`docs/runbooks/github-configuration.md` when instantiating the repository.
