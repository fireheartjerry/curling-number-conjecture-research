# The minimal final-3 branch in CLSW normal form

This note assumes the standard primitive critically synchronized binary
word `P`, with `P[0]=2`, and the strict predecessor inequality supplied
by minimum seed length.  Put

```
P=T3,                 cn(T)<3,
Q=3T.
```

Thus `Q` is the right rotation of `P`, so it has the same proper circular
profile.  In particular

```
Q[0]=3,               Q[1]=2.                    (1)
```

No numerical curling number is asserted in this note.  Every occurrence
of `cn` below is derived symbolically from a displayed suffix power and
the strict predecessor bound.

## 1. The wrapping terminal cube

Let a proper circular cube of root length `q<|Q|=n` end immediately
before `Q[0]`.  Since `T` has curling number below three, this cube cannot
fit in the `n-1` symbols preceding the final `3` in the original
distinguished lift.  Therefore

```
3q>=n.
```

Put

```
h=3q-n.
```

The case `h=0` would make `Q` a whole cube, contradicting primitivity.
The proper-power span lemma gives

```
3q<n+q-gcd(n,q),
```

and hence

```
1<=h<q.                                            (2)
```

Let

```
A=suffix_h(Q).
```

In the periodic lift, the terminal cube is exactly

```
A Q=Z^3                                           (3)
```

for a length-`q` word `Z`.  Because `h<q`, splitting (3) at the first
root boundary gives

```
A=prefix_h(Z),
Q=Z[h:] Z^2.                                      (4)
```

Since `A` is also the length-`h` suffix of `Q` and `Q` ends in `Z`,

```
A=suffix_h(Z).                                    (5)
```

Thus `A` is a nonempty proper border of `Z`.

Put

```
X=Z[h:].
```

Equations (4)--(5) give the exact canonical form

```
Z=A X,
Q=X(A X)^2=X A X A X.                            (6)
```

This is the `k=2` non-robust normal form in Theorem 18 of Chaffin,
Linderman, Sloane and Wilks (CLSW), *On Curling Numbers of Integer
Sequences*, JIS 16 (2013), Article 13.4.3.  Here it follows directly
from the fact that the selected proper cube is the whole word `AQ`,
so no choice of a non-robust witness is hidden.

## 2. Exact finite curling numbers of the canonical blocks

Every power suffix of `Q` with exponent at least three would also be a
power suffix of `T=Q[1:]`, unless it used the first symbol of `Q`.
In the latter case the powered suffix starts at zero and is all of `Q`,
contradicting primitivity.  Hence

```
cn(Q)<=2.
```

Equation (6) displays the square suffix `Z^2`, so

```
cn(Q)=2.                                           (7)
```

An earlier draft incorrectly inferred `cn(Z)=1` from (7).  If a word
`Z` merely has a square *suffix*, the two copies in `Z^2` need not join
those suffixes into a fourth power; the intervening prefix of the second
copy can break that repetition.

What follows rigorously is

```
cn(Z),cn(X) in {1,2}.                              (8)
```

Indeed, both `Z` and `X` are suffixes of `T=Q[1:]`, and `cn(T)<3`.
The root `Z` is primitive for a different reason: if `Z=U^d` with
`d>=2`, the proper circular cube `Z^3` would be the power `U^(3d)` at a
cut whose exact profile value is three.

The executed audit `research/audit_final_three_upstream.py` records the
concrete algebraic countermodel

```
X=322,   A=2,   Z=2322,   Q=32223222322,
```

for which both independent implementations return

```
cn(X)=cn(Z)=cn(Q)=cn(Q[1:])=2.
```

It obeys (1)--(7), including `AQ=Z^3`; it fails the full circular profile
at another cut.  Thus the full profile may still eliminate this branch,
but equations (1)--(7) alone do not establish the curling-one hypotheses
used below.

## 3. The two seam symbols

The cube `Z^3` in (3) ends at cut zero, whose label is `Q[0]=3`.
If the first symbol of `Z`, equivalently `A[0]`, were also `3`, appending
`Q[0]` would shift the complete cube one symbol to the right.  A
`Z`-root cube would then end at cut one, contradicting `Q[1]=2`.
Therefore

```
A[0]=2.                                           (9)
```

