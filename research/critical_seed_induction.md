# Critical deletion self-replay

This note assumes a hypothetical counterexample `P` whose first-symbol
deletion terminates and whose two orbits first differ only after the high
orbit has replayed `P` into a whole power.  It derives the exact residual
square-to-cube problem.  It does not prove termination.

## 1. Synchronization equations

Put `p=|P|`.  Suppose the two states at first divergence are

```
P^k
P[1:p] P^(k-1)
```

and their exact curling numbers are respectively `k` and `k-1`.  Before
that cut they appended the common word `P^(k-1)`.  Thus, for
`1<=a<=k-1` and `0<=j<p`,

```
cn(P^a P[:j]) = P[j],
cn(P[1:p] P^(a-1) P[:j]) = P[j].                 (1)
```

At the state `P^(k-1)`, equation (1) gives

```
cn(P^(k-1))=P[0].
```

The displayed word has a `(k-1)`-power suffix, so `P[0]>=k-1`.  It is
also a suffix of the low first-divergence state, whose curling number is
exactly `k-1`; suffix monotonicity gives the reverse inequality.  Hence

```
m:=P[0]=k-1.                                      (2)
```

For every phase `j`, the state `P^(k-1)P[:j]` ends in `k-1` copies of
the conjugate `P[j:]P[:j]`.  Equation (1) and (2) therefore give

```
P[j]>=m                                           (3)
```

at every position.  In particular `P[0]` is a minimum symbol of `P`.

## 2. Proper circular fixed profile

Let `pc_P(j)` denote the maximum exponent at phase `j` in `P^Z` among
roots of length strictly below `p`.  The first high replay in (1) shows
that `P P[:j]` has a proper root witnessing exponent `P[j]`: its total
length is below `2p`, so a root of exponent at least two cannot have
length `p` or more.  Thus

```
pc_P(j)>=P[j].
```

At a later replay cut, every proper circular power is visible in two
copies.  If a proper root of length `q<p` persisted for length at least
`p+q-gcd(p,q)`, Fine--Wilf would give a proper divisor period to a full
conjugate of the primitive word `P`.  Hence every proper circular power
has length below `2p`, and equation (1) at the third visible copy gives

```
pc_P(j)<=P[j].
```

Consequently

```
pc_P(j)=P[j]                                      (4)
```

for all phases.

## 3. The minimum is two

Equations (3)--(4) rule out `m>=3`.  If `m>=3`, every cut of the
two-sided periodic word `P^Z` ends in a cube whose root is shorter than
`p`.  After reversing the periodic word, every position begins in such a
cube.

Let `alpha=phi+1=(3+sqrt(5))/2`.  A cube has order `3>alpha`.  The
reversed word is therefore everywhere `alpha`-repetitive in the sense of
Kalle Saari, *Everywhere alpha-repetitive sequences and Sturmian words*,
European Journal of Combinatorics 31 (2010), 177--192,
DOI `10.1016/j.ejc.2009.01.004`.  Theorem 5.3 in the corresponding
thesis presentation of that result states that every everywhere
`alpha`-repetitive sequence is ultimately periodic.  Its proof chooses
the least period `N` of a longest minimal `alpha`-repetition and proves
that the tail is `N`-periodic.

Here every minimal `alpha`-repetition has least period below `p`.
Indeed, at its starting position choose a cube root `q<p`.  The prefix of
that cube of length `ceil(alpha*q)` is already an `alpha`-repetition and
has period `q`; the shorter minimal repetition has least period at most
`q`.  Therefore the period `N` produced in Saari's proof satisfies
`N<p`.

The reversed `P`-periodic word has primitive least period `p`.  An
eventual period `N` of a purely `p`-periodic word is a global period:
translate any requested index into the periodic tail by a multiple of
`p`, apply the tail equality at distance `N`, then translate back.
This contradicts `N<p`.  Therefore

```
P[0]=2,  k=3.                                    (5)
```

Every critical one-symbol maturation is a square-to-cube maturation.

## 4. Rotation of the terminating low branch

Write `P=2B`.  At first divergence the low state is

```
B P^2
```

and appends its exact curling number `2`.  The resulting word is

```
B P^2 2 = (B2)^3 = rot_left(P)^3.                 (6)
```

