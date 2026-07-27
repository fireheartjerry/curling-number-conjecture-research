# The bounded-reset sink is a copy-parent ray

This note isolates the gap left by the anchor descent in
`nested_replay.md`.  It does not prove that the gap is impossible.

## Exact coordinates for one reset step

Let `T` be the one-sided word consisting of a seed followed by its curling
orbit, and let

`W=T[x:x+d]`, `cn(W)=1`.

Assume that `e=x+d` is beyond the seed and put

`k=T[e]=cn(T[0:e]) >= 2`.

Choose a primitive root of length `p` which attains this maximum.  Thus
`T[0:e]` ends in a `k`-th power of a length-`p` word.  The power crosses
the left edge of `W`, so

`k p>d`.                                                       (BS1)

There are exactly two coordinate updates.

* If `p<d`, then `p` is a period of all of `W`.  Since `cn(W)=1`,
  `p>d/2`.  Put `b=d-p`.  The prefix and suffix of `W` of length `b`
  are equal.  Translating the suffix occurrence back by one root length
  sends

  `(x+p,b)` to `(x,b)`.                                       (BS2)

  Following the copy to its source therefore changes the reset state by

  `(x,d) -> (x,d-p)`, with `0<d-p<d/2`.                       (BS3)

* If `p>=d`, the whole target copy of `W` lies in the last root block and
  its corresponding copy one block earlier is

  `T[x-p:x-p+d]=W`.                                           (BS4)

  Following this copy changes the state by

  `(x,d) -> (x-p,d)`.                                         (BS5)

  Since the terminal `k`-th power fits in the prefix,

  `k p<=x+d`, hence `(k-1)x<=k(x-p)+d`.                       (BS6)

Every new factor in (BS3) or (BS5) still has curling number one: in (BS3)
it is a suffix of `W`, and in (BS5) it is equal to `W`.

Thus short normalization decreases length while preserving the source
coordinate, whereas a long edge decreases the source coordinate while
preserving length.  The latter coordinate can undergo arbitrarily many
halving-scale moves without leaving an unbounded family of factor
lengths at any one coordinate.

## Exact form after the length reaches a bounded sink

Suppose the reset word has stabilized to a fixed word `B` of length `b`
and occurs at starts

`x_0>x_1>...>x_m`,

where the edge from `x_j` to `x_(j+1)` is long.  Put

`p_j=x_j-x_(j+1) >= b`

and let `k_j=T[x_j+b]`.  Define

`M_j=T[x_(j+1)+b:x_j]`.

The length-`p_j` maximizing root is exactly

`R_j=M_j B`,                                                  (BS7)

and the complete terminal power gives

`T[x_j+b-k_j p_j:x_j+b]=R_j^(k_j)`.                           (BS8)

In particular, the last two copies read

`M_j B M_j B`,                                                (BS9)

and

`k_j(x_j-x_(j+1))<=x_j+b`.                                   (BS10)

The word after the source occurrence of `B` begins with `M_j`; when
`M_j` is nonempty its first symbol is the actual orbit label at the
source cut:

`M_j[0]=cn(T[0:x_(j+1)+b])`.                                  (BS11)

For `b=1`, write the sole symbol of `B` as `a` and put
`v_j=x_j`.  Equations (BS7)--(BS9) say exactly that `v_(j+1)` is a
copy-parent of `v_j` with span `p_j`, except that an arbitrary maximizing
root rather than the least maximizing root may have been selected.
If least maximizing roots are selected throughout, a bounded-sink chain
with `B=(a)` is precisely a monochromatic ray in the canonical
copy-parent graph of `dependency_dag.md`.

This identifies the strength of the unresolved case.  The existing
counterorbit reductions give an infinite canonical ray of appended
`2` symbols.  Every singleton `(2)` has autonomous curling number one,
and every edge on that ray is long because its root length is at least
one.  Hence a hypothetical counterorbit itself supplies an infinite
bounded-sink cascade with `B=(2)`, anchored at a seed occurrence.
Eliminating all bounded-sink cascades therefore requires a new argument
that also eliminates this canonical infinite ray; it is not a consequence
of the unbounded-factor anchor descent alone.

## An all-depth border-only stress test

Define `A_0=(2)` and

`A_(n+1)=A_n x_n A_n`,

