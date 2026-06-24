# the brain transplant

**hook:** swap the model running a live agent mid-operation. the company does not notice.

## the setup

- a running autonomos company doing real work (issue triage, spend decisions, commitments)
- it has been running on claude-opus-4-8, writing decisions to the ledger
- mid-stream, swap to gpt-5-2 via the openrouter adapter
- the handbook does not change. the ledger does not reset. nothing is re-prompted by hand.

## what the viewer sees

1. opus makes decisions, each one landing in the ledger with its rule and rationale
2. the swap happens (one model string changes)
3. gpt reads the ledger cold, inherits the reasoning standard, and continues
4. the verifier replays the whole history and confirms: same handbook, two models, full continuity

## why it lands

the obvious expectation is that swapping the brain breaks the company. it does not, because the company was never in the model. it was in the state. that inversion is the entire pitch in fifteen seconds.

## the seam is in the data

`state/ledger/ledger.jsonl` already shows it: led_0001 on opus, led_0004 on gpt, same rule 4.2, continuous chain. run `verifier/verify.py` to see the seam confirmed independently.
