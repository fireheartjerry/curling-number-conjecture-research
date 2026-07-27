# Curling Number Conjecture Research

Private working archive for a multi-stage attack on the Curling Number
Conjecture.

> **Current status:** no complete proof and no counterexample is known in this
> repository. Many claims are natural-language proofs, conditional reductions,
> bounded computations, provisional arguments, or refuted approaches. Status
> labels are part of the mathematics and must not be flattened.

## Start here

1. Read [`FULL_PROOF_CHECKLIST.md`](FULL_PROOF_CHECKLIST.md) for the durable
   critical path, strengthening track, completion gates, and immediate work.
2. Read [`CURRENT_STATUS.md`](CURRENT_STATUS.md) for the detailed live state.
3. Read the canonical external consolidation:
   [`external/chatgpt-mega-ledger-2026-07-27/CURLING_NUMBER_CONJECTURE_MEGA_LEDGER_2026-07-27.md`](external/chatgpt-mega-ledger-2026-07-27/CURLING_NUMBER_CONJECTURE_MEGA_LEDGER_2026-07-27.md).
4. Read [`docs/REPOSITORY_AUDIT_2026-07-27.md`](docs/REPOSITORY_AUDIT_2026-07-27.md)
   before treating any computational or packaging claim as load-bearing.
5. For cloud continuation, use
   [`cloud/CLOUD_CONTINUATION_PROMPT.md`](cloud/CLOUD_CONTINUATION_PROMPT.md).

## Repository layout

- `research/` — internal Codex proof notes, failed routes, Python/Z3 probes,
  C++ searches, literature logs, and the chronological research ledger.
- `tests/` and `curling.py` — calibrated reference implementation and tests.
- `external/chatgpt-mega-ledger-2026-07-27/` — consolidated work from three
  external ChatGPT research chats, including source code, outputs, handoff
  ledgers, and the original prompt PDF.
- `archive/` — the original external handoff ZIP, preserved byte-for-byte.
- `docs/` — provenance and cross-source audit notes.
- `cloud/` — authoritative continuation prompt for remote work.

## Quick validation

```bash
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python -m pytest -q
python external/chatgpt-mega-ledger-2026-07-27/sources/verify_part3_examples.py
```

The external C++ audits require a C++20 compiler. Z3-based probes require
`z3-solver`; see `requirements.txt`.

## Research discipline

- A displayed suffix power proves only a lower bound on the curling number.
- Every numerical curling-number claim must come from executed, calibrated
  code that checks every suffix block length.
- Distinguish preloaded powers, final-copy-generated powers, and entirely
  generated powers.
- Bounded computation is evidence, never an unbounded theorem.
- Do not claim the conjecture from bridge promotion alone; autonomous
  exact-power termination remains a separate global wall.
