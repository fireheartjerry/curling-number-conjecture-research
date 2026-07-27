# Bounded-defect graph and the strict carrier descent

This note combines the seed-anchoring result in
`reset_root_transition_split.md` with the two-generation quotient in
`internal_k3_hidden_audit.md`.  It proves that one of the two possible
orders of consecutive defects gives a genuine strict descent in an
orbit-defined maturation class.  The opposite order remains open.

## 1. Maturation carriers

Work in the late all-deletions-terminate reset branch.  Let `T` be the
bad orbit word and let `N_0` be the starting length.  A late internal
transition has

```
U=C A,
|U|=p,       |A|=a,       |C|=h=p-a,
U[:a]=U[-a:]=A,
1<=a<N_0,
T[a]=3.                                           (1)
```

The surviving Euclidean quotient from
`internal_k3_hidden_audit.md` is

```
U=A B A,              C=A B,                     (2)
```

with `A,B` nonempty.  The root `U` is an orbit state with

```
cn(U)=2.
```

Its actual orbit emits the prefix `A`, because `U` self-replays inside
the later whole cube.  At the last of those `a` cuts,

```
cn(U A)=T[a]=3.                                  (3)
```

The word `A` is primitive.  Indeed `U A` ends in `A^2`; if
`A=Z^m` with `m>=2`, that suffix would be `Z^(2m)` and (3) would be at
least four.

Call the pair `(U,A)` a **maturation carrier**: it is a bad visible orbit
state with terminating first deletion, exact value two, a primitive
prefix/suffix `A`, and its actual orbit emits `A` before the value rises
to three.

## 2. The next defect

Suppose the next reset transition is internal as well.  The
two-generation quotient supplies an integer `d` and the prefix

```
D=T[:d]
```

such that

```
0<d<h,
d!=a,
C[:d]=C[-d:]=D,
T[d]=3.                                          (4)
```

The seed-anchoring argument applied to the next root also gives

```
d<N_0.                                           (5)
```

Thus consecutive internal transitions define an edge

```
a -> d
```

between two distinct `3`-labelled cuts in the finite initial seed.
The end of the old carrier has the exact two-block suffix

```
U ends in D A.                                   (6)
```

## 3. A decreasing defect gives a strictly shorter carrier

Assume

```
d<a.
```

Since `A` and `D` are prefixes of the same word, write

```
A=D E
```

with `E` nonempty.  Equation (6) becomes

```
U ends in D D E.                                 (7)
```

More is true than the static square in (7).  The shorter prefix `C` is
itself a visible orbit state once the reset tower is in the late regime.
At its next cut,

```
T[h]=U[h]=A[0]=2,
```

so

```
cn(C)=2.                                         (8)
```

For `0<=j<d`, the actual symbols following `C` are

```
T[h+j]=A[j]=D[j].
```

Therefore the orbit from `C` emits all of `D`.  At the endpoint,

```
T[h+d]=A[d]=T[d]=3,
```

and hence

```
cn(C D)=3.                                       (9)
```

Since `C` ends in `D`, the word `C D` ends in `D^2`.  The word `D`
must be primitive: if `D=Z^m` with `m>=2`, then `D^2=Z^(2m)` would make
the value in (9) at least four.

The first deletion `C[1:]` terminates because it is one of the fixed
first-symbol deletion states in the all-terminating branch.  The word
`C` is bad because it is an actual state of the bad high orbit.
Consequently `(C,D)` is another maturation carrier, and

```
|C|=h<p=|U|.                                     (10)
```

This is a strict descent in carrier length, not merely in a root chosen
inside a static suffix.

## 4. The increasing residual

If

```
d>a,
```

write

```
D=A E
```

with `E` nonempty.  Equation (6) becomes

```
U ends in A E A.                                 (11)
```

The argument of Section 3 does not apply: the actual continuation after
`C` supplies only `A`, then reaches the state `U`; it does not supply the
remaining word `E`.  Thus `(C,D)` is not known to be a maturation
carrier.

There is nevertheless an exact post-promotion interpretation.  The next
root is

```
V=C A C A C.
```

Therefore

```
V A=(C A)^3=U^3,
V D=U^3 E.                                       (12)
```

The word `E` is precisely the nonempty orbit segment beginning with the
promoted `3` at phase `a` and ending just before the next `3`-labelled
cut at phase `d`.  Since `(V,D)` is the next maturation carrier,

```
cn(V D)=3,
V D ends in D^2.                                 (13)
```

Thus `D` is primitive by the same exponent-four argument as in Section
3.  Every primitive maximizing cube root `R` of `V D` has length

```
r=|R|<p.                                         (14)
```

Indeed (12) occurs fewer than `p` outputs after the promotion `U^3 3`,
and the post-promotion escape lemma in
`post_promotion_escape.md` excludes maximizing roots of length at least
`p` throughout that first block.

The literal primitive `D^2` and a primitive maximizing `R^3` are
co-terminal.  Put `g=gcd(d,r)`.  Fine--Wilf gives the exhaustive split

```
r=d,
r<d  and  2r+g<d,
r>d  and  r>d+g.                                 (15)
```

For `r!=d`, otherwise their common suffix of length
`min(2d,3r)` would reach the Fine--Wilf threshold and give a proper gcd
period to one of the primitive roots.  If `r<d`, the alternative
`2d<3r` would make threshold failure imply `d+g<r`, contradicting
`r<d`; hence `3r<=2d` and the middle inequality follows.  If `r>d`,
the common length is `2d`, giving the last inequality.

Equations (12)--(15) turn the increasing defect into a strict drop below
the old reset scale `p`, but they do not close the descent: the
large-root alternative `d+g<r<p` need not produce another maturation
carrier.  The form (11) remains the exact unresolved orientation.

## 5. Iterated suffix coding

For completeness, an internal run has a precise finite-defect encoding.
Let its successive reset roots and defects be

```
U_i,       p_i=|U_i|,       a_i<N_0,
U_(i+1)=U_i^3 with its final a_i symbols deleted.
```

Put `A_x=T[:x]`.  If

```
a_i+a_(i+1)+...+a_j < p_i,                       (12)
```

then repeated cancellation in the last copy gives

```
U_i ends in
A_(a_j) A_(a_(j-1)) ... A_(a_i).                 (13)
```

The proof is induction on `j-i`.  The base case is the border in (1).
For the induction step, the suffix of
`U_(i+1)=U_i^3[:-a_i]` lies in the final copy of `U_i` by (12);
removing the terminal `A_(a_i)` translates the asserted suffix one
level back.

If a finite block of defect symbols occurs three consecutive times and
the corresponding total raw length satisfies (12), equation (13) gives
a literal cubic suffix of `U_i`, contradicting `cn(U_i)=2`.

This last observation does not finish the finite graph: infinite
cube-free words over a finite alphabet exist, and no determinism of the
edge `a -> d` has been proved.  Treating the blocks `A_x` as abstract
weighted letters also loses raw boundary information; the Q21 and
length-37 quotient audits in `max_label_circular.md` exhibit that exact
failure.  A completion must therefore eliminate the increasing form
(11), or use the raw fixed-profile equations to show that every directed
cycle in the bounded defect graph creates a fitting cubic suffix.
