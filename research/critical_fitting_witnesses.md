# Critical synchronization as a fitting-witness condition

This note isolates the content added by the deleted-context equations to
a binary proper circular fixed profile.  It also gives the exact
scale-replacement rule at an adjacent `33` component.  It does not prove
that adjacent `33` is impossible.

## 1. Definitions

Let `P` be a primitive word of length `n` over `{2,3}`, with `P[0]=2`.
For a circular cut `j`, let

`Pow(j,e,r)`

mean that the length-`e r` circular suffix ending at `j` is an `e`-th
power with root length `r<n`.

Assume throughout that the exact proper circular profile is

`pc_P(j)=P[j]` for every `0<=j<n`.                         (1)

For `a in {1,2}`, define the high and deleted states

`H_(a,j)=P^a P[:j]`,

`D_(a,j)=P[1:] P^(a-1) P[:j]`.                            (2)

The full critical synchronization equations are

`cn(H_(a,j))=cn(D_(a,j))=P[j]`.                           (3)

Call a maximizing circular root at cut `j` *first-copy fitting* when

`P[j] r <= n+j-1`.                                        (4)

The right side is exactly the length of `D_(1,j)`.

## 2. Proper circular powers have span below two periods

### Lemma 1

If `Pow(j,e,r)` holds with `e>=2` and `r<n`, then

`e r < n+r-gcd(n,r) < 2n`.                                (5)

### Proof

The powered factor has periods `n` and `r`.  Put `g=gcd(n,r)`.  If its
length met the Fine--Wilf threshold `n+r-g`, Fine--Wilf would give period
`g` to the factor.  The threshold is at least `n`, so the factor contains
a complete length-`n` conjugate of `P`.  That conjugate would have period
`g<n`, contradicting the primitivity of `P`.  This proves the first
inequality.  The second follows from `r<n` and `g>=1`.

## 3. Exact equivalence

### Theorem 2 (fitting-witness equivalence)

Under (1), all equations (3) hold if and only if, at every cut `j`, there
is a root `r<n` satisfying

`Pow(j,P[j],r)` and `P[j] r<=n+j-1`.                       (6)

Thus the entire extra content of the deleted replay is the positive
fitting condition (6) in the first copy.  The equations with `a=2`
add no further condition once (1) and (6) hold.

### Proof: necessity

Assume (3).  The deleted first-copy state `D_(1,j)` has length
`n+j-1<2n`.  Since its curling number is `P[j]>=2`, it has a
`P[j]`-power suffix with some root length `r`.  The powered suffix fits
in the state, giving `P[j]r<=n+j-1`.  Also `r<n`, because two copies of
a root of length at least `n` do not fit in a word shorter than `2n`.
The finite suffix is a factor of `P^Z`, so it gives `Pow(j,P[j],r)`.
This proves (6).

### Proof: sufficiency for the first copy

Assume (6).  Its power suffix lies in `D_(1,j)` and therefore also in
`H_(1,j)`, giving the lower bound `P[j]` in both words.

Every powered suffix of either first-copy word has root length below
`n`, since both words have length below `2n`.  It is consequently a
proper circular power at cut `j`.  Equation (1) excludes every exponent
above `P[j]`.  The lower and upper bounds prove (3) for `a=1`.

### Proof: sufficiency for the second copy

Lemma 1 puts every proper circular maximizing witness inside a suffix of
length below `2n`.  Both second-copy states have length at least `2n-1`,
so those witnesses give the lower bound `P[j]`.

It remains to exclude a finite suffix power which is not represented by
a proper circular root.  Any suffix of exponent at least three in a word
of length at most `3n-1` has root length below `n`; equation (1) therefore
bounds it by `P[j]`.

For a square suffix, let its root length be `r>=n`.  The state-length
bound gives `r<3n/2`.  If `r>n`, then `gcd(n,r)<n`, and

`2r >= n+r-gcd(n,r)`.

Fine--Wilf gives the proper gcd period to a complete conjugate of `P`,
contradicting primitivity.  The only remaining nonproper root is `r=n`.
It supplies exponent two and cannot fit three copies in either
second-copy state.  Since `P[j]>=2`, it cannot raise the value above the
target.  This proves (3) for `a=2`.

## 4. Scale replacement at a nonfitting cube

At a `3`-cut every cube root is primitive: a nonprimitive root
`V^d`, with `d>=2`, would give exponent at least six with root `V`,
contradicting (1).

