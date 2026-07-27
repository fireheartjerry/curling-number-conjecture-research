# Current status — 2026-07-27

## Bottom line

There is no complete proof or counterexample.

The Generated Two-Cube statement is now repaired and split into two explicit
targets with identical antecedents:

- the stronger two-window target (G2CS-\(\mathcal I\));
- the weaker natural full-precompletion target
  (G2CS-\(\mathcal J\)), where
  \(\mathcal J=\{S_t:t_0\le t<t_H\}\).

Cell B is `PROVED-NL` for both. Cell A is `BRIDGE-PROVED-NL` for the
\(\mathcal J\)/strict-record route but remains open for the stronger
\(\mathcal I\)-only target. Cell C remains open for both. These are
natural-language proof statuses, not formal verification.

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

In external Cell A, actual chronology supplies the genuine bridge state

\[
K=S_{t_0+q}=LR^2T,\qquad t_G<t_0+q<t_F.
\]

The repaired Cell A proof establishes

\[
\max\{\pi(E),\pi(K)\}\ge P.
\]

This is enough for strict-record contradiction because \(K\) precedes \(H\),
but \(K\notin\mathcal I\); it therefore does not prove the stronger
\(\mathcal I\)-only statement. The load-bearing Border--conjugate lemma now
has a complete four-case natural-language proof and an independent exhaustive
index certificate with `1776` binary plus `690` ternary retained tuples and
zero failures.

## Immediate open work

- Internal later cube (Cell C) for both synchronization targets.
- External later cube with `r=q` (Cell A) only for the stronger
  \(\mathcal I\)-only target.

The generated-block hypothesis remains essential: static word equations admit
explicit impostors. The repaired definitions include \(G\), exclude \(H\),
and distinguish the two-window family \(\mathcal I\) from the full proper
precompletion family \(\mathcal J\), so the terminal value
\(\pi(H)=P\) cannot make either target tautological.

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
