# verifier/ - the independent audit role

the orchestrator decides. the verifier checks that it decided within the rules. the point of the role is independence: the verifier does not use the orchestrator's own evaluation criteria, because an orchestrator that grades itself is unverified by definition.

## what it does

- replays `state/ledger/ledger.jsonl` from genesis, independently
- for each entry, checks the cited `rule` actually permits the `decision` given the `inputs`
- confirms every required human gate was actually taken
- verifies the hash chain is intact and no entry was edited in place
- flags any decision where the rationale does not follow from the rule

## what it must never do

- it must not share an eval suite with the orchestrator
- it must not be the same model instance as the orchestrator
- it must not be able to write to the ledger except to append its own verification entries

## why it owns its own criteria

a self-referential eval suite is the most common way a governance story quietly fails: the agent passes its own tests because it wrote them. the verifier's mandate is to hold criteria the orchestrator does not control. that independence is the difference between an audit and a performance.

## output

the verifier appends its findings to the ledger as `actor: verifier` entries. a clean pass is itself a recorded, reasoned decision. a failure is an escalation.
