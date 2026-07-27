# Cross-rank tower audit: reset equivalence and the golden-ratio barrier

This note audits the tower obtained by repeatedly taking the terminal
bottom-left branch in `contained_completion_commutative_square.md`.
It proves that the resulting word tower is not a new transition system:
it is exactly the late consecutive-reset tower already classified in
`reset_root_transition_split.md`.  The increasing endpoint rank is extra
terminal information, but it supplies no new word equation.  The note also
records why the Mignosi--Restivo--Salemi golden-ratio theorem does not close
the remaining tower from the currently proved hypotheses.

## 1. Setup

Let `T` be the right-infinite word traced by a hypothetical bad orbit, and
let the initial seed occupy `T[0:N_0]`.  A late normalized reset root is a
primitive prefix

```
C=T[0:n]
```

such that

```
T[0:3n]=C^3,             cn(T[1:3n])=2,
pc_C=C,                  C[0]=min(C)=2.                (1)
```

Write

```
D=T[1:3n],
H=T[0:3n+1]=C^3 3,
F=T[1:3n+1]=D3.                                 (2)
```

Assume the terminal-bottom-left branch:

```
H is bad,                F is terminal.          (3)
```

Lemma 4 of `contained_completion_commutative_square.md` follows the two
orbits in (3) to their first unequal values.  For their common output `G`
it produces a primitive word `Y`, of length `r`, with

```
H G=Y^3=T[0:3r],
F G=(Y^3)[1:]=T[1:3r].                            (4)
```

The high word in (4) is bad, the low word is terminal, `pc_Y=Y`, and
`Y[0]=min(Y)=2`.

## 2. Lemma: the new root is the consecutive fixed-origin reset

The reset endpoints `3n` and `3r` are consecutive strict mismatch
endpoints for the pair

```
T[0:t],              T[1:t].                      (5)
```

More precisely,

```
cn(T[0:3n])=3,       cn(T[1:3n])=2,               (6)
```

and

```
cn(T[0:t])=cn(T[1:t])=T[t]
             for 3n+1<=t<3r,                     (7)
```

while

```
cn(T[0:3r])=3,       cn(T[1:3r])=2.               (8)
```

### Proof

Equation (6) is (1), including the displayed primitive cube and the exact
deleted value.  At `t=3n+1`, the two words in (5) are exactly `H,F`.
Lemma 3 of `contained_completion_commutative_square.md` proves that their
curling numbers are equal.  The definition of `G` as the complete common
output before the first unequal values gives (7).  Equation (4), together
with the first-mismatch conclusion of its cited Lemma 4, gives (8).  There
is no integer cut strictly between `3n` and `3n+1`, so the enumeration is
exhaustive.

Consequently Section 3 of `reset_root_transition_split.md` applies with

```
p=n, q=r, k=ell=3.
```

Its exhaustive late-reset dichotomy strengthens the raw inequality
`r>2n+gcd(n,r)` to exactly one of

```
external:
    r>3n,
    Y begins C^3 3;                               (9a)

internal:
    r=3n-a,
    1<=a<N_0,
    C[:a]=C[-a:],
    T[a]=3.                                       (9b)
```

The equality `r=3n` is impossible because it would make `Y=C^3`
imprimitive.  In the internal case the parameter used in the short
calculation of Lemma 4 is `s=n-a`: its identity
`C[:n-s]=C[s:]` is exactly the border in (9b).  Thus that apparent
short external branch is the bounded seed-anchored internal reset
mechanism already isolated in the older tower.

## 3. What the terminal rank adds

For every `t` in the common interval of (7), the shifted word

```
S_t=T[1:t]
```

is a state on the terminal orbit from `F`.  Hence

```
tau(S_t)=tau(F)-(t-(3n+1))
```

and its endpoint rank is constant:

```
t+tau(S_t)
 =3n+1+tau(F)
 =3r+tau(T[1:3r]).                               (10)
```

If the preceding reset was selected by the minimum-deleted-tail rule,
Lemma 3 of `contained_completion_commutative_square.md` gives

```
tau(F)>tau(D).
```

Writing

