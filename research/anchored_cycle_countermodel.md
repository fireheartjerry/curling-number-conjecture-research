# Unbounded anchored least-root cycles: a cycle-local countermodel

This note records a sharp limitation of Lemma 8 in
`recurrent_tower.md`.  The winding bound, seed anchoring, monochromaticity,
and even the exact least-root and self-label equations at every vertex of
one parent cycle do not bound the number of vertices.  The construction
below is not a global solution of `pc_Q(d)=Q[d]` at every cut, so it leaves
open any argument that uses the off-cycle equations.

## Construction

Fix an integer `L>=2`.  For `3<=r<=L+2`, define

`A_r = 2^(r-2) 3 2`

and concatenate

`Q_L=A_3 A_4 ... A_(L+2)`.

Write `q=|Q_L|`.  The lengths of the arcs are `3,4,...,L+2`, and hence

`q=3+4+...+(L+2)=L(L+5)/2`.                         (1)

Let `c_r` be the circular cut immediately after `A_r`.  Thus

`c_r=3+4+...+r (mod q)`.

There are exactly `L` such cuts.

## Lemma 1 (exact proper profile at the selected cuts)

At `c_r`, the proper cyclic curling number is exactly `2`, and its unique
maximizing proper root length is `r`.

**Proof.**  First consider `r>3`.  The symbol immediately before
`A_(r-1)` is the final `2` of `A_(r-2)`, so the length-`r` block ending
immediately before `A_r` is

`2 A_(r-1)=2 2^(r-3) 3 2=A_r`.

For `r=3`, the length-three suffix of the last arc `A_(L+2)` is `232`,
which is `A_3`.  Therefore the two length-`r` blocks ending at `c_r` are
both `A_r`.  This proves that exponent `2` occurs with root length `r`.

It remains to prove maximality over every proper root length.  Mark the
positions of the symbols `3` in the two-sided periodic word
`Q_L^Z` as

`...<t_(i-1)<t_i<t_(i+1)<...`.

The cyclic list of consecutive differences `t_i-t_(i-1)` is a rotation
of

`3,4,...,L+2`;                                             (2)

in particular, all `L` differences in one period are distinct.

Suppose a square of a proper root length `s<q` ends at `c_r`.  Its final
block contains the `3` at position `t_i=c_r-2`.  Equality with the
preceding block puts another `3` at `t_i-s`.  Since `0<s<q`, there is a
unique `h` with `1<=h<L` such that

`t_i-s=t_(i-h)`.                                          (3)

Assume `h>=2`.  Then `t_(i-1)` lies in the final length-`s` block, so
block equality puts a `3` at `t_(i-1)-s`.  There cannot be another `3`
strictly between `t_(i-1)-s` and `t_(i-h)`: translating such a position
forward by `s` would put a `3` strictly between the consecutive marked
positions `t_(i-1)` and `t_i`.  Consequently

`t_(i-1)-s=t_(i-h-1)`.

Subtracting this equation from (3) gives

`t_i-t_(i-1)=t_(i-h)-t_(i-h-1)`,

contradicting the distinctness in (2), because `1<=h<L`.  Thus `h=1`,
and (3) gives

`s=t_i-t_(i-1)=r`.                                        (4)

Every suffix power of exponent at least two contains a suffix square
with the same root.  Equation (4) therefore proves that `r` is the only
proper root attaining exponent at least two.

An exponent of at least three with root `r` would put a third `3` at
`t_i-2r`.  The last two copies each contain exactly one `3`, so this
would make the two consecutive gaps ending at `t_i` both equal to `r`.
That again contradicts (2).  The exponent at root `r` is therefore
exactly `2`, completing both the maximality and uniqueness proof. ∎

## Lemma 2 (primitivity)

Every `Q_L` is primitive.

**Proof.**  Suppose `Q_L=V^e` for an integer `e>=2`.  Each copy of `V`
contains the same positive number of symbols `3`.  The cyclic sequence
of gaps between successive `3` symbols would consequently be an
`e`-fold repetition of a shorter gap sequence.  Each gap in that shorter
sequence would occur at least twice.  This contradicts (2), where all
`L` gaps are distinct. ∎

## Lemma 3 (an unbounded winding-one parent cycle)

Under the least-maximizing-proper-root parent map, the selected cuts form
one directed cycle of length `L`.  Its spans are `3,4,...,L+2`, their sum
is `q`, and its winding is one.  Every selected cut has both self-label
and preceding-symbol color `2`.

**Proof.**  Lemma 1 says that the parent edge at `c_r` has span `r`.
The definition of the endpoint cuts gives

`c_r-r=c_(r-1) (mod q)`,

where `c_2` denotes `c_(L+2)=0`.  These `L` edges visit every selected
cut and close after one traversal.  Equation (1) says their spans sum to
`q`, so the winding number is one.

The symbol after each endpoint is the first symbol of the next arc, and
the symbol before it is the last symbol of the current arc.  Both are
`2`.  Lemma 1 gives `pc_(Q_L)(c_r)=2`, so the self-label equation at each
selected cut is exact. ∎

## Fixed seed bound and exact scope

The construction also satisfies the finite-prefix containment inequality
from Lemma 8 with the fixed bound `N=8` at every selected cut to which
that inequality applies.  The only selected cuts below `8` are
`0,3,7`.  For `r>=5`, the ordinary representative of `c_r` is

`c_r=3+4+...+r=r(r+1)/2-3`,

and

`c_r-2r=(r^2-3r-6)/2>=0`.

Thus `r<=c_r/2` whenever `c_r>=8`.  In particular, `L` is unbounded
while the seed bound is the constant `8`, the alphabet is `{2,3}`, the
winding is one, and all selected-cycle equations above remain exact.

This does **not** produce an autonomous nonterminating orbit.  The
equation

`pc_(Q_L)(d)=Q_L[d]`

fails at off-cycle cuts.  Therefore the construction blocks only a
cycle-local compression lemma: no length bound can follow solely from
the Lemma 8 cycle data plus exact root-copy, maximality, leastness, and
self-label equations on the cycle.  A viable global classification must
use equations at cuts outside the chosen cycle (or another genuinely
global consequence of autonomy).

The program `check_unbounded_parent_cycles.py` independently enumerates
every proper root length at every selected cut for `2<=L<=30`.  It checks
the exact maximizing exponent and all maximizing roots, primitivity,
copy equations, labels, parent closure, winding, and `N=8` containment.
It also computes an explicit off-cycle profile mismatch for `L=5`.
