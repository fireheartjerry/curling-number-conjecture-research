# Maximal-run stack and circular-profile variation

This note records two exact results and one exact remaining gap.  It does
not prove termination.

## 1. Canonical powered suffixes as maximal runs

Use half-open cuts in a bi-infinite word.  A maximal run is an interval
`[l,r)` with least period `p`, length at least `2p`, and

```
W[l-1] != W[l-1+p],       W[r] != W[r-p].
```

For a canonical value-`2` copy-parent ray vertex `v_i`, let `d_i` be its
least maximizing-root length and let `e_i=cn(W[0..v_i])`.  The complete
canonical power

```
[v_i+1-e_i*d_i, v_i+1)
```

lies in a unique maximal run of least period `d_i`.  Primitivity of the
maximizing root proves that `d_i` is the least period: if its square also
had a period `p<d_i`, Fine--Wilf on length `2d_i` would give the root a
proper divisor period.

The last copy begins at the parent cut.  Its first symbol is
`e_(i-1)` and its last symbol is `2`.  Therefore this run extends one
symbol to the right exactly when `e_i=e_(i-1)`.  At a flip, it ends at the
ray vertex.  This gives the exact ascent/descent normal forms already
recorded in `dependency_dag.md`.

This representation does not by itself produce a well-founded stack.
Runs can cross in FIFO order: both left and right endpoints may increase.
The following exact family reaches the Fine--Wilf threshold minus one at
every successive overlap.

For `n>=3`, put

```
A_n = 2^(n-2) 3 2
W_n = 9 A_3 A_3 A_4 ... A_n
    = 9 (2^1 3)(2^2 3)...(2^(n-1) 3)2.
```

Then `|W_n|=n(n+1)/2+1`, and `W_n` ends in `A_n^2`.
In fact `cn(W_n)=2` and `n` is its unique square-root length.

Proof.  Let `z` be the position of the final `3`.  The distances between
successive `3` symbols, from left to right, are

```
2,3,...,n.
```

If a square suffix has root length `p`, the final `3` is copied to a `3`
at distance `p`.  Hence `p>=n`.  The value `p=n` gives the displayed
`A_n^2`.  If `p>n`, the immediately preceding `3`, at distance `n` from
`z`, lies in the last copy and is also copied by `-p`.  The open interval
between it and `z` contains no `3`, so its translated interval contains no
`3`.  Thus two earlier consecutive `3` symbols would also be at distance
`n`, impossible because all earlier consecutive gaps are smaller than
`n`.  A third copy at period `n` is impossible because the gap preceding
the penultimate `3` is `n-1`.  This proves both assertions.

Let `v_n=|W_n|-1=n(n+1)/2`.  The least-root parent relation is

```
v_n-n=v_(n-1).
```

In the right-infinite limit, the maximal period-`n` run containing the
terminal square of `W_n` is

```
R_n = [v_(n-2), v_n+n-1)
```

and has length `3n-2`.  It does not extend left because the compared
symbols are `3` and `2`.  It extends exactly `n-2` symbols right because

```
A_n     = 2^(n-2) 3 2,
A_(n+1) = 2^(n-1) 3 2.
```

Successive runs overlap in exactly

```
|R_n intersect R_(n+1)| = 2n-1.
```

Their periods are `n` and `n+1`, so the Fine--Wilf threshold is
`n+(n+1)-gcd(n,n+1)=2n`.  Every overlap misses the threshold by one.

This is an infinite exact model of the suffix-power, least-root, and
copy-parent equations.  It is **not** an orbit-word model:
executed code gives `cn(W_n without its last 2)=1`, not `2`.  Thus it
falsifies a rank based only on maximal-run interval geometry, but it does
not falsify a rank that also retains the birth-label equation at every
ray vertex.

`research/search_square_ray.cpp` independently found this family by exact
search.  `curling.py` recomputed the displayed curling numbers.

## 2. Proper circular profiles and cubic-run components

Let `Q` be a primitive binary circular word of length `N`.  At every
half-open cut `c`, let `F(c)` be the largest exponent of a periodic suffix
in `Q^Z` whose root length is strictly less than `N`.  Assume

```
F(c) in {2,3} for every c.
```

