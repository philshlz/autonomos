# adapters/ - model-agnostic boot

an adapter boots an agent from the handbook and points it at the shared state. the handbook and `state/` are identical across every adapter. that identity is the proof of the thesis: the model is the one swappable part.

| adapter | path | use it for |
|---------|------|-----------|
| claude-code | `claude-code/` | claude family, agentic coding workflows |
| openrouter | `openrouter/` | cross-family swapping (claude, gpt, gemini, llama...) |
| ollama | `ollama/` | local-first, no external host, full privacy |

## the test that matters

clone the repo, run the same company under all three adapters, and the ledger entries are interchangeable. a decision recorded by the claude-code adapter is read, understood, and continued by the ollama adapter without translation. if that breaks, the adapter is wrong, never the handbook.

## adding an adapter

an adapter is thin. it must:

1. load the handbook sections its role requires
2. read and append to `state/ledger/` in the schema format
3. route all egress through the enforcement proxy
4. record its `model` value on every ledger entry it writes

nothing in an adapter may live in `handbook/` or `state/`. keep model-specifics here.
