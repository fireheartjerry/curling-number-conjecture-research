# Backward copy-parent graph

This note records a structural reduction for a hypothetical counterorbit.  It
does not prove termination.

## Canonical graph

Let `W` be the one-sided word obtained by concatenating the seed and all
appended curling numbers.  Let the seed length be `N`.  The symbol appended
at time `t` occupies position `v=N+t`, using zero-based positions.

For every appended position `v`, the prefix `W[0..v]` is `S_(t+1)`.  In a
counterorbit its curling number is at least two.  Choose the least root length
`p(v)` among roots attaining that curling number, and define

`parent(v) = v - p(v)`.

The final symbols of the last two root copies are equal, so
`W[parent(v)] = W[v]`.  Thus every appended vertex has one earlier parent of
the same value.  Repeated parent steps reach the seed because the position
strictly decreases.

## Lemma A: local finiteness and a monochromatic infinite ray

For a fixed vertex `u`, only finitely many appended vertices can have parent
`u`.  Indeed, if `parent(v)=u`, then `p(v)=v-u`.  The square formed by the
last two copies fits in `W[0..v]`, so

`2(v-u) <= v+1`,

and hence `v <= 2u+1`.

Consequently, if a value `a` occurs at infinitely many appended positions,
the subforest induced by value `a` contains an infinite ray.  There are only
finitely many seed roots of value `a`, and every vertex has finite outdegree,
so this is König's infinity lemma applied after adjoining one super-root.

In particular, the already-proved fact that a counterorbit has infinitely
many appended `2` values supplies an infinite ray of `2` vertices.

## Exact equations along a ray

Write an infinite monochromatic ray as

`v_0 < v_1 < v_2 < ...`,

where `parent(v_i)=v_(i-1)` and every `W[v_i]=a`.  Discarding the seed root
if necessary, every displayed `v_i` below is appended.  Put

`d_i = v_i-v_(i-1)` and `e_i = W[v_i+1]`.

The prefix ending at `v_i` has curling number `e_i`, and its canonical
maximizing root has length `d_i`.  Therefore:

1. `2 <= e_i <= a+1`.  The upper bound is the one-step rise bound applied
   to the consecutive orbit labels `W[v_i]=a` and `W[v_i+1]=e_i`.
2. If `B_i` is the length-`d_i` suffix, the prefix ends in `B_i^(e_i)`.
   In particular, `W[v_i-j*d_i]=a` for `0 <= j < e_i`.
3. `e_i*d_i <= v_i+1`, equivalently
   `(e_i-1)*v_i <= e_i*v_(i-1)+1`.

### Lemma B: equal spans cannot persist

If `r` consecutive ray spans ending at `d_i` are all equal to `d`, then the
prefix ending at `v_i` has `r+1` consecutive copies of one length-`d` block.

Proof: the square at the first of the `r` edges equates the block immediately
before its parent with the block immediately after it.  Each later edge
equates the latter block with the next adjacent length-`d` block.  These are
exactly `r+1` adjacent blocks, with no omitted interval.

It follows that `r+1 <= e_i <= a+1`, so `r <= a`.  On a `2`-ray, at most two
consecutive spans can be equal.

### Lemma C: a sufficiently large span jump forces exponent ascent

For consecutive ray spans, if

`d_i >= e_(i-1) * d_(i-1)`,

then `e_i > e_(i-1)`.

Proof: the length-`d_i` source block ending at `v_(i-1)` contains the whole
canonical suffix power of length `e_(i-1)*d_(i-1)`.  The target block ending
at `v_i` is an exact copy, so the prefix ending at `v_i` also has that suffix
power.  Hence `e_i >= e_(i-1)`.  If equality held, the shorter length
`d_(i-1)` would attain the maximum `e_i` at `v_i`.  Since
`d_i >= 2*d_(i-1)`, this contradicts the definition of `d_i` as the least
maximizing-root length.

Thus `e_i <= e_(i-1)` implies
`d_i < e_(i-1)*d_(i-1)`.

### Lemma E: exact Fine--Wilf overlap dichotomy

Let `D=d_(i-1)`, `d=d_i`, `E=e_(i-1)`, `e=e_i`, and
`g=gcd(D,d)`.  The old power interval and the part of the new power interval
ending at their common ray vertex overlap in exactly