Thus the terminating low branch reaches the cube of the left rotation of
`P`.  In fact the synchronization equations say that this rotation has
autonomously replayed itself to that cube.  This gives a same-length
terminating rotation, not a shorter counterexample.

## 5. First post-promotion root

Put

```
C=P^3 3
```

and suppose `cn(C)=c>=2`.  Choose a primitive maximizing root `Z` of
length `q`.  Put `g=gcd(p,q)`.  Then

```
q<p,
(c-1)q+g<=p,
c<=3.                                             (7)
```

The equality `q=p` fails because the last two length-`p` blocks are
`P[1:]2` and `P[1:]3`.  If `q>p`, deleting the final artificial `3`
from the terminal square leaves a length `2q-1` factor in `P^3` with
periods `p` and `q`; Fine--Wilf gives a proper divisor period of `Z`.
Thus `q<p`.

Deleting the final symbol from the complete `c`-power gives a factor of
length `cq-1` with periods `p` and `q`.  Meeting the Fine--Wilf threshold
would make a full conjugate of `P` or a full copy of `Z` have period
`g`, contradicting primitivity.  Threshold failure is exactly the middle
inequality in (7).

Finally, the last `(c-1)q` symbols before the artificial `3` are a
`(c-1)`-power of a conjugate of `Z` ending at phase zero of `P`.
Equation (4) gives `c-1<=pc_P(0)=2`, proving `c<=3`.  If `c=3`, (7)
implies `q<p/2`.

The root blocks also give the exact internal-marker equations

```
Z=P[p-q+1:p] 3,
P[p-l*q]=3                  (1<=l<c).              (8)
```

At the cut immediately after the penultimate copied marker, the circular
word ends in `Z^(c-1)`.  Hence, with

```
b=P[p-q+1]=Z[0],
```

one has

```
b>=c-1,  equivalently c<=b+1.                     (9)
```

If `c=b`, the next appended symbol is the first symbol of `Z` and extends
the active `q`-periodic run.  If `c=b+1`, the artificial cut is an upward
one-symbol phase defect.  If `c<b`, every `b`-power witnessing the
internal profile cut must extend left of the visible suffix
`Z^(c-1)`; otherwise the same witness would occur at the artificial cut
and force `cn(C)>=b`.  These three cases are exhaustive.

An internal `3` does not by itself create a smaller critical maturation.
In the length-21 fixed profile, an exact first post-promotion root is
`Z=23`; rotating it to begin at the marker gives `32`, whose executed
curling number is one.

## 6. Exact remaining induction obstruction

At every actual post-promotion cut before `p` further outputs have been
appended, no primitive maximizing root can have length at least `p`.
The proof and exact crossing equations are in
`post_promotion_escape.md`.

This makes the following finite-window assertion the next precise target:

> If the first `p` outputs after `P^3 3` all avoid one, then those outputs
> form a circular rotation of `P`.

The assertion survives all generated exact models, but is not proved.
For the binary length-21 profile, exhaustive execution over all
minimum-start rotations leaves one full-window survivor.  Starting with
the rotation

```
223232223222322322232
```

the first 21 post-promotion outputs are the rotation

```
222322232232223222323.
```

This example also blocks a root-length induction.  Immediately after
promotion its only maximizing root has length two, but before termination
a maximizing root has length 38, exceeding `p=21`; the first `1` occurs
only after 59 non-one post-promotion outputs.  All values and root sets are
recomputed by both implementations in `curling.py` by
`check_critical_seed_induction.py`.

Thus the strict first-step root drop is genuine but not well founded.
The missing lemma must turn the collection of short copy pointers during
the first `p` cuts into one contiguous circular phase of `P`.  Root
length bounds alone allow the pointers to switch among different
occurrences of the marker.

## 7. Exact normal form at the first loss of circular phase

There is a sharper description of any putative failure of the finite-window
assertion.  Let

```
A=P^3 U,                 e=|U|,
k=cn(A),
B=A k,                   ell=cn(B)>=2.
```

Assume that `U` is a circular factor of `P`, but `U k` is not.  This is
the first-factor-loss situation, although the argument only uses the two
displayed factor statements.  Suppose also that every primitive maximizing
root of `B` has length below `p`, as supplied by the post-promotion escape
lemma.  Choose such a root `Y` of length `q`.

Then

```
q<=e,
U[e-q]=k,
Y=U[e-q+1:e] k.                                (10)
```

