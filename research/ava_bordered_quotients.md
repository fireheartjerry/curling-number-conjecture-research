# Euclidean quotients of the bordered root in the `j=z` low branch

This note continues the `s<d` branch of Lemma 7 in
`ava_fixed_inheritance.md`.  It proves an exhaustive quotient split for
the bordered primitive root.  The split either contradicts the exact
profile or exposes a strictly smaller primitive square occurrence.  It
does not by itself prove that every subsequent ancestry edge decreases
in scale.

## Hypotheses inherited from Lemma 7

Inside

```
A=D D C,
D[0]=2,
C[0]=3,
```

suppose

```
D=X H X H X=XU^2,
U=H X,
|X|=m,
|H|=h,
H=suffix_h(D),
m>gcd(m,h).                                         (1)
```

The word `U` is primitive.  Every cut used below lies strictly inside
the displayed `D D` prefix of `A`.  At such a cut, the inherited exact
profile has the following two consequences:

```
label 2: no cube ends at the cut;
label 3: a cube ends there and no fourth power ends there.   (2)
```

There is no fourth power at a cut with either label.

## Lemma 1 (complete border normal form)

There are nonempty words `P,T` and a word `R=P T` such that, for one
and only one `q` in `{0,1,2}`,

```
h=q m+r,                  0<r<m,
P=prefix_r(R),
X=T P,
H=R^q P,
U=R^(q+1) P.                                      (3)
```

### Proof

Because `h<|U|=m+h`, the suffix condition in (1) gives

```
suffix_h(U)=suffix_h(D)=H=prefix_h(U).
```

Thus `U` has period `|U|-h=m`.

The inequality `h<3m` follows from the negative fourth-power profile.
If `h>=3m`, the first `4m` letters of the first displayed copy of `U`
would be four consecutive copies of `R:=prefix_m(U)`.  This fourth
power ends inside the first copy of `D`, contradicting (2).

The inequality in (1) excludes divisibility of `h` by `m`, because
`m|h` would give `gcd(m,h)=m`.  Euclidean division therefore gives

```
h=q m+r,        q in {0,1,2},        0<r<m.
```

Period `m` gives

```
U=R^(q+1)P,             P=prefix_r(R).
```

Write `R=P T`; both factors are nonempty.  Comparing this expression
with `U=H X` gives

```
H=R^qP,                 X=T P.
```

Euclidean division makes `q` unique, proving (3).

## Lemma 2 (the quotient `q=2` is impossible)

The alternative

```
H=R^2P,       U=R^3P
```

contradicts the negative fourth-power profile.

### Proof

The final copy of `U` in the first `D` is followed by the prefix `T`
of the next `D`, since that next copy begins with `X=T P`.  The
resulting factor is

```
R^3 P T=R^4.
```

It ends at cut

```
|D|+m-r,
```

strictly between the two ends of the displayed `D D`.  This is a
proper fourth power, contradicting (2).

## Lemma 3 (the quotient `q=1` gives a smaller exact maturation)

In the alternative

```
H=R P,       U=R^2P,
```

one necessarily has

```
r=1,
P=(3).
```

Writing `R=3T` and `X=T3`, the word `T` is nonempty and

```
T[0]=T[-1]=2.                                       (4)
```

Let `d=|D|`.  Then:

* the primitive root `X` occurs squared at the low cut `d`;
* its conjugate `R` occurs cubed at the high cut `d+m-1`;
* the exact maxima at these two cuts are respectively two and three.

Thus this quotient exposes an exact conjugacy-class square-to-cube
maturation of scale `m<d`.

### Proof

The final copy `U=R^2P` of the first `D`, followed by the prefix `T`
of the next `D`, is

```
R^2 P T=R^3.
```

This cube ends at cut `d+m-r`.  After appending a further prefix
`P[:i]`, for each `0<=i<r`, the preceding length `3m` factor remains
an `m`-root cube: it is a length-`3m` factor of the `m`-periodic word
`R^3P`.  The displayed labels at these cuts are

```
P[0],P[1],...,P[r-1].
```

Equation (2) forces every one of these letters to be `3`.  Hence
`P=3^r`.

At the internal boundary `X|U`, the suffix `P` of `X` is followed by
the prefix `P` of `U`.  The factor there is `P^2=3^(2r)`.  If `r>=2`,
it contains a root-one fourth power, contrary to (2).  Therefore
`r=1` and `P=(3)`.

