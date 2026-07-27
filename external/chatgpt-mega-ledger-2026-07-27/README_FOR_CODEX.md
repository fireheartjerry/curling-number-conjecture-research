# Curling Number Conjecture handoff package

This folder consolidates all preserved work from three ChatGPT research chats into one repository-ready package.

## Start here

1. Read `CURLING_NUMBER_CONJECTURE_MEGA_LEDGER_2026-07-27.md`.
2. Use `CODEX_CONTINUATION_PROMPT.md` as the opening task for Codex.
3. Treat `PROJECT_STATUS.json` as a machine-readable snapshot, not a proof.
4. Use `sources/` for code, outputs, older ledgers, the original prompt PDF, and raw reports.

## Current state

The full bridge-promotion lemma is not yet proved. Every `2`-position promotes, and every first failure has been reduced to a `3 -> 2` configuration with two generated external cube windows. The latest work divides the remaining synchronization problem into three rigid cells.

The final global wall after the square branch is autonomous exact-power termination.

## Verification

```bash
python sources/verify_part3_examples.py

g++ -O3 -std=c++20 sources/audit_all_square_replay.cpp -o /tmp/audit_replay
/tmp/audit_replay 18 500
```

Checksums for every source artifact are in `MANIFEST.json` and at the end of the mega-ledger.