Indeed, if `q>=e+1`, the final root block contains the whole word `U k`.
The preceding equal root block contains an equal copy shifted left by `q`.
That copy lies wholly before the start of `U`, hence in `P^3`; it would
make `U k` a circular factor of `P`, contrary to the hypothesis.  Thus
`q<=e`.  Equality of the terminal symbols in the last two root blocks
then gives `U[e-q]=k`, and the last equality in (10) is just the explicit
form of the final root block.

Put

```
Z=U[e-q+1:e],        so Y=Z k.
```

For every circular occurrence

```
U=P^Z[a:a+e]
```

write `b=P^Z[a+e]`.  Nonextendibility says `b!=k`, while (10) gives the
exact one-letter defect

```
P^Z[a+e-q+1:a+e+1] = Z b,
actual final root                 = Z k.          (11)
```

Thus the first loss of phase cannot be an arbitrary new block.  It changes
only the last letter of a length-`q` block whose preceding occurrence of
that new letter is exactly `q` positions earlier.

There are two further consequences.  Deleting the final `k` from the
terminal power `(Z k)^ell` leaves

```
A ends in (k Z)^(ell-1).                         (12)
```

Hence `k>=ell-1`.  If `(ell-1)q<=e`, equation (12) lies wholly in `U`
and transports to every circular occurrence above, giving

```
b>=ell-1.                                        (13)
```

Finally, if `q` is chosen least among all maximizing roots of `B`, then

```
cn(Y)<=ell-1.                                    (14)
```

For if `cn(Y)>=ell`, a strictly shorter root inside `Y` would also attain
the exact maximum `ell` at the suffix of `B`, contradicting leastness of
`q`.  In particular, when `ell=2`, the first lost phase produces an
explicit shorter autonomous reset word:

```
cn(Y)=1,       |Y|=q<p.                           (15)
```

The old mismatch is also forced to cross the matched phase.  If one of
the continuation labels `b` in (11) satisfies `b<k`, every maximizing
`k`-power of `A` has powered length greater than `e`; otherwise that power
would lie in `U` and occur at the circular cut, forcing `b>=k`.  Dually,
if `b>k`, every circular `b`-witness at that occurrence has powered length
greater than `e`; otherwise it would occur at the suffix of `A` and force
`cn(A)>=b`.

For the length-21 fixed profile, all five rotations whose first phase loss
is an upward `2 -> 3` defect have `ell=2` and least reset-root length one;
the following curling number is one.  This last
two-step death is an executed property of that profile, not a consequence
of (10)--(15).  The unproved residual statement is that a succession of
the one-letter defects (11), with each reset word governed by the complete
fixed profile, cannot avoid an autonomous-one reset indefinitely.

## 8. A two-period locking radius

Although a short circular match can be lost as in Section 7, a match of
length `2p` cannot be lost while the post-promotion root bound remains in
force.

Precisely, suppose a finite state `A` has a suffix of length `L>=2p`
equal to the length-`L` factor of `P^Z` ending at phase `j`.  Assume every
primitive maximizing root of `A` has length below `p`.  Then

```
cn(A)=P[j].                                      (16)
```

For the lower bound, a proper circular power attaining `P[j]` has total
length below

```
p+r-gcd(p,r)<2p
```

when its root length is `r<p`.  It is therefore visible in the common
suffix, and `cn(A)>=P[j]`.

For the reverse inequality, suppose `cn(A)=a>P[j]`, and take a primitive
maximizing root of length `q<p`.  If `a q<=L`, its whole power lies in the
common suffix and would give the circular phase exponent at least `a`.
If `a q>L`, the common suffix itself has periods `p` and `q`.  Its length
meets the Fine--Wilf threshold

```
L>=2p>=p+q-gcd(p,q).
```

It consequently has period `gcd(p,q)<p` and contains a complete
length-`p` conjugate of `P`, contradicting primitivity.  Both alternatives
contradict `a>P[j]`, proving (16).

After appending the value in (16), the circular match extends by one
symbol.  Induction therefore locks the orbit to that phase for as long as
all maximizing roots remain shorter than `p`.  In particular, during the
first post-promotion window the only unresolved part is the interval before
the best circular suffix match first reaches length `2p`; the escape lemma
then supplies the required root bound at every subsequent cut.