### Lemma 3 (same-cut separation)

If primitive cube roots of lengths `r<p` end at the same cut, then

`p>2r+gcd(p,r)`.                                          (7)

### Proof

The smaller cube is a suffix of the larger one, so its length-`3r`
interval has periods `p` and `r`.  Put `g=gcd(p,r)`.  If
`p<=2r+g`, then

`3r>=p+r-g`.

Fine--Wilf gives period `g` on the smaller cube.  The same inequality
also gives `3r>=p`, so this interval contains a complete conjugate of
the primitive length-`p` root.  That conjugate would have period
`g<p`, a contradiction.

### Corollary 4 (fitting child)

Let a primitive cube root of length `p` end at cut `j`.  If it is not
first-copy fitting, then the same cut has a fitting primitive cube root
of length `r` satisfying

`p>2r+gcd(p,r)`, and hence `r<p/2`.                        (8)

### Proof

Theorem 2 supplies a fitting cube root `r`.  Nonfitting of `p` and
fitting of `r` give `3p>n+j-1>=3r`, so `r<p`.  Lemma 3 gives (8).

The replacement can be repeated whenever a copied cube is moved to an
earlier lift and ceases to fit.  Its positive integer root length drops
by more than a factor of two at every such replacement, so only finitely
many replacements are possible.

## 5. Adjacent `33`

Suppose

`P[c-1],P[c],P[c+1],P[c+2]=2,3,3,2`.                     (9)

Let cube roots of lengths `p` and `q` end at cuts `c` and `c+1`.
The bridge/separation lemma in `research/adjacent_double_bridge.md`
gives:

- if `p=q`, then `U^3 3=3 rot(U)^3`;
- if `q>p`, then `q>2p+gcd(p,q)`;
- if `p>q`, then `p>=2q+gcd(p,q)`.

Corollary 4 strengthens the equal-root branch under full critical
synchronization.  If its common bridge root fails to fit at either
occurrence, that occurrence has a fitting cube root below half the
bridge scale.  Comparing the fitting roots at the two cuts therefore
terminates in one of two normal forms:

1. a common bridge root which fits at both cuts; or
2. two fitting roots in one of the separated scale regimes.

No appeal to an unfitted circular witness is needed after this
normalization.

There are also exact transport equations in the two separated regimes.
They identify what a further descent must control.

### Lemma 5 (large root at the second cut)

Assume `q>p`.  The `q`-cube contains a translated copy of the `p`-cube
ending at cut

`d=c-q`.

At this copied cut,

`P[d],P[d+1]=3,2`.                                        (10)

### Proof

The `p`-cube interval is `[c-3p,c)`, and the `q`-cube interval is
`[c+1-3q,c+1)`.  The separation inequality makes the translate

`[c-3p-q,c-q)`

lie wholly in the `q`-cube.  Period `q` therefore copies the complete
`p`-cube to that interval.

The same period copies position `c` to `c-q`, so `P[d]=P[c]=3`.
Let `B` be the length-`q` root ending at `c+1`.  If its first symbol
were `3=P[c+1]`, appending `P[c+1]` would extend the `q`-period and give
a `q`-cube at cut `c+2`, contradicting `P[c+2]=2`.  Hence `B[0]=2`.
Its first symbol is `P[c+1-q]=P[d+1]`, proving (10).

If the copied `p`-cube in Lemma 5 does not fit at its new lifted cut,
Corollary 4 replaces it by a fitting root below `p/2`.  This is the
finite fit-scale descent available in the `q>p` branch.

### Lemma 6 (large root at the first cut)

Assume `p>q` and that `p` is not also a cube root at cut `c+1`.  Write
the length-`q` root ending there as `B=Z3`.  At cut

`d=c-p`

the word ends in the square `(3Z)^2`, while `P[d]=2`.       (11)

### Proof

Delete the final symbol from the `q`-cube `B^3`.  Its remaining
length-`3q-1` factor is

`Z(3Z)^2`.

The separation inequality makes this factor and its translate left by
`p` lie wholly in the `p`-cube, so period `p` copies it to the interval
ending at `d`.

If `P[d]=3=P[c]`, the `p`-period would extend through the appended
symbol at `c`, making `p` a cube root at cut `c+1`, contrary to the
hypothesis.  Therefore `P[d]=2`.  The copied factor ends in `(3Z)^2`,
which proves (11).  Equation (1) at cut `d` excludes a third copy.

