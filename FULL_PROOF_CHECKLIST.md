# Curling Number Conjecture Full-Proof Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to execute a scoped checkpoint. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the current natural-language reductions and executable
evidence into a complete contradiction to every hypothetical nonterminating
curling-number orbit.

**Architecture:** The active route starts from the proved record-root and
bounded-overhang reductions, converts every sufficiently large record cube
into an exact generated square-to-cube maturation, and tries to rule out an
unbounded changing-origin family via generated two-cube synchronization.
The bridge-inclusive target \(\mathcal J\) is the present critical path; the
stronger sampled-only target \(\mathcal I\) is tracked separately.

**Evidence stack:** Markdown word proofs, definition-first Python witnesses,
exhaustive bounded scans, SAT/SMT diagnostics, adversarial review, and
eventual Lean 4 formalization.

---

## How to use this file

- This is the stable top-level roadmap. Update it whenever a checkpoint
  changes a status, dependency, countermodel, or proof obligation.
- `[x]` means the named repository-standard checkpoint exists. It does not
  turn a natural-language argument into a formally verified theorem.
- `PROVED-NL` means an unbounded natural-language proof is recorded.
- `COMPUTED`, `CHECKED`, `SAT`, and `UNSAT` describe only the executed
  finite domain. They are never substitutes for an unbounded proof.
- `OPEN` means no valid closure proof is currently recorded.
- The detailed live state is in `CURRENT_STATUS.md`; immutable decisions and
  rejected inferences belong in `docs/DECISION_LOG.md`.
- Baseline when this roadmap was created: private branch
  `research/generated-two-cube-wall`, checkpoint `9bfab19`.

## Canonical context

- Conjecture: every finite nonempty starting sequence of positive integers
  eventually generates a `1`.
- \(\kappa(W)\) is the maximal suffix exponent at state \(W\).
- \(\pi(W)\) is the least root length attaining that maximal exponent.
- The binary hard core uses generated labels in \(\{2,3\}\).
- \(\mathcal I\) contains the two sampled generated \(U\)-windows.
- \(\mathcal J\) contains every proper state before the completion state
  \(H\), including the otherwise omitted \(G\)-to-\(F\) bridge.
- Since \(\mathcal I\subseteq\mathcal J\), proving
  G2CS-\(\mathcal I\) is stronger. G2CS-\(\mathcal J\) is nevertheless
  sufficient for the current strict-record contradiction route.

Canonical files:

- `research/generated_two_cube_statement.md`
- `research/generated_two_cube_cells.md`
- `research/research_ledger.md`
- `research/bounded_overhang_maturation.md`
- `research/one_sided_threshold_ancestry.md`
- `CURRENT_STATUS.md`
- `docs/DECISION_LOG.md`

## Dependency spine

```text
hypothetical nonterminating orbit
    |
    +-- finite tail alphabet and unbounded least maximizing roots
    |
    +-- unbounded label-3 record roots; high-label roots bounded
    |
    +-- bounded-overhang exact maturation:
    |       L Z^2 --append actual Z--> L Z^3
    |
    +-- OPEN: exclude an unbounded changing-origin maturation family
            |
            +-- active mechanism: generated two-cube synchronization
            |       |
            |       +-- Cell A
            |       +-- Cell B
            |       +-- Cell C
            |
            +-- replay/return monotonicity and record recurrence
                    |
                    +-- autonomous exact-power termination
                            |
                            +-- lift binary hard core and assemble contradiction
```

## Phase 0 — Preserve and audit the research base

- [x] Preserve the original prompt and complete external ChatGPT.com ledger.
- [x] Preserve all code, searches, artifacts, witnesses, and literature notes.
- [x] Record provenance and evidence status instead of silently promoting
  external claims.
- [x] Freeze the exact \(\kappa/\pi\) conventions, generated-state
  coordinates, endpoint inclusion, and \(\mathcal I/\mathcal J\) scopes.
- [x] Establish definition-first witness implementations and regression
  tests.
- [ ] Perform one final whole-repository provenance audit before claiming
  the conjecture.

## Phase 1 — Existing global reductions

- [x] **`PROVED-NL`: finite-tail and root-growth reductions.**
  Under a hypothetical counterorbit, late labels lie in a finite alphabet
  and least maximizing-root lengths are unbounded.
