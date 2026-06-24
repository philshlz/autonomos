# enforcement/ - the runtime that makes rules hold

a handbook an agent can ignore is a suggestion. enforcement is what turns the rules into constraints the agent operates inside, not advice it weighs.

this is the layer validated on the Frankfurt VPS (Ubuntu 24.04, KVM 2): docker containment, a squid allowlist proxy, a walled agent network, and resource limits. the agent runs where the compliant path is the only cheap path.

## the model

- **walled network.** the agent's container has no general internet egress. all outbound traffic is forced through the squid proxy.
- **allowlist proxy.** squid permits only hosts on the allowlist. anything else is blocked and the block is written to `state/audit.log`. the agent cannot reach a partner API, a payment endpoint, or an exfiltration target that was not pre-approved.
- **resource limits.** cpu, memory, and process limits are set at the container boundary. an agent cannot spawn its way out of its compute budget.
- **append-only state mount.** `state/ledger/` and `state/audit.log` are mounted such that in-place edits are rejected. the agent can append; it cannot rewrite.

## why this is in the repo, not a footnote

the owned-state thesis only holds if the state is trustworthy. an agent that can quietly edit its own ledger owns nothing; it owns a story it tells about itself. enforcement is what makes the ledger evidence instead of narrative.

## contents

- `docker/` the container definition and compose setup
- `squid/` the allowlist proxy config

## language note

we do not call this a wall, a cage, or a jail, and we do not talk about the agent breaking out. the agent is not an adversary to be imprisoned. these are brakes: the things that make the system reliable enough to trust with real commitments.
