# Rigorously established reductions

These are reductions only. They do not resolve the conjecture.

## Definitions used below

For a nonempty finite word `W`, let `c(W)` be its curling number. A
*maximizing root* is a nonempty word `Y` for which `W = X Y^c(W)`.
Among maximizing roots, `rho(W)` is the least root length.

## Lemma 1 — a new final symbol forces curling number one

If an integer `a` does not occur in `W`, then `c(Wa)=1`.

Proof. If `Wa` ended in `Y^r` for some `r >= 2`, the final symbol of the
penultimate copy of `Y` would be `a`. That occurrence lies in `W`, contrary
to the hypothesis. Therefore no exponent at least two is feasible, while
exponent one is feasible.

Consequently, in an orbit with `c(S_n) >= 2` for every `n`, every appended
value occurs in the seed. Follow the earlier equal-symbol occurrence from
Lemma 1 backwards through the finite list of prior append positions; the
strictly decreasing position index eventually reaches the seed. Thus the
set of appended values is finite and bounded.

## Lemma 2 — a maximizing root is primitive

If `W = X Y^k`, where `k=c(W)`, then `Y` is not a proper power.

Proof. If `Y=Z^r` with `r>=2`, then `W=X Z^(rk)`, so `c(W)>=rk>k`, contrary
to `k=c(W)`.

## Lemma 3 — the next curling number rises by at most one

Let `k=c(W)` and `l=c(Wk)`. Then `l <= k+1`.

Proof. Choose `B=P k` with `Wk=Q B^l`. Deleting the last symbol gives
`W=Q B^(l-1) P`. The last `(l-1)|B|` symbols of this word are
`(kP)^(l-1)`. Hence `c(W)>=l-1`, so `l<=k+1`.

## Lemma 4 — a counterorbit has unbounded maximizing-root lengths

Assume an orbit has no curling number one. Let `K` bound its appended
values as supplied by Lemma 1. If `rho(S_n)<=P` from some point onward, put
`L=KP`. For all sufficiently large `n`, a maximizing suffix of `S_n` lies
inside its last `L` symbols. Every powered suffix of that length-`L` suffix
is also a powered suffix of `S_n`; therefore the two words have the same
curling number. The length-`L` suffix then evolves by a deterministic map on
the finite set of length-`L` words over the seed alphabet. Its sequence is
eventually periodic. The corresponding appended tail is eventually a
nonempty periodic block `B` repeated indefinitely. At the end of `r`
copies, the current word ends in `B^r`, giving curling number at least `r`.
Taking `r>K` contradicts the bound. Therefore `rho(S_n)` is unbounded.

## Lemma 5 — an orbit cannot have curling numbers eventually at least three

External theorem used: F. Mignosi, A. Restivo, and S. Salemi, “Periodicity
and the golden ratio,” *Theoretical Computer Science* 204 (1998), 153–167,
DOI 10.1016/S0304-3975(98)00037-1. Their infinite-word characterization is:
a right-infinite word is ultimately periodic if and only if every
sufficiently long prefix has a suffix whose exponent is at least
`phi^2`, where `phi=(1+sqrt(5))/2`.

Suppose `c(S_n)>=3` for every `n>=T`. Form the right-infinite word consisting
of `S_0` followed by every appended curling number. Its prefixes of all
lengths at least `|S_0|` are exactly the orbit states. Each prefix from
`S_T` onward ends in a cube, whose exponent `3` exceeds `phi^2`. The cited
theorem makes the infinite word ultimately periodic.

The tail alphabet is finite: for `n>=T`, the fact that `c(S_{n+1})>=3`
and Lemma 1 force the symbol appended at step `n` to occur earlier, and
backward iteration places it in `S_T`. Let `K` bound the positive symbols
of `S_T`. In the ultimately periodic tail, choose a period length `p` and
then a sufficiently late prefix ending in `K+1` complete period blocks.
That prefix has curling number at least `K+1`, although its next appended
value belongs to the finite set bounded by `K`. This is a contradiction.

Thus every orbit has infinitely many indices with curling number at most
two unless it fails to be infinite. In particular, every hypothetical
counterorbit has curling number exactly two infinitely often.

## Lemma 6 — recurrent values form an integer interval

In a hypothetical counterorbit, let `M` be the greatest appended value that
occurs infinitely often. Then every value `2,3,...,M` occurs infinitely
often.

Proof. Lemma 3 says an appended value can increase by at most one at the
next step. Lemma 5 supplies infinitely many occurrences of `2`. Fix
`r` with `2<r<M`. If only finitely many `r` occurred, discard the prefix
through its last occurrence. Infinitely many later `2` values and `M`
values remain. Every passage from a value below `r` to a value above `r`
must contain `r`, because each individual increase is at most one. This
contradicts the discarded last occurrence.

