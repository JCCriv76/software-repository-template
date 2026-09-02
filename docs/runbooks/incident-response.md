# Incident-response runbook

This is a coordination skeleton, not a substitute for the organization's incident process.

## Declare and contain

1. Open the approved private incident channel and assign incident commander, technical lead,
   communications lead, and scribe.
2. Record detection time, affected systems, suspected impact, current evidence, and data
   classification.
3. Preserve evidence. Do not paste secrets, customer data, or embargoed vulnerability details into
   public issues or unapproved AI tools.
4. Revoke or rotate exposed credentials, isolate affected paths, pause deployments, or roll back as
   risk requires.
5. Notify legal, privacy, security, customers, or regulators through approved escalation paths.

## Investigate and recover

- Build a timestamped timeline and distinguish facts from hypotheses.
- Identify affected commits, artifacts, dependencies, identities, environments, and data.
- Validate remediation in an isolated environment.
- Restore service from a known-good, attributable artifact.
- Monitor for recurrence and confirm containment before standing down.

## Follow-up

Create owned actions for root cause, missing detection, control failures, documentation, tests, and
recovery improvements. Update the threat model and runbooks. Avoid attributing system failures to a
single human action when process or control design allowed the outcome.
