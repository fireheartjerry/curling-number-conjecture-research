# Recurrent fixed-origin cube towers

This note isolates what recurrence and local-period theorems can and cannot
do to the residual fixed-origin cube tower.  It does **not** prove the
Curling Number Conjecture.  Its main result is a countermodel showing that
the exact orbit self-label equations, rather than recurrence or ordinary
power avoidance, must carry any remaining argument.

## 1. A Fibonacci countermodel

Let

`mu(0)=01`, `mu(1)=0`,

put `h=mu^3`, and write

`A=h(0)=01001`, `B=h(1)=010`.

Define `Q_0=B`.  Inductively, `Q_n` starts in `0`, so `h(Q_n)` starts in
`A`; write

`h(Q_n)=A R_n`

and define

`Q_(n+1)=R_n A`.

Equivalently, the defining conjugacy equation is

`A Q_(n+1)=h(Q_n) A`.                                      (1)

### Lemma 1 (avoidance invariant)

Every `Q_n` starts in `0` and avoids `11`.

**Proof.**  The assertion holds for `Q_0=010`.  Both images `A=01001` and
`B=010` start in `0` and avoid `11`.  At a boundary between two images,
the right image starts in `0`, so no `11` is created.  Removing the first
copy of `A` from `h(Q_n)` leaves a word starting in `0`, because `Q_n` has
at least two letters and the next image starts in `0`.  Appending `A`
again creates no `11`, because `A` starts in `0`.  This proves the
induction step.  ∎

### Lemma 2 (nested cubes)

For every `n>=0`, `Q_n^3` is a prefix of `Q_(n+1)`.

**Proof.**  Directly from the definitions,

`Q_1=0100100101001=Q_0^3 1001`.

Assume `Q_(n+1)=Q_n^3 E`.  The word `E` has at least two letters.  One way
to see this without using an asymptotic estimate is that each letter image
under `h` has length at least three, while `Q_n` contains a `0`, whose
image has length five; hence

`|Q_(n+1)|=|h(Q_n)|>=3|Q_n|+2`.

By Lemma 1, `E` avoids `11`.  If `E` starts in `0`, then `h(E)` starts in
`A`.  If `E` starts in `1`, its first two letters are `10`, and

`h(10)=01001001`

also starts in `A`.  Thus in both cases `h(E)=A Z` for some word `Z`.

Put `H=h(Q_n)`.  Equation (1) gives

`H A=A Q_(n+1)`.

Multiplying this conjugacy equation successively gives

`H^2 A=A Q_(n+1)^2`,

`H^3 A=A Q_(n+1)^3`.                                      (2)

Applying `h` to the induction hypothesis and using (2),

`h(Q_(n+1))=H^3 h(E)=H^3 A Z=A Q_(n+1)^3 Z`.

Equation (1) at level `n+1` is

`A Q_(n+2)=h(Q_(n+1))A`.

Deleting the common initial `A` shows that `Q_(n+2)` starts in
`Q_(n+1)^3`.  This is the induction step.  ∎

The words `Q_n` are nested prefixes, so they define a right-infinite limit

`x=lim_n Q_n`.

Lemma 2 says that `x` has the primitive cube prefix `Q_n^3` for every
`n`.

### Lemma 3 (the roots are primitive)

Every `Q_n` is primitive.

**Proof.**  Equation (1) says that `Q_(n+1)` is conjugate to `h(Q_n)`.
Therefore `Q_n` is conjugate to

`mu^(3n)(Q_0)=mu^(3n+3)(1)`.

With Fibonacci numbers indexed by `F_0=0`, `F_1=1`, this word has length
`F_(3n+4)` and contains `F_(3n+2)` copies of `1`.  These two counts are
coprime:

`gcd(F_(r+2),F_r)=gcd(F_(r+1),F_r)=1`.

If `Q_n=V^e` for an integer `e>=2`, then `e` divides both its length and
its number of `1` symbols, contradicting coprimality.  ∎