Lemma 6 is an exact one-letter period-completion defect, not yet a
contradiction.  A complete adjacent-`33` elimination must show that the
finite descent cannot terminate in either a fitting equal bridge or one
of these separated defects without creating a cube at one of the
`2`-cuts in (9).

## 6. Distinguished-origin lift calculus

Retain the four-cut coordinates (9), with canonical
`1<=c<=n-2`, and choose fitting roots `p` at `c` and `q` at `c+1`.
Thus

```
3p<=n+c-1,                 3q<=n+c.             (12)
```

These inequalities make the transports in Lemmas 5 and 6 genuine
factors of the distinguished deleted-copy window, not merely circular
factors.

### Lemma 7 (equal bridge reaches an in-window predecessor)

If `p=q`, put

```
e=c-3p-1.
```

Then `e,e+1` is the predecessor double component and

```
1-n<=e<c.
```

If

```
sigma=n+c-1-3p,
```

then `sigma=n+e`, and the canonical phase of the predecessor is
`sigma mod n`.

### Proof

The predecessor assertion is Lemma 1 of
`research/adjacent_double_bridge.md`.  The first inequality in (12)
gives `e>=-n`.  Equality would make `P[e]=P[0]=2`, whereas the
predecessor assertion gives `P[e]=3`.  Therefore `e>=1-n`.
The remaining statements follow by substitution.

The lifted predecessor cut is strictly earlier, but this alone is not
a well-founded descent.  After a circular phase cycle it may be the same
component translated one whole period to the left.

### Lemma 8 (the `q>p` transport is fitting in the common lift)

Assume `q>p`.  At

```
d=c-q
```

there is a `p`-root cube with

```
P[d-1],P[d],P[d+1]=2,3,2,
d-3p>=1-n.                                      (13)
```

Its start is earlier by exactly `q` than the start `c-3p` of the
original `p`-cube.

### Proof

Lemma 5 gives the copied cube and the last two labels.  Period `q`
inside the `q`-cube also copies `P[c-1]=2` to `P[d-1]`.

The separation inequality is strict over integers:

```
q>2p+gcd(p,q)  implies  q>=2p+2.
```

Consequently

```
3q-(q+3p)=2q-3p>=p+4.
```

Using `3q<=n+c` from (12) gives

```
q+3p<=n+c-1,
```

which is equivalent to the last inequality in (13).  Finally,

```
(c-q-3p)-(c-3p)=-q.
```

The copied period-`p` run is exactly the displayed cube.  A left
extension would put a period-`p` cube at the `2`-cut `d-1`, and a right
extension would put one at the `2`-cut `d+1`.  Both extensions are
excluded by (1).

### Lemma 9 (the `p>q` completion-defect square is fitting)

Assume `p>q` and the hypotheses of Lemma 6.  At

```
d=c-p
```

the displayed `q`-root square `(3Z)^2` satisfies

```
d-2q>=1-n.                                      (14)
```

Its start is strictly earlier than the start of the original `q`-cube
ending at `c+1`.

### Proof

Since `p>q`,

```
3p-(p+2q)=2(p-q)>=2.
```

The first inequality in (12) therefore gives

```
p+2q<=n+c-1,
```

which is (14).  The difference between the transported square start
and the original cube start is

```
(c-p-2q)-(c+1-3q)=q-p-1<0.
```

There is a sharper run description.  Put `R=3Z`.  The factor copied in
Lemma 6 is

```
Z R^2,
```

which has period `q` and length `3q-1`.  The symbol immediately to its
right is `P[d]=2`, whereas a period-`q` extension requires the initial
`3` of `R`.  The symbol immediately to its left is also `2`: a `3`
there would complete `R^3` at the `2`-cut `d`.  Hence this is an exact
maximal period-`q` run of length `3q-1`.  Its least period is `q`,
because `R` is primitive and Fine--Wilf would otherwise give a proper
period to a complete copy of `R`.

Lemmas 7--9 give an exact trichotomy for the first transport:

* an equal bridge reaches an earlier double component without crossing
  the deleted left boundary;
* the larger second root creates an earlier fitting isolated cube; or
* the larger first root creates an earlier fitting square with a
  one-letter cube-completion defect.

They do not yet supply an iterable descent.  At a negative lifted cut,
the critical equation supplies a fitting witness at its *canonical*
representative; translating that witness one period left can put its
start below `1-n`.  Fitting is pointed at the deleted origin and is not
translation invariant.

