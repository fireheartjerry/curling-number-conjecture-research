# Fixed-profile inheritance in the canonical `A V A` branch

This note records a strict self-similarity consequence of the canonical
terminal-`2` form.  It does not close that branch.

## Setup

Let `Q` be a primitive binary circular word over `{2,3}` and suppose

```
Q=A V A,
0<|V|<|A|,
V is a suffix of A,
cn(Q)=cn(A)=1,
Q[0]=Q[1]=2.                                      (1)
```

Write `a=|A|`, `v=|V|`, and `n=2a+v`.  Assume the exact cube-label
equation

```
Q[j]=3  iff  a proper circular cube ends at cut j. (2)
```

Also retain the upper half of the exact proper circular profile:

```
no proper circular fourth power ends at any cut of Q.     (2a)
```

The factorization in (1) is the CLSW canonical form forced in the
remaining final-`2` terminal-prefix branch.  The proof below uses only
(1)--(2a), not square coverage at the other cuts.  Condition (2a) is
logically separate from the cube-indicator equivalence (2); both follow
from the ambient fixed-profile equation `pc_Q=Q`.

## Lemma 1 (early cube roots)

If a proper circular cube of root length `s` ends at a cut `j` with
`0<j<a`, then

```
s<j.                                               (3)
```

### Proof

The proper-power Fine--Wilf bound gives

```
2s+gcd(n,s)<n,
```

so `2s<n`.  If `s>=j`, the length-`2s` factor ending `j` symbols before
the cube endpoint is an `s`-root square contained in the cube.  That
endpoint is cut zero.  Since `2s<n`, this square is a suffix of the
finite word `Q`, contradicting `cn(Q)=1`.  Hence `s<j`.

## Theorem 2 (`A` inherits the cube-indicator fixed equation)

For every cut `0<=j<a`,

```
A[j]=3  iff  a proper circular cube of A ends at cut j.  (4)
```

### Proof

The word `A` is primitive because `cn(A)=1`.

First suppose an `s`-root proper circular cube of `A` ends at cut `j`.
The same early-root argument as Lemma 1, now applied to the finite word
`A` with `cn(A)=1`, gives

```
s<j.
```

The proper-power bound relative to the primitive period `a` gives

```
2s+gcd(a,s)<a.
```

Consequently `3s<a+j`.  Around the boundary between the final and
initial copies of `A` in the circular word `Q`, the context preceding
cut `j` is literally `A A[:j]`, of length `a+j`.  The whole cube lies
in that context, so the same cube occurs in `Q` at cut `j`.  Equation
(2) gives `Q[j]=A[j]=3`.

Conversely suppose `A[j]=Q[j]=3`.  Equation (2) supplies a proper
`s`-root circular cube of `Q` at cut `j`.  The case `j=0` is impossible
because `A[0]=Q[0]=2`, so take `0<j<a`.  Lemma 1 gives `s<j<a`.

The context from cut `-a` through cut `j` is exactly

```
A A[:j],
```

and has period `a`.  If the cube began before cut `-a`, this entire
factor of length `a+j` would also have period `s`.  Its length meets
the Fine--Wilf threshold because

```
a+j >= a+s-gcd(a,s).
```

Fine--Wilf would give period `gcd(a,s)<a` to a factor containing a
complete copy of `A`, contradicting the primitivity of `A`.  Therefore
the cube is wholly contained in `A A[:j]` and is a proper circular cube
of `A`.  This proves (4).

## Corollary 3 (normal form of a first prefix/suffix mismatch)

Assume `0<=j<v` is least with

```
V[j] != A[j].                                     (5)
```

Then necessarily

```
A[j]=2,  V[j]=3.                                  (6)
```

Every cube witnessing `V[j]=3` at the middle cut `E=a+j` begins before
the visible word

```
A A A[:j]
```

of length `2a+j`.

### Proof

Minimality of `j` identifies the circular context of `Q` from cut
`-a` through cut `E` with `A A A[:j]`.  If `A[j]=3`, Theorem 2 supplies
a cube of `A` at phase `j`; its proper span is below `2a`, so the same
cube is visible at cut `E`.  Equation (2) would force `V[j]=3`.
Therefore a mismatch cannot have direction `3 -> 2`, proving (6).

If a cube at `E` were contained in the displayed length-`2a+j` word,
it would be a cube in the `a`-periodic word `A^Z` at phase `j`.
Theorem 2 would then give `A[j]=3`, contradicting (6).  Hence every
such cube crosses its left boundary.

## Lemma 4 (scale gap after the first mismatch)

Let `r` be a root length of a cube from Corollary 3, and put

```
g=gcd(a,r),   G=gcd(n,r).
```

Then either `r=a`, or

```
r>a+j+g,                                         (7)
2r+G<n.                                          (8)
```

In the second branch, writing `r=a+d` gives

