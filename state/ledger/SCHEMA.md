# ledger schema

the rationale ledger is an append-only sequence of JSON-lines entries. one decision per line. plain JSON, no model-specific fields, readable by any adapter.

## why JSON-lines

- append is a single line write, atomic enough for the enforcement runtime to guarantee
- a corrupt tail line never destroys prior history
- diffs are clean for the Section 10 governance story
- any language, any model, any tool can parse it without a dependency

## entry format

```json
{
  "id": "led_0001",
  "ts": "2026-06-24T14:03:00Z",
  "actor": "orchestrator",
  "model": "claude-opus-4-8",
  "decision": "approve_compute_spend",
  "inputs": { "amount_eur": 40, "purpose": "risk reduction batch" },
  "rule": "handbook/HANDBOOK.md#4-resources",
  "rationale": "projected risk reduction exceeded threshold; below 50 EUR human-gate ceiling in effect at decision time",
  "gate": { "required": false, "reason": "below ceiling" },
  "prev": "led_0000",
  "hash": "sha256:..."
}
```

## fields

| field | meaning |
|-------|---------|
| `id` | monotonic, unique. references in `prev` and corrections point to it. |
| `ts` | ISO 8601, UTC. decision time, not write time if they differ. |
| `actor` | which role made the call: orchestrator, sub-agent, verifier, human. |
| `model` | which model was running at decision time. **records the rental, does not bind the state to it.** |
| `decision` | machine-stable verb. the kind of decision, not free text. |
| `inputs` | the facts the decision was made on. |
| `rule` | exact handbook section the decision was made under. links rationale to law. |
| `rationale` | why this was correct given the rule. the part a new model inherits. |
| `gate` | whether a human gate was required and why or why not. |
| `prev` | id of the previous entry. forms the chain. |
| `hash` | sha256 over the canonical entry plus `prev` hash. tamper-evidence. |

## corrections

never edit a past entry. append a correction:

```json
{
  "id": "led_0042",
  "ts": "2026-06-25T09:00:00Z",
  "actor": "human",
  "decision": "correct_entry",
  "corrects": "led_0007",
  "rationale": "original spend was misclassified; reclassifying does not change the approval, only the category",
  "prev": "led_0041",
  "hash": "sha256:..."
}
```

the original stays. the chain stays intact. the correction is itself a recorded, reasoned decision.

## the model field is the thesis in one line

every entry records which model made the call, and nothing in the format depends on that value. read the field and you can see exactly where one model handed off to another, with full continuity of reasoning across the seam. that seam is the brain-transplant showcase. the ledger is what makes it boring instead of catastrophic.
