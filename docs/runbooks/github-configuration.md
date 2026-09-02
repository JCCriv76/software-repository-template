# GitHub configuration runbook

Repository files are not enforcement by themselves. Prefer organization-managed settings or
infrastructure as code so controls remain consistent and auditable.

## Organization controls

Apply, according to the GitHub plan:

- organization rulesets targeting the repository's default branch;
- a security configuration enabling dependency graph, Dependabot alerts and security updates,
  secret scanning, push protection, and CodeQL default setup where available;
- an Actions policy allowing only GitHub-owned and explicitly approved full-SHA-pinned actions;
- two-factor authentication or enterprise identity requirements;
- least-privilege base repository permissions and team access;
- custom properties for owner, risk tier, data classification, lifecycle, and deployment status.

## Default-branch ruleset

Recommended baseline for `main`:

- block deletion and force push;
- require a pull request;
- require at least one approval and Code Owner review;
- dismiss stale approvals after new commits;
- require conversation resolution;
- require required status checks and an up-to-date branch or merge queue;
- prevent direct pushes except a narrowly controlled break-glass role;
- require signed commits when the organization can operate the exception process reliably;
- restrict bypass to named emergency actors and audit every use.

Use stable job names. A required check whose workflow was renamed can become an unavailable or
detached control.

## Repository settings

- Set `main` as default.
- Allow only approved merge methods; squash merge is a reasonable default for short-lived branches.
- Delete head branches after merge.
- Disable unused features and unnecessary Actions permissions.
- Set the workflow token to read-only by default.
- Create labels: `security`, `dependencies-approved`, `architecture-approved`, `breaking-change`,
  `risk-high`, `bug`, `enhancement`, and `task`.
- Assign real CODEOWNERS teams and confirm they have repository access.

## Environments and deployments

For each deployment environment:

- require explicit production approval;
- scope secrets and variables to the narrowest environment;
- prefer OIDC/workload identity over long-lived credentials;
- restrict deployment branches or tags;
- record the deployment URL and rollback procedure;
- separate build provenance from deployment authority.

## Verification drills

Before declaring setup complete, prove:

1. A pull request with a failing required check cannot merge.
2. Direct and force pushes to `main` are rejected.
3. A new commit dismisses an existing approval.
4. A fake secret is blocked by push protection in an approved test procedure.
5. An unpinned Action reference fails repository policy.
6. Pull-request code cannot access production secrets or deploy.
7. A production deployment pauses for its required reviewer.
8. Security alerts route to an owned team.

Record the date and operator. Repeat after material ruleset, workflow, plan, or organization-policy
changes.
