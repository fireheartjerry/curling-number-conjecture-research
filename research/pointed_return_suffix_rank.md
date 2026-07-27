# Pointed return suffix rank at the one-letter straddle

This note refines the unmatched-copy trichotomy in
`top_return_straddle.md`.  It gives a strict finite rank on pointed
return defects and a second rank for the exceptional tight square in
`recursive_threshold_signature.md`.  It also audits why neither rank
yet makes the return quotient an ordinary lower-maximum fixed profile.

## 1. Literature boundary

For a recurrent language, the set of first right returns to a fixed word
is a prefix code.  See Berthé--De Felice--Dolce--Leroy--Perrin--Reutenauer,
*Maximal bifix decoding*, Section 4, where first right returns are
defined and the prefix-code property is stated.  Recognizability results
for morphisms likewise give uniqueness of a tiling under hypotheses on
a morphic shift.

Those results do not align the unmatched root here.  The first marker
uses symbols to the left of the root start, while the equal root block
contains only its final symbol.  The argument below therefore retains
that point explicitly; it uses no recognizability theorem.

## 2. Exact tokenization of the one-letter straddle

Let `F` be a nonoverlapping marker ending in a symbol `e`.  Put a
boundary after every occurrence of `F`, and let a return be the exact
raw word between consecutive boundaries.

Suppose equal root blocks of length `q` occupy

```
[x,z),       [z,z+q),
z=x+q,
```

and `z` is a marker boundary.  Assume the sole straddling alternative:
an occurrence of `F` ends at

```
x+1.
```

Thus the root starts at the terminal symbol `e` of this marker.  List
all boundaries from the straddling one through `z`:

```
x+1=s_0<s_1<...<s_m=z,
H_i=P[s_(i-1):s_i].
```

### Lemma 1 (one-letter retokenization)

The aligned block `[z,z+q)` has the exact return-token decomposition

```
(e H_1), H_2, ..., H_m.                            (1)
```

In particular, `e H_1` is one exact return word.

### Proof

The first root is

```
P[x:z]=e H_1 H_2 ... H_m.
```

Root equality gives the same raw word on `[z,z+q)`.

For every `i>=1`, the marker ending at `s_i` lies wholly inside
`[x,z)`: the return `H_1` contains its terminal marker and has length
at least `|F|`.  Translation by `q` therefore gives marker boundaries
at

```
z+1+|H_1|+...+|H_i|.                               (2)
```

There is no additional marker boundary between consecutive cuts in
(2).  If one existed at least `|F|` symbols after `z`, translation
back by `q` would put a marker strictly inside one of the returns
`H_i`.  A marker ending fewer than `|F|` symbols after `z` would overlap
the marker ending at `z`, contrary to the marker hypothesis.

Hence (2) is the complete boundary list.  Its first gap is the raw word
`e H_1`; all later gaps are `H_2,...,H_m`, proving (1).

## 3. A strict suffix rank, and its orientation defect

Combine Lemma 1 with the other unmatched alternative from
`top_return_straddle.md`.

* With no straddling marker, the return `H` containing the unmatched
  start has

  ```
  H=J G,       J nonempty,
  ```

  where `G` is the first aligned return.

* With the one-letter straddle, Lemma 1 gives

  ```
  G=e H_1.
  ```

Orient an edge from the proper suffix to the containing return:

```
G -> H            in the no-straddle case,
H_1 -> e H_1      in the one-letter case.          (3)
```

Every edge in (3) strictly increases raw return length.  The graph on
the finitely many exact return types of one circular word is therefore
acyclic.  This is an honest strict rank on pointed defects.

It is not monotone in the direction needed by the usual rescue-parent
cycle.  Moving backward from the aligned boundary:

* the no-straddle case replaces `G` by the longer token `H`;
* the one-letter case replaces the longer aligned token `e H_1` by the
  shorter token `H_1`.

One can restore a formal suffix inclusion in the second case by also
retaining the return `D` ending at the straddling boundary:

```
e H_1 is a proper suffix of D H_1,
```

because `D` ends in `e`.  But `D H_1` is a pointed two-token block, not
the token attached to the next edge of the chosen rescue-parent
functional graph.  No closure theorem identifies those two-token blocks
with successive cycle states.  Thus cyclic monotonicity cannot be
claimed from (3).

There is a bounded entry subrank for consecutive one-letter edges.  Put

```
rho_e(H)=length of the initial run of e in H.
```

Equation (1) gives

```
rho_e(e H)=rho_e(H)+1.                              (4)
```

If `H` follows a marker ending in `e` in an exact circular profile, the
entire run has length `1+rho_e(H)`.  A run of the symbol `e` has length
at most `e+1`: at the cut before an `(e+2)`-nd consecutive `e`, the
trailing unary power would have exponent at least `e+1`, exceeding the
prescribed label `e`.  Hence

```
rho_e(H)<=e.                                       (5)
```

Equations (4)--(5) bound a chain consisting only of one-letter
promotions by `e` strict steps.

For every threshold `k>e`, prepending `e` creates no new `H_k`
position.  Every maximal `H_k` component word is the corresponding
component word of `H`, translated one position to the right, and every
entry witness wholly internal to `H` is transported with it.  The only
changed datum is the left context of the first such component: it gains
the new leading `e`.  The run rank `rho_e` records precisely this
pointed entry change.  The internal high-threshold data alone cannot
reverse the orientation defect above.

## 4. The exceptional tight square has a sibling rank

Use the notation of `recursive_threshold_signature.md`.  At a cut `d`
after an exit symbol `e`, put

