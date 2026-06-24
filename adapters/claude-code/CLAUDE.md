# claude-code adapter

boots an autonomos agent on the claude family via claude code.

- loads `/handbook` (read-only mount)
- appends decisions to `/state/ledger/ledger.jsonl` in schema format
- records `"model": "claude-opus-4-8"` (or current) on every entry
- egress through the enforcement proxy only

this file is the only claude-specific artifact in the repo. the rules it enforces and the state it writes are identical to what every other adapter produces.