where `x_n=3` for even `n` and `x_n=2` for odd `n`.  Then

`|A_n|=2^(n+1)-1`                                             (BS12)

and

`cn(A_n)=1` for every `n>=0`.                                 (BS13)

Here is a proof of (BS13).  In one-based coordinates,

`A_n[i]=2` when `v_2(i)` is even, and
`A_n[i]=3` when `v_2(i)` is odd.                              (BS14)

This follows by induction on `n` from the displayed recurrence.  Also
`v_2(2^(n+1)-i)=v_2(i)` for `0<i<2^(n+1)`, so `A_n` is a palindrome.
If a prefix of length `2r` were a square, its symbols at positions `r`
and `2r` would agree.  Equation (BS14) makes them different because
`v_2(2r)=v_2(r)+1`.  Thus no prefix is a square.  Reversing a square
suffix of the palindrome would give a square prefix, so no square suffix
exists.  A suffix power of exponent at least two contains a terminal
square, proving (BS13).

The proper borders of `A_n` are exactly

`A_0,A_1,...,A_(n-1)`.                                       (BS15)

For completeness, a border of a palindrome has length `q` exactly when
its prefix of length `q` is palindromic.  Put `L=q+1`.  If `L` is not a
power of two, write `L=2^v u` with odd `u>=3`.  Choose `c=1` when
`u=3 mod 4` and `c=3` when `u=1 mod 4`; in the second case `u>=5`.
Then the two mirror positions `2^v c` and `L-2^v c` have valuations
`v` and `v+1`, so their symbols differ by (BS14).  Conversely,
`v_2(2^m-i)=v_2(i)` proves that every prefix of length `2^m-1` is
palindromic.  This proves (BS15).

In particular, the longest-border candidate has

`d=|A_n|`, `b=|A_(n-1)|`, `p=d-b=2^n`,

so `p<d`, `b<d/2`, and it maps `A_n` to `A_(n-1)`.  The construction
therefore passes, to arbitrary depth, every local `cn=1`, period, and
less-than-half-border condition used by a short normalization, over the
fixed alphabet `{2,3}`, ending at the bounded reset `(2)`.  It does not
provide the preceding context that would make every candidate period an
actual maximizing root.  It is therefore a countermodel to a
*border-only* bound on the depth, not an orbit counterexample.

## One context realizes all sparse copy labels to arbitrary depth

The preceding border model can be made exact at every nested source cut
simultaneously.  Fix an odd `n` and put

`P_n=2 A_n 2`.

For every `0<=j<=n`,

`cn(P_n A_j)=x_j`,                                            (BS16)

where `x_j=3` for even `j` and `x_j=2` for odd `j`.  Notice that
`x_j` is exactly the symbol following the prefix occurrence of `A_j`
inside `A_(j+1)`, and `x_n=2` because `n` is odd.  Thus the single
ambient word `P_n A_n 2` has the correct actual curling-number label at
all `n+1` nested normalization cuts.

Here is a complete maximality proof.  It is useful first to classify the
possible square roots at the relevant endpoints.  Let

`a(i)`

be the infinite valuation-parity word from (BS14), let

`M=2^A+2^B`, with even `A>B>=0`,

and consider the prefix `a(1)...a(M-1)`.  If a suffix square has root
length `r`, write `r=2^v u` with odd `u`.  Then:

1. if `B>=1`, then `v>=B-1`;
2. if `v>=B`, then `u=1`, `v` is even, and `v<=A-2`;
3. if positive `B` is even, then `v!=B-1`.

For item 1, equality of the two root blocks at reverse offset `z=r`
equates the symbols at `M-r` and `M-2r`.  If `v<B-1`, their valuations
are respectively `v` and `v+1`, because after factoring `2^v` and
`2^(v+1)` the remaining factors are odd.  Their symbols differ.

For item 2, put `D=A-B` and `R=r/2^B`.  At reverse offsets
`z=2^B y`, `1<=y<=R`, square equality reduces, after cancelling the
common parity shift `B`, to

`v_2(2^D-(y-1)) = v_2(2^D-(R+y-1)) mod 2`.                   (BS17)

At `y=1`, this says `D=v_2(R) mod 2`.  For `1<y<=R`, it says

