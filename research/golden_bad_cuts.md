# Golden bad cuts and canonical period episodes

This note records reductions for a hypothetical counterorbit.  It does not
prove termination.

Put

`alpha = phi^2 = (3+sqrt(5))/2`.

For a nonempty finite word `W`, let `E(W)` be the maximum of
`|Z|/per(Z)` over all nonempty suffixes `Z` of `W`.

## Curling number is the integer part of the suffix exponent

For every nonempty `W`,

`c(W) = floor(E(W))`.

If `W` ends in `Y^k`, that suffix has exponent at least `k`, so
`floor(E(W)) >= c(W)`.  Conversely, let a suffix `Z` have length `L` and
least period `p`.  Its last `floor(L/p)*p` symbols are consecutive copies of
one length-`p` block.  Hence `c(W) >= floor(L/p)`.  Taking a suffix attaining
`E(W)` gives the reverse inequality.

Call an orbit state *golden-bad* when `E(W)<alpha`.

## Golden-bad cuts occur infinitely often in every counterorbit

The appended alphabet of a counterorbit is finite by the new-symbol lemma
in `reductions.md`.  Its infinite orbit word cannot be ultimately periodic:
an ultimately periodic tail supplies suffix powers with arbitrarily large
integer exponent, contrary to the finite bound on appended values.

Mignosi, Restivo, and Salemi, “Periodicity and the golden ratio,”
*Theoretical Computer Science* 204 (1998), 153--167,
DOI 10.1016/S0304-3975(98)00037-1, prove that a right-infinite word is
ultimately periodic if and only if every sufficiently long prefix has a
suffix of exponent at least `alpha`.  Their theorem therefore gives
infinitely many golden-bad orbit states.  At each one

`c(W)=floor(E(W))=2`,

because a counterorbit has curling number at least two.

## The three-step small-cube theorem

Let `S_n` be golden-bad in a counterorbit, and write `c_i=c(S_i)`.  There is
a least `d` in `{1,2,3}` such that

`c_n=...=c_(n+d-1)=2` and `c_(n+d)=3`.

Indeed, as long as the value remains two, the orbit appends a `2`.  After
three such appends the current state ends in `222`, so its curling number is
at least three.  At the first non-two value, the one-step rise bound
`c_(i+1)<=c_i+1` makes the value exactly three.

Let `Y^3` be any cube suffix of `S_(n+d)` and put `p=|Y|`.  Then

`p < d*alpha`.

If `p>=d*alpha`, deleting the `d` appended twos leaves a suffix of `S_n`
with period `p`, length `3p-d`, and exponent at least `3-d/p`.  The identity

`3-alpha = 1/alpha`

makes `3-d/p >= alpha`, contradicting the golden-bad hypothesis.  Therefore
the exact integer bounds are

| `d` | possible upper bound on `p` |
|---:|---:|
| 1 | 2 |
| 2 | 5 |
| 3 | 7 |

Every such `Y` is primitive, since a proper-power root would make the state
end in at least six copies of a shorter word although its curling number is
three.  If `p<=d`, the last complete copy of `Y` lies in the appended run of
twos; hence `Y=2^p`, and primitivity gives `p=1`.  Thus either

`p=1, Y=2`,

or

`p>d, Y=A 2^d`

with `A` nonempty.  In the latter case the preceding golden-bad state ends
in the kernel

`K=(A 2^d)^2 A`,

obtained by deleting the final `2^d` from `Y^3`.  Its length is
`3p-d<=18`.

Consequently, for any fixed finite tail alphabet, there are only finitely
many triples `(d,Y,K)`, and every hypothetical counterorbit has infinitely
many occurrences of these bounded kernels.  This conclusion does not
assume that the tail alphabet is `{2,3}`.

## Exact bad-to-good exits

Suppose `E(P)<alpha` and `E(Pa)>=alpha`.  Let a suffix of `Pa` witnessing
the latter inequality have least period `q` and length `L`.  Removing the
last letter preserves period `q`, while the resulting suffix of `P` has
exponent below `alpha`.  Hence

`L = ceil(alpha*q)`.

In an orbit, a golden-bad `P` appends `a=2`.  Periodicity of the new suffix
gives a same-symbol copy edge from this new `2` to the position `q` places
earlier.  Before the append, `P` already has a latent `q`-periodic suffix of
length

`floor(alpha*q)`.

This latent suffix contains a square of root length `q`, but it can have
arbitrarily large `q`; the bounded kernel does not bound this background
period.

## Fractional masking lemma

Let `U` be a suffix of `W`.  If

`E(U)<alpha<=E(W)`,

then a witnessing suffix of `W` crosses the left boundary of `U`.  If its
least period is `q`, then

`q > |U|/alpha`.

For if `q<=|U|/alpha`, the final `ceil(alpha*q)` letters of the witness lie
inside `U`, inherit period `q`, and have exponent at least `alpha`.  This
contradicts `E(U)<alpha`.

Thus a local suffix evolution can have curling number two and look
golden-bad while the full state is golden-good because of a long fractional
power crossing the retained context.

## Exact PUSH/POP dichotomy at a period break

Suppose a prefix `P` has a suffix of length `ell>=ceil(alpha*q)` and least
period `q`.  Append a letter `a` that breaks this period:

`a != P[-q]`.

Assume `Pa` is still golden-good, and choose a suffix of `Pa` of length
`m>=ceil(alpha*r)` and least period `r`.  Put `g=gcd(q,r)`.

The old suffix and the new suffix with its final letter deleted overlap at
the end of `P` in

`O=min(ell,m-1)`

symbols.  This overlap has periods `q` and `r`.  If