## Lemma 7 — the exact two-level escape block

Suppose an appended label is `r>=2`. If, before the next label at most `r`,
the orbit first reaches a label at least `r+2`, then the intervening factor
is exactly

`r (r+1)^(r+2) (r+2)`.

Proof. Put `c=r+1`, and suppose there are `m` copies of `c` before the
first `r+2`. Lemma 3 forces every intervening label to equal `c`. There
cannot be more than `r+2` copies: after appending `r+2` copies of `c`, the
current word has curling number at least `r+2`, so it cannot request another
`c`.

Assume `m<=r+1`, and let `P` be the state immediately before the displayed
`r`. The state `P r c^m` ends in `Y^(r+2)` for some nonempty `Y`. If
`|Y|<=m`, that power lies in the terminal run of `c` far enough to include
the preceding `r`, forcing `r=c`. If `|Y|>=m+1`, write `B=r c^m` and
`Y=A B`. Removing the final `B` from `(AB)^(r+2)` shows that `P` ends in
`(AB)^(r+1)A=A(BA)^(r+1)`, so `c(P)>=r+1`, contrary to the displayed label
`r`. Hence `m=r+2`.

This lemma is not a descent: explicit marker-word families realize the
escape and return with the same maximizing-root length.

## Lemma 8 — the bounded `{2,3}` core has infinitely many small cube states

Assume a hypothetical counterorbit is eventually confined to `{2,3}`.
Three consecutive appended `3` values force a fourth `3`, after which the
terminal run has exponent four, contradicting the bound. Three consecutive
appended `2` values force the following curling number to be `3`. Therefore
from every sufficiently late index `n`, the next index `j` with curling
number `3` satisfies `0<=j-n<=3`.

If `S_j` has a cube suffix with root length `p`, deleting the `j-n` future
symbols leaves `S_n` with a suffix of period `p` and length at least
`3p-3`. For `p>=8`, its exponent is at least `21/8`, which is greater than
`phi^2`. If every sufficiently late `3`-state had at least one cube root of
length at least eight, every sufficiently long prefix of the infinite orbit
word would have a `phi^2`-suffix. The Mignosi–Restivo–Salemi theorem cited
in Lemma 5 would make the word ultimately periodic, contradicting bounded
curling numbers.

Consequently, infinitely many `3`-states have no cube root longer than
seven. This leaves a finite family of terminal cubes, but a comparison with
the autonomous promoted suffix orbit can be broken by a longer cube that
crosses the retained context. No monotone rank preventing repeated resets
of that crossing root has yet been established.

## Lemma 9 — successive `2` events have a root-gap trichotomy

Let `t<s` be successive indices with curling number `2`, let
`D=(c_t,...,c_(s-1))`, and put `d=|D|=s-t`. Thus `D` begins with its unique
`2`. If `S_s=Q V^2` and `n=|V|`, exactly one of the following holds:

1. `d<n`, with `V=F D` and `S_t=Q F D F`;
2. `d=n`, with `V=D` and `S_t=Q D`;
3. `d>2n`, with `D=E V^2`, where `V` contains no `2`.

For `n<d<2n`, suffix comparison writes `D=G V` with nonempty `G` a suffix
of `V`. The unique `2` in `D` lies in `G`, so its copied occurrence lies in
`V`, a contradiction. For `d=2n`, the equality `D=V^2` gives zero or at
least two occurrences of `2`, also a contradiction. The remaining length
ranges give the displayed cancellation equations.

In the `{2,3}` core the only third-branch possibility is `D=233`, `V=3`.
Repeated occurrences of this branch can increase the neighboring cube
period, so root length, gap length, and predecessor period do not supply a
strict return descent.

## Lemma 10 — low-root square states are syndetic in the `{2,3}` core

Let `t_j` be the successive indices carrying label `2`, put
`d_j=t_j-t_(j-1)`, and define `h(1)=2`, `h(2)=23`, `h(3)=233`. Runs of
three `3` labels are impossible, so every `d_j` lies in `{1,2,3}` and the
state at `t_j` ends in `h(d_j)`.

Let `rho(S)` denote the least length of a root attaining `cn(S)`. If
`d_j=3`, then `S_(t_j)` ends in `33` and `rho=1`. If two consecutive gaps
are `1,1`, the state ends in `22` and again `rho=1`. If they are `2,2`, it
ends in `(23)^2`, so `rho<=2`.