```
d>j+g,
2d+G<v,
m:=n-2r=v-2d>0.                                  (9)
```

### Proof

Corollary 3 gives `3r>2a+j`.  The length-`2a+j` overlap has periods
`a` and `r`.  If it met the Fine--Wilf threshold `a+r-g`, it would
give period `g` to a complete copy of the primitive word `A`.  This is
impossible when `g<a`.  Threshold failure is (7).

The only case with `g=a` is `r=a`: indeed the proper cube-span bound
(8) gives `r<n/2<3a/2`, so no larger multiple of `a` is possible.
Equation (8) is the proper-power bound for the primitive period `n`.
Substitution of `r=a+d` and `n=2a+v` gives (9).

## Lemma 5 (part of the same-scale branch)

Put `z=a-v`, so `A=D V` with `|D|=z`.  In the exceptional branch
`r=a`, the first mismatch cannot satisfy `j>z`.

### Proof

Assume `j>z`.  The root-`a` cube ends at `E=a+j`.  For every
`1<=t<=j-z`, it also ends at `E-t`.  To verify this without an implicit
extension claim, put `k=j-u` for `1<=u<=t`.  The only new equality
needed when the cube window is shifted `t` symbols left is

```
Q[E-3a-u]=Q[E-a-u].                              (10)
```

Modulo `n=2a+v`, the two positions in (10) are `v+k` and `k`.
Because `z<=k<j<v`, position `v+k` lies in the middle copy of `V` at
offset `k-z`.  Therefore

```
Q[v+k]=V[k-z]=A[k]=Q[k].                         (11)
```

The middle equality uses `V=A[z:]`; the equality with `A[k]` follows
from first-mismatch minimality, since `k<j`.

Take `t=j-z`.  An `a`-root cube then ends at the middle cut of offset
`z`.  Its displayed label is `V[z]=A[z]`, again because `z<j`.
The equality at mismatch offset zero gives

```
A[z]=V[0]=A[0]=2.
```

Thus a proper cube ends at a cut labelled `2`, contradicting (2).
Hence `j<=z`.

## Theorem 6 (first-copy fitting kills the strict scale gap)

Retain Corollary 3 and suppose the cube selected at the middle mismatch
is a first-copy fitting witness.  Thus, for `E=a+j`,

```
3r<=n+E-1.                                         (12)
```

Then the strict branch `r=a+d>a` in Lemma 4 is impossible.

### Proof

Suppose `d>0`.  The fitting inequality gives

```
3d<=v+j-1.
```

Put

```
ell=v+j-3d.
```

Then `ell>=1`.  Lemma 4 gives `d>j`, and hence

```
ell<v<a.
```

In the lift formed by one copy of `Q` followed by its prefix through
cut `E`, the cube begins at phase `ell`.  Using `Q=A V A` and the
first-mismatch equality `V[:j]=A[:j]`, its full word is

```
A[ell:] V A A A[:j].                              (13)
```

Consequently the suffix

```
W=V A A A[:j]                                     (14)
```

is a factor of the root-`r` cube and has period `r`.

The same word `W` has period `a`.  Its first `v` symbols are the suffix
`V` of `A`, and shifting them by `a` places them on the suffix `V` of
the first displayed `A`.  Shifting the following complete copy of `A`
by `a` places it on the next copy.  Shifting the next `j` symbols
places them on `A[:j]`.  These three ranges exhaust all comparisons
required for period `a`.

Let `g=gcd(a,r)=gcd(a,d)`.  The length of (14) meets the Fine--Wilf
threshold:

```
|W|-(a+r-g)
  =(2a+v+j)-(2a+d-g)
  =v+j-d+g
  >0.                                               (15)
```

Fine--Wilf gives period `g` to `W`.  The word `W` contains a complete
copy of `A`, so `A` has period `g`.  Lemma 4 gives `d<v/2<a`, and
therefore `g<a`.  Since `g` divides `a`, `A` is a nontrivial integral
power, contradicting `cn(A)=1`.

Thus every first-copy fitting cube at the first mismatch has root

```
r=a.                                                (16)
```

The fitting inequality is used to put the cube start at
`1<=ell<a`; without it, the full initial copy of `V` in (14) need not
lie inside the selected cube.

## Remaining branches

The exceptional same-scale cube `r=a` is real.  Lemma 5 eliminates
`j>z`, but `j=z` and `j<z` remain.  Executed code gives

```
A=2223,  V=223,  Q=22232232223,
```

where the first mismatch is at `j=2` and an `a`-root cube ends at the
middle cut.  The word is not a model of (2): a preceding `2`-cut has
an unwanted root-`4` cube.  Thus `r=a` must be eliminated using the
negative half of (2), not by the Fine--Wilf scale gap.

Theorem 6 closes the strict branch in the critical setting, so no
recursive `m=v-2d` descent is needed there.