## 9. Maximum-label backchains

There is an exact descent at the level of the maximum symbol, although it
does not yet close under autonomous replay.  Let

```
M=max_j P[j],
```

and let a phase `j` with `P[j]=M` have a primitive maximizing proper root
`Y` of length `q<p`.  Thus `P^Z` ends in `Y^M` at cut `j`.  At the source
cut `j-q` it ends in `Y^(M-1)`, so

```
P[j-q] in {M-1,M}.                              (17)
```

Moreover every symbol of `Y` lies in `{M-1,M}`.  To verify this, take a
cut through the final copy of `Y`.  The preceding suffix consists of
`M-1` copies of the corresponding conjugate of `Y`, so the fixed profile
at that cut is at least `M-1`; maximality of `M` supplies the upper bound.

Starting at any `M`-phase, repeatedly choose a primitive maximizing
`M`-root and move backward by its root length.  Equation (17) either
reaches an `(M-1)`-phase or stays at an `M`-phase.  If `M>=4`, it must
eventually reach `M-1`.  Otherwise finiteness of the phase set gives a
repeated `M`-phase.  Lift the successive phases to integers

```
j_(i+1)=j_i-q_i.
```

Between the two occurrences of the repeated phase, the positive sum of
the `q_i` is a positive multiple of `p`.  Every contiguous interval
`[j_(i+1),j_i)` is an `M`-root and hence consists only of symbols at
least `M-1`.  Their concatenation covers one or more complete periods of
`P`, forcing every symbol of `P` to be at least `M-1>=3`.  This
contradicts the proved minimum value two.

Consequently, for `M>=4` there is a primitive word `Y`, of length
`q<p`, such that

```
Y[0]=M-1,
Y uses only {M-1,M},
cn(Y^(M-1))=M-1,
cn(Y^M)=M.                                       (18)
```

The two finite curling-number equalities need a root-length check because
the circular profile excludes roots of length at least `p`.  A root
shorter than `p` giving exponent `M` at `Y^(M-1)` would contradict the
circular value `M-1` at the source.  A root of length at least `p` cannot
fit `M` copies in a word of length `(M-1)q<(M-1)p`.  This proves the first
equality.  The same argument with exponent `M+1` proves the second.

There is also an exact audit of the intermediate replay.  Put

```
L_t=Y^(M-1)Y[:t],             0<=t<q.
```

The last `(M-1)q` symbols of `L_t` are `M-1` copies of a conjugate of
`Y`.  Comparison with the circular context, including the same
root-at-least-`p` length exclusion, gives

```
M-1 <= cn(L_t) <= Y[t].                         (19)
```

Thus every `(M-1)` symbol of `Y` is replayed autonomously.  At a symbol
`Y[t]=M`, the local value is either `M-1` or `M`; only the latter replays
the symbol.

The context-masked alternative in (19) has a sharp scale cost.  Suppose
`cn(L_t)=M-1`, and let `r<p` be a primitive circular `M`-root at that
phase.  Put `g=gcd(q,r)`.  The `r`-power must cross the whole finite
prefix, so

```
M r > (M-1)q+t.
```

The common suffix of length `(M-1)q+t` has periods `q` and `r`.
Fine--Wilf and primitivity show that either

```
r=q,
```

or the threshold must fail, which is exactly

```
r > (M-2)q+t+g.                                 (20)
```

For if the threshold held and `g<q`, a complete conjugate of the
primitive word `Y` would have period `g`; if `g=q<r`, the overlap would
contain the complete primitive `r`-root and give it the proper divisor
period `q`.  These exhaust the unequal-root cases.

Equations (18)--(20) isolate the obstruction to induction on the maximum
symbol.  The endpoint maturation is genuinely shorter, and all low
symbols replay.  A missing internal `M` either uses the same root scale or
is supplied by a root more than `(M-2)` times as large.  What is not yet
proved is that recursively adjoining those context-masked `M`-witnesses
produces a shorter circular fixed profile rather than a finite hierarchy
whose largest roots cross the left boundary of `Y^(M-1)`.

## 10. Ancestry of the first promoted marker

The first appended `3` carries more structure than an arbitrary occurrence
of the symbol `3`.  Let

```
C=P^3 3,
c=cn(C)>=2,
```

