# The all-long quotient after contracting a gap-four pair

This note replaces the unary marker in the all-long ancestry quotient by
the atomic pair

```
G=222322232.
```

The contraction gives one unconditional orientation, `q<r`, and then a
strict border-word descent.  It does not yet prove that the descended
border word inherits every fitting equation.

## 1. Setup and equality quotient

Put the selected high pair endpoint at cut zero.  Let its incoming cube
root have length `r`, let the loss square which copies the high pair to
the first low pair have root length `q`, and let the second low copy be
the next endpoint of the incoming cube.  One ancestry circuit has

```
N=q+2r,                                           (1)
```

with pair endpoints

```
0, q, q+r  (mod N).                               (2)
```

Both roots are long pair parents, so

```
r>=9, q>=9.
```

Let `B` be the length-`r` incoming root, indexed as the copy from
`q+r` to `N`.  The cube and square equalities give the component formula

```
P[i]=B[((i mod N)-q) mod r].                      (3)
```

If `q<r`, the circular seam additionally gives

```
B[j]=B[q+j], 0<=j<r-q.                            (4)
```

The pair and endpoint labels give

```
B[-9:]=G,
B[0]=2,
P[0]=3.                                          (5)
```

Maximality of the incoming period-`r` run gives the pointed
non-extension symbol

```
P[-3r-1]=3.                                       (6)
```

Equations (1)--(6) are the pair version of Section 6 of
`research/terminal_marker_ancestry.md`.

## 2. Every all-long pair quotient has `q<r`

### Lemma 1

Under (1)--(6),

```
q<r.                                              (7)
```

### Proof

If `q=r`, then `N=3r`, so the phase `-3r-1` in (6) is the phase `-1`.
The last symbol of `G` in (5) gives `P[-1]=2`, contradicting (6).

Suppose `q>r`.  Since the ancestry bound is `q<3r`, the integer

```
x=q-r-1
```

is a phase in `[0,N)`.  It represents `-3r-1` modulo `N`, because

```
x-(-3r-1)=q+2r=N.
```

Formula (3) gives

```
P[x]=B[(x-q) mod r]
    =B[-r-1 mod r]
    =B[-1]
    =2,
```

where the last equality is the last symbol of `G`.  Equation (6)
requires the same symbol to be three.  This contradiction proves (7).

This is stronger than the scalar winding identity: an outgoing
pair-parent is always strictly shorter than the incoming cube root.

## 3. Deleted-prefix normal form and deficit classification

Put

```
delta=r-q>0.                                      (8)
```

Then (3)--(4) become

```
P=B[delta:] B^2,                                  (9)
B[0:delta]=B[q:r].                                (10)
```

Thus the incoming root has the proper border

```
D:=B[0:delta]=B[q:r].                             (11)
```

The high label and pointed defect become

```
B[delta]=3,
B[q-1]=3.                                         (12)
```

To verify the second identity, reduce the phase in (6) twice modulo
`N=3r-delta`, then apply (3):

```
-3r-1 mod N = 3r-2delta-1,
B[(3r-2delta-1-q) mod r]=B[q-1].
```

There is a complete classification when the border is shorter than the
pair word.

### Lemma 2

If `delta<9`, then

```
delta in {1,5}.                                   (13)
```

### Proof

The position `q-1=r-delta-1` lies in the final occurrence of `G`.
Measured from the start `r-9` of that occurrence, its index is

```
(r-delta-1)-(r-9)=8-delta.
```

The two symbols `3` of `G=222322232` have indices three and seven.
The requirement `B[q-1]=3` in (12) therefore gives

```
8-delta in {3,7},
```

which is equivalent to (13).

For `delta=1`, the border is the one-symbol word `2`.  For `delta=5`,
it is exactly the unary terminal marker `22232`.  Every other surviving
deficit is at least nine.

## 4. The strict border-word descent

### Lemma 3

If `delta>=9`, the border `D` in (11) has all of the following
properties:

1. `|D|=delta<r`;
2. `D` ends in the complete pair `G`;
3. `cn(D)=2`;
4. one occurrence of `D` is followed at its endpoint by exact label
   three, while an identical occurrence is followed by exact label two;