## Lemma 7 (exact smaller maturation when `j=z`)

Suppose the remaining same-scale branch has `j=z=a-v`.  Then there are
nonempty words `D,C` such that

```
A=D D C,
V=D C,
D[0]=2,
C[0]=3.                                            (17)
```

Put `d=|D|` and `c=|C|`.  The word `D` is primitive.  At cut `2d`,
choose a proper cube root `s`; such a root exists because the displayed
letter there is `C[0]=3`.  Then `s<2d`, the witness is first-copy
fitting relative to the shorter word `A`, and `s!=d`.

If `s<d`, putting

```
g=gcd(d,s),
m=d-2s,
h=3s-d
```

gives

```
d>2s+g,
d<3s,
0<m<d/3,
h>0,
D=X H X H X,
|X|=m,
|H|=h,
H=suffix_h(D),
U:=H X is primitive,
D=X U^2,
suffix_h(A)!=H.                                   (18)
```

If `s>d`, putting `e=s-d` gives

```
e>gcd(d,s),
D has period e,
d<3e,
2e+gcd(|A|,s)<c.
```

Moreover, with

```
P=prefix_e(D), H=suffix_e(D), U=H D,
```

one has

```
U is primitive,
suffix_(2e)(C)=H P.                               (19)
```

### Proof

The first-mismatch equality through offset `z-1` says that the
length-`z` prefix of `V` is the length-`z` prefix `D` of `A`.
The mismatch itself has direction `2 -> 3` by Corollary 3.  This is
exactly (17).

If `D` were a nontrivial power, the literal factor `D^2` ending at cut
`2d` would have exponent at least four.  Its span is below `|Q|`, so it
would be a proper circular fourth power of `Q`, contradicting (2a).
Thus `D` is primitive.

Theorem 2 and the early-root proof inside it apply at cut `2d<a`.
They give `s<2d` and the primitive-span inequality

```
2s+gcd(|A|,s)<|A|.
```

Adding `s<2d` shows

```
3s<|A|+2d-gcd(|A|,s),
```

so the cube fits in the first-copy lift of `A` through cut `2d`.

If `s=d`, the cube needs a copy of `D` immediately before the displayed
`D^2`, so

```
suffix_d(D D C)=D.                                 (20)
```

If `c<d`, taking the final `c` letters in (20) gives
`C=suffix_c(D)`.  The final displayed `D C` in `A=D D C` then ends in
`C^2`, contradicting `cn(A)=1`.  Therefore `c>=d`; now (20) says that
`C` ends in `D`.  Write `C=K D`.  Then

```
A=D D K D,
V=D K D,
A V=D D K D D K D
```

has suffix `A`, so `Q=A V A` has suffix `A^2`.  This contradicts
`cn(Q)=1`.

Assume `s<d`.  If the root-`s` cube began before the displayed `D^2`,
their common length-`2d` suffix would have periods `d` and `s` and
would meet the Fine--Wilf threshold `d+s-gcd(d,s)`.  A complete copy
of the primitive word `D` would acquire a proper gcd period.  Hence
the cube is contained in `D^2`.

If `3s<=d`, the same cube occurs in each copy of `D` and therefore ends
at cut `d`, whose displayed letter is `D[0]=2`; this contradicts the
cube-label equation.  Thus `d<3s`.

The contained cube and `D^2` have a common suffix of length `3s`.  If
`2s+gcd(d,s)>=d`, this length meets the Fine--Wilf threshold and again
makes `D` imprimitive.  Therefore `d>2s+g`, which makes `m,h`
positive and gives `m<d/3`.

The cube begins `h=3s-d` symbols before the final copy of `D`, so with
`H=suffix_h(D)` it is

```
H D=U^3.
```

Since `|U|=s=h+m`, write `U=H X`.  Left cancellation gives the word
equation in (18).

The same equation can be regrouped as `D=X(HX)^2=XU^2`.  The root
`U` is primitive: if `U` were a nontrivial integral power, the
displayed `U^3` would contain a proper fourth power at cut `2d`,
contradicting (2a).  At cut `d`, the final two roots are again `U^2`.
The preceding root would be completed exactly when the `h` circular
letters before the initial `X` equal `H`, namely when
`suffix_h(A)=H`.  Such a cube is forbidden because the label at cut
`d` is `D[0]=2`.  This proves the last inequality in (18).

Finally assume `s>d` and put `e=s-d`.  The common suffix `D^2` has
periods `d` and `s`.  Fine--Wilf would make `D` imprimitive if
`s<=d+gcd(d,s)`, so `e>gcd(d,s)`.  The period-difference lemma applied
to this length-`2d` word gives period `e` to its length-`d` prefix and
suffix, both equal to `D`.