```
R_n=3n+tau(D),       R_r=3r+tau(T[1:3r]),
```

equation (10) yields

```
R_r-R_n=1+tau(F)-tau(D)>=2.                       (11)
```

Thus repeated terminal-bottom-left transitions produce a strict
cross-rank tower.  Equations (9a)--(9b) are nevertheless its complete
word-combinatorial content: (10)--(11) give no upper bound on `r`, on
`tau(F)`, or on the next rank.  In particular, rank growth cannot be
substituted for the equal-rank maximum-period contradiction used for an
ordinary prefix seam.

## 4. Golden-ratio periodicity does not follow

Mignosi, Restivo, and Salemi prove the following exact threshold theorem.
For `phi=(1+sqrt(5))/2`, a right-infinite word is ultimately periodic if
and only if every sufficiently long prefix has a suffix whose rational
exponent is at least

```
phi+1=phi^2.
```

Source: F. Mignosi, A. Restivo, S. Salemi, *Periodicity and the golden
ratio*, Theoretical Computer Science 204 (1998), 153--167,
DOI `10.1016/S0304-3975(98)00037-1`.

At a cut labelled `3`, the orbit supplies a cube, so the threshold is
met.  At a cut labelled `2`, the proved information supplies an integer
square only.  Neither the proper circular fixed profile nor first-copy
fitting upgrades that square to exponent `phi^2`.

The calibrated Q21 audit makes the failure exact.  For

```
P=223222322232322232223
```

the code verifies primitivity, `pc_P=P`, and full first-copy fitting.
The orbit from `P` replays its initial symbols.  At total cut `24`, whose
phase in `P` is `3`, the curling number is `2`, and exhaustive
enumeration of every suffix and every finite-word period gives maximum
rational suffix exponent exactly

```
2 < phi^2.                                       (12)
```

Thus no phase-local conversion from the exact profile/fitting equations
to the Mignosi--Restivo--Salemi hypothesis is valid.

The fixed-origin delimiters also do not supply that conversion on their
own.  The construction in `recurrent_tower.md` gives primitive nested
roots `Q_i` with

```
Q_i^3 is a prefix of Q_(i+1),
the symbol after Q_i^3 in the limit is fixed,
|Q_(i+1)|/|Q_i| -> phi^3>3,
```

and its limit lies in the aperiodic Fibonacci subshift and contains no
fourth power.  It is therefore an explicit all-external S-adic model for
the delimiter geometry (9a).  By the cited threshold theorem, its
aperiodicity forces infinitely many prefixes whose maximum suffix
exponent is strictly below `phi^2`.  This model is not a curling orbit:
it fails the exact symbol/profile equality.  That failure is precisely
the hypothesis a future argument must use.

