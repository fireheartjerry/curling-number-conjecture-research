# Cell C surviving-row transition atlas

**Date:** 2026-07-27
**Status sought:** exact `PROVED-NL` transition reductions plus a
definition-first `COMPUTED` atlas. Cell C remains `OPEN`.

## Objective

Characterize the sole simultaneous-boundary first-mismatch row

\[
(z,h)=(1,0),\qquad U[0:2]=32,\qquad X[0]=2
\]

without claiming that either target-specific word wall is closed. The
checkpoint must distinguish theorem-level consequences from bounded binary
evidence and must preserve the different scopes of \(\mathcal I\) and
\(\mathcal J\).

## Exact state contract

Retain

\[
q>2r>0,\qquad P=q+r,\qquad R=BQB,\qquad U=QB,
\]

\[
B[0]=2,\qquad Q[0]=3,
\]

and the localized states

\[
E_\ell=X^3U[0:\ell],\qquad
F_\ell=X^3UB^2U[0:\ell].
\]

Their phase-zero pairs are

\[
(\kappa(E_0),\pi(E_0))=(3,p),\qquad
(\kappa(F_0),\pi(F_0))=(3,r).
\]

Under the negation of either target, the sampled phase-one states have

\[
(\kappa(E_1),\pi(E_1))=(2,\alpha),\qquad
(\kappa(F_1),\pi(F_1))=(2,\beta),\qquad
\alpha,\beta<P.
\]

The executable atlas also retains the exact standalone filters
\((2,q)\) at \(R^2\), label `2` at \(R^2B\), pair \((3,r)\) at
\(BRB^2\), and the exact local endpoint words.

## Theorem-level transition reductions

The following statements may be labeled `PROVED-NL`.

### Phase-one pop and dichotomy

The appended `3` disagrees with the next symbols of both old cubes:
\(X[0]=B[0]=2\). All-continuation localization puts the
\(\alpha\)-square in \(X^3\,3\). If \(\alpha>p\), adjacent-root separation
would give \(\alpha>2p+\gcd(p,\alpha)\), hence
\(2\alpha>4p+2>|X^3\,3|=3p+1\), impossible. Thus

\[
\alpha<p,\qquad
p\ge\alpha+\gcd(p,\alpha).
\]

At \(F_0\to F_1\), equality \(\beta=r\) is impossible and adjacent-root
separation gives exactly

\[
\boxed{
\begin{array}{ll}
\beta<r:&r\ge\beta+\gcd(r,\beta),\\
\beta>r:&\beta>2r+\gcd(r,\beta).
\end{array}}
\]

Both states end in the common suffix

\[
T_1=B^2\,3,\qquad |T_1|=2r+1.
\]

If either canonical square fits in \(T_1\), it is a square in both states.
Least-root minimality in both directions then proves

\[
\boxed{
\min(\alpha,\beta)\le r
\Longrightarrow
\alpha=\beta<r.
}
\]

Otherwise both roots exceed \(r\). For \(r=1\), \(T_1=223\) has no square,
so only this context-crossing alternative is possible.

In the low case, writing \(s=\alpha=\beta\), the exact terminal square is

\[
\operatorname{suf}_{2s}(B^2\,3)
  =(B[r-s+1:r]\,3)^2,\qquad B[r-s]=3,
\]

and both adjacent transitions add

\[
r\ge s+\gcd(r,s),\qquad
p\ge s+\gcd(p,s).
\]

### High-\(\beta\) restriction

In the high alternative,

\[
2r+\gcd(r,\beta)<\beta<P.
\]

The endpoint \(\beta=q\) is impossible: the terminal \(q\)-square at
\(F_1\) equates \(R_2[r]=Q[0]=3\) with \(B_4[0]=B[0]=2\).

The range \(\beta=q+w\), \(0<w<r\), is also impossible. Copying
\(T_1=B^2\,3\) left by \(q+w\) inside \(R_1R_2\) gives

\[
R[q-w:q]R[0:|T_1|-w]=B^2\,3.
\]

Its first \(w\) positions give \(B[-w:]=B[:w]\), and its next \(r\)
positions give

\[
B=B[w:]B[:w].
\]