If `3e<d`, the length-`3e` prefix of `D` is an `e`-root cube ending at
cut `3e`, while period `e` gives `D[3e]=D[0]=2`.  If `3e=d`, the whole
prefix `D` is an `e`-root cube ending at cut `d`, whose displayed
letter is again `D[0]=2`.  Both alternatives contradict the exact
profile, so `d<3e`.

Substitution of `s=d+e` and `|A|=2d+c` in the primitive-span
inequality gives the last inequality in (19).

For the final word equation, the last root of the selected cube is

```
U=H D,       H=suffix_e(D).
```

The preceding root begins `2e` letters before the end of `C` and is

```
suffix_(2e)(C) D[:d-e].
```

Because `D` has period `e`,

```
D[:d-e]=D[e:].
```

Equating the two roots and cancelling this common suffix gives
`suffix_(2e)(C)=H P`, where `P=prefix_e(D)`.  The inequality already
proved in (19) ensures `c>2e`, so this suffix is defined.  As in the
smaller-root branch, `U` must be primitive by (2a).

## Lemma 8 (exact normal forms when `j<z`)

Suppose the remaining same-scale branch has `j<z=a-v`, and put

```
delta=z-j.
```

Then

```
A[j:]=A[v+j:] V,                                  (21)
delta<v,
A[j:z]=suffix_delta(V).                           (22)
```

In particular `z!=v`.  More explicitly:

* if `z<v`, there are words `P,S,M`, with `S,M` nonempty, such that

  ```
  A=P S P M S,
  V=P M S,
  |P|=j, |S|=delta, |M|=v-z,
  S[0]=2, M[0]=3;                                 (23)
  ```

* if `z>v`, there are nonempty words `U,B,C` such that

  ```
  A=U B B C U B C,
  V=U B C,
  |U|=j-(z-v), |B|=z-v, |C|=v-j,
  B[0]=2, C[0]=3.                                 (24)
  ```

Let `k=z+j`.  The length-`z` circular left contexts at cuts `j` and
`k` of `A` are identical.  Hence every cube root `s` at the required
`3`-cut `k` satisfies

```
3s>z.                                             (25)
```

### Proof

Read the root-`a` cube ending at `E=a+j` in the lift of `Q`.  Its three
root blocks are

```
A[v+j:] V A[:j],
A[j:] A[:j],
A[j:] V[:j].
```

The last two are equal because `V[:j]=A[:j]`.  Equality of the first
two and right cancellation of `A[:j]` gives (21).

Equation (21) says that the suffix `A[j:]`, of length `v+delta`, has
period `v`.  If `delta>=v`, its final `2v` letters would be `V^2`,
contradicting `cn(A)=1`.  Thus `delta<v`.  Comparing the first
`delta` letters in (21) gives the second equation in (22).

Put `P=A[:j]=V[:j]` and `S=A[j:z]`.  If `z<v`, the prefix `P` and
suffix `S` of `V` are disjoint; the intervening word `M` has length
`v-z>0`.  Thus `V=P M S` and `A=P S V`, which gives (23).
The mismatch orientation gives `S[0]=2` and `M[0]=3`.

If `z=v`, (22) gives `V=A[:z]`, contradicting the mismatch at `j`.
Now suppose `z>v`.  Set `h=z-v` and `q=j-h`; the inequality
`delta<v` gives `q>0`.  Decompose

```
V=U B C
```

at lengths `|U|=q`, `|B|=h`, and `|C|=v-j`.  Then
`P=U B` and `S=B C`, so `A=P S V` gives (24).  Here all three words
are nonempty, and the mismatch orientation gives the displayed first
letters.

It remains to compare the contexts at `j` and `k=z+j`.  For
`1<=t<=j`, first-mismatch minimality gives

```
A[j-t]=V[j-t]=A[z+j-t].
```

For `j<t<=z`, both `z+j-t` and `a+j-t` lie in `A[j:]` and differ by
`v`; the period-`v` conclusion from (21) gives

```
A[z+j-t]=A[a+j-t].
```

These two ranges prove equality of the preceding length-`z` circular
contexts.  The displayed letters are `A[j]=2` and
`A[k]=V[j]=3`.  Theorem 2 therefore requires a proper cube at cut
`k` and forbids one at cut `j`.  A cube at `k` of span at most `z`
would copy verbatim to cut `j`; consequently its span must exceed
`z`, proving (25).

## Lemma 9 (a primitive square-to-cube child when `j<z`)

Under Lemma 8, put `k=z+j` and let

```
B=A[j:k],       |B|=z.
```

Then a proper circular square `B^2` ends at cut `k`, its midpoint cut
`j` is labelled `2`, its endpoint cut `k` is labelled `3`, and `B` is
primitive.

Let `s` be any cube root at cut `k`, and put

```
g=gcd(z,s),      G=gcd(a,s).
```

Exactly one of the following three scale regimes holds.

