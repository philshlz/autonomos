# autonomos

**models are rented. state is owned.**

autonomos is the governance and enforcement layer for organizations run by AI agents. it is the operating handbook for companies where the rules actually hold, instead of being suggestions a model may or may not follow this week.

the model running your agent is a commodity. it will be deprecated, swapped, repriced, or beaten by a competitor inside a year. what you own is the state: the rules the agent operates under, the rationale behind every decision it made, and the audit trail that lets a new model pick up cold and keep going. autonomos is built so that state outlives any single model.

## the core claim

escalation rules are commodity. anyone can write "ask a human before spending over $X." what is hard, and what autonomos owns, is **portable, model-agnostic state**:

- a written handbook the agent must operate under, not just be prompted with
- an append-only rationale ledger that records why every decision was made
- an enforcement runtime that makes the rules hold even when the model tries to route around them
- an independent verifier that audits the orchestrator instead of trusting it

swap the model underneath all of this and the company keeps running. that is the whole point.

## what's in here

| path | what it is |
|------|-----------|
| `state/` | the owned-state layer. the ledger, the audit log, the memory. this is the asset. |
| `handbook/` | the rules. 11 sections. commodity on their own, load-bearing in combination with state. |
| `enforcement/` | the runtime that makes rules hold. docker + squid allowlist + walled network + resource limits. |
| `verifier/` | the independent role that audits the orchestrator. |
| `adapters/` | model-agnostic boot adapters. claude-code, openrouter, ollama. the model is one swappable part. |
| `prompts/` | instantiation prompts (basic, red-team, federation). |
| `showcases/` | demonstrations that the state survives a model swap. |
| `site/` | landing page + the federation animation. |

## run it

start with `adapters/` and pick the model path that fits you. the handbook and the ledger are identical across all three. that identity is the proof.

## license

docs under CC BY 4.0. code under MIT. see `LICENSE`.

## what autonomos is not

it is not an agent orchestrator. it sits beneath the orchestrator as the layer that makes its decisions reliable and auditable. orchestrators decide what to do. autonomos decides what is allowed, records why, and proves it held.