5. every cube root `s` at the label-three occurrence satisfies

   ```
   3s>delta.                                      (14)
   ```

### Proof

Items 1 and 2 follow from (8), (10), and `B[-9:]=G`.

Place one copy of `B` inside the incoming cube.  Its prefix occurrence
`B[0:delta]=D` is followed by `B[delta]=3`, by (12).  Its suffix
occurrence `B[q:r]=D` is followed, at either internal boundary between
copies of `B`, by `B[0]=2`.  These are exact profile labels, proving
item 4.

At the label-two occurrence, suffix monotonicity gives `cn(D)<=2`.
The suffix `G` ends in the square

```
(2232)^2,
```

so `cn(D)>=2`.  Hence `cn(D)=2`, proving item 3.

Let `s` be any cube root at the label-three occurrence.  If
`3s<=delta`, its complete cube is a suffix of `D`, which would give
`cn(D)>=3`, contradicting item 3.  Therefore (14) holds.

Thus a large deficit does not remain an unstructured integer.  It
produces a strictly shorter pair-bearing word with an explicit
contextual `2 -> 3` hole.  The descent target is `(D, distinguished
label-three occurrence, distinguished label-two occurrence)`, not merely
the number `delta`.

There is a further contained descent when `B` is a globally maximal
cube root.  Put the prefix occurrence of `D` in the third copy of
`B^3`, and let `s` be any cube root at its label-three endpoint.  The
maximal-root separation lemma gives

```
s<r/2,
```

and the entire `s`-cube lies in `B^3`.  Item 5 gives `3s>delta`.
If `s<delta`, the factor `D` has period `s`, so

```
E:=D[s:]=D[:delta-s].                            (15a)
```

The two distinguished occurrences of `D` give identical suffix
occurrences of `E` with the same divergent continuations `3` and `2`.
If `|E|>=9`, then `E` ends in `G` and is a strictly shorter pair-hole
word.  If `|E|<9`, it is one of the nine explicitly checked suffixes of
`G`; lengths one through seven have standalone value one, while lengths
eight and nine have standalone value two.  Thus the branch `s<delta`
cannot hide another unclassified long pair word.

The remaining subcase is

```
delta<=s<r/2.                                    (15b)
```

Here the cube copies the complete border object into its first two root
copies.  This is already a strict *contained cube child*: its complete
cube lies in the displayed `B^3` and its root scale is below `r/2`.
Thus the immediate descent does not lose fitting.  What is not automatic
is that every later terminal continuation from this child remains in the
same slab; a long rescue may still exit through the distinguished
origin.  Subcase (15b) therefore returns to the contained halving
hierarchy with a certified pair, rather than creating a new unclassified
local mask.

There is also a strict rank inside the fixed equality quotient.
The base quotient in (3)--(4) has exactly `q` components, represented by
the residues of `B` modulo its period `q`.  The high prefix occurrence of
`D` in the third copy ends at cut `2r`.  If
`delta<s<r/2`, the equality between the last two root blocks of an
`s`-cube, at their first symbols, identifies the positions

```
2r-2s  and  2r-s.
```

Both lie in the same displayed copy of `B`; their `B`-indices differ by
`s`.  Here

```
0<s<r/2<q,
```

so the residues are distinct.  If `s=delta`, the last two blocks use
the already forced border equality.  The first symbols of the preceding
two blocks have `B`-indices `q-delta` and `q`, hence quotient residues
`q-delta` and zero.  They are distinct because `0<delta<q`.  Hence every
cube in (15b) strictly merges at least two of the `q` quotient
components.  It cannot recur unchanged in the enriched state

```
(pair endpoint, equality relation).
```

This is a finite recurrence charge within one `(r,q)` geometry.  As in
the deleted-one-symbol quotient, a component merge does not automatically
produce an ordered word with inherited fitting equations; it is not by
itself a global induction.

For `delta=5`, the same proof with the standalone value
`cn(22232)=1` gives the already classified terminal-marker hole.  The
case `delta=1` is the deleted-one-symbol seam branch.

## 5. A second scale bound