Thus every cut is squareful and no proper fourth power occurs.  Write
`Var(U)` for the number of cyclic adjacent symbol changes in a binary
word `U`.

For every proper maximal run `R=[l,r)` of least period `p`, its cube-end
interval is

```
J(R) = [l+3p,r]
```

as an interval of half-open cuts.  Therefore

```
{c : F(c)=3} = union_R J(R),
```

where `R` ranges over the proper cubic runs.  The equality includes
maximality: every cube extends uniquely to a maximal run, and every cut
in `J(R)` ends a period-`p` cube.

Let the cyclic connected components of this union be
`C_0,...,C_(m-1)`.  Then

```
Var(F)=2m.
```

Each component can be mapped to a specific cubic run: choose a run whose
cube-end interval contains the first cut of the component.  Distinct
components map to distinct runs, because `J(R)` is connected and is
contained in one component.

### CKRRW handles

The handle theorem used here is Definition 7 and Lemma 8 of

M. Crochemore, M. Kubica, J. Radoszewski, W. Rytter, and T. Walen,
“On the Maximal Number of Cubic Runs in a String,” *LATA 2010*,
LNCS 6031, 227--238.

For a non-unary run of period `p`, take the lexicographically least and
greatest conjugates `u_min,u_max` of its primitive period word.  A handle
is an inter-position in the middle of an occurrence of
`u_min u_min` or `u_max u_max` contained in the run.  Handle sets of
different linear runs are disjoint, and a cubic run has at least two
handles.

For a binary alphabet ordered `2<3`, `u_min` begins in `2` and ends in
`3`, while `u_max` begins in `3` and ends in `2`.  Hence every
`u_min|u_min` handle is a `3->2` symbol boundary and every
`u_max|u_max` handle is a `2->3` boundary.  A non-unary cubic run has at
least one handle of each orientation.

For a unary period-one cubic run, CKRRW instead uses its internal
equal-letter inter-positions.  Under `F<=3`, such a maximal run has length
exactly three.  Its two external edges are unequal and consist of one
`2->3` edge and one `3->2` edge.  Replacing the two equal handles by
these external edges is the exact obstruction.

### The naive replacement is false

The smallest admissible executed counterexample is

```
Q = 32232223222
F = 32332223222.
```

There are three `F=3` components:

```
{0}, {2,3}, {7}.
```

The unary cubic runs for the first and third components offer external
edge pairs

```
{7,10}, {3,6}.
```

The middle component is supplied by the maximal circular run

```
l=1, p=4, length=13,
```

whose CKRRW min/max handle set is exactly `{6,7}`.  Thus CKRRW handles
plus unary external edges have union

```
{3,6,7,10},
```

only four edges for the six charges required.  The two uncharged symbol
boundaries are `{0,2}`; both are internal transitions of the period-four
cubic run but are not CKRRW handles.  No alternating-path proof restricted
to CKRRW handles can work.

`research/analyze_profile_variation.cpp` produced all profile values,
maximal runs, handles, and edge sets in this example.  No admissible
primitive binary circular word exists at lengths below eight, and the
same executable finds no failure of the naive replacement at lengths
eight through ten, so length eleven is minimal.

## 3. Exact oriented-Hall residual

For an `F=3` component `C` and an orientation
`sigma in {2->3,3->2}`, define `E_sigma(C)` as follows.

1. For every non-unary maximal cubic run `R` with `J(R) subset C`,
   include every internal `sigma`-oriented symbol boundary of `R`.
2. For every unary length-three run with its cube-end cut in `C`, include
   its unique external `sigma`-oriented boundary.

These candidates are word-theoretic: the extra positions in item 1 are
the other copies, inside the same maximal periodic run, of oriented
period-word transitions.  They are not arbitrary nearby boundaries.

The desired lemma is the pair of oriented Hall inequalities

```
|union_(C in A) E_sigma(C)| >= |A|
```

for every set `A` of `F=3` components and each orientation `sigma`.
It gives injections from components to `2->3` and to `3->2` boundaries.
The two images are disjoint, so

```
Var(F)=2m <= Var(Q).
```

The exact computational status originally reached here was:

* every `E_sigma(C)` is a cyclic interval in the cyclic order of
  `sigma`-oriented boundaries;
* for every cyclic interval `I` of consecutive `F=3` components,
  `|union_(C in I) E_sigma(C)|>=|I|`;
