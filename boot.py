#!/usr/bin/env python3
"""autonomos boot stub.

the adapter (claude-code / openrouter / ollama) overrides this with a real
agent loop. its job is always the same: load the handbook as binding,
read and append to the ledger, route egress through the proxy, and record
which model is running on every decision.
"""
print("autonomos: handbook loaded as binding. ledger mounted append-only.")
print("egress restricted to allowlist. model recorded per decision.")
print("the model is rented. the state is owned.")