Consequently, if six consecutive incoming gaps led to `2`-states all having
`rho>2`, those gaps would have to alternate `1,2`. Their encoded output
would end in either `h(12)^3=(223)^3` or `h(21)^3=(232)^3`. The final
state would then have curling number at least three, contrary to its label
`2`. Thus every six consecutive `2`-states contain one with `rho<=2`.
Since successive `2` states are at distance at most three, these low-root
reset states are syndetic.

## Lemma 11 — strict nesting of primitive cubes more than doubles the root

Suppose a factor `Y^3`, with primitive root length `p`, is strictly contained
in `Q^3`, with primitive root length `q`, and `q>p`. Then `q>2p`.

Assume instead `p<q<=2p`, and put `g=gcd(p,q)`. The length-`3p` word `Y^3`
has periods `p` and `q`; the latter is inherited from the containing
`q`-periodic cube. Since `3p>=p+q-g`, Fine--Wilf makes `g` a period. The
least period of `Y^3` is `p`, so `g=p` and `p` divides `q`. Hence `q=2p`.
But the first `q` symbols of the contained `Y^3` equal `Y^2`, while every
length-`q` factor of `Q^3` is a conjugate of `Q`. A conjugate of `Q` is
therefore a square. Conjugacy preserves being a proper power, contradicting
the primitivity of `Q`.

This lemma alone does not give a descent. Iterated images of a cube under
the square of the Fibonacci morphism give strictly nested primitive cubes
whose root lengths grow by a factor greater than two inside a fourth-power-
free recurrent word. The exact self-label condition is therefore essential.

## Lemma 12 — full root transport across a successive-`2` gap

In case 1 of Lemma 9, write `V=FD`, so

`S_t=Q F D F` and `S_s=Q (F D)^2`.

The later root of length `|V|` is a rotation of an old co-terminal root of
the same length exactly when `Q` ends in `D`. Indeed, if `Q=Q'D`, then
`S_t=Q'(D F)^2`, and appending `D` turns the old root `DF` into `FD`.
Conversely, cancellation from an old same-length square forces this terminal
copy of `D` in `Q`. When `Q` does not end in `D`, the equation
`S_t=X R^2=QFDF` describes a genuine root birth rather than transport.

A fixed transported root of length `n` cannot survive through `2n` appended
symbols: those symbols supply two complete successive rotations and make a
fourth power at the corresponding state. Hence an infinite `{2,3}` model
would require infinitely many genuine births of unbounded root length. No
well-founded order on these births has yet survived audit.

## Lemma 13 — increases between consecutive cube states more than double

In an eventual `{2,3}` tail, let `i<j` be consecutive indices labelled `3`,
and let `p,q` be the least primitive maximizing cube-root lengths there.
There are at most three intervening `2` labels, so `Delta=j-i<=4`. If
`q>p` and `q>=p+2`, then `3(q-p)>Delta`; the later cube strictly contains
the earlier one, and Lemma 11 gives `q>2p`.

The remaining putative increase has `q=p+1`. For `Delta<=3`, containment
again invokes Lemma 11 and is impossible. For `Delta=4`, the cubes overlap
in `3p-1` symbols with periods `p` and `p+1`. Fine--Wilf applies because
`3p-1>=2p`, so this overlap has period one. It contains a full length-`q`
block of the later root (including when `p=1`), making that root constant
and nonprimitive. Therefore every increase satisfies `q>2p`.

Root lengths may still fall abruptly. Executed orbit traces exhibit rises
such as `1 -> 4 -> 21`; the lemma supplies growth of rises but no global
monotonicity.

## Lemma 14 — a counterorbit has an infinite monochromatic copy-parent ray

Let `W` be the seed followed by the infinite appended tail. For an appended
position `v`, choose the least root length `p(v)` attaining the curling
number of the prefix ending at `v`, and define `parent(v)=v-p(v)`. The last
symbols of the final two root copies agree, so the parent has the same symbol
as `v`.

This directed forest is locally finite. If `parent(v)=u`, the final square
has length `2(v-u)` and fits in a prefix of length `v+1`; hence

`v <= 2u+1`.

Every infinitely recurrent appended value therefore has an infinite
monochromatic parent ray by Koenig's infinity lemma. In particular, Lemma 5
gives an infinite ray of `2` vertices in every counterorbit.

Write the ray as `v_0<v_1<...`, put `d_i=v_i-v_(i-1)`, and let
`e_i=W[v_i+1]`. Then the prefix ending at `v_i` ends in `B_i^(e_i)` with
`|B_i|=d_i`; moreover `2<=e_i<=a+1` on an `a`-ray. Two useful exact
constraints are:

* `r` consecutive equal spans create `r+1` adjacent equal blocks, so
  `r<=a`;