`v_2(y-1)=v_2(R+y-1) mod 2`.                                 (BS18)

If `R=2^h u` with odd `u>1`, choose `y-1=2^(h+1)`.  This lies
strictly between zero and `R`; its valuation is `h+1`, whereas
`R+2^(h+1)=2^h(u+2)` has valuation `h`.  Hence `u=1`.
Equation (BS17) then gives `h=D mod 2`, so
`v=B+h=A mod 2`, which is even.  The square must fit, so
`2R<=2^D`; the parity condition excludes `h=D-1`, giving
`v<=A-2`.

For item 3, first take `u=1`.  The same reverse-offset comparison at
`z=r` gives valuations `B-1` and `A`, of opposite parity because `B`
and `A` are even.  If `u>=3`, use `z=2^B<r`: the positions
`M-z` and `M-r-z` have valuations `A` and `B-1`, again of opposite
parity.  This proves the square-root classification.

Now take `A=n+1`, `B=j+1`, and first assume `j<n`.  The word

`A_n 2 A_j`

is exactly the valuation-parity prefix ending at `M-1`: its first
`2^A-1` symbols form `A_n`, its next symbol is two because `A` is
even, and for `0<t<2^B` one has
`v_2(2^A+t)=v_2(t)`, producing the final copy of `A_j`.

If `j` is odd, then `B` is even.  Since `A_n` ends in
`A_(j+1)=A_j 2 A_j`, the displayed word ends in

`(2 A_j)^2`,

so a square exists.  Every possible square root is covered by item 2.
For such a root, put `h=v-B`.  A third root copy would equate the
symbols at reverse offset `2^B` in three consecutive blocks.  Their
valuations are

`A`, `B+h`, and `B+h+1`,

respectively.  The first two are even and the third is odd, so no cube
exists in `A_n 2 A_j`.  Prepending the initial symbol of `P_n` cannot
create a cube.  A new cube would have to occupy the whole word
`P_n A_j`, whose length is
`M=2^B(2^(A-B)+1)`.  Here `A-B` is even, so the odd factor is two
modulo three and `M` is not divisible by three.  The maximum in
`P_n A_j` is exactly two.

If `j` is even, then `B` is odd.  For `j=0`, the displayed prefix ends
in `222`.  For positive even `j`, put `R=2 A_(j-1)`.  The word `A_j`
ends in `R`, while `2 A_j=R^2`; hence `A_n 2 A_j` ends in `R^3`.
No fourth power can occur.  Indeed, a fourth power of root length `r`
would make both `r` and `2r` square-root lengths.  If
`v_2(r)=B-1`, item 2 applied to `2r` would require the odd integer
`B` to be even.  If `v_2(r)>=B`, item 2 says `v_2(r)` is even but
would also require `v_2(2r)=v_2(r)+1` to be even.  Both alternatives
are contradictions.  The maximum is exactly three.

The preceding no-fourth-power argument was for `A_n 2 A_j`.
Prepending the initial symbol of `P_n` cannot create a fourth power.
Such a new fourth power would have to occupy all `M` symbols.  If
`B=1`, then `M` is not divisible by four.  If `B>=3`, its root would
have length `M/4` and valuation `B-2`.  Its last two copies lie wholly
inside `A_n 2 A_j`, making `M/4` a square-root length there, contrary
to item 1 because `B-2<B-1`.  Hence the maximum in `P_n A_j` is
exactly three.

It remains to take `j=n`.  Since `n` is odd,

`P_n A_n=(2 A_n)^2`,

so the maximum is at least two.  The word
`A_n 2 A_n=A_(n+1)` has curling number one by (BS13).  If the
one-symbol extension on its left created a suffix cube of root length
`r`, that cube would have to include the new symbol, so

`3r>|A_(n+1)|=2^(n+2)-1`.

It would also have to fit in `P_n A_n`, so `3r<=2^(n+2)`.  No integer
multiple of three lies in this one-integer interval because
`2^(n+2)` is not divisible by three.  Thus the maximum at the last cut
is exactly two.  This completes the proof of (BS16).

The same square-root classification with `B=0`, followed by the same
three-block comparison at reverse offset one, shows that `A_n 2`
has no suffix cube and ends in the square `22`.  Prepending the first
symbol of `P_n` cannot create a cube: such a cube would have length
strictly greater than `2^(n+1)` and at most `2^(n+1)+1`.  The only
integer in that interval, `2^(n+1)+1`, is not divisible by three
when `n+1` is even.  Hence

