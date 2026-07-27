# Generated Two-Cube Wall Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** State, finitely falsify, and either prove or rigorously refute the repaired Generated Two-Cube Synchronization lemma.

**Architecture:** The canonical mathematical statement and coordinate table live
in one Markdown file. A small independent Python witness engine mirrors those
quantifiers and enumerates actual-orbit candidates; tests pin down endpoint,
generation, canonical-period, and calibration semantics. Cells A, B, and C are
audited independently before a synthesis document changes project status.

**Tech Stack:** Python 3, `pytest`, exact finite-word combinatorics, Markdown,
Git, optional Z3 only after a finite model is stated without hidden caps.

---

## File map

- Create `research/generated_two_cube_statement.md`: canonical notation,
  exact state families, theorem statement, and coordinate audit.
- Create `research/generated_two_cube_falsifier.py`: independent canonical
  witness engine and actual-orbit candidate extraction.
- Create `tests/test_generated_two_cube_falsifier.py`: semantic and regression
  tests.
- Create `research/generated_two_cube_cells.md`: Cell A/B/C proof ledger.
- Create `research/outputs/generated_two_cube_scan_2026-07-27.txt`: exact
  bounded scan output and parameters.
- Modify `docs/DECISION_LOG.md`: append every theorem, computation, and branch
  decision.
- Modify `CURRENT_STATUS.md`: only after a verified status change.

### Task 1: Freeze the repaired theorem statement

**Files:**
- Create: `research/generated_two_cube_statement.md`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Define the canonical functions**

Write:

```markdown
For a nonempty word \(W\), let \(\kappa(W)\) be its curling number. When
\(\kappa(W)\ge2\), let \(\pi(W)\) be the least period among suffixes
\(X^{\kappa(W)}\). Thus \(\pi(W)\) is a shortest maximizing period, not merely
the period of a displayed power. When \(\kappa(W)=1\), set
\(\pi(W)=|W|\) as the explicit executable sentinel; this is not a claim that
\(|W|\) is the literal shortest period of an \(X^1\) display.
```

- [ ] **Step 2: Enumerate both generated state families**

Write, with \(m=|U|=q-j\):

```markdown
\[
E_\ell=LRTU[0:\ell]\quad(0\le\ell\le m),\qquad
F_\ell=LR^2BTU[0:\ell]\quad(0\le\ell\le m).
\]

Hence \(E_0=E\), \(E_m=G=LR^2\), \(F_0=F\), and \(F_m=H\).
The proper pre-completion state set is
\[
\mathcal I=\{E_\ell:0\le\ell\le m\}
\cup\{F_\ell:0\le\ell<m\}.
\]
It includes \(G\) and excludes \(H\).
```

- [ ] **Step 3: State actual generation without shorthand**

Take the full-state orbit occurrences as primitive:

```markdown
\[
E_\ell=S_{t_0+\ell},\qquad
F_\ell=S_{t_0+P+\ell}
\qquad(0\le\ell\le m).
\]
```

Then derive, rather than separately assume:

```markdown
\[
\kappa(E_\ell)=U[\ell]=\kappa(F_\ell)
\qquad(0\le\ell<m).
\]
```

Explicitly note that the full-state equalities assert generation in the full
contexts \(LRT\) and \(LR^2BT\); they are stronger than a static word equation
or standalone continuation from \(R^2T\). Derive the actual pre-completion
order from \(P-m=b+j>0\).

- [ ] **Step 4: State the repaired synchronization implication**

Write:

```markdown
If \(R^2T\) has no cube suffix, then
\[
\max_{W\in\mathcal I}\pi(W)\ge P.
\]
```

List all hypotheses: \(R=AB=TU\), \(0<b<q\), \(P=q+b\), \(Y=BR=BTU\),
the primitive full-state orbit equalities, \(\kappa(E)=\kappa(F)=3\),
\(\kappa(G)=2\) with \(\pi(G)=q\), \(\kappa(R^2T)=2\), and \(H\) a completed
square state with \(\kappa(H)=2\), \(\pi(H)=P\). State the
strict-record minimality hypothesis separately as a contradiction corollary;
do not bake it into the record-free combinatorial core. Also state the fully
generated specialization using
\[
|H|-2P=x+q-b\ge n_{\mathrm{seed}}.
\]

- [ ] **Step 5: Audit endpoint coordinates**

Add a table with word, start, end, length, inclusion, and known canonical
period for \(E_\ell,F_\ell,G,H,R^2T\). Use half-open intervals throughout.

- [ ] **Step 6: Record and commit the decision**

Append a decision that \(G\) is included and \(H\) excluded, then run:

```bash
git diff --check -- research/generated_two_cube_statement.md docs/DECISION_LOG.md
git add research/generated_two_cube_statement.md docs/DECISION_LOG.md
git commit -m "State repaired generated two-cube lemma"
git push origin main
```

