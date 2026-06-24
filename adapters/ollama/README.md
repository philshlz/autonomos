# ollama adapter

boots an autonomos agent against a local Ollama model. the local-first path: no external model host, the agent reaches no internet at all, and the walled network can be fully closed.

- model runs in-network; nothing leaves the box
- ideal for the LocalLLaMA audience and privacy-sensitive deployments
- proves the thesis at the extreme: even with a small local model, the handbook holds and the ledger is portable back to a frontier model later
