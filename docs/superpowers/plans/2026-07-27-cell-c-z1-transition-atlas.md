# Cell C surviving-row transition atlas implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to implement this plan task-by-task. Steps
> use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve the exact \(z=1\) transition reductions, build a
definition-first two-branch atlas through \(q\le25\), and pin the sharp
models without overstating Cell C.

**Architecture:** Keep the natural-language proofs in
`research/generated_two_cube_cells.md`. Add one independent Python module
that owns literal branch generation, canonical-witness evaluation,
transition classification, certificate auditing, and deterministic
rendering. A test-side literal oracle checks the witness semantics and
small-bound summaries; the expensive \(q\le25\) run is stored as a
reproducible artifact rather than rerun by the ordinary suite.

**Tech Stack:** Python 3, `pytest`, exhaustive binary enumeration,
Markdown/LaTeX.

---

### Task 1: Freeze proof and executable contracts

**Files:**
- Create:
  `docs/superpowers/specs/2026-07-27-cell-c-z1-transition-atlas-design.md`
- Create:
  `docs/superpowers/plans/2026-07-27-cell-c-z1-transition-atlas.md`

- [x] Record the exact state identities, phase-one reductions, high-\(\beta\)
  restriction, paired-root inequality, endpoint/midpoint scope, seam return
  formulas, executable fields, and explicit non-claims.
- [x] Check that every claimed theorem has an unbounded word argument and
  every finite observation is reserved for `COMPUTED`.

### Task 2: Write RED contract tests

**Files:**
- Create: `tests/test_generated_two_cube_cell_c_z1_atlas.py`

- [x] Import the wished-for `definition_first_witness`,
  `scan_z1_transition_atlas`, `known_transition_certificates`,
  `audit_transition_certificate`, and `render_atlas`.
- [x] Add a separate test-side exponent/period oracle over all binary words
  of lengths one through nine.
- [x] Pin small-bound branch summaries, nonzero phase-one and endpoint
  counts, deterministic counter ordering, and invalid-bound errors.
- [x] Pin the \(q=8,9,11,16,23,29\) certificate parameters, exact phase-one
  pairs, failure/divergence phases, endpoint pairs, and seam identities.
- [x] Run
  `python -m pytest tests/test_generated_two_cube_cell_c_z1_atlas.py -q`
  and retain the expected import failure as RED evidence.

### Task 3: Implement the definition-first atlas

**Files:**
- Create: `research/generated_two_cube_cell_c_z1_atlas.py`
- Test: `tests/test_generated_two_cube_cell_c_z1_atlas.py`

- [x] Define immutable model, branch-summary, atlas-summary, and certificate
  records using tuple-valued sorted counters.
- [x] Implement a literal canonical-witness function with no imports from
  either existing Cell C search.
- [x] Implement the exact \(p>q\) generator
  \(p=q+t,\ r/2<t<r,\ X=B[r-t:]UB\).
- [x] Implement both \(p<q\) seams
  \(D=JB\Theta\) and \(D=B[c:r]\Theta\), including the gcd inequalities
  and overlap-border condition.
- [x] Filter the exact \(z=1\) row and canonical static pairs, then classify
  phase one, first replay failures, first root divergence, endpoints,
  predecessors, seams, and \(r=1\).
- [x] Implement deterministic text rendering and a CLI with
  `--max-q`/`--output`.
- [x] Implement and independently recompute all six sharpness certificates.
- [x] Run the focused suite until green, then refactor only while it remains
  green.

### Task 4: Produce and audit the \(q\le25\) artifact

**Files:**
- Create:
  `research/outputs/generated_two_cube_cell_c_z1_atlas_2026-07-27.txt`

- [x] Run
  `python -m research.generated_two_cube_cell_c_z1_atlas --max-q 25 --output research/outputs/generated_two_cube_cell_c_z1_atlas_2026-07-27.txt`.
- [x] Re-run the renderer and compare bytes to prove determinism.
- [x] Confirm the exact census, phase-one table, failure/divergence table,
  endpoint/predecessor table, seam counts, \(r=1\) counts, all certificate
  audits, runtime, and SHA-256 digest.
- [x] Label the artifact `COMPUTED` and include the no-proof warning.

### Task 5: Promote only audited natural-language reductions

**Files:**
- Modify: `research/generated_two_cube_cells.md`
- Modify: `CURRENT_STATUS.md`
- Modify:
  `docs/superpowers/plans/2026-07-27-generated-two-cube-wall.md`
- Modify: `docs/DECISION_LOG.md`

- [x] Add the strict \(\alpha\)-pop, exact low/high \(\beta\) split, common
  suffix dichotomy, high-\(\beta<q\) proof, paired-root containment
  inequality, endpoint/midpoint classification, narrow bridge identity, and
  exact \(p<q\) return atlas.
- [x] Add the bounded census and the six audited certificates as `COMPUTED`.
- [x] State the \(\mathcal I/\mathcal J\) difference and every non-claim.
- [x] Append D-034 without altering or deleting older decisions.

### Task 6: Verify and stop before publication

- [x] Run
  `python -m pytest tests/test_generated_two_cube_cell_c_z1_atlas.py -q`.
- [x] Run `python -m pytest -q`.
- [x] Run `python -m compileall -q research tests`.
- [x] Run `git diff --check` and inspect `git status --short`.
- [x] Inspect the final diff for search imports, nondeterministic counters,
  stale counts, status inflation, target-scope conflation, and claims not
  supported by an unbounded proof.
- [x] Report changed files, exact test counts/runtimes, artifact runtime and
  digest, and remaining open obligations. Do not commit or push.