`O = min(E*D, (e-1)*d)`

symbols.  If `O >= D+d-g`, Fine--Wilf gives period `g` on the overlap.  The
overlap then contains both the length-`D` old root and the length-`d` new
root, each ending at a root boundary.  Since `g` divides both lengths, either
root would be a proper power unless `g=D=d`.  Both roots are primitive, so
the overlap threshold forces `D=d`.

Consequently, if `D != d`, at least one of the following strict inequalities
holds:

`d > (E-1)*D+g`,

`D > (e-2)*d+g`.

These alternatives are exhaustive: their simultaneous failure says that
both arguments of the minimum defining `O` meet the Fine--Wilf threshold.

For a `2`-ray, `E,e` lie in `{2,3}`.  Put
`L_i=v_i-e_i*d_i+1`, the left endpoint of the complete canonical power.
The dichotomy and Lemma C give the following complete transition table.

* If `e=2`, then `d<E*D` and `L_i>L_(i-1)`.
* If `e=3` and `D=d`, this is an equal-span step.  Its left endpoint is
  unchanged when `E=2` and moves right when `E=3`.
* If `e=3`, `D!=d`, and `d>(E-1)*D+g`, then
  `L_i<L_(i-1)`.  For `E=2` this is exponent ascent.  For `E=3` it has
  `d>2D+g`.
* The only remaining `e=3` case has `D>d+g`; it is a strict scale drop and
  `L_i>L_(i-1)`.

Thus every step either advances the left boundary, uses the same span, or
is a cube step that reaches strictly farther left.  In the latter case it
either raises the exponent from two to three or more than doubles an already
cube-scale root.  This classification still permits a large left expansion
followed by a short right-shifting reset.

## Birth-root transfer

Let `q_i` be the least maximizing-root length of the prefix ending one
position before `v_i`.  That prefix has curling number `a`, because the next
appended symbol is `W[v_i]=a`.

### Lemma D: a long copy transfers the birth root

The following implications hold:

* If `d_i >= a*q_(i-1)+1`, then `q_i <= q_(i-1)`.
* If `d_i >= a*q_i+1`, then `q_(i-1) <= q_i`.
* Therefore, if `d_i >= a*max(q_(i-1),q_i)+1`, then
  `q_i=q_(i-1)`, and the two canonical root words are identical.

For the first implication, the source length-`d_i` block ending at
`v_(i-1)` contains the suffix `A^a a`, where `|A|=q_(i-1)`.  Its copied
target ending at `v_i` has the same suffix, so the prefix ending at `v_i-1`
ends in `A^a`.  Its maximum is exactly `a`, proving
`q_i <= q_(i-1)`.  The second implication translates the corresponding
suffix at `v_i` back to the source block.  If the lengths are equal, the
root words are equal because a suffix of a fixed length is unique.

This is transfer, not descent: equality can persist across arbitrarily larger
copy spans unless an additional global mechanism forbids it.

## Delimiter birth descriptors and interior mirrors

In an eventual `{2,3}` tail, let `q(z)` be the least square-root length at
the state immediately before an appended `2` at position `z`, and let
`delta(z)` be its incoming gap from the preceding appended `2`.  A birth
descriptor of root length `p` and incoming gap `delta` is determined by the
suffix window of length `2p+delta`: this window determines root membership
and whether the root is transported, a crossing birth, an equality birth, or
an internal birth.

A ray edge `u -> v` of span `d` gives equality of the two length-`d` root
copies.  Removing their terminal `2` symbols gives equal predecessor-state
suffixes of length `d-1`.  Hence a descriptor at the target is copied
exactly to the source whenever

`2p+delta <= d-1`.

This preserves the birth subtype, not just the root word.  If the inequality
fails in the `{2,3}` core, then `d <= 2p+3`.

Lemma 10 of `reductions.md` can make this internal.  From any appended `2`,
the most recent `2`-state with `q<=2` lies at raw distance at most eight.
Indeed, during a run of states with `q>2`, incoming gaps are in `{1,2}`,
they alternate, and there are at most five such states; five alternating
gaps have total at most eight.  Such a low-root descriptor has window length
at most `2*2+3=7`.  Therefore every ray edge with `d>=16` contains, in its
target copy, a low-root descriptor whose whole window is interior, and the
source copy contains the identical descriptor shifted by `-d`.