Expected: a clean diff and a pushed theorem-specification commit.

### Task 2: Build the canonical witness engine test-first

**Files:**
- Create: `tests/test_generated_two_cube_falsifier.py`
- Create: `research/generated_two_cube_falsifier.py`

- [ ] **Step 1: Write failing witness tests**

Create:

```python
from research.generated_two_cube_falsifier import canonical_witness


def test_canonical_witness_checks_every_block_length():
    assert canonical_witness((2, 3, 2, 3, 2)) == (2, 2)


def test_canonical_witness_uses_shortest_maximizing_period():
    assert canonical_witness((2, 2, 2, 2)) == (4, 1)


def test_canonical_witness_handles_no_repeated_suffix():
    assert canonical_witness((2, 3)) == (1, 2)
```

- [ ] **Step 2: Verify the tests fail for the missing module**

Run:

```bash
python -m pytest -q tests/test_generated_two_cube_falsifier.py
```

Expected: collection failure because
`research.generated_two_cube_falsifier` does not exist.

- [ ] **Step 3: Implement the independent witness function**

Create:

```python
from __future__ import annotations

from collections.abc import Sequence


Word = tuple[int, ...]


def canonical_witness(sequence: Sequence[int]) -> tuple[int, int]:
    word = tuple(sequence)
    if not word:
        raise ValueError("canonical_witness requires a nonempty word")
    best_exponent = 1
    best_period = len(word)
    for period in range(1, len(word) + 1):
        block = word[-period:]
        exponent = 1
        cursor = len(word) - 2 * period
        while cursor >= 0 and word[cursor : cursor + period] == block:
            exponent += 1
            cursor -= period
        if exponent >= 2 and (
            exponent > best_exponent
            or (exponent == best_exponent and period < best_period)
        ):
            best_exponent = exponent
            best_period = period
    return best_exponent, best_period
```

- [ ] **Step 4: Run the focused tests**

Run:

```bash
python -m pytest -q tests/test_generated_two_cube_falsifier.py
```

Expected: `3 passed`.

- [ ] **Step 5: Add cross-checks against `curling.py`**

Add:

```python
import itertools

from curling import curling_number


def test_witness_exponent_matches_reference_on_small_words():
    for length in range(1, 9):
        for word in itertools.product((2, 3), repeat=length):
            assert canonical_witness(word)[0] == curling_number(word)
```

Run the focused file and expect all tests to pass.

- [ ] **Step 6: Commit**

```bash
git add research/generated_two_cube_falsifier.py \
  tests/test_generated_two_cube_falsifier.py
git commit -m "Add canonical witness engine"
git push origin main
```

### Task 3: Encode actual generation and the nonterminal state set

**Files:**
- Modify: `research/generated_two_cube_falsifier.py`
- Modify: `tests/test_generated_two_cube_falsifier.py`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Write failing tests for paired generation**

Add:

```python
from research.generated_two_cube_falsifier import generated_states


def test_generated_states_include_start_and_terminal():
    states = generated_states((2, 2), (2,))
    assert states == ((2, 2), (2, 2, 2))


def test_generated_states_reject_wrong_requested_symbol():
    try:
        generated_states((2, 3), (2,))
    except ValueError as error:
        assert "expected 2 but generated 1" in str(error)
    else:
        raise AssertionError("wrong generation was accepted")
```

- [ ] **Step 2: Implement exact generated states**

Add:

```python
def generated_states(start: Sequence[int], requested: Sequence[int]) -> tuple[Word, ...]:
    current = tuple(start)
    states = [current]
    for expected in requested:
        actual, _ = canonical_witness(current)
        if actual != expected:
            raise ValueError(f"expected {expected} but generated {actual}")
        current += (actual,)
        states.append(current)
    return tuple(states)
```

- [ ] **Step 3: Test \(G\)-included/\(H\)-excluded semantics**

Add a `synchronization_evaluation_states(early_states, later_states)` function that
returns `early_states + later_states[:-1]`, and test:

```python
def test_evaluation_states_includes_g_and_excludes_h():
    early = ((1,), (1, 2))
    later = ((3,), (3, 2))
    assert synchronization_evaluation_states(early, later) == ((1,), (1, 2), (3,))
```

- [ ] **Step 4: Run tests and record the semantic decision**

Run:

```bash
python -m pytest -q tests/test_generated_two_cube_falsifier.py
```

Expected: all focused tests pass. Append the result and exact semantics to
`docs/DECISION_LOG.md`.

- [ ] **Step 5: Commit**

```bash
git add research/generated_two_cube_falsifier.py \
  tests/test_generated_two_cube_falsifier.py docs/DECISION_LOG.md
git commit -m "Encode paired generated state semantics"
git push origin main
```