1. If `s<z`, then

   ```
   z>2s+g,       z<3s.                            (26)
   ```

   With `m=z-2s` and `h=3s-z`, there are nonempty words `X,H`
   such that

   ```
   B=X H X H X=X(HX)^2,
   |X|=m, |H|=h, H=suffix_h(B),                  (27)
   ```

   and `HX` is primitive.

2. If `s=z`, then

   ```
   z+gcd(a,z)<v.                                 (28)
   ```

3. If `s>z`, put `e=s-z`.  Then

   ```
   e>g,
   B has period e,
   z<3e,
   2e+G<v-z.                                     (29)
   ```

   In the normal form (23), put

   ```
   P_B=prefix_e(B), H_B=suffix_e(B).
   ```

   Then the complement `M` satisfies

   ```
   suffix_(2e)(M)=H_B P_B,                       (29a)
   ```

   and `H_B B` is a primitive word.

In particular, if `z>v`, only regime 1 can occur, and its cube root
satisfies `s<z/2`.

### Proof

Lemma 8 says that the length-`z` blocks immediately before cuts `j`
and `k` are equal.  These blocks are adjacent because `k-j=z`;
therefore they form `B^2`.  Its second copy is `A[j:k]=B`, so
`B[0]=A[j]=2`, while `A[k]=3`.

If `B` were a nontrivial integral power, `B^2` would be a fourth power
ending at cut `k`.  Its length is `2z<a+k`, so the factor fits in the
`A A[:k]` context inside the circular word `Q`.  This contradicts
(2a), proving that `B` is primitive.

Assume first that `s<z`.  If the cube began before the displayed
`B^2`, the full `B^2` would have periods `z` and `s`.  Fine--Wilf
would give it period `g`, making primitive `B` an integral power.
Thus the cube is contained in `B^2`.

If `3s<=z`, the cube lies in the final copy of `B`; translation left
by `z` copies it to a cube ending at the `2`-cut `j`.  Hence `z<3s`.
If `2s+g>=z`, the common suffix of the cube and `B^2`, of length
`3s`, meets the Fine--Wilf threshold `z+s-g`.  It contains a complete
copy of `B`, so period `g` again makes `B` an integral power.  This
proves (26).

Now put `m=z-2s` and `h=3s-z`.  The cube begins `h` letters before
the final copy of `B`, so, with `H=suffix_h(B)`, it is

```
H B=U^3.
```

Since `s=h+m`, write `U=H X` and cancel the initial `H`; this gives
(27).  The root `U=HX` is primitive, since otherwise `U^3` would
contain a proper fourth power at cut `k`, contrary to (2a).

If `s=z`, the proper-power span bound in primitive `A` is

```
2z+gcd(a,z)<a=v+z,
```

which is (28).

Finally suppose `s>z`.  The early-root argument applied to `A` at cut
`k` gives `s<k=z+j<2z`.  Thus `B^2` has the two genuine periods `z`
and `s`.  If `s<=z+g`, Fine--Wilf makes `B` an integral power.
Consequently `e=s-z>g`.  The period-difference lemma gives period `e`
to the length-`z` prefix and suffix of `B^2`, both equal to `B`.

If `3e<z`, the prefix `e`-root cube of `B` ends at cut `j+3e`.
Period `e` gives its displayed letter

```
A[j+3e]=B[3e]=B[0]=2,
```

contradicting (2).  Equality `3e=z` would make `B` an integral power,
so `z<3e`.  Substitution of `s=z+e` and `a=v+z` in the proper-power
span bound gives the last inequality in (29).

This inequality gives `|M|=v-z>2e`.  Rotating `A` to cut `k` gives

```
M B B.
```

The last root of the selected cube is `H_B B`.  The preceding root is

```
suffix_(2e)(M) B[:z-e].
```

Since period `e` gives `B[:z-e]=B[e:]`, equality of these roots and
right cancellation gives (29a).  The root `H_B B` is primitive by
(2a).

Regimes 2 and 3 both force `z<v`; hence `z>v` leaves regime 1.
The strict inequality `z>2s+g` then gives `s<z/2`.

## Lemma 10 (the same-root child is impossible)

In Lemma 9, regime 2 (`s=z`) cannot occur.

### Proof

Equation (28) gives `z<v`, so use the normal form (23):

```
A=P S P M S,       V=P M S.
```

Put `B=S P`, as in Lemma 9, and `c=|M|=v-z>0`.  Rotating `A` to cut
`j=|P|` gives the circular presentation

```
B M B.
```

The root-`z` cube ending after the initial displayed `B` already uses
the final displayed `B` as its preceding root.  Its third root is the
length-`z` suffix of `B M`.  Hence there is a word `K`, of length `c`,
such that

```
B M=K B,
S P M=K S P.                                      (30)
```

Set `L=P M`.  The second equation is

```
S L=K S P.
```

