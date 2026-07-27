# Transported root episodes and origin ancestry

This note records exact local reductions for a hypothetical counterorbit.  It
does not prove termination.

Let `N` be the seed length and let `C_t=cn(S_t)` be the symbol appended at
time `t`.  Thus `S_t` ends at the half-open absolute position `N+t`.  At a
time `t` with `C_t=2`, let

`R_t={p>=1 : S_t ends in a square with root length p}`.

## Maximal transported episodes

List the times with `C_t=2` in increasing order.  If `s>t` are consecutive
such times, a root occurrence `p in R_s` is transported from `t` when

`s-t<p` and `p in R_t`.

A `p`-episode is a maximal chain of occurrences joined by these transport
edges.  If an episode begins at time `b`, put

`A=N+b-2p`.

At every event `e` in the episode, the whole interval

`[A,N+e)`

has period `p`.  The proof is inductive.  The first occurrence supplies the
square `[A,N+b)`.  If the next event is `d<p` positions later, its terminal
`p`-square overlaps the previous periodic union in `2p-d>p` positions.
Two intervals with the same absolute period `p` and an overlap containing
all `p` residue classes have a `p`-periodic union.

Consequently,

`e-b<p`.

If `e-b>=p`, the terminal `3p` symbols of the periodic union would be three
copies of one length-`p` block, contrary to `C_e=2`.  Thus an episode has
fewer than `p` positions of temporal drift.

If the same length `p` dies and is later born in a new episode at `b'>b`,
the new origin is

`A'=N+b'-2p`,

so `A'-A=b'-b>0`.  Rebirth at a fixed scale therefore moves the episode
origin strictly right; this fact alone does not bound the number of
rebirths.

## Exact birth types

Let `s>t` be consecutive `2`-events, put `d=s-t`, and suppose `p in R_s`
is not transported.

* `d<p`: crossing birth.
* `d=p`: equality birth.
* `p<d<=2p`: impossible.
* `d>2p`: internal birth.

For a crossing birth, put

`r=t-p`, `f=p-d`, `a=s-2p=r-f`.

In time coordinates the square has the exact form

`C[a:r] C[r:r+d] C[r+d:t] C[t:s] = F D F D`,

where

`C[a:r]=C[r+d:t]=F`

and

`C[r:r+d]=C[t:s]=D`.

The source time `r` is itself a `2`-event, because the first symbols of the
two copies of `D` agree and the second one is `C_t=2`.

## Generated-birth midpoint lemma

Let a new `p`-episode be born at `s`, and suppose its displayed square
origin is generated rather than in the seed:

`A=N+s-2p>=N`.

Put `a=s-2p`, `m=a+p`, and write the birth square as `P^2` on
`[A,N+s)`.  The two copies of `P` imply

`h:=C_a=C_m`.

In a counterorbit `h>=2`.

If `h>=3`, let `q` be a maximizing-root length at `S_m`.  Then

`h q>p`.

Otherwise the complete `q`-rooted `h`-power ending at the midpoint lies
inside the first copy of `P`.  Translating it by `p` through `P^2` gives the
same `h`-power at the endpoint `S_s`, contradicting `C_s=2`.  Hence the
earlier `h`-power starts strictly before `A` and crosses the new episode's
origin.

If `h=2`, the origin time `a` is itself a `2`-event.  Every root episode
present there has periodic-union origin strictly before `A` and ends at
`A`.  At the midpoint, a root `q in R_m` has one of two exact behaviours:

* if `2q>p`, its square occurrence starts before `A`;
* if `2q<=p`, its complete square lies in the first copy of `P` and
  translates into the second copy, so `q in R_s`.

Thus every generated birth has a strict earlier origin parent if touching
the child origin at the parent's right endpoint is admitted.  A stronger
claim that a prior episode must remain active and enclose the child at time
`s` is false.

Executed counterexample: from seed `22322232`, at time `20` the complete
square-root spectrum is `(7)`.  The root `7` is a generated crossing birth:
the previous `2`-event is time `18`, the gap is `2`, and its absolute square
origin is `14`, beyond the seed length `8`.  Its exact square is

`(23222 23)^2`.

No larger episode is active at the birth.  At the midpoint time `13`,
however, the spectrum is `(4,10)` and the corresponding episode origins are
`11` and `1`, both earlier than `14`.  Those prior episodes die before the
new root-`7` birth.  This is the death-and-reconstitution obstruction.