`O>=q+r-g`,

Fine--Wilf gives period `g`.  The overlap contains a complete terminal
length-`q` block of the old suffix and a complete length-`r` factor of the
new suffix.  The latter is a conjugate of its primitive period block.  Both
blocks are primitive because `q` and `r` are least periods.  A period `g`
dividing their lengths therefore forces `q=r=g`.  The new `r`-periodicity
would then give `a=P[-q]`, contrary to the break.

It follows that `O<q+r-g`.  Since

`O >= min(ceil(alpha*q), floor(alpha*r))`,

at least one of the following two strict alternatives holds:

`r > ceil(phi*q)+g`  (PUSH),

`q > floor(phi*r)+g`  (POP).

In particular, every active-period handoff changes scale by a factor
strictly greater than `phi`.  The inequalities are exhaustive, but they are
not oriented: a word can make arbitrarily many pushes and pops unless the
exact orbit labels or a nesting mechanism supplies an additional
restriction.

## Coexisting periods and exact record origins

Suppose one prefix ending at position `v` has golden suffixes with distinct
least periods `q>r`, and put `g=gcd(q,r)`.  Their common terminal overlap has
length at least `ceil(alpha*r)`.  If this reached `q+r-g`, Fine--Wilf and
the primitive-block argument from the preceding section would force `q=r`.
Therefore

`q > ceil(phi*r)+g > phi*r`.

This separation has an exact origin consequence.  The inequalities above
give

`q + ceil(alpha*r) < ceil(alpha*q)`.

To verify it, use

`q >= ceil(phi*r)+g+1 > phi*r+g+1`,

multiply by `phi`, and use `alpha=phi^2`.  Thus the terminal minimal
`r`-witness and its translate `q` positions earlier both lie inside the
terminal minimal `q`-witness.  The `q`-periodicity makes them equal.  Hence
the prefix ending at `u=v-q` already has the same golden `r`-witness.

Let

`L_q = v-ceil(alpha*q)+1`,

`L_r = (v-q)-ceil(alpha*r)+1`

be the left endpoints of the outer witness and the copied parent witness.
The strict length inequality gives

`L_q < L_r`.

Consequently, along a lineage in which successively larger golden periods
enclose copies of earlier golden records, witness left endpoints strictly
decrease.  Such a lineage cannot remain wholly to the right of the finite
seed forever.  This is an exact descent for simultaneous golden witnesses;
what is still missing is a proof that every unbounded orbit scale belongs
to one fixed lineage rather than relocating among different copied
records.

## Entry lemma: unbounded maximizing roots force unbounded golden periods

Let `K` be the finite upper bound on all labels of a hypothetical
counterorbit.  Suppose a label-`2` state ending at orbit-word position `v`
has a primitive maximizing root of length `q`, so its terminal `2q` symbols
are `Q^2`.  Put `u=v-q`.  For `q` larger than the seed length, both `u` and
`v` are appended positions: the first copy of `Q` ends at `u`, so
`q<=u+1`.

Compare the subsequent label streams after the prefixes ending at `u` and
`v`.  They cannot agree forever, since that would make the orbit word
ultimately `q`-periodic.  Let `h>=0` be their first mismatch offset.  The
target square has then extended to a `q`-periodic suffix of length

`2q+h`,

and the two prefixes immediately before the mismatch share an identical
terminal `q`-periodic word of length

`H=q+h`.

Put

`b=ceil((alpha-2)q)=ceil(q/phi)`.

If `h>=b`, the target prefix reached after `b` matching labels already has
a suffix of period `q` and length at least `alpha*q`.  Thus `q` is a golden
period.

If `h<b`, let `k` be the larger of the two different labels at the first
mismatch, and let `r` be a primitive maximizing-root length on that side.
Then `3<=k<=K`.  Its terminal `k`-power cannot fit inside the common
length-`H` suffix, because the other prefix would then also have curling
number at least `k`.  Therefore

`k*r>H=q+h`,

and hence

`r>(q+h)/k>=q/K`.

This `r` is itself a golden least period, because `k>=3>alpha`.

Lemma 4 of `reductions.md` gives unbounded least maximizing-root lengths.
If an unbounded subsequence occurs at labels at least three, those roots
are already unbounded golden periods.  Otherwise take an unbounded
subsequence of label-`2` roots and apply the dichotomy above.  Either
unboundedly many of them survive to exponent `alpha`, or their first
divergences produce golden roots `r>q/K`.  In both cases the set of golden
least periods, and consequently the set of global golden-period records, is
unbounded.

Geometrically, an early-death cube crosses the whole common shadow.  On the
source-high side its left endpoint lies strictly before the left endpoint
of the original square; on the target-high side it lies strictly before
the square midpoint.  No separate seed-crossing ancestry argument is
needed for entry: bounded label size converts every dying large square into
a comparably large cube.

## First shadow divergence of a new golden record

Let `q` be larger than every golden least period at earlier orbit-word
positions, and let it first occur as a golden suffix at position `v`.  Put

`L=ceil(alpha*q)` and `u=v-q`.

The terminal length-`L` word at `v` has period `q`.  Compare the two streams
of subsequent orbit labels generated after the prefixes ending at `u` and
`v`.  They cannot agree forever, since that would make the orbit word
ultimately `q`-periodic.  Let `h>=0` be the first offset at which they
differ.  Immediately before that mismatch, the prefixes ending at

`U=u+h` and `V=v+h`

have an identical terminal word `C` of length

`H=L-q+h=ceil(phi*q)+h`

