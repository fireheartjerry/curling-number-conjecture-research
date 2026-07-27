# Cell C double-`3` elimination implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:executing-plans` to implement this plan task by task.

**Goal:** Promote the simultaneous-boundary \(z=2\) contradiction to
`PROVED-NL`, independently regress it in both period branches, and expose
the exact surviving \(p<q\) seam geometry without overstating Cell C.

**Architecture:** Keep the unbounded proof in
`research/generated_two_cube_cells.md`. Add one small definition-first
finite oracle whose literal canonical-witness engine and structural word
construction do not import production Cell C search code. Tests pin
nonvacuous row/seam counts, zero \(F_1\)-label-`3` candidates, and a
\(q=23\) endpoint-correct \(z=1\) sharpness certificate.

**Tech stack:** Python 3, `pytest`, Markdown, exhaustive binary word
enumeration.

---

### Task 1: Freeze the theorem and evidence contracts

**Files:**
- Create:
  `docs/superpowers/specs/2026-07-27-cell-c-double-three-elimination-design.md`
- Create:
  `docs/superpowers/plans/2026-07-27-cell-c-double-three-elimination.md`

Record the exact \(G,F,F_1\) state identities, all \(\rho\)-cases, target
scope, the \(p<q\) seam split, executable independence requirements, and
explicit non-claims.

### Task 2: Write the independent regressions first

**Files:**
- Create:
  `tests/test_generated_two_cube_cell_c_double_three.py`

Add tests for:

1. literal canonical-witness behavior on a small complete word domain;
2. nonzero \(p>q\) counts in both \(z=2\) rows and zero retained
   \(\kappa(F_1)=3\);
3. nonzero \(p<q\) counts in both \(z=2\) rows, both seam branches, and zero
   retained \(\kappa(F_1)=3\);
4. exact \(q=23\), \(z=1\) endpoint-correct sharpness data and its first
   nonlocal replay failure.

Run only this new file and capture the expected import/contract failure
before implementation.

### Task 3: Implement the bounded definition-first oracle

**Files:**
- Create:
  `research/generated_two_cube_cell_c_double_three.py`
- Modify:
  `tests/test_generated_two_cube_cell_c_double_three.py`

Implement a local exhaustive canonical-witness function, explicit branch
enumerators, row/seam counters, direct \(F_1\) evaluation, and the pinned
near-model certificate. Do not import either production Cell C search.

Run the new test file until green. Record exact caps, counts, and runtime in
the theorem documentation.

### Task 4: Promote the natural-language theorem

**Files:**
- Modify: `research/generated_two_cube_cells.md`
- Modify: `CURRENT_STATUS.md`
- Modify:
  `docs/superpowers/plans/2026-07-27-generated-two-cube-wall.md`
- Modify: `docs/DECISION_LOG.md`

Add the branch-independent double-`3` lemma with every endpoint inequality
and comparison stated. Replace the three-row residual by the sole
\((1,0)\) row under either target negation. Document both \(p<q\) seams and
the unified \(X=AC,\ U=CAH\) form. Add the exact bounded evidence and the
\(q=23\) warning. Append D-033. Preserve `OPEN` for Cell C and every
remaining wall.

### Task 5: Verify before handoff

Run:

```text
python -m pytest tests/test_generated_two_cube_cell_c_double_three.py -q
python -m pytest -q
python -m compileall -q research tests
git diff --check
git status --short
```

Inspect the final diff for status inflation, accidental production-search
imports, target-scope conflation, and undocumented generated artifacts.
Report exact changed files, test counts, runtimes, and remaining claims.
Stop before commit or push.
