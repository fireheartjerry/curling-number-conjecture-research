# Threshold containment and the globally longest maximum root

This note records two exact root-graph lemmas and combines them with the
top-component automaton.  The combination removes every replay mask after
choosing a canonical globally longest maximum root.  It does not control
the lower-alphabet episode between two top components.

## 1. Every threshold root is component-contained

Let `P` be a primitive circular fixed profile.  Suppose a primitive
`k`-root `R`, of length `r<|P|`, occurs as

```
R^k=[a,a+kr),             k>=3.
```

For `0<=t<r`, consider the cut

```
a+(k-1)r+t.
```

The preceding suffix of length `(k-1)r` is exactly `k-1` copies of the
conjugate

```
R[t:r] R[0:t].
```

The fixed-profile label at this cut is therefore at least `k-1`.
These `r` cuts read one complete copy of `R`; hence every symbol of `R`
belongs to

```
H_(k-1)={d:P[d]>=k-1}.                              (1)
```

All copies of `R` have the same symbols, so the whole displayed `k`-power
is contained in one circular component of `H_(k-1)`.

This applies at every threshold `k`, not only at the maximum label.

## 2. Exact source-scale dichotomy

Let a primitive `k`-root of length `r` end at cut `c`.  Its source cut
`d=c-r` has label at least `k-1`.  If the source label is at least `k`,
choose a primitive `k`-root of length `s` ending at `d`, and put
`g=gcd(r,s)`.

The two powers overlap in exactly

```
O=min((k-1)r,ks).                                   (2)
```

If `r!=s`, Fine--Wilf cannot reach its threshold `r+s-g`: at the
threshold the overlap contains a complete conjugate of each primitive
root, and period `g` gives a proper divisor period to the longer root
(or to both roots when `g` is smaller than both).  Therefore

```
O<r+s-g.
```

The two alternatives in (2) give the exhaustive scale split

```
r>(k-1)s+g,          or          s>(k-2)r+g.        (3)
```

If `r` is globally longest among all primitive `k`-roots, the second
alternative is impossible.  Thus a source backchain from a globally
longest root either keeps the same scale or drops by more than a factor
`k-1`.

After a drop, (3) permits a later jump by more than a factor `k-2`.
Consequently (3) alone is not a monotone rank.

## 3. Canonical orientation of a globally longest `M`-root

Now let `M>=4` be the maximum label.  Section 1 puts every `M`-power
inside one `H_(M-1)` component.  Encode `M-1` by `0` and `M` by `1`.
The exact component theorem in `top_component_automaton.md` says that
each component is a prefix of the valuation word and that every
nonunary `M`-root crosses

```
M^h
```

zero-runs for some `h>=0`.

Define

```
A_(-1)=0,
A_h=A_(h-1)^M 1.                                   (4)
```

An `M`-root crossing `M^h` zero-runs can end at an early offset in the
distinguished terminal one-run.  Moving its endpoint right within that
same one-run preserves the `M`-power until the endpoint offset is
`h+1`.  At that canonical endpoint the root begins in `0`; the valuation
block identity from the component theorem identifies the root word as
`A_h`.  Its physical length is

```
|A_h|=(M^(h+2)-1)/(M-1).                           (5)
```

Hence a globally longest root scale always has a canonical occurrence
whose root is exactly `A_h` and whose source symbol is `M-1`.
If every maximum root is unary, this statement uses `h=-1` and
`A_(-1)=0`; formula (5) remains valid.

## 4. The canonical longest root has no replay masks

Return to the original labels by replacing `0` with `M-1` and `1` with
`M`; retain the notation `A_h`.

The displayed canonical occurrence lies in an exact top component.
For every `0<=t<|A_h|`, the state

```
A_h^(M-1) A_h[:t]
```

ends in the outer `(M-1)`-power of the corresponding conjugate.  Thus
its curling number is at least `M-1`.

The valuation continuation theorem says exactly that an `M`-power is
present at every cut with `A_h[t]=M`.  This can also be read directly
from (4): every occurrence of `M` in `A_h` is the final symbol of an
embedded block

```
A_s=A_(s-1)^M M
```

for a unique hierarchy level `-1<s<=h`, so the prefix immediately before
that symbol ends in the displayed `M`-power.  No exponent above `M` can
occur, because the finite state is the actual suffix at a cut of the
fixed profile, whose maximum label is `M`.  Therefore

```
cn(A_h^(M-1) A_h[:t])=A_h[t]                      (6)
```

at every phase.  In particular, choosing a canonical globally longest
maximum root eliminates not merely nonterminal masked `M`-components but
all maximum-label replay masks.

Equation (4) also gives the exact endpoint identity

```
A_h^M M=A_(h+1).                                  (7)
```

Thus the autonomous replay constructs the next valuation block.

## 5. Why this does not yet contradict circularity

The component is allowed to exit before it accumulates `M` copies of
`A_(h+1)`.  At an exit, the orbit enters symbols at most `M-2`; the next
top component can restart with the unary maximum root.  Root scale is
therefore not monotone around the circle.

The reset is exact, not a missing estimate.  For every `M>=4`, put

```
B=M-1,       C=M-2,       R=C B^(B-1).
```

The executed regression `research/check_top_marker_rescue.py` verifies
for `M=4,5,6,7` the symbolic family proved in
`top_marker_rescue.md`:

```
cn(R^B)=B,
cn(R^B B)=B,
cn(R^B B^2)=M,
```