Its right side ends in `P`.  Since `|L|=|P|+c>=|P|`, the same suffix
lies wholly in `L`; write `L=R P`.  (When `P` is empty, take
`R=L`.)  It follows that

```
V=P M S=L S=R P S.
```

Thus `V` ends in `D:=P S=A[:z]`.  Write `V=R D`.  Then

```
A=D V=D R D,
A V=D R D R D,
```

so `A V` ends in `A`.  Consequently `Q=A V A` has suffix `A^2`,
contradicting `cn(Q)=1`.

## Lemma 11 (the upward child exposes a smaller internal square)

Consider either upward regime: `s=d+e>d` in Lemma 7 or
`s=z+e>z` in Lemma 9.  Write the corresponding square root as `B`
and its length as `r`:

```
(B,r,C)=(D,d,C)       in Lemma 7,
(B,r,C)=(B,z,M)       in Lemma 9.
```

Then

```
e<r<2e.                                             (31)
```

Put `b=r-e`, and define nonempty words `R,T` by

```
B=R T R,
|R|=b,
|T|=e-b.
```

The word `R` is primitive, and the complement has the exact suffix

```
suffix_(2e)(C)=T R R T.                            (32)
```

Thus a primitive square `R^2`, of root length

```
b=r-e<r/2,
```

occurs inside the complement.  Its midpoint cut is labelled `2`; its
endpoint cut is labelled `T[0]`.  If `T[0]=3`, this is another
square-to-cube node at the strictly smaller scale `b`.

### Proof

Both upward regimes give `e<r`: in Lemma 7 this follows from `s<2d`,
and in Lemma 9 from `s<2z`.  They also give period `e` to `B`, and the
suffix equation

```
suffix_(2e)(C)=H P,
P=prefix_e(B), H=suffix_e(B).                     (33)
```

Use the circular presentation `C B^2`, ending at the structural
`3`-cut.  Equation (33) puts a copy of `P` at the end of `C`.
If `2e<r`, period `e` makes the first `2e` letters of the first
displayed `B` equal to `P^2`.  Hence `P^3` ends at the cut exactly
`2e` letters into that copy of `B`.  The cut is strictly internal, and
its displayed letter is

```
B[2e]=B[0]=2.
```

This contradicts (2).  If `2e=r`, the same `P^3` ends at the midpoint
between the two displayed copies of `B`, whose displayed letter is
again the first letter `B[0]=2`; equivalently, `B=P^2` also contradicts
the primitivity of `B`.  Thus both `2e<=r` cases are discharged, proving
(31).

Period `e` now says that `B` has a border of length `b=r-e`.  With
`R` equal to that common prefix and suffix, write

```
P=R T.
```

The positive length of `T` follows from `r<2e`.  Then

```
B=P R=R T R,
H=T R,
H P=T R R T,
```

which proves (32).

If `R` were a nontrivial integral power, the visible factor `R^2`
would contain a proper fourth power, contradicting (2a).  Thus `R` is
primitive.  The letter after the first copy of `R` in (32) is
`R[0]=B[0]=2`; the letter after the second copy is `T[0]`.  These are
exactly the midpoint and endpoint labels claimed.

## Lemma 12 (both endpoint labels after the upward reduction)

Retain Lemma 11 and put `t=|T|`, `b=|R|`.  The endpoint `h` of the
literal `R^2` and its midpoint `m=h-b` have the following coordinates
inside the inherited word `A`:

```
h=a-t,       m=a-e                 in Lemma 7,     (34)
h=v+j-t,     m=v+j-e               in Lemma 9.     (35)
```

In both cases

```
0<m<h<a,
A[m]=2,
A[h]=T[0].                                        (36)
```

If `T[0]=3`, the occurrence `(h,R^2)` is an exact smaller
square-to-cube node: `R` is primitive, its midpoint is a `2`-cut, its
endpoint is a `3`-cut, and every cube root `q` supplied at `h` by
Theorem 2 is first-copy fitting relative to `A`:

```
3q<=a+h-1.                                        (37)
```

If `T[0]=2`, restore the ambient square/fitting part of the critical
profile.  It supplies a first-copy fitting square root `q` at the
midpoint `m`, and necessarily

```
q!=b.                                             (38)
```

Thus the negative cube condition at `h` forces a distinct low-square
endpoint at `m`; it cannot terminate the ancestry at the same root.

### Proof

In Lemma 7 the complement `C` is the final word of `A=D^2C`.
Its suffix (32) ends with a final copy of `T`, so the endpoint of
`R^2` is `t` letters before cut `a`; its midpoint is a further `b`
letters earlier.  Since `e=t+b`, this is (34).

In Lemma 9, rotating at cut `k=z+j` gives `M B^2`.  The word `M`
ends at lifted cut

```
k+|M|=z+j+(v-z)=v+j<a.
```