and let `Z` be a primitive maximizing `c`-root of length `q<p`.  Use
coordinates in which the appended marker occupies position `n=3p`.
Equality of the last two `Z` blocks copies that marker from the position

```
u=n-q.
```

Thus, in circular coordinates,

```
a=p-q,
P[a]=3.                                          (21)
```

Fixedness now supplies a fact absent from a merely symbol-matching
near-model: immediately before this parent marker, `P^Z` ends in a proper
cube.  Let `V^3` be such a cube with primitive root length `r<p`.  The
usual proper-period Fine--Wilf bound gives

```
2r+gcd(p,r)<p.                                   (22)
```

The outgoing copy distance and the incoming cube scale obey

```
q<=3r.                                           (23)
```

To prove (23), suppose `q>=3r+1`.  The preceding length-`q` copy of `Z`
contains the whole interval `V^3` immediately before its final parent
marker.  Translation by `q`, using equality of the two `Z` blocks, puts
an equal proper `r`-cube immediately before the appended marker.  That is
a proper circular cube at phase zero of `P`, contradicting
`pc_P(0)=P[0]=2`.

This also gives a useful overlap split.  The final `q-1` symbols before
the appended marker are an exact copy of the final `q-1` symbols before
the parent marker.  Therefore, if

```
q>=2r+1,
```

phase zero ends in the proper square `V^2`; its proper circular value is
exactly two.  The sharp boundary of (23) has a complete normal form.  If

```
q=3r,
```

then

```
Z=V^3[1:] 3,
cn(V^3)=3,
cn(V^3[1:])=2.                                  (24)
```

The word identity follows because the preceding `q`-block is exactly the
cube with its first symbol deleted, followed by its marker.  For the
curling numbers, `V^3` occurs at a circular phase of exact value three and
has length `q<p`, so no excluded root of length at least `p` can alter its
finite value.  Its first-symbol deletion ends in `V^2`, giving value at
least two; it is copied to phase zero, whose proper value is two, and its
length is again below `p`, giving the reverse bound.

Thus the marker has a genuine two-sided ancestry:

```
global incoming cube scale p
        -> outgoing copy scale q
        -> circular incoming cube scale r,

q<=3r,       2r+gcd(p,r)<p.                      (25)
```

At equality, (24) is a strictly shorter exact deletion-critical pair.
The inequality is not a monotone descent in general: the length-21 fixed
profile realizes `q/r` equal to `1/4, 1/2, 3/4, 1, 3/2, 7/4, 2,
5/2`, and `3` across its phase-zero rotations and maximizing roots.
Consequently a proof must use repeated marker ancestry or the synchronized
continuation, not only the single-scale bounds in (25).

The incoming-cube condition at one parent marker is still not sufficient.
The executed primitive local model

```
P=23232332223232
```

has proper circular values `2,3,2` at phases `0,6,7`, respectively.
Thus phase zero has the required low value, the marker at phase six is
genuinely cube-born, and its circular next label is two.  Nevertheless,
after the exact global birth at `P^3`, the state `P^3 3` has value three
rather than that circular two, and its exact subsequent values through the
first one are

```
3,2,2,2,3,2,2,2,3,2,2,2,3,3,2,1.
```

So even a genuine incoming cube does not force the `3,2,1` death seen in
the short length-21 branches.  This model is not a circular fixed profile;
it demonstrates that a successful ancestry argument has to use the fixed
equations at later copied markers as well, not only at the first parent.

## 11. Two-context synchronization and the last-marker seam

Let two finite contexts have a common suffix of length `L` and the same
exact curling number `k>=2`.  Let their least primitive maximizing-root
lengths be `r` and `s`.  Then either

```
r=s,
```

or all three strict inequalities hold:

```
k r>L,
k s>L,
L<r+s-gcd(r,s).                                  (26)
```

If, for example, `k r<=L`, the `r`-power is visible in both contexts.
The other least root has length at most `r`, so its complete power is also
visible in both contexts; leastness in the first context gives the reverse
inequality, hence equality.  This proves the first two strict inequalities
when the roots differ.  Their powers then both cover the whole common
suffix, which has periods `r` and `s`.  At or beyond the Fine--Wilf
threshold, that suffix contains a complete terminal root of each length.
The gcd period would make one of the two roots imprimitive unless
`r=s`, proving the last inequality.