and the final maximum root is unary.  This realizes a reset from a
contaminated lower-threshold root to scale one without leaving the high
component.

The remaining load-bearing statement must constrain the lower episode
between top components, or prove that the hierarchy indices `h` around a
marker-parent cycle cannot return to their starting value.  Threshold
containment, the multiplicative split (3), and canonical unmasked replay
do not supply that cross-component constraint.

## 6. Colored exit markers give a monotone component parent map

There is nevertheless a useful monotonicity across the lower episode.
Let `C` be one complete maximal `H_(M-1)` component, and let

```
e<=M-2
```

be the first symbol after it.  Put `F=C e`, and let `d` be the cut after
this occurrence of `F`.

The word `C` contains only `M-1` and `M`, so the terminal `e` is the only
occurrence of `e` in `F`.  At cut `d`, choose a primitive maximizing root
of length `r` and exponent `a=P[d]>=2`.  Equality of its last two root
blocks copies the terminal `e` to distance `r`.  Since there is no `e`
inside `C`,

```
r>=|C|+1=|F|.                                      (8)
```

Consequently the complete suffix `F` lies in the last root block and is
copied into the preceding root block.  There is an earlier occurrence of
the same colored marker `F` ending at cut `d-r`.

Section 1, applied at threshold `a`, also bounds the rescue exponent.
The last root block contains `e`, while every symbol of an `a`-root is at
least `a-1`.  Hence

```
2<=a<=e+1<=M-1.                                   (9)
```

Let `C'` be the maximal `H_(M-1)` component ending at this copied
occurrence of `e`.  The copied word `C` is a suffix of `C'`, so

```
|C'|>=|C|.                                        (10)
```

Thus choosing one rescue root at every top-component exit defines a
parent map whose component length is nondecreasing.  On every directed
parent cycle, (10) is equality at every edge.  The copied suffix is then
the whole component:

```
C'=C.
```

In particular the complete valuation hierarchy, including every
canonical `A_h` occurrence and every corresponding `M`-root, is preserved
around a parent cycle.  The hierarchy index does not become strictly
monotone; it becomes constant on the recurrent part.

This reduces the recurrent obstruction to return words between identical
colored exits.  If all rescue root lengths on such a cycle were equal,
say the common length is `r` and the cycle has `d` edges and winding
`w`.  Then `dr=w|P|`.  The period-`r` intervals on consecutive edges
overlap and cover an interval of length `(d+1)r=w|P|+r`.  This interval
has periods `r` and `|P|` and exceeds the Fine--Wilf threshold.  It
contains a full copy of `P`, so `gcd(r,|P|)<|P|` would be a proper period
of `P`, contradicting primitivity.

Unequal lengths remain.  At a vertex following a rescue of exponent at
least three, the old root still supplies a nontrivial power, so a
co-terminal Fine--Wilf comparison with the vertex's own rescue root is
available.  The two exponents can differ, and the resulting separation
need not orient consistently around the cycle.  A rescue of exponent two
leaves only one old root block at the parent vertex, so there is no second
power to compare at all.  These square edges are exactly the unresolved
first-copy mask mechanism from the binary `Q64` analysis.

For the special standalone endpoint in (7), one has

```
A_(h+1) ends in M^(h+2),
cn(A_(h+1))=h+2.
```

When `h<=M-4`, the symbol `h+2` is absent from `A_(h+1)`, and therefore

```
cn(A_(h+1) (h+2))=1.
```

If an actual exit uses this standalone value, its marker is the preceding
construction with `C` ending in `A_(h+1)` and `e=h+2`.  Equations
(8)--(10) show that every ambient rescue copies the entire marker and has
exponent at most `h+3`.  This is a strict alphabet drop, but its
parent-cycle obstruction can still be carried entirely by exponent-two
edges.

## 7. Exact unequal square-cycle countermodel to the marker constraints

The square-edge obstruction in Section 6 is realized by a finite cyclic
model; it is not merely an artifact of weak inequalities.

Take `M=6`, the shortest formal top block

```
C=5^6 6,
```

and three exit colors `e in {2,3,4}`.  Encode each color by the
equal-length raw return

```
Phi(e)=2,4,C,e,
```

of length ten.  Use the primitive ternary token cycle

```
0010200100101001020010200100101.
```

Executed circular enumeration gives proper token curling number two at
all 31 cuts.  Consequently every token square maps to an aligned raw
square between complete colored exit markers.

`research/check_exit_marker_cycle_model.py` verifies all of the following:

* the raw cycle has length `310` and is primitive;
* all 31 marker cuts have exact raw profile value two;
* lifted primitive square-root lengths are

  ```
  10,20,30,50,130,180;
  ```

* every lifted root is at least `|C e|=8`, so it copies the complete
  component/exit marker;
* choosing the least root at every marker gives four parent 2-cycles,
  with unequal root pairs `(130,180)` or `(180,130)`.

Thus the component-boundary equations, constant component length,
primitivity, exponent bound (9), and exact marker-cut curling equations
do not contradict an unequal square-rescue cycle.

The same executed audit computes the full raw proper profile.  Its first
failure is cut one:

```
prescribed label 4, actual proper value 2.
```

There are no marker-cut failures.  The first missing condition is the
lower-gap profile immediately after the rescued `2` and before the top
entrance.  Any proof excluding the square cycle must therefore recurse
into lower-threshold profile compatibility; marker overlap algebra alone
cannot do it.