- [x] **`PROVED-NL`: high-label root bound.**
  Sufficiently late roots at labels at least four have a uniform bound.
- [x] **`PROVED-NL`: unbounded label-three record roots.**
  Every hypothetical counterorbit has unbounded cube-root records, and every
  sufficiently late new cube-root record has exact label three.
- [x] **`PROVED-NL`: bounded-overhang exact maturation.**
  Every sufficiently large record cube yields, after a uniformly bounded
  rotation, generated states
  \(LZ^2\) and \(LZ^3\), separated by the actual output \(Z\), with exact
  labels two and three and \(Z[0]=2\).

**Open obstruction handed to Phases 2–3:** Phase 1 exposes, but does not
close, the changing-origin problem. The actual completion checkbox is in
Phase 3, after generated two-cube synchronization and the required
recurrence machinery are available. This is one obligation recorded at its
input and output points, not two separate proof gaps.

Completion gate:

- [ ] Re-audit the full dependency chain from the counterorbit assumption to
  bounded-overhang maturation without importing any conclusion from a
  bounded experiment.

## Phase 2 — Generated two-cube synchronization

### 2A. Completed cell reductions

- [x] **Cell A for \(\mathcal J\): `BRIDGE-PROVED-NL`.**
  The required period-\(P\) witness occurs at \(E\) or at a genuine bridge
  state.
- [ ] **Cell A for \(\mathcal I\): `OPEN`, strengthening track.**
  A witness must be forced inside the sampled family rather than only on the
  omitted bridge. This is not required if the final strict-record proof uses
  only G2CS-\(\mathcal J\).
- [x] **Cell B for both targets: `PROVED-NL`.**
- [x] **Cell C simultaneous-boundary normalization: `PROVED-NL`.**
  Reduce to \(s=2r,\ j=r,\ b=r,\ R=BQB,\ U=QB,\ q>2r\), with exact
  \(p>q\) and \(p<q\) normal forms.
- [x] **D-033: eliminate both \(z=2\) rows.**
- [x] **D-034: preserve the unique-\(z=1\) transition atlas.**
  The strict \(\alpha\)-pop, low/high \(\beta\) split, high-\(\beta<q\)
  restriction, return atlas, and bounded \(q\le25\) census are recorded.

### 2B. D-035 two-half bridge atlas — `IN PROGRESS`

- [x] **`PROVED-NL`: every proper actual-orbit bridge cut requesting `2`
  self-caps.**
  The two indexed halves exhaust all such cuts. Its visible circular square
  gives canonical-root length at most \(q\) on the first half and at most
  \(r\) on the second half, without assuming the negation of either target.
- [ ] For a capped first-half cut requesting `3`, prove the canonical root
  satisfies \(h<q\) and gives a proper circular cube of \(R\).
- [ ] For a capped second-half cut requesting `3`, prove either
  \(h<r\) and a proper circular cube of \(B\), or \(h=r\) at the terminal
  seam.
- [ ] Prove that the full-root case \(h=r\) implies
  \(\operatorname{suf}_{r-i}(BQ)=B[i:r]\), and that
  \(\lambda\le1\) forces \(i=r-1\).
- [ ] Record the target distinction: \(\mathcal J\) caps every proper bridge
  state; \(\mathcal I\) automatically caps `2` cuts but not arbitrary `3`
  cuts.
- [ ] Prove that no visible proper fourth power is compatible with an actual
  binary bridge cut.
- [ ] Build a definition-first two-branch bridge census through \(q\le25\),
  pin sharp models, and label every finite result `COMPUTED`.
- [ ] Obtain independent exact-proof and code/publication reviews.
- [ ] Commit and push the reviewed D-035 checkpoint.

Frozen D-035 correction:

- The seam equation is **not** equivalent to the canonical equality \(h=r\).
  The safe implication is \(h=r\Rightarrow\) seam. A seam can coexist with
  a smaller maximizing cube; the \(q=13,r=4,B=2232\) audit model realizes
  local pair \((3,1)\). Never restore the false converse.

### 2C. Close Cell C

- [ ] **Boundary \(p>q\) wall for \(\mathcal J\).**
  Exclude the surviving \(z=1\) trajectory using the transition and
  two-half bridge atlases.
- [ ] **Boundary \(p<q\) wall for \(\mathcal J\).**
  Handle both exact seams, the large \(r=1\) family, and the nontrivial
  \(r=4\) bridge models.