Thus \(B\) is fixed by a nontrivial rotation and is a proper power,
contradicting \(\kappa(F_0)=3\). Hence

\[
\boxed{2r+\gcd(r,\beta)<\beta<q}
\]

in the high alternative. With \(v=P-\beta\), the copied \(T_1\)-return
satisfies

\[
1\le v\le m-\gcd(r,\beta)-1
\]

and

\[
\operatorname{suf}_{2\beta}(R^2B^2\,3)
  =(R[r+v+1:q]B^2\,3)^2,\qquad R[r+v]=3.
\]

Deleting the final \(B\,3\) leaves a \(\beta\)-periodic suffix of
\(K=R^2B=B(UB)^2\) of length \(L=2\beta-r-1\). Put
\(d_\beta=\gcd(\beta,q)\). If \(d_\beta=\beta\), then
\(\beta\mid q\) and \(\beta<q\), so \(q\ge2\beta\) and
\(L<2\beta\le q=\beta+q-d_\beta\); the threshold misses automatically.
If \(d_\beta<\beta\) and the threshold were attained, Fine--Wilf would
give the whole shorter common suffix period \(d_\beta\). On the
length-\(L\) side, attainment gives \(L>\beta\), so the remaining initial
segment of the canonical \(\beta\)-square contains its complete first
primitive root and makes it imprimitive. On the length-\(2q\) side, the
common suffix is the whole displayed \(q\)-square, so its primitive root
\(UB\) becomes imprimitive. Hence Fine--Wilf must miss:

\[
\boxed{\min(L,2q)<\beta+q-d_\beta.}
\]

Equivalently,

\[
2v\ge r-1\Longrightarrow v\ge d_\beta,\qquad
2v<r-1\Longrightarrow v<r-d_\beta.
\]

These are restrictions, not an elimination of the high branch.

### Differing paired roots

At any paired sampled phase \(\ell\), suppose both states have the
requested label \(k_\ell\in\{2,3\}\), with canonical roots
\(a_\ell\ne b_\ell\). They share the suffix

\[
T_\ell=B^2U[0:\ell],\qquad |T_\ell|=2r+\ell.
\]

If either full canonical power lay inside \(T_\ell\), the same maximizing
power would occur in both states and least-root minimality would force the
roots equal. Therefore

\[
\boxed{
k_\ell\min(a_\ell,b_\ell)>2r+\ell.
}
\]

This inequality permits later context-crossing divergence; it does not
force synchronized roots or synchronized failures.

### Endpoint and midpoint scope

Suppose the paired roots remain equal through phase \(m-1\), write their
common predecessor root as \(s<P\), and put \(k=B[-1]\). Adjacent-root
separation gives the exact endpoint-only classification:

\[
\begin{array}{c|l}
k=3&
s<q,\quad q>2s+\gcd(s,q),\quad
P>2s+\gcd(s,P),\\[1mm]
k=2,\ s<q&
q>s+\gcd(s,q),\quad P>s+\gcd(s,P),\\[1mm]
k=2,\ s=q&
\text{the early root extends and the later root pushes, with }
r>\gcd(q,r),\\[1mm]
k=2,\ q<s<P&
s\ge q+\gcd(s,q),\quad P>s+\gcd(s,P).
\end{array}
\]

The atlas records predecessor pairs even when the roots have already
diverged; an exact endpoint alone does not force a valid predecessor
transition.

The true bridge midpoint

\[
M=LR^2B
\]

is omitted from \(\mathcal I\), but it acquires a cap directly. Its suffix

\[
K=R^2B=B(UB)^2
\]

has standalone label `2` and displays the \(q\)-square \((UB)^2\). If
\((2,c)\) is the global canonical pair at \(M\), suffix persistence and
canonical minimality give

\[
c\le\pi(K)\le q<P.
\]

The all-continuation localization lemma therefore applies at \(M\) even
under the \(\mathcal I\)-negation. Under \(\mathcal J\), every proper bridge
state is capped already. This midpoint fact does not cap arbitrary
interior bridge states under \(\mathcal I\).

For \(0<i<r\), write the cyclic cut \(B=AD\), \(|A|=i\). The bridge word
satisfies the literal identity

