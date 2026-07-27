# Threshold inheritance, seam masks, and the blocked alphabet induction

This note isolates the part of threshold-component normalization that is
automatic and the part that is not.  High internal coordinates inherit
their exact finite curling equations.  The first coordinate at the
threshold can cross the component seam.  Quotienting component returns
then produces a pointed, colored, weighted profile rather than an
ordinary smaller-alphabet critical profile.

The exact critical word of length 21 realizes both quotient defects:
first-copy boundary misalignment persists even when the token-to-weight
map is injective, and a coarser constant-component quotient also has
several return colors of one weight.  Thus the proposed unconditional
extraction lemma is false in that generality.  The special implication
from a hypothetical maximum `M>=4` profile remains conditional on new
boundary-closure and pointed-fitting statements.

## 1. Setup

Let `P` be a primitive circular word of length `n` with exact proper
circular profile

```
pc_P(d)=P[d]>=2                                      (1)
```

at every cut `d`.  For an integer `k>=2`, put

```
H_k={d:P[d]>=k}.                                    (2)
```

A component of `H_k` is a maximal circular interval of positions in
`H_k`.  When it is not the whole circle, orient one such component as

```
C=P[u:v],
P[u-1]<k, P[v]<k.                                  (3)
```

All coordinates are interpreted in one fixed lift of the circle.

For a cut `d`, an attaining `j`-root means a root `R` such that `R^j`
ends at `d` and `j=P[d]`.  Every attaining root is primitive.  If
`R=V^h` with `h>=2`, then `R^j=V^(hj)` would give an exponent strictly
above the exact value `j` in (1).

## 2. High coordinates are contained and inherit exactly

### Lemma 1 (threshold containment)

If an attaining `j`-root `R` ends at cut `d`, then every symbol of `R`
is at least `j-1`.  The complete displayed power `R^j` lies in one
component of `H_(j-1)`.

### Proof

Write `r=|R|`.  For each `0<=t<r`, consider the cut

```
x=d-r+t.
```

The length-`(j-1)r` suffix ending at `x` consists of `j-1` copies of
the conjugate

```
R[t:r] R[0:t].
```

It follows from (1) that `P[x]>=j-1`.  As `t` ranges over one root,
these are all symbols of `R`.  Every copy of `R` has the same symbols,
so every position of `R^j` belongs to `H_(j-1)`.  A connected circular
factor contained in `H_(j-1)` lies in one of its components.

### Lemma 2 (exact internal inheritance)

Let `d` be a position of the component `C` in (3), and put

```
j=P[d]>=k+1,       t=d-u.
```

Then every attaining `j`-power at `d` is contained in `C[0:t]`, and

```
cn(C[0:t])=j,
cn(P[u-1] C[0:t])=j.                              (4)
```

The attaining powered suffix in both finite words starts strictly to
the right of the normalized separator `P[u-1]`.

### Proof

Lemma 1 puts every symbol of the power in `H_(j-1)`, which is a subset
of `H_k`.  The endpoint position `d` also belongs to `H_k`.  Therefore
no position below `k` separates the power from `d`, and maximality of
`C` puts the whole power in `C[0:t]`.  In particular `t` is positive,
so both finite words in (4) are nonempty.

This gives the lower bounds in (4).  Suppose one of the two finite
words had a suffix power of exponent `e>j` and root length `q`.  Its
length is at most `n`, so `q<n`.  The same factor is a proper circular
`e`-power of `P` ending at `d`, contradicting (1).  Hence both upper
bounds are `j`, proving (4).  The containment already proved places the
attaining powered suffix after the separator.

Thus normalization loses no equation at labels strictly above the
threshold.  It also loses no *local* first-copy visibility there: the
witness lies wholly on the normalized side of the seam.  This local
statement does not assert the circular profile or the deleted-copy
equations of the complete normalized component word.

## 3. The only internal losses are threshold seam masks

There is a useful exact entrance theorem before considering arbitrary
seams.

### Lemma 3 (forced threshold entrance)

Let

