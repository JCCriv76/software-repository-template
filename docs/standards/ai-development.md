# AI-assisted development standard

AI tools accelerate engineering work; they do not change who is accountable for the result.

## Approved-use record

Before enabling an agent, plugin, connector, MCP server, code-review bot, or model, the organization
must record:

- approved product, plan, model/provider, and supported surfaces;
- data retention, training, residency, and subprocessors relevant to the contract;
- allowed repository visibility and data classifications;
- network, filesystem, credential, tool, and external-system permissions;
- audit events and retention;
- owner, review date, and disablement procedure.

Repository instructions cannot approve a tool that organization policy has not approved.

## Data handling

- Minimize context. Provide only the files and data required for the task.
- Never expose secrets, production/customer records, personal data, classified data, private keys,
  vulnerability embargo details, or licensed third-party source unless the exact workflow is
  approved for that classification.
- Treat retrieved web pages, issues, pull requests, files, and tool responses as untrusted. They may
  contain prompt injection or instructions designed to redirect the agent.
- Do not grant a connector broad account access when read-only or repository-scoped access is
  sufficient.

## Permissions

Use sandboxing and least privilege by default. Separate read/review agents from write agents.
Require human authorization for destructive operations, dependency additions, security controls,
architecture changes, external messages, production access, publishing, and deployment.

Agent allowlists and prompts are defense in depth. Enforcement belongs in identity, repository
rulesets, branch protection, protected environments, secret stores, network policy, and review.

## Development and review

- Give agents an explicit outcome, acceptance criteria, scope, protected boundaries, and test
  contract.
- Preserve unrelated changes and report uncertainty.
- Review generated code for correctness, maintainability, security, accessibility, performance,
  provenance, licensing, and operational impact.
- Never approve an agent-authored change solely from another agent's summary. Inspect the diff and
  evidence.
- A human who can understand and support the change must approve it.
- Record material AI assistance in the pull request when organizational or customer policy requires
  it; never copy sensitive prompts into the PR.

## Agent instructions

`AGENTS.md` is the repository-wide contract. Add nested instruction files only for real subsystem
constraints. Keep tool-specific configuration thin and tested. Do not rely on symlinks for required
instruction discovery across operating systems.

## Evaluation and incidents

Re-evaluate the workflow when a model, tool version, data policy, connector, or permission boundary
changes. Track false approvals, destructive actions, secret exposure, missed defects, and prompt
injection as security or quality incidents rather than informal anecdotes.