The same subtraction gives (35).  The inequalities
`|C|>2e` in Lemma 7 and `|M|>2e` in Lemma 9 put both cuts strictly
inside the displayed complement, proving the coordinate bounds in
(36).  The labels follow directly from the factor `T R R T`.

Suppose `T[0]=3`.  Theorem 2 supplies a proper cube of `A` at `h`;
let its root length be `q`.  The early-root argument gives `q<h`,
while the proper-power bound gives

```
2q+gcd(a,q)<a.
```

Adding these strict integer inequalities yields (37).  Lemma 11
already proves every other square-to-cube hypothesis, including the
strict scale drop `b<r/2`.

Finally suppose `T[0]=2`.  The literal `R^2` is a fitting square at
the low endpoint `h`.  The ambient fixed profile and first-copy
fitting condition supply a fitting square at the other low cut `m`;
call its root length `q`.  If `q=b`, the square ending at `m` contributes
a copy of `R` immediately before the two displayed copies in (32).
A proper cube `R^3` would then end at `h`, contradicting
`A[h]=2` and (2).  Therefore (38) holds.

## Lemma 13 (exact continuation from the `T[0]=2` endpoint)

Assume the `T[0]=2` branch of Lemma 12.  If `b=1`, then `R` is the
one-letter word `2`.  If `b>1`, let

```
a_0=h-d
```

be the last `3`-cut inside the final copy of `R` in `R^2`.  Then

```
1<=d<=3,       d<=b.                               (39)
```

For any first-copy fitting cube root `u` at `a_0`, the square at

```
a_0-u
```

is first-copy fitting and ends at a `2`-cut.  Moreover `u!=b`, and
exactly one of the following holds:

```
u<b:
    b>2u+gcd(b,u), so u<b/2,
    and the u-cube is contained in R^2;             (40)

u>b:
    u>b+gcd(b,u)-d,
    and the u-cube crosses the left boundary of R^2. (41)
```

Thus the negative endpoint has an exact dichotomy: either it produces
a fitting child below half scale, or it leaves the explicit crossing
ascent (41).  The low-midpoint square from Lemma 12 alone does not
exclude the second branch.

### Proof

For `b>1`, primitivity prevents `R` from being the constant word
`2^b`, so the final copy of `R` contains a `3`.  By choice of `a_0`,
all phases from `a_0+1` through `h` are labelled `2`.  Four consecutive
`2` terms would form a proper fourth power of root one, contrary to
(2a), proving `d<=3`; the location inside the final root gives `d<=b`.

The cube at `a_0` is followed by a `2`-cut.  Its first two roots form
a square ending at `a_0-u`.  If that midpoint were labelled `3`, the
period-`u` cube would extend one symbol to the right and end at
`a_0+1`, a `2`-cut.  Hence the midpoint is labelled `2`.  If the cube
fits with

```
3u<=n+a_0-1,
```

then

```
2u<=n+(a_0-u)-1,
```

so the child square also fits.

If `u=b`, the root-`b` cube ending at `h-d` and the root-`b` square
ending at `h` overlap in `2b-d>=b` symbols.  Their period-`b` union
contains a root-`b` cube ending at the `2`-cut `h`, a contradiction.

Suppose `u<b`.  If the cube is contained in `R^2`, its length-`3u`
factor has periods `b` and `u`.  Fine--Wilf and the primitivity of
`R` give

```
b>2u+gcd(b,u).
```

If instead the cube crosses the left boundary, its overlap with
`R^2` has length `2b-d`.  Fine--Wilf gives the same contradiction
unless

```
b-u+gcd(b,u)<d.                                    (42)
```

Since `b-u>=1`, `gcd(b,u)>=1`, and `d<=3`, the only possible integer
escape is

```
d=3, u=b-1, gcd(b,u)=1.
```

On the overlap of length `2b-3`, periods `b` and `b-1` identify
positions `0,...,b-3,b-1,...,2b-4` in one component.  The root-`b`
square gives

```
A[h-b-3]=A[h-3]=3,
A[h-b-1]=A[h-1]=2.
```

The two left positions have overlap coordinates `b-3` and `b-1`,
which lie in that same component, a contradiction.  Therefore the
crossing case is impossible and (40) holds.

Finally suppose `u>b`.  The cube cannot be contained in `R^2`.
The same overlap has periods `b` and `u`.  If its length met the
Fine--Wilf threshold `b+u-gcd(b,u)`, it would contain complete
conjugates of both primitive roots and give them the common proper gcd
period.  Threshold failure is exactly (41).

## Lemma 14 (the enclosing cube makes every exit a giant ascent)

In the upward regime of Lemma 11, put

```
s=r+e,       t=|T|,       b=|R|.
```

The selected primitive root-`s` cube has root word

```
U=T R R T R                                  (43)
```

