# A peak in the bounded-defect sequence

This note combines the increasing-residual cube with the immediately
following decreasing carrier.  It treats one local-extremum pattern

```
a<d>e
```

in a late run of internal cubic resets.  The result is an exact nested
power geometry and an exhaustive Fine--Wilf split.  The final crossing
ascent is not eliminated here.

## 1. Coordinates

Let `U` be the first reset root, with

```
p=|U|,
A=T[:a].
```

The next root is

```
V=U^3[:-a],
q=|V|=3p-a.
```

Put

```
D=T[:d]=A E,       |E|=d-a,
G=T[:e].
```

The pointed labels at cuts `a,d,e` are all `3`.

For the increasing move `a<d`, retain the sole unresolved rescue from
`increasing_defect_phase_lock.md`: a primitive maximizing cube root
`R` at

```
S_+=V D=U^3 E
```

with

```
r=|R|,
d<r<p/2.                                           (1)
```

Put

```
H_+=T[:|S_+|-2r].
```

The selected cube gives the visible suffix-maturation episode

```
H_+ ends in R,
H_+ R^2=S_+,
|H_+|=3p+d-a-2r.                                  (2)
```

For the following decreasing move `d>e`, put

```
L=V[:-d]=T[:q-d].
```

The decreasing-carrier lemma gives

```
cn(L)=2,
L ends in G,
cn(L G)=3,
L G ends in G^2.                                  (3)
```

Every value in (2)--(3) is a symbolic orbit equality from the stated
hypotheses; no concrete curling number is asserted in this note.

## 2. Exact nesting

The start of the decreasing carrier is later than the start of the
outer maturation by

```
|L|-|H_+|
 =(3p-a-d)-(3p+d-a-2r)
 =2(r-d)>0.                                       (4)
```

Its endpoint is earlier than the outer endpoint by

```
|S_+|-|L G|
 =(3p+d-a)-(3p-a-d+e)
 =2d-e=:Delta.                                    (5)
```

Since `0<e<d<r`,

```
0<2(r-d)<2(r-d)+e<2r.
```

Thus the whole episode `L -> L G` lies strictly inside the two copies
of `R` emitted in (2).

Include the copy of `R` already ending at `H_+`.  In the resulting
displayed cube `R^3`, the two copies of `G` occupy the exact interval

```
[|L|-e, |L|+e].
```

Relative to the left endpoint `|H_+|-r` of `R^3`, its two endpoints are

```
3r-2d-e,
3r-2d+e.
```

Both are strictly between `0` and `3r`, because `r>d>e`.  Hence

```
G^2 is a strict internal factor of R^3.            (6)
```

Its right endpoint is the `3`-labelled cut `|L G|`.

## 3. The inner cube root is not the outer root

Choose a primitive maximizing cube root `Q` at `L G`, and put

```
x=|Q|.
```

Here

```
|L G|=3p-(a+d-e).
```

The defects are bounded by `N_0`.  On the unbounded late branch take
`p>a+d-e`; the cut then lies strictly after position `2p`, in the
third replay copy of the primitive fixed-profile root `U`.  A proper
circular witness can therefore be chosen, so

```
x<p,
2x+gcd(p,x)<p.                                    (7)
```

The second inequality is the proper-power span bound: meeting the
Fine--Wilf threshold inside the `p`-periodic lift would give a proper
gcd period to `U` or `Q`.

One cannot have `x=r`.  If an `r`-root cube also ended at `L G`, its
interval would overlap the displayed cube ending at `S_+` in

```
3r-Delta>r
```

symbols, because `Delta=2d-e<2r`.  Their union would be one
period-`r` run.  It would contain an `r`-cube ending at every cut from
`L G` through `S_+`.  But

```
Delta=2d-e>=3
```

for positive integers `e<d`, producing three consecutive `3` labels.
A primitive binary fixed profile has no circular factor `333`.
Therefore

```
x!=r.                                              (8)
```

## 4. Outer-overlap split

Normalize the endpoint of the displayed `R^3` to coordinate zero.  Its
interval and the inner cube interval are

