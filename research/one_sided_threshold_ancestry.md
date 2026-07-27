# One-sided threshold ancestry and the bounded pointed cube

This note works inside one hypothetical nonterminating orbit.  It proves a
uniform bound on every threshold component above `2`, bounds every
maximizing root at a label at least `4`, and gives an exact finite-return
description of every sufficiently long label-three cube.  The description
retains one bounded pointed overhang.  A suffix-duplication construction
shows why ordinary return-word or ancestry arguments do not remove that
overhang without using more of the exact orbit profile.

The results are natural-language proofs, not Lean 4 formalizations.  They
are therefore `PROVED-NL` in the research ledger and are not `VERIFIED`
claims for the final report.

## 1. Setup and literature boundary

Index the one-sided orbit word `T` from zero.  A cut `d` means the prefix

```
T[0:d].
```

Once `d` is beyond the seed,

```
T[d]=cn(T[0:d]).                                      (1)
```

Lemma 1 of `reductions.md` puts every appended value of a hypothetical
counterorbit in a finite set.  Choose `N` beyond the seed and beyond the
last occurrence of every transient appended value.  Write `M` for the
largest recurrent value.  Then

```
T[d] in {2,...,M}       for every d>=N.                (2)
```

Lemma 5 of `reductions.md`, using the
Mignosi--Restivo--Salemi golden-ratio periodicity criterion, proves that
the value `2` occurs infinitely often.

For `k>=3`, an `H_k` component is a maximal nonempty consecutive block of
letters at least `k`.  An exit of such a component has the form

```
T[d-ell-1:d]=C e,     |C|=ell,     C[i]>=k,     e<k,   (3)
```

where `C` is maximal immediately before `e`.  The exit cut is `d`.

The literature search preceding this argument is recorded in
`literature_search_log.md`.  Vuillon's return-word characterization of
Sturmian words shows that finite return multiplicity is compatible with
aperiodicity.  First-return prefix-code and circular-code results decode
words whose initial boundary is already known; they do not move a boundary
backward across a partial return.  Bognini--Kaboré--Ouedraogo prove that
maximal-suffix duplication can itself generate the Fibonacci word.  None
of these results converts the ancestry below into periodicity.  The
project-specific statements therefore retain the cut coordinates and the
unmatched initial return.

## 2. Every high-threshold component is uniformly bounded

### Theorem 1 (one-sided exit-parent bound)

Fix `k>=3`.  Every `H_k` component whose exit cut is at least `N` has
length strictly below `N`.

### Proof

Take the exit (3).  By (1)--(2), the cut has a maximizing factorization

```
T[0:d]=Q Y^a,       a=T[d]>=2,       r=|Y|.           (4)
```

The final letter `e` of the last copy of `Y` is copied one root length to
the left, to coordinate

```
d-r-1.                                               (5)
```

If `r<=ell`, coordinate (5) lies in the interval occupied by `C`.  Its
letter would then be both `e<k` and a letter of `C`, where every letter is
at least `k`.  Therefore

```
r>=ell+1=|C e|.                                      (6)
```

The complete marker `C e` lies in the last root block in (4), so the
preceding root block contains an equal copy ending at the cut

```
u=d-r.                                               (7)
```

At `u`, let `C'` be the maximal `H_k` component immediately before the
copied `e`.  It contains the copied `C`, and hence

```
|C'|>=|C|.                                           (8)
```

The final two root copies in (4) fit in `T[0:d]`, so `2r<=d`.  Equations
(7) and `d=u+r` give

```
1<=r<=u<d.                                           (9)
```

If `u>=N`, apply the same construction to the exit at `u`.  Every step
strictly decreases the nonnegative integer cut, while (8) makes component
length weakly increase in the backward direction.  The iteration reaches
an exit cut `q<N`.  The component before its exit symbol occupies
coordinates in `[0,q-1)`, so its length is at most `q-1<N`.  The original
component length is at most that terminal length by all the inequalities
(8).  This proves `ell<N`.

