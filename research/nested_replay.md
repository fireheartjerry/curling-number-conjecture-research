# Nested replay-fixed roots

This note isolates consequences of the following hypothetical configuration.
`Q` and `R` are primitive replay-fixed words, `q=|Q|`, `r=|R|`,
`Q[0]=2`, and `R` begins in `Q^3 3`.

## The masking bridge

Let `W` be any prefix of `R` which extends through the promoted symbol,

`W = Q^3 3 U`,

and put `d=|W|<r`.  More generally than the terminating case, suppose

`ell := cn(W) < R[d]`.

This is exactly the situation at the first divergence between the
autonomous continuation after `Q^3 3` and the continuation supplied by the
larger circular context.  Suffix monotonicity orients every such divergence
in this direction.  The replay equation at phase `d` says that

`a := R[d] = cn(RW) > ell`.

Choose a primitive maximizing root of length `p` in `RW`.  Then

`a p > d`.                                                     (1)

Indeed, otherwise its entire `a`-power would be a suffix of `W`, contrary
to `cn(W)=ell<a`.  Thus every first divergence, including every rescue of
an autonomous `1`, is a powered bridge crossing the circular join between
`R` and its prefix.

There are two exact geometries.

### Short bridge

If `p<d`, then all of `W` lies in the terminal `p`-periodic power, so `p`
is a period of `W`.  Write `g=gcd(p,q)`.  In fact

`p > 2q+g`.                                                     (2)

To prove this, assume `p<=2q+g`.  The prefix `Q^3` has periods `p` and
`q`, and its length `3q` is at least `p+q-g`.  Fine--Wilf makes it
`g`-periodic.  If `g<q`, the first length-`q` block `Q` is imprimitive.
If `g=q`, then `p` is one of `q,2q,3q` under the assumed inequality.
The period comparison between position `3q` and position `3q-p` in `W`
equates the promoted `3` with `Q[0]=2`, a contradiction.  These cases are
exhaustive.

Thus a short bridge is exactly the old surviving border exception: writing
`p=2q+s` when `p<3q`, the overlap equation makes a prefix and suffix of
`Q` agree at shift `s`, and (2) says `s>gcd(q,s)`.

### Long bridge

If `p>=d`, put

`h=r-p`.

Since `p<r`, `h>0`.  Equality of the last two length-`p` root blocks copies
the whole target prefix back into `R`:

`R[h:h+d] = W`.                                                 (3)

Let `B(W)` be the length of the longest proper border of `W`, with
`B(W)=0` for an unbordered word.  If `h<d`, the two occurrences at offsets
zero and `h` overlap and give a border of length `d-h`.  If `h>=d`, the
same lower bound below is automatic.  Hence

`h >= d-B(W)` and `r=h+p >= 2d-B(W)`.                           (4)

So a long bridge does not merely have comparable scale: it creates a
second exact copy of the complete promotion-and-reset marker inside the
next replay root.

Equations (1)--(4) are purely word-combinatorial and do not invoke the
Curling Number Conjecture.

## Executed length-21 model

The workspace implementations were executed on

`Q=223222322232322232223`.

They give

`cn(Q^3 3)=2`, `cn(Q^3 3 2)=1`.

For

`W=Q^3 3 2`

the only periods at most `|W|=65` are `64` and `65`; equivalently its only
proper border has length one.  Consequently a long bridge into any
replay-fixed `R` beginning `Q^3 3` has

`|R| >= 2*65-1 = 129`.

The short bridge can only have `p=64`.  Its square forces the last 63
symbols of `R` to be `W[1:64]`.  Executed code gives

`cn(W[1:64] W[0])=1`,

so this branch immediately needs a second circular masking bridge at phase
one; it is not a closed construction.

`research/search_nested_replay.cpp` exhaustively enumerates every binary
suffix after the fixed prefix `Q^3 3`.  It found no replay-fixed extension
of total length 64 through 90.  This is only a finite check, but the bridge
calculation explains why the long-bridge branch cannot occur in that
range.

## Remaining exact obstruction

The bridge lemma leaves two mechanisms, neither eliminated by Fine--Wilf:

1. a short bridge encoded by a long border of `Q`, followed by another
   masking bridge when the forced circular continuation locally has
   curling number one;
2. a long bridge which installs another full copy of `Q^3 3 U` at offset
   `h=r-p` in `R`.

