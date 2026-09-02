# Threat model

- Status: incomplete template
- Owner: `YOUR-ORG/YOUR-TEAM`
- Last reviewed: YYYY-MM-DD
- Next review: YYYY-MM-DD

Complete this document before the project accepts external input, handles credentials or sensitive
data, exposes a network service, or deploys to production.

## Scope

Define the system, environments, users, dependencies, administrative surfaces, and exclusions.

## Assets

| Asset | Sensitivity | Integrity/availability need | Owner |
|---|---|---|---|
| _To be defined_ | | | |

## Actors

Include ordinary users, administrators, operators, service identities, third parties, and plausible
attackers. State what each is allowed to do.

## Trust boundaries and data flow

For every boundary, record authentication, authorization, encryption, validation, logging,
retention, and failure behavior. Link an architecture diagram when one exists.

## Abuse cases

| ID | Scenario | Impact | Existing controls | Residual risk | Owner |
|---|---|---|---|---|---|
| TM-001 | _To be defined_ | | | | |

Consider at minimum: broken authorization, injection, unsafe file handling, secret disclosure,
supply-chain compromise, CI workflow abuse, dependency confusion, data exfiltration, denial of
service, insecure defaults, privileged insider action, prompt injection, and compromised connected
AI tools.

## Assumptions and accepted risks

Assumptions must be testable. Accepted risks require the exception fields defined in
`GOVERNANCE.md`.

## Verification and review triggers

Review after authentication, public API, data classification, dependency trust, deployment,
external integration, or AI-tool access changes, and after every relevant incident.
