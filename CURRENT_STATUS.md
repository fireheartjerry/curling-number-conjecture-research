# Current status — 2026-07-28

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
K=S\_{t_0+q}=LR^2T,\qquad t_G<t_0+q<t_F.
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

Write the phase-one pairs as

\[
E_1:(2,\alpha),\qquad F_1:(2,\beta),\qquad \alpha,\beta<P.
\]

The surviving row now has an exact transition atlas. The broken early
\(p\)-cube and adjacent-root separation force the strict pop

\[
\alpha<p,\qquad p\ge\alpha+\gcd(p,\alpha).
\]

At the later cube, either

\[
\beta<r,\quad r\ge\beta+\gcd(r,\beta),
\]

or

\[
\beta>2r+\gcd(r,\beta).
\]

Both phase-one states end in \(T_1=B^2\,3\). If either square fits this
common suffix, canonical minimality forces the common low root
\(\alpha=\beta<r\); otherwise both roots exceed \(r\). The high later root
is further restricted by

\[
2r+\gcd(r,\beta)<\beta<q,
\]

an exact copied-\(T_1\) return, and a Fine--Wilf threshold miss against the
visible \(q\)-square in \(R^2B\). In particular, \(r=1\) has only the
context-crossing alternative.

At any paired phase \(\ell\), differing roots \(a*\ell,b*\ell\) with
requested exponent \(k\_\ell\) obey

\[
k*\ell\min(a*\ell,b\_\ell)>2r+\ell.
\]

The endpoint predecessor transitions now have an exact adjacent-root
push/pop classification. D-035 now begins the exact two-half bridge atlas.
For \(0\le i<r\), put \(A_i=B[0:i]\), write
\(R=A_iC_i\), \(B=A_iD_i\), and let \(G_i,M_i\) be the cuts before the
two occurrences of the bridge symbol \(B[i]\). Their visible suffixes obey

\[
R^2A_i=A_i(C_iA_i)^2,\qquad
B^2A_i=A_i(D_iA_i)^2.
\]

If \(B[i]=2\), actual generation makes both curling numbers exactly two,
so the displayed squares are maximizing witnesses and

\[
\pi(G_i)\le q<P,\qquad \pi(M_i)\le r<P.
\]

The two families are exactly the proper actual-orbit bridge cuts:
\(G*i=K_i\) and \(M_i=K*{r+i}\) for \(0\le i<r\). Thus every bridge cut
whose actual next curling number is `2` self-caps and localizes,
independently of either target negation. This includes the omitted midpoint
and strengthens its old bound to \(\pi(M)\le r\). That visible-square
argument alone supplies no conclusion at cuts requesting `3`.

D-035 now also closes the capped first-half `3` classification. If
\(G_i=LR^2B[0:i]\) requests `3` and
\(h=\pi(G_i)<P\), then \(h>q\) would make
\(u=h-q<r\) a period of \(R\), contradicting
\((\kappa(G),\pi(G))=(2,q)\). If \(h=q\), finishing the remaining
symbols \(B[i:r]\) rotates the canonical cube into a cube at the midpoint
\(M\), contradicting its actual request `2`. Hence \(h<q\). Fine--Wilf
then prevents that cube from crossing the left edge of
\(R^2B[0:i]\), so the canonical cube lies wholly in the periodic word
\(R^{\mathbb Z}\) and is a proper circular cube of \(R\).

The actual midpoint label is essential: a pinned \(q=6,r=2\) local word
has \(h=q\) at the first-half `3` cut but requests `3`, not `2`, at
\(M\). Under the \(\mathcal J\)-negation all first-half bridge cuts are
capped. Under the \(\mathcal I\)-negation this result remains conditional
at omitted interior `3` cuts.