and therefore contains, in each copy of `U`, the low square `R^2`
from Lemma 12.  Assume `T[0]=2` and `b>1`.  In the final copy of `U`,
let `a_*` be the last `3`-cut in the final root of that `R^2`, at
distance `d` from its endpoint as in Lemma 13.  For every cube root
`u` at `a_*`, with `g=gcd(s,u)`, exactly one of the following holds:

```
the u-cube is contained in U^3:
    s>2u+g, and hence u<s/2;                        (44)

the u-cube crosses the left boundary of U^3:
    either u=s,
    or u>s+r-d+g.                                  (45)
```

Thus an ancestry ascent which exits the enclosing cube jumps from below
`s/2` either to the repeated outer scale `s` or to strictly above
`s+r-d`; there is no other intermediate root scale.

### Proof

From Lemma 11,

```
B=R T R,       H=T R,
```

so the selected cube root is

```
U=H B=T R R T R.
```

Its length is `s=r+e`.  The endpoint of the displayed `R^2` is
`r=t+2b` letters into each copy of `U`.  Let the outer `U^3` occupy
the lifted interval `[L,K]`, where `K-L=3s`.  In the final copy of
`U`, the chosen inner cube ends at

```
a_*=L+2s+r-d.                                      (46)
```

If its start is at or after `L`, then `3u<=3s`, so `u<=s`.
Equality is impossible: a length-`3s` subinterval of the
length-`3s` interval `[L,K]` must equal `[L,K]`, whereas its right
endpoint `a_*=L+2s+r-d` is strictly below `K` because `r-d<s`.
Hence `u<s`.  The full root-`u` cube has periods `s` and `u`.  If

```
s<=2u+g,
```

its length meets the Fine--Wilf threshold `s+u-g` and contains a
complete conjugate of the primitive root `U`.  Fine--Wilf gives that
conjugate the proper gcd period, a contradiction.  This proves (44).

If the inner cube begins before `L`, its intersection with `U^3` is
the interval `[L,a_*]`, of length

```
2s+r-d.
```

This overlap has periods `s` and `u`.  If `u=s`, this is the
exception displayed in (45).  Suppose `u!=s`.  If the overlap met the
Fine--Wilf threshold `s+u-g`, then its length, being at least both
`s` and `u`, would contain complete conjugates of both primitive
roots.  Fine--Wilf would give at least one of them the proper period
`g<max(s,u)`, a contradiction.  Therefore

```
2s+r-d<s+u-g,
```

which is exactly (45).

## Lemma 15 (the repeated outer scale cannot persist one copy left)

Retain Lemma 14.  For `i=0,1,2`, let

```
a_i=L+i*s+r-d
```

be the corresponding last `3`-cut in the final `R` of the displayed
`R^2` in copy `i+1` of `U`.  Suppose the cube selected at `a_2` has
root length `s`, the exceptional branch of (45).  For every cube root
`w` at `a_1`, with `g=gcd(s,w)`, exactly one of the following holds:

```
the w-cube is contained in the s-cube ending at a_2:
    s>2w+g, and hence w<s/2;                        (47)

the w-cube crosses the left boundary of that s-cube:
    w>s+g.                                         (48)
```

In particular, `w=s` is impossible.

### Proof

Put

```
delta=s-r+d.
```

The inequalities `d<=b<r<s` give `0<delta<s`.  The root-`s` cube
ending at `a_2` occupies

```
I=[L-delta,K-delta],
```

and `a_1=L+2s-delta`.  If a root-`s` cube also ended at `a_1`, its
interval would be

```
[L-s-delta,L+2s-delta].
```

The union of these two overlapping period-`s` intervals is
`[L-s-delta,K-delta]`, of length `4s`.  It is a fourth power ending
at `a_2`, contrary to (2a).  Hence `w!=s`.

If the root-`w` cube is contained in `I`, then `3w<=2s`, so `w<s`.
The cube has periods `s` and `w`.  If `s<=2w+g`, its length meets the
Fine--Wilf threshold `s+w-g` and contains a complete conjugate of
the primitive word `U`.  Fine--Wilf gives that conjugate the proper
period `g<s`, a contradiction.  This proves (47).

If the root-`w` cube crosses the left endpoint of `I`, its intersection
with `I` is `[L-delta,a_1]`, of length `2s`.  This intersection has
periods `s` and `w`.  Since `w!=s`, meeting the Fine--Wilf threshold
would give a complete conjugate of the longer primitive root the
proper period `g<max(s,w)`.  Therefore

```
2s<s+w-g,
```

which is (48).

## Executed calibration

`research/audit_canonical_ava.py` enumerates the canonical form and
recomputes every curling number with both implementations in
`curling.py`.  `research/analyze_clsw_terminal_form.py` reports the
exact failed cube-profile cuts.  The displayed same-scale example and
all numeric data in this note were obtained from those executions.
