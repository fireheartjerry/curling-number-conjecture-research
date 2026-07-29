# \(p>q,\ r=4\): closing the exit band — the period-ten collapse

Status: `PROVED-NL` (Lemmas V0, V1, the root-ten kill); `COMPUTED`
(the alignment disposition over all late exit phases and all residues
of \(q\)). Scope: Cell C simultaneous boundary, \(p>q\), row
\((z,h)=(1,0)\), \(r=4\), \(B=\texttt{2232}\); both targets. This
note eliminates the last surviving family (B.1) of
`pgtq_r4_band_kill.md` —

\[
2s=q+13,\qquad \ell^*\ge22,\qquad q\ \text{odd},
\]

in the generic regime \(q\ge2\ell^*+31\) — and with it **completes
the exit band**: no exit cube root in the band exists at any exit
phase for any generic \(q\).

## Lemma V0 — the two-occurrence period ten

The cube window contains the word \(Q\) twice: once as the reversed
\(Q\) of \(X_3\) (positions \(n+1\) to \(\ell^*+q\), depth
\(\rho=\mathrm{pos}-n\)) and once inside \(X_2\) (positions
\(\ell^*+q+12\) to \(\ell^*+2q+3\), depth
\(\rho=\mathrm{pos}-\ell^*-q-11\)). For \(2s=q+13\),

\[
n+\rho+2s=(\ell^*+q+11)+(\rho+10),
\]

so the two-hop relation \(t_{n+\rho}=t_{n+\rho+2s}\) identifies depth
\(\rho\) of the first copy with depth \(\rho+10\) of the second copy —
the same word:

\[
\boxed{Q[-\rho]=Q[-(\rho+10)]\qquad
(1\le\rho\le\min(s-n,\ q-18)).}
\tag{V.1}
\]

In the generic regime this is a long stretch: \(Q\) has period ten
from depth one.

## Lemma V1 — the shallow letters are determined

The one-hop pins \(Q[-(s-n+i)]=t_i\) (\(1\le i\le n\)) fix the ten
consecutive depths \(s-n+1,\ldots,s-n+10\) inside the period-ten
stretch. Chaining (V.1) downward, every shallow depth
\(\rho\le s-n+10\) is forced:

\[
Q[-\rho]=t_{j(\rho)},\qquad j(\rho)\in[1,10],\quad
j(\rho)\equiv\rho+n-s\pmod{10}.
\tag{V.2}
\]

Thus the entire shallow tail of \(Q\) is a rotation of the known
ten-letter word \(t_1\ldots t_{10}\) (the reversed last ten letters of
the forced tail), with rotation class \((n-s)\bmod10\), i.e.
determined by \(\ell^*\) and \(q\bmod20\).

## The alignment disposition (`COMPUTED`)

For each of the \(28\) late exit phases and each odd residue of
\(q\bmod20\) (generic regime; verified over sixty-two consecutive odd
\(q\) per phase, confirming dependence on the residue only), the full
copy-back system — both occurrences of \(Q\) identified, all known
letters of the tail, the \(232\) prefixes, and the \(B^2\) blocks of
\(X_3,X_2\) attached — was closed under union-find. The outcome is a
dichotomy with no third case:

- **Chain conflict.** Two known letters collide through the relation
  chains; the phase--residue class is impossible outright. This kills
  every class at the exit phases
  \(\ell^*\in\{33,34,35,37,38,39,54,56,57,58,60\}\) and all but one
  residue class at each remaining late phase.
- **Determined shallow \(Q\) with reversed \(B\) at depths
  \(7,8,9,10\).** In every surviving class the forced rotation places

  \[
  (Q[-7],Q[-8],Q[-9],Q[-10])=(2,3,2,2),
  \]

  and the forced shallow word is
  \(Q[-1..-10]=(2,3,2,3,2,2,2,3,2,2)\), uniformly across all
  surviving classes.

## Theorem V — the root-ten kill and the closure of the band

In a surviving class, \(R=BQB\) ends in a square of root ten: the
last twenty letters of \(R\) satisfy \(R[j]=R[j+10]\) for
\(1\le j\le10\) — positions \(j\le4\) are reversed \(B\) and match
depths \(7..10\) by the disposition, and positions \(5\le j\le10\)
compare \(Q\)-depths \(j-4\) and \(j+6\), equal by (V.1). Hence
\(\pi(R^2)\le10<q\), contradicting
\((\kappa(R^2),\pi(R^2))=(2,q)\). Together with the chain-conflict
classes, the family (B.1) is impossible everywhere. Combining with
the band theorem of `pgtq_r4_band_kill.md`:

\[
\boxed{\text{At every exit phase and every }q\ge2\ell^*+31,\
\text{the exit band is empty.}}
\tag{V.3}
\]

Item (1) of the exit residue is closed. The \(r=4\) branch of the
\(p>q\) wall now rests on exactly two items: the bounded shallow zoo
(\(q\le2\ell^*+30\le150\)) and the \(r\ge5\) catalogue.

## Non-claims

- The shallow zoo and \(r\ge5\) remain open; nothing here closes the
  \(p>q\) wall, Cell C, either G2CS target, or the conjecture.
- The alignment disposition is exact finite letter arithmetic
  (union-find over the explicit window), run across sweeps confirming
  mod-\(20\) stability; per the math-only policy no script is
  committed.
