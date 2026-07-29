# \(p>q,\ r=4\): killing the exit cubes — the \(R\)-square theorem

Status: `PROVED-NL` (Theorem R, Lemma M's forcing step, Lemma F);
`COMPUTED` (the finite Lemma M disposition table, exact letter
arithmetic). Scope: Cell C simultaneous boundary, \(p>q\), row
\((z,h)=(1,0)\), \(r=4\), \(B=\texttt{2232}\); both targets, every
\(q\). Builds on the forced-replay theorem
(`pgtq_r4_forced_replay.md`): at the exit phase \(\ell^*\) the tail
\(T=B^2U_f[0:\ell^*]\) is the known forced word, \(n=|T|=8+\ell^*\),
and the early window \(E=X^3U_f[0:\ell^*]\) ends in a window-crossing
canonical cube of root \(s\) (\(3s>n\)), \(s<P\). Letters of the state
from the right are \(t_1,t_2,\ldots\); \(t_p\) for \(p\le n\) is the
reversed tail, and \(t_{n+d}=Q[-d]\) for \(1\le d\le q-8\).

## Theorem R — the \(R\)-square kill

If the early exit cube has root \(s\) with

\[
\ell^*+4\ \le\ s\ \le\ \frac{q-4}{2},
\]

then \(R\) ends in a root-\(s\) square, so \(\pi(R^2)\le s<q\),
contradicting \((\kappa(R^2),\pi(R^2))=(2,q)\). **No such exit root
exists.**

**Proof.** Write \(R=BQB\) with letters from the right \(r_j\): for
\(j\le4\), \(r_j\) is reversed \(B\), i.e. \((2,3,2,2)\); for
\(4<j\le q-4\), \(r_j=Q[-(j-4)]=t_{n+j-4}\). Since
\(2s\le q-4\), every index below stays in these two zones. The cube
gives

\[
t_p=t_{p+s}\qquad(1\le p\le2s).
\tag{R.1}
\]

We claim \(r_j=r_{j+s}\) for \(1\le j\le s\), i.e. the last \(2s\)
letters of \(R\) form a square.

_Case \(5\le j\le s\)._ Both sides are \(Q\)-letters:
\(r_j=t_{n+j-4}\) and \(r_{j+s}=t_{n+j-4+s}\). Apply (R.1) at
\(p=n+j-4\); admissible because
\(n+j-4\le n+s-4\le2s\iff s\ge n-4=\ell^*+4\), which is the
hypothesis. The deepest letter touched is \(Q[-(j+s-4)]\) with
\(j+s-4\le2s-4\le q-8\), inside \(Q\).

_Case \(1\le j\le4\)._ Here \(r_{j+s}=t_{n+j-4+s}\). Apply (R.1)
at \(p=n+j-4\le n\); this is admissible because
\(s\ge\ell^*+4=n-4\) gives \(2s\ge2n-8\ge n\ge n+j-4\) (using
\(n\ge9\) and \(j\le4\)). Hence \(r_{j+s}=t_{n+j-4}\). But
\(t_{n-3},t_{n-2},t_{n-1},t_n\) are the four leftmost tail letters
read right-to-left, and the tail begins with
\(B^2=\texttt{2232}\ldots\), so
\((t_{n-3},t_{n-2},t_{n-1},t_n)=(2,3,2,2)\) — exactly reversed
\(B=(r_1,r_2,r_3,r_4)\). Hence \(r_{j+s}=r_j\). \(\square\)

No deep-window hypothesis is used: every relation invoked has
\(p\le2s\), and every letter lies in the tail or in \(Q\). The
argument needs only \(q\ge2s+4\), which is the upper hypothesis.

## Lemma M — short roots force a tail period, and all die

If \(s\le\ell^*+7=n-1\), then the pairs \((p,p+s)\) with
\(p+s\le n\) are all admissible in (R.1) — the crossing condition
\(3s>n\) gives \(n-s<2s\) — so **the known tail \(T\) must have
period \(s\)**, and by chaining (R.1), the letters
\(Q[-d]\) for \(1\le d\le3s-n\) are pinned to the \(s\)-periodic
extension of \(T\) (valid inside \(Q\), i.e. when \(q\ge3s-\ell^*\);
smaller \(q\) is the shallow regime, deferred).

The periods of the \(43\) forced exit tails in the crossing range
\(((n)/3,\ n-1]\) form a finite list: exactly \(118\) pairs
\((\ell^*,s)\), reflecting the near-period-\(21\) self-similarity of
the forced word (\(s\in\{9,10,13,14,17,20,21,24,25,30,31,34,35,38,
41,42,45,46,51,52,55,56,59,64,65\}\)). Their complete disposition
(`COMPUTED`, exact letter arithmetic on pinned values):

- \(45\) pairs force \((Q[-2],Q[-1])=(2,3)\) — dead by the sieve
  (P2.1a);
- \(51\) pairs force \(Q\) to end in \(B=\texttt{2232}\) — dead by
  the sieve (P2.1b);
- \(11\) pairs have \(s\ge\ell^*+4\) — dead by Theorem R (its
  \(q\)-condition \(q\ge2s+4\) is implied by the deep condition
  \(q\ge3s-\ell^*\));
- the remaining \(9\) pairs,
  \((\ell^*,s)\in\{(7,10),(9,10),(10,10),(28,31),(30,31),(31,31),
  (49,52),(51,52),(52,52)\}\), pin \(R\)'s tail to an explicit word
  ending in a terminal square of root \(6\) (root \(21\) also appears
  at \(s=52\)), so \(\pi(R^2)\le6<q\) — dead.

**Correction (2026-07-29).** Two of the pairs originally counted
under the second bullet, \((\ell^*,s)=(52,21)\) and \((54,21)\),
have valid pin depth \(3s-n\) equal to \(3\) and \(1\)
respectively, which is below the depth \(4\) needed for the
\(B\)-tail sieve; their original kills were invalid. They are the
only such rows (re-audited mechanically over the full table with
the corrected validity bound). These two pairs — the exit cube
riding the quasi-period \(21\) of the forced word at the last two
\(21\)-periodic exit phases — are **open at this stage for every**
\(q\) and are carried forward as the *period-21 exit family*;
the shallow-zoo closure eliminates them for \(q\le150\).

Hence every short exit root except the period-21 family is
impossible in the deep regime.

## Lemma F — huge roots die by Fine--Wilf and primitivity

Let \(g=\gcd(s,p)\).

1. \(s=p\) is impossible: the cube would give
   \(t_{\ell^*}=t_{\ell^*+p}\), i.e. \(U_f[0]=3\) equal to
   \(X[0]=2\).
2. If \(2s\ge p+\ell^*-g\) and \(s<p\): the window portion inside
   \(X^3\) (positions \(\ell^*+1\) to \(3s\)) has length
   \(3s-\ell^*\ge s+p-g\) and periods \(s\) and \(p\), so Fine--Wilf
   gives it period \(g\); it contains \(p\) consecutive letters, a
   reversed conjugate of \(X\), which then has period \(g\mid p\)
   with \(g\le s<p\) — a proper power. Conjugacy and reversal
   preserve primitivity, contradicting the primitivity of \(X\).
   **Dead.**

## Corollary — the exit residue

At every exit phase \(\ell^*\), the early exit-cube root is confined
to

\[
\boxed{
\frac{q-4}{2}\ <\ s\ <\ \frac{p+\ell^*-\gcd(s,p)}{2}
}
\tag{X.1}
\]

— a band of width less than \((\ell^*+7)/2\) just above \(q/2\) —
apart from the **shallow leftovers**: short-root pairs from Lemma M's
list in the finitely many cases \(q<3s-\ell^*\) (all with
\(q\le2\ell^*+20\le140\)), where the pinned window collides with the
left end of \(Q\). Every deep exit configuration is dead. Since an
exit requires crossing cubes in **both** windows and the kills above
use the early window alone, each exit phase dies entirely once its
early residue is empty; the later window admits an exactly analogous
Theorem R (with \(n\) replaced by \(n+4\) and the same reversed-\(B\)
match), which will further constrain (X.1).

Together with the forced-replay theorem, the entire \(r=4\) branch now
rests on: (i) the band (X.1) at the \(43\) exit phases, (ii) the
bounded shallow zoo \(q\le140\), and (iii) \(r\ge5\).

## Non-claims

- The band (X.1) and the shallow zoo are restricted, not eliminated.
- The Lemma M table is exact finite arithmetic verified mechanically
  during drafting (two independent scans); per the math-only policy no
  script is committed.
- Nothing here closes the \(p>q\) wall, Cell C, either G2CS target,
  or the conjecture.