An exhaustive executed audit over all `524286` binary starts of lengths
`1` through `18` found `95920` generated births with `p>=4` and no failure
of the origin/midpoint alternatives.  This is finite evidence only.

## Same-period golden divergence is fixed-origin maturation

Use the notation from `golden_bad_cuts.md` for the first shadow divergence
of a new golden record `q`: `V=U+q`, the first `h` subsequent labels after
the source and target agree, and the two different next labels have maximum
`k>=3`.  Suppose the high side has maximizing-root length `r=q`.

The high side cannot be `U`.  If `h<q`, its `q`-rooted `k`-power occurs at
`U<v`, before the first golden occurrence of `q`.  If `h>=q`, the matched
labels give

`W[x]=W[x+q]` for `x=u+1,...,u+h`.

In particular, the last length-`q` block ending at `U` is copied to
`[U+1,V]`.  A `q`-rooted `k`-power at `U` would therefore extend to a
`q`-rooted `(k+1)`-power at `V`, contradicting the choice of `k` as the
larger mismatch label.

The target `V` is therefore the high side.  Truncating its terminal
`q`-rooted `k`-power by one block leaves a `q`-rooted `(k-1)`-power at
`U`.  The source label is at least `k-1`, and because it is different from
and below `k`, it is exactly `k-1`.  The two powers have the identical left
endpoint:

`V-kq+1=U-(k-1)q+1`.

Thus the `r=q` branch is a one-block maturation of one fixed-origin period,
not a scale relocation.  When `k=3`, this is exactly a transported
root-`q` square episode maturing into a cube.

## Copying a midpoint episode through a newly born square

Keep the generated birth square `P^2` from the midpoint lemma.  In absolute
coordinates write its interval as `[A,B)`, its midpoint as `M=A+p`, and
`B=M+p`.  Suppose a `q`-episode ending at `M` has absolute periodic-union
origin `O>=A`.

Every event in that episode translates by `+p` to a `q`-occurrence in the
second copy of `P`.  Indeed, every displayed `q`-square starts at or after
`O`, hence lies inside the first `P`, and the equality of the two copies
preserves both the square and every event gap.  The translated occurrences
therefore form a transported chain ending at `B`, with candidate origin
`O+p`.

Let `O'` be the actual origin of the `q`-episode ending at `B`.  Exactly one
of the following holds.

1. `O'<M`.  The episode crosses the copy boundary.  Its periodic union at
   `B` has length greater than `B-M=p` and less than `3q`, so `q>p/3`.
2. `O'>=M`.  Every square in the actual episode is internal to the second
   `P`.  Translating the complete episode by `-p` gives an episode ending
   at `M`.  Maximality and uniqueness of the episode containing that
   occurrence force `O'=O+p`.

Thus a small internal midpoint episode either produces a comparable
boundary-crossing episode or undergoes an exact death-and-rebirth copy.

In the exact-copy case, compare the future label streams after `m` and
`s`, where `M=N+m` and `B=N+s`.  If they agreed forever, the orbit word would be ultimately
`p`-periodic.  At the first mismatch after `h` matched labels, the two
prefixes share a terminal `p`-periodic word of length `p+h`.  If the larger
mismatch label is `k<=K` and has primitive maximizing root `r`, its
`k`-power cannot fit inside that common word.  Therefore

`k r>p+h`, and hence `r>(p+h)/K>=p/K`.

On the source-high side this power starts before `A`; on the target-high
side it starts before `M`.  The unresolved branch is the latter: exact
small-root rebirth followed by a comparable target-side relocation.

## Local replay dichotomy for a generated square

Assume the orbit is already confined to `{2,3}`.  Suppose the output word
contains `P^2` on `[A,B)`, where `|P|=p`, `M=A+p`, `B=A+2p`, and the state
ending at `B` has curling number two.  The last condition makes `P`
primitive: if `P=Q^d` with `d>=2`, the endpoint would end in `Q^(2d)` and
have curling number at least four.

For `0<=j<p`, put

`L_j=cn(P P[:j])`,

where `P[:0]` is empty.  The word `P P[:j]` is a suffix of the actual state
ending at `M+j`, whose label is `P[j]`.  Hence

`L_j<=P[j]`.

If the inequality is strict, take any maximizing root `r` at the actual
state ending at `M+j`.  Its `P[j]` copies cannot fit inside the terminal
word `P P[:j]`, since that would give `L_j>=P[j]`.  Therefore