The point at which such a chain loses the common lift can be stated
exactly.

### Lemma 10 (isolated-cube predecessor and first-loss interval)

Suppose

```
P[d-1],P[d],P[d+1]=2,3,2
```

and a primitive `r`-root cube ending at lifted cut `d` starts at
`a=d-3r>=1-n`.  Then

```
P[a-1],P[a]=3,2
```

and `a-1>=1-n`.

Now let `t in [1-n,-1]` be a `3`-cut at which no cube occurrence is
wholly contained in the distinguished window.  If `r` is any fitting
cube root at its canonical phase `t+n`, then

```
n+t <= 3r <= 2n+t-1.                            (15)
```

Equivalently, for a unique integer `delta` with `1<=delta<=n`,

```
t-3r=1-n-delta.                                 (16)
```

### Proof

If the period-`r` cube extended one symbol to the right, it would give
an `r`-root cube at the `2`-cut `d+1`.  Thus its first symbol is
`P[a]=2`, opposite the appended symbol `P[d]=3`.

If it extended one symbol to the left, shifting the length-`3r` window
left would give an `r`-root cube at the `2`-cut `d-1`.  Hence
`P[a-1]` is opposite the cube's final symbol `P[d-1]=2`, so
`P[a-1]=3`.  The assumed start gives `a-1>=-n`.  Equality would identify
`P[a-1]` with `P[0]=2`; therefore `a-1>=1-n`.

For the second assertion, failure to fit in the displayed lift says

```
3r>n+t-1.
```

Fitting at canonical phase `t+n` says

```
3r<=n+(t+n)-1=2n+t-1.
```

Integral endpoints give (15).  Defining
`delta=3r-(n+t-1)` gives (16) and the stated bounds.

The period-21 bridge calibration makes this obstruction exact.  Rotate
the length-64 word in `research/check_double_three.py` by one symbol so
that phase zero is `2`.  Its unique double component begins at phase
`62`, and its common root `21` gives

```
62 -> 62-64=-2 -> -66 -> ...
```

in the lifted predecessor chain.  The starts decrease by `64` forever,
while the circular phase repeats.  Direct computation shows that this
word obeys every no-cube and no-fourth constraint; it fails instead at
two square-labelled cuts with no square and one `3`-labelled cut with no
cube.  Thus strict decrease of lifted starts is not by itself a
contradiction.  A successful continuation must prove that every such
phase re-entry forces one of those missing positive witnesses or a
forbidden cube.

### Lemma 11 (three-for-one double-component count)

Let `B` be any primitive cube root ending at the second cut `c+1` of
the double component (9).  Then `B` begins with `2` and ends with `3`.
In the linear factor

```
B^3 3
```

ending at cut `c+2`, every occurrence of `33` is either the terminal
one or one of the three aligned copies of an occurrence wholly internal
to `B`.  In particular,

```
number_of_33(B^3 3)=3 number_of_33(B)+1.         (17)
```

### Proof

The last symbol of `B` is the symbol immediately before cut `c+1`,
namely `P[c]=3`.  If the first symbol of `B` were `3`, the period of
the displayed cube would extend through `P[c+1]=3`; a cube would then
end at cut `c+2`, contradicting its label `2`.  Thus the first symbol
is `2`.

There is no `33` across a join between copies of `B`, because each such
join is `3|2`.  Internal occurrences repeat once in each copy.  The
appended symbol is `3`, so it forms exactly one additional occurrence
with the final symbol of the third copy.  This proves (17).

For a globally maximal physical cube root, the internal third-copy
components in (17) have roots below half the parent scale by the
maximal-root lemma in `research/gadget_cycle_structure.md`.  This is
only a one-generation statement: a deeper root can cross its immediate
parent and regrow.  Equation (17) therefore identifies a ternary
component structure, but does not by itself justify an iterated
halving descent.

## 7. Executed bounded audit

`research/z3_critical_adjacent33.py` encodes (1) and (6), requires an
adjacent `33`, and independently checks every satisfying model against
the original finite equations (3) with both implementations in
`curling.py`.

The known length-21 word

`223222322232322232223`

calibrates the encoding: it satisfies every equation (3) and has no
adjacent `33`.  The adjacent-`33` formula is unsatisfiable for every
length from `2` through `41` in the executed run.  This bounded result is
open beyond the checked range and is not used as a proof.