```
D=P[a:b]
```

be a proper maximal `H_(k-1)` component, where `k>=3`, and suppose it
contains a position in `H_k`.  If `d` is its first such position, then

```
P[a:d+1]=(k-1)^k k.                                (5)
```

In particular, the first `H_k` position has label exactly `k`, its
attaining root is the unary symbol `k-1`, and there are no earlier
positions in `D`.

### Proof

Put `j=P[d]`.  If `j>=k+1`, Lemma 1 puts the complete attaining
`j`-power in `H_(j-1)`, hence in `H_k`, immediately before `d`.  This
contradicts the choice of `d`.  Therefore `j=k`.

Lemma 1 puts an attaining `k`-power inside `D`.  Every position of this
power precedes the first `H_k` position, so each of its symbols is
exactly `k-1`.  Its primitive root is consequently the one-symbol word
`(k-1)`, and the `k` positions immediately preceding `d` are all
`k-1`.

If another position of `D` preceded those `k` positions, it would also
be `k-1`, producing a unary exponent at least `k+1` at cut `d` and
contradicting `P[d]=k`.  Thus the run begins at `a`, proving (5).

At a cut with label exactly `k`, Lemma 1 gives only

```
symbols of an attaining root >=k-1.                (6)
```

The power is contained in the ambient `H_(k-1)` component, but it may
cross the left boundary `u` of `C`.

Call the cut a **threshold seam mask** when every attaining `k`-root
crosses `u`.  This definition is exact:

* if one attaining root is contained in `C[0:t]`, the argument of
  Lemma 2 proves the local equation;
* if `cn(C[0:t])=k`, its attaining suffix is also a proper circular
  `k`-power of `P`, so one attaining root is contained.

A seam mask forces

```
P[u-1]=k-1.                                        (7)
```

Indeed, the crossing root contains `P[u-1]`; (6) gives
`P[u-1]>=k-1`, while (3) gives `P[u-1]<k`.

Consequently every internal loss descends by exactly one threshold:
the missing witness is contained in the larger `H_(k-1)` component and
crosses one or more positions labeled `k-1`.  Iterating this observation
eventually reaches threshold two, but it does not create a smaller
ordinary fixed profile.  The containing component can grow, different
seams can select different roots, and at threshold two the component is
the whole no-`1` profile.

## 4. Return quotients and the second seam

Now take a cyclic family of synchronized component/exit markers

```
F_i=C_i e_i,       e_i<k,                          (8)
```

and put a boundary immediately after every selected occurrence.  Assume
that copying a selected marker produces another selected boundary; the
constant component-word conclusion on a component-parent cycle supplies
this hypothesis.

The raw interval from one boundary to the next is a **return token**.
Two token colors are equal only when their complete raw integer words
are equal.  Let `T` be the circular word of token colors.  Give the
token cut at raw boundary `b_i` the numerical weight

```
w_i=P[b_i]=a.                                      (9)
```

Choose an attaining `a`-root of raw length `q` at `b_i`.  Its final
symbol is `e_i`.  Lemma 1 at threshold `a` therefore gives

```
2<=a<=e_i+1<=k.                                   (10)
```

Also,

```
q>=|C_i|+1=|F_i|.                                 (11)
```

If `q<=|C_i|`, equality of the last two root blocks would copy the
terminal `e_i` to a position inside `C_i`, whose symbols are all at
least `k`; this contradicts `e_i<k`.

Equality of the `a` root blocks copies the final marker to

```
b_i-q, b_i-2q, ..., b_i-(a-1)q.                   (12)
```

These are selected boundaries.  The raw intervals between consecutive
cuts in (12) are equal, and exact marker synchronization decomposes each
one into the same token block.  Hence `T` ends at this token cut in
`a-1` copies of a token block.

The earliest raw power start

```
b_i-aq                                             (13)
```

is not constrained by block equality to be a boundary.  It is the
**return-start seam**.  A token `h`-power expands to a raw `h`-power;
if its token root is proper, its positive-length expansion is shorter
than `P`.  Equation (1) bounds `h` by `a`.  Therefore the exact token
profile `c_i` satisfies

