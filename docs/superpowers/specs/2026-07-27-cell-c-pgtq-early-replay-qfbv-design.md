# Cell C \(p>q\) Early-Replay QF_BV Checkpoint Design

## Objective

Create a durable, reproducible bounded audit of the following exact
necessary early-replay relaxation of the simultaneous-boundary residual:

\[
q>2r>0,\qquad r/2<t<r,\qquad p=q+t,
\]

\[
B[0]=2,\quad B\text{ has period }t,\quad Q[0]=3,
\]

\[
U=QB,\qquad R=BQB,\qquad X=B[r-t:r]UB.
\]

The audited conjunction is:

1. \(X^3\) has canonical pair \((3,p)\);
2. the autonomous orbit from \(X^3\) emits every symbol of \(U\);
3. \(R^2\) has canonical pair \((2,q)\).

This deliberately omits the standalone \(R^2B\) condition, canonical
\(F=B^3\), the later replay, the \(\mathcal J\)-only bridge replay,
terminal canonical \(H=(2,P)\), and all target-specific proper-period caps.
Every full \(p>q\) boundary survivor would satisfy the audited conjunction,
but the converse is not asserted.

The bounded computation is evidence about this residual only. Zero models
must be labelled `COMPUTED`, never treated as a proof of the unbounded word
obstruction, Cell C, either Generated Two-Cube target, or the Curling Number
Conjecture.

## Chosen architecture

Use two deliberately different engines.

The production engine is a fixed-parameter QF_BV satisfiability model. It
maps `2` to bit zero and `3` to bit one, constructs \(B,Q,U,R,X\) from the
structural coordinates, and expresses suffix powers by exact bit-vector
slice equalities. It checks every admissible \((q,r,t)\) through \(q=40\)
with a per-triple timeout and records `sat`, `unsat`, and `unknown`
separately.

The oracle is definition-first exhaustive enumeration through \(q=14\).
It independently enumerates all concrete structural assignments and computes
canonical curling pairs by literal exponent/period loops. The oracle shares
neither the bit-vector power predicates nor solver models. Its existential
answer for each parameter triple is compared with the solver answer.

This hybrid was chosen over:

- extending raw structural enumeration to \(q=40\), which grows
  exponentially and duplicates the existing \(q\le25\) checkpoint; or
- keeping an ad hoc notebook/inline solver, which would not preserve
  semantics, counts, witnesses, or a stable artifact.

## Exact solver semantics

For a word \(W\), exponent \(k\), and root length \(d\), `power(W,k,d)`
means that the last \(k\) consecutive length-\(d\) blocks are equal.

The displayed \(p\)-cube in \(X^3\) is canonical exactly when:

- no suffix cube has root \(d<p\); and
- no suffix fourth power exists.

The displayed \(q\)-square in \(R^2\) is canonical exactly when no suffix
square has root \(d<q\). This also excludes every cube suffix, because a cube
inside the length-\(2q\) word has root below \(q\) and contains a square of
the same root.

At phase \(\ell\), the requested bit \(U[\ell]\) selects one of two exact
conditions:

- bit zero / label `2`: some square suffix and no cube suffix;
- bit one / label `3`: some cube suffix and no fourth-power suffix.

Phase zero is already enforced by canonical \(X^3=(3,p)\) and
\(U[0]=3\). The solver checks phases \(1,\ldots,|U|-1\), so the endpoint
after all of \(U\) is not silently given an extra output constraint.

No first-mismatch trichotomy is imposed. That trichotomy uses paired later
replay and is not an early-replay-only consequence.

## Preserved sharpness data

The checkpoint retains five positive early-replay models after dropping only
canonical \(R^2=(2,q)\): the four known models at
\((q,r,t)=(10,4,3),(17,4,3),(17,7,4),(19,9,8)\), plus a representative
\((27,10,7)\) model. Their endpoint periods are \(6,3,4,4,4\),
respectively, all strictly below \(q\).

It also retains the exact endpoint-jump model

\[
(q,r,t)=(9,4,3),\quad B=2332,\quad Q=3.
\]

For \(Y=B^2U\), the final symbol `2` simultaneously changes

\[
R^2[:-1]:(2,1)\longrightarrow R^2:(2,9)
\]

and

\[
Y^2[:-1]:(2,1)\longrightarrow Y^2:(2,13).
\]

This model has canonical \(X^3=(3,12)\) but fails early replay at phase
one. It proves that endpoint root-push geometry alone cannot close the
wall.

## Outputs and tests

The implementation will add:

- `research/generated_two_cube_cell_c_pgtq_early_replay_smt.py`;
- `tests/test_generated_two_cube_cell_c_pgtq_early_replay_smt.py`;
- `research/outputs/generated_two_cube_cell_c_pgtq_early_replay_smt_2026-07-27.txt`.

Tests pin:

- the parameter domain and fail-closed bounds;
- solver/oracle agreement through \(q=14\);
- all preserved collapse and endpoint-jump certificates;
- deterministic rendering and the authoritative artifact hash;
- the command-line entry point.

Observed wall-clock timings belong in the decision log, not in the
deterministic artifact.
