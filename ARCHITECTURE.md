# Architecture overview

Owner → Intelligence → directions → departments → agents.

This is a role diagram, not a count of running workers. Existing contracts feed a
shared owner read-model: tasks, decisions, costs, content and learning. Deterministic
rules keep unknown/estimated values distinct from observed records.

Request → analysis → plan → commercial draft → owner gate is preparation, not sale.
Idea → brief → production → review → publication package → manual results → learning
requires evidence at every transition; approval is never publication.

The local implementation has an explicitly known cross-store non-atomic boundary:
a failure between linked records may require reconciliation; do not imply a global
transaction or production recovery guarantee. Private implementation details excluded.

## Head Manager boundary

The local private implementation projects bounded evidence from existing owner
contracts into an advisory management summary. Deterministic rules are the
fallback; optional bounded model selection can only select existing evidence
references and actions. It cannot grant owner approval or execute external work.
Unknown coverage remains unknown, and suggestions are not authorizations.
Head Manager runtime, Telegram integration and cockpit components are NOT shipped
in this snapshot. No active production OpenAI/ChatGPT integration is claimed.
The offline replay demonstrates contract boundaries, not live Head Manager logic.
