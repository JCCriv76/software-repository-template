# Architecture

This file describes the architecture that exists now. Replace this template before application code
is merged.

## System purpose

State the user or organizational outcome, primary actors, and what this system explicitly does not
do.

## Context and trust boundaries

Describe upstream callers, users, external services, data stores, deployment environments, and
administrative systems. Link to `../THREAT_MODEL.md` rather than duplicating security analysis.

## Components

| Component | Responsibility | Interface | Owner |
|---|---|---|---|
| _To be defined_ | | | |

## Data flow

Describe where data originates, how it is validated, transformed, stored, transmitted, logged, and
deleted. Name authoritative data sources and derived representations.

## Load-bearing constraints

List only constraints whose violation causes distant or expensive failures. For each, name the
automated check or review boundary that enforces it.

## Dependency direction

Document allowed component-to-component dependencies. Prefer a small number of explicit boundaries
that can be tested with the language's native architecture tooling.

## Deployment and operations

Link environments, release flow, rollback, observability, ownership, RTO/RPO, and incident runbooks.

## Known debt and exceptions

Link tracked issues and dated exceptions. Do not hide known risk in prose without an owner and
review date.