and `C` has period `q`.  Let the two different next labels be `a` and `b`,
put `k=max(a,b)>=3`, and let `r` be the primitive root length of a
maximising `k`-power suffix on the side whose label is `k`.

The `k`-power cannot fit inside `C`, because then the other side would have
curling number at least `k`.  Therefore

`k*r>H`.

If `H>=q+r-gcd(q,r)`, Fine--Wilf applied to the overlap of `C` with the
terminal `r`-power makes a complete primitive length-`q` block and a
complete primitive length-`r` block share period `gcd(q,r)`.  This forces
`q=r`.  Hence

`r=q`, or `r>H-q+gcd(q,r)>=ceil(q/phi)+h+gcd(q,r)>q/phi`.

This yields the following exhaustive trichotomy.

1. If `r=q`, the high side must be the target `V`.  For `h<q`, a high
   source would put a golden `q`-suffix before its first occurrence at `v`.
   For `h>=q`, the matched shadow copies the complete last `q`-block after
   `U`; a source suffix `q^k` would therefore make the target end in
   `q^(k+1)`, contradicting the choice of the source label `k` as the larger
   label.  Truncating the target `q^k` suffix by its last block gives a
   `q^(k-1)` suffix at `U`.  Hence the source label is exactly `k-1`, and
   the two powers have the same origin:

   `V-k*q+1 = U-(k-1)*q+1`.

   Thus this case is a fixed-origin one-copy maturation, not a relocation.
2. If `r<q`, the high-label side is the source side `U`, and `h<q`.  If it
   were the target side, periods `q` and `r` would coexist at `V`; if
   `h>=q`, they would coexist at `U`.  In either event the coexistence
   inequality would give `q>phi*r`, contrary to `r>q/phi`.  Thus this
   `r`-power occurs before the first golden occurrence of `q`.  The
   preceding global golden-period record `P` consequently satisfies
   `P>=r>q/phi`, or equivalently `q<phi*P`.
3. If `r>q`, either the high side is the target, or it is the source with
   `h>=q`; otherwise `r` would have occurred before the first occurrence of
   the record `q`.  At the high endpoint both `q` and `r` are golden
   periods.  The coexistence inequality gives
   `r>ceil(phi*q)+gcd(q,r)>phi*q`, so this is a genuine larger record.

Every nonself branch also moves the powered-run origin strictly left.  On
the source-high side this is immediate from `k*r>H`, because the common
shadow starts at the parent origin.  On a target-high push, the target
`q`-suffix has length `L+h`, and its label `k` implies

`L+h < (k+1)q`;

otherwise `q` itself would witness curling number at least `k+1`.  Since
`r>phi*q` and `k>=3`,

`k*r > k*phi*q > (k+1)q > L+h`.

The terminal `r^k` therefore begins strictly before the fixed origin of the
extending `q`-run.  In the middle case, the source `r^k` already crosses
that origin.  Self-maturation is the unique first-divergence branch that
does not create a farther-left powered run.

The middle case has an additional exact subtraction structure.  Write
`s=q-r`.  The common word `C` has periods `q` and `r`; its suffix obtained
by deleting its first `r` symbols has period `s`.  Indeed, for every
`i<H-q`,

`C[i+r]=C[i]=C[i+q]`,

so the shifted suffix has period `q-r`.  Moreover,

`H-r >= phi*q-r > alpha*(q-r)`,

where the strict inequality is equivalent to `phi*r>q`.  Thus this shifted
suffix is itself golden, with some least period at most `s`.  If `A` is the
fixed left endpoint of the extending `q`-periodic shadow, this earlier
golden parent starts at `A+r`, while the child `q`-witness starts at `A`.
The child has moved its left endpoint exactly `r` positions to the left of
that parent occurrence.

In every branch the first divergence therefore produces an actual cube
root `r>q/phi`.  Together with the entry lemma, this shows that every
hypothetical counterorbit has both unbounded golden-period records and
unbounded cube-root records.

## Every large cube-root record has label three

The scale-selection argument can be made directly in the counterorbit,
without first passing to a circular fixed profile.  Let a primitive
maximizing root `Y`, of length `r`, set a new global cube-root record at a
state whose label is `e>=3`; write its displayed suffix as `Y^e`, beginning
at position `A`.  Take the record sufficiently large that all positions
used below are beyond the finite seed.

Then necessarily

`e=3`.

Assume `e>=4`.  For every phase `0<=t<r`, the occurrence of `Y[t]` in the
last copy is preceded by `e-1` complete rotated copies.  Since that
occurrence is an appended position, its value is its preceding state's
curling number, so

`Y[t]>=e-1>=3`.

The root `Y` is primitive.  The proper-cube corollary of Saari's local
period theorem, proved in the circular-profile section below, therefore
gives a phase `t` at which the bi-infinite periodic word `Y^Z` has no cube
ending there with root shorter than `r`.

Now inspect the appended cut at position `A+2r+t`, through the third copy
of `Y`.  Its label is `Y[t]>=3`; let `p` be a primitive maximizing-root
length there.  Its power cannot start at or after `A`: a root `p<r` would
be the forbidden proper cube at phase `t`, `p=r` would require three
complete copies although only `2r+t<3r` symbols are available, and `p>r`
would require still more space.  Thus the `p`-power starts before `A`.

The overlap from `A` to this earlier endpoint has length `2r+t` and
periods `p` and `r`.  With `g=gcd(p,r)`, Fine--Wilf would contradict the
primitivity of `Y` or of the `p`-root if

`2r+t>=p+r-g`.

Consequently

`p>r+t+g>r`.