More precisely, if `r(x)` is the last low-root `2`-state at or before a ray
vertex `x`, then for `d>=16`,

`r(v)=r(u)+d`.

The chosen target marker is at distance at most eight from `v`, so its
window is interior.  Its translate is a low-root marker before `u`.  A later
low-root marker before `u` would translate to one later than `r(v)`, and a
later one before `v` would translate back, proving the equality.

This marker mirror is also not a descent.  It is intrinsically one-edge:
iteration requires a new enclosing copied block at the earlier marker.
The first outer square supplies no third copy from which another mirror
could be inferred.

## Siblings at one copy center

### Lemma F: sibling spans either double or cast a smaller square shadow

Suppose one vertex `u` has canonical copy-children at spans `p<q`.  Let
`R_p` and `R_q` be the target root blocks immediately after `u`.  Then
`R_p` is both a prefix and a suffix of `R_q`: it is a prefix because the two
target blocks start at `u+1`, and it is a suffix because the corresponding
source blocks both end at `u`.

The equality `q=2p` is impossible, since the prefix and suffix copies would
be disjoint and fill `R_q`, making `R_q=R_p^2` nonprimitive.  If
`p<q<2p`, put `r=2p-q`.  The prefix and suffix occurrences of `R_p` overlap
in `r` symbols, so their overlap is simultaneously the prefix and suffix of
`R_p`.  At the raw endpoint `u+r`, the `r` symbols before `u` and the `r`
symbols after `u` are equal.  Thus that prefix ends in a square of root
length `r<p`.

Hence every sibling pair has either `q>2p` or a strictly smaller powered
shadow at the same center.  The shadow need not be the canonical maximizing
root at its endpoint: a crossing cube can dominate it.  This is the same
failure mode that prevents the one-edge descriptor mirror from being
iterated automatically.

## Executed rank counterexamples

The values below were produced by `curling.py` through
`research/dependency_graph.py`; `tests/test_dependency_graph.py` checks the
parent equality and complete suffix power for every binary seed of length at
most eight.

* Seed `2323` has appended stream `2223` before the first curling number one.
  One canonical `2`-ray has `(position, next exponent, span)`
  `(4,2,2),(5,2,1),(6,3,1)`.  Thus span can decrease along a ray, and the
  third appended `2` on this ray has graph depth three, exceeding its value.
* Seed `23222322` has a canonical `2`-ray beginning with spans
  `4,3,4,4,6`.  Thus span can increase as well as decrease.  The equal pair
  `4,4` ends at a next exponent of three, attaining the bound in Lemma B.
* Seed `22323222322` has a ray edge from position `41` to position `62` with
  `a=2`, `d=21`, and `q_(parent)=q_(child)=7`; the next exponent changes
  from two at the parent to three at the child.  The condition
  `21 >= 2*7+1` in Lemma D holds, but the birth-root rank is preserved rather
  than decreased.  The next ray vertex is at position `68`, with birth-root
  length six, copy span six, and next exponent two.  Hence the exponent
  ascent forced by a large jump can reset after a later span drop.
  On a different continuation of the same canonical parent branch, the
  spans and left endpoints include
  `(position,e,d,L)=(41,2,4,34),(62,3,21,0),(68,2,6,57),
  (69,2,1,68),(73,3,4,62)`.  Thus the same ray can make two distinct
  left-expansion steps; the first need not be the only reset.
* On the span-`21` edge from `41` to `62`, the last low-root marker before
  the child is at position `60`, with `q=1`; its exact translated marker is
  at position `39`.  Both lie two symbols before their respective ray
  vertices.  Nevertheless the outer canonical scale rises from four to
  twenty-one.  The mirrored finite marker therefore does not control the
  enclosing scale.

The exact remaining obstacle for this route is to rule out an infinite
alternation of (i) large copy edges that reproduce the same local descriptor
`A^a a` and (ii) short edges that reset both the birth scale and the next
exponent.  Absolute position is a well-founded backward rank, and canonical
origin is constant along every ray; neither supplies a global bound on ray
depth.  Fine--Wilf makes the reset geometry exhaustive but does not orient
it: the executed path above cycles

`(L,d,e): (34,4,2) -> (0,21,3) -> (57,6,2)`,

so left endpoint, scale, exponent, and power-interval length all reverse
direction.
