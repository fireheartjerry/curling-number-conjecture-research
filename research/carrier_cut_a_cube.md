# The cube at the first carrier defect

This note analyzes the pointed cube already present in every internal
three-block carrier.  It removes two of the three co-terminal-root
branches without using a later defect.

## 1. Setup

Let

```
U=A B A=C A,
a=|A|,       b=|B|,       p=|U|=2a+b,
C=A B,       h=|C|=p-a.
```

Assume:

```
A,B are nonempty,
U and A are primitive,
A[0]=2,       B[0]=3,
cn(U)=2,      cn(U A)=3,
pc_U=U.
```

The actual orbit from `U` emits `A`; the last displayed equality is the
pointed maturation at cut `a`.  The next internal reset root is

```
V=C A C A C,
q=|V|=3p-a,
pc_V=V.                                             (1)
```

Primitivity of `A` also follows from `cn(UA)=3`: if `A=Z^m` for
`m>=2`, the displayed suffix `A^2=Z^(2m)` would give exponent at least
four.

Choose a primitive maximizing cube root `R` of `UA`, and put

```
r=|R|,
g=gcd(a,r).
```

The primitive powers `A^2` and `R^3` are co-terminal.

## 2. Exact Fine--Wilf split

If `r<a`, their common suffix has length `min(2a,3r)`.  The alternative
`2a<=3r` reaches the Fine--Wilf threshold `a+r-g`, so it would give a
proper gcd period to `A` or `R`.  Hence the common length is `3r`, and
threshold failure is

```
2r+g<a.                                             (2)
```

If `r>a`, the common suffix has length `2a`.  Threshold failure is

```
a+g<r.                                             (3)
```

For equal lengths, the terminal root blocks agree.  Thus the exhaustive
split is

```
r<a and (2),       r=a with R=A,       or       r>a and (3).    (4)
```

## 3. Exact fractional-period form of the shorter-root branch

Assume `r<a`.  Equation (2) gives `2r<a`, so the terminal `R^2` lies
wholly in the appended copy of `A`.  Write

```
A=X R^2,
ell=|X|=a-2r>0.                                    (5)
```

If `3r<=a`, then the entire terminal cube `R^3` would lie in that copy
of `A`.  Since `U` also ends in `A`, the state `U` would end in the same
cube, contradicting `cn(U)=2`.  Therefore

```
0<ell<r.                                           (6)
```

In the terminal cube at `UA`, the copy of `R` immediately before the
displayed `R^2` consists of the last `r-ell` symbols of `U`, followed
by `X`.  Since `U` ends in `A=X R^2`, those `r-ell` symbols are
`R[ell:]`.  Equality of that copy with `R` gives

```
R=R[ell:] X,       X=R[r-ell:].                   (7)
```

In particular,

```
R[:r-ell]=R[ell:],
```

so `ell` is a proper finite-word period of `R`.  This is not a
primitivity contradiction.  Indeed

```
gcd(r,ell)=gcd(r,a)=g<ell                           (8)
```

by (2).  Thus the available period `ell` need not divide `r`; a
primitive word may have such a proper period.  The exact residual form
is

```
0<gcd(r,ell)<ell<r,
R has period ell,
A=R[r-ell:] R^2.                                  (9)
```

There is also an orbit interpretation.  Put `H=U X`.  Equation (7)
shows that `H` ends in `R`, and the actual continuation from `H` emits
the two copies `R^2` before reaching the displayed cube:

```
H ends in R,
H R^2=U A ends in R^3,
cn(H R^2)=3.                                      (10)
```

The root scale has dropped strictly below `a/2`, but `R` is a suffix
block rather than a prefix anchored at the global origin.  Therefore
(10) is a shorter suffix maturation, not yet a reset-root or
prefix-carrier descent.

The binary fixed profile bounds the nondivisorial quotient.  Since `R`
occurs as a factor of `U`, the inequality `r>=4ell` would put four
consecutive copies of an `ell`-block inside `U`.  That would be a proper
fourth power at a cut whose exact profile value belongs to `{2,3}`.
Hence

```
r<4ell.
```

There is a sharper complementary bound from the absence of circular
`333`.  For every integer `k` with

```
3ell<=k<r,
```

the length-`3ell` factor of `R` ending at offset `k` is an
`ell`-root cube.  Fixedness forces the following label `R[k]` to be
`3`.  Three such consecutive offsets would give a factor `333` in
`U`, which is impossible in a primitive binary fixed profile.
Therefore