At a first output divergence, if one context has value `h` and the other
has a smaller value, every maximizing `h`-root on the high side satisfies

```
h r>L.                                           (27)
```

Otherwise the high power would be wholly common and would force value at
least `h` on the low side.  Equations (26)--(27) are the exact two-stack
constraint: differing root decorations, and the root causing the first
symbol loss, must cross the entire synchronized suffix.  They also explain
the two-period locking lemma: once a shared suffix is long enough for all
eligible roots, the decorations cannot differ.

There is a sharper seam statement in the `{2,3}` core.  Consider a first
upward `3` versus `2` loss.  Start at the last synchronized marker `3`
before the loss, and suppose the `d` intervening matched symbols are all
`2`.  If the high cube has primitive root length `r`, then

```
r>d.                                             (28)
```

For if `r<=d`, its final root lies wholly in the run `2^d`, so the root is
`2^r`.  Primitivity forces `r=1`.  When `d>=3`, the terminal unary cube is
wholly common and contradicts the low value two.  When `d` is one or two,
the last marker `3` prevents the high context itself from ending in three
twos.  These cases exhaust `r<=d`.

Thus tracing a crossing cube backward through its root copies either
encounters an earlier synchronized marker and restarts with a strictly
shorter marker-to-loss distance, or reaches the last-marker seam with the
entire matched run shorter than one root.  For all five upward phase losses
in the length-21 profile the reduced seam is immediate (`d=0`), with
incoming cube-root lengths `10,3,7,2,6`.  The seam reduction is
well-founded in the distance `d`, but the seam case itself is not closed:
the local marker model in Section 10 also has `d=0` and survives fifteen
non-one outputs.  Full fixed ancestry of the earlier markers inside the
crossing root remains load-bearing.

## 12. A wrapping maximum cube forces a half-scale internal cube

There is a useful global consequence of fixedness that is invisible in a
single-marker local model.  Assume in this section that the proper circular
fixed profile `P` uses only the symbols `{2,3}`.  Let `p=|P|`, and choose,
among every proper cube witnessing a phase of value three, a primitive root
`V` of globally maximum length `r`.  Rotate circular coordinates so that

```
P^Z[0:3r]=V^3.
```

The cube ends at cut `3r`, so fixedness gives

```
P^Z[3r]=3.                                      (29)
```

Suppose the cube wraps around one period, so `3r>=p`.  Put

```
ell=3r-p,             g=gcd(p,r)=gcd(ell,r).
```

The proper-period Fine--Wilf bound for `V^3` is

```
2r+g<p.
```

Consequently

```
1<=ell<r,             g+ell<r.                  (30)
```

Coordinates `p,...,3r-1` are simultaneously the final `ell` symbols of
`V^3` and the first `ell` symbols of the next circular copy of `P`.
Therefore

```
V[0:ell]=V[r-ell:r].                            (31)
```

Also, `3r` has circular phase `ell`; equations (29) and (31) give

```
V[ell]=3.                                       (32)
```

Now inspect the occurrence of the same symbol in the third copy of `V`.
It is at coordinate

```
E=2r+ell<3r.
```

At cut `E`, fixedness and (32) supply a primitive proper cube `S^3`.
Write `s=|S|`.  Global maximality of `r` gives `s<=r`.

First suppose `3s>E`.  The intervals of `S^3` and `V^3` then overlap on
`[0,E)`, a word of length

```
E=2r+ell>=2r
```

having periods `s` and `r`.  This length meets the Fine--Wilf threshold
`r+s-gcd(r,s)`.  If `s<r`, the resulting gcd period is a proper divisor
period of a complete copy of `V` in the overlap, contradicting the
primitivity of `V`.  Hence this crossing alternative would force `s=r`.

When `s=r`, the two length-`3r` cubes ending at cuts `E` and `3r` overlap
in at least one whole root.  Their union

```
[ell-r,3r)
```

is therefore `r`-periodic and has length `4r-ell`.  It is also a factor
of the `p`-periodic word `P^Z`.  The Fine--Wilf threshold for periods
`p,r` is

```
p+r-g = 4r-ell-g,
```

which is strictly below the union length.  Thus the union has period
`g<r` and contains a complete copy of `V`, again contradicting
primitivity.  The crossing alternative is impossible, so

```
3s<=E.                                          (33)
```