Equation (6) and (1) also give

```
X[0]=3.                                           (10)
```

Thus the selected terminal cube has the pointed nonextension

```
Z^3 3 2,
Z=A X,
A[0]=2,
X[0]=3.                                          (11)
```

## 4. Exact quotient of the border length

The border `A` gives period `x=|X|` to `Z`.  Write

```
a=|A|=k x+s,              0<=s<x.
```

Reading the period-`x` word `Z` backwards from its final length-`x`
block `X` gives

```
Z=B X^(k+1),
A=B X^k,
B=suffix_s(X).                                    (12)
```

The case `s=0` would give `A[0]=X[0]`, contrary to (9)--(10).
Therefore `B` is a nonempty proper suffix of `X`, and
`B[0]=A[0]=2`.

At cut `p+x` of `Q`, immediately after the copy of `X` following the
middle cut `p`, the displayed label is `A[0]=2`.  The preceding suffix
is `X^(k+1)`: the copy of `A` before cut `p` ends in `X^k`, and the
next block is `X`.  If `k>=2`, a proper root-`x` cube would consequently
end at this `2`-cut, contradicting the exact circular profile.  Hence

```
k in {0,1}.                                       (13)
```

There are exactly two remaining word forms:

```
k=0:  A=B,     Q=X B X B X;
k=1:  A=B X,   Q=X B X X B X X.                 (14)
```

The second form is impossible.  Put `b=x-s`, so `X=C B` with
`|C|=b`.  The cut `b` lies at the beginning of the suffix `B` in the
initial copy of `X`, and its displayed label is `B[0]=2`.  In the
circular lift, the length-`3x` suffix ending there is

```
B X X C = B C B C B C = (B C)^3.
```

Its root length `x` is proper because `x<n`.  Thus a proper cube ends
at a cut labelled `2`, contradicting the exact profile.  Consequently
only the short-border form

```
A=B,        0<|B|<|X|,       B=suffix_|B|(X)
```

survives.

Thus the earlier unconditional claim `|A|<|X|` must be replaced by the
two-branch alternative (14), after which the long branch is eliminated
by the displayed cube.  The executed algebraic word `X=32, A=232`
realizes that long form before the full circular profile is imposed.

Sections 5--7 below discuss only the additional conditional hypotheses

```
k=0,
cn(Z)=cn(X)=1,
A is a nonempty proper suffix of X.               (15)
```

## 5. A strictly shorter embedded final-2 defect

At the circular cut

```
c=|X|
```

the `|X|` symbols immediately before the distinguished origin and the
first `|X|` symbols after it are both `X`, by (6).  Hence a root-`|X|`
square `X^2` ends at cut `c`.  Its next label is `A[0]=2` by (9), while
the finite prefix at that cut is exactly `X` and has curling number one
by the additional hypotheses (15).

Thus every minimal final-3 branch contains the exact shorter defect

```
finite prefix X:             cn(X)=1,
circular power at next cut:  X^2,
next label:                  2.                   (14)
```

It is not yet an autonomous shorter counterexample.  The square in
(14) uses the copy of `X` immediately before the distinguished circular
origin.  Starting the finite orbit from `X` would append `1`, not the
ambient label `2`.  Any use of (14) as a minimality contradiction must
prove an inheritance statement that carries the required earlier copy
of `X`; simply calling (14) a shorter seed would be invalid.

There is one further exact deletion fact.  Since `X[0]=3` and `cn(X)=1`,
CLSW Theorem 7 applied to `X=3X[1:]` forces

```
cn(X[1:])=1.                                      (15)
```

After returning to the original rotation `P=Q[1:]3`, the shorter prefix
`X[1:]` therefore starts at the distinguished symbol `P[0]=2`.  The
same circular `X^2` ends one cut earlier in that rotation.  The remaining
gap is still context inheritance: the displayed square contains the
deleted leading `3`, so it is not a suffix power of the standalone word
`X[1:]`.

## 6. Exact next split supplied by CLSW Theorem 13

By the additional hypotheses (15), `A` is a proper suffix of `X`, and
those same hypotheses give

```
cn(A X)=1.
```

The word

```
X A X
```

therefore falls into the exact dichotomy:

