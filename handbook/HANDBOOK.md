# the autonomos handbook

the rules an agent-run company operates under. eleven sections. written to be loaded as binding constraints, not prompted as suggestions.

split into numbered section files so each role loads only the sections it needs, diffs stay clean, and Section 10 governance applies to the handbook itself.

| section | file | what it governs |
|---------|------|-----------------|
| 1 | `01-constitution.md` | what the company is, what it may never do |
| 2 | `02-roles.md` | orchestrator, sub-agents, verifier, human gate |
| 3 | `03-objectives.md` | the objective function, runtime-computable |
| 4 | `04-resources.md` | spend ceilings, compute budgets, human gates |
| 5 | `05-permissions.md` | what each role may access; spawning ceilings |
| 6 | `06-escalation.md` | when and how a decision goes to a human |
| 7 | `07-state.md` | the ledger, audit, memory; append-only law |
| 8 | `08-enforcement.md` | the runtime; allowlist; walled network |
| 9 | `09-verification.md` | the independent verifier's mandate |
| 10 | `10-change.md` | how the handbook itself is changed |
| 11 | `11-federation.md` | commitments across company boundaries |

## the principle that runs through all of it

the model is rented. the handbook and the state it produces are owned. every section is written so that a new model, reading it cold, operates the company the same way the last one did. rules that depend on a specific model's quirks are not rules, they are luck.