The capped second-half `3` classification is now also closed. If
\(M_i=LR^2B\,B[0:i]\) requests `3` and
\(h=\pi(M_i)<P\), then \(h\le r\). For \(h\ge r+i\), deleting the
appended \(B\,B[0:i]\) carries an \(h\)-square back to \(G\), forcing
\(h\ge q\). The case \(h=q\) contradicts \(B[0]=2\), \(Q[0]=3\);
the case \(q<h<q+r\) gives \(R\) a forbidden shorter period. For
\(r<h<r+i\), Fine--Wilf instead makes \(B\) a proper power, contradicting
the exact terminal label \(\kappa(F)=3\). If \(h<r\), the same
Fine--Wilf argument prevents the cube from crossing the visible
\(B^2B[0:i]\), so it is a proper circular cube of \(B\). The only
retained alternative is the full-root case \(h=r\), whose cube reaches
the \(BQ\mid B^2B[0:i]\) seam. Its exact suffix equation and cut location
are now closed by the next bridge step. Writing \(D_i=B[i:r]\), the
canonical root is \(D_iB[0:i]\), so comparison of its cube with the
structural suffix gives

\[
\operatorname{suf}\_{r-i}(BQ)=D_i.
\]

As the actual remaining word \(D_i\) is appended, that cube persists at
every intermediate cut with a cyclically shifted root. Hence every
remaining curling number is at least three. Because the bridge is binary
and actual generation gives \(\kappa(M_j)=B[j]\), it follows that
\(B[i:r]=3^{r-i}\). Thus \(r-i\le\lambda\), and the run bound
\(\lambda\le1\) from (C.33), also packaged in (C.35l), forces
\(i=r-1\) and \(\lambda=1\). At that cut the seam reduces to
\(Q[-1]=B[-1]=3\).

The actual future chronology is essential: a checked \(r=3,B=232,Q=332\)
static word has the full-root pair \((3,3)\), the seam, and \(\lambda=0\)
at \(i=1<r-1\), but the rotated cube generates `3` where its proposed
future bridge asks for `2`. No converse seam implication is claimed.

The D-035 target split is now explicit. On the boundary,
\(K*0=G,\ K_r=M,\ K*{2r}=F\), and

\[
\mathcal I\cap\{K_h:0\le h\le2r\}=\{G,F\},
\qquad
\{K_h:0\le h\le2r\}\subseteq\mathcal J.
\]

Thus a \(\mathcal J\)-negation caps every proper bridge cut. The
\(\mathcal I\)-negation omits every strict interior cut, but the visible
squares in (C.35y), via (C.35z), independently cap every actual cut
requesting `2`. Because \(B[0]=2\), every proper cut requesting `3` is
interior and its cap remains an explicit hypothesis under the
\(\mathcal I\)-negation. The localization lemma is used only after a cap
is established; it cannot prove its own period hypothesis.

Every proper actual binary bridge cut also excludes a fourth-power
suffix. For \(0\le h<2r\), actual generation gives

\[
\kappa(K_h)=B[h\bmod r]\in\{2,3\}.
\]

If \(K_h\) ended in \(Y^4\) for a nonempty word \(Y\), its curling number
would be at least four, a contradiction. This excludes every proper
circular fourth power which is visible as a suffix of \(R^2A_i\) or
\(B^2A_i\) at the corresponding cut. It does not exclude an internal
fourth-power factor ending somewhere else. No period cap, target
negation, localization, Fine--Wilf argument, or primitivity hypothesis
is used. That proof does not depend on the approved bounded audit recorded
next.

The approved D-035 bridge census through \(q\le25\) is now `COMPUTED` in
the standalone-local scope. It starts from
\(G\_{\rm loc}=X^3U\) and directly replays the requested continuation
\(B^2\); it does not enumerate an arbitrary left context \(L\), so it does
not classify the actual full bridge states
\(K_h=LR^2(B^2)[0:h]\). In the \(p>q\) branch the scan
has `2,388,798` structural assignments, `595,896` surviving \(z=1\)
assignments, `105,851` exact static candidates, `15,881` complete local
replays, and `127,048` proper cuts. Every complete replay has
\(r=4,\ B=\texttt{2232}\). In the \(p<q\) branch the corresponding counts
are `1,115,405 / 418,622 / 100,053 / 93,497 / 187,018`; the complete
replays split into `93,493` cases with \(r=1,\ B=\texttt{2}\) and four
with \(r=4,\ B=\texttt{2223}\).