* a full oriented matching exists;

for every primitive binary circular word of lengths at most `25` whose
proper profile lies in `{2,3}`.  Enumeration is exhaustive over all
`2^N` binary words, followed by primitivity and exact-profile filters.

The first bullet has a direct interval explanation.  The cube-end
intervals belonging to one `F=3` component form a connected cover.
Every corresponding full maximal run contains its cube-end interval, so
their full intervals have connected union.  Intersecting that union with
the cyclically ordered boundaries of one orientation gives a cyclic
interval; unary external boundaries attach at its ends.

The interval-Hall step is false.  Exhaustive exact enumeration through
length `29`, now quotiented only by cyclic rotation, finds no failure,
but the minimal length-`30` obstruction is given in Section 6.  It
consists of two consecutive singleton components supplied by adjacent
unary cubes.  Thus no alternating-cycle argument can prove the proposed
statement: the obstruction is already a two-vertex Hall deficit.

## 4. Equality grammar with singleton 3-runs

This section assumes the equality branch `F(Q)=Q` and that every
`3`-run in `Q` is a singleton.  Encode

```
Q(A) = product_i 2^(a_i) 3,       a_i in {1,2,3},
```

with cyclic indices in a run code `A=(a_0,...,a_(m-1))`.

### Exact square equation at a 2-cut

Let the cut be after `r` twos in run `i`, where
`0 <= r < a_i`.  A nonunary proper square root containing exactly `h`
symbols `3` exists if and only if

```
1 <= h < m,
r <= a_(i-h),
a_(i-2h) >= a_(i-h)-r,
a_(i-2h+j) = a_(i-h+j)       for 1 <= j < h.       (SQ)
```

Its physical root length is

```
p = sum_(j=0)^(h-1) (a_(i-h+j)+1).
```

Proof of necessity and sufficiency: the later root copy is exactly

```
2^(a_(i-h)-r) 3
2^(a_(i-h+1)) 3 ... 2^(a_(i-1)) 3 2^r.
```

The earlier copy can start in the final part of run `i-2h`.  It has the
same first 2-block precisely when that run has at least
`a_(i-h)-r` twos, and its complete internal 2-runs are equal precisely
when the displayed `h-1` equations hold.  These conditions also
construct the two copies.  The formula for `p` follows by counting.
If `h=m`, that formula is `|Q|`, so properness is exactly `h<m`.

For the load-bearing offsets `r=0,1`, the condition
`r<=a_(i-h)` is automatic.  In particular the cut before the first
`2` is squareful exactly when, for some `h`,

```
(a_(i-2h),...,a_(i-h-1))
    = (x,V),
(a_(i-h),...,a_(i-1))
    = (y,V),
x >= y.                                             (WSQ)
```

Thus it is a clipped or weak square in the run code: the two length-`h`
blocks agree except that the first entry of the earlier block may be
larger.  A witness for `r=0` is automatically a witness for `r=1`.
Offsets `r>=2` already have the unary square `22`.

`research/check_run_length_grammar.py` verifies `(SQ)` against direct
binary-word square enumeration at every 2-cut of the model below.

### General cube equation and the tightness lemma

At the cut immediately before the `3` following run `i`, put
`beta=a_i`.  A nonunary cube root containing `s` symbols `3` gives

```
g = a_(i-s) = a_(i-2s),
alpha = g-beta >= 0,
a_(i-3s) >= alpha,
a_(i-3s+j)=a_(i-2s+j)=a_(i-s+j)  for 1<=j<s.       (GCUBE)
```

The root has physical length

```
p = sum_(j=1)^s (a_(i-3s+j)+1) < |Q|.
```

The factor itself has clipped run code

```
[alpha,C,g,C,g,C,beta],       g=alpha+beta,          (CUBE)
```

where `C` has length `s-1`.  The first displayed `alpha` need not,
in a general word, be the whole ambient run `a_(i-3s)`; `(GCUBE)`
initially gives only capacity.  `alpha=0` is the case in which the root
begins with `3`.  Conversely these equations expand directly to three
copies of the binary root.  They remain valid when `3s>=m`; all code
indices are taken in the periodic lift, not in a nonwrapping segment.

