# \(p>q,\ r=4\): the terminal-square sieve and the phase-two dichotomy

Status: `PROVED-NL`. Scope: Cell C simultaneous boundary, branch
\(p>q\), surviving row \((z,h)=(1,0)\), bridge \(r=4\), where PB.4 of
`research/pgtq_boundary_small_r.md` forces \(B=\texttt{2232}\),
\(t=3\), \(p=q+3\), \(P=q+4\), \(X=232\,Q\,B^2\), \(U=QB\),
\(m=q-4\), \(|Q|=q-8\ge1\), \(Q[0]=3\), and \(Q[1]=2\) when
\(|Q|\ge2\). Every claim holds for every \(q\) and under the negation
of either target; only the inherited standalone conditions and paired
generation are used. This note treats **one** replay step — phase two
of the low case — and nothing else.

Notation: for a state \(S\), write its letters from the right as
\(t_1,t_2,t_3,\ldots\), so \(t_1\) is the last letter. A canonical cube
with root length \(\ell\) forces the copy-back system

\[
t*i=t*{i+\ell}\qquad(1\le i\le 2\ell).
\tag{P2.0}
\]

## P2.1 — terminal-square sieve on \(R\)

\(R=BQB\) ends in \(w_2\,w_1\,2232\), where \(w_1,w_2\) are the two
letters preceding the final \(B\) (namely \(Q[-1],Q[-2]\) when
\(|Q|\ge2\), and \(Q[-1]=Q\), \(w_2=B[3]=2\) when \(|Q|=1\)).

**(a) \((w_2,w_1)=(2,3)\) is impossible.** The last six letters of
\(R\) would be

\[
2\,3\,2\,2\,3\,2=(232)^2 .
\]

Since \(R^2\) ends in \(R\) and \(\kappa(R^2)=2\) exactly, the
canonical root of \(R^2\) would be at most \(3<q\), contradicting the
inherited condition \((\kappa(R^2),\pi(R^2))=(2,q)\).

Consequences: \(Q\) never ends in \(23\); and \(|Q|=1\) is impossible,
because \(Q=(3)\) gives \((w_2,w_1)=(2,3)\). Hence

\[
\boxed{|Q|\ge2,\qquad q\ge10,\qquad (Q[-2],Q[-1])\ne(2,3).}
\tag{P2.1a}
\]

**(b) \(Q\) cannot end in \(B=\texttt{2232}\).** The last eight
letters of \(R\) would be \(B^2\), an \(r\)-square, so
\(\pi(R^2)\le4<q\), the same contradiction. (For \(|Q|\le3\) the four
letters preceding the final \(B\) include letters of the leading
\(B\) and are never \(2232\); checked directly.)

\[
\boxed{Q\text{ does not end in }\texttt{2232}.}
\tag{P2.1b}
\]

## P2.2 — the phase-two dichotomy in the low case

Assume the low branch of PB.7c: both phase-one pairs are \((2,2)\).
The two phase-two states are

\[
E_2=X^3\,32,\qquad F_2=X^3UB^2\,32,
\]

and paired generation requires \(\kappa(E_2)=\kappa(F_2)=U[2]\).
Their shared right end is \(B^2\,32\); in \(t\)-coordinates

\[
(t*1,\ldots,t*{10})=(2,3,2,3,2,2,2,3,2,2),
\]

after which \(E_2\) continues into \(Q[-1],Q[-2],\ldots\) while
\(F_2\) continues into the final \(B\) of \(R^2\) and then \(Q\):

\[
E*2:\ t*{10+k}=Q[-k];\qquad
F*2:\ (t*{11},\ldots,t*{14})=(2,3,2,2),\quad t*{14+k}=Q[-k].
\]

**Horn 1 (\(U[2]=2\)).** Root \(1\) is not a square
(\(t_1\ne t_2\)); root \(2\) is the square \((32)^2\)
(\(t_1=t_3\), \(t_2=t_4\)) of exponent exactly two
(\(t_4=3\ne2=t_6\)). Hence if \(\kappa=2\), the canonical pair of both
windows is exactly

\[
\boxed{(\kappa,\pi)(E_2)=(\kappa,\pi)(F_2)=(2,2).}
\tag{P2.2a}
\]

