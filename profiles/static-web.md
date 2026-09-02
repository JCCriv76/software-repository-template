# Static web profile

Use this for projects that can remain HTML, CSS, and browser JavaScript without a Node build.

## Baseline

- Standards-valid markup and accessible keyboard, focus, contrast, and semantics behavior.
- CSP and other response headers appropriate to the hosting platform.
- No secrets or privileged credentials in client code.
- Browser tests for critical journeys and at least one no-script/degraded-behavior decision.
- Asset size and third-party origin budgets.
- An explicit supported-browser matrix.

Adding Node solely for linting or bundling is a dependency decision, not an automatic consequence of
having frontend code. Document the value and maintenance cost first.