In a fixed profile the capacity must be tight:

```
a_(i-3s)=alpha >= 1.                               (TIGHT)
```

Here is the full physical proof.  Lift `Q` periodically to a word on
integer coordinates and let the cube occupy `[l,c)`, with period `p`,
where `c` is the cut before the terminating `3`.  The root ends in the
whole terminal block `2^beta`.  Let

```
d=a_(i-3s)-alpha.
```

If `d>0`, choose `delta=min(d,beta)`, so
`1<=delta<=beta`.  The `delta` symbols immediately left of `l` are
`2`; their positions one period to the right are among the final
`delta` symbols of the first root copy, also `2`.  Hence the
period-`p` factor extends left by `delta`, and

```
[l-delta,c-delta)
```

is another length-`3p` cube.  Its endpoint is the cut after
`beta-delta` twos in run `i`, whose next symbol is `2`.  The root
length is still the same proper `p<|Q|`.  Thus that cut has proper
curling number at least three, contradicting `F=Q`, which labels it
`2`.  Therefore `d=0`.  Since every ambient 2-run has positive length,
this also excludes `alpha=0`.

No fourth power at the original `3`-cut means that the cube root is
primitive.  Equivalently its circular run code

```
P=(C,g)
```

is primitive.  Every defect `a_i in {1,2}` in a fixed profile must
therefore end at least one tight primitive gadget `(CUBE)`.

For `s=1`, the only tight possibilities are

```
[1,2,2,1], [1,3,3,2], [2,3,3,1].
```

If all defects use `s=1`, the first possibility is impossible: either
middle `2` is itself a defect, but its preceding three entries do not
have any of the three displayed forms.  The other two possibilities
force defects every third code position and force their values to
alternate `1,2`.  Under `(WSQ)` the defect-free primitive exception
`A=(3)` is impossible.  Therefore a primitive code in the all-`s=1`
branch is, up to rotation,

```
A=133233.
```

Its binary expansion has length `21`.

### A local `s>1` exclusion is false

The claim “a primitive `s>1` cube gadget forces an unsquareful 2-cut”
is false even when the whole proper profile lies in `{2,3}`.  The
primitive code

```
A=12112121
```

has, at endpoint `i=0`, the exact `s=2` gadget

```
[alpha,C,g,C,g,C,beta]=[1,1,2,1,2,1,1],
P=(1,2).
```

Every 2-cut is squareful: the executed `r=0` witness sets, in code
order, are

```
{1,2}, {1}, {3,5}, {1,3,5}, {1,3}, {3}, {1,3}, {2}.
```

Direct enumeration gives

```
Q=2322323232232322323,
F=2333222223323333222.
```

Thus `F` uses only `2,3`, but it is not equal to `Q`.  Only the defect
at code endpoint zero has a cube gadget; the other seven defects do
not.  Any exclusion of `s>1` must therefore use the global hypothesis
that **every** defect is covered, not only squarefulness or local
periodicity.

Even squarefulness plus global (nontight) cube coverage is insufficient.
The primitive code

```
A=133233233
```

has all 2-cuts squareful and every defect cube-covered.  Endpoint zero
has a tight `s=3` gadget with `P=332`, as well as an `s=1` gadget.
However, the `s=1` gadget ending at run six has

```
beta=2, alpha=1, a_3=2>alpha.
```

The tightness shift with `delta=1` produces a period-four cube at
offset `r=1` of run six.  Direct computation gives one profile
disagreement, at binary cut 22:

```
Q[22]=2, F[22]=3.
```

This is the smallest executed illustration of why the no-cube
condition at every 2-cut is load-bearing.

### The length-33 globally cube-covered near-model

The primitive code

```
A_33=133233133233133213323313323313323
```

has a primitive `s=6` gadget ending at zero with

```
alpha=2, beta=1, P=133233,
```

and another ending at 16 with `P=313323`.  Together with ten `s=1`
gadgets, these cover every defect.  Its binary word has length `114`;
its proper profile agrees with the word at 112 of 114 cuts.

The two failures are the first two 2-cuts, `r=0,1`, of code run
`i=18`, which are binary cuts 61 and 62.  Here `a_18=3`.  For `h=1`,
`(SQ)` fails because

```
a_16=1 < a_17-r=3-r,       r=0,1.
```

