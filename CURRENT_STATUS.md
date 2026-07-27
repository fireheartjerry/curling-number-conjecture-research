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

For internal Cell C, exact half-open geometry now reduces every survivor to

\[
\alpha=P+b+j-3r\ge0,\qquad
r<b+j<3r,\qquad
2r\le P-\gcd(r,P)-1,\qquad
b<2r,\qquad j>0.
\]

An equality-first record-free scan exhausts every binary local start
\(|E=LRT|\le18\). It checks `2361` integer tuples, `714444` equality-class
root assignments, and `2866488` bounded contexts with an exact canonical
witness implementation that is independently cross-checked on every binary
word through length `10`. The `120` complete G2CS antecedents all have
\((R,b,j,r)=((2,3,2),1,1,1)\), all lie on \(b+j=2r\) and \(j=r\), and all
already have period at least \(P\) in both \(\mathcal I\) and
\(\mathcal J\). There are zero bounded survivors, but this computation is
not a proof; Cell C remains open for both targets.

On the simultaneous boundary selected by every bounded antecedent,
\(b+j=2r,j=r\), the exact symbolic form is

\[
b=j=r,\qquad R=BQB,\qquad T=B,\qquad U=QB,\qquad q>2r,
\]

with \(B[0]=2\), \(Q[0]=3\), and later cube \(B^3\). Under
\(p=\pi(E)<P\), the early cube forces two explicit branches. For \(p>q\),
writing \(t=p-q\), one has \(r/2<t<r\) and
\(X=B[r-t:r]UB\). In this branch every proper state whose canonical period
is below \(P\) has the same canonical pair as the standalone continuation
\(X^3(UB^2U)[0:v]\). Thus an \(\mathcal I\)-negation localizes both sampled
windows but not its uncapped bridge interior, while a
\(\mathcal J\)-negation makes the entire proper \(UB^2U\) episode
autonomous.

Writing \(z\) for the first \(2\) in \(U\) and \(h\) for the first
\(X/U\) mismatch, the autonomous early window forces \(h<z\), and the
terminal run of \(3\)'s at the later copy leaves only
\((z,h)=(1,0),(2,0),(2,1)\), with explicit coordinates in \(B\).
This sharpens but does not close the word wall: a checked \(q=10\) near-model
replays both sampled windows below \(P\) while failing the required
\(G,H\) endpoint scales. The \(p<q\) shifted-border/frontier equations and
the non-boundary Cell C placements also remain open.

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
