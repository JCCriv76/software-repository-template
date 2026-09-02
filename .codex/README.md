# Codex project configuration

Codex reads the root `AGENTS.md` directly and can layer additional `AGENTS.md` files closer to
specialized code. That native mechanism is the project contract.

Do not add experimental command rules, hooks, agents, skills, or permission profiles here merely
because another repository has them. Add tool-specific configuration only after it is:

1. required by a recurring project workflow;
2. tested on every Codex surface the team supports;
3. narrower than the repository and organization security policy;
4. covered by a smoke test or conformance check;
5. assigned an owner and update process.

Agent configuration is defense in depth, not an enforcement substitute for sandboxing, GitHub
rulesets, protected environments, secret management, or human review.