Every complete local replay has all proper canonical periods below \(P\)
and the exact endpoint pair \((3,r)\). Across those replays there are zero
fourth-power suffix roots in either the full standalone-local state or the
visible proper-circular context. Every recorded theorem violation count is
zero, but the canonical second-half `3` period never equals \(r\), so the
full-root seam, suffix, and terminal conclusions have zero opportunities
and receive no bounded corroboration. The \(p>q\) seam cross-tab has
`15,881` low-root second-half `3` cuts with false seam; the four nontrivial
\(p<q\) cuts have low roots with true seam, directly protecting the
one-way nature of the seam implication.

Six literal certificates pin the \(q=12\) \(p>q\) replay, the \(q=8\)
\(p<q,r=1\) replay, and all four \(p<q,r=4\) replays at
\(q=23,24,25,25\). A production-independent oracle reconstructs both
normal forms and the complete \(q\le12\) census from literal
exponent/period loops, and independently checks all six certificates.
The deterministic artifact has SHA-256
`60A3D2F846AC34D081A5321AC24BB7114C8C6B1A5DBF7E846756331CA6454DF7`;
independent mathematical and code/publication reviews returned
`APPROVED`. This is finite `COMPUTED` evidence, not an unbounded proof or
an arbitrary-\(L\) orbit census. The reviewed checkpoint was published on
`main` at `65eaea25d3617e5cd81efa959782b82e3f5532ef`, so D-035 is now
`CLOSED`. Both boundary word walls, non-boundary Cell C, Cell C, both G2CS
targets, and the Curling Number Conjecture remain open.

The D-035 census code is now frozen under the proof-first research policy.
The next work is synthetic and unbounded: first the \(p>q\) boundary word
wall, then the \(p<q\) wall. Short brute-force scripts or direct
lemma-specific helpers remain allowed only when they test, falsify,
discover, or verify a precise mathematical claim.

The new definition-first \(z=1\) atlas through \(q\le25\) checks
`2388798` \(p>q\) and `1115405` \(p<q\) structures, retaining `105851`
and `100053` exact static rows. Phase one is valid in `79471` and `61200`
cases respectively. Every \(p>q\) valid pair is equal/local; the \(p<q\)
cases split into `6555` equal/local and `54645` unequal/high cases, with
all unequal cases occurring at \(r=1\). All bounded static words fail a
sampled replay, but failure phases need not synchronize. The exact
\(q=8,9,11,16,23,29\) certificates pin the sharp failures and high-root
geometry. This is `COMPUTED`, not a closure of the remaining row.
The LF-stable authoritative artifact was reproduced byte-for-byte in
`43.451` and `43.523` seconds; its SHA-256 is
`975E542B6AEF428B39C087095BCB0A77AD68E390D597CC21F1FB43DA72BCEFE9`.

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

The synthetic \(p>q\) attack has begun with a complete small-\(r\)
classification of the bridge word
(`research/pgtq_boundary_small_r.md`). The six inherited necessary
conditions on \(B\) — normal form, period \(t\) with \(r/2<t<r\),
\(B[a]=X[0]=2\) at \(a=r-t\), primitivity, no period \(\le r/2\), and
\(\lambda\le1\) — force \(r\ge3\); eliminate \(r=3\) outright; force
\((t,B)=(3,\texttt{2232})\) uniquely at \(r=4\); and reduce \(r=5\) to
exactly four words. The terminal-run transfer \(B[r-1]=B[a-1]\) shows
\(\lambda=1\) requires \(a\ge2\) and \(r\ge5\), so the D-035 full-root
seam cannot occur in this branch below \(r=5\). At \(r=4\) all interior
bridge cuts have exact \(q\)-independent canonical pairs
(\((2,1),(3,1),(2,4)\) patterns, with only \(\pi(G_3)\) still
\(q\)-dependent), phase one collapses to \(\alpha=\beta=2\) or a doubly
high pair with \(\alpha\ge9\), and every high root must return onto an
explicit `3` coordinate of \(Q\) or \(B\). These are proved for every
\(q\) and both targets; they concentrate the wall on
\(B=\texttt{2232}\) but do not close it. The remaining obstruction is
still the unbounded two-window replay.

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
