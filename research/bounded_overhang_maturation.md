# Bounded-overhang replay becomes exact square-to-cube maturation

This note combines the one-sided threshold-component bound with a long
label-three cube.  It removes both outstanding local uncertainties in the
pointed normal form: long label-three roots really are unbounded, and the
first future failure of its bounded overhang is forced at a symbol `2`.
The result is an exact fixed-origin square-to-cube maturation.  It does not
exclude an infinite family of such maturations.

All statements here are natural-language proofs.  They are `PROVED-NL` in
the research ledger, not `VERIFIED` final-report claims.

## 1. Setup and imported results

Let `T` be a hypothetical nonterminating orbit word, indexed from zero.
Choose `N` and `M` as in `one_sided_threshold_ancestry.md`, so every cut
used below is generated, every tail label belongs to `{2,...,M}`, and every
maximizing root at a cut labelled at least four has length below `N`.

We use three earlier results.

1. Lemma 4 of `reductions.md` says that least maximizing-root lengths are
   unbounded.
2. The shadow-divergence argument of `golden_bad_cuts.md` converts every
   sufficiently large label-two root `q` into a high-label root longer than
   `q/M` unless the two compared futures agree forever.  Eternal agreement
   would make the tail periodic and is impossible.  Together with the
   high-label bound just recalled, this proves that label-three maximizing
   roots are unbounded.  Section 4 below spells out the short proof.
3. Theorem 4 of `one_sided_threshold_ancestry.md` gives a constant `R` and,
   for every sufficiently long label-three cube, a return boundary within
   `R` symbols of the start of its root.

The public-literature search made before this synthesis looked for a
curling-number or combinatorics-on-words theorem about a cube followed by a
partial conjugate replay.  It found only the standard conjugacy identity
used below and the already recorded Curling Number papers.  No external
source located in that scoped search states the orbit-specific mismatch or
maturation theorem.

## 2. The pointed cube and its long square shadow

Take a generated cut `d` with exact label three and a primitive maximizing
root `Y` of length `r`, so, for `x=d-3r`,

```
T[x:d]=Y^3.                                             (1)
```

Take `r>R` and use the boundary supplied by the pointed normal form.  Write

```
b=x+s,       1<=s<=R,
Y=U V,       |U|=s,       T[b-1]=2.                    (2)
```

Put

```
p=b-1,       u=p+r,       v=p+2r,
W=T[p:u].                                               (3)
```

Period `r` in (1) gives

```
T[p:v]=W^2,       T[u]=T[v]=2.                         (4)
```

The second equality is an equality of orbit labels: all three positions
`p,p+r,p+2r` lie inside the displayed cube.  Therefore the cut `v` has
exact value two, and the root `r` in (4) is a maximizing square root there.

Compare the two future streams beginning at cuts `u` and `v`.  The cube
period forces them to agree for the first

```
j_0=d-v=r-s+1                                           (5)
```

symbols.  At that point the source stream is at the start of the third
copy of `Y`, while the target stream is at the first symbol after the
cube.  For `0<=t<s`, continued agreement compares

```
T[u+j_0+t]=U[t]       with       T[v+j_0+t]=T[d+t].     (6)
```

They cannot agree through all `s` positions.  If they agreed through
`U[:s-1]`, the target prefix at cut `d+s-1` would end in a cube of a
conjugate of `Y`, by the identity in the next section.  Its next label
would be at least three, whereas (2) requires the matched symbol
`U[s-1]=2`.

Let `h`, with `0<=h<s`, be the first mismatch in (6), and put

```
ell=j_0+h.                                             (7)
```

At the mismatch cuts `u+ell` and `v+ell`, the two prefixes have a common
terminal word of length

```
H=r+ell=2r-s+1+h.                                     (8)
```

Indeed, they had the same terminal word `W` of length `r` at cuts `u,v`
and then appended `ell` equal symbols.

## 3. The first mismatch is exactly `2 -> 3`

For `0<=t<=h`, put

```
A_t=U[:t],       B_t=U[t:]V.
```