As a bounded strengthening of this negative control, executed code checks
the encoded Fibonacci tower roots of lengths `13,55,233`.  At every
circular phase their proper profile lies in `{2,3}`, they have full
first-copy fitting, and no proper fourth power occurs.  Their profile is
not equal to the encoded root.  These three rows are finite evidence, not
an unbounded theorem.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_cross_rank_tower_audit.py
```

## 5. Exact remaining gap

Repeated terminal-bottom-left transitions are therefore the existing
late reset tower with an additional strictly increasing terminal rank.
The two surviving mechanisms are:

1. an all-external S-adic chain in which every new root begins the old
   cube and delimiter;
2. a seed-anchored internal chain
   `Y=C^3` with one of finitely many initial-seed borders deleted.

Nested delimiters, primitivity, square coverage, fourth-power avoidance,
and geometric growth do not exclude the first mechanism.  The
golden-ratio theorem cannot be invoked until the label-two cuts are
upgraded from squares to `phi^2`-repetitions.  The exact
`pc_C=C` symbol alignment and the autonomous orbit equations are the
remaining load-bearing data; no theorem located in the searched
squareful/Sturmian literature performs that upgrade.

## 6. A profile-sensitive seam at an external child

The exact symbol/profile equality does give one new restriction which is
invisible in the Fibonacci delimiter model.

### Lemma (an external child copies at most one parent-tail symbol)

Let `P,Q` be primitive binary words over `{2,3}`, of lengths `p,q`, with

```
pc_P=P,                 pc_Q=Q,
P[0]=Q[0]=2,
Q begins P^3 3.                                      (13)
```

Let

```
lambda=lcs(Q,P^3).
```

Then

```
lambda<=1.                                           (14)
```

#### Proof

First note that an exact binary profile contains no circular factor
`333`.  If three consecutive positions were `3`, the proper unary cube
ending at the next cut would force that next profile symbol to be `3`.
There would then be four consecutive `3` symbols, giving a proper unary
fourth power at the following cut.  This contradicts the fact that every
symbol of `Q` is at most three.

For every cut

```
3p-lambda<=d<3p,
```

the length-`3p` circular factor of `Q^Z` ending at `d` is a cube of
root length `p`.  Its portion at nonnegative coordinates is
`P^3[:d]`.  Its portion before coordinate zero has length `3p-d` and,
by the definition of `lambda`, is the matching suffix `P^3[d:]` copied
from the end of `Q`.  These two portions concatenate to the required
three consecutive rotations of `P`.

The root length `p` is proper for `Q`, because (13) gives `q>3p`.
Exactness of `pc_Q=Q` therefore forces

```
Q[d]=3
```

at every displayed cut.  Since `d<3p`, equation (13) identifies this
letter with `P[d mod p]`.  If `lambda>=2`, the last two displayed cuts,
together with the delimiter, give

```
Q[3p-2:3p+1]=333.
```

This is the forbidden circular factor above, proving (14).

There is also an exact endpoint description.  If `lambda=1`, the last
displayed wrapping cube forces `P[-1]=3`, while the suffix equality gives
`Q[-1]=P[-1]=3`.  Conversely these two endpoint equalities give
`lambda>=1`, hence equality by (14).  Thus

```
lambda=1  iff  P[-1]=Q[-1]=3.                    (14a)
```

In every other case `lambda=0`.  In particular an external parent and
child cannot both end in `2`.

The lemma pinpoints why the actual-parent near-model in
`check_external_reset_tau_rank.py` fails.  Its child has length `80`,
its parent has length `21`, and their common terminal parent-periodic
suffix has length `25`.  The first forced wrapping parent cube ends at
phase

```
3*21-25=38,
```

which is exactly the checker's first profile failure: the child letter
is `2` while its proper circular profile is `3`, with root `21`.

By contrast, the partial length-`140` SAT near-model has common suffix
length one with its displayed Q21 parent cube.  It passes this seam and
first fails after the inherited marker.  Thus (14) is a genuine
profile-sensitive filter, not a closure: an all-external chain may keep
choosing fillers whose final symbol avoids the old periodic tail.
The next required theorem must constrain that separated filler using
its phase-zero square or its actual orbit provenance.

## 7. Phase-zero square: contained filler or strict Fine--Wilf gap

Retain the hypotheses of Section 6 and write

```
Q=P^3 3 E,             e=|E|,             q=3p+1+e.   (15)
```

Let `Z^2` be any suffix square of `Q` whose root `Z` is primitive, and
put `s=|Z|`.  First-copy fitting at phase zero guarantees that at least
one such square can be selected with

```
2s<=q-1.
```

The minus one is the deleted-first-copy fitting condition at phase zero;
the weaker bound `2s<=q` is not the exact critical condition.

There is an exhaustive alternative:

```
2s<=e+1;                                             (16a)

