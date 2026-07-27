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
\(X=B[r-t:r]UB\). For \(p<q\), writing \(d=q-p\), the overlap equations
now force
\[
d>2r,\qquad q>4r,\qquad p>2r.
\]
With \(\nu=d-2r=|\Theta|>0\), the middle word \(Q\) begins in
\(\Theta B^2\), ends in \(B\Theta\), and \(X=Q[d:|Q|]B^2\).
Writing \(D=Q[d:|Q|]\) and \(e=2p-P\), its terminal seam is exactly

\[
D=JB\Theta\quad(e\ge0),\qquad
D=B[c:r]\Theta\quad(e<0,\ c=P-2p).
\]

In the overlap case \(0<c<r/2\) and \(B[0:c]=B[r-c:r]\). With
\(C=\Theta B^2\), \(H_0=\Theta B\), and
\(A=JB\) or \(B[c:r]\), both seams have the unified form
\(X=AC,\ U=CAH_0\).

In either period branch, every proper state whose canonical period is below
\(P\) has the same canonical pair as the standalone continuation
\(X^3(UB^2U)[0:v]\). Thus an \(\mathcal I\)-negation localizes both sampled
windows but not its uncapped bridge interior, while a
\(\mathcal J\)-negation makes the entire proper \(UB^2U\) episode
autonomous.

Writing \(z\) for the first \(2\) in \(U\) and \(h\) for the first
\(X^\omega/U\) mismatch, paired early/later replay forces \(h<z\), and the
terminal run of \(3\)'s at the later copy first leaves
\((z,h)=(1,0),(2,0),(2,1)\), with explicit coordinates in \(X\), and in
\(B\) for the \(p>q\) form.

A branch-independent full-state lemma now eliminates both \(z=2\) rows.
If \(z=2\), the sampled state \(F_1=LR^2B^2\,3\) must have a canonical
pair \((3,\rho)\) with \(\rho<P\). Deleting its last `3`, comparing the
resulting \(\rho\)-periodic suffix first with the terminal \(B^3\) and then
with \(R^2\), forces \(\rho=q\). The terminal \(q\)-cube would then equate
the positions \(R_2[r]=Q[0]=3\) and \(B_4[0]=B[0]=2\), which are exactly
\(q\) apart. This contradiction applies to both \(\mathcal I\)- and
\(\mathcal J\)-negations because both include and cap \(F_1\). Thus only

\[
(z,h)=(1,0),\qquad U[0:2]=32,\qquad X[0]=2,\qquad\lambda\le1
\]

remains on the simultaneous boundary.

In the \(p>q\) branch, the canonical \(G\)-scale now also gives a
two-scale phase restriction. If an early canonical pair is \((k,s)\), with
\(k\in\{2,3\}\), \(s<P\), and \(s\ne q\), then, for
\(g=\gcd(s,q)\),
\[
\min(ks,q+r+\ell)<s+q-g.
\]
Thus every such root lies in an exact contained-low or crossing-high
branch. At the first \(X^\omega/U\) mismatch, the old \(p\)-root cannot
survive; the replacement is a strict adjacent pop. These reductions do not
exclude a later root push back to the endpoint scale.

This sharpens but does not close the word wall: a checked \(q=10\) near-model
replays both sampled windows below \(P\) while failing the required
\(G,H\) endpoint scales. The older \(q=20,p=11\) \(p<q\) model realizes the
exceptional \(2p<P\) seam and all static endpoint scales, but lies in the
now-eliminated \(z=2\) row and fails at \(F_1\), exactly as the theorem
predicts.

The surviving row has a stronger \(q=23,r=4,p=13,P=27\) warning. It lies on
the \(c=1\) overlap seam, has \((z,h)=(1,0)\), and has exact static
\(G,F,H\) pairs \((2,23),(3,4),(2,27)\). Both sampled local traces replay
the first `13` symbols of \(U=3222322232232322232\), but at phase `13` the
requested `3` meets pair \((2,3)\) in both. The remaining row is therefore
a later, nonlocal replay obstruction. The target-specific word walls in
both branches and the non-boundary Cell C placements remain open.

An independent definition-first regression through \(q\le20\) checks
`73470` \(p>q\) and `34405` \(p<q\) structural assignments. It retains
`2841` and `2016` exact \(z=2\) candidates respectively, split
`1394,1447` and `1343,673` across the two rows. All `4857` have
\(\kappa(F_1)\in\{1,2\}\); zero has the required value `3`. The \(p<q\)
counts exercise both exact seams. This is nonvacuous bounded corroboration,
not the proof.

The exact \(p>q\) boundary residual now has a durable structural search
through \(q\le25\). It reduces `1792552320` theoretical raw
root--parameter pairs to `2388798` assignments, with `563688` surviving the
canonical \(R^2\), standalone, and \(X^3\) filters. Exactly one word replays
the later window with the required initial pair \((3,r)\): the known
\(q=9,r=3,t=2\) certificate. Its final proper later state already has
period \(P=12\), and its early replay fails at phase \(1\). Consequently
there are zero bounded \(\mathcal I\)- or \(\mathcal J\)-survivors in this
branch. An independent raw-root definition-first oracle reproduces the
complete stage counts through \(q\le10\).

The earlier first-mismatch diagnostic is also nonvacuous: `197773`
canonical assignments satisfy the preliminary three-row trichotomy,
including the terminal-\(3\)-run bound, and all fail exact early replay by
\(q=25\). The new theorem discards its `45116` and `46806` double-`3`
rows; the `105851` \((1,0)\) assignments remain a bounded diagnostic. This
is `COMPUTED` evidence, not a proof of the remaining wall. The unbounded
\(p>q\) word wall therefore remains open alongside the \(p<q\) and
non-boundary cases.

A second, independent \(p>q\) checkpoint encodes the weaker necessary
conjunction "canonical \(X^3\), full autonomous early replay, canonical
\(R^2\)" directly in QF_BV, without using the paired-replay trichotomy.
It does not encode standalone \(R^2B\), canonical \(F\), later or
\(\mathcal J\)-bridge replay, terminal canonical \(H=(2,P)\), or any
target-specific proper-period cap.
Every one of the `1050` admissible parameter triples through \(q\le40\) is
UNSAT, with zero solver unknowns. A definition-first oracle separately
enumerates all `1014` concrete assignments through \(q\le14\) and agrees on
all `26` triple outcomes. Dropping canonical \(R^2\) recovers five exact
positive early replays, all collapsing to roots `3`, `4`, or `6`.
This is stronger bounded exclusion evidence, still only `COMPUTED`; it does
not prove the unbounded early-replay collapse lemma or close Cell C.

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
