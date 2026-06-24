# contributing to autonomos

contributions are governed by the handbook's own Section 10 (change management). the project eats its own dog food: the rules for changing autonomos are the same kind of rules autonomos asks agents to operate under.

## the rule

every change to the handbook, the ledger format, or the enforcement runtime must:

1. open as a pull request, never a direct push to main
2. state the rationale in the PR description, not just the diff
3. land an entry in `state/ledger/` describing why the change was made, not only what changed

the rationale requirement is not bureaucracy. it is the same discipline the ledger imposes on agents: a decision without a recorded reason is not a decision, it is an accident waiting to be repeated.

## scope of changes

- **handbook/** changes are spec changes. they affect every adapter. treat them as breaking until proven otherwise.
- **state/ledger/** format changes are the most sensitive in the repo. the ledger is the owned asset. a format change that breaks portability defeats the entire thesis. these need two reviewers.
- **adapters/** changes are local. a fix to the ollama adapter should never require touching the handbook.
- **enforcement/** changes are tested against the walled-network setup before merge.

## what not to do

- do not add model-specific assumptions to `handbook/` or `state/`. those layers are model-agnostic by definition.
- do not introduce language of walls, breaking, prisons, or cages. the framing is rules that hold, reliability, trust, and brakes.