```
C=C_(e+1)(d),       ell=|C|.
```

Consider the exceptional square edge

```
cn(T[:d])=2,
r=ell+1,
Y=C e,
d'=d-r.                                           (6)
```

The two square blocks show that `T[:d']` ends in `Y` and `T[:d]` ends
in `Y^2`.  Exact value two at `d` gives the exact maximal `Y`-run
counts

```
mu_Y(d')=1,
mu_Y(d)=2.                                        (7)
```

Indeed, a second copy already ending at `d'` would give three copies
ending at `d`.

The copied parent component satisfies

```
|C_(e+1)(d')|>=ell.                               (8)
```

If (8) is strict, component length is already a strict rank.  Suppose
equality holds.  Then the copied occurrence of `C` is the complete
maximal `H_(e+1)` component at `d'`.  The parent and child occurrences
of `C` are separated by the single symbol `e`, so they are consecutive
`H_(e+1)` children of one maximal `H_e` component.

Number those children from left to right inside that `H_e` component.
The child at `d` has index exactly one larger than the parent at `d'`.
Thus the parent direction `d -> d'` strictly decreases this child
index whenever component length is constant and the enclosing `H_e`
component is a proper linear interval.

There is also a first-child dichotomy.  If the parent occurrence is the
first `H_(e+1)` child of its enclosing `H_e` component, the
component-entry lemma forces that child to be the singleton

```
C=(e+1).
```

Otherwise the pointed signature contains an earlier `H_(e+1)` child.
Consequently every tight edge either reaches this bounded singleton or
has the strict sibling rank above.

There is one exact wrap exception.  If the enclosing `H_e` component is
the whole circular word, its children are cyclic rather than linearly
ordered.  The lifted sibling index still decreases by one in the parent
direction, but a cycle modulo the word length can wrap through the
distinguished origin.  In this exception every symbol is at least `e`
and some symbol equals `e`, so `e` is the global minimum.  Thus an
all-tight parent cycle is eliminated inside every proper `H_e`
component; the sole surviving form is the bottom-threshold circular
wrap.

Loose rescue edges can jump between enclosing `H_e` components and can
reset the child index.  The present rank therefore eliminates an
all-tight cycle away from the bottom-threshold wrap, but not that wrap
or a mixed loose/tight cycle.

## 5. Exact local family showing the remaining freedom

The one-letter geometry survives with arbitrarily long lower gaps under
all local marker and endpoint equations.  Let

```
M>=4,
A=M-1,
2<=e<=M-2,
F=A^M M e,
H_j=e^j F,
G_j=e H_j,
S_j=F[:-1] G_j^2.                                  (9)
```

The word `S_j` has exactly three occurrences of `F`.  Their consecutive
return words through the two displayed root copies are

```
H_j,       G_j=e H_j.
```

The final square has primitive root `G_j`, and

```
cn(G_j)=1,
cn(S_j)=2.                                        (10)
```

The isolated word `G_j` contains only one `M`.  A square suffix
containing `M` would require a second occurrence, while a square suffix
avoiding `M` lies after the final `M`, where only the single terminal
symbol `e` remains.  This proves its first equality in (10).

For the upper bound on `S_j`, count its occurrences of `M`.  There are
exactly three.  Their consecutive gaps are `|G_j|-1` and `|G_j|`, so no
cubic suffix containing `M` exists.  A powered suffix avoiding `M`
again lies in the final one-symbol suffix.  Hence no exponent at least
three is possible.  The displayed square proves the lower bound.

This family is local, not a circular fixed profile.  Long initial
`e`-runs eventually violate (5), and other off-marker profile equations
are not imposed.  It proves that the marker equation, the complete top
entrance `A^M M`, threshold-entry identities internal to that entrance,
and exact endpoint value two do not bound the raw suffix-extension
rank.

After the required A094004 calibration was executed,
`check_pointed_return_suffix_rank.py` recomputed both values in (10) with
both
independent curling-number implementations and verified all marker
boundaries for `476` parameter triples with

```
4<=M<=10,
2<=e<=M-2,
0<=j<=16.
```

## 6. Exact remaining quotient obstruction

The new facts are:

1. every pointed defect yields a strict proper-suffix edge between exact
   return objects;
2. one-letter chains have the additional bounded rank (4)--(5);
3. every tight square has either component-length growth or a strict
   predecessor-sibling step.

They do not yet produce an ordinary lower-maximum sequence.  Even if
all unmatched starts were aligned, the quotient symbols are exact return
identities while their prescribed outputs are numerical weights.
Distinct identities can share a weight.  Collapsing them can create
token powers which do not lift to raw powers.

This is not a hypothetical concern: `mixed_weight_counterexample.md`
gives primitive weighted fixed profiles with two distinct weight-two
tokens and a weight-three token.  Therefore a completion needs both:

* a closure theorem putting the pointed one- or two-token predecessor
  blocks on one monotone cycle; and
* a lifting argument that uses the internal raw profile equations to
  overcome noninjective weights.

There is also an actual-state obstruction before the weight issue.
Equation (10) gives it uniformly: the pointed block `G_j`, treated as a
standalone sequence, already has curling number one, while the full raw
prefix ending in the two displayed copies has curling number two.
Therefore deleting the left context to make a pointed block into a
candidate lower-maximum seed does not preserve even its current curling
number.  The actual orbit state is the full prefix; `G_j` and `D H_1`
are only suffix factors of such a state.

Neither required closure follows from the strict local ranks proved
here.