Iterating the second mechanism gives a return-word/S-adic decomposition
by repeated marker copies.  Its scales grow at least by (4), but geometric
growth alone is compatible with an infinite chain.  A proof still needs
either to show that the forced short-bridge cascade closes into a proper
period of `R`, or that the return-word decomposition eventually makes one
of the replay equations exceed its prescribed label.  The bridge lemma by
itself does not establish either assertion.

## Copy-parent normalization when the low side is `1`

There is a sharper normalization specifically at an autonomous `1`.
Assume `cn(W)=1`, and retain the bridge root length `p`.

If `p<d`, the fact that `p` is a period of `W` combines with `cn(W)=1` to
give

`p>d/2`.

Otherwise the last `2p` symbols of `W` would be a square.  Put

`b=d-p`, so `0<b<d/2`.

The period equation says that the prefix and suffix of `W` of length `b`
are the same word `A`.  Thus

`W=A M A`, with `|M|=d-2b`.

Since `A` is a suffix of a word of curling number one,

`cn(A)=1`.

The shift from the first occurrence of `A` to the last is exactly
`p=d-b`, and `p>|A|`.  Therefore what looked like a short bridge for the
reset word `W` is a long copy-parent edge for the strictly shorter reset
word `A`.  Repeating this normalization replaces the reset-word length by
a proper border of length less than half the old length.  Consequently
there can be at most

`ceil(log_2 d)`

consecutive short-bridge normalizations before a long edge is exposed.

In absolute coordinates, every normalized long edge maps a target reset
occurrence to an earlier equal occurrence and decreases its start
coordinate by at least the reset-word length.  Hence an infinite backward
copy-parent ray in a one-sided orbit cannot consist of infinitely many
unanchored reset copies: it eventually reaches the finite seed.  The exact
remaining obstruction is anchoring.  Different large promotion scales can
send their border-normalized reset rays into one of finitely many seed
cuts, and the argument above does not yet show that two such anchored rays
force a common period or an excessive curling number.

This border normalization uses `cn(W)=1`; at an earlier first divergence
with low value greater than one, a proper border need not itself be a
low-valued reset, so the halving argument does not apply without an
additional step.

## Exact form of an anchored unbounded reset family

The anchoring obstruction has a rigid form.  Fix a start coordinate `s`
in the finite seed.  Suppose words `A_i` of unbounded lengths `L_i` all
start at `s`, satisfy `cn(A_i)=1`, and their actual following labels are
`k_i` in a fixed alphabet `{2,...,K}`.  Let `r_i` be a primitive
maximizing-root length at that actual cut.  Since the power must cross the
left edge of `A_i` but cannot cross the beginning of the whole sequence,

`L_i < k_i r_i <= L_i+s`.                                    (5)

For all sufficiently large `i`, `k_i=2`.  If `k_i>=3`, then (5) gives

`2r_i <= 2(L_i+s)/3 < L_i`

once `L_i>2s`.  The terminal square of root `r_i` would then fit inside
`A_i`, contradicting `cn(A_i)=1`.

After taking a subsequence, the positive integer

`delta=2r_i-L_i`

is fixed, with `1<=delta<=s`.  If `C` is the fixed length-`delta` word
immediately preceding coordinate `s`, then

`C A_i = Y_i^2`, `|Y_i|=(L_i+delta)/2`.                       (6)

Each `Y_i` is primitive; otherwise the displayed square would give an
actual curling number at least four rather than two.  Thus infinitely many
border-normalized reset rays anchored at one seed cut reduce to an
unbounded tower of primitive square prefixes with one fixed finite
overhang `C`.

Equation (6) is stronger than a vague “seed anchoring” exception, but it
is still not a contradiction.  Nested primitive square prefixes with a
fixed origin exist in ordinary word combinatorics.  The unresolved step is
to combine their exact internal replay labels with the cube-promotion
markers; Fine--Wilf and origin budget alone do not exclude (6).

## Exhaustive overlap split for two anchored square prefixes

Translate the fixed origin in (6) to zero.  Let

`P^2` and `Q^2`

be two nested primitive square prefixes, with `p=|P|<q=|Q|`, and assume
that the actual curling number at the end of `P^2` is exactly two.

The equality `q=2p` is impossible, because then `Q=P^2` is imprimitive.
There are exactly two remaining cases.

1. `q>2p`.  The whole smaller square lies strictly inside the first copy
   of `Q`.  Raw overlap supplies no second period on `P^2`.
