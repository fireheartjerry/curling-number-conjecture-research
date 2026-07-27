# Exact origin-zero re-entry after cube promotion

This note audits the proposed implication

> after the reset at `Q^3 3`, the first return of a powered-run origin to
> the fixed tower origin must be a nonself golden push which overshoots that
> origin.

That implication is false.  There is an exact boundary-square branch which
lands at the origin, followed by same-period cube maturation.

## Boundary-square lemma

Let a normalized fixed-origin cube tower contain a larger primitive root
`R`, of length `r`, so that the orbit copies `R` through

`R -> R^2 -> R^3`.

Assume that, immediately after an earlier promoted prefix `Q^3 3`, every
maximizing power begins strictly to the right of coordinate zero.  If no
powered suffix has returned to zero before the last symbol of `R^2` is
appended, then the transition completing `R^2` is an admissible first
return:

* before the append, at cut `2r-1`, choose a primitive maximizing root of
  length `p`, exponent `c`, and origin
  `A=2r-1-cp>0`;
* after the append, the displayed square has root length `r`, exponent
  two, and origin `2r-2r=0`;
* necessarily `p<r`, since `cp<=2r-1` and `c>=2`;
* the consecutive-root laminar-shadow lemma therefore puts the new
  length-`2r` square strictly around the old power together with the
  appended site.  Its exact left endpoint is nevertheless

  `2r-2r=0`,

  and the length equation is

  `2r=cp+A+1`.

Thus strict containment gives `0<A`; it does not give a negative new
origin.

The root-episode classification gives the same branch without referring to
adjacent cuts.  Let `f` be the last phase in the second copied block at
which the current curling number is two, and put `d=r-f`.  The new
length-`r` square at cut `2r` was not present at that preceding `2`-event.
If `f=0`, the gap is `d=r` and this is an equality birth.  If `f>0`, then
`d<r` and this is a crossing birth.  Writing

`F=R[0:f]`, `D=R[f:r]`,

the exact crossing equation is

`R^2=F D F D`,

and its new origin is

`2r-2r=0`.

Neither birth is a branch of the golden first-divergence trichotomy:
`R^2` has exponent two and is below the golden threshold.  At the later
transition

`R^2 -> R^3`,

the source exponent is two, the target exponent is three, the root length
is `r` on both sides, and

`2r-2r=3r-3r=0`.

This is exactly the `r=q` same-period self-maturation branch of
`golden_bad_cuts.md`, not a nonself push.

## Executed finite model

`research/check_origin_reentry.py` executes both curling-number
implementations on

`Q=2232`,

`R=223222322232322232223`.

Here `R` is primitive, begins with `Q^3 3`, and is a genuine full replay
root through `R^3`.  The smaller `Q` supplies the exact local promotion
marker but is not itself asserted to be a lower replay-tower level.

At the promoted prefix of length `13`, the curling number is two and its
only primitive maximizing root has length two and origin nine.  The
successive new minimum maximizing origins, computed over all intermediate
prefixes through `R^2`, are

`(end,origin)=(13,9),(17,5),(21,1),(42,0)`.

No complete power beginning at zero occurs at an intermediate prefix of
length `13` through `41`.  At cut `41`, the unique primitive maximizing
root has exponent three, length one, and origin `38`.  Appending its label
`3` completes `R^2`; at cut `42`, the primitive maximizing roots are

`(length,origin)=(4,34),(10,22),(21,0)`.

This is the root-growth branch of the laminar-shadow lemma, with the exact
boundary equality

`42=3*1+38+1`.

For the episode description, the preceding `2`-event is cut `40`, so
`d=2<21`, `f=19`, and the root-`21` occurrence is a crossing birth with
`R=F D`, `|F|=19`, `|D|=2`.  At cut `63`, the unique primitive maximizing
root has exponent three, length `21`, and origin zero.  Hence the
origin-zero square birth followed by fixed-origin maturation is realized
exactly; no step requires or produces a powered origin below zero.

The executed model does not construct two levels of an infinite tower.
It falsifies the local re-entry implication, while the boundary-square
lemma shows that the same branch remains available under the hypothetical
nested-tower assumptions.
