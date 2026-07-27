# Current status — 2026-07-27

## Bottom line

There is no complete proof or counterexample.

The newest external work reduces the immediate square-bridge problem to a
Generated Two-Cube Synchronization statement. That statement is still open
and, as written in the mega-ledger, needs a quantifier repair before it can be
load-bearing.

## Strongest current local picture

Using the mega-ledger notation

\[
R=AB=TU,\quad q=|R|,\quad b=|B|,\quad P=q+b,
\]

\[
T=R[0:j],\quad U=R[j:q],\quad Y=BR=BTU,
\]

the actual windows are

\[
E=LRT \xrightarrow{\,U\,} G=LR^2,
\qquad
F=LR^2BT \xrightarrow{\,U\,} H=LR^2BR.
\]

At a first promotion failure, the current ledger derives

\[
\operatorname{cn}(E)=3,\quad
\operatorname{cn}(G)=2,\quad
\operatorname{cn}(F)=3,\quad
\operatorname{cn}(R^2T)=2.
\]

Every `2`-position promotes. Therefore a first failure must be a `3 -> 2`
configuration with two context-dependent cube witnesses.

## Immediate open cells

- External later cube with `r=q`.
- External later cube with `q<r<P`.
- Internal later cube.

The generated-block hypothesis is essential: static word equations admit
explicit impostors.

## Required specification repair

The phrase “an intermediate canonical period at least `P` during one of the
generated copies of `U`” must exclude the terminal completed state `H`, whose
canonical period is `P` by hypothesis. Otherwise the synchronization statement
is tautological.

Any formal statement must explicitly list the proper prefixes included on
`E -> G` and `F -> H`, and state whether `G` is included and `H` is excluded.

## Global work remaining even after bridge promotion

1. Replay stability and first return to `R^2`.
2. Consecutive square bridge monotonicity `q2 <= q1`.
3. Elimination of infinite square-record-only chains.
4. Record-cube recurrence.
5. Autonomous exact-power termination.
6. Lift from the binary hard core to arbitrary finite integer sequences.
7. Lean 4 formalization and adversarial audit of every load-bearing claim.

## Conditional dependency

The Mignosi–Restivo–Salemi golden-ratio periodicity theorem exists and states
that an infinite word is ultimately periodic exactly when every sufficiently
long prefix ends in a suffix of exponent at least \(\varphi^2\). The project
still must audit each application against the theorem's exact one-sided-prefix
hypotheses before using it to eliminate record exponents `K >= 4` or derive
infinitely many generated `2`s.