This longer cube root occurs strictly before the alleged record endpoint,
a contradiction.  Hence every sufficiently large new cube-root record
has curling number exactly three.  Since the entry lemma supplies
unbounded cube-root records, every hypothetical counterorbit has
unbounded label-three record roots even if its finite tail alphabet
contains larger values.

## Residual fixed-origin tower

The origin descent above leaves one exact obstruction.  Suppose infinitely
many record episodes use the self branch, and after passing to a
subsequence their power origin and maturation exponent are fixed.  Translate
the common origin to zero.  There are primitive words `Q_i`, with
`q_i=|Q_i|`, such that

`Q_i^k k`

is a prefix of the orbit tail for a fixed `3<=k<=K`.  The symbols at the
starts of the first `k` copies are `k-1`, and the symbol after the last copy
is `k`.  Thus, at generated positions, the prefixes immediately before
those starts have curling number `k-1`, while the prefix immediately before
the delimiter has curling number `k`.

Two distinct levels satisfy a sharp Fine--Wilf separation.  If `p<q` are
two root lengths in the tower and `g=gcd(p,q)`, then

`q>(k-1)p+g`.

If the reverse weak inequality held, the common prefix of length `kp`
would meet the Fine--Wilf threshold `p+q-g`.  It has periods `p` and `q`;
period `g` would make the complete primitive `q`-block imprimitive.  The
case `q>=kp` is automatic except for `q=kp`; in that equality case the
length-`q` root is `Q_p^k` and is directly nonprimitive.  In particular,
successive tower scales grow by a factor greater than `k-1`.

There are two exact transition forms.

* If `q<kp+1`, put `s=kp-q`.  The two occurrences of the prefix
  `Q_p^k k`, one at each adjacent `q`-block start, overlap in `s+1`
  symbols.  Consequently `1<=s<p`,

  `Q_p[0:s]=Q_p[p-s:p]` and `Q_p[s]=k`.

  Thus a close next scale is encoded by a border of the old primitive
  root.  The equality `q=kp` is excluded because it would identify the
  old delimiter `k` with the new block-start symbol `k-1`.
* If `q>=kp+1`, the whole earlier word `Q_p^k k` is a prefix of the new
  root `Q_q`.  It is copied at the same offset in all `k` copies of
  `Q_q`.

More generally, whenever `kp+1<=q`, the positions

`m*q+kp`, for `0<=m<k`,

all carry the symbol `k`, and the positions `m*q`, for `0<=m<k`, carry
`k-1`.  In an actual orbit these are exact curling-number constraints, not
merely letter equalities: immediately before every first family position
the state ends in `Q_p^k` and has curling number exactly `k`; immediately
before every second family position its curling number is exactly `k-1`.
Any equality between a position in the two families is therefore
impossible.

The copied endpoints do not create a hidden `(k+1)`-power.  Split
`Q_q` at offset `d=kp` and put

`R=Q_q[d:q] Q_q[0:d]`.

Starting at the copied old delimiter, the word contains `R^(k-1)` followed
by `Q_q[d:q]`.  Continuing one more rotated copy would require the next
symbol `Q_q[0]=k-1`, whereas the actual large delimiter is `k`.  Thus every
copied old maturation is synchronized with the same final one-symbol break.

The full internal orbit condition nevertheless gives one global
restriction that word combinatorics alone misses.  Fix a level `Q^k`, with
`|Q|=q`, and an offset `0<=d<q`.  The length-`(k-1)q` factor beginning at
offset `d` is

`(Q[d:q] Q[0:d])^(k-1)`.

It ends immediately before the occurrence of `Q[d]` in the last copy.
That occurrence is an appended orbit label, so

`Q[d]>=k-1`.

As the fixed-origin roots are nested and unbounded, every sufficiently late
tail symbol belongs to some `Q_i`.  Hence the entire tower tail uses only
labels at least `k-1`.  Lemma 5 of `reductions.md` supplies infinitely many
labels equal to two in every counterorbit.  Therefore an infinite
fixed-origin self-maturation tower must have

`k=3`.

Thus all exponent-four-or-higher fixed-origin towers are excluded.  The
irreducible tower is a cube tower: every cyclic rotation of every root has
a square occurrence, which only recovers the already-known lower bound two
on its following label.

For this cube tower there is an exact small-root/pre-origin dichotomy at
every non-`2` internal offset.  Let `Q` be a primitive record root of length
`q`, let `0<=d<q`, and suppose `Q[d]=a>=3`.  Immediately before the
occurrence of this symbol in the third copy, the prefix has curling number
`a`; let `r` be a primitive maximizing-root length there.  The interval
from the fixed origin through that endpoint has period `q` and length
`2q+d`.

If the `r^a` suffix starts at or after the fixed origin and `r>=q/2`, it has
periods `r` and `q`, and

`a*r>=3r>=q+r-gcd(q,r)`.

Fine--Wilf plus primitivity forces `r=q`.  But then `a*r>=3q>2q+d`, so the
power could not have started at or after the origin.  Consequently,

`r<q/2`,

or the `r^a` suffix crosses the fixed origin.  In the crossing case

`r>(2q+d)/a>=2q/K`,

so it is a comparable-scale cube reaching strictly farther left.

The small-root alternative can occur at linearly many offsets; raw
coverage cannot exclude it.  Four consecutive appended `2` labels are
impossible, because after three appended twos the state already ends in a
cube.  Hence every long root contains linearly many symbols at least three.
Nevertheless, for every `m>=1` the primitive word

`Q_m=(2223)^(m+4) 4`

