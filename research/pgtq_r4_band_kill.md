# \(p>q,\ r=4\): the separator kill of the exit band

Status: `PROVED-NL` (Lemmas S, W, Proposition B); `COMPUTED` (the
per-phase survivor geography, exact letter arithmetic). Scope: Cell C
simultaneous boundary, \(p>q\), row \((z,h)=(1,0)\), \(r=4\),
\(B=\texttt{2232}\); both targets. This slice treats item (1) of the
residue of `pgtq_r4_exit_root_kill.md` — the early exit-cube band

\[
\frac{q-4}{2}<s<\frac{p+\ell^*-\gcd(s,p)}{2}
\]

at an exit phase \(\ell^*\) — and nothing else.

## Coordinates and the separator

State letters from the right are \(t_1,t_2,\ldots\); the tail
\(T=B^2U_f[0:\ell^*]\) occupies \(t_1..t_n\), \(n=\ell^*+8\). Beyond
the tail, \(E=X^3U_f[0:\ell^*]\) continues with reversed \(Q\)
(positions \(n+1\) to \(\ell^*+q\)), then the reversed \(232\) prefix
of \(X_3\) and the reversed terminal \(B^2\) of \(X_2\): eleven
consecutive **known** letters, the separator

\[
\mathrm{Sep}=(2,3,2,\ 2,3,2,2,2,3,2,2)
\]

at positions \(\sigma_0..\sigma_0+10\), \(\sigma_0=\ell^*+q+1\).
Parametrize the band by the offset

\[
d=\ell^*+q+1-2s,\qquad 0\le d\le\ell^*+4 ,
\]

(the lower bound from the Fine--Wilf boundary of the band, the upper
from \(2s>q-4\)). The **generic regime** is
\(q\ge2\ell^*+31\), which puts \(\sigma_0+10\le3s\) for every band
\(d\); smaller \(q\) joins the bounded shallow zoo.

## Lemma S — the separator equations

For a band exit cube, for every \(k\in[0,10]\) with
\(1\le d+k\le n\) and \(\sigma_0+k\le3s\):

\[
t_{d+k}=\mathrm{Sep}[k].
\tag{S.1}
\]

**Proof.** Two hops of the cube relation \(t_i=t_{i+s}\)
(\(i\le2s\)): from \(d+k\) (tail, known) to \(d+k+s\) (inside the
reversed \(Q\), since \(n+1\le d+k+s\le\ell^*+q\) in the band) to
\(d+k+2s=\sigma_0+k\) (separator, known). Both indices are at most
\(2s\). \(\square\)

## Proposition B — the bottom of the band dies identically

For \(d\in[\ell^*-1,\ \ell^*+4]\) (equivalently \(q-4<2s\le q+2\)),
the constrained positions \(d+k\le n\) lie in the tail's
\(B^2\)-part (or at \(t_{\ell^*}=U_f[0]=3\)), and comparing the fixed
letters of reversed \(B^2=(2,3,2,2,2,3,2,2)\) with \(\mathrm{Sep}\)
fails at an explicit \(k\le4\) for each of the six offsets:
\(d=\ell^*-1\) at \(k=3\); \(d=\ell^*\) at \(k=0\)
(\(3\ne2\)); \(d=\ell^*+1\) at \(k=4\); \(d=\ell^*+2\) at \(k=0\);
\(d=\ell^*+3\) at \(k=1\); \(d=\ell^*+4\) at \(k=1\). These clashes
are phase-independent. Hence the bottom of the band is impossible at
every exit phase (needing only \(\sigma_0+4\le3s\)).

## The survivor geography (`COMPUTED`)

Checking (S.1) against the known forced tails at all \(43\) exit
phases leaves exactly the offsets

\[
d\equiv\ell^*-12\pmod{21},\qquad d\ge0 ,
\]

reflecting the fact that the forced word itself contains the
separator: \(U_f[2:13]\) is reversed \(\mathrm{Sep}\), and the
quasi-period \(21\) repeats it. In particular the eight exit phases
\(\ell^*\in\{1,2,3,5,6,7,9,10\}\) have **no** surviving band offset at
all.

## Lemma W — the mirrored \(R\)-square kills the small offsets

Let a band cube satisfy (S.1) with \(d\le\ell^*-9\) and
\(2d\le\ell^*-4\), and put \(w=p-s\). Then \(R\) ends in a root-\(w\)
square, so \(\pi(R^2)\le w<q\): contradiction with \((2,q)\).

**Proof.** (i) *Period.* For \(w+1\le\delta\le2s-n\), the relation
\(t_{n+\delta}=t_{n+\delta+s}\) pairs the reversed-\(Q\) position of
depth \(\delta\) in \(X_3\) with the reversed-\(Q\) position of depth
\(\delta-w\) in \(X_2\) — the same word \(Q\) — so
\(Q[-\delta]=Q[-(\delta-w)]\): \(Q\) has period \(w\) there.
(ii) *B-match.* Depths \(w-3..w\) are pinned through one hop to
\(t_{d+7},t_{d+8},t_{d+9},t_{d+10}\) (the index arithmetic gives
\(n+\delta-s=d+7..d+10\) for \(\delta=w-3..w\)), and by (S.1) these
equal \(\mathrm{Sep}[7..10]=(2,3,2,2)\) — reversed \(B\).
(iii) *Square.* The last \(2w\) letters of \(R\): positions
\(j\le4\) are reversed \(B\) and match the pinned depths
\(w-3..w\) by (ii); positions \(5\le j\le w\) compare \(Q\)-depths
\(j-4\) and \(j+w-4\), covered by (i) since
\(j+w-4\le2w-4\le2s-n\iff2d\le\ell^*-4\). The square fits in \(R\)
because \(2w\le q-4\iff d\le\ell^*-9\). \(\square\)

## Theorem — the band theorem

In the generic regime, at every exit phase the entire band is
impossible except possibly the single alignment

\[
\boxed{\,d=\ell^*-12,\quad\text{i.e.}\quad 2s=q+13,\,}
\tag{B.1}
\]

and only at the \(28\) exit phases \(\ell^*\ge22\). In particular:

- **\(q\) even: the band is empty at every exit phase** (\(2s=q+13\)
  has no integer solution);
- exit phases \(\ell^*\le20\): the band is empty (survivors
  \(d=\ell^*-12-21j\ge0\) are all killed by Lemma W there);
- the surviving family has \(v=2s-p=10\): its two-hop relations force
  \(Q[-\delta]=Q[-(\delta+10)]\) on a long deep stretch together with
  a full reversed-tail pin block — a two-occurrence fixed-point system
  (the cube window contains \(Q\) twice) that is the natural next
  target.

**Proof.** Proposition B kills \(d\ge\ell^*-1\); Lemma S with the
computed geography kills every other \(d\not\equiv\ell^*-12\pmod{21}\);
Lemma W kills the surviving offsets with \(2d\le\ell^*-4\) and
\(d\le\ell^*-9\), which covers \(d=\ell^*-12-21j\) for \(j\ge1\)
always, and \(j=0\) exactly when \(\ell^*\le20\). \(\square\)

## Non-claims

- The family (B.1) at odd \(q\), exit phases \(\ell^*\ge22\), is
  restricted, not eliminated.
- The generic-regime bound \(q\ge2\ell^*+31\) leaves a bounded
  extension of the shallow zoo (\(q\le2\ell^*+30\le150\)).
- The geography table and the letter clashes are exact finite
  arithmetic, machine-cross-checked twice during drafting; no script
  is committed, per the math-only policy.
- Nothing here closes the \(p>q\) wall, Cell C, either G2CS target,
  or the conjecture.