### Corollary 2 (no missing infinite component)

Every `H_k` component in the tail is finite, and all components exiting
after `N` have length below `N`.

### Proof

The infinitely many occurrences of `2` supplied by Lemma 5 of
`reductions.md` lie outside `H_k` for every `k>=3`.  Thus no `H_k`
component can occupy a final infinite suffix.  Theorem 1 applies at the
exit of each remaining late component.

## 3. The exit-parent forest has stabilized-marker rays

Choose one maximizing root at each late `H_k` exit and direct the exit to
the earlier exit `u` in (7).  Reverse these edges when viewing descendants:
an earlier exit `u` is a parent of a later exit `d`.

This forest is locally finite.  If `u` is the parent of `d`, then
`r=d-u`, and `2r<=d=u+r` gives

```
d<=2u.                                               (10)
```

For fixed `u`, only finitely many integer cuts satisfy (10).  All backward
chains enter the finite set of exits below `N`.  If there are infinitely
many late exits, one of those finite anchors has infinitely many
descendants.  At least one child of that anchor has infinitely many
descendants, since it has finitely many children.  Repeating this selection
constructs an infinite forward ray.

The exit color `e` is copied unchanged along every edge.  In the forward
direction, (8) says that component lengths are weakly decreasing.  A
weakly decreasing sequence of positive integers becomes constant.  Once
the lengths are equal, the child component is a suffix of the parent
component of the same length, so the two component words are equal.
Consequently every infinite ray eventually carries one exact fixed marker

```
F=C e.                                                (11)
```

This is stronger than the circular parent-cycle monotonicity in
`maximum_threshold_root_graph.md`: the fixed left origin forces every
backward chain into the finite prefix.  It does not bound the distances
between successive vertices on a forward ray.

## 4. Maximizing roots at labels at least four are bounded

### Theorem 3 (high-label root bound)

Let `d>=2N`, let `a=T[d]>=4`, and choose any maximizing factorization

```
T[0:d]=Q Y^a,       r=|Y|.
```

Then

```
r<N.                                                 (12)
```

### Proof

The displayed power fits, so `2r<=d` and

```
d-r>=N.                                              (13)
```

Write `Y=A B` with `|A|=t`, where `0<=t<r`, and consider the cut

```
j=d-r+t.
```

Immediately before this cut, the last `a-1` complete copies followed by
`A` satisfy

```
(A B)^(a-1) A = A (B A)^(a-1).                      (14)
```

Thus `T[0:j]` has the suffix `(B A)^(a-1)`.  Equations (1) and (13)
give

```
T[j]=cn(T[0:j])>=a-1.                                (15)
```

As `t` ranges from `0` to `r-1`, these cuts read every letter of the
final copy of `Y`.  Hence every letter of `Y` is at least
`a-1>=3`.  The whole root lies inside one `H_(a-1)` component.  Corollary
2 makes that component finite, and Theorem 1 bounds its length below
`N`.  Therefore `r<N`.

Lemma 4 of `reductions.md` proves that the least maximizing-root lengths
of a counterorbit are unbounded.  Theorem 3 consequently confines all
such unboundedness to cuts labelled `2` or `3`.  It does not by itself
prove that the label-three subfamily is unbounded.

## 5. A finite marker alphabet at threshold three

Assume `M>=3`.  Every late `H_3` component is a word over
`{3,...,M}` of length in `{1,...,N-1}`.  There are therefore finitely
many possible component words.

A run of appended `2` values has length at most three.  If three
consecutive values are `2`, the prefix after the third ends in the unary
cube `2^3`, so its next curling number is at least three.  No fourth `2`
can follow.

Put a boundary immediately after the first `2` following each `H_3`
component.  If `b_i<b_(i+1)` are consecutive late boundaries, then

```
T[b_i:b_(i+1)] = 2^q C 2,
q in {0,1,2},       1<=|C|<N.                       (16)
```

These raw returns form a finite alphabet, and every return has length at
most

```
L=N+2.                                               (17)
```

