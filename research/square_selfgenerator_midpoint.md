# Minimal-square midpoint map for a square self-generator

This note applies Saari's minimal-square mechanism to the complete copied
block of a normalized square self-generator.  It produces an exact seam
dichotomy, but the dichotomy does not by itself eliminate an early masked
cube.

## 1. The minimal circular square is always source-visible

Let `P` be primitive, `p=|P|`, and suppose that its autonomous orbit
appends one complete copy of `P`:

`cn(P P[:d])=P[d]>=2` for `0<=d<p`.

At circular phase `d`, let `mu(d)` be the least proper root length of a
square ending at that cut in `P^Z`.

Then

`2 mu(d) <= p+d`.                                      (1)

Indeed, the source word `P P[:d]` has curling number at least two, so it
has a square suffix with some root length `q` satisfying `2q<=p+d`.
That square is also a proper circular square, and minimality gives
`mu(d)<=q`.  This proves (1).

Consequently the shortest circular square and its root word already occur
in the short source state.  An extra target cube may be masked by the
missing left context, but the minimal-square profile cannot be masked.

Reverse the circular word and let the midpoint map send a phase to the
beginning of the second copy of its minimal square.  If consecutive
minimal roots are `U,V`, Saari's local lemma gives

`2|V|>|U|`,

and `U,V` are prefix-comparable.  This map is defined at every phase of
the copied block by (1).

## 2. What an early target cube forces

Suppose the longer target at phase `h` has a primitive cube of root length
`r`, while the short source at the same phase has curling number two.  In
the notation of the early-square reduction,

`p=2r+s` and `3r>p+h`.

In reversed coordinates write the cube as

`z[0:3r]=Y^3`, with `|Y|=r`.

The two length-`2r` words beginning at positions zero and `r` are both
`Y^2`.  Since root length `r` is a square witness at both positions, the
minimal roots at the two positions have length at most `r`.  Testing every
shorter root uses only this common word `Y^2`.  Therefore

`mu(0)=mu(r)`,                                         (2)

and the corresponding minimal root words are identical.

There is a useful synchronized extension of (2).  For `0<=x<=r`, the
contexts beginning at `x` and `x+r` agree for `2r-x` symbols.  If

`2 mu(x) <= 2r-x`,                                     (3)

then

`mu(x+r)=mu(x)`,                                       (4)

with identical root words.  The square at `x` translates by `r` and fits
inside the common context by (3), giving one inequality between the two
minimal lengths.  A hypothetical shorter square at `x+r` also fits in the
common context and translates back, giving the reverse inequality.

Thus midpoint trajectories begun at the two adjacent cube-root
boundaries remain exactly `r` apart while (3) holds.  Their first possible
loss of synchronization is a phase satisfying

`x+2 mu(x)>2r`.                                        (5)

## 3. Landing or seam crossing

Follow the lifted midpoint trajectory from zero, writing

`x_0=0`, `x_(i+1)=x_i+mu(x_i)`.

Positive increments imply that there is a first `j` with `x_j>=r`.
There are two exhaustive cases.

### Landing

If `x_j=r`, then the minimal root at the endpoint is the initial root by
(2).  The roots `U_0,...,U_(j-1)` form a finite closed
prefix-comparability chain satisfying

`r=sum_(i=0)^(j-1) |U_i|`,

`U_j=U_0`,

and, for every `i<j`,

`U_i` is a prefix of `U_(i+1)^2`,

`2|U_(i+1)|>|U_i|`.

This is the exact finite cycle equation supplied by Saari's map.

### Crossing

If `x_(j-1)<r<x_j`, put

`x=x_(j-1)`, `u=mu(x)`, `q=r-x`.

Then

`0<q<u`.

The crossing root is the factor of the circular cube beginning `q`
letters before a root boundary, hence it has the exact form

`U=Y[r-q:]Y[:u-q]`.                                   (6)

Its square is a prefix at that phase, and its next minimal root is
prefix-comparable with `U` and longer than `u/2`.  Equation (6), rather
than a closed chain of total length `r`, is the complete seam alternative.

## 4. Executed fixed-profile crossing model

Executed exhaustive root checks on

`Q=223222322232322232223`

give a proper cube at circular cut 2 with root length `r=4`.  In reversed
orientation its root is

`Y=2232`.

The minimal midpoint trajectory from the cube endpoint has root lengths
`1,4`, hence lifted positions

`0 -> 1 -> 5`.

It crosses the root boundary at `r=4`; it does not land there.  The two
minimal root words are

`U_0=2`,

`U_1=2322`.

Here `q=3` in (6), and indeed

`U_1=Y[1:]Y[:1]=2322`.

The trajectory begun at the adjacent cube boundary has root length one
and moves

`4 -> 5`.

Thus the two trajectories form a diamond and coalesce just after the
seam.  This word is a genuine primitive proper-circular fixed profile, so
the landing conclusion cannot be obtained from the cube plus the
minimal-square rules.

## 5. Distinct cycles with the same preserved letter

The midpoint map preserves the letter at the beginning of each minimal
square.  This does not imply that each letter class has only one directed
cycle.

The executable `research/search_min_square_cycles.cpp` exhaustively
checks all proper root lengths of binary circular words.  It found the
primitive squareful word

`3323223323232233232322`

with two distinct midpoint cycles whose preserved letter is `3`:

* cuts `(1,15)`, with root lengths `(8,14)`;
* cuts `(4,18,10)`, with root lengths `(8,8,6)`.

Each displayed sum is 22, but the cycles are disjoint.  This example is
not a square self-generator; it isolates the exact limitation of the
minimal-square mechanism.  To force the paired early-cube trajectories to
coalesce, one must use the numeric source labels or another
self-generation equation, not merely squarefulness, primitivity, and
Saari's midpoint lemma.