2s>e+1 and
s<q-2p-gcd(p,s).                                    (16b)
```

The first alternative says that the square starts at or after the
delimiter position `3p`; if `2s<=e`, it lies wholly in the filler.
The one-symbol equality case includes the delimiter as its first
symbol.  The second alternative is a strict two-period separation.

### Proof

Only (16b) needs proof.  Suppose `2s>e+1`, so the square interval

```
[q-2s,q)
```

overlaps the parent-periodic interval `[0,3p)`.  Their overlap has
length

```
L=3p-(q-2s)=2s-e-1.                                (17)
```

It has periods `p` and `s`.  Put `g=gcd(p,s)`.  If

```
L>=p+s-g,
```

Fine--Wilf gives period `g` on the overlap.  The overlap length is at
least both `p` and `s`; it therefore contains a full conjugate of the
primitive parent root `P` and a full conjugate of the primitive square
root `Z`.  Hence neither `g<p` nor `g<s` is possible, so

```
p=s=g.
```

The two period-`p` intervals then overlap in at least `p` symbols and
merge into one period-`p` interval through the delimiter.  It would
force

```
Q[3p]=Q[2p]=P[0]=2,
```

contrary to `Q[3p]=3`.  Thus the Fine--Wilf threshold is missed:

```
2s-e-1<p+s-g.
```

Substituting `q=3p+1+e` and rearranging gives (16b).

This classification still permits both live geometries.  A phase-zero
square may be manufactured entirely inside a long new filler, or a
crossing square may miss Fine--Wilf by the strict amount in (16b).
Neither case alone forces an internal reset.  The critical
factorization theorem supplies a critical *centered* local period, but
does not turn the suffix-square endpoints in (16a)--(16b) into a
covering of all centers; the existing midpoint-graph countermodels
prevent that unproved identification.

## 8. Exact phase-zero splice and the endpoint components

It is useful to absorb the delimiter into

```
D=3E,              d=|D|=e+1,
Q=P^3 D,           q=3p+d.                        (18)
```

The no-`333` observation in Section 6 completely describes the
`H_3` component containing the delimiter.

* If `P[-1]=3`, then `P[-2]=2`, the delimiter is the second symbol of
  a `33` component, and `D[1]=2` when that symbol exists.
* If `P[-1]=2`, the delimiter begins its component.  It is either a
  singleton followed by `2`, or the first symbol of `33`, followed by
  `2` when a further symbol exists.

The same observation makes every last `H_3` component of `E` have
length one or two.  Since `pc_Q(0)=Q[0]=2`, the terminal run of `2`
symbols after that component has length at most two: three terminal
`2` symbols would give a unary cube at phase zero.

Now choose a fitting suffix square `Z^2` at phase zero, and put
`s=|Z|`.  Thus

```
2s<=q-1.                                           (19)
```

Every such root is primitive, since a nonprimitive square root would
give a proper fourth power at a phase whose exact value is two.  If
`2s<=d`, the square begins at or after the delimiter and there is
nothing further to prove.  Suppose `2s>d`.  There are three exhaustive
center positions.

### 8.1 The center lies in the filler

Suppose

```
d/2<s<d,
alpha=d-s,             beta=2s-d=s-alpha.
```

Both `alpha` and `beta` are positive.  Direct comparison of the two
root blocks gives

```
D[alpha:s]=P^Z[-beta:0],
D[s:d]=D[:alpha].                                  (20)
```

Thus `D` has the proper border `D[:alpha]`, and the delimiter symbol
`D[0]=3` is copied to `D[s]=3`.  If the border reaches through the
exit of the first delimiter component, the complete component and its
exit are copied near the end of `D`; for a shorter border only its
initial part is copied.  This is the exact relation between the first
and last `H_3` data in this branch.

To verify (20), the square begins `beta` symbols before the delimiter
and its midpoint lies `alpha` symbols after it.  Its first root is

```
P^Z[-beta:0] D[:alpha],
```

while its second root is `D[alpha:d]`.  Equality of the first `beta`
and final `alpha` portions is precisely (20).

### 8.2 The center is the delimiter

If `s=d`, the two roots are

```
P^Z[-s:0],          D.
```

Hence `D=P^Z[-s:0]`, so `lcs(Q,P^3)>=s`.  Section 6 forces

```
s=d=1,             D=3=P[-1].                     (21)
```

This is the only centered landing allowed by the tail seam.

### 8.3 The center lies in the parent cube

Suppose `s>d` and put

```
delta=s-d>0.
```

The square midpoint is the parent phase `-delta`.  Splitting the two
roots at the delimiter gives

```
D=P^Z[-s:-delta],
P^Z[-s-delta:-s]=P^Z[-delta:0].                   (22)
```

The first equality forces

```
P^Z[-s]=3,             P[0]=2.                    (23)
```

Thus (22) is a literal `3/2` completion seam: the parent histories
immediately before phases `-s` and zero agree for `delta` symbols, but
their next prescribed profile symbols are respectively `3` and `2`.
If a cube root of length `rho` ends at phase `-s`, then

```
3 rho>delta.                                       (24)
```

Indeed, a cube with `3 rho<=delta` lies wholly in the common histories
in (22), so it translates to a proper cube ending at phase zero.  This
would contradict `pc_P(0)=2`.

Equations (20)--(24) are stronger than the numerical Fine--Wilf gap in
Section 7.  They still leave three live objects: a bordered filler, the
one-symbol landing (21), or an internal parent completion seam (22).

## 9. The shortest phase-zero root forces a robust square reset

Take `Z` to be the shortest maximizing root at phase zero.  Lemma 4 of
Chaffin--Linderman--Sloane--Wilks says that this root is unique and
primitive and, because the maximum exponent is two,

```
cn(Z)=1.                                           (25)
```

The external-child provenance supplies more than the circular equation.
The midpoint state

```
M=Q[:q-s]
```

is an actual state on the bad orbit, it emits the second copy of `Z`,
and

```
cn(M)=Z[0] in {2,3}.                               (26)
```

Let `C` be the shortest suffix of `M` whose curling number is at least
two.  Then

```
C=Y^2,             cn(C)=2,
cn(C[1:])=1,        cn(Y)=1,                       (27)
```

where `Y` is primitive.  Moreover, writing `r=|Y|`,

```
2r>s.                                              (28)
```

### Proof

Minimality gives `cn(C[1:])=1`.  Prefixing one symbol can raise a
curling number by at most one, so `cn(C)=2`.  In a maximizing
factorization `C=X Y^2`, a nonempty `X` would leave the same square
suffix after deleting the first symbol.  Therefore `X` is empty and
`C=Y^2`.  The root is primitive because otherwise `C` would have
curling number at least four.  CLSW Lemma 4 gives `cn(Y)=1`.

Both `C` and `Z` are suffixes of `M`.  If `|C|<=s`, then `C` is a
suffix of `Z`, forcing `cn(Z)>=2`, contrary to (25).  Hence
`|C|=2r>s`, proving (28).

There is also a reset whose first autonomous output matches the
context-forced replay.  Put `k=Z[0]` and choose the shortest suffix
`C_k` of `M` with curling number at least `k`.  The same one-symbol
argument gives

```
C_k=Y_k^k,
cn(C_k)=k,
cn(C_k[1:])=k-1.                                  (29)
```

Thus its autonomous orbit emits `k=Z[0]`, the first symbol of the
second copy.  Equation (29) does not say that it emits all of `Z`;
the executed examples below realize both immediate failure of the
square carrier and complete replay by the matching carrier.

The robust square has a useful delimiter dichotomy.  Its left edge is

```
a=q-s-2r,
```

which is

```
epsilon=2r-s>0                                    (30)
```

symbols to the left of the first copy of `Z` in `Z^2`.
If `s<d`, the midpoint lies in the filler.  Either the complete robust
square is filler-contained, in which case

```
d>=s+2r>2s,                                       (31)
```

or it crosses the delimiter.  In the crossing case its overlap with
`P^3` has length

```
L=s+2r-d
```

and periods `p,r`.  Fine--Wilf and the delimiter mismatch give the
strict gap

```
s+2r-d<p+r-gcd(p,r).                              (32)
```

For if the threshold were met, the overlap would contain complete
conjugates of both primitive roots.  A proper gcd would contradict
one of their primitivities.  The only remaining case is `p=r`; the two
period-`p` intervals would then merge through the delimiter and force
`D[0]=P[0]=2`, contrary to `D[0]=3`.

If `s=d`, the midpoint is exactly the old reset cut and (21) applies.
If `s>d`, the midpoint already lies in the parent cube and (22)--(24)
give the internal parent seam.  Consequently the shortest-root
argument always creates a genuine robust-square reset, but it does not
always create a new fixed-origin reset.

## 10. Iterating midpoint resets: landing or an explicit crossing

The preceding construction can be iterated without assuming that a
minimal square is maximizing at a label-three cut.  Start at

```
c_0=q.
```

While `c_i>3p`, let `Y_i^2` be the shortest suffix of the actual state
at cut `c_i` having curling number at least two, put `u_i=|Y_i|`, and
set

```
c_(i+1)=c_i-u_i.                                   (33)
```

Every `Y_i^2` satisfies the robust equations (27).  The positive
increments make (33) reach a first index `j` with `c_j<=3p`.

If `c_j=3p`, the previous square has one root on each side of the
delimiter, so

```
D[:u_(j-1)]=P^Z[-u_(j-1):0].                     (34)
```

This is exact landing at the earlier reset origin.

If `c_j<3p`, put

```
u=u_(j-1),
x=3p-c_j,
h=c_(j-1)-3p.
```

Then `x,h>=1`, `u=x+h`, and equality of the two square roots gives

```
P^Z[-u-x:-u]=P^Z[-x:0],
D[:h]=P^Z[-u:-x].                                 (35)
```

In particular

```
P^Z[-u]=3,             P[0]=2.                    (36)
```

This is the same explicit completion seam as (22), now for the first
midpoint square which crosses the delimiter.  Every cube root `rho`
at phase `-u` satisfies `3rho>x`, by the proof of (24).  The prefix
`D[:h]` copies the first delimiter `H_3` component as far as the
crossing reaches.  The tail bound `lambda<=1` does not compare this
filler prefix with the end of `Q`, so it does not exclude (35).

Saari's local minimal-square lemma gives, whenever both consecutive
midpoints stay on the filler side,

```
2u_(i+1)>u_i,
```

and makes the two root words prefix-comparable.  This inequality does
not provide a monotone scale.  For the exact critical word

```
223222322232322232223
```

the midpoint cycle

```
0 -> 17 -> 11 -> 7 -> 0
```

has root lengths

```
4,6,4,7
```

and positive edge deficits

```
2u_(i+1)-u_i = 8,2,10,1.
```

Their sum is `21`, so the lifted coordinate winds once around the
word.  Root length and the positive deficit both rise and fall.  A
landing-distance coordinate decreases only until (35), and a
delimiter-crossing count increases by one on every winding.  None is a
well-founded continuation past the crossing.

The same checker gives two exact context-forced replay calibrations.
For Q21, the shortest phase-zero root is

```
Z=2223,
```

and the robust carrier

```
C=(232223)^2
```

has deleted curling number one but autonomously emits all of `2223`.
For the exact critical word

```
223222322322232223232,
```

the shortest root is `Z=32`.  Its shortest square carrier is
`(2232)^2` and immediately outputs `2` rather than `3`, while the
matching carrier `(2232)^3` has deleted value two and autonomously
emits all of `32`.  Thus even complete critical replay permits both
carrier mismatch and full root replay.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_external_child_midpoint.py
```

## 11. Calibrated SAT boundary

The Boolean solver `z3_nested_replay_bool.py` fixes the Q21 parent
prefix `P^3 3` and imposes both the exact proper circular profile and
the first-copy fitting equation at every selected cut.

At child length `140`, imposing cuts only through `64` is satisfiable.
The executed model is the archived partial near-model used in Section 6,
and it has `lcs(Q,P^3)=1`.  Adding cut `65` makes the formula
unsatisfiable.  Imposing all `140` cuts is also unsatisfiable.  The
sparse delimiter core is unsatisfiable at every length `66` through
`90`.

These are bounded SAT statements, not a uniform nonexistence theorem.
No exact external child was produced.  The precise commands executed
after calibration were:

```
python research/z3_nested_replay_bool.py 140 --max-cut 64 --timeout-ms 120000
python research/z3_nested_replay_bool.py 140 --max-cut 65 --timeout-ms 120000
python research/z3_nested_replay_bool.py 140 --timeout-ms 120000
python research/z3_nested_sparse.py 66 90 --timeout-ms 5000
```