The complete local marker at the right boundary in (16) is

```
2 C 2.                                               (18)
```

The leading `2` in (18) is the last `2` before `C`; the trailing `2` is
the first `2` after `C`.  Thus an occurrence of (18) determines its
component and its exit boundary without consulting symbols outside the
occurrence.

## 6. A long label-three cube contains an aligned token square

### Theorem 4 (bounded pointed-start normal form)

There is a constant `R`, depending only on the finite initial prefix and
`N`, with the following property.  Suppose a label-three cut has a
maximizing cube

```
T[x:x+3r]=Y^3,       |Y|=r,       d=x+3r,            (19)
```

and `r>R`.  Then there are nonempty or possibly empty raw words `U,V` and
a word `Z` such that

```
Y=U V,
Z=V U,
|U|<=R,
Y^3=U Z^2 V,                                         (20)
```

and each copy of `Z` in (20) is the same concatenation of complete return
tokens from (16).

### Proof

Fix one late boundary `b_*`.  Consecutive boundaries after `b_*` have
gaps at most `L` by (17).  Given `x`, choose the first boundary
`b_0>x` at or after `b_*`, and let `b` be its successor.  If
`x>=b_*`, then `b-x<=2L`; if `x<b_*`, then `b-x<=b_*+L`.  Set

```
R=max(2L,b_*+L).                                     (21)
```

The complete marker ending at `b` starts no earlier than `b_0-1`, so it
lies wholly to the right of `x`.  Since `b-x<=R<r`, it also lies wholly
inside the first root copy in (19).

The period `r` equality in (19) translates this complete marker to equal
occurrences ending at

```
b+r       and       b+2r.                            (22)
```

Because the marker includes both flanking `2` values, all three endpoints
in (22) are genuine boundaries of the decomposition (16).

Put `s=b-x`, and split

```
U=T[x:b],       V=T[b:x+r].
```

Then `Y=U V`, `|U|=s<=R`, and the word from `b` to `b+2r` is

```
(V U)^2.
```

Set `Z=V U`.  Its start, midpoint, and endpoint are the boundaries
`b,b+r,b+2r`.  Every additional boundary inside its first copy translates
by `r` to a boundary inside its second copy, and the inverse translation
does the reverse.  Hence the two equal raw copies have the same exact
return-token decomposition.  The identity

```
(U V)^3 = U (V U)^2 V
```

proves (20).

### The pointed defect

The cube in (19) determines only two aligned copies of `Z`.  A third copy
starting at `b` would end at

```
b+3r=d+s,                                            (23)
```

which uses `s` symbols after the cube endpoint.  Rotating the other way
would require symbols before `x`.  Neither extension follows from the
equality (19).  Thus all root copies synchronize after a bounded offset,
but one pointed overhang `U` remains at the left and the matching
overhang `V` remains at the right.  First-return code theorems decode the
middle square; they do not supply the missing equality across (23).

### Corollary 5 (the cube scale becomes an exact label-two parent edge)

Use the complete marker `2 C 2` ending at `b` in the proof of Theorem 4,
and put

```
p=b-1.
```

The letter at `p` is the trailing `2` of the marker.  Its two translates
at `p+r` and `p+2r` are also `2`.  The cube equality gives

```
T[p:p+2r] = T[p:p+r]^2.                              (24)
```

At the cut

```
v=p+2r,
```

the next orbit label is `T[v]=2`.  Equation (24) supplies a suffix square,
while (1) says its maximum is exactly that next label.  Hence `r` is a
maximizing root at this label-two cut.  Its copy-parent cut is

```
u=v-r=p+r,
```

and `T[u]=T[v]=2`.  Thus every sufficiently long label-three maximizing
root exports its entire scale to an earlier exact label-two parent edge.
The statement concerns a maximizing root, not necessarily the least
maximizing root at `v`.

Both root blocks in this exported square start one letter before a return
boundary:

```
p=b-1,       u=b+r-1,       v=b+2r-1.
```