```
a-1<=c_i<=a.                                      (14)
```

Moreover,

```
c_i=a
```

if and only if some attaining raw `a`-power has its start (13) at a
selected boundary.  Thus constant components give a defective weighted
profile with a one-unit boundary defect, not an exact fixed profile.

The token word is primitive when the return decomposition is
unambiguous and token colors denote complete raw return words.  A token
period would expand to a proper integral period of a rotation of `P`.

## 5. A rigorous conditional alphabet reduction

The following conditions are sufficient for the desired static
extraction.

1. At every selected boundary, some attaining raw root has its earliest
   start (13) at a selected boundary.
2. Distinct token colors have distinct weights.
3. An origin boundary can be chosen so that, at every token cut, one
   boundary-aligned attaining power starts no earlier than the boundary
   following the deleted first token.

Under condition 1, (14) becomes

```
pc_T(i)=w_i.                                       (15)
```

Under condition 2, replacing each token color by its weight preserves
all equality relations.  The numerical weight word

```
W=(w_0,...,w_(N-1))
```

therefore has

```
pc_W(i)=W[i],       2<=W[i]<=k.                   (16)
```

Condition 3 gives the first-copy fitting witness for every cut of `W`.
The fitting-witness equivalence in
`research/critical_fitting_witnesses.md` then gives the complete critical
synchronization equations for `W`.

Taking `k=M-1` would yield a critical synchronized word of maximum at
most `M-1`.  This is a conditional reduction.  None of its three
conditions follows from component-length constancy or separator
constancy.

Condition 2 is only a convenient sufficient hypothesis.  Without it,
collapsing several return colors to one numerical weight can create new
token powers which have no raw lift.  Conditions 1 and 3 are distinct:
raw first-copy fitting locates a power after deletion of one raw symbol,
whereas token fitting must locate it after deletion of one complete
return token.

## 6. Exact critical Q21 audit

The executed audit

```
research/check_threshold_quotient_audit.py
```

uses

```
P=223222322232322232223.
```

It recomputes:

* `pc_P=P`;
* both high and one-symbol-deleted finite curling equations at every
  phase for one and two copies;
* every raw attaining root;
* both quotient profiles below.

Every `H_3` component is the singleton `3` and is followed by the same
exit symbol `2`.  Boundaries after these constant `32` markers give raw
return words

```
232, 2232, 2232, 32, 2232, 2232.
```

Their exact identity word, successor weights, and two profiles are

```
T       = (0,1,1,2,1,1),
w       = (2,2,2,3,2,2),
pc_T    = (2,1,1,2,1,1),
pc_w    = (2,3,4,5,1,1).                          (17)
```

At raw cut four, the target is two and the only attaining root has
length three.  The preceding marker boundary is aligned, but the
earliest square start is not a marker boundary.  At raw cut twelve, the
target is three and the only attaining root has length four.  The first
two predecessor boundaries are aligned; the earliest cube start is not.
These are literal return-start seams.

A finer quotient puts a boundary after every symbol below threshold
three.  It has only the return identities

```
(2), (3,2),
```

and they map injectively to weights two and three.  Its identity profile
equals its weight profile but differs from the prescribed weight word:

```
pc_T=(2,2,2,2,2,2,2,2,2,2,1,2,2,1,2).           (18)
```

Hence first-copy boundary closure can fail in a completely synchronized
critical word even when numerical relabeling is injective.  The coarser
quotient (17) independently exhibits noninjective weights and the extra
powers created by collapsing colors.

This is an exact counterexample to the general assertion that a constant
component signature automatically extracts a smaller critical profile.
It is not a counterexample to a theorem restricted by additional
maximum-`M>=4` entrance structure; such a theorem must prove that the
extra structure enforces conditions 1--3.

## 7. The formal M=6 adversary

The executed model in

```
research/check_exit_marker_cycle_model.py
```

uses the three equal-length returns

```
2,4,5^6,6,e,       e in {2,3,4}.
```

