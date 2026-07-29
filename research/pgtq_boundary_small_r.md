# Synthetic small-\(r\) structure of the \(p>q\) boundary bridge word

Status: lemmas `PROVED-NL`; per-\(r\) catalogues `COMPUTED` (complete for
every \(q\) at each fixed \(r\)). Scope: Cell C, simultaneous boundary
\(b=j=r\), branch \(p>q\), surviving row \((z,h)=(1,0)\). Every hypothesis
below follows from the negation of **either** synchronization target
(G2CS-\(\mathcal I\) or G2CS-\(\mathcal J\)); no bridge-interior cap is
used except where explicitly flagged in PB.6. Nothing here closes the
\(p>q\) word wall.

## Inherited constraint set

Fix the boundary normal form of
`research/generated_two_cube_cells.md`:

\[
R=BQB,\quad T=B,\quad U=QB,\quad q>2r,\quad
p=q+t,\quad r/2<t<r,\quad X=B[r-t:r]\,U\,B,
\]

and write

\[
a=r-t=P-p,\qquad 1\le a<r/2,\qquad
\lambda=\text{length of the terminal run of \(3\)'s in }B.
\]

The following six conditions on the bridge word \(B\in\{2,3\}^r\) are
already proved there; each is a consequence of the negation of either
target.

- **(S1)** \(B[0]=2\) and \(Q[0]=3\) (boundary normal form).
- **(S2)** \(t\) is a period of \(B\): \(B[0:a]=B[t:r]\) (C.18).
- **(S3)** \(B[a]=X[0]=2\) (C.19 with the surviving row of C.35).
- **(S4)** \(B\) is primitive (else the terminal \(B^3\) at \(F\) makes
  \(\kappa(F)>3\)).
- **(S5)** \(B\) has no period \(\delta\le r/2\) (else \(B\), hence
  \(G\), ends in a \(\delta\)-square, contradicting \(\pi(G)=q\)).
- **(S6)** \(\lambda\le1\) (C.33 with \(z=1\)).

## PB.1 — the branch forces \(r\ge3\)

(S2) requires an integer \(t\) with \(r/2<t<r\). For \(r\in\{1,2\}\) that
open interval contains no integer. Hence \(r\ge3\); in particular the
\(r=1\) family, which dominates the \(p<q\) branch, is void here. This
matches `pgtq.r1_static_candidates=0` in the \(z=1\) atlas.

## PB.2 — terminal-run transfer through the border

From (S2), \(B[t+i]=B[i]\) for \(0\le i<a\). Taking \(i=a-1\) gives

\[
\boxed{B[r-1]=B[a-1].}
\tag{PB.2a}
\]

Consequently:

1. If \(a=1\), then \(B[r-1]=B[0]=2\), so \(\lambda=0\).
2. If \(\lambda=1\), then \(B[a-1]=B[r-1]=3\); since \(B[0]=2\) this
   forces \(a\ge2\). Taking \(i=a-2\) in (S2) gives
   \(B[a-2]=B[r-2]=2\) (the run has length exactly one), so with (S3)

   \[
   B[a-2:a+1]=232.
   \]

3. If \(\lambda=1\), then \(a\ge2\) gives \(t=r-a\le r-2\), and
   \(t>r/2\) forces \(r/2<r-2\), i.e.

   \[
   \boxed{\lambda=1\ \Longrightarrow\ r\ge5.}
   \tag{PB.2b}
   \]

In particular the D-035 full-root seam (which requires \(\lambda=1\),
\(i=r-1\), \(Q[-1]=B[-1]=3\)) is impossible in the \(p>q\) branch for
\(r\le4\).

## PB.3 — \(r=3\) is impossible

\(r=3\) forces \(t=2\), \(a=1\). Then (S2) gives \(B[2]=B[0]=2\) and
(S3) gives \(B[1]=2\), so \(B=222\), contradicting (S4) and (S5).

\[
\boxed{r\ne3.}
\tag{PB.3}
\]

The sharp \(q=9,r=3,t=2\) endpoint model with \(B=232\) is consistent:
it has \(B[a]=B[1]=3\), which is exactly the (S3) violation already
recorded for it in the cell ledger.

## PB.4 — \(r=4\) forces \(B=2232\)

\(r=4\) forces \(t=3\), \(a=1\). Then (S2) gives \(B[3]=B[0]=2\) and
(S3) gives \(B[1]=2\), so \(B=2\,2\,x\,2\) with \(x\in\{2,3\}\). Period
\(2\) holds iff \(B[0]=B[2]\) and \(B[1]=B[3]\), i.e. iff \(x=2\);
period \(1\) also needs \(x=2\). (S5) excludes both, so \(x=3\):

\[
\boxed{r=4\ \Longrightarrow\ (t,B)=(3,\texttt{2232}),\quad\lambda=0.}
\tag{PB.4}
\]

This turns the bounded observation "every complete \(p>q\) replay has
\(r=4,\ B=\texttt{2232}\)" into a synthetic necessity at \(r=4\), valid
for every \(q\): there is no other admissible \(r=4\) bridge word.

## PB.5 — the complete \(r=5\) catalogue

\(r=5\) allows \(t\in\{3,4\}\).

- \(t=3,\ a=2\): (S2) gives \(B[3:5]=B[0:2]\), (S3) gives \(B[2]=2\),
  so \(B=2\,y\,2\,2\,y\). Periods \(1\) and \(2\) each hold iff
  \(y=2\); (S5) forces \(y=3\). Catalogue entry \(B=\texttt{23223}\),
  with \(\lambda=1\) and \(a=2\), as PB.2 requires.
- \(t=4,\ a=1\): (S2) gives \(B[4]=2\), (S3) gives \(B[1]=2\), so
  \(B=2\,2\,x\,y\,2\). Periods \(1\) and \(2\) each hold iff
  \(x=y=2\); (S5) excludes exactly that. Catalogue entries
  \(B\in\{\texttt{22232},\texttt{22322},\texttt{22332}\}\), all with
  \(\lambda=0\).

\[
\boxed{r=5\ \Longrightarrow\
B\in\{\texttt{23223},\texttt{22232},\texttt{22322},\texttt{22332}\}.}
\tag{PB.5}
\]

The catalogue is keyed by \((r,t)\): a single word may qualify under two
values of \(t\) (e.g. \(\texttt{22322}\) has periods \(3\) and \(4\),
but qualifies only at \(t=4\), since \(t=3\) would need
\(B[2]=2\)).

## PB.6 — exact \(r=4\) bridge-cut atlas

Let \(r=4\), \(B=\texttt{2232}\), and let
\(G_i=LR^2B[0:i]\), \(M_i=LR^2B\,B[0:i]\) be the bridge cuts, with the
actual-generation labels \(\kappa(G_i)=\kappa(M_i)=B[i]\). A suffix
\(\ell\)-square is determined by the last \(2\ell\) symbols, and for
every cut below those symbols are independent of \(L\), \(Q\), and
\(q\) (the states end in at least eight known symbols, except \(G_1\),
\(G_2\), \(M_1\), \(M_2\), where fewer are needed). Direct inspection of
the terminal words gives the exact global canonical pairs

\[
\begin{array}{c|c|c|l}
\text{cut} & \text{tail} & (\kappa,\pi) & \text{note}\\
\hline
G_1 & \cdots2232\,2 & (2,1) & \text{terminal }22\\
G_2 & \cdots2232\,22 & (3,1) & \text{terminal }222\\
G_3 & \cdots2232\,223 & (2,s),\ 4\le s\le q &
s=4\iff Q[-1]=2\\
M_0 & \cdots2232\,2232 & (2,4) & \text{roots }1,2,3\text{ fail}\\
M_1 & \cdots22322232\,2 & (2,1) & \text{terminal }22\\
M_2 & \cdots22322232\,22 & (3,1) & \text{terminal }222\\
M_3 & \cdots2\,2232\,223,\ \operatorname{suf}\_8=22232223 & (2,4) &
(2223)^2,\ \text{roots }1,2,3\text{ fail}
\end{array}
\]

Derivations. \(G_1,M_1\): the tail ends \(322\), so root \(1\) has
exponent exactly \(2=\kappa\). \(G_2,M_2\): the tail ends \(3222\), so
root \(1\) has exponent exactly \(3=\kappa\); this is the proper
circular cube \(222\) of \(B\) at the \(BB\) seam (resp. of \(R\) at its
\(BB\) seam), the unique proper circular cube of \(\texttt{2232}\):
roots \(2\) and \(3\) fail by inspection and Fine--Wilf. \(M_0\): the
last eight symbols are \(22322232\); roots \(1,2,3\) fail, root \(4\)
is the visible \(B^2\), and \(\kappa(M_0)=2\) makes it canonical, so
\(\pi(M_0)=4\) exactly, sharpening \(\pi(M)\le r\) to equality at
\(r=4\). \(M_3\): the last eight symbols are \(22232223=(2223)^2\)
(the visible \((D_3A_3)^2\)); roots \(1,2,3\) fail. \(G_3\): roots
\(1,2,3\) fail on the last six symbols \(232223\); root \(4\) requires
the preceding symbol \(Q[-1]=2\); the self-cap bound
\(\pi(G_3)\le q\) uses the visible \((C_3A_3)^2\) and needs no target
negation. All rows except the exact value of \(s\) at \(G_3\) are
independent of \(q\), \(Q\), and \(L\), and no localization or period
cap is used. The exponents are exact only because the actual orbit
supplies \(\kappa(K_h)=B[h\bmod r]\); an artificial choice of \(L\) or
\(Q\) can inflate the raw curling number, so the table does not apply
to static words outside the actual orbit.

## PB.7 — phase-one mid-range early roots need a second large period

At phase one, retain the pairs
\((\kappa,\pi)(E_1)=(2,\alpha)\), \((\kappa,\pi)(F_1)=(2,\beta)\) of
(C.35m). Suppose \(r<\alpha<2r+1\). The transition-atlas analysis of
\(T_1=B^2\,3\) gives: \(a'=\alpha-r\) is a period of \(B\) with
\(r/2<a'<r\) and \(B[r-a']=3\). Two new restrictions follow.

1. **\(a'\ne t\).** Otherwise \(B[r-t]=B[a]=3\), contradicting (S3).
   Hence

   \[
   \boxed{\alpha\ne r+t=p-q+r.}
   \tag{PB.7a}
   \]

2. **Fine--Wilf gap.** The two periods \(t\ne a'\) of \(B\) must miss
   the threshold:

   \[
   \boxed{t+a'-\gcd(t,a')>r.}
   \tag{PB.7b}
   \]

   Otherwise \(B\) has period \(g=\gcd(t,a')\). If \(g<\min(t,a')\),
   then \(g\le\min(t,a')/2<r/2\), contradicting (S5). If
   \(g=\min(t,a')\), the smaller of \(t,a'\) divides the larger; both
   lie in \((r/2,r)\), so they are equal, contradicting \(a'\ne t\).

**Corollary (\(r=4\) trichotomy).** For \(r=4\) the admissible set
\(a'\in(2,4)\setminus\{t\}=\{3\}\setminus\{3\}\) is empty, so no early
root lies in \((4,9)\). With (C.35p) and \(B=\texttt{2232}\) (whose only
low-square root is \(s=2\), from \(B[2]=3\) and the terminal square
\((23)^2\) of \(B^2\,3\)), phase one collapses to exactly two cases:

\[
\boxed{
r=4:\quad
\alpha=\beta=2
\quad\text{or}\quad
\bigl(\alpha\ge9\ \text{and}\ 8+\gcd(4,\beta)<\beta<q\bigr).
}
\tag{PB.7c}
\]

## PB.8 — explicit \(p>q\) placement coordinates for high roots

Write \(X=B[a:r]\,Q\,B^2\), so \(|X|=p\) and positions
\([0,t)\), \([t,p-2r)\), \([p-2r,p)\) of \(X\) hold
\(B[a:r]\), \(Q\), \(B^2\) respectively.

- **Early.** If \(\alpha\ge2r+1\), the canonical square of
  \(E_1=X^3\,3\) forces \(X[p-\alpha]=3\), with
  \(0<p-\alpha<p-2r\), hence exactly

  \[
  \boxed{
  \begin{array}{ll}
  p-\alpha<t:& B[a+p-\alpha]=3,\\[1mm]
  p-\alpha\ge t:& Q[p-\alpha-t]=3.
  \end{array}}
  \tag{PB.8a}
  \]

- **Later.** In the high branch of (C.35o), the return (C.35q) forces
  \(R[r+v]=3\) with \(v=P-\beta\), and \(r<v<q-r-\gcd(r,\beta)\), hence
  exactly

  \[
  \boxed{
  \begin{array}{ll}
  v<q-2r:& Q[v]=3,\\[1mm]
  v\ge q-2r:& B[v-q+2r]=3.
  \end{array}}
  \tag{PB.8b}
  \]

**\(r=4\) specialization.** \(B[a:r]=B[1:4]=232\), so (PB.8a) reads:
\(p-\alpha=1\) is allowed (\(X[1]=3\)), \(p-\alpha=2\) is impossible
(\(X[2]=B[3]=2\)), \(p-\alpha=3\) is always allowed
(\(X[3]=Q[0]=3\)), and \(p-\alpha\ge4\) requires
\(Q[p-\alpha-3]=3\). In (PB.8b), \(B[v-q+8]=3\) holds only at
\(v=q-6\), i.e. \(\beta=10\); every other high \(\beta\) requires
\(Q[P-\beta]=3\).

## Bounded catalogue through \(r\le12\) (`COMPUTED`)

`research/enumerate_pgtq_small_r_catalogue.py` enumerates all
\((r,t,B)\) satisfying (S1)--(S6). For each fixed \(r\) this is a
complete finite classification valid for **every** \(q\); the \(q\)- and
\(Q\)-dependent replay conditions are deliberately not imposed, so
membership is necessary, not sufficient. Counts of admissible
\((t,B)\) pairs:

\[
\begin{array}{c|cccccccccc}
r&3&4&5&6&7&8&9&10&11&12\\
\hline
\#&0&1&4&9&23&47&105&211&447&899
\end{array}
\]

The authoritative artifact is
`research/outputs/pgtq_small_r_catalogue_2026-07-28.txt`.

## Consistency with bounded evidence

- Every complete bounded \(p>q\) replay in the D-035 census has
  \(r=4,\ B=\texttt{2232}\); PB.4 shows no other \(r=4\) bridge word
  exists for any \(q\).
- The \(q=10\) near-model has \(B=\texttt{2232}\), matching PB.4; the
  \(q=9\) sharp model has \(B=\texttt{232}\) and is excluded by (S3),
  exactly as the cell ledger records.
- All \(\lambda=1\) catalogue entries have \(a\ge2\) and \(r\ge5\)
  (PB.2b), and every entry satisfies (PB.2a) and (PB.7b) for each of its
  large period pairs.

## Non-claims

- No claim that any catalogue entry is realizable by an actual orbit;
  membership uses only the necessary conditions (S1)--(S6).
- No claim about the \(p<q\) branch, non-boundary Cell C, either G2CS
  target, or the conjecture.
- PB.6 uses actual-generation labels and visible suffix squares only;
  the exact value of \(\pi(G_3)\) remains \(q\)-dependent.
- The catalogue growth (\(\sim2^{r-4}\) tail) shows small-\(r\)
  classification alone cannot close the wall; the open work is the
  unbounded replay obstruction, now concentrated on
  \(B=\texttt{2232}\) at \(r=4\) and the PB.5 words at \(r=5\).
