# state/ - the owned-state layer

this is the asset. everything else in the repo is replaceable. this is not.

when the model running your agents is deprecated next year, you do not lose the company. you point a new model at `state/`, and it inherits every rule, every prior decision, and the reasons behind them. it picks up cold and keeps going. that continuity is what you own.

## what lives here

| path | what it is | mutability |
|------|-----------|------------|
| `ledger/` | the append-only rationale ledger. every decision and why it was made. | append-only |
| `audit.log` | append-only event stream. what happened, when, under which rule. | append-only |
| `memory/` | working memory the agent reads and writes during operation. | read/write |

## the ledger is not a log

a log records what happened. the ledger records **why a decision was the right one given the rules at the time**. that distinction is the whole product.

- a log says: "agent spent 40 EUR on compute at 14:03."
- the ledger says: "agent approved 40 EUR compute spend under Handbook 4.2 because projected risk-reduction exceeded the threshold; human gate not required because amount was below the 50 EUR ceiling in effect at decision time."

the second one survives a model swap. the new model reads it and understands not just the state of the world but the reasoning standard the company operates by. that is inheritance, not logging.

## append-only is load-bearing

the ledger and audit log are append-only by design, not by convention.

- an agent cannot rewrite its own history to make a past decision look better
- the verifier (see `verifier/`) can replay the full decision history independently
- a model swap cannot quietly drop inconvenient prior reasoning

if an entry is wrong, you append a correction that references the original. you never edit in place. the enforcement runtime treats in-place edits to ledger files as a violation.

## portability is the test

the ledger format is plain, model-agnostic, and adapter-independent. the same `ledger/` directory must be readable and writable by the claude-code adapter, the openrouter adapter, and the ollama adapter without modification. if a format change breaks that, the change is wrong, not the adapters.

see `ledger/SCHEMA.md` for the entry format.