`cn(P_n)=2`.                                                  (BS19)

Thus `P_n` also produces the first attempted symbol `A_0=2`.  At an
even cut `j>0`, the exhibited maximizing cube root has length
`2^j<|A_j|` and normalizes to the border `A_(j-1)`; at `j=0` its root
has length one.  At an odd cut, the exhibited maximizing square root
has length `2^(j+1)=|A_j|+1` and is a long edge.  The model therefore
realizes an arbitrary alternation of short border normalization and
long copying at the sparse cuts, with exact maxima and exact following
labels.

This is stronger than a border-only stress test: arbitrary-depth
normalization cuts, their common left context, their copy exponents, and
the prescribed following labels are mutually compatible.  It is still
not an orbit counterexample.  The cuts strictly between `A_j` and
`A_(j+1)` also have to carry their prescribed labels.

The first failure is explicit.  Executed code gives

`A_3=232223232322232`,

`P_3=22322232323222322`.

The orbit from `P_3` emits the first four intended symbols `2322`.  At
the next cut the state is

`223222323232223222322`

and ends in

`(2322)^3`.

Both workspace implementations return maximum three at this cut, while
the fifth symbol of `A_3` is two.  Thus the first unrepresented
intermediate replay equation kills this particular realization.

The construction refutes the following precise kind of proposed lemma:
there is no depth bound, independent of the finite left context, derived
only from

* autonomous curling number one of every nested reset;
* its complete proper-border and period data;
* one common context for all selected cuts;
* exact maximality and the correct following label at every selected
  normalization cut; and
* the alternating short-copy/long-copy coordinates at those cuts.

For every proposed depth, `(P_n,A_0,...,A_n)` with sufficiently large
odd `n` satisfies all five data sets.  This does not refute a theorem
which uses a fixed seed globally: the length of `P_n` grows with `n`.
It also does not refute a theorem using all intermediate replay
equations.  Any closure of the bounded-sink gap must use one of those
two sources of information; the selected reset cuts themselves do not
suffice.

## What the actual copy labels add

The stress test is not by itself an orbit tail.  Its sparse normalization
cuts show exactly where extra masking is required.

More generally, suppose

`A_n=A_j M A_j`, `j<n`,

and put `R=M A_j`, `p=|R|=|A_n|-|A_j|`.  If a context `P` makes the cut
after `P A_n` have curling number `k` through this root `R`, then the
terminal power equation forces

`P` to end in `R^(k-2) M`,                                    (BS20)

and consequently the earlier cut after `P A_j` ends in

`R^(k-1)`.                                                    (BS21)

For the immediate border `j=n-1`, the next prescribed symbols at these
two cuts are `x_(n-1)` and `x_n`, which alternate.

* If `n` is even, the target label is `x_n=3` and the source label is
  `x_(n-1)=2`.  Equations (BS20)--(BS21) force exactly the needed square
  at the source; no contradiction occurs.
* If `n` is odd, the target label is `x_n=2` and the source label is
  `x_(n-1)=3`.  The source cube must use a root `Z` different from the
  displayed `R`.  Moreover

  `3|Z|>p`.                                                    (BS22)

  If `3|Z|<=p`, the entire source cube lies in the terminal source copy
  of `R`.  The target cut copies that `R` once more, so the same cube is
  a suffix at the target, contradicting its prescribed maximum two.

Thus the exact labels do not turn the border descent into a
well-founded argument.  They replace every other level by a new
large-root masking obligation, with root length greater than one third
of the current copy scale.  Ruling out an infinite alternation of these
large masks is the remaining load-bearing step.

`research/check_bounded_sink.py` executes the curling-number assertions
for the first ten stress-test levels and the full sparse profiles for
odd depths through nine, using both workspace implementations.  It also
checks the earlier finite context `P=22322`, for which the sparse cuts
after `A_0,A_1,A_2,A_3` have curling numbers `3,2,3,1`.  The script
additionally checks that this context is not a full orbit realization:
after it emits the first two desired symbols `2,3`, its next curling
number is `1` rather than the required `2`.