```
r<=3ell+2.
```

In particular `floor(r/ell)` belongs to `{1,2,3}`.  In the last case,
write

```
r=3ell+s,       s in {1,2}.
```

The same forced-cube labels and the period `ell` give

```
R[:s]=3^s.
```

On the other hand, `A[0]=X[0]=2`, while (7) and period `ell` give
`X[0]=R[r-ell]=R[s]`.  Thus the complete quotient-three prefix is

```
R[:s+1]=3^s 2.
```

These bounds leave quotient-one, quotient-two, and two terminal
quotient-three seam types.  They do not determine the longer context
that supplies the squares at all `2`-cuts.

## 4. The equal-root branch is impossible in the child

Assume `r=a`.  Then `R=A`, and the terminal cube says that `UA` ends
in `A^3`.  Thus `U` ends in `A^2`, or equivalently

```
C ends in A.                                      (11)
```

At circular cut zero of `V`, the preceding `a` symbols are `A` by
(11).  The complete suffix ending at that cut is

```
A V=A C A C A C=(A C)^3.                         (12)
```

Its root has length `p<q`, so it is a proper circular cube of `V`.
But fixedness requires

```
pc_V(0)=V[0]=A[0]=2,
```

contradicting (12).  The branch `r=a` is impossible.

## 5. Exact surviving branch

It remains that

```
r>a.                                              (13)
```

The cube is fitting in the actual state `UA`, so

```
3r<=p+a.
```

Since `p=2a+b` with `b>0`, one has `a<p/2`, and therefore

```
r<p/2.                                            (14)
```

The final `a` symbols of `R` are the final appended `A`; write

```
R=F A,
f=|F|=r-a,
W=A F.
```

Deleting the final appended `A` from `(FA)^3` shows that the final
`2r` symbols of `U` are `(AF)^2`.  Thus, with

```
sigma=p-2r,
K=U[:sigma],
```

one has the exact prefix-square decomposition

```
U=K W^2.                                          (15)
```

The fitting inequality gives a slightly stronger location bound.  From
`3(a+f)<=3a+b` one gets `3f<=b`, and hence

```
sigma=b-2f>=f>0.                                  (16)
```

If `sigma>=N_0`, then `K=T[:sigma]` is a visible bad orbit state.
The literal continuation in (15) gives

```
cn(K)=W[0]=A[0]=2,
K W^2=U,
cn(U)=2,
```

and `K[1:]` terminates in the fixed-deletion branch.  This is a strict
prefix reduction, but `W` is not anchored at the global origin and no
proper-circular fixed profile for `K` or `W` follows.

The child fixedness records one further load-bearing target.  At
circular cut `h=|C|` of `V`, the word ends in `C^2` across the
`V|V` seam, while its required label is

```
V[h]=A[0]=2.
```

Therefore `C` must be primitive.  If `C=Z^m` with `m>=2`, that cut
would end in `Z^(2m)` and have proper circular exponent at least four.
Consequently any proof that (13)--(16), together with `pc_U=U`, makes
`C` imprimitive immediately contradicts `pc_V=V`.

The precise unresolved cases at this cut are therefore:

```
r<a/2 with the fractional-period form (9),          or
r>a,
U=K(AF)^2,
0<r-a<=|K|,
C=AB primitive,
pc_U=U,
pc_V=V.                                          (17)
```

The equal branch is eliminated.  The shorter branch is a
nondivisorial-period/suffix-maturation obstruction; the longer branch is
the same square-prefix closure obstruction as in the later
increasing-defect analysis.  Both are present one generation earlier
and do not depend on a third internal reset.

## 6. Unified moving-boundary form

The two residual branches have one common coordinate description.
Because the selected cube is a fitting suffix of `UA`, put

```
L=p+a-3r>=0,
P=T[:L].
```

Then

```
U A=P R^3.                                         (18)
```

Define

```
H=P R=T[:L+r],
|H|=p+a-2r.                                        (19)
```

Equations (18)--(19) give the literal factorization

```
H ends in R,
T[|H|:p+a]=R^2,
H R^2=U A.                                         (20)
```

If `|H|>=N_0`, then `H` is an actual state of the bad orbit, its
one-symbol deletion terminates, and determinism upgrades (20) to the
full phase equations

```
cn(H R^j R[:t])=R[t]
    for j in {0,1}, 0<=t<r,
cn(H R^2)=3.                                       (21)
```

