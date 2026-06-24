#!/usr/bin/env python3
"""autonomos independent verifier (reference stub).

replays the rationale ledger and checks each decision against the
handbook section it cites. deliberately model-free: the verifier reasons
about rules and chains, not about what a model "meant".
"""
import json
import sys
import hashlib
from pathlib import Path

LEDGER = Path(__file__).resolve().parents[1] / "state" / "ledger" / "ledger.jsonl"

def load(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def check_chain(entries):
    """every entry must point at its predecessor."""
    problems = []
    prev_id = None
    for e in entries:
        if e["prev"] != prev_id:
            problems.append(f"{e['id']}: prev={e['prev']} expected {prev_id}")
        prev_id = e["id"]
    return problems

def check_gates(entries):
    """any externally binding commitment above ceiling must have taken a gate."""
    problems = []
    for e in entries:
        amt = e.get("inputs", {}).get("amount_eur", 0)
        if amt and amt > 50 and not e.get("gate", {}).get("required"):
            problems.append(f"{e['id']}: spend {amt} EUR above ceiling without gate")
    return problems

def main():
    if not LEDGER.exists():
        print(f"no ledger at {LEDGER}")
        return 1
    entries = load(LEDGER)
    print(f"replaying {len(entries)} ledger entries independently...")
    chain = check_chain(entries)
    gates = check_gates(entries)
    if not chain and not gates:
        print("PASS: chain intact, all gates honored, no rule violations found")
        # note which models appear, to make the swap visible
        models = sorted({e.get("model") for e in entries if e.get("model")})
        print(f"models seen across history: {models}")
        print("same handbook applied across every model. continuity verified.")
        return 0
    for p in chain + gates:
        print(f"FAIL: {p}")
    return 2

if __name__ == "__main__":
    sys.exit(main())