has no run of more than three twos, every displayed `3` is immediately
preceded by the cube `222`, and its unique `4` is immediately preceded by
the fourth power `(2223)^4`.  The unique `4` also proves `Q_m` primitive.
Thus a linear density of independently witnessed small cubes, bounded gaps,
and primitivity do not force a comparable period.  These words do not
satisfy all exact curling-number equalities; they isolate why any successful
counting argument must use maximality at every internal offset.

## Removing a finite context from a fixed-origin tower

There is an exact earliest-mismatch argument that reduces a tower whose
origin lies inside a finite seed to a tower at the start of an autonomous
counterorbit.

Call `A` a *power-tower origin* if, for some fixed `e in {2,...,K}`, there
are unbounded primitive root lengths `p_i` such that

`W[A:A+e*p_i]=R_i^e` and `W[A+e*p_i]=e`.

The delimiter position is required to be appended, so its symbol is the
actual curling number of the preceding prefix.  A fixed-origin cube tower
supplies at least one such `A`.  Choose the least power-tower origin `B`.

The rotation argument from the preceding section applies to any such
fixed-exponent tower: every symbol in its unbounded nested roots is at least
`e-1`.  Infinitely many labels equal two therefore imply only

`e in {2,3}`.

Both cases must be retained.  Compare two evolutions:

* the global state ending with the first `R_i`, whose following output is
  the continuation of `W`;
* the local seed `R_i` with the finite context `W[0:B]` removed.

As long as their next labels agree, the local state is a suffix of the
global state.  If their first mismatch is after `t>=0` matching labels,
suffix monotonicity makes the global label `k` strictly larger than the
local label.  If the local orbit has reached curling number one, this is
already such a mismatch because the global label is at least two.  A
primitive maximizing `k`-root of the global state cannot fit in its
terminal local suffix of length `p_i+t`; otherwise the local
curling number would also be at least `k`.  Hence

`k*s_i>p_i+t`,

where `s_i` is that maximizing-root length.  Its complete primitive power
starts at some position `A_i<B` and is immediately followed by the
appended symbol `k`; primitivity is Lemma 2 of `reductions.md`.  Since
`2<=k<=K`, infinitely many
mismatching levels have a subsequence with fixed `k` and fixed
`A_i=A<B`, while `s_i>p_i/K` is unbounded.  The exact fixed left endpoint,
fixed exponent, primitive roots, and following labels make `A` a
power-tower origin earlier than the minimal `B`, a contradiction.

It follows that only finitely many levels can ever mismatch.  For every
remaining `R_i`, the orbit starting from the finite seed `R_i` agrees
forever with the global continuation.  In particular,

* if `e=2`, it appends one further copy of `R_i` and then `2`;
* if `e=3`, it appends two further copies of `R_i` and then `3`.

In the cube case this is

`R_i -> R_i^2 -> R_i^3 -> R_i^3 3`.

At the last step the local curling number is at least three because of the
displayed cube and at most the global curling number three by suffix
monotonicity.

Thus a finite context can be removed completely at the least power-tower
origin.  The normalized counterorbit word `T` has one of two irreducible
forms:

1. unbounded primitive prefix cubes `R_i^3 3`, with every large `R_i` a
   genuine cube self-replicator seed;
2. unbounded primitive prefix squares `R_i^2 2`, with every large `R_i` a
   genuine square self-replicator seed.

Any context-sensitive failure at even one offset for infinitely many
levels would create a strictly earlier unbounded power tower.  The second
case cannot be discarded by the rotation argument: for exponent two that
argument supplies only the vacuous lower bound one.  An early target-high
death of an anchored square can create a comparable cube whose origin lies
strictly between the square origin and its midpoint, so the current entry
lemma does not move that cube tower farther left.

### Exact replay dichotomy for the normalized square tower

Let `P` be one primitive root in the autonomous square case, with
`p=|P|`.  Since the orbit from `P` appends another `P`, its first appended
label is `P[0]=cn(P)`.  But `P` is a suffix of `P^2` and
`cn(P^2)=2`, so suffix monotonicity gives

`P[0]=cn(P)=2`.

The delimiter after `P^2` is therefore the symbol that would start a third
copy.  Compare the source evolution after `P` with the target evolution
after `P^2`.  Their first labels agree.  Let `h>=1` be their first
divergence; it occurs no later than `h=p`, because at that offset the source
has reached `P^2`, while the target has reached `P^3`.

For `h<p`, the common terminal word has length `p+h`.  Suffix monotonicity
makes the target label `k` strictly larger than the source label, so
`k>=3`.  If `r` is a primitive maximizing-root length at the target, then

`k*r>p+h`.

Thus the `r^k` suffix crosses the midpoint between the two displayed copies
of `P`.  Its left endpoint, relative to the square-tower origin, is

`C=2p+h-k*r`, with `0<=C<p`.

The target word `P^2 P[0:h]` has period `p`.  If `r>=p/2`, Fine--Wilf on
the `r^k` factor, using `k>=3`, forces `r=p`; that is impossible because
`k*p>2p+h`.  More exactly, with `g=gcd(p,r)`, Fine--Wilf must fail, so

`(p+h)/k < r < (p-g)/(k-1) <= p/2`.

Writing `s=p-(k-1)r` gives

`g<s<r-h`.

If `Y` is the primitive length-`r` root, the length-`p` factor beginning at
`C` is a conjugate of `P`, and the power equation gives the exact form

`conj(P)=Y^(k-1) Y[0:s]`.

In fact the target-high label in this early branch is forced to be

`k=3`,

and the source label is exactly two.  The terminal `Y^k` starts at `C` and
ends at the first mismatch.  For every `0<=t<r`, consider the occurrence
of `Y[t]` in its final copy, at position

`C+(k-1)r+t`.