```
I=[-3r,0],
J=[-Delta-3x,-Delta].
```

Their overlap length is exactly

```
min(3x,3r-Delta).                                  (9)
```

It has periods `r` and `x`.  Put `gamma=gcd(r,x)`.  Reaching length
`r+x-gamma` would give a proper gcd period to a complete conjugate of
one of the primitive roots.  Hence the threshold must fail.

There are exactly two cases:

```
3x<=3r-Delta:
    2x+gamma<r;                                   (10)

3x>3r-Delta:
    x>2r-Delta+gamma
     =2(r-d)+e+gamma.                             (11)
```

Case (10) is a strict drop below half the outer root.  Case (11) is the
sole crossing ascent; its cube begins to the left of the portion of the
outer run long enough for Fine--Wilf completion.

## 5. Co-terminal split at the decreasing carrier

At the same inner endpoint, the primitive square `G^2` from (6) and
the primitive cube `Q^3` are co-terminal.  Put

```
eta=gcd(e,x).
```

The standard co-terminal Fine--Wilf calculation gives the exhaustive
split

```
x=e;
x<e  and  2x+eta<e;
x>e  and  x>e+eta.                                (12)
```

In particular, if `x=e`, alternative (11) is impossible, because its
right side is strictly larger than `e`.  Equation (10) then gives

```
2e+gcd(e,r)<r.                                    (13)
```

Thus the same-root child is a strict scale drop.  The `x<e` line is
smaller still.  Every failure of descent is confined to the conjunction

```
x>e+gcd(e,x),
x>2(r-d)+e+gcd(r,x),                              (14)
```

together with the global proper-root bound (7).

There is a useful bounded-versus-doubling refinement of (14).

If `x<=r`, then (14) implies

```
r<2d-e-gcd(r,x)<2d<2N_0.                         (15)
```

Thus every non-increasing crossing rescue has bounded root length and
belongs to a finite seed-scale family.

If `x>r`, then `gcd(r,x)>=1` strengthens (14) to

```
x>2r-(2d-e-1).                                    (16)
```

This is an affine near-doubling: the additive loss is bounded entirely
by the fixed defects.  The exact integral form is slightly sharper.
Put

```
gamma=gcd(r,x),       rho=gcd(p,x).
```

The strict integer inequalities (7) and (11) give

```
x >= 2r-2d+e+gamma+1,
p >= 2x+rho+1,
p >= 4r-4d+2e+2gamma+rho+3.                      (17)
```

In particular,

```
r <= p/4+d-e/2-3/2.                               (18)
```

Consequently an unbounded crossing branch cannot hover at one scale.
Within one ambient period `p`, successive crossings of the same form
would have only logarithmically many opportunities before violating
(7).  Turning this observation into a global contradiction requires a
proof that the inner crossing node inherits the next peak in the same
ambient period; that inheritance is not asserted here.

There is one standard three-square refinement.  If `r>Delta`, the
prefix of the displayed `R^3` ending at `c` still contains a complete
conjugate `R`-square.  Thus the primitive squares of root lengths

```
e<r<x
```

are co-terminal at `c`.  Reversal turns them into three common-prefix
squares.  The Three Squares Lemma gives

```
x>=r+e.                                           (19)
```

