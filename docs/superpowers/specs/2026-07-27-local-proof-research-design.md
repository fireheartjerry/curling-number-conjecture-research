# Local proof-research design

Date: 2026-07-27

## Objective

Continue the attack on the Curling Number Conjecture locally while keeping
GitHub as the canonical durable state. The immediate target is the Generated
Two-Cube Synchronization wall, not a premature claim about the full
conjecture.

## Chosen approach

Use a theorem-first proof/falsification loop:

1. Write the exact quantified synchronization statement, including every
   generated intermediate prefix and all endpoint conventions.
2. Encode the same statement as a bounded falsifier that rejects static
   impostors and preserves deterministic-generation hypotheses.
3. Split the proof obligation into Cells A, B, and C using exact interval
   coordinates.
4. Attack each cell independently, promoting a result only after a
   counterexample search and an index audit agree with it.
5. Update the dependency graph and downstream status only after the local wall
   is genuinely closed.

This is preferred over a foundations-first audit because the repository audit
already isolates the immediate wall, and over a computation-first census
because bounded survival cannot prove the synchronization theorem.

## Research artifacts

- `docs/DECISION_LOG.md`: append-only numbered decisions, including reversals.
- `research/generated_two_cube_statement.md`: canonical theorem statement and
  coordinate conventions.
- `research/generated_two_cube_falsifier.py`: calibrated bounded falsifier.
- `research/generated_two_cube_cells.md`: proof attempts and status for Cells
  A, B, and C.
- Exact command outputs under `research/outputs/` when a computation becomes
  evidence for a claim.

## Evidence discipline

Every claim receives one status:

- `PROVED-NL`: complete natural-language proof with endpoints audited.
- `PROVISIONAL-NL`: plausible proof with an identified audit obligation.
- `COMPUTED`: exact executable program, parameters, and preserved output.
- `CONJECTURED`: unproved target.
- `REFUTED`: explicit counterexample or contradiction.

Displayed powers are lower bounds until maximal curling number and shortest
maximizing period are checked. “Generated” must identify whether the final
copy begins after the seed or the entire power lies after the seed.

## Commit protocol

Commit and push after each durable unit:

1. statement or convention change;
2. executable falsifier or calibration change;
3. proof-cell advance, refutation, or branch closure;
4. status/dependency update.

No force-pushes. Historical imported artifacts remain byte-preserved.

## Verification

Before each push:

- run the targeted falsifier or proof-checking script;
- run `python -m pytest -q` when shared code changes;
- inspect `git diff --check` on newly authored files;
- ensure the decision log names the reason and evidence for the change.

## Success boundary

The immediate phase succeeds only when the repaired Generated Two-Cube
Synchronization theorem is either proved with all three cells closed or
refuted with a fully verified generated counterexample. That result still does
not solve the full Curling Number Conjecture.
