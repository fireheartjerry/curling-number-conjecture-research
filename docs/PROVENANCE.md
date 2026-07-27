# Provenance

This repository combines two research lines.

## Internal Codex archive

Source directory at consolidation time:

`C:\Users\fireh\OneDrive\Documents\Curling Problem`

Included:

- all Markdown proof and research notes;
- Python and C++ source;
- tests;
- preserved small text outputs;
- literature-search logs;
- dependency and approach registries.

Excluded as reproducible/non-authoritative build material:

- `.git/`;
- `.vendor/` (vendored Z3 runtime);
- `__pycache__/` and `.pytest_cache/`;
- compiled `.exe`, `.dll`, `.obj`, and `.pyc` files.

## External ChatGPT archive

Original package:

`Curling_Number_Conjecture_Mega_Ledger_2026-07-27.zip`

The original ZIP is preserved under `archive/`. Its extracted contents are
under `external/chatgpt-mega-ledger-2026-07-27/`.

The ZIP contains two distinct filenames that differ only by case:

- `sources/Curling_Number_Proof_Ledger.md`
- `sources/curling_number_proof_ledger.md`

Windows cannot preserve both paths directly. The second was retained as
`sources/curling_number_proof_ledger__case_collision_2.md`. Both byte streams
match their respective source-manifest hashes.

## Authority order

When sources conflict:

1. `CURRENT_STATUS.md` and `docs/REPOSITORY_AUDIT_2026-07-27.md`;
2. the front current-status sections of the 2026-07-27 mega-ledger;
3. Part 3 of that mega-ledger;
4. the 2026-07-26 handoff;
5. older internal/external ledgers;
6. bounded computational output.

Older files remain valuable for proof details and countermodels, but their
status labels are not automatically current.