This is a generated position rather than part of the seed: using
`p=(k-1)r+s` and `C=2p+h-kr` gives

`C+(k-1)r-p=(k-2)r+s+h>0`.

Immediately before that symbol, the state has a suffix of period `r` and
length at least `(k-1)r`, so the symbol appended there, which is `Y[t]`,
is at least `k-1`.  Hence every symbol of `Y`, and therefore every symbol
of its conjugate

`P=conj(Y^(k-1)Y[0:s])`,

is at least `k-1`.  But `P[0]=2`, proved above, so `k-1<=2`.  Since the
target is strictly higher than a counterorbit label at least two, `k=3`
and the source label is two.  Thus the exact early-death data reduce to

`p=2r+s`, `gcd(p,r)<s<r-h`,

`C=r+2s+h`,

with a one-step mismatch `2 -> 3`.

The early-death branch is therefore a comparable but strictly smaller
power, rooted at a relocated interior origin.  For any larger prefix root
that contains this event, the whole equation is copied at the same offset
in every outer copy; this transports the fixed event but does not make its
root length grow.

If no divergence occurs before `h=p`, the target is `P^3` and the source
is `P^2`.  Let the target label be `k` and its primitive maximizing-root
length be `r`.  The maximizing power cannot fit in the common suffix
`P^2`, so `k*r>2p`.  It lies in the length-`3p`, period-`p` word `P^3`,
and `r<=3p/k<=p`.  Hence

`k*r>2p>=p+r-gcd(p,r)`.

Fine--Wilf and primitivity force `r=p`; fitting the power in `P^3` then
forces `k=3`.  Thus full replay gives the fixed-origin maturation

`P^2 -> P^3 -> P^3 3`

exactly.  The sole square-tower obstruction is infinite early target-high
death with the displayed conjugate near-power equations.

Those equations alone admit arbitrarily large primitive word
countermodels.  For any odd `r>=5`, put

`Y=(32)^((r-1)/2) 3`, `s=h=2`, `p=2r+2`,

let `Z=Y^2 Y[0:2]`, and let `P` be the rotation of `Z` by `r-4`
positions.  The word `Y` has period two but is primitive: the numbers of
`2` and `3` symbols are consecutive integers, so no proper-power exponent
can divide both.  The same count argument makes `Z`, and hence `P`,
primitive.  Direct index substitution gives

`P[0]=P[2]=2`,

and the word `P^2 P[0:2]` ends in `Y^3`; its cube starts at offset `r+6`.
Thus it realizes the full `k=3`, `s=h=2` overlap equation with the desired
one-symbol mismatch `2 -> 3` at arbitrarily large scale.

For the smallest member, `r=5`,

`P=232332323323`, `Y=32323`.

Both implementations in `curling.py` give

`cn(P)=2`, `cn(P^2)=2`, `cn(P^2 P[0:2])=3`.

It is not a self-replicator: after appending the first required `2`,
`cn(P P[0:1])=2` while the next word symbol is `P[1]=3`.  This family
therefore falsifies any attempted proof based only on the endpoint curling
numbers and the Fine--Wilf overlap equation.  The equality at every
internal replay offset is indispensable.

## Circular fixed-point profile of a cube self-replicator

Let `Q` be a normalized cube self-replicator of length `q`.  For
`0<=d<q`, put

`A_d=Q Q[0:d]`, `B_d=Q^2 Q[0:d]`, `a_d=Q[d]`.

Full internal replay says

`cn(A_d)=cn(B_d)=a_d`.

Let `r_d` be the least maximizing-root length in either word.  This length
is the same for `A_d` and `B_d`.  Indeed, `A_d` is a suffix of `B_d`, so
its least root is available in `B_d`.  Conversely, a shorter maximizing
root in `B_d` would have powered length at most the powered length of the
root from `A_d`, hence at most `|A_d|`; it would fit completely inside
`A_d` and contradict minimality there.  The root words are then identical
because both are the terminal word of the same length.

Consequently

`1<=r_d<q`.

The outer length-`q` square in `B_d` is a dormant noncanonical maximizing
root exactly when `a_d=2`; it does not replace the repeated shorter
canonical profile.  At `Q^3` the outer root promotes to exponent three and
causes the final break.

There is a useful exact extension of this observation.  Define the
*proper circular curling profile* of a primitive word `Q` at phase `d` to
be the largest integer exponent of a suffix ending at that phase in the
bi-infinite periodic word `Q^Z`, where the root length is required to be
strictly less than `q`.  Every such powered suffix with root length `p<q`
has length

`L < p+q-gcd(p,q) < 2q`.

Indeed, at or above the first bound Fine--Wilf would give period
`gcd(p,q)` to a complete length-`q` conjugate of `Q`, making `Q`
imprimitive.  It follows that `B_d`, which has at least `2q` symbols of
left context, detects the whole proper circular profile.  Therefore a cube
self-replicator satisfies the intrinsic circular fixed-point equation

`proper_cn_Q(d)=Q[d]`

at every phase.  The shorter source `A_d` additionally certifies that a
maximizing proper root already fits in its available `q+d` symbols.

More generally, for every `j>=2` and `0<=d<q`,

`cn(Q^j Q[0:d]) = max(j,Q[d])`.

To prove this, roots shorter than `q` are completely detected in the last
`2q` symbols and have maximum exponent `Q[d]`.  The length-`q` circular
rotation is repeated exactly `j` times at the suffix.  A primitive
maximizing root `p>q` is impossible: its square has length at least `2p`,
and Fine--Wilf with the ambient period `q` gives the smaller period
`gcd(p,q)<p` to the complete root, contradicting primitivity.  These three
root-length ranges are exhaustive.

