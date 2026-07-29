# \(p>q,\ r\ge5\): the cut-filter theorem and the catalogue collapse

Status: `PROVED-NL` (the filter lemmas); `COMPUTED` (the complete
disposition for \(5\le r\le20\)). Scope: Cell C simultaneous boundary,
\(p>q\), row \((z,h)=(1,0)\), bridge length \(r\ge5\); the bridge-cut
filters use the \(\mathcal J\)-caps through D-035, which is the
checklist target for this wall.

## The filters

Beyond the catalogue conditions (S1)--(S6) of
`pgtq_boundary_small_r.md`, the inherited exact pairs and the D-035
bridge atlas impose pure-\(B\) conditions never previously applied:

- **S8 (record canonicity).** \((\kappa,\pi)(R^2)=(2,q)\): \(B\) has
  no terminal square of root \(\rho\le r/2\) — strictly stronger than
  the absence of a full period \(\le r/2\).
- **S7 (later-cube canonicity).** \((\kappa,\pi)(F)=(3,r)\): \(B^3\)
  has no suffix cube of root \(\rho<r\).
- **S20/S21 (phase-one exactness).** \(\kappa(E_1)=\kappa(F_1)=2\):
  neither \(B^2\,3\) nor \(B^3\,3\) has a suffix cube.
- **S11 (bridge `2`-cuts).** At every proper bridge cut requesting
  `2`, the visible \(B\)-periodic suffix (length \(r+h\)) admits no
  ending cube: otherwise \(\kappa\ge3\ne2\).
- **S12 (bridge `3`-cuts, second half).** By D-035, a capped
  second-half cut requesting `3` has its canonical cube as a proper
  circular cube of \(B\) inside the visible zone, except the
  full-root seam (\(i=r-1\), \(\lambda=1\)): such a cube must
  therefore **exist**.
- **S16 (label bound).** No cut admits a visible fourth power:
  \(\kappa\le3\) always. In particular every circular run of equal
  letters in \(B\) has length at most three.

Each filter is finite letter arithmetic on \(B\) alone.

## The collapse (`COMPUTED`)

Applying the filters to the complete catalogue (all words satisfying
(S1)--(S6)) for \(5\le r\le20\) — \(384{,}135\) words in total:

\[
\boxed{\text{every catalogue word dies, except exactly two at }r=13:}
\]

\[
B_1=\texttt{2232223322232},\qquad B_2=\texttt{2232223222332},
\]

with periods \(t=9\) and \(t=12\) respectively, both \(\lambda=0\), both of the
form "quasi-\((2223)\)-periodic with a single \(33\) defect", the
defect fed by the circular cube \((2223)^3\) — the two words embed the
\(r=4\) solution. Kill counts per \(r\) and per filter are in the
disposition table produced during drafting; the checks were run twice.

## Reductions of the two survivors

- **\(B_1\):** the inner curling orbit of the seed \(B_1^2\,3\) is
  \(3,2,2,2,3\) and reaches curling number \(1\) at phase \(5\): by
  the forced-replay argument (which is \(B\)-generic), every
  \(B_1\)-counterorbit must exhibit a window-crossing exit at a phase
  \(\ell^*\le5\), with double crossing cubes at
  \(\ell^*\in\{1,2,3\}\) and squares admissible only at \(5\).
- **\(B_2\):** the seed \(B_2^2\,3\) has **no square at all**
  (\(\kappa_{\rm loc}=1\) at phase one), so both windows require
  context-crossing squares already at phase one — the high branch of
  (C.35) with no local alternative. A new pure-\(B\) restriction
  derived here: a phase-one early root \(\alpha\in(r,2r]\) forces a
  second large period \(\delta=\alpha-r\) of \(B\) with
  \(B[r-\delta]=3\); \(B_2\) has no second large period, so its early
  root satisfies \(\alpha>2r\).

## Non-claims and the residual

- The two words are reduced, not eliminated: \(B_1\) needs its (at
  most four) exit events killed with the \(r=4\) machinery
  generalized to \(r=13\); \(B_2\) needs an exponent-two
  (crossing-square) analogue of the exit-root machinery at phase one.
- The disposition is complete for \(5\le r\le20\); for \(r\ge21\) a
  uniform argument is still required. The structural route is
  visible: S11/S16 bound all letter runs by three, S12 grounds every
  `3` in either a \(222\)-feed or an exotic circular cube whose
  root must itself satisfy miniature S11/S12 conditions, and interior
  slide analysis bounds exotic periodic segments; this points to a
  finite-tile classification of admissible \(B\), with the border
  (S2) and primitivity closing large \(r\). This is the named next
  slice.
- Nothing here closes the \(p>q\) wall, Cell C, either G2CS target,
  or the conjecture.
