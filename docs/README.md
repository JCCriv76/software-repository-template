# Documentation index

Every durable document belongs in this index. Add the row in the same pull request that creates the
document.

| Document | Purpose | Owner/review cadence |
|---|---|---|
| `architecture/README.md` | Current system boundaries and load-bearing constraints | Owning team; each structural change |
| `adr/README.md` | ADR lifecycle and index | Owning team; each ADR |
| `THREAT_MODEL.md` | Assets, trust boundaries, abuse cases, and controls | Security owner; at least annually and after boundary changes |
| `runbooks/repository-bootstrap.md` | Instantiate this template safely | Platform owner; each template release |
| `runbooks/github-configuration.md` | Apply and verify GitHub settings not copied by the template | Platform/security owner; quarterly |
| `runbooks/release.md` | Select and operate a release model | Owning team; each release-process change |
| `runbooks/incident-response.md` | Triage and coordinate production/security incidents | Owning team; after each incident exercise |
| `standards/ai-development.md` | AI tool, data, approval, and review boundaries | Security/platform owner; quarterly |
| `standards/dependency-management.md` | Dependency admission, updates, exceptions, and provenance | Security/platform owner; quarterly |
| `standards/quality.md` | Verification contract, risk tiers, and baselines | Owning team; each gate change |
| `standards/secure-development.md` | Secure SDLC baseline | Security owner; at least annually |