The target prefix at cut `d+t` ends in

```
(A_t B_t)^3 A_t = A_t (B_t A_t)^3.                    (9)
```

Thus its exact label is at least three.

Let `a=T[u+ell]=U[h]` be the source label and
`c=T[v+ell]=T[d+h]` the target label.  They are distinct, `c>=3`, and
both lie in `{2,...,M}`.  Put `k=max(a,c)` and choose a primitive
maximizing root of length `q` on the side labelled `k`.

Its complete `k`-power cannot fit inside the common suffix of length `H`
in (8).  If it did, the same suffix would make the other label at least
`k`.  Therefore

```
k q>H,       q>(2r-s+1+h)/M.                          (10)
```

Choose the record root so large that

```
2r-R+1>=M N.                                          (11)
```

If `k>=4`, the high-label root bound gives `q<N`, while (10), `s<=R`,
and (11) give `q>=N`.  This is impossible.  Hence `k=3`.  Since `c>=3`
and `a,c` are distinct counterorbit labels, necessarily

```
a=2,       c=3.                                      (12)
```

For every `t<h`, equation (9) and agreement give `U[t]>=3`; equation
(12) gives `U[h]=2`.  Consequently `h` is exactly the first occurrence
of `2` in `U`.

Set

```
A=U[:h],       B=U[h:]V,       Z=B A,       L=T[:x]A.
```

The source and target states at the mismatch are, respectively,

```
T[:u+ell]=T[:x](A B)^2 A=L Z^2,
T[:v+ell]=T[:x](A B)^3 A=L Z^3.                      (13)
```

Their cut distance is exactly `r=|Z|`, and the intervening actual orbit
output is exactly one copy of `Z`.  Equations (12)--(13) therefore give
the exact same-origin maturation

```
cn(L Z^2)=2,
L Z^2  --append the actual word Z-->  L Z^3,
cn(L Z^3)=3,
Z[0]=2.                                              (14)
```

The rotation offset satisfies `h<R`.  Thus every sufficiently large
label-three record cube admits a bounded rotation to a generated
root-scale square episode which matures without interruption into a cube.

## 4. Short proof that label-three roots are unbounded

Suppose instead that label-three maximizing roots were bounded.  Theorem 3
of `one_sided_threshold_ancestry.md` bounds every sufficiently late root at
a label at least four.  Hence there is one constant `B` bounding all late
maximizing roots at labels at least three.

Take a late label-two cut with a maximizing square root `q`.  Such `q` are
unbounded by Lemma 4 of `reductions.md` under the supposition just made.
Compare the future streams after the square midpoint and endpoint.  They
cannot agree forever, because the orbit tail would then be `q`-periodic.
After `t` common outputs, the two prefixes share a terminal word of length
`q+t`.  At their first mismatch the larger label is some `k>=3`; a
maximizing `k`-root of length `z` cannot fit in that common word, so

```
k z>q+t,       z>q/M.                               (15)
```

But `z<=B`, making `q<MB`.  This contradicts the unbounded choice of `q`.
Therefore label-three maximizing roots are unbounded.  This is a shorter
dependency route than the stronger golden-record theorem in
`golden_bad_cuts.md`; the latter also supplies record-scale and origin
information not used here.

## 5. Exact remaining obstruction

Equation (14) is the fixed-origin maturation branch already recognizable
in `golden_bad_cuts.md` and `root_episodes.md`, now obtained at every
sufficiently large label-three record after a uniformly bounded rotation
selected by the one-sided return geometry.  It rules out an arbitrary
high/high context mismatch in the pointed overhang.

It does not yet contradict nontermination: the contexts `L`, roots `Z`,
and maturation origins may change between record levels.  The next global
obligation is to show that an unbounded sequence of these bounded-rotation
maturations either stabilizes at one origin (giving the already normalized
cube self-replicator tower) or creates a strictly earlier power-tower
origin.  Any proposed rank must survive the Q21 fixed-profile reset cycle
and the terminal-`F` inflation tower already recorded elsewhere.
