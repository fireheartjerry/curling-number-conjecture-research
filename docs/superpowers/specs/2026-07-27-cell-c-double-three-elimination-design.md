# Cell C simultaneous-boundary double-`3` elimination

**Date:** 2026-07-27
**Status sought:** `PROVED-NL` under the exact simultaneous-boundary and
target-negation hypotheses below. Cell C remains `OPEN`.

## Objective

Eliminate the two first-mismatch rows with first `2` at phase \(z=2\):

\[
(z,h)=(2,0),(2,1).
\]

The argument must be independent of the \(p>q\) versus \(p<q\) description
of the early canonical cube. It must use the actual state \(F_1\), not a
standalone surrogate, and it must preserve the different scopes of
\(\mathcal I\) and \(\mathcal J\).

## Exact theorem contract

Assume the simultaneous Cell C boundary

\[
q>2r>0,\qquad P=q+r,
\]

and words

\[
B[0]=2,\qquad Q[0]=3,\qquad
R=BQB,\qquad U=QB.
\]

For a common left context \(L\), put

\[
G=LR^2,\qquad
F=LR^2B^2,\qquad
F_1=LR^2B^2\,3.
\]

Assume the exact canonical data

\[
(\kappa(G),\pi(G))=(2,q),\qquad
(\kappa(F),\pi(F))=(3,r).
\]

If the first `2` in \(U\) is at \(z=2\), paired actual generation gives
\(U[0:3]=332\). In particular

\[
\kappa(F_1)=U[1]=3.
\]

Under the negation of either target, \(F_1\) is a proper sampled later
state and its canonical root obeys

\[
(\kappa(F_1),\pi(F_1))=(3,\rho),\qquad \rho<P.
\]

The theorem must prove that these hypotheses are inconsistent. The
first-mismatch index \(h\) and the early root \(p\) are not used.

## Proof architecture

Delete the final `3` from the canonical \(\rho\)-cube at \(F_1\). The
result is a \(\rho\)-periodic suffix of \(F\) of length

\[
3\rho-1.
\]

Put \(g=\gcd(r,\rho)\). Exhaust the following cases.

1. **\(\rho<r\), with \(2\rho\le r\).** The last \(2\rho\) symbols form a
   \(\rho\)-square inside the final copy of \(B\). The identical copy of
   \(B\) ends \(G\), contradicting the canonical pair \((2,q)\).

2. **\(\rho<r\), with \(2\rho>r\).** The suffix of length
   \(3\rho-1\) has periods \(r,\rho\), and
   \[
   3\rho-1\ge r+\rho-g.
   \]
   Fine--Wilf gives period \(g<r\). The suffix contains a complete \(B\);
   since \(g\mid r\), \(B\) is a proper power and \(B^3\) gives exponent
   at least six at \(F\), contradicting \(\kappa(F)=3\).

3. **\(\rho=r\).** The final `3` in the \(\rho\)-cube must equal the
   symbol \(\rho\) positions earlier, namely \(B[0]=2\).

4. **\(r<\rho\le2r+g\).** The whole terminal \(B^3\) lies in the
   \(\rho\)-periodic suffix. Fine--Wilf gives period \(g\) on \(B^3\).
   If \(g<r\), \(B\) is again a proper power. If \(g=r\), then
   \(\rho\in\{2r,3r\}\), and in either case the final `3` copies the first
   symbol of one of the displayed \(B\)'s, namely `2`.

5. **\(\rho>2r+g\).** Remove the final \(B^2\) from the deleted-letter
   suffix. The remaining suffix of \(G\) is \(\rho\)-periodic and has
   length
   \[
   L_\rho=3\rho-1-2r>2\rho.
   \]
   Thus \(G\) ends in a \(\rho\)-square, and its canonical pair forces
   \(\rho\ge q\). Write \(\rho=q+u\), where \(0\le u<r\) follows from
   \(\rho<P\). If \(u>0\), then
   \[
   L_\rho-2q=q+3u-2r-1>0.
   \]
   Hence the whole terminal \(R^2\) is \((q+u)\)-periodic. Comparing its
   two copies gives
   \[
   R[0:q-u]=R[u:q],
   \]
   so \(R\) has period \(u<r<q/2\). Its final \(2u\) letters give a
   forbidden \(u\)-square at \(G\). Therefore \(u=0\).