For every `2<=h<=32`, an internal equality in `(SQ)` fails.  The first
failing `j` for each `h` is the following exact certificate:

```
2:1 3:1 4:1 5:1 6:4 7:1 8:1 9:3 10:1 11:4
12:1 13:1 14:2 15:1 16:1 17:15 18:1 19:1 20:1
21:1 22:4 23:1 24:1 25:2 26:1 27:3 28:2 29:2
30:1 31:2 32:2.
```

Here `h:j` means

```
a_(18-2h+j) != a_(18-h+j)
```

modulo 33.  `research/check_run_length_grammar.py` recomputes every
profile value, both gadgets, and this certificate.

`research/z3_run_code_fixed.py` encodes the complete proper power
conditions, including wrapping roots:

* every 2-cut has a square and no cube;
* every 3-cut has a cube and no fourth power;
* every physical root length is strictly below `|Q|`;
* `A` is primitive.

In unconstrained mode through `m=28` it finds only the rotation class
of `A=133233`.  With a required nontrivial `s>1` cube it reports
unsatisfiable for every `m<=33`; combined with the proved all-`s=1`
classification above, this leaves only the six rotations of
`A=133233` throughout that range.  The `m=34` nontrivial query timed
out as `unknown` after 60 seconds.  The solver is exhaustive over the
symbolic domain `{1,2,3}^m`; this is bounded evidence, not a proof for
arbitrary `m`.  `research/check_run_length_grammar.py` calibrates
the general exponent-`k` code equation against direct binary
enumeration for every one of the 363 codes of lengths at most five.

The remaining singleton-3 classification lemma is:

> A primitive cyclic code over `{1,2,3}` satisfying the exact
> square/no-cube equations at every 2-cut and the exact
> cube/no-fourth equations at every 3-cut has no primitive tight cube
> gadget with `s>1`.

The local counterexamples show that squarefulness, global cube
coverage, tightness, and exclusion of unwanted cubes are separate
load-bearing parts of this residual lemma.

### Maximal physical-period descent for internal 3-cuts

Choose, among all primitive cube roots at 3-cuts, one of maximal
physical length `p`, and write its tight maximal run as

```
R=[l,l+3p)=U^3.
```

Tightness makes the left comparison `3` versus `2`; singleton 3-runs
make the right comparison `3` versus `2`.  Hence `R` is indeed
maximal on both sides.

Take any `3` inside `U`, and its aligned occurrence at the cut

```
x=l+2p+r,       0<r<p,
```

in the third copy.  Let `q<=p` be a primitive cube-root length at
`x`, which exists because `F(x)=3`; maximal choice of `p` gives the
inequality.  Put `d=gcd(p,q)`.

If the `q`-cube begins left of `l`, its intersection with `R` has
length `2p+r`, which is greater than `p+q-d`.  Fine--Wilf gives period
`d` on a factor containing a full length-`p` conjugate of `U`, making
`U` imprimitive.  If the `q`-cube begins inside `R` and

```
2q+d >= p,
```

then its full length `3q` is at least the Fine--Wilf threshold
`p+q-d` and at least `p`; the same contradiction follows.  The case
`q=p` would give two period-`p` runs overlapping in more than `p`
symbols and extend `R` to the left, contradicting maximality.
Therefore every such internal cube satisfies

```
2q+gcd(p,q) < p,
q < p/2,
```

and its entire cube lies inside `R`.  This is a genuine finite descent:
every 3-cut inside the third copy of a maximal root is supplied by a
strictly half-sized cube.  What it does not yet control is the square
root required at the 2-cuts in the first copy; that is the remaining
compatibility bottleneck.

For the period-21 root in the length-33 near-model, executed code gives

```
U=223232223222322322232.
```

Its six 3-cuts, at offsets

```
2,4,8,12,15,19,
```

have third-copy child cube periods

```
1,4,1,1,4,1.
```

The two period-four child intervals overlap in one symbol, below their
Fine--Wilf threshold; unary children nest inside them.  Thus the raw
family is not laminar, but every crossing is shallow in exactly the
run-overlap sense above.  In the circular word `U`, the 2-cut offsets
with no square wholly contained in the linear prefix `U[0:cut]` are

```
0,1,3,9,10.
```