The whole cube `S^3` consequently lies inside `V^3`.  It has periods `s`
and `r`.  Put `d=gcd(r,s)`.  If its length meets the Fine--Wilf threshold,
then either `d=s`, meaning `s` is a proper divisor of `r`, or `S` is
imprimitive.  If the threshold is not met, its exact failure is

```
2s+d<r.
```

The imprimitive alternative is excluded, and `s=r` is excluded by (33)
and `ell<r`.  Hence the two surviving cases both give

```
s<=r/2.                                         (34)
```

The marker following this internal cube makes

```
C=S^3 3
```

a nonwrapping circular factor.  Equations (30) and (34) imply

```
|C|=3s+1<p.                                     (35)
```

Thus a wrapping maximum-scale cube cannot be the only high-period
structure.  It forces an explicitly located marker cube at at most half
the root scale, and that smaller cube together with its marker is a
proper factor of `P`.

This is a genuine finite descent in cube-root length, but it is not yet a
termination proof.  Repeating the descent can end at the legal unary
configuration `2^3 3`; its standalone curling number is one.  The
circular profile can rescue the following value by a square or cube whose
power crosses the whole short factor, so the next ancestry edge may jump
back to a larger scale.  The resulting object is a finite ancestry tree,
not a monotone chain.  A closing argument would have to prohibit those
scale-increasing rescue edges or show that their overlap intervals force a
proper period of `P`.

## 13. Maximal periodic runs remove the wrapping hypothesis

The half-scale conclusion does not actually require the maximum cube to
wrap around the chosen period boundary.  Continue to assume a binary
proper fixed profile.  Let `r>1` be the globally largest primitive
cube-root length, and let `I` be a maximal `r`-periodic interval in
`P^Z` containing an `r`-cube.

The interval is finite because `P` is primitive.  It also has length
strictly below `4r`: an `r`-periodic factor of length `4r` would end in an
`r`-root fourth power, forcing a circular profile value at least four.
Translate coordinates so that the left endpoint of `I` is zero.  Its
first `3r` symbols have the form

```
V^3
```

for a primitive conjugate `V` of the original root.  Since `r>1` and the
alphabet is binary, `V` contains a `3`; fix an offset `0<=t<r` with
`V[t]=3`.

The occurrence of that marker in the third copy is at cut

```
E=2r+t.
```

Fixedness supplies a primitive cube `S^3` ending there.  Put `s=|S|`.
Global maximality gives `s<=r`.

If `S^3` crossed the left endpoint of `I`, its overlap with `V^3` would
be `[0,E)`, of length at least `2r`, with periods `r` and `s`.
Fine--Wilf would make a complete copy of `V` have period
`gcd(r,s)`.  For `s<r` this contradicts primitivity, so crossing would
force `s=r`.  In that case the two `r`-periodic intervals overlap in
more than one root and glue to an `r`-periodic interval extending
strictly left of zero, contradicting the maximal choice of `I`.

Thus `S^3` lies wholly inside `I`, and in fact wholly inside the displayed
prefix `V^3`.  The same internal Fine--Wilf calculation as in Section 12
gives

```
s divides r,  or  2s+gcd(r,s)<r.
```

Since `s=r` cannot fit before `E<3r`, both alternatives imply

```
s<=r/2.                                         (36)
```

Every nonunary globally maximum cube therefore contains a fixed-profile
marker whose incoming cube has at most half the root length.

For a cube root `r` that is not globally maximum, the identical
maximal-run construction gives the exact dichotomy

```
s<=r/2,    or    s>r.                            (37)
```

In the increasing case the child cube must cross the left endpoint.  If
the chosen marker has offset `t`, failure of the Fine--Wilf threshold is

```
s>r+t+gcd(r,s).                                 (38)
```

One may choose the last `3` in `V`.  Four consecutive `2`s are impossible
in a binary fixed profile, so this choice has `t>=r-4`; equation (38)
then makes every increasing edge nearly double its parent scale.

Equations (36)--(38) still permit alternating decreases and rescue
increases.  The proof above controls root lengths but does not make the
corresponding periodic intervals nested: after a half-scale embedded
child is selected, its own maximal periodic interval can extend outside
the parent interval.  Therefore iterating (37) produces a finite directed
ancestry graph, potentially with cycles, rather than a well-founded
descent.  Any use of (36) as an induction must additionally control this
interval displacement.