The identity `D[0]=X[0]=2` gives `T[0]=2`.  If `T[-1]=3`, the last
letter of `T` followed by the two adjacent copies of `P` at `X|U`
would be a root-one cube.  Its endpoint label is the following letter
`T[0]=2`, contradicting (2).  This proves (4).

For `r=1`,

```
suffix_(2m)(U)=X^2.
```

Consequently `X^2` ends at cut `d`, whose displayed label is the first
letter of the next `D`, namely `X[0]=2`.  The preceding construction
gives `R^3` at cut `d+m-1`, whose displayed label is `R[0]=3`.

If `X` were a nontrivial integral power, the displayed `X^2` would
have exponent at least four at the low cut.  Thus `X` is primitive.
Conjugation preserves primitivity, so `R` is primitive.  Finally (2)
excludes a cube at the low cut and excludes a fourth power at the high
cut.  The exhibited powers therefore attain the exact maxima two and
three.

Both witnesses are first-copy fitting.  Here

```
d=|D|=5m+2.
```

The square interval is `[d-2m,d]`, and the cube interval is
`[d-2m-1,d+m-1]`.  Their left endpoints are nonnegative, and their
right endpoints occur before the end of the second displayed `D`.
Thus the lower-scale maturation is admissible in the fitting
occurrence graph, not merely as a circular power.

## Lemma 4 (the quotient `q=0` gives two smaller low square nodes)

In the alternative

```
H=P,       U=R P,
```

the word `P` is primitive.  Root-`P` squares end at the two cuts

```
m+r,              2m+2r,                          (5)
```

inside the first copy of `D`.  Both cuts have displayed label `2` and
exact maximum two.  Their root length satisfies

```
r<m<d.
```

If `P` contains no `3`, then `r=1`; otherwise the final copy of `P` in
either displayed square contains a high phase from which the local
square-ancestry construction may continue.

### Proof

With `R=P T` and `X=T P`, direct substitution gives

```
D=T P P T P P T P.                                 (6)
```

The first `P^2` in (6) ends at cut `m+r`, and the second ends at cut
`2m+2r`.  In both cases the next letter is `T[0]`.  Since

```
T[0]=X[0]=D[0]=2,
```

both endpoint labels are `2`.  Equation (2) excludes a cube at either
cut.  If `P` were a nontrivial integral power, the displayed `P^2`
would have exponent at least four, also contrary to (2).  Hence `P` is
primitive.

The quotient bounds give `0<r<m`, and (1) gives `m<d`.  A primitive
word over `{2,3}` which contains no `3` must be the one-letter word
`(2)`, proving the last assertion about `r`.  If `P` contains a `3`,
that phase lies in the final root of one of the two fitting squares in
(5), so the exact profile supplies its cube witness.

## Lemma 5 (the retained suffix defect bounds every outer ascent)

Keep the general hypotheses (1), put

```
s=|U|=m+h,
d=|D|=m+2s,
suffix_h(A)!=H.                                     (7)
```

The final displayed `U` in the low square `U^2` ending at cut `d` is
followed by the label `D[0]=2`.  Suppose it contains a `3`, and let
`a=d-delta` be its last `3`-phase.  Thus

```
1<=delta<=s,
A[a]=3,
A[a+1]=...=A[d]=2.
```

Let `w` be a cube root at cut `a`.  If `w<s`, then

```
s>2w+gcd(s,w),
```

and the cube is contained in `U^2`.  The case `w=s` is impossible.  If
`w>s`, write

```
w=s+e.
```

Then the cube crosses the distinguished origin of `A`, and the retained
suffix defect forces

```
e>m-delta.                                          (8)
```

More precisely, every ascent belongs to one of the two disjoint
regimes

```
m-delta<e<s-delta,             short escape;
e>=s-delta,                    long escape.         (9)
```

In the short escape, `prefix_(s-delta)(U)` has period `e`.

### Proof

The unequal-scale alternatives and the contained inequality are the
local Fine--Wilf edge trichotomy applied to the primitive low square
root `U`.  In the ascent branch,

```
a-3w
  < d-delta-3s
  =-h-delta<0,
```

so the cube crosses the origin.  The early-root argument from
`cn(A)=1` gives `w<a`.

The length-`h` suffix of `A`, viewed immediately before the origin in
the circular lift, lies inside this cube.  Translation by one cube
root therefore gives the exact identity

```
suffix_h(A)=U^2[e:e+h],                            (10)
```

where the right side is indexed from the beginning of the first `U`
in `D=XU^2`.

