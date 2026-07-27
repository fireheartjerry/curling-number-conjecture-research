# Square-root word-equation bridge audit

This note tests whether a primitive proper-circular curling-profile word
automatically supplies the word equation used by Peltomäki and Saarela.
It does not.  The length-21 replay word is an explicit counterexample to
that proposed bridge.

The executable audit is
`research/check_square_root_equation.py`.  It tests the displayed word
equalities directly and computes every proper circular repeated-block
exponent rather than inferring one from a exhibited factorization.

## 1. The exact criterion

Let `R` be a word of length `q`, and read `R^omega` from phase zero.  At a
current position `z`, let `mu(z)` be the least positive root length for
which the length-`2 mu(z)` factor beginning at `z` is a square.  Suppose
these roots exist at every position encountered.  Starting with `z_0=0`,
put

`X_i = R^omega[z_i : z_i+mu(z_i)]`,

`z_(i+1) = z_i + 2 mu(z_i)`.

Stop at the first `m` for which `z_m >= 2q`.

There is a greedy shortest-square factorization of the finite word `R^2`
ending exactly at its right boundary if and only if `z_m=2q`.  In that
case

`R^2 = X_0^2 X_1^2 ... X_(m-1)^2`

and

`|X_0 X_1 ... X_(m-1)|=q`.

Consequently

`X_0^2 X_1^2 ... X_(m-1)^2
 = (X_0 X_1 ... X_(m-1))^2`                         (1)

if and only if

`X_0 X_1 ... X_(m-1)=R`.                             (2)

The proof uses only the definitions.  The update for `z_i` says that the
successive square factors concatenate without gaps.  If `z_m=2q`, their
half-lengths sum to `q`, so their root concatenation has length `q`.
The left side of (1) is `R^2`.  Equality (1) therefore holds exactly when
the first `q` letters of its right side, namely the root concatenation,
are `R`, which is (2).

Thus return of the square-factor boundary after one period is not enough:
the root output must also equal the input period.

For a proper circular curling profile, every cut has a square ending at
it.  After reversal this gives a square beginning at every phase, so the
shortest-square map is defined on the reversed periodic word.  This fact
does not imply either `z_m=2q` or (2).

The midpoint map used in Saari's local lemma is also a different map.  It
moves from a square endpoint to its midpoint by one root length.  The
factor-boundary map above moves by two root lengths.  A midpoint cycle
whose root lengths sum to `q` therefore does not constitute a
factorization of `R^2` into consecutive squares.

## 2. Exact audit of the length-21 fixed profile

The tested word is

`Q=223222322232322232223`.

Executed exhaustive checks give:

* `Q` is primitive;
* its proper circular exponent profile is
  `223222322232322232223`, so the profile is exactly `Q`;
* every phase of both `Q^omega` and `(rev Q)^omega` begins in a square
  with root length less than 21.

For each zero-based rotation `s`, the following table gives the successive
shortest root lengths in the periodic continuation.  The column `sum`
is their sum.  When `sum>21`, the final displayed square crosses the
right boundary of `R^2`; when `sum=21`, `R^2` is factored exactly and the
last column is the first zero-based index at which the root output differs
from `R`.

| `s` | shortest root lengths | sum | result |
|---:|:---|---:|:---|
| 0 | `1,4,2,1,7,2,1,4` | 22 | overshoot |
| 1 | `4,2,1,4,4,2,1,7` | 25 | overshoot |
| 2 | `4,2,1,7,2,1,4` | 21 | mismatch at 7 |
| 3 | `1,6,1,3,1,6,1,3` | 22 | overshoot |
| 4 | `1,6,1,3,6,1,3` | 21 | mismatch at 1 |
| 5 | `6,1,3,1,6,1,3` | 21 | mismatch at 7 |
| 6 | `6,1,3,6,1,3,1` | 21 | mismatch at 6 |
| 7 | `1,2,1,4,4,2,1,7` | 22 | overshoot |
| 8 | `1,2,1,7,2,1,4,4` | 22 | overshoot |
| 9 | `2,1,4,4,2,1,7` | 21 | mismatch at 3 |
| 10 | `2,1,7,2,1,4,4` | 21 | mismatch at 2 |
| 11 | `4,3,1,6,1,3,6` | 24 | overshoot |
| 12 | `4,3,6,1,3,1,6` | 24 | overshoot |
| 13 | `1,4,4,2,1,7,2` | 21 | mismatch at 2 |
| 14 | `1,7,2,1,4,4,2` | 21 | mismatch at 1 |
| 15 | `4,4,2,1,7,2,1` | 21 | mismatch at 4 |
| 16 | `7,2,1,4,4,2,1` | 21 | mismatch at 7 |
| 17 | `1,3,1,6,1,3,6` | 21 | mismatch at 2 |
| 18 | `1,3,6,1,3,1,6` | 21 | mismatch at 1 |
| 19 | `3,1,6,1,3,6,1` | 21 | mismatch at 11 |
| 20 | `3,6,1,3,1,6,1` | 21 | mismatch at 3 |