The last two are the two failed cuts in the length-33 insertion.
This calibration isolates the missing interval-tree assertion:
shallowly crossing child cubes do not by themselves supply the square
needed at the last first-copy hole.  A proof must show that any
external square filling that hole either crosses a child/main boundary
past the Fine--Wilf threshold or forces a wrapping border of the form
analyzed below.

There is a distinct wrapping subcase.  Under `(TIGHT)`, `3s>=m`
implies that the physical cube factor traverses at least one whole
period of `Q`, hence `3p>|Q|`.  Fine--Wilf rules it out when

```
2p+gcd(p,|Q|) >= |Q|,
```

because the factor then has period `gcd(p,|Q|)` and contains a full
length-`|Q|` rotation.  The complementary inequality is not empty:
the near-models above have wrapping cubic factors below the
Fine--Wilf threshold.  Excluding this complementary wrapping case
using the exact no-cube constraints remains part of the lemma.

There is a further exact reduction in that complementary case.  Let
the tight cube be `U^3=[l,l+3p)` and write `n=|Q|`.  Fine--Wilf gives
`2p+gcd(p,n)<n`, so if `3p>n` there is a unique

```
t=n-2p,       0<t<p.
```

The period-`n` continuation at `l+n` must agree with the third copy of
`U`.  Therefore

```
U[t:p]=U[0:p-t],
```

so `t` is a period of `U`, and the length-`n` rotation beginning at
`l` is

```
Q = U U U[0:t].
```

Consequently the `t` symbols immediately before `l` are
`T=U[0:t]`, and `T U` is `t`-periodic.  At the first internal
`U|U` boundary, which lies strictly inside a merged 2-run and is
therefore a 2-labelled cut, the preceding `t+p` symbols are
`t`-periodic.  If `p>=2t`, their final `3t` symbols form a `t`-root
cube at that 2-cut, a contradiction.  Every surviving wrapping
gadget must hence satisfy

```
n/3 < p < 2n/5,
t > p/2,
b=p-t=3p-n < p/2.
```

Thus its root `U` has the short border of length `b` forced by
`U[t:p]=U[0:b]`.  The code `A=133233133233133` realizes the excluded
side with `p=21,n=52,t=10`: its first internal boundary has the
unwanted period-ten cube.  The code `A=133233233` has
`p=11,n=32,t=10`; only a period-ten square is forced there, so the
short-border survivor still needs a separate argument.

The survivor has an exact truncation normal form.  Put

```
T=U[0:t]=B C,       |B|=b.
```

Since `U` has period `t` and length `t+b`,

```
U = T B = B C B
```

and the rotation of `Q` beginning at the tight cube start is

```
Q = U U T = B C B B C B B C,
U^3 = Q B.
```

Thus a conjugate period-`p` square ends at the cut just before the
displayed prefix `B`, and its exponent first reaches three at the cut
just after that `B`.  In the `A=133233233` model,

```
B=2,       C=322232223.
```

The two truncation-adjacent cuts have both the long period-eleven root
and a shorter period-four root: the long root changes from a square
to a cube across `B`, while the shorter root masks the same endpoint.
This supplies the concrete target for a descent proof: either force a
strictly smaller cube root at the end of `B`, as in this model, or use
the exact fixed-profile equations inside `B` to produce an unwanted
cube at a 2-cut.  That dichotomy has not yet been proved.

One more wrapping obstruction follows from the least linear period
`r` of `U`.  Both `T=U[0:t]` and `U` are prefixes of the same
right-infinite `r`-periodic word.  If

```
r divides t,
```

then the phase resets correctly at the join, so the `t+p` symbols
`T U` preceding the first internal `U|U` boundary are `r`-periodic.
That boundary is a 2-cut.  Hence

```
t+p >= 3r
```

forces an unwanted `r`-cube there (and `t+p>=4r` forces a fourth
power).

The executed essential-survivor near-model

```
A=133133233133233133
```

has `n=62,p=21,t=20,b=1`, with no smaller cube root at the main
endpoint.  Its root `U` has least period `r=10`.  Thus `T U` has
length 41 and produces the observed period-ten fourth power at a
2-cut.  Direct profile computation finds unwanted period-ten cubes at
cuts 10, 12--18 and fourth powers at cuts 20--21.  This falsifies the
simpler claim that every short-border survivor must have a smaller
masking cube at its main endpoint; the no-cube constraint can instead
fail later along the phase stream.