Thus this is a repeated one-letter-offset edge.  It is not the asymmetric
configuration of Lemma 1 in `pointed_return_suffix_rank.md`, where the
second root starts at a boundary.  That lemma's retokenization cannot be
imported without a new shifted argument.

## 7. Long label-two roots force comparable high-label roots

The entry argument in `golden_bad_cuts.md` has a short consequence which,
combined with Theorem 3, removes the possible “only label two is
unbounded” branch.

### Theorem 6 (shadow-divergence transfer)

Let a late label-two cut `d` have a maximizing square root of length `q`,
with `q>=N`.  Then some later cut labelled at least three has a maximizing
root of length

```
s>q/M.                                                (25)
```

### Proof

Put

```
u=d-q.
```

The terminal square in `T[0:d]` equates

```
T[u-q:u]=T[u:d].                                     (26)
```

Since `2q<=d`, one has `u>=q>=N`, so every cut used below satisfies the
self-label equation (1).

Compare the two future streams

```
T[u],T[u+1],...
and
T[d],T[d+1],....
```

They cannot agree at every offset.  If they did, the tail from `u` would
be `q`-periodic.  At the cut after `m` complete tail periods, the prefix
would end in the `m`-th power of one length-`q` block.  Taking `m>M`
would make its curling number exceed the tail-alphabet bound (2).

Let `h>=0` be the first mismatch offset.  Equation (26) and the `h`
matched future symbols show that the prefixes at cuts

```
u+h       and       d+h
```

have an equal terminal suffix of length `q+h`.  Their next labels are
different integers in `{2,...,M}`.  Let `k` be the larger label; then
`3<=k<=M`.  Choose a maximizing root of length `s` on that side.

If `k s<=q+h`, the complete terminal `k`-power would lie inside the common
suffix.  It would then be a suffix of the lower-label prefix as well,
forcing that prefix's curling number to be at least `k`.  This contradicts
the choice of the lower label.  Hence

```
k s>q+h>=q,
```

and `k<=M` proves (25).

### Corollary 7 (unbounded label-three maximizing roots)

Every hypothetical counterorbit has unbounded maximizing-root lengths at
label-three cuts.

### Proof

Assume instead that all label-three maximizing-root lengths are bounded.
Theorem 3 bounds every maximizing root at each sufficiently late label at
least four by `N`.  The finitely many earlier cuts have finitely many root
lengths, so there is a global constant `B` bounding every maximizing root
at every label at least three.

Lemma 4 of `reductions.md` supplies unbounded least maximizing-root
lengths.  For all sufficiently large such roots, Theorem 3 excludes labels
at least four and the assumed bound excludes label three, so they occur at
label-two cuts.  Apply Theorem 6 to a label-two root `q>M B`.  It produces
a high-label maximizing root `s>q/M>B`, contradicting the definition of
`B`.

## 8. One-sided ancestry does not remove the point by itself

The static two-return model in `static_return_synchronization.md` realizes
both orientations of the unmatched return start.  The suffix rank in
`pointed_return_suffix_rank.md` strictly orders local return containments,
but its orientation reverses between the no-straddle and one-letter-
straddle cases.  Neither construction is a curling orbit, so these are
mechanism countermodels rather than counterexamples to the conjecture.

The following unbounded one-sided construction adds suffix-copy ancestry
and bounded `H_3` components.

Define Fibonacci words

```
X_0=0,
X_1=01,
X_(n+1)=X_n X_(n-1).
```

For odd `n>=3`, put

```
Z_n=X_(n-3) X_(n-2).                                (27)
```

The recurrence gives the two exact identities

```
X_n=X_(n-2) X_(n-3) X_(n-2),
X_(n+2)=X_n^2 Z_n.                                  (28)
```

For the first identity, substitute
`X_(n-1)=X_(n-2)X_(n-3)` into
`X_n=X_(n-1)X_(n-2)`.  For the second, the two words

```
X_(n-1) X_n
and
X_n X_(n-3) X_(n-2)
```