* if `cn(X A X)>1`, CLSW Theorem 13 supplies unique nonempty words
  `S,R` with

  ```
  A X=S R S,
  R a suffix of X,
  R a proper suffix of S,
  cn(S)=1,
  ```

  and either `|S|=|A|` or `|S|>2|A|`;
* if `cn(X A X)=1`, `A X` is robust under this particular second
  extension and Theorem 13 does not apply.

The second branch is real at the level of finite word equations; it
contains the terminal-marker forms studied in
`research/terminal_root_closure.md`.  It cannot be discarded as an
“analogous” case.

## 7. The middle cut eliminates the curling-one subbranch

Put

```
p=|X|+|A|=|Z|,             n=|Q|=3p-|A|.
```

The cut `p` is strictly positive and strictly below `n`.  Since `Q` is
the right rotation of `P`,

```
Q[j]=P[j-1]                for 1<=j<n.
```

Thus cut `p` of `Q` is exactly phase `p-1` of `P`.  In particular,
this is not the exceptional phase-zero cut created by the rotation.
The first-copy fitting witness at phase `p-1` of `P` supplies a cube
root of some length `r<n` ending at this cut with

```
3r<=n+(p-1)-1=n+p-2.                              (16)
```

The label at the cut is

```
Q[p]=X[0]=3,
```

so this is the required fitting cube.  If it is read in the lift ending
at cut `p+n`, (16) says that its starting coordinate is at least `2`.
Equivalently, in the lift ending at `p`,

```
p-3r>=2-n>1-n.                                   (17)
```

Under the additional hypotheses (15), all hypotheses of the middle-cut
obstruction proved in
`research/final_three_middle_cut_lemma.md` now hold:

```
0<|A|<|X|,
A is a suffix of X,
cn(X)=cn(AX)=1,
X[0]!=A[0],
p-3r>=1-n.
```

That lemma proves that no such cube can end at cut `p`, contradicting
the fitting witness.  It therefore eliminates the conditional subbranch
(15).  It does **not** eliminate the remaining cases in which
`cn(X)=2`, `cn(AX)=2`, or `|A|>=|X|`.

The dichotomy in Section 6 is consequently not needed for this
elimination.

## 8. Audit of the canonical-form prerequisites

The derivation of `Q=XAXAX` uses no unproved maximality assertion.
The root `q` at phase zero is an arbitrary proper circular cube witness,
not a longest or a shortest one.  The strict predecessor inequality
forces `3q>=n`; the standard proper-power span bound and primitivity then
give `0<3q-n<q`.  These are exactly the inequalities needed for the
linear identity `AQ=Z^3` and its cancellation.

Rotation introduces no profile ambiguity.  Proper circular powers are
invariant under rotation, and cut `j>0` of `Q` maps to phase `j-1` of
`P`.  The only fitting equation that need not survive a right rotation
is cut zero of `Q`.  The closing cube is at cut `p>0`, so it inherits
the stronger bound (16).

The finite curling-number bound for `Q` requires no hidden maximizing
choice.  A displayed factorization is used only for a lower bound.
The upper bound `cn(Q)<=2` follows by considering every possible suffix
power of exponent at least three: a proper suffix lies in `T=Q[1:]`,
while a suffix using `Q[0]` is all of `Q` and would make `Q`
nonprimitive.  Hence the displayed suffix `Z^2` proves equality.  No
corresponding deduction of `cn(Z)=cn(X)=1` is valid; Section 2 gives an
executed countermodel and records the correct upper bound.

Finally, `A[0]=2` uses exactness of the circular profile, not merely the
existence of the terminal cube: if `A[0]=Q[0]=3`, shifting `Z^3` one
letter right produces a proper cube at the next cut, whose exact label
is `Q[1]=2`.  The alphabet restriction to `{2,3}` is used precisely in
turning `A[0]!=3` into `A[0]=2`.

## Source use

The external results used here are:

* CLSW Theorem 7: prefixing one symbol raises a curling number by at
  most one;
* CLSW Theorem 18: the unique structural form of a primitive
  non-robust word of curling number `k>1`;
* CLSW Theorem 13: the refined second-extension form and its exact
  equal-scale / greater-than-two scale alternative.

Primary source:
<https://cs.uwaterloo.ca/journals/JIS/VOL16/Sloane/CNC.pdf>.