### Task 4: Extract fully generated strict-record-square candidates

**Scope:** this extractor covers only the fully generated strict-record
application specialization of (G2CS), not every antecedent of the general
record-free combinatorial core.

**Files:**
- Modify: `research/generated_two_cube_falsifier.py`
- Modify: `tests/test_generated_two_cube_falsifier.py`

- [ ] **Step 1: Define the event record**

Add:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class OrbitEvent:
    time: int
    word: Word
    exponent: int
    period: int
    seed_length: int

    def final_copy_generated(self) -> bool:
        return len(self.word) - self.period >= self.seed_length

    def entire_power_generated(self) -> bool:
        return len(self.word) - self.exponent * self.period >= self.seed_length
```

- [ ] **Step 2: Test the two generation predicates are distinct**

Add:

```python
def test_final_copy_and_entire_power_generation_are_distinct():
    event = OrbitEvent(
        time=4,
        word=(9, 9, 2, 3, 2, 3),
        exponent=2,
        period=2,
        seed_length=3,
    )
    assert event.final_copy_generated()
    assert not event.entire_power_generated()
```

- [ ] **Step 3: Implement capped orbit tracing with an explicit result**

Add `trace_orbit(seed, step_limit)` returning `(events, termination)`, where
`termination` is exactly one of `"hit_one"` or `"step_limit"`. Never stop
merely because the curling number leaves `{2,3}`.

- [ ] **Step 4: Add calibration tests**

Test total lengths `5`, `66`, and `142` for the three preserved seeds, and
test that a one-step cap returns `"step_limit"` rather than silently dropping
the trajectory.

- [ ] **Step 5: Implement candidate extraction**

Extract only events satisfying all of:

```text
exponent == 2
period is a new strict record period
entire_power_generated() is true
the earlier generated root boundary is present in the trace
q < P
b = P - q > 0
2*q - P > 0
```

For the terminal exponent-\(2\), period-\(P\) event,
`entire_power_generated()` is the exact seed-boundary test
`len(word) - 2*P >= seed_length`. Do not replace it by a seed-free word-length
inequality.

Store `seed`, `L`, `R`, `A`, `B`, `Y`, `P`, `q`, and the exact trace indices
used to derive them.

- [ ] **Step 6: Run focused and full tests**

```bash
python -m pytest -q tests/test_generated_two_cube_falsifier.py
python -m pytest -q
```

Expected: all tests pass; the full suite remains at least the prior 16 tests
plus the new file.

- [ ] **Step 7: Commit**

```bash
git add research/generated_two_cube_falsifier.py \
  tests/test_generated_two_cube_falsifier.py
git commit -m "Extract fully generated record-square candidates"
git push origin main
```

### Task 5: Run the repaired bounded falsifier

**Scope:** run and report the falsifier only over Task 4's fully generated
strict-record specialization. Counts from this scan are not exhaustive counts
of the general-core antecedent.

**Files:**
- Modify: `research/generated_two_cube_falsifier.py`
- Create: `research/outputs/generated_two_cube_scan_2026-07-27.txt`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Classify first failures**

For every candidate and every `j`, construct \(T,U,E_\ell,F_\ell,G,H\)
directly from stored coordinates. Require paired actual generation before
classifying a case. Report:

```text
seed_length, seed, P, q, b, j
kappa(E), pi(E), kappa(F), pi(F), kappa(G), pi(G)
kappa(R^2T), pi(R^2T)
max pi over I
cell = A | B | C | none
```

- [ ] **Step 2: Add regression tests for both inherited impostors**

Assert that:

- `D=223222, R=322232` is rejected because the strict-record bridge
  generation hypothesis is absent;
- the static `R=233323, B=23, j=1` configuration is rejected because the
  first requested copy of \(R\) is not generated from \(LR\).

- [ ] **Step 3: Run a bounded scan with explicit caps**

Run:

```bash
python research/generated_two_cube_falsifier.py \
  --max-seed-length 18 --step-limit 500 \
  > research/outputs/generated_two_cube_scan_2026-07-27.txt
```

The first lines must print calibration results and the final lines must report
seed count, candidate count, capped trajectories, fully generated
specialization antecedent count, Cell A/B/C counts, and verified/refuted count.

- [ ] **Step 4: Interpret without overclaiming**

Append a `COMPUTED` decision containing the command, caps, exact counts, and
whether a generated counterexample was found. State explicitly that zero
bounded counterexamples is not a proof.

- [ ] **Step 5: Verify and commit**

```bash
python -m pytest -q
git diff --check -- research/generated_two_cube_falsifier.py \
  tests/test_generated_two_cube_falsifier.py \
  research/outputs/generated_two_cube_scan_2026-07-27.txt \
  docs/DECISION_LOG.md