\[
B^2B[0:i]=ADAD A=A(DA)^2.
\]

When the requested bridge symbol is \(B[i]=2\), the displayed square gives
a root at most \(r\), so the actual pair has period below \(P\) and
localizes under \(\mathcal I\). When \(B[i]=3\), this identity alone gives
no converse, no fixed canonical root, and no fixed bridge profile.

## Exact \(p<q\) return atlas

Use the existing seams

\[
X=AC,\qquad U=CAH_0,
\]

where \(C=\Theta B^2\), \(H_0=\Theta B\), and

\[
A=JB\quad(e\ge0),\qquad
A=B[c:r]\quad(e<0).
\]

For a high \(\beta<q\), put \(m=q-r\). The copied common suffix has one of
the exact forms

\[
\begin{array}{ll}
\beta\le m:&U[m-\beta:m-\beta+|T_1|]=T_1,\\
m<\beta<q:&
B[r-\delta:r]U[0:|T_1|-\delta]=T_1,\quad
\delta=\beta-m.
\end{array}
\]

For \(r<\alpha<|T_1|\), writing \(\alpha=r+a\) forces \(B\) to have
period \(a\), with \(B[r-a]=3\) and \(r/2<a<r\). For
\(\alpha\ge|T_1|\), put \(\sigma=p-2r\). Its return is

\[
\begin{array}{ll}
\alpha\le\sigma:&
X[\sigma-\alpha:\sigma-\alpha+|T_1|]=T_1,\\
\alpha>\sigma:&
X[p-\delta_\alpha:p]X[0:|T_1|-\delta_\alpha]=T_1,\quad
\delta_\alpha=\alpha-\sigma.
\end{array}
\]

Here \(T_1\) has no period \(\Delta\le r\): for \(\Delta<r\), comparison
at indices \(r-\Delta\) and \(2r-\Delta\) would equate
\(B[r-\Delta]\) first with \(B[0]=2\) and then with the final `3`; the
case \(\Delta=r\) compares \(B[0]\) directly with that `3`. The endpoint
\(\Delta=2r\) compares \(T_1[0]=2\) directly with \(T_1[2r]=3\).
Thus every proper period of \(T_1\) has the form
\(\Delta=r+a\), \(1\le a<r\). Its comparisons make \(B\) period \(a\)
and give \(B[r-a]=3\). If \(2a\le r\), the final \(2a\) symbols of \(B\)
form an \(a\)-square at \(G\), forcing \(\pi(G)\le a<r<q\). Therefore
\(a>r/2\).

These formulas expose the remaining finite-word wall. They do not prove
that the high case is impossible.

## Executable atlas contract

Create one standalone scanner that imports neither production Cell C
search. It must:

- enumerate both exact branch normal forms over the binary alphabet;
- recompute every canonical pair by literal suffix-block enumeration;
- retain the exact \(z=1\) static row;
- count the phase-one label/pair split, replay-failure phases, first
  post-phase-zero root divergence, endpoint pairs, predecessor labels,
  \(p<q\) seams, and the \(r=1\) exception;
- render counters in a deterministic sorted form;
- emit a reproducible \(q\le25\) artifact labeled `COMPUTED`;
- expose small-bound summaries for an independent test-side reference;
- audit fixed certificates for \(q=8,9,11,16,23,29\).

The \(q=8\), \(q=11\), and \(q=16\) words refute overstrong equality,
synchronized-failure, and persistent-locality claims. The \(q=9\) word is
an endpoint-correct \(r=1\) high model; \(q=23\) is the overlap-seam long
replay; and \(q=29\) is a high-\(\beta\) static model. None is a survivor or
counterexample to the conjecture.

## Scope discipline

This checkpoint does **not**:

- eliminate the high phase-one alternative;
- eliminate the \(r=1\) family;
- force paired roots to remain equal after phase one;
- force synchronized replay failures;
- give a fixed canonical profile for bridge positions labeled `3`;
- close either \(\mathcal I\)- or \(\mathcal J\)-word wall;
- move non-boundary Cell C instances to the boundary;
- close Cell C, either G2CS target, or the Curling Number Conjecture.