Here the invoked statement is Crochemore--Rytter's Three Squares Lemma:
if `u^2,v^2,w^2` are common prefixes, `|u|>|v|>|w|`, and `w` is
primitive, then `|u|>=|v|+|w|`; see Bannai--Mieno--Nakashima,
Lemma 1, [arXiv:2006.13576](https://arxiv.org/abs/2006.13576).
On an unbounded fixed-defect branch, the first lower bound in (17)
eventually dominates (19), so the named lemma does not create a
cross-peak rank.

### The inequalities do not compose across two peaks

The obstruction is exact, rather than an artifact of loose constants.
Consider the periodic defect pattern

```
1<5>1<5>...
```

and at successive peaks define

```
p_n=4r_n-12,
x_n=2r_n-7,
r_0=12,
r_(n+1)=9r_n-26.                                  (20)
```

Two reset transitions give

```
p_(n+1)=9p_n-3*1-5=9p_n-8=4r_(n+1)-12.
```

Also `r_n=5 mod 7` for every `n`, and hence

```
gcd(r_n,x_n)=gcd(p_n,x_n)=1.
```

Every proved crossing constraint is then satisfied with equality plus
the minimum integer slack:

```
2x_n+gcd(p_n,x_n)=p_n-1,
x_n=2(r_n-5)+1+gcd(r_n,x_n)+1.                   (21)
```

Moreover `r_n>2*5-1`, `5<r_n<p_n/2`, and
`x_n>1+gcd(1,x_n)`.  Thus

```
r_n/p_n -> 1/4,
x_n/p_n -> 1/2,
```

while both scales grow without bound.  The executed exact-integer audit
`check_peak_affine_countergeometry.py` verifies the first 64 stages;
the displayed recurrences and gcd identities prove all stages.  This
is an arithmetic countergeometry, not a word construction: it proves
that (7), (11), (12), and reset-length recurrence alone cannot yield a
monotone rank over successive peaks.

The missing implication is consequently precise.  A completion must
transport an actual word/profile constraint from the current inner
cube `Q` to the maximizing residual root at the next peak.  No such
relation between `x_n` and `r_(n+1)` follows from the present overlap
inequalities.

The crossing cube also copies the inner square marker.  Let

```
c=|L G|
```

be its endpoint.  If `x>=2e`, the suffix `G^2` lies wholly in the final
copy of `Q`.  Translation by the cube period copies it to complete
occurrences ending at

```
c-2x,       c-x,       c.                         (22)
```

The exact labels at the first two cuts are both `Q[0]`, because they
are the boundaries before the second and third copies of `Q`; the last
label is the external pointed value `3`.

This gives an exhaustive binary split.

* If `Q[0]=2`, put `H_Q=T[:c-2x]`.  The three cube blocks give a new
  visible suffix maturation

  ```
  H_Q ends in Q,
  H_Q Q^2=T[:c],
  cn(H_Q)=cn(H_Q Q)=2,
  cn(H_Q Q^2)=3.                                  (23)
  ```

  Visibility follows from `c>2p` and `x<p/2`.

* If `Q[0]=3`, all three copied occurrences in (22) are
  square-at-three nodes.  At each of the first two cuts, fixedness
  supplies a possibly different maximizing cube root co-terminal with
  the copied `G^2`.

  This branch has an exact two-symbol seam.  Appending the external
  `3` at cut `c` extends the root-`x` cube by one symbol, because it
  equals `Q[0]`.  Hence an `x`-root cube also ends at cut `c+1`, forcing
  the next label to be `3`.  A third consecutive `3` is impossible in
  the binary bad profile, so the following label is `2`.  If
  `Q[1]=3`, the same period-`x` run would extend once more and force
  that following label to be `3`.  Therefore

  ```
  Q[:2]=32,
  T[c:c+3]=332.                                   (24)
  ```

  At each earlier copied endpoint in (22), the following two symbols
  are the internal root prefix `Q[:2]=32`; only the final endpoint has
  the adjacent-double continuation `332`.

If `x<2e`, then `x<2N_0`, so the crossing root is already in the
bounded seed-scale branch.  Thus every unbounded crossing either
reproduces a larger visible suffix maturation as in (23), or branches
into three copied high square markers.  The remaining missing statement
is a well-founded rank for this reproduction/branching alternative.

## 6. Exact remaining peak obstruction

The peak `a<d>e` therefore cannot hide an arbitrary local power.  It
contains a visible, strictly nested square-at-three node `G^2` inside
the visible cube `R^3`.  Every maximizing inner cube either

1. has root below half of `r`;
2. equals `G` and satisfies the sharper drop (13); or
3. is the explicit left-crossing ascent (14).

The first two alternatives supply a genuine smaller suffix-maturation
scale.  The third cube may extend left of the displayed `R^3`, although
it remains a proper root of the ambient fixed profile by (7).  Ruling
out repeated occurrences of (14), or proving that their left endpoints
cross a reset boundary in a well-founded direction, is the exact
remaining local-extremum problem.