## 5. Consecutive 3-components

This section drops the singleton-3 assumption.  In a binary fixed
profile, `333` is impossible: a maximal run of at least three `3`
symbols is followed by a `2`, but the cut before that `2` has the
unary cube `333`.  Hence only a double component

```
Q[c],Q[c+1],Q[c+2] = 3,3,2
```

needs analysis.  The preceding symbol `Q[c-1]` is also `2`.

### Exact two-root Fine--Wilf alternative

Let primitive cube roots of lengths `p` and `q` end at cuts `c` and
`c+1`, respectively.  They are primitive because an imprimitive cube
root would give exponent at least six, whereas the profile value is
three.  Their cube intervals overlap in exactly

```
L = min(3p,3q-1)
```

symbols.  If `p!=q` and

```
L >= p+q-gcd(p,q),
```

Fine--Wilf gives the gcd period on a factor containing a complete
conjugate of the longer root, contradicting its primitivity.  Thus

```
q>p  implies  q > 2p+gcd(p,q),
p>q  implies  p >= 2q+gcd(p,q).                  (SEP)
```

Distinct roots at the two adjacent cuts therefore differ by a factor
strictly greater than two.

If `p=q`, the adjacent cubes merge into one period-`p` interval of
length `3p+1`.  In a fixed profile it cannot extend one symbol left or
right, since either extension would shift a period-`p` cube to the
neighboring 2-cut.  If `U` is the root ending at cut `c`, exact
transport gives

```
U starts with 32,
U ends with 2,
U^3 3 = 3 (rot(U))^3.                            (BRIDGE)
```

Here `rot(U)` moves the initial `3` to the end.  Tightness at the left
edge also forces another double component: if the bridge starts at
`a=c-3p`, then

```
Q[a-1],Q[a] = 3,3.
```

Thus an equal-root double component has a predecessor double component
exactly `3p+1` symbols earlier.  These bridge edges can nest or cross
when `U` itself contains double components; they do not automatically
tile the circle.

For a globally maximal bridge period `p`, every double component
inside the third copy of `U` has both of its cube roots below `p/2` by
the maximal-period descent lemma.  If those roots are equal, its
entire shorter bridge is contained in the outer bridge.  If they are
unequal, `(SEP)` supplies a further factor-two separation.  This is a
rigorous nested reduction, but it does not yet exclude a finite cycle
of bridge and separated-root components.

### Exact local falsifiers

Same-period transport does occur.  The smallest primitive executed
example is

```
Q=3323232,
F=3321222.
```

At both consecutive 3-cuts the primitive cube root is `U=32`, of
length two:

```
(32)^3 3 = 3 (23)^3.
```

The following 2-cut has curling number exactly two, not three.  Thus
no local argument from the two cubes alone can force a cube at the
following 2-cut.

Even global squarefulness and absence of fourth powers do not suffice:

```
Q=332323323232,
F=332222222223.
```

This word is primitive, every profile value lies in `{2,3}`, the
initial profile is exactly `332`, and the same period-two bridge
accounts for the two 3-cuts.

Global squarefulness does not even force the adjacent cube-root sets to
intersect.  The executed primitive example

```
Q=3322232233222332223223322232233222,
F=3322232222222322223222223333222222
```

has every profile value in `{2,3}` and has the exact local profile
`F[0:3]=332`, but its cube-root sets at the consecutive 3-cuts are
respectively `{1}` and `{8}`.  Thus `(SEP)` is an essential branch, not
merely an artifact of choosing noncanonical roots.  The full fixed
equation at all other cuts is load-bearing.

A larger calibration embeds the known period-21 singleton word as a
bridge root.  For

```
U=322232322232223223222,
Q=U^3 3,
```

the primitive word `Q` has length 64, its proper profile has maximum
three, and the double component and following 2-cut are all exact.
Only cuts 2, 6, and 11 fail, each because it is not squareful.  This
is the double-component analogue of the length-33 singleton
near-model: after exact bridge transport, the remaining obstruction is
again the first-copy square-hole compatibility.