### Lemma 4

The full exact profile also forces

```
r<3q,                                             (15)
```

or equivalently `delta<2q`.

### Proof

Equation (4) says precisely that the word `B` has period `q`.  If
`r>3q`, then the first `3q` symbols of a generated occurrence of `B`
form a cube with root `B[0:q]`.  At the cut after those symbols, the
prescribed next label is

```
B[3q]=B[0]=2.
```

The displayed cube gives curling number at least three at that cut,
contradicting exactness.  If `r=3q`, the period-`q` word `B` is a third
power, contradicting primitivity of an incoming root whose cube attains
exact value three.  This proves (15).

## 6. Executed classification boundary

`research/z3_gap_four_pair_quotient.py` constructs the equality
components in (1)--(6), imposes the exact profile at every cut from
`e-6` through `e` for all three pair endpoints `e`, and independently
checks each satisfying model with exhaustive proper circular root
enumeration.

The computation confirms the theorem-level consequences:

* every equality survivor has `q<r`;
* every survivor with `delta<9` has `delta=1` or `delta=5`;
* the equality quotient has `q=min(r,q)` components.

It also prevents an invalid finite-state conclusion.  The deficits
`1,5` are not the only families surviving the full local pair slab.
Executed models occur for every tested `r=25,...,30` at deficits

```
1,5,9,11,12,
```

and at several larger deficits.  Requiring the first forward cut also
does not eliminate all models.  Hence neither the first uncovered cut
nor a finite alphabet of deficit values supplies the global rank.

## 7. Exact remaining load

Lemma 3 provides strict length descent

```
B (length r) -> D (length delta)
```

whenever `delta>=9`, and routes `delta=5` to the finite terminal-marker
graph.  What remains is to prove inheritance of the pointed fitting
conditions needed to iterate that descent.  The cube in (14) crosses the
left edge of `D`; translating it from the label-three occurrence to the
identical label-two occurrence is exactly the forbidden operation, so
the two occurrences do not share one autonomous left context.

The `delta=1` branch is the square-hole normal form in
`research/deleted_cube_profile_inheritance.md`.  A complete induction
must either:

1. turn its seam-crossing square mask into a shorter pointed object; or
2. show that the mask supplies the common fitting context missing from
   Lemma 3.

Without that step, the border descent is strict but not closed.

## 8. What a global-maximum closure would need

Let `R` be the largest primitive cube-root length in the proposed fixed
profile.  Once a square witness has a gap-four pair at its *endpoint*,
the preceding sections give a sharp dichotomy:

* a long incoming cube gives `q<r<=R`;
* a short incoming cube belongs to the finite terminal overlay, whose
  only closed circular macro is Q21 under the full fitting hypotheses.

This suggests the following exact missing statement.

> **Endpoint-capture lemma.**  Let a label-two cut in an aligned copy of
> a globally maximal root have a square witness of length `q>=R`.
> Then its deterministic forward defect chain either reaches a complete
> gap-four pair ending at a cut to which the same `q`-translation still
> applies, or produces a primitive cube root of length strictly below
> `R` which carries the unresolved square phase into the induction.

If the first alternative ended at a long incoming cube, Lemma 1 would
give `q<r<=R`, contradicting `q>=R`.  A short incoming cube would enter
the terminal classification.  If all such long square masks were
eliminated, every square at a phase of the maximal root could be chosen
with root below `R`; its complete square would then fit inside the
displayed maximal cube.  That is the missing positive inheritance step
in the proposed strict-profile descent.

Terminal ancestry and pair contraction do not by themselves prove the
endpoint-capture lemma.  Q64 gives an executed obstruction.  It has
maximum proper cube-root length 21 and long square witnesses

```
cut 22: roots 7,22,
cut 43: roots 7,21,43.
```

The length-22 and length-43 squares do not end at any pair.  They
transport internal complete pairs with unchanged continuation labels:

```
q=22:  16 -> 58,
q=43:  16 -> 37, 27 -> 48, 37 -> 58       (mod 64).
```

