# conformance

this repository is the **reference implementation** of the autonomos spec.

- the spec is canonical: `handbook/` (the 11 sections) and `state/ledger/SCHEMA.md` (the ledger format).
- everything else (`enforcement/`, `adapters/`, `verifier/`, `state/` tooling, `site/`) is one conformant implementation of that spec.
- the model running an agent is rented and swappable. the spec is owned. the implementation declares which spec version it conforms to, exactly the way the ledger records which model made each decision.

**this implementation conforms to autonomos-spec v0.2.**

when a third party wants the spec without this runtime, the spec directories
split into a standalone `autonomos-spec` repo via `git subtree split`, and this
repo pins it back via submodule or package. the seam is already clean.