### Lemma 4 (Fibonacci language and recurrence)

Every factor of `x` is a factor of the Fibonacci fixed word
`f=mu^omega(0)`.  Consequently `x` belongs to the Fibonacci subshift and
is uniformly recurrent.

**Proof.**  Put `W_n=mu^(3n+3)(1)=mu^(3n+2)(0)`.  The word `Q_n` is a
conjugate of `W_n`.  Since `00` is a factor of `f` and `mu(f)=f`,

`W_n^2=mu^(3n+2)(00)`

is a factor of `f`.  Every conjugate of `W_n` occurs as a length-`|W_n|`
factor in `W_n^2`; hence `Q_n` is a factor of `f`.

Any finite factor of `x` is contained in a sufficiently long prefix
`Q_n`, so it is a factor of `f`.  Thus `x` is in the orbit closure of
`f`.  The Fibonacci substitution is primitive, so its subshift is
minimal; every point in it is uniformly recurrent.  ∎

The Fibonacci word has critical exponent `2+phi<4`.  Hence neither `f`
nor `x` contains a fourth power.  This is a standard background theorem;
one source is F. Mignosi and G. Pirillo, *Repetitions in the Fibonacci
infinite word*, RAIRO Theoretical Informatics and Applications 26 (1992),
199--204.  This citation is not being used as an orbit theorem.

### Lemma 5 (a fixed delimiter on an infinite subtower)

For every `n>=1`, the symbol immediately following the prefix `Q_n^3` in
`x` is `0`.

**Proof.**  In the notation in the proof of Lemma 2, write `h(E)=A Z`.
If `E` starts in `0`, the symbol after the initial image `A` is the first
symbol of the next image and is `0`.  If `E` starts in `10`, the first six
symbols of `h(E)` are the first six symbols of
`h(10)=01001001`, and the sixth symbol is `0`.  Thus `Z` starts in `0`.
The proof of Lemma 2 identifies `Z A` as the suffix of `Q_(n+2)` after
`Q_(n+1)^3`.  The base suffix after `Q_1^3` in `Q_2` also starts in `0`,
by the same calculation applied to the suffix `1001` after `Q_0^3`.
∎

Code the letters by `0 -> 3`, `1 -> 2`.  The resulting word is a uniformly
recurrent word over `{2,3}`, is fourth-power-free, and has unbounded
primitive cube prefixes followed by `3`.  It is **not** an orbit word:
it does not obey the full equality

`W[n]=cn(W[0:n])`

at every generated position.  The construction therefore identifies the
missing hypothesis precisely: recurrence, primitivity, a fixed origin,
fourth-power avoidance, and even the correct delimiter on the record
cubes do not replace the internal self-label equations.

## 2. Why the local-period gap theorem does not close the tower

Use a cut coordinate `t` equal to the number of symbols strictly to the
left of the cut.  The central local period `c_2(x,t)` of
Duval--Mignosi--Restivo is the least period of a square centered at that
cut, allowing an external square at the left edge of a one-sided word.
Their gap theorem says, in their zero-based point convention, that a
recurrent aperiodic word has infinitely many record cuts whose local
period reaches past the left edge; in the present cut coordinate this is
`c_2(x,t)>=t`.

If `x` starts in `Q_n^3`, then every cut in the middle copy,

`|Q_n| <= t <= 2|Q_n|`,

has a centered square of period `|Q_n|`.  Therefore

`c_2(x,t)<=|Q_n|<=t`

throughout that interval.  The gap-theorem cuts must lie outside the
union of these middle-third intervals.  The tower roots are strongly
separated; in the explicit Fibonacci construction their lengths are
`F_(3n+4)`, so the intervals leave large gaps.  The local-period theorem
does not supply a covering statement for those gaps, and the explicit
word above realizes both the cube tower and the theorem's unbounded local
periods.