Its colored token word is primitive and has exact token profile two at
all 31 token cuts.  Every raw marker cut also has value two.  The least
root marker-parent cycles alternate raw root lengths 130 and 180 while
all nested component lengths and separators remain constant.

The model fails the full raw profile first at the prescribed label-four
cut immediately before the top entrance; the executed proper value is
two.  This is the first high coordinate that Lemma 2 would force in an
exact profile.  It is the first `H_4` symbol of its `H_3` component, so
an attaining fourth power must lie before it inside that component.
Every preceding symbol there is three, forcing the missing entrance

```
3^4 4.
```

For the exit-three return, the analogous first `H_5` entrance has only
one preceding four where the exact equation requires `4^5`.

Thus the M=6 marker algebra does not evade threshold induction.  Its
repair obligation moves into the lower component exactly as Lemma 3
predicts.  What remains absent is a theorem turning the repaired seam
data into boundary closure and an ordinary lower-weight profile.

The same model has three return colors but one marker-cut weight, namely
two.  Replacing the colors by that weight destroys primitivity and
creates token powers which do not lift to the unequal raw returns.  This
is the noninjective branch of the quotient obstruction.

## 8. Contaminated resets prevent orbit closure

Static profile extraction would still need a dynamical lifting theorem.
For every `M>=4`, put

```
A=M-1,       L=M-2,       R=L A^(A-1).
```

The symbolic proof in `research/top_marker_rescue.md` gives

```
cn(R^A)=A,
cn(R^A A)=A,
cn(R^A A^2)=M.                                    (19)
```

`research/check_top_marker_rescue.py` independently executes (19) for
`M=4,5,6,7`.  The last maximizing root is unary.  A contaminated
lower-threshold root can therefore pass through two deterministic
`A`-appends and recreate the old maximum at scale one.

The complementary family

```
Q=A^A L
```

is sharper for the forced-entrance lemma.  The symbolic calculation in
`research/top_marker_rescue.md` gives

```
cn(Q^A A^t)=A       for 0<=t<=A,
cn(Q^A A^(A+1))=M.
```

Thus its deterministic output is the complete forced entrance

```
A^(A+1)M=(M-1)^M M.
```

The executed checker recomputes every value and maximizing-root set for
`M=4,5,6,7`: the length-`M` contaminated root survives through the
first `A` outputs, ties the unary root at the last `A` cut, and then
hands off to the unary maximum.  Hence even the exact entrance from
Lemma 3 is compatible with a scale reset.

Equation (19) does not refute the conditional static proposition in
Section 5.  It refutes the additional assumption that the extracted
lower-weight object is automatically closed under the raw orbit map, or
that maximum label/root scale supplies a well-founded cross-seam rank.
A complete alphabet induction must specify the pointed colored state,
prove that its deterministic evolution is represented by the smaller
ordinary sequence, and exclude precisely this reset branch.

## 9. Exact status of the route

The following statements are proved:

* labels strictly above a threshold inherit exact finite equations and
  locally fitting witnesses inside the normalized component;
* all internal failures occur at threshold labels and cross into the
  next lower threshold component;
* a synchronized return quotient has weights at most the threshold and
  token profile in `{weight-1,weight}`;
* boundary closure, injective weights, and pointed token fitting imply a
  genuine smaller critical synchronized profile.

The unconditional reduction

```
maximum M>=4  ->  critical profile of maximum at most M-1
```

has not been proved.  Its missing statements are exactly:

1. eliminate every return-start seam, or convert it to a strictly
   smaller pointed candidate;
2. preserve a first-copy fitting window measured in complete tokens;
3. prevent equal-weight return colors from creating nonlifting powers,
   or retain colors in a theorem strong enough to replace ordinary
   alphabet induction;
4. prove that the resulting lower object controls the raw deterministic
   evolution across contaminated resets.

Q21 shows that items 1--3 are not consequences of exact fixedness,
critical fitting, and constant component signatures alone.  The reset
family shows why item 4 cannot be omitted.