Fourteen rotations close exactly at input length `2q`, and all fourteen
root outputs mismatch; the other seven rotations overshoot.  Hence no
rotation of `Q` gives (1) under the greedy shortest-square factorization.
The script separately repeats the prefix-square
calculation for every rotation of `rev Q`; none gives (1) there either.
This separate calculation is needed because shortest-prefix minimality is
not itself invariant under reversal.

This supplies a direct counterexample to the implication

`primitive and F(Q)=Q  =>  a rotation is fixed by the shortest-square map`.

## 3. Exhaustion of all non-greedy word equations

The script also checks whether a non-greedy square factorization might
nevertheless make the Peltomäki--Saarela equation available.

For a rotation `R`, let

`0=a_0<a_1<...<a_m=q`

be the partial sums of a composition of `q`, and put

`X_i=R[a_(i-1):a_i]`.

Such a composition satisfies (1) if and only if every `i` satisfies

`R^2[2a_(i-1):2a_i]=X_i^2`.                           (3)

The forward direction follows by restricting (1) to its `i`th square
block.  The reverse direction follows by concatenating all equalities
(3).  Therefore paths from 0 to `q` in the directed graph

`a -> a+r` when
`R^2[2a:2a+2r]=R[a:a+r]^2`

are in bijection with all possible equation factorizations.  The dynamic
program tests every `a` and every `1<=r<=q-a`, so this is an exhaustive
enumeration rather than a search with pruning.

Every rotation has the trivial one-factor composition `(21)`.  Apart
from it, only rotation 1 has solutions, and its complete list of
root-length compositions is

`(10,1,10)`,

`(4,2,4,1,10)`,

`(10,1,4,2,4)`,

`(4,2,4,1,4,2,4)`.

For the last composition, for example,

`R=232223222323222322232`

and the executed equality is

`(2322)^2 (23)^2 (2223)^2 (2)^2
 (3222)^2 (32)^2 (2232)^2 = R^2`.

None of the four is a shortest-square factorization.  In the order
listed above, the flags saying whether each chosen root is shortest at
its square-block start are

`(false,true,false)`,

`(true,true,false,true,false)`,

`(false,true,true,true,false)`,

`(true,true,false,true,true,true,false)`.

Reversing the base word gives the same four nontrivial compositions at
rotation 20, with the same minimality flags.

## 4. Why the published classification does not apply

Peltomäki and Saarela, *Standard words and solutions of the word
equation* (arXiv:2004.14657), study (1) under the additional hypothesis
that every `X_i` belongs, for one fixed pair `a>=1`, `b>=0`, to the six
minimal-square roots

`S_1=0`,

`S_2=010^(a-1)`,

`S_3=010^a`,

`S_4=10^a`,

`S_5=10^(a+1)(10^a)^b`,

`S_6=10^(a+1)(10^a)^(b+1)`.

These are the minimal squares of an optimal squareful word; arbitrary
squareful periodic words do not automatically have this six-root form.

For every one of the four nontrivial factorizations above, the executable
audit tests both binary letter identifications and every possible common
parameter pair.  No pair works.  The finite parameter test is exhaustive:
if `a` exceeds the longest tested root, only `S_1` can have an admissible
length; if a root uses `S_5` or `S_6`, its length bounds `b`; and if no
root uses them, `b=0` already tests the same first four roots.

Thus the only equations present in `Q` fail both relevant requirements:
they are not decompositions into the shortest squares at their positions,
and their roots do not lie in one Peltomäki--Saarela six-root family.

## 5. Usable conclusion and exact gap

The criterion in Section 1 is usable in one direction: if another
argument forces a circular-profile period `R` to have a one-period
shortest-square factorization whose root output is `R`, then (1) follows.
To invoke the Peltomäki--Saarela classification, one must additionally
prove that all selected roots belong to one common optimal six-root
family.

The required conjunction does not follow from primitivity,
`F(R) in {2,3}^q`, or even `F(R)=R`: the word `Q` already fails
square-root invariance in every phase, and all of its nontrivial
non-greedy equations fail the six-root hypothesis.  A route through that
classification therefore needs a new global replay hypothesis that
forces square-root invariance and optimal squarefulness; the circular
curling-profile equations alone do not provide the bridge.