* if `d_i>=e_(i-1)d_(i-1)`, copying the entire previous canonical power
  forces `e_i>e_(i-1)` (equality would give a shorter maximizing root).

The ray is a fixed-lineage object that avoids the drifting-subsequence flaw
of recurrence arguments. Its spans can nevertheless rise and fall in
calibrated finite orbits, and no well-founded overlap rank is known yet.

## Lemma 15 — top-level excursions have exact returns for every `M>=4`

Put `r=M-2`, let `A` be the one-letter word `(M-1)`, let `R=(M-2)` and
`H=(M)`, and define

`B=A^r R`, `Y=B^(M-1) A^M H`, `W=Y B^r A^r`.

Then the orbit of `W` begins with the labels

`r, (M-1)^M, M, 2`.

For the maxima before `M`, the unique `H` confines powered suffixes to the
displayed tail. Counting occurrences of `R` bounds roots containing `R`,
while the terminal `A` run handles roots avoiding it; the factorizations

`B^(M-1)A^h=A^h(A^(r-h) R A^h)^(M-1)`

supply the lower bounds. After the final `M`, the identity

`W R A^M H=Y^2`

gives curling number two; exactly two occurrences of `H` exclude exponent
three. Thus a forced rise from `M-2` to `M` can return immediately to `2`
with an arbitrarily large exact root. This blocks every local reduction of
the recurrent maximum to three.

For any genuine top entrance `E=(M-2)(M-1)^M M`, a surviving state after
the final `M` has a maximizing root of length at least `M+2`, and `E` is a
suffix of that root. Repetition of the root therefore points to earlier
copies of the whole entrance `E`. Since all recurrent values form
`{2,...,M}`, infinitely many such entrances yield another locally finite
return-word hierarchy; its global incompatibility remains to be proved.

## Lemma 16 — golden-ratio bad cuts force bounded cube kernels

For a finite word `W`, let `E(W)` be the maximum exponent of any suffix,
allowing fractional exponents. Then

`cn(W)=floor(E(W))`.

One direction truncates a periodic suffix to an integral number of periods;
the other is immediate from a powered suffix. Let
`alpha=phi^2=(3+sqrt(5))/2`. A counterorbit is aperiodic, since an ultimately
periodic tail would produce arbitrarily large integral suffix powers. The
Mignosi--Restivo--Salemi criterion therefore gives infinitely many states
`S_n` with `E(S_n)<alpha`. Every such state has label `2`.

Let `d` be the least positive index with `c_(n+d)>=3`. Three appended `2`
values force a cube, and the rise bound makes the first higher value exactly
`3`; hence `d` is `1`, `2`, or `3`. If `Y^3` is any cube suffix at that
state and `p=|Y|`, deletion of the `d` appended `2` values gives a periodic
suffix of `S_n` with exponent `3-d/p`. Since `3-alpha=1/alpha`, badness
forces

`p<d*alpha`.

Thus every cube root at this distinguished `3`-state has length at most
`2`, `5`, or `7` for `d=1`, `2`, or `3`. Primitivity further says either
`p=1,Y=2`, or `p>d` and `Y=A 2^d`. The preceding bad cut ends in the kernel
obtained from `Y^3` by deleting its last `d` symbols, of length at most 18.
This conclusion holds for an arbitrary recurrent maximum, not only a
`{2,3}` tail.

The finite kernel does not determine future badness. Executed orbit states
can share one complete bad word as a suffix and nine subsequent integer
labels, while a hidden period crossing that suffix makes only the longer
state golden-good. The remaining state is therefore a stack of latent
fractional periods, not a finite automaton on the kernel.

## Lemma 17 — canonical-ray run breaks have exact normal forms

On the infinite `2`-ray of Lemma 14, the root `B_i` begins with `e_(i-1)`
and ends with `2`: its last copy is exactly the output block after the parent
vertex. Hence the `d_i`-periodic run extends through the next appended label
exactly when `e_i=e_(i-1)`. A flip is a maximal-run boundary, with normal
form

`(2 A 2)^3 3` for an ascent and `(3 A 2)^2 2` for a descent.

For consecutive ray spans `D,d`, exponents `E,e`, and `g=gcd(D,d)`, the
two canonical powers overlap in

`O=min(E D,(e-1)d)`

symbols. Fine--Wilf and primitivity show that unequal spans must satisfy

`d>(E-1)D+g` or `D>(e-2)d+g`.

In the `{2,3}` core this is exhaustive: an `e=2` step shifts the complete
power interval right; an unequal `e=3` step either expands its left boundary
(and, after a preceding cube, more than doubles the scale) or drops to
`d<D-g` and shifts right. Calibrated rays realize repeated expansion/drop
cycles, so the dichotomy is structural but is not itself a descent.