If `|H|<N_0`, (20) remains a word identity inside the prescribed
initial seed, but none of the intermediate equalities in (21) may be
asserted before the generated boundary.  This is the exact visibility
distinction.

The location of `H` relative to `U` is:

```
r<a:   |H|=p+ell,       ell=a-2r in (0,a);
r=a:   |H|=p-a=h;
r>a:   |H|=p-c,         c=2r-a>a.                 (22)
```

The first line uses (2), which gives `2r<a`; the last uses `r>a`.
Thus the fractional-period branch begins its suffix maturation a
bounded distance after `U` and is automatically visible in the late
regime.  The longer-root branch begins before `U`; it is visible
exactly when `p-c>=N_0`.

If the reset root `U` arose from the preceding internal root with
incoming defect `a_-`, the preceding reset endpoint has length

```
p+a_-.
```

In the `r<a` line, the complete episode (21) occupies

```
[p+ell,p+a].
```

Consequently it contains that preceding reset endpoint exactly when

```
ell<=a_-<=a.
```

Otherwise no reset lies inside the episode, because the reset endpoints
under discussion are consecutive.  All three quantities
`ell,a_-,a` are bounded by the fixed seed length; this is the finite
moving-boundary datum that a two-generation or tau-rank argument still
has to orient.

## 7. A long-root episode in an internal child is always visible

There is a clean two-generation improvement to the last line of (22).
Let

```
V=U^3[:-a],
q=|V|=3p-a.
```

Write `U=C A`, so

```
V=C A C A C=C(AC)^2.                              (23)
```

Let `D=T[:d]` be the carrier prefix at the child `V`, and suppose the
cube at `VD` is in its long-root branch.  Write its primitive cube root
as `F D`, put `s=|FD|>d`, and use the conjugate square supplied by
Section 5:

```
V=K'(D F)^2,
kappa=|K'|=q-2s>0.                                (24)
```

The complete square `(DF)^2` is a factor of `V`, hence of the
`p`-periodic word `U^3`.  If `s>p`, this square has periods `s` and
`p`, and

```
2s>=p+s-gcd(p,s).
```

Fine--Wilf would give period `gcd(p,s)<=p<s` to the complete primitive
root `DF`, a contradiction.  Therefore

```
s<=p,
kappa=q-2s>=p-a=|C|.                              (25)
```

In the late regime `C=T[:p-a]` is already a visible orbit state.
Equation (25) proves that `K'`, and hence the unified maturation state
`K'D`, is visible as well.  Thus the hidden alternative in the
long-root line of (22) can occur only before this root has an internal
parent; it cannot recur in the late internal tower.

If the child defect increases, `d>a`, equality in (25) is impossible.
Indeed `s=p` makes the last two root blocks in (24) equal the literal
last two blocks in (23), so

```
D F=A C.
```

Comparison at offset `a<d` would give

```
T[a]=D[a]=(AC)[a]=A[0]=2,
```

whereas the pointed old defect has `T[a]=3`.  Hence

```
d>a  implies  s<p and kappa>p-a.                  (26)
```

For `d<a`, the prefix comparison does not contradict `s=p`, because
both `D` and `AC` begin with the same prefix `A[:d]`.  This equality
case is exactly the canonical conjugate square in (23), not an omitted
branch.

Combining Sections 3, 6, and 7: every cut-`a` cube in every sufficiently
late internal child supplies a **visible** suffix maturation (21).
The short-root branch starts after its carrier root; the long-root
branch starts at or before it, but (25) keeps it beyond the generated
boundary.  Visibility is therefore closed.  What remains is to orient
these visible suffix maturations against the adjacent reset endpoints
they may cross.

For the long child branch, that crossing is explicit.  The parent reset
endpoint is

```
3p=q+a,
```

whereas the maturation interval from (24) is

```
[q+d-2s,q+d].
```

If `d>a`, then `s>d` gives

```
q+d-2s < q+a < q+d.
```

Thus every increasing-defect long-root maturation contains the parent
reset endpoint in its interior.  It can also begin before the immediately
preceding reset endpoint; no claim that the parent is the only reset in
the interval is made.  If `d<a`, its right endpoint `q+d` lies strictly
before the parent reset.  This is the exact dynamical split:
the increasing long branch is a reset-straddling suffix maturation,
while the decreasing long branch is wholly on the pre-reset side.
