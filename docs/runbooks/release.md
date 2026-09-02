# Release runbook

The template has no release model. Select one in `repository-profile.json` before publishing an
artifact or deploying a service.

## Required release properties

- Version source and compatibility policy.
- Trigger: immutable tag, protected branch, or approved promotion.
- Artifact identity and retention.
- Changelog or release-note mechanism.
- Required test, security, and approval gates.
- SBOM and provenance requirements.
- Signing or attestation verification.
- Deployment environment and workload identity.
- Rollback, migration compatibility, and recovery owner.
- End-of-life and vulnerability-support policy.

## Safe sequence

1. Build once in a trusted workflow after all merge gates pass.
2. Identify the artifact by commit and immutable digest.
3. Generate checksums, SBOM, and provenance as appropriate.
4. Promote the same artifact between environments; do not rebuild for production.
5. Require protected-environment approval for production.
6. Verify health and security signals, then record the release.
7. Roll back using the documented path if acceptance signals fail.

Never publish from an unreviewed developer workstation or expose a long-lived cloud credential to
pull-request code.