Thus an internal pair need not be a high-to-low loss node.  Q64 fails
the positive profile equations at exactly three cuts, `2,6,11`; all
no-cube and no-fourth constraints hold.  Any proof of endpoint capture
must use the missing positive equations to continue the transported
pair to a genuine endpoint defect.  Pair containment alone is false.

These values and mappings are recomputed in
`research/check_terminal_markers.py`.

## 9. The complementary long-square branch is an adjacent bridge

The pair hypothesis in Lemma 1 is used only at the last step.  Without
it, the same general equality quotient identifies the exact alternative
when the outgoing loss root is not shorter than its incoming cube root.

### Lemma 5

Consider a high cube of primitive root length `r`, followed in the
one-high/two-low ancestry circuit by a loss square of root length `q`.
Assume

```
N=q+2r,
q<3r,
B[0]=2,
P[0]=3,
P[-3r-1]=3,                                      (16)
```

and the component formula (3), but do not assume that the high endpoint
ends in `G`.  If `q>=r`, then `q>r` and

```
B[-1]=P[0]=3.                                    (17)
```

Thus the incoming cube `B^3` is followed by a second `3`; its endpoint
is the first cut of an adjacent-`33` bridge.

### Proof

If `q=r`, formula (3) gives `P[0]=B[0]=2`,
contradicting (16).  Hence `q>r`.

As in Lemma 1, the phase of `-3r-1` is

```
x=q-r-1.
```

Formula (3) gives

```
P[x]=B[(x-q) mod r]=B[-1].
```

The pointed defect in (16) makes this symbol three.  The high endpoint
also has `P[0]=3`, proving (17).

In the binary exact profile, the symbols on both sides of this `33`
are `2`: a third consecutive `3` would give a cube at a cut labelled
two.  Let the cube root at the second `3`-cut have length `s`.  The
adjacent bridge alternative of
`research/adjacent_double_bridge.md` gives exactly:

```
s=r,
r>2s+gcd(r,s),
or
s>=2r+gcd(r,s).                                  (18)
```

If `r` is globally maximal, the last case is impossible.  Hence an
outgoing loss with `q>=r` produces either an equal-root maximal bridge
or a cube root `s<r/2`.

Lemma 5 supplies the correct global split:

```
pair endpoint       -> q<r by Lemma 1,
non-pair q>=r loss  -> adjacent bridge by Lemma 5.
```

Q64 realizes the equal-root branch.  Therefore a global-maximum proof
must eliminate or descend equal-root adjacent bridges in addition to
capturing terminal pairs; pair contraction alone cannot bound all
square roots.

## 10. Minimality forbids a pair at the distinguished final cut

The predecessor-rotation lemma in
`research/critical_rotation_descent.md` supplies information which a
bare circular quotient does not have.  If a minimum-length critical word
`P` ends in `2`, then

```
cn(P[:-1])=1,        cn(P)=2.                    (19)
```

Consequently the distinguished final cut cannot be a gap-four pair
endpoint.

### Lemma 6

No minimum-length critical word ends in

```
G=222322232.                                      (20)
```

More generally, it cannot end in any border object `D` from Lemma 3,
because every such `D` ends in `G`.

### Proof

If `P` ended in `G`, then `P[-1]=2`, so (19) would apply.  But deleting
that final symbol leaves the suffix

```
G[:-1]=22232223=(2223)^2.
```

This square gives `cn(P[:-1])>=2`, contradicting (19).  A word ending
in `D` also ends in `G`, so the same argument applies.

The cut immediately before the final seam is excluded as well.  If a
complete `G` ended at cut `n-1`, then the autonomous word `P[:-1]`
would itself end in `G`, whose standalone value is two.  This again
contradicts (19).  In marker-end coordinates, neither of the two cuts
`-1,0` can therefore be the endpoint of a complete pair word.

Lemma 6 turns the origin issue into an exact prohibition: pair endpoints
may occur only at internal generated phases or in the seed part of the
distinguished lift, never at its final seam.  It does not by itself
eliminate a winding pair cycle, since such a cycle can cross the origin
between two pair endpoints.  A closing rank must use the autonomous-one
anchor `P[:-1]` to control that crossing edge, rather than rotating the
critical origin to the pair endpoint.
