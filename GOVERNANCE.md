# Governance

## Decision ownership

The primary owning team in `repository-profile.json` is accountable for maintenance, security,
availability, and lifecycle decisions. A backup team should be assigned for production or
business-critical systems.

| Decision | Required authority |
|---|---|
| Routine implementation | Maintainer review under branch rules |
| New dependency | Human maintainer other than the author |
| Public API or architecture boundary | Owning-team maintainer |
| Authentication, secrets, sensitive data, or cryptography | Owning team and security reviewer |
| Production deployment or rollback | Protected-environment approver |
| License or third-party terms | Authorized legal or organizational owner |
| Repository archive or transfer | Organization owner and owning team |

AI agents may research, implement, test, or review within their granted scope. They are never the
required approving authority.

## Decision records

Durable technical decisions use ADRs under `docs/adr/`. An ADR records context, options, decision,
consequences, owner, date, and supersession status. Issue comments may link to an ADR but do not
replace it.

## Exceptions

Policy or security exceptions must state the control, owner, business reason, compensating control,
approver, creation date, expiry or review date, and removal issue. Expired exceptions fail closed.

## Lifecycle

Every repository must document how it is supported, released, monitored, and eventually archived.
An unowned repository must not remain a production dependency.