- [ ] **Non-boundary Cell C for \(\mathcal J\).**
  Cover every strict placement region and every equality endpoint.
- [ ] If pursuing the stronger theorem, close the corresponding
  \(\mathcal I\)-only boundary and non-boundary walls separately.
- [ ] Reject any proposed closure that uses only zero bounded survivors,
  SAT/UNSAT up to a finite bound, synchronized sample traces, or static word
  equations without actual generation.

### 2D. Synthesize G2CS

- [ ] Audit that every later cube belongs to exactly the intended Cell A,
  B, or C placement, with no missing equality boundary.
- [ ] Verify all canonical pairs in full context; do not replace them with
  standalone suffix calculations.
- [ ] Prove G2CS-\(\mathcal J\) from the completed cell results.
- [ ] Confirm explicitly that G2CS-\(\mathcal J\) is sufficient for the
  strict-record route used in the global proof.
- [ ] Optionally prove the stronger G2CS-\(\mathcal I\) after its Cell A and
  Cell C strengthening branches close.
- [ ] Run the complete executable evidence suite and compare every
  authoritative artifact byte-for-byte.
- [ ] Obtain an adversarial cell-coverage review before promotion.

## Phase 3 — Convert synchronization into a global contradiction

- [ ] **Replay stability and first return to \(R^2\).**
  Show the synchronized generated episode has the required next record-scale
  return, rather than merely a static repeated block.
- [ ] **Consecutive square-bridge monotonicity.**
  Prove the required root-scale inequality \(q_2\le q_1\), including equality
  and overlap cases.
- [ ] **Eliminate infinite square-record-only chains.**
  Rule out an orbit that evades cube recurrence through endlessly changing
  maximizing square roots.
- [ ] **Record-cube recurrence.**
  Connect successive large label-three records with an exact ancestry or
  descent relation strong enough to control their origins.
- [ ] **Close the changing-origin maturation family.**
  Combine recurrence, bridge monotonicity, and generated synchronization to
  force stabilization or a strictly descending well-founded rank.
- [ ] **Survive known countermodels.**
  Any proposed rank must handle the Q21 fixed-profile reset cycle, terminal
  \(F\)-inflation tower, Fibonacci suffix-copy countermodel, and known
  midpoint rank failures.
- [ ] **Autonomous exact-power termination.**
  Once a fixed-origin tower is forced, prove that its exact self-generation
  cannot continue forever without producing `1`.

## Phase 4 — Generality and final proof assembly

- [ ] Audit every use of the Mignosi–Restivo–Salemi golden-ratio periodicity
  theorem against its exact one-sided-prefix hypotheses, or remove that
  dependency.
- [ ] Lift the binary \(\{2,3\}\) hard core to every finite starting
  sequence of positive integers.
- [ ] Handle all sentinels, degenerate roots, empty bridges, duplicate
  states, and endpoint equalities explicitly.
- [ ] Assemble one linear proof from the counterorbit assumption to a
  contradiction, with no forward references to unproved lemmas.
- [ ] Re-run every executable checker from a clean checkout and record tool
  versions, commands, runtimes, bounds, and artifact hashes.
- [ ] Perform a fresh hostile review whose only job is to find a missing
  case, a reversed implication, a standalone/full-context substitution, or
  an illicit finite-to-infinite inference.
- [ ] Produce a dependency-minimal paper draft with precise literature
  attribution and no novelty claim unsupported by the search record.
- [ ] Formalize the load-bearing combinatorics in Lean 4.
- [ ] Mark the conjecture proved only after the complete dependency chain
  passes both mathematical and provenance audits.

## Immediate next actions

1. Finish and independently review D-035 with the corrected one-way seam
   implication.
2. Use its bridge root ceilings against the \(p>q\) and \(p<q\) boundary
   word walls.
3. Decide whether the critical route needs only \(\mathcal J\) or whether a
   later global lemma unexpectedly requires the stronger \(\mathcal I\).
4. Update this file and `docs/DECISION_LOG.md` at every proof checkpoint,
   rejected inference, or dependency change.

## Final claim gate

Do **not** claim a proof of the Curling Number Conjecture until all critical
unchecked boxes above are closed by unbounded arguments and the resulting
single dependency chain has passed an independent adversarial audit.