Reference: J.-P. Duval, F. Mignosi, A. Restivo, *Recurrence and
periodicity in infinite words from local periods*, Theoretical Computer
Science 262 (2001), 269--284, DOI
`10.1016/S0304-3975(00)00204-8`.  Their central local period is defined in
Section 3; recurrence and local periods are treated in Theorem 5 and the
record/gap argument following it.

## 3. What exact self-labels do transfer

Let `U` and `V` be two finite words with the same suffix of length `L`.
For every root length `r` and exponent `e` with `er<=L`,

`U ends in an e-power of root length r`

if and only if

`V ends in an e-power of root length r`.

Thus finite returns transfer all lower-bound certificates that fit inside
the common suffix.  They do not transfer the upper half of a curling
number equality: a longer repeated suffix can cross the left edge of the
common context on only one side.

More quantitatively, suppose the next labels after `U` and `V` differ,
the larger is `k`, and a maximizing `k`-power on the high side has
primitive root length `r`.  Then necessarily

`k r>L`;                                                     (3)

otherwise the same `k`-power would occur on the low side.  Equation (3)
is the exact source of the comparable-scale roots in all first-divergence
arguments.

For a generated cube `Q^3`, at the occurrence of `Q[d]` in the third
copy, the prefix immediately before that symbol ends in the square of the
rotation

`Q[d:|Q|] Q[0:d]`.

Hence the copied label is at least `2`.  If that label is exactly `2`, the
rotation square is compatible with maximality.  If the label is at least
`3`, some additional power certificate is required, but its root can be
small or can cross the fixed origin.  Recurrence copies the visible
rotation square; it does not by itself copy this hidden maximizing root.
That is the residual return-word obstruction.

## 4. Proper cyclic curling fixed points

The normalized autonomous tower gives a sharper finite object.  Let `Q` be
a primitive word of length `q`.  At a cut `d mod q`, define

`pc_Q(d)`

to be the largest integer exponent of a power ending at that cut in the
two-sided periodic word `Q^Z`, when the root length `p=q` and its multiples
are excluded.  Call this the *proper cyclic curling profile*.

### Lemma 6 (two copies detect every proper cyclic power)

If a factor of `Q^Z` has a period `p<q`, then its length is strictly less
than

`q+p-gcd(q,p)<2q`.

**Proof.**  Suppose a factor has length at least
`q+p-gcd(q,p)`.  It has periods `p` and `q`, so Fine--Wilf gives period
`g=gcd(q,p)`.  Its length is at least `q`, hence it contains a complete
length-`q` conjugate of `Q`.  Since `g` divides `q` and `g<q`, that
conjugate is a proper power.  Conjugacy preserves primitivity, contradicting
the hypothesis on `Q`.  ∎

It follows that `pc_Q(d)` can be computed from the suffixes of

`Q^2 Q[0:d]`

using only root lengths `p<q`; no still earlier periodic context can add a
proper power.  Indeed, if `p>q` is not a multiple of `q`, a square of
root length `p` has length `2p>=p+q-gcd(p,q)`.  Fine--Wilf would again
make a complete conjugate of `Q` imprimitive.  Root lengths that are
multiples of `q` are the excluded global periodic roots.

### Lemma 7 (necessary fixed-point equation)

If the orbit from `Q` appends two complete further copies of `Q`, then,
for every `0<=d<q`,

`pc_Q(d)=Q[d]`.                                             (4)

**Proof.**  Immediately before the occurrence `Q[d]` in the third copy,
the state is `Q^2 Q[0:d]`, and the orbit hypothesis says that its curling
number is exactly `Q[d]`.  The length-`q` root supplies an exponent-two
suffix, and all roots of length less than `q` are precisely the proper
cyclic roots detected by Lemma 6.  Since every tower symbol is at least
two, taking the maximum of the global-root contribution `2` and the
proper profile leaves exactly equation (4).  ∎

For the binary specialization, equation (4) says:

* every cut ends in a proper square;
* a cut is followed by `3` exactly when it ends in a proper cube;
* no proper fourth power occurs.

This follows because the only allowed profile values are `2` and `3`.
It is much stronger than being squareful and fourth-power-free.

The program `search_proper_cyclic_fixed.cpp` exhaustively checks (4).  In
the executed binary search through length `24`, the only solutions were
the `21` rotations of

`P=223222322232322232223`.

There were no solutions of any other length in that interval.  This is a
finite computation, not a classification theorem.  The same `P` is a
genuine cube self-replicator: executed code shows that the orbit from `P`
appends `P^2`, reaches `P^3` with curling number three, appends `3`, and
then has output `2,1`.  Even more specifically, the seed

`P[0:8]=22322232`

generates the remainder of `P`, then two more complete copies of `P`, then
`3,2,1`.  These values were produced by both implementations in
`curling.py`.

For `P`, the least maximizing proper-root lengths at its `21` cuts are

`4,4,4,3,3,1,1,7,4,1,1,4,4,2,2,1,1,6,6,1,1`.

Writing `f(d)=d-r_d mod 21`, the functional graph has two directed cycles:

`0 -> 17 -> 11 -> 7 -> 0`, with spans `4,6,4,7`,

and

`1 -> 18 -> 12 -> 8 -> 4 -> 1`, with spans `4,6,4,4,3`.

Each set of spans sums to `21`.  The symbols immediately preceding cuts
on the first cycle are all `3`; those on the second are all `2`.  This is
an instance of a general fact: a root edge preserves the symbol
immediately before its endpoint.

### Lemma 8 (cycles are anchored in the finite seed)

Suppose an infinite autonomous orbit word has a finite seed of length
`N`, and an unbounded family of primitive prefix roots `Q_i` satisfying
(4).  Choose at each cut a least maximizing proper root `r_i(d)`.  For
every generated cut `d>=N`, the actual maximizing witness is contained in
the finite prefix ending at `d`; hence

`r_i(d)<=d/Q_i[d]<=d/2`

and the non-cyclic lift `d -> d-r_i(d)` is nonnegative and strictly
decreasing.  Consequently every directed cycle of the circular parent map
must contain a cut `s<N` whose edge wraps modulo `|Q_i|`.

Along a directed cycle the sum of its edge lengths is

`m |Q_i|`,

where `m` is the number of such wrap edges.  There are at most `N` wrap
edges.  The parent map preserves the preceding symbol, so every cycle is
monochromatic in that cut-coloring.

This reduces the circular fixed-point classification to finitely anchored
long copy-parent chains, but no well-founded rank on those chains is
currently proved.  The `P` cycles above show that the return equations can
close nontrivially at one finite scale.

## 5. Cycle-local compression is false

The note `anchored_cycle_countermodel.md` gives an explicit unbounded
family showing that Lemma 8 cannot be compressed using only equations on
one selected cycle.  For every `L>=2`, set

`A_r=2^(r-2)32` for `3<=r<=L+2`

and

`Q_L=A_3 A_4 ... A_(L+2)`.

The `L` arc-end cuts form a single winding-one parent cycle.  At the end
of `A_r`, exhaustive maximization over every proper root gives proper
cyclic curling number exactly `2` and unique maximizing root length `r`.
The root-copy equation and self-label equation are both exact there.
The cycle is monochromatic, its spans sum to `|Q_L|`, and every
finite-prefix containment inequality outside the fixed seed window
`N=8` holds.

Thus the cycle length is unbounded even with fixed `N=8`, binary word
alphabet `{2,3}`, and winding one.  The construction fails the global
fixed-profile equation at off-cycle cuts.  Consequently the
seed-anchored cycle route is blocked as a standalone compression
argument: any surviving proof must use the off-cycle equations
`pc_Q(d)=Q[d]` or another global compatibility condition.  The executed
checker is `check_unbounded_parent_cycles.py`.