`P[j] r>p+j`,

so the power starts strictly before `A` and

`r>(p+j)/P[j]>=p/3`.

Suppose instead that equality holds for every `j`.  Starting from the
finite word `P`, the autonomous curling-number orbit emits the complete
word `P` once and reaches `P^2`.

Compare this local replay with the actual orbit after `B`.  At the state
ending at `B+j`, the suffix `P P[:j]` gives curling number at least
`P[j]`.  Until a mismatch, the actual orbit therefore emits the prescribed
next copy of `P`.  In the `{2,3}` core, a first mismatch has prescribed
label two and actual label three.  If its maximizing cube root is `r`, the
cube cannot fit inside `P P[:j]`, and hence

`3r>p+j`, `r>p/3`.

Its left endpoint is strictly before `M`.  If there is no mismatch for a
full `p` positions, the actual state ends in `P^3`; its curling number is
exactly three in the bounded core, and the primitive root `P` is a
maximizing cube root of length `p` with left endpoint `A`.

The proof works with a finite tail-label bound `K` after replacing `p/3`
by `p/K`: at a mismatch the actual label `k` is larger than the local one
and `k r>p+j`.  If a whole replay completes, `P^3` remains a primitive
cube suffix, although it need not maximize when labels above three are
allowed.

This is a forward/backward ancestry dichotomy, not a termination proof.
Its exact residual is a self-replaying `P` which matures at the fixed
origin `A`, or an internal target-side cube whose left endpoint lies
between `A` and `M`.

If the replay completes and the actual output contains `P^3` on
`[A,A+3p)`, inspect the third copy rather than the second.  At its cut
`j`, the local word

`P^2 P[:j]`

has curling number at most the actual label `P[j]`.  A strict inequality
can only be `2<3`.  The actual maximizing cube then has length greater
than `2p+j`, so its root `r` satisfies

`r>(2p+j)/3>2p/3`

and the cube starts strictly before `A`.

If equality holds at every third-copy cut, `P` obeys the complete proper
cyclic self-label equations.  Let `pc_P(j)` be the maximum integer exponent
at phase `j` of the circular word `P` among roots shorter than `p`.  The
earlier no-deficit equations `cn(PP[:j])=P[j]` give
`pc_P(j)>=P[j]`, because every witnessing root there is shorter than `p`.
Conversely, every proper cyclic power ending at phase `j` occurs in the
terminal two rotated copies contained in `P^2P[:j]`; equality at the
third-copy cut gives `pc_P(j)<=P[j]`.  Therefore

`pc_P(j)=P[j]`

at every cut.  The fixed-maturation residual is consequently not an
arbitrary self-generating word: it is a fixed point of this finite
proper-cyclic curling operator.

For a primitive circular word, a proper-root periodic factor with root
length `q<p` has length strictly less than

`p+q-gcd(p,q)<2p`.

If it reached the first bound, Fine--Wilf would give period `gcd(p,q)` on
a complete length-`p` conjugate of `P`, making `P` imprimitive.  Hence two
rotated copies really do detect every proper cyclic integer power used in
the preceding definition.

## Executed falsifier for the midpoint-parent assertion

The stronger empirical assertion that every generated `p>=5` square has,
at its midpoint, a `2`-episode of root greater than `p/3` and episode
origin before the child origin is false, even for a binary seed.

The executed seed

`2332232223322233223222332223322322233`

has length `37`.  Its orbit begins with three copies of

`P=223222322232322232223`

of length `21`, followed by the labels `3,2,1`.  At time `42`, the state
ends with the generated square `P^2`; its curling number is two, its full
root spectrum is `(4,10,21)`, and the root-`21` episode starts at absolute
position `37`, exactly the square origin.  At midpoint time `21`, the root
spectrum is `(4,10)`.  Their episode origins are respectively `48` and
`38`, both on or to the right of the child origin `37`.

The missing ancestry has moved earlier.  At times `1` and `2`, the actual
maximizing root is `13`; its power starts at absolute position `11`, before
the child origin.  Thus the broader replay ancestry survives in this
example, but no midpoint-only formulation can prove it.

An arbitrary-alphabet version occurs already at seed length `25`:

`(2,2,2,3,10,2,2,10,2,2,10,2,2,3,2,2,2,3,10,2,2,10,2,2,10)`.

It emits the same `P^3`, followed by `3,2,1`.  Its comparable earlier root
has length `14` and periodic-union origin zero.