Thus, if `m=min_d Q[d]`, the orbit continues copying `Q` while the outer
copy count is at most `m`.  At copy count `m+1`, the first phase carrying
the minimum symbol is forced upward from `m` to `m+1`.  In the normalized
cube tower `Q[0]=2`, so the first such promotion is the exact boundary

`Q^3 -> Q^3 3`.

This identity also shows why inspecting only three block-boundary values
loses information: the entire proper circular fixed-point equation is what
controls all phases before the outer promotion.

If `r_d` is a maximizing proper root for phase `d`, Fine--Wilf gives the
additional sharp inequality

`(Q[d]-1)r_d < q-gcd(q,r_d)`.

Also, if `Q[d]=a>=3` and the terminal root word is `Y` of length `r_d`,
then every symbol of `Y` is at least `a-1`.  For `0<=t<r_d`, the cut
through the last copy just before `Y[t]` has a suffix consisting of
`a-1` copies of the corresponding rotation of `Y`; the fixed-point
equation at that cut therefore gives `Y[t]>=a-1`.  In particular, a
maximum-label `M`-power in a profile with alphabet maximum `M` has a root
over the two symbols `{M-1,M}`.

The circular fixed profile necessarily has minimum symbol two.  A useful
external local-period theorem makes this exact.  K. Saari, “Everywhere
alpha-repetitive sequences and Sturmian words,” *European Journal of
Combinatorics* 31 (2010), 177--192, Theorem 5.3, proves that every
everywhere `phi^2`-repetitive right-infinite word is ultimately periodic;
“everywhere” includes the hypothesis that only finitely many distinct
minimal `phi^2`-repetitions occur.  Its proof chooses a longest minimal
repetition, writes `N` for its least period, and proves that the infinite
word is eventually `N`-periodic.

If every symbol of a primitive circular fixed profile `Q` were at least
three, reverse the bi-infinite periodic word `Q^Z`.  At every position a
cube begins whose root is strictly shorter than `q`.  The word is periodic,
so it has only finitely many distinct minimal `phi^2`-repetitions and
Saari's theorem applies.  The least period `N` of the selected longest
minimal repetition is strictly below `q`, because a proper cube is
available at its starting position.  The proof of the theorem makes the
right-infinite word eventually `N`-periodic.  Since it is also purely
`q`-periodic, shifting any index far enough by multiples of `q` shows that
`N` is a period everywhere.  This contradicts the primitivity of `Q`.
Therefore

`min_d Q[d]=2`.

This conclusion uses proper roots essentially; the outer period `q` itself
would otherwise make the local-period theorem tautological.

There is also an exact scale-selection consequence.  Among all primitive
maximizing roots at phases whose labels are at least three, choose one of
maximum length `r`; let its label be `e` and its root word be `Y`.  Then

`e=3`.

Assume instead `e>=4`.  The root-symbol observation above makes every
symbol of `Y` at least `e-1>=3`.  Since `Y` is primitive, the preceding
proper-cube corollary, applied to `Y`, supplies a phase `t` at which
`Y^Z` has no cube ending there with root shorter than `r`.

Place the displayed `Y^e` at coordinates `[0,e*r)`.  At the cut
`2r+t`, through the third copy, the circular fixed profile has label
`a=Y[t]>=3`; let `p` be a primitive maximizing-root length there.  Its
`a`-power cannot start at or after zero.  If it did, a root `p<r` would
be the forbidden proper cube at phase `t`, the root `p=r` would require
three full copies although only `2r+t<3r` symbols are available, and a
root `p>r` would require still more space.  Thus this `p`-power crosses
zero.

Its overlap with `Y^e` has length `2r+t` and periods `p` and `r`.  Put
`g=gcd(p,r)`.  If

`2r+t >= p+r-g`,

Fine--Wilf makes a complete primitive `r`-block or a complete primitive
`p`-block have the smaller period `g`; the divisibility edge cases give
the same contradiction to one of the two primitive roots.  Hence

`p>r+t+g>r`,

contradicting the maximal choice of `r`.  Therefore exponent-three roots
carry every largest proper cube scale.

For a fixed alphabet bound `K`, unbounded primitive circular fixed-profile
lengths force these exponent-three root lengths to be unbounded.  First,
an unbounded label-two root also forces a comparable root at a label at
least three.  Compare the two phase streams at the ends of its final two
copies.  They cannot agree through a whole root period, unless the square
extends to a proper cube of the same root.  At an earlier mismatch after
`h<r` matching symbols, the higher label `k>=3` has a maximizing root `s`
whose complete `k`-power cannot fit in the common suffix of length `r+h`.
Thus `k*s>r+h` and `s>r/K`.

If every maximizing proper root at every label had length at most `R`, the
next profile symbol would be determined by the last `K*R` symbols: that
window contains a maximizing power, and checking roots at most `R`
recovers its exact exponent.  The resulting deterministic finite-state
rule has at most `K^(K*R)` states, so a primitive periodic profile has
bounded length.  Hence an unbounded family first has unbounded proper
roots, then unbounded roots at labels at least three by the comparison
above, and finally unbounded label-three roots by the maximum-scale
selection paragraph.

The first root after the outer promotion has an exact scale bound.  Suppose
`Q[0]=2`, put `V=Q^3 3`, let `k=cn(V)>=2`, and let `s` be any primitive
maximizing-root length in `V`.  With `g=gcd(q,s)`,

`(k-1)s <= q-g`,