**Horn 2 (\(U[2]=3\)).** This needs \(|Q|\ge3\) and \(Q[2]=3\)
(\(|Q|=2\) gives \(U[2]=B[0]=2\)). Both windows must end in canonical
cubes; let their roots be \(\ell\) (early) and \(\ell'\) (later).
Applying (P2.0) to the displayed tails:

- \(\ell\le8\) is impossible: the system already fails on the known
  letters, at \((i,\ell)\) mismatch pairs
  \(t*1\ne t_2\), \(t_4\ne t_6\), \(t_1\ne t_4\), \(t_2\ne t_6\),
  \(t_2\ne t_7\), \(t_4\ne t*{10}\), \(t*2\ne t_9\),
  \(t_2\ne t*{10}\) for \(\ell=1,\ldots,8\).
- \(\ell=9\) forces \(t*2=t*{11}\), \(t*3=t*{12}\), i.e.
  \((Q[-2],Q[-1])=(2,3)\), which (P2.1a) forbids.
- \(\ell=10\) forces, through the full system (P2.0), the twenty
  letters

  \[
  Q[-20:]=(B^2\,32)^2=(2232223232)^2,
  \]

  so in particular \(q\ge28\), and \((Q[-2],Q[-1])=(3,2)\), which the
  sieve permits.

- On the later side, \(\ell'\le8\) fails exactly as above (the shared
  ten letters), and \(\ell'=9,10,11,12\) fail against the final
  \(B\) of \(R^2\): \(t*2\ne t*{11}\), \(t*4\ne t*{14}\),
  \(t*2\ne t*{13}\), \(t*2\ne t*{14}\).
- \(\ell'=13\) forces \((Q[-2],Q[-1])=(2,3)\), forbidden by (P2.1a).
- \(\ell'=14\) forces the twenty-eight letters

  \[
  Q[-28:]=(B^3\,32)^2=(22322232223232)^2,
  \]

  so in particular \(q\ge36\).

Hence

\[
\boxed{U[2]=3\ \Longrightarrow\ \ell\ge10\ \text{and}\ \ell'\ge14.}
\tag{P2.2b}
\]

## P2.3 — the minimal horn-2 pair is inconsistent

If \(\ell=10\) and \(\ell'=14\) held together, \(Q[-20:]\) would be
\((B^232)^2\) while the last twenty letters of \((B^332)^2\) are
\(223232\,B^332\). These disagree at \(Q[-16]\):

\[
(B^232)^2[0:6]=223222,\qquad
(223232\,B^332)[0:6]=223232,
\]

i.e. \(Q[-16]=2\) from the early cube and \(Q[-16]=3\) from the later
cube. Therefore

\[
\boxed{(\ell,\ell')=(10,14)\text{ is impossible.}}
\tag{P2.3}
\]

The surviving horn-2 configurations need \(\ell\ge10\), \(\ell'\ge14\),
\((\ell,\ell')\ne(10,14)\), with both copy-back systems consistent on
\(Q\)'s tail simultaneously; each system makes a long suffix of \(Q\)
\(\ell\)- resp. \(\ell'\)-periodic, so the natural next slice is a
Fine--Wilf compatibility argument on that shared suffix.

## Summary of the slice

In the low case at \(r=4\), for every \(q\): either the replay opens
\(U[0:3]=322\) with exact phase-two pairs \((2,2)\) in both windows, or
\(U[2]=3\) and both windows carry context-crossing cubes with
\(\ell\ge10,\ \ell'\ge14\), \((\ell,\ell')\ne(10,14)\), whose copy-back
systems dictate long forced suffixes of \(Q\). Additionally, for the
whole \(r=4\) branch (independent of the low case): \(q\ge10\), \(Q\)
never ends in \(23\), and \(Q\) never ends in \(B\).

## Non-claims

- Phase three and beyond are not treated; the high phase-one branch is
  not treated; horn 2 is restricted, not eliminated.
- The letter tables in P2.2 are finite letter arithmetic; they were
  cross-checked mechanically during drafting, but no census script or
  test is attached, per the proof-first policy.
- Nothing here closes the \(p>q\) wall, Cell C, either G2CS target, or
  the conjecture.