git add research/generated_two_cube_falsifier.py \
  tests/test_generated_two_cube_falsifier.py \
  research/outputs/generated_two_cube_scan_2026-07-27.txt \
  docs/DECISION_LOG.md
git commit -m "Falsify generated two-cube wall on bounded orbits"
git push origin main
```

### Task 6: Audit Cell A

**Files:**
- Create: `research/generated_two_cube_cells.md`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Restate Cell A in half-open coordinates**

Record \(r=q\), \(b<q/2\), border \(B\), prefix equality
\(R[0:j]=R[b:b+j]\), and the exact overlap supporting (22.5)–(22.7).

- [ ] **Step 2: Test the desired short-period extraction**

Search bounded symbolic words satisfying the static Cell A equations and
separately those satisfying paired generation. For each survivor, compute all
periods \(t<b\) of \(UT\). Save the smallest counterexample to any proposed
universal extraction.

- [ ] **Step 3: Prove or refute the missing implication**

The only acceptable branch outcomes are:

- a complete index-audited derivation of \(0<t<b\) on \(UT\);
- a direct cube in \(R^2T\);
- a state in \(\mathcal I\) with canonical period at least \(P\);
- an explicit generated counterexample.

- [ ] **Step 4: Status and commit**

Mark Cell A `PROVED-NL`, `PROVISIONAL-NL`, `COMPUTED`, or `REFUTED`, cite the
exact evidence, append the decision log, commit, and push.

### Task 7: Audit Cell B

**Files:**
- Modify: `research/generated_two_cube_cells.md`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Normalize Cell B variables**

Use \(c=r-q\), \(\delta=b-c=P-r\), and record:

```text
q/2 < c < b
R has period c
B = suf_c(R) R[0:delta]
R[0:j] = R[delta:delta+j]
delta+j <= q-gcd(r,P)-1
```

- [ ] **Step 2: Enumerate equality classes before letters**

Build the union-find equality system induced by period \(c\), the definition
of \(B\), and the \(\delta\)-shift. Determine which parameter tuples force a
square or cube independently of alphabet labels.

- [ ] **Step 3: Inject paired-generation inequalities**

For surviving equality classes, impose exact canonical-witness conditions at
every \(E_\ell,F_\ell\). Reject any model using a displayed nonmaximal power.

- [ ] **Step 4: Prove, refute, record, and commit**

Use the same four acceptable outcomes as Cell A; append exact evidence and
push the checkpoint.

### Task 8: Audit Cell C

**Files:**
- Modify: `research/generated_two_cube_cells.md`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Replace prose geometry by intervals**

Let the later \(r\)-cube be the suffix interval
\([|F|-3r,|F|)\). Express its containment in \(YBT\) and all crossings of
\(Y|B\) and \(B|T\) using half-open inequalities. Do not use the inherited
ambiguous three-way prose split.

- [ ] **Step 2: Apply the internal bound**

Record \(2r\le P-\gcd(r,P)-1\), then enumerate all possible placements relative
to the copied \(B,T,U\) blocks.

- [ ] **Step 3: Couple to the early external cube**

Use the common suffix \(BT\), the conjugate \(UBT\), and paired actual
generation to force either the synchronization conclusion or a finite
parameter survivor family.

- [ ] **Step 4: Prove, refute, record, and commit**

Use the same evidence statuses and checkpoint protocol as Cells A and B.

### Task 9: Synthesize and adversarially audit

**Files:**
- Modify: `research/generated_two_cube_statement.md`
- Modify: `research/generated_two_cube_cells.md`
- Modify: `CURRENT_STATUS.md`
- Modify: `docs/DECISION_LOG.md`

- [ ] **Step 1: Check complete cell coverage**

Verify that every later cube is either external with \(r=q\), external with
\(q<r<P\), or internal. Check that no placement is lost at equality endpoints.

- [ ] **Step 2: Re-run all executable evidence**

```bash
python -m pytest -q
python research/generated_two_cube_falsifier.py \
  --max-seed-length 18 --step-limit 500
```

Expected: tests pass and output matches the preserved scan file.

- [ ] **Step 3: Update status conservatively**

Only call synchronization proved if Tasks 6–8 each have a complete proof and
the synthesis audit finds no missing case. Otherwise list the exact surviving
cell and strongest established restrictions.

- [ ] **Step 4: Commit and push**

```bash
git add research/generated_two_cube_statement.md \
  research/generated_two_cube_cells.md CURRENT_STATUS.md \
  docs/DECISION_LOG.md
git commit -m "Audit generated two-cube synchronization wall"
git push origin main
```

- [ ] **Step 5: Start downstream work only if justified**

If the wall is proved, write a new design/plan for replay stability and first
return. If refuted, revise the bridge-promotion route around the verified
counterexample. If still open, continue only on the named surviving cell.