2. `p<q<2p`.  Put `s=q-p`.  Since

   `Q=P P[0:s]`

   and the prefix of length `2p` of `Q^2` is `P^2`, comparison on the
   overlap gives

   `P[j]=P[j+s]` for `0<=j<p-s`.

   Thus `s` is a period of `P`.  Put `g=gcd(p,s)=gcd(p,q)`.  Primitivity
   forces

   `s>g`;

   if `s<=g`, then `s=g` divides `p`, so the length-`p` word with period
   `s` is a proper power.  Finally, the last `P` in `P^2` contains
   `floor(p/s)` consecutive copies of its terminal length-`s` block.
   Since the curling number at this endpoint is two,

   `p<3s`.

   Consequently every close transition obeys the strict growth bound

   `q=p+s>4p/3`.

This split is exhaustive.  It does not prove periodicity: the close case
is the standard difference-period/Fibonacci-compatible exception, while
the far case permits a factor greater than two.  The next load-bearing
step must use the positions of the internal replay labels or of the
`Q_i^3 3` markers; nested-square overlap alone allows both cases
indefinitely.

## Anchor descent for autonomous-one factors

The fixed-overhang family in (6) is in fact incompatible with a one-sided
counterorbit.  The point is that its square roots are themselves
autonomous-one factors at a strictly earlier fixed coordinate.

Write the counterorbit word as `T[0:]`, let every `A_i` start at coordinate
`s`, and retain a subsequence on which

`C A_i=Y_i^2`, `|C|=delta`, `1<=delta<=s`.

Thus `C=T[s-delta:s]` and every `Y_i` starts at the fixed coordinate
`s-delta`.  Discard finitely many terms so that `|Y_i|>=delta`.  Removing
the first `delta` symbols from the displayed square then gives

`A_i=Y_i[delta:] Y_i`.

In particular, `Y_i` is a suffix of `A_i`.  Since `cn(A_i)=1`, suffix
monotonicity gives

`cn(Y_i)=1`.                                                   (7)

The lengths of the `Y_i` are unbounded.  At the end of the first copy of
`Y_i` in `Y_i^2`, the actual next symbol is its first symbol
`T[s-delta]`.  For all sufficiently large `i` this cut lies beyond the
finite seed, so that symbol is the actual curling-number label of the
global prefix and is at least two.  Consequently the words `Y_i` satisfy
the hypotheses of the anchored-family argument at the strictly earlier
fixed coordinate `s-delta`.

Apply (5)--(6) again, after taking a further subsequence.  Either the new
coordinate is zero, in which case (7) is also the curling number of the
entire global prefix and contradicts the counterorbit assumption, or a
new positive overhang moves the fixed start coordinate strictly farther
left.  At each iteration the family remains unbounded: the new root
length is half the old factor length up to a fixed additive constant.

The start coordinate is a nonnegative integer and decreases by at least
one at every iteration.  Hence after at most `s` iterations the process
reaches coordinate zero and gives the contradiction above.  Therefore an
unbounded family of autonomous-one factors with one fixed seed anchor
cannot occur in a counterorbit.

This eliminates the case in which the border-normalized factors arriving
at one seed anchor still have unbounded length.  It does **not** yet
eliminate a bounded-sink cascade: reset words of unbounded original length
may undergo an unbounded number of less-than-half border normalizations
and reach one of finitely many bounded reset words before their first long
edge.  Nor does the argument apply to first divergences whose low curling
number is at least two.  Either situation needs an additional mechanism.

The circular-profile/Saari machinery also does not presently manufacture
a low-side-one factor from an arbitrary contexted primitive maturation
`R^2 -> R^3`.  During the copied third block, every autonomous word
`R^2 R[:d]` ends in the square of a rotation of `R`, so its curling number
is at least two.  After the delimiter `3`, proving that the autonomous
continuation eventually has curling number one is a termination statement
for the new finite seed `R^3 3`; a circular phase having no proper cube
does not imply it.

An executed example rules out an immediate-reset substitute.  For the
primitive word `R=2322`, exhaustive curling-number evaluation gives the
labels `2,3,2,2` while extending `R^2` to `R^3`, and `cn(R^3)=3`.
Starting autonomously from `R^3 3`, the first state of curling number one
occurs only after 52 extensions, at total length 65.  Thus the two-step
reset of the length-21 model is special computed behavior, not a
consequence of square-to-cube maturation alone.