so in particular `s<q`.  Delete the final promoted `3` from the terminal
`k`-power.  The remaining length-`ks-1` word lies in `Q^3` and has periods
`s` and `q`.  If `ks-1>=s+q-g`, Fine--Wilf gives period `g` to a complete
length-`q` conjugate of `Q`.  For `g<q` this contradicts primitivity.  For
`g=q`, the equality `q|s` says that the copied symbol paired with the final
`3` is `Q[0]=2`, also a contradiction.  Hence the Fine--Wilf threshold
must fail, which is the displayed integer inequality.  Lemma 3 of
`reductions.md` additionally gives `k<=4`, because the preceding label at
`Q^3` is three.  Thus a nonterminating continuation after a promoted outer
cube must immediately reset its canonical period from `q` to a proper
period; for `k>=3` it resets below `q/2`.

There is a finite circular parent map

`f(d)=d-r_d (mod q)`.

The last two root copies show that it preserves the symbol immediately
before the cut:

`Q[d-1]=Q[f(d)-1]`.

More strongly, it equates the two adjacent circular length-`r_d` blocks
ending at the cut.  Every directed cycle of `f` is therefore monochromatic
in the preceding symbol, and if its vertices are `d_0,...,d_(m-1)`, its
lift has

`sum_j r_(d_j)=ell*q`

for some positive integer `ell`.  This is the exact finite functional graph
that must be classified; merely observing that it has cycles gives no
contradiction, because only two replay shifts are available before the
outer cube promotes.

As an executed model, take

`Q=223222322232322232223`, `q=21`.

The least-root profile produced by `curling.py` is

`(4,4,4,3,3,1,1,7,4,1,1,4,4,2,2,1,1,6,6,1,1)`.

Its circular parent map has cycles

`(0,17,11,7)` with root-span sum `21`,

`(1,18,12,8,4)` with root-span sum `21`.

The first cycle's preceding symbols are all `3`; the second cycle's are all
`2`.  Thus this exact model already realizes multiple monochromatic cycles
with variable edge spans.  Any proposed classification must accommodate
this configuration rather than assuming one constant period around a
cycle.

Fine--Wilf, borders, primitivity, and the two boundary symbols alone cannot
exclude this tower.  A binary combinatorial countermodel exists
recursively.  Start with `Q_1=(k-1)`, put `T_i=Q_i^k k`, choose
`M_i>|T_i|+1`, and set

`Q_(i+1)=T_i k (k-1)^M_i`.

The words `T_i` are nested prefixes, so they define an infinite limit word
having every required prefix `Q_i^k k`.  Each `Q_(i+1)` is primitive: if it
were a proper power with root length `d`, then
`d<=|Q_(i+1)|/2<M_i`; its last `d` symbols would make the root the constant
word `(k-1)^d`, contradicting the occurrence of `k`.  This construction
uses only the two symbols `k-1,k`.

Even the three block-boundary curling numbers do not capture the missing
condition.  Executing both implementations in `curling.py` on
`P=23322` gives

| word | curling number | maximizing-root lengths |
|---|---:|---|
| `P` | 2 | `1` |
| `P^2` | 2 | `1,5` |
| `P^3` | 3 | `5` |

Nevertheless, the executed orbit from seed `P` begins with labels
`2,3,1`, rather than generating another complete copy of `P`.  The
load-bearing extra condition is therefore equality of the curling numbers
at every corresponding internal offset of all copied blocks.  Ruling out
an infinite fixed-origin tower with those full internal equalities remains
the exact unresolved case; a purely periodicity- or border-based argument
cannot do it.

## Executed masking counterexample

All curling numbers in this subsection were produced by both implementations
in `curling.py`.

Start the orbit at `23222323`.  Two states are

`S_25 = A = 232223232223222322322232223232223`,

`S_46 = B = 232223232223222322322232223232223222322322232223232223`.

The word `B` ends in the entire 33-term word `A`.  Executed values are

| word | curling number | `E` |
|---|---:|---:|
| `A` | 2 | `2` |
| `A2` | 2 | `13/6` |
| `B` | 2 | `18/7` |
| `B2` | 2 | `55/21` |

The polynomial `x^2-3x+1` has value `1/441` at `x=55/21`, so
`55/21>alpha`; its value at `18/7` is `-5/49`, so `18/7<alpha`.
Therefore `A` returns to a golden-bad cut after one append, while `B`
returns after eleven appends.  The executed curling-number streams from
these two states agree for their first nine labels.

The masking witness in `B2` has length 55 and period 21.  It crosses the
left boundary of the identical suffix `A2`.  Hence neither the bounded
kernel, an arbitrarily longer copied local suffix, nor the initial exact
integer labels determine the next golden-bad return.

## Exhaustive binary kernel table

For the eventual `{2,3}` specialization, an exhaustive script enumerated
all `Y in {2,3}^p` under the bounds above.  For `p>d`, it formed
`T=(Y^3)` with the final `d` twos removed, checked `E(T)<alpha` using exact
rational arithmetic, and executed `curling_number(T 2^i)` for
`0<=i<=d`.  The surviving nonconstant roots were:

| `d` | `p` | roots `Y` |
|---:|---:|---|
| 1 | 2 | `32` |
| 2 | 3 | `322` |
| 2 | 4 | `2322, 3222, 3322` |
| 2 | 5 | `22322, 23222, 23322, 32322, 33222` |
| 3 | 4 | `3222` |
| 3 | 5 | `23222, 33222` |
| 3 | 6 | `223222, 233222, 323222` |
| 3 | 7 | `2223222, 2233222, 2323222, 3223222, 3233222, 3323222` |

The constant root `Y=2`, `p=1`, is possible for every `d`.  This table is a
finite computation, not a substitute for the missing global compatibility
argument.
