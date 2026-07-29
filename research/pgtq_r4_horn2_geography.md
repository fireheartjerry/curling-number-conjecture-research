# \(p>q,\ r=4\): root geography of the phase-two double cube

Status: `PROVED-NL`. Scope: Cell C simultaneous boundary, branch
\(p>q\), surviving row \((z,h)=(1,0)\), \(r=4\), \(B=\texttt{2232}\),
low phase-one case, horn 2 of the phase-two dichotomy of
`research/pgtq_r4_phase_two.md`: \(U[2]=3\), with canonical cube roots
\(\ell\ge10\) at \(E_2\) and \(\ell'\ge14\) at \(F_2\). This note
proves one theorem: the exact geography of the admissible pairs
\((\ell,\ell')\) in the deep-\(Q\) regime, with a \(q\ge66\)
consequence. Both targets, every \(q\); one replay step only.

## Depth coordinates and the deep-\(Q\) hypothesis

Write \(Q[-d]\) for the \(d\)-th letter of \(Q\) from its right end
("depth \(d\)"). The two cubes impose on \(Q\):

- period \(\ell\) on the last \(3\ell-10\) letters (early window);
- period \(\ell'\) on the last \(3\ell'-14\) letters (later window),

as long as those windows stay inside \(Q\). The **deep-\(Q\)
hypothesis** (D) is

\[
3\ell-10\le q-8
\quad\text{and}\quad
3\ell'-14\le q-8 .
\]

When (D) fails, a copy-back window collides with the left end of
\(Q\) and picks up the known letters of \(232\), \(B\), or the second
\(R\); that shallow-\(Q\) regime is deliberately left to the next
slice.

## Lemma G.1 — pinned blocks

Let \(\tau=(2,3,2,3,2,2,2,3,2,2)\) and
\(\tau'=(2,3,2,3,2,2,2,3,2,2,2,3,2,2)\) be the reversed known tails of
\(E*2\) and \(F_2\) (\(t_1..t*{10}\), resp. \(t*1..t*{14}\)). A cube
of root \(\ell\) gives \(t*i=t*{i+\ell}=t\_{i+2\ell}\) for
\(1\le i\le\ell\). Since \(\ell\ge10\) and \(\ell'\ge14\), the known
letters copy into \(Q\):

- the early cube pins \(\tau\) (as a function of depth) on the depth
  intervals \([\ell-9,\ \ell]\) and \([2\ell-9,\ 2\ell]\);
- the later cube pins \(\tau'\) on \([\ell'-13,\ \ell']\) and
  \([2\ell'-13,\ 2\ell']\).

Under (D) all four blocks lie inside \(Q\).

## Lemma G.2 — correlation tables

For two pinned blocks, let \(\sigma\) be the depth of the second
block's start minus the depth of the first block's start. Direct
letter comparison of the overlaps (finite arithmetic on \(\tau,\tau'\))
gives the complete admissible shift sets

\[
\begin{aligned}
\Delta(\tau,\tau)&=\{0,\pm9\}\cup\{|\sigma|\ge10\},\\
\Delta(\tau,\tau')&=\{0,9\}\cup\{\sigma\le-13\}\cup\{\sigma\ge10\},\\
\Delta(\tau',\tau')&=\{0\}\cup\{|\sigma|\ge13\}.
\end{aligned}
\]

Every other shift produces a direct letter conflict; note \(\pm9\) is
admissible for \(\tau\) against itself but **not** for \(\tau'\)
against itself.

## Lemma G.3 — Fine--Wilf kill

Put \(g=\gcd(\ell,\ell')\) and \(M=\min(3\ell-10,\ 3\ell'-14)\). If
\(\ell\ne\ell'\) and

\[
M\ \ge\ \ell+\ell'-g,
\]

then horn 2 is impossible. Indeed, the last \(M\) letters of \(Q\)
carry both periods, so Fine--Wilf gives them period \(g\). Since
\(M\ge\ell+\ell'-g>\max(\ell,\ell')\), this suffix contains a factor
of length \(\max(\ell,\ell')\) inside the corresponding periodic
window; that factor is a reversed conjugate of the longer canonical
cube root. It inherits period \(g\), and \(g\mid\max(\ell,\ell')\)
with \(g\le\min<\max\), so the factor is a proper power. Conjugacy and
reversal preserve primitivity, so the canonical root would be
imprimitive, contradicting \(\kappa=3\) exactly.

## Theorem G.4 — the band theorem

Assume horn 2 and (D). Then

\[
\boxed{
\ell'=2\ell+4,\quad\text{or}\quad
\ell'\ge2\ell+13,\quad\text{or}\quad
\ell=2\ell'-4,\quad\text{or}\quad
\ell\ge2\ell'+9 .}
\tag{G.4}
\]

In particular the two roots are never comparable: one exceeds twice
the other (up to the stated offsets).

**Proof.** Put \(u=\ell'-\ell\). The four cross pairs of pinned blocks
give shifts

\[
\sigma_1=u-4,\quad
\sigma_2=\ell'+u-4,\quad
\sigma_3=u-\ell-4,\quad
\sigma_4=2u-4,
\]

each of which must lie in \(\Delta(\tau,\tau')\).

- \(\sigma_1\): \(u\in\{4,13\}\cup(-\infty,-9]\cup[14,\infty)\).
- \(\sigma_4\): \(2u-4\) is even, so \(2u-4=9\) is impossible;
  \(u\in\{2\}\cup(-\infty,-5]\cup[7,\infty)\). Intersecting kills
  \(u=4\) (this is the P2.3 conflict in general form) and leaves
  \(u=13\), \(u\le-9\), or \(u\ge14\). In particular \(u=0\) is dead
  (\(\sigma_1=-4\)), so \(\ell\ne\ell'\) always.
- \(u=13\): \(\sigma_3=9-\ell\in[-12,-1]\) for \(10\le\ell\le21\),
  which is forbidden; for \(\ell\ge22\), \(M=3\ell-10\ge2\ell+13-g\)
  holds (\(\ell\ge23-g\)), so Lemma G.3 kills it. Dead for every
  \(\ell\).
- \(u\ge14\): \(\sigma_3=u-\ell-4\in\Delta(\tau,\tau')\) forces
  \(\ell'=2\ell+4\) (\(\sigma_3=0\)), \(\ell'=2\ell+13\)
  (\(\sigma_3=9\)), \(\ell'\ge2\ell+14\) (\(\sigma_3\ge10\)), or
  \(\ell'\le2\ell-9\) (\(\sigma_3\le-13\)); in the last case
  \(\ell'\le2\ell-10+g\) always holds (for \(\ell'\le2\ell-10\)
  trivially, and \(\ell'=2\ell-9\) needs only \(g\ge1\)), so Lemma
  G.3 kills it.
- \(u\le-9\): \(\sigma_3,\sigma_4\le-13\) hold automatically;
  \(\sigma_2=2\ell'-\ell-4\in\Delta(\tau,\tau')\) forces
  \(\ell=2\ell'-4\) (\(\sigma_2=0\)), \(\ell=2\ell'-13\)
  (\(\sigma_2=9\)), \(\ell\le2\ell'-14\) (\(\sigma_2\ge10\)), or
  \(\ell\ge2\ell'+9\) (\(\sigma_2\le-13\)). The middle two meet the
  Fine--Wilf threshold \(\ell\le2\ell'-14+g\) and die by Lemma G.3;
  \(\ell=2\ell'-4\) misses it because
  \(g=\gcd(\ell',4)\le4<10\).

What remains is exactly (G.4). \(\square\)

## Corollary G.5 — the deep-\(Q\) regime needs \(q\ge66\)

Under (D), the smallest band value is \(\ell'=2\ell+4\ge24\) with
\(q\ge3\ell'-6\ge66\); the bands \(\ell=2\ell'-4\),
\(\ell'\ge2\ell+13\), \(\ell\ge2\ell'+9\) need \(q\ge70\), \(93\),
\(109\) respectively. Hence

\[
\boxed{q\le65\ \Longrightarrow\ \text{horn 2 forces a window--edge
collision (shallow-}Q\text{ regime).}}
\tag{G.5}
\]

## Sharpness

The band theorem is complete for its toolset: a mechanical
constraint-propagation check of the full copy-back systems of both
cubes (union-find over all \(t*i=t*{i+\ell}\) relations, \(Q\)
unbounded to the left) over \(10\le\ell\le160\), \(14\le\ell'\le160\)
returns exactly \(8204\) consistent Fine--Wilf-missing pairs, all of
them in (G.4) and covering it. No further pair can be eliminated by
pin consistency and Fine--Wilf alone; killing the bands requires new
ingredients (deeper phases, the shallow-\(Q\) edge letters, or the
endpoint scales).

## Non-claims

- The shallow-\(Q\) regime (window--edge collision, in particular
  every \(q\le65\)) is not analyzed here; it is the next slice.
- The four bands are restricted, not eliminated; horn 2 survives in
  them at this depth of analysis.
- The mechanical sharpness check was a drafting aid, not a repository
  artifact, per the proof-first policy.
- Nothing here closes the \(p>q\) wall, Cell C, either G2CS target,
  or the conjecture.
