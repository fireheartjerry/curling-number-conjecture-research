# Minimal-seed compactness and the bounded-overhang cover

This note is a reduction only.  It does not prove the Curling Number
Conjecture.

## 1. Uniform termination at a fixed shorter length

Assume that a counterexample exists and let `n` be the least length of a
counterexample seed.  Put `m=n-1`.  Every seed of length `m` reaches curling
number one.

### Lemma 1

There is one finite integer `B` such that every length-`m` seed reaches
curling number one by time `B`.

#### Proof

Let `U` be a length-`m` seed, let `U_j` be its orbit, put
`c_j=cn(U_j)`, and let `t` be the least index with `c_t=1`.

For every `j<=t-2`, the appended value `c_j` occurs in the original seed
`U`.  Indeed, `cn(U_(j+1))>=2`.  The new-symbol lemma therefore says that
`c_j` occurred before its append position.  Iterating this observation
backwards through earlier append positions reaches an occurrence in `U`.

Also `c_0<=m`, and the one-step rise lemma gives `c_(j+1)<=c_j+1`.  If
`R>c_0` is any one of `c_0,...,c_(t-1)`, consider its first occurrence.
To rise from `c_0` to `R`, the orbit must previously output every integer in

`{c_0,c_0+1,...,R-1}`.

All these outputs occur no later than time `t-2`, and hence are distinct
entries of `U`.  Consequently

`R-c_0<=m`,

so `R<=2m`.  Outputs `R<=c_0` satisfy the same bound directly.  Therefore
every output before the first one is at most `2m`.

Let `A={2,3,...,2m}`.  Define the *type* of a length-`m` seed by:

1. which coordinates have a value in `A`, including that exact value; and
2. the equality partition of all remaining coordinates.

There are finitely many types.  Seeds of the same type are related on their
used symbols by a bijection that fixes every member of `A`.  Curling number
depends only on equality of symbols.  Since all outputs before the first one
belong to `A`, induction on the orbit time shows that two seeds of the same
type have the same outputs and reach one at the same time.  Taking the
maximum first-one time over the finite set of types gives `B`.

This argument is genuinely uniform over the unbounded integer alphabet:
values outside `A` survive only through their equality pattern.

## 2. The cover forced along a shortest counterword

Let `W` be the infinite word consisting of a shortest counterexample seed
of length `n` followed by its appended labels; use zero-based positions.
Thus, for every `r>=n`,

`W[r]=cn(W[0..r-1])>=2`.

For each `i>=1`, take the length-`m` window

`U_i=W[i..i+m-1]`

and compare its autonomous orbit with the actual continuation of `W`.
The local orbit reaches one by time `B`, whereas the global labels never
equal one.  Let `h_i<=B` be the first mismatching output index.  Put

`e_i=i+m+h_i-1`.

Immediately before the mismatch, the local state is exactly
`W[i..e_i]`, a suffix of the global state `W[0..e_i]`.  Write

`ell_i=cn(W[i..e_i])`,

`k_i=cn(W[0..e_i])=W[e_i+1]`.

Every powered suffix of the local word is also a powered suffix of the
global word, so `k_i>=ell_i`.  The outputs differ, hence

`k_i>ell_i`.

Choose a maximizing suffix `Y_i^(k_i)` of the global word, and let `a_i`
be its left endpoint.  If `a_i>=i`, the same power is a suffix of the local
word and would give `ell_i>=k_i`, a contradiction.  Therefore

`a_i<i`,

`i+m-1<=e_i<=i+m+B-1`.

In particular, with `C=m+B`, every position `i>=1` is crossed by a
maximal integer power whose endpoint is strictly before `i+C`, whose
exponent is the exact next label `W[e_i+1]`, and whose total length is at
least `m+h_i+1`.

The set of witness endpoints is syndetic: after translating by `m-1`,
every interval of `B+1` consecutive positions contains at least one
endpoint.

## 3. Bounded-overhang power covers do not imply periodicity

The geometric cover, without the exact curling-label condition, is much too
weak even when all roots have length at most two.

Let `t_0 t_1 ...` be the Thue--Morse word, and define

`C_j=(23)^(2+t_j) 2`.

Thus `C_j` is either `23232` or `2323232`.  Let

`V=C_0 C_1 C_2 ...`.

Apart from the first position, every position `i` is crossed by a square
ending at most two positions to its right:

* at the first position of a block, use the boundary square `22`;
* at block offset one or two, use the factor `2323` beginning at the block
  start;
* at every block offset at least three, use the alternating length-four
  factor ending at `i`.

Every displayed square starts strictly before `i`.

The word `V` is not ultimately periodic.  The factor `22` occurs exactly
at block boundaries.  The successive gaps between its occurrences are
`5+2t_j`.  Ultimate periodicity of `V` would make the occurrence indicator
of `22`, and therefore its bounded gap sequence, ultimately periodic.  That
would make the Thue--Morse word ultimately periodic, a contradiction.

For completeness, non-ultimate-periodicity of Thue--Morse follows directly
from `t_j` being the parity of the binary digit sum.  If `p` were an
eventual period, choose arbitrarily large `k` of parity equal to the binary
digit sum of `p-1`.  Then

`t_(2^k-p)=0`

while `t_(2^k)=1`, contradicting period `p`.

Thus a power interval that merely covers each point with bounded right
overhang is not an internal central square at that point.  Eventual
periodicity criteria based on proper/internal local periods do not apply.

## 4. Exact overlap dichotomy and the remaining configuration

Suppose two selected witness powers have consecutive endpoints `e<e'`,
endpoint gap `d=e'-e`, primitive root lengths `p,q`, and exponents `k,l`.
Their intervals are

`[e-kp+1,e]` and `[e'-lq+1,e']`.

If they overlap, the overlap length is

`O=min(kp,lq-d)`.

Put `g=gcd(p,q)`.  If `O>=p+q-g`, Fine--Wilf gives period `g` on an
overlap long enough to contain a complete factor of each primitive root.
It follows that `p=q=g`.  Hence unequal roots obey the exhaustive
alternative

`q>(k-1)p+g`

or

`p>(l-1)q-d+g`.

If `lq<=d`, the intervals do not overlap at all, which is another reset
case.  Since consecutive selected endpoints can be taken with
`d<=B+1`, the only way indefinitely many large unequal roots avoid merging
into one periodic run is by repeated large-scale expansion followed by
sharp scale drops (or by short disjoint resets).  The bounded-overhang
cover supplies no monotone quantity that excludes this alternation.

The exact-label facts

`k=W[e+1]=cn(W[0..e])`

and

`l=W[e'+1]=cn(W[0..e'])`

do not turn these off-center powers into internal central squares.
Maximality rules out higher integral suffix exponents at the two endpoints,
but it does not rule out either strict inequality above.  Proving that the
self-label dynamics forbids an infinite expansion/drop chain is therefore
the exact remaining gap in this route.