`research/check_double_three.py` recomputes all values.  It exhaustively
shows that the length-seven example is minimal through length six, the
squareful length-twelve example is minimal through length eleven, and
audits `(SEP)` for every relevant primitive root pair through circular
word length 14.

The four-cut argument and two sharper global falsifiers are recorded in
`adjacent_double_bridge.md` and recomputed by
`check_double_three_near_fixed.py`.  In particular:

* if a double component is the only one on the circle and has a common
  root `p` at its two cuts, then necessarily `|Q|=3p+1` and a rotation is
  exactly `U^3 3`;
* a primitive length-35 model satisfies full square coverage, full cube
  coverage at every 3-label, and exclusion of fourth powers, but four
  2-labels acquire unwanted cubes;
* a primitive length-41 model satisfies full square coverage and every
  no-cube/no-fourth constraint, but four 3-labels lack cubes.  Its exact
  normalized double component realizes the separated root scales
  `(1)` and `(16)`.

Thus bridge maximality, `(SEP)`, and full square coverage still do not
recover either direction of the global label/profile equality from the
other.  A complete adjacent-`33` exclusion must use both positive cube
coverage at every 3-cut and negative cube exclusion at every 2-cut.

For a globally maximal wrapping cube, the exact positive consequence is
proved in `maximal_wrapping_marker.md`: if `p=3r-ell`, the copied marker
at cut `E=2r+ell` has a contained cube root `s` satisfying

`2s+gcd(r,s)<r`.

This is a strict one-generation descent.  It is not directly iterable,
because `s` need not be globally maximal.  In the length-35 model the
forced descent is `13 -> 4`, while a later forbidden cube regrows to
root `9`; in the complementary length-41 model the formula points
exactly to one of the four missing positive cube witnesses.

## 6. The oriented-Hall route and profile-variation inequality are false

The oriented-Hall residual in Section 3 cannot be completed as stated.
The following executed primitive binary circular word of length `30` is
a minimal counterexample to the interval-Hall statement:

```
Q=222333233232223332332322233323,
F=322322322222223223222222232233.
```

Direct enumeration of every proper root length at every cut gives

```
F(c) in {2,3} for every c,
Var(Q)=16,
Var(F)=12.
```

The `F=3` components are

```
{3}, {6}, {14}, {17}, {25}, {28,29,0}.
```

The consecutive singleton components `{3}` and `{6}` each have exactly
one cubic root length, namely `1`.  Their cubes are the adjacent maximal
unary runs `222` and `333`.  For orientation `2->3`, the only external
candidate of either run is the shared boundary after position `2`.
Consequently

```
|E_(2->3)({3}) union E_(2->3)({6})|=1<2.
```

`research/check_interval_hall_counterexample.py` recomputes the exact
profile, all components, all square and fourth-power conditions, the two
singleton cube-root sets, and the shared oriented candidate.  The
exhaustive program `research/search_interval_hall_necklaces.cpp` uses
the FKM necklace recursion to enumerate exactly one representative of
every primitive binary circular word.  It finds zero interval-Hall
failures at every length `1` through `29`; at lengths `28` and `29` it
checks respectively `9,586,395` and `18,512,790` primitive necklaces,
with `42` and `24` passing the full squareful/no-fourth profile filter.

The weaker numerical inequality `Var(F)<=Var(Q)` survives this
length-`30` example, but is independently false.  The following executed
primitive binary circular word of length `38` is a counterexample:

```
Q=22233323332333222333233322233323332333,
F=33232232223222332322333333232232223222.
```

Direct enumeration of every proper root length at every cut gives

```
F(c) in {2,3} for every c,
Var(Q)=16,
Var(F)=20.
```

The `F=3` components are

```
{0,1}, {3}, {6}, {10}, {14,15}, {17},
{20,21,22,23,24,25}, {27}, {30}, {34}.
```

There is again a two-vertex failure of the proposed oriented Hall
system, with the same adjacent-unary mechanism at components `{3}` and
`{6}`.

`research/check_profile_variation_counterexample.py` recomputes the
profile, both variations, all components, the two singleton root sets,
and the shared oriented boundary.  Therefore neither

```
Var(F) <= Var(Q)
```

nor the stronger oriented-Hall statement can be used as a global
invariant, even under the complete squareful/no-fourth hypothesis.