both equal `X_(n-1)^2 X_(n-2)`.  Substitution in
`X_(n+2)=X_n X_(n-1) X_n` proves the second identity.  The first identity
makes `Z_n` a suffix of `X_n`.  Therefore (28) is obtained by two suffix
duplications:

```
X_n  ->  X_n^2  ->  X_n^2 Z_n=X_(n+2),              (29)
```

where the second endpoint ends in `Z_n^2`.

Fix `M>=4`, set

```
B=(M-1)^M M,
theta(0)=B,
theta(1)=2.                                         (30)
```

Equivalently, `X_n=mu^n(0)` for `mu(0)=01`, `mu(1)=0`.  Every `1` in a
`mu`-image is the last letter of `01`, so no two `1` values are adjacent.
A run of three zeroes in a `mu`-image would require two adjacent source
letters `1`; hence no such run occurs in the limit.  Every zero-run in the
Fibonacci word consequently has length one or two.  Thus every `H_3`
component of `theta(X_infinity)` is `B` or `B^2`, with length at most
`2|B|`.

For odd `n>=3`, repeatedly taking the suffix `X_(n-2)` reduces to
`X_3=01001`.  Every odd `X_n` therefore ends in `1001`, so all odd-stage
endpoints carry the same complete marker

```
2 B^2 2.                                            (31)
```

For `n>=5`, both `X_n` and `Z_n`, whose final factor is `X_(n-2)`, end in
`1001`.  The marker is therefore wholly contained in each suffix copied
in (29).  Applying `theta` to (29) gives an infinite same-marker one-sided
suffix-copy ray with unbounded copy spans and uniformly bounded `H_3`
components.

The limit is aperiodic.  Let `f` be the Fibonacci limit.  The number of
`1` values in `X_n` is the Fibonacci number `F_n`, while
`|X_n|=F_(n+2)`.  Thus the `1` frequency along these prefixes tends to
`1/phi^2`, an irrational number.  An ultimately periodic binary word has
a rational limiting frequency, so `f` is not ultimately periodic.
Erase `M-1`, map `M` to `0`, and map `2` to `1`; this morphism sends
`theta(f)` to `f`.  The image of an ultimately periodic word under a
morphism is ultimately periodic unless the period has empty image.  The
image here is infinite, excluding the empty-image case.  Therefore
`theta(f)` is aperiodic.

This construction proves that the following implication is false:

```
bounded H_3 components
+ a stabilized complete-marker suffix-copy ray
+ unbounded literal suffix-square equalities
=> ultimate periodicity.                            (32)
```

It does not satisfy the full orbit equation (1) at every cut, and the
symbolic argument above does not assert that every displayed square is a
globally maximizing curling factorization.

## 9. Executed finite audit and evidence boundary

The A094004 total-orbit-length calibration was run before the companion
checker.  The convention is total orbit length including the starting
word, and the calibration reproduced

```
a(3)=5,       a(8)=66,       a(22)=142.
```

Then

```
python research/check_one_sided_threshold_ancestry.py
```

checked `M` in `{4,5,6}` and odd indices `n` in `{3,5,7,9}`.  It verified
all identities (27)--(31), the component bound, and both suffix squares.
For the `24` raw endpoints, up to raw length `1097`, two independent
curling-number implementations agreed that the endpoint curling number
was `2`.  This is `CHECKED` evidence on that finite domain, not an
unbounded maximality theorem.

## 10. Exact remaining gap

Theorem 1 eliminates unbounded high-threshold components.  Theorem 3
eliminates unbounded maximizing roots at every label at least four.
Corollary 7 forces unbounded label-three roots, and Theorem 4 reduces each
large cube to an aligned square over a finite return alphabet plus one
bounded pointed overhang.

No proved step transports the missing `s` symbols in (23) along the actual
maximizing-root ancestry so that the bounded point disappears or descends.

Finite return types, stabilized exit markers, and raw suffix duplication
do not supply that conclusion.  A completion of this route must use the
exact labels at the intervening cuts to close the pointed state, not only
the component geometry or the return code.