6. **The endpoint \(\rho=q\).** The displayed suffix
   \[
   R_1R_2B_3B_4\,3
   \]
   of \(F_1\) has length \(2q+2r+1\le3q\), so it lies wholly in the
   terminal \(q\)-cube. Its \(q\)-periodicity compares
   \[
   R_2[r]=Q[0]=3
   \quad\hbox{with}\quad
   B_4[0]=B[0]=2,
   \]
   a contradiction.

It follows that \(z=2\) is impossible. Together with the existing
first-mismatch trichotomy, only \((z,h)=(1,0)\) remains on the simultaneous
boundary under the negation of either target.

## Why both target negations supply the cap

For \(\mathcal I\), the later sampled states are
\(F_\ell\) for \(0\le\ell<m\). Since \(z=2<m\), \(F_1\in\mathcal I\);
negating the conclusion gives \(\pi(F_1)<P\).

For \(\mathcal J\), every proper precompletion state is included, so the
same \(F_1\) and cap occur. No uncapped bridge state is used.

## Exact \(p<q\) seam normal form

This refinement is documentary support for the surviving row, not a
hypothesis of the branch-independent elimination.

Let

\[
d=q-p=2r+\nu,\qquad |\Theta|=\nu>0,
\]

and write the forced prefix form as

\[
Q=\Theta B^2D,\qquad \sigma=|D|=p-2r.
\]

The suffix equation
\(\operatorname{suf}_{r+\nu}(Q)=B\Theta\) has exactly two seams. Put

\[
e=\sigma-r-\nu=2p-P.
\]

- If \(e\ge0\), then
  \[
  D=JB\Theta,\qquad |J|=e.
  \]
- If \(e<0\), put \(c=-e=P-2p\). Then
  \[
  0<c<r/2,\qquad B[0:c]=B[r-c:r],\qquad
  D=B[c:r]\Theta.
  \]

The inequality \(p>q/2\) gives \(\sigma>\nu\), so define the nonempty word

\[
A=
\begin{cases}
JB,&e\ge0,\\
B[c:r],&e<0,
\end{cases}
\qquad
C=\Theta B^2,\qquad H_0=\Theta B.
\]

In both seams \(D=A\Theta\), and therefore

\[
\boxed{X=AC,\qquad U=CAH_0.}
\]

The local tail \(H_0\) is not the global completion state \(H\).

## Executable regression contract

Add an independent, definition-first bounded oracle that imports neither
production Cell C search nor the proof reductions used above.

For meaningful bounded domains in both \(p>q\) and \(p<q\), it must:

- construct binary simultaneous-boundary candidates from literal word
  identities;
- recompute every canonical pair by exhaustive exponent/period loops;
- retain both \(z=2\) rows only after the exact standalone and canonical
  endpoint filters;
- evaluate \(F_1=X^3UB^2\,3\) directly;
- pin nonzero antecedent counts and zero candidates with
  \(\kappa(F_1)=3\);
- keep row and, for \(p<q\), seam counts visible so a vacuous pass cannot
  masquerade as evidence.

The finite regression is an independent sanity check, not the proof.

Also pin the endpoint-correct \(q=23,r=4,p=13,P=27\), \(z=1\) model

\[
B=2232,\quad\Theta=32,\quad D=23232,\quad
X=2323222322232,
\]

\[
U=3222322232232322232.
\]

Its sampled local traces replay phases `0` through `12` and both fail at
phase `13`, where the request is `3` but the canonical pair is \((2,3)\).
Its role is to show that the sole remaining row is a genuinely later,
nonlocal replay obstruction, not to claim a survivor or counterexample.

## Scope discipline

This checkpoint does **not**:

- prove the surviving \((1,0)\) row impossible;
- close either full \(p>q\) or \(p<q\) word wall;
- move arbitrary Cell C instances to the simultaneous boundary;
- close Cell C or either G2CS target;
- prove the Curling Number Conjecture.