Assume for contradiction that `e<=m-delta`.  The intersection of the
cube and `U^2` is

```
U^2[:2s-delta].
```

It has periods `s` and `s+e`.  Since

```
e<=m-delta<s-delta,
```

the period-difference lemma gives period `e` to its prefix of length
`s-delta`, namely `prefix_(s-delta)(U)`.  The bound

```
e+h<=m-delta+h=s-delta
```

then makes (10) equal to

```
prefix_h(U)=H.
```

This contradicts (7), proving (8).  Splitting at `e=s-delta` gives
(9), and the same period-difference argument proves the last statement
in the short regime.

## Corollary 6 (exact short-escape data for `q=0`)

In quotient `q=0`, suppose `P` contains a `3`, and let `delta` be the
distance from the end of the final `P` in `U` to its last `3`-phase.
Thus `1<=delta<=r`.  In a short ascent from the outer low square
`U^2`, there is an integer `k` such that

```
e=m-delta+k,
1<=k<r,
k!=delta.                                           (11)
```

The first two roots of the ascending cube form an origin-crossing
square ending at cut

```
s-k.
```

Its displayed label supplies the forced letter

```
P[r-k]=2.                                           (12)
```

The suffix defect has the explicit form

```
suffix_r(A)
  =P[:r-k] P[r-delta:r-delta+k]                    if k<=delta,

suffix_r(A)
  =P[:r-k] P[r-delta:r] P[:k-delta]                if k>delta,    (13)
```

and this word is not `P`.

### Proof

Here `h=r` and `s=m+r`.  The short inequalities in (9) turn (8) into

```
m-delta<e<m+r-delta.
```

This is (11) except for `k!=delta`.

The square made by the first two cube roots ends at

```
a-w
 =d-delta-(s+e)
 =s-k.
```

Lemma 1 of `max_square_terminal_forest.md` makes its displayed label
`2`.  In the decomposition

```
D=(T P P)(T P P)(T P),
```

cut `s-k` lies in the second `P` of the first parenthesized block, at
letter `P[r-k]`.  This proves (12) and uses the earlier of the two
literal `P^2` occurrences.

For (13), apply (10) and the period-`e` prefix supplied by Lemma 5.
The first `r-k` letters of `U^2[e:e+r]` equal `P[:r-k]`.  Its remaining
`k` letters begin at phase `s-delta`: they first traverse the final
`delta` letters of the first `U`, then, if `k>delta`, the prefix of the
next `U`.  This is exactly (13).

If `k=delta`, either (12) would identify the last high letter
`P[r-delta]=3` with `2`, or (13) would give
`suffix_r(A)=P`.  Both conclusions contradict the hypotheses.

## Corollary 7 (exact ascent intervals for `q=1`)

In quotient `q=1`, where `r=1`, `H=R3`, and `s=2m+1`, every ascent from
the outer low square `U^2` has

```
m<=e<3m.                                            (14)
```

It is short exactly when `m<=e<2m`, and long exactly when
`2m<=e<3m`.  In the short case write

```
e=m-1+k,            1<=k<=m.
```

Then the first-two-roots square ends at cut `s-k`, and

```
k>=2,
R[m+1-k]=2.                                         (15)
```

### Proof

The final symbol of `U` is the one-letter word `P=(3)`, so
`delta=1`.  Lemma 5 gives `e>=m`.  The early-root inequality

```
s+e<a=d-1=m+2s-1
```

gives `e<3m`, proving (14).  The short/long split follows from
`s-delta=2m`.

In the short case the child square endpoint is again `s-k`.  For
`k=1`, this cut displays the first letter of the second copy of `R` in
`U=R^2 3`, namely `R[0]=3`.  Lemma 1 of
`max_square_terminal_forest.md` requires the label to be `2`, so
`k>=2`.  For such `k`, the displayed position inside the first copy of
`R` is `m+1-k`, proving (15).

## Exhaustive conclusion of the quotient split

The three cases in Lemmas 2--4 exhaust the bordered-root branch:

```
q=2: contradiction by an internal fourth power;
q=1: exact primitive maturation at scale m<d;
q=0: exact primitive low square nodes at scale r<m<d.
```

Lemma 5 and its corollaries isolate the remaining canonical leverage:
an ascent from the outer low square crosses the distinguished origin,
and the inherited suffix defect forces a strict period-difference
escape.  The short `q=0` escape also lands at a specified low letter in
the earlier `P^2`.  The long escapes in (9), and the short escapes
surviving (11)--(15), are not eliminated here.
