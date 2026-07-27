# Tight-gadget cycles: exact structural lemmas

This note isolates what follows rigorously from tight cube gadgets.  It
does not prove the singleton-`3` classification.

## 1. Weighted defect graph

Let `A=(a_0,...,a_(m-1))` be a primitive cyclic run code and let

```
Q(A) = product_i 2^(a_i) 3.
```

A tight gadget ending at a defect `i`, with span `s`, has a lifted
leading index `j=i-3s` and code

```
[alpha,C,g,C,g,C,beta],
alpha=a_j, beta=a_i, g=alpha+beta.
```

Its primitive physical root has run code `P=(C,g)`.  Direct the gadget
edge from its endpoint to its leading defect:

```
i -> j mod m,
weight(i->j)=s.
```

If one gadget is selected at each defect, every directed cycle
`i_0,...,i_(L-1)` has a positive integer winding number `w` satisfying

```
3 sum_(k=0)^(L-1) s_k = w m.                 (1)
```

Indeed, lift each edge as the strictly negative displacement `-3s_k`.
After one cycle the phase is unchanged modulo `m`, so the total
negative displacement is `-wm`.  Positivity of all `s_k` gives `w>=1`.

Let `N=|Q(A)|`, and let `p_k` be the physical root length of the
corresponding cube.  The cube from run `j` to run `i` has length

```
3p_k = sum_(r=j)^(i-1) (a_r+1) + a_i.        (2)
```

The full-run parts of the lifted cycle arcs traverse the code circle
exactly `w` times.  Their endpoint 2-runs are counted once more in
(2).  Therefore

```
3 sum_k p_k = wN + sum_(i in cycle) a_i.      (3)
```

For a `g=3` edge, the endpoint value `beta` and target value `alpha`
satisfy `alpha=3-beta`.  A cycle consisting only of `g=3` edges
therefore has even length, alternates endpoint values `1,2`, and has

```
sum_(i in cycle) a_i = 3L/2.                 (4)
```

A `g=2` edge is necessarily `1->1`; it is the only way that the
alternation in (4) can fail.

## 2. Globally maximal gadget contains a smaller defect graph

Choose a tight primitive cube `U^3=[l,l+3p)` whose physical root
length `p` is maximal among all proper cube roots in the circular
word.  Write its code span as `s`.

Let `x=l+2p+r`, with `0<r<p`, be a `3`-cut inside the third copy of
`U`, and suppose its corresponding entry in the circular root code is
a defect.  Its required cube is nonunary.  Let `q` be the length of
any primitive cube root at `x`, and put `d=gcd(p,q)`.  Global
maximality gives `q<=p`.

The `q`-cube cannot begin to the left of `l`.  If it did, its
intersection with `U^3` would have length `2p+r`.  This exceeds the
Fine--Wilf threshold `p+q-d`.  If `q<p`, the resulting period `d<p`
on a factor containing a complete conjugate of `U` contradicts
primitivity of `U`.  If `q=p`, the two period-`p` cubes overlap in
more than `p` symbols and their union extends the maximal
period-`p` run to the left, contradicting maximality of `U^3`.

The `q`-cube begins inside `U^3`.  If

```
2q+d >= p,
```

then its full length `3q` reaches the Fine--Wilf threshold
`p+q-d` and is at least `p`.  The overlap then contains a complete
conjugate of `U` and has period `d<p`, again contradicting
primitivity.  Hence

```
2q+gcd(p,q) < p,  and in particular q<p/2.   (5)
```

Thus the entire child cube lies strictly inside the parent cube.
The tightness lemma makes its leading position the beginning of an
ambient 2-run.  If its code span is `t`, its edge is

```
e -> e-3t
```

for the appropriate third-copy defect endpoint `e`.

There is a direct marker-count descent which does not depend on reading
the clipped endpoints from the physical containment.  The parent period
code has `s` entries in `{1,2,3}`: it is `(C,g)`, where
`g=alpha+beta` belongs to `{2,3}`.  Hence its physical length satisfies

```
2s <= p <= 4s.                                  (6a)
```

The child ends at a defect run of length one or two, so it cannot be a
unary cube.  Its primitive root contains `t>=1` singleton `3` markers,
and its period code likewise has `t` entries in `{1,2,3}`.  Therefore

```
q >= 2t.                                        (6b)
```

Since `gcd(p,q)>=1`, inequality (5) gives

```
4t <= 2q <= p-2 <= 4s-2.
```

Both `s` and `t` are integers, so

```
1 <= t <= s-1.                                  (6)
```

This proof is insensitive to both possible clipping runs and to wrapping
around the ambient circular word: the period-code length formula counts
the literal singleton `3` markers in one primitive root on the periodic
lift.

Fine--Wilf in marker coordinates strengthens (6).  Delete the two
clipped endpoint entries from the child's tight code.  If its primitive
period code is

```
R=(D,h),       |R|=t,
```

the remaining literal factor is

```
D,h,D,h,D,
```

of length `3t-1`.  This factor has code period `t`; because it occurs in
the periodic lift of the primitive parent code `P`, it also has code
period `s`.  Put `e=gcd(s,t)`.  If

```
3t-1 >= s+t-e,
```

Fine--Wilf gives period `e` on the factor.  The displayed inequality
also gives

```
3t-1-s >= t-e >= 0,
```

so the factor contains a full length-`s` conjugate of `P`.  Since
`e|s` and (6) gives `e<s`, that conjugate would be an `e`-periodic
proper power, contradicting primitivity of `P`.  Hence the threshold
inequality fails.  By integrality,

```
2t+gcd(s,t) <= s,                               (6c)
t <= (s-1)/2.                                   (6d)
```

Thus the child hierarchy halves in marker count as well as in physical
root length.  The argument uses only the unclipped interior, so neither
endpoint clipping nor wrapping changes it.

Between the two clipped boundary runs, the parent code is three
copies of `(C,g)`.  Therefore the child target, reduced modulo `s`,
is another defect entry of the primitive root code `P=(C,g)`.

Consequently every defect vertex of `P` has an internal child edge of
span below `s`.  Any deterministic selection gives a finite
functional graph on the defects of `P`, hence at least one directed
cycle.  This is a one-generation result.  It does not license
reapplying (5) with a child as parent: roots at the child's internal
cuts need not be at most the child's root length.

## 3. Exact ascent-or-descent dichotomy away from the maximum

The preceding proof gives a useful dichotomy without assuming that
`p` is globally maximal.  At the same internal cut
`x=l+2p+r`, a root `q<=p` obeys (5) and is strictly contained.

If `q>p`, its cube begins before `l` and ends at `x` inside `U^3`.
The overlap has length `2p+r`.  If `p` does not divide `q`,
Fine--Wilf and primitivity force

```
2p+r < p+q-gcd(p,q),
q > p+r+gcd(p,q).                             (7)
```

If `p` divides `q`, then `q>p` gives

```
q >= 2p.                                      (8)
```

Thus an internal defect either has a root below `p/2`, or a
left-crossing parent satisfying the strict scale jump (7), or the
divisible jump (8).  There is no uncontrolled root in the middle
range.  A proof based on iterated containment must nevertheless
handle the crossing-parent alternatives.

## 4. Isolated winding-one cycle is exactly `133233`

Assume a perfect matching of defects has been selected.  Let a
directed cycle satisfy all of the following:

1. every chosen edge has `g=3`;
2. its winding number in (1) is one;
3. no vertex of that cycle lies strictly inside one of its own lifted
   forward edge arcs; and
4. no vertex of any other cycle lies in those interiors.

The winding-one arcs concatenate to a single traversal of the code
circle.  Conditions 3 and 4, plus bijectivity of the matching, say
that every open edge interior is defect-free.

For an edge of span `s`, the open code is

```
C,3,C,3,C.
```

Defect-freeness forces `C=3^(s-1)`.  Its period code is then `3^s`,
which is primitive only for `s=1`.  Every cycle edge therefore has
span one and code

```
[1,3,3,2]  or  [2,3,3,1].
```

The endpoint values alternate, so the whole cyclic code is a power of
`133233`.  Primitivity of `A` leaves one copy:

```
A = 133233
```

up to rotation.

This terminal lemma uses neither the weak-square condition nor a
bounded enumeration.  What remains is to derive its four hypotheses.

## 5. Crossing lemma for nonnested gadget arcs

Tightness and singleton `3`-runs make each gadget cube a maximal run:
the symbol immediately before its left endpoint is `3` while its
period mate is `2`, and the symbol at its right endpoint is `3` while
its period mate is `2`.

Let two distinct gadget runs of periods `p,q` cross:

```
l < l' < r < r',
r-l=3p, r'-l'=3q.
```

Their overlap length `L=r-l'` satisfies

```
L < p+q-gcd(p,q).                             (9)
```

Otherwise Fine--Wilf gives their union the common period
`gcd(p,q)`.  If that period is smaller than one of `p,q`, a complete
root conjugate in the overlap contradicts its least-period property.
If `p=q`, the two runs belong to the same maximal period-`p` run,
contrary to distinctness.

Equation (9) shows that straddling is necessarily a shallow
Fine--Wilf crossing.  It does not by itself produce a weak-square
hole.  In the length-33 near-model the two period-21 long gadgets
cross with physical overlaps `4` and `8`, both below the threshold
`21`.  Any claimed laminarity theorem must explicitly eliminate this
shallow branch using square coverage; maximal-run geometry alone
cannot do it.

## 6. Exact remaining graph gaps

The following statements are not established by the lemmas above:

* existence of a perfect matching in the endpoint-to-leading-defect
  graph;
* exclusion of `g=2` edges;
* winding number one for every matched cycle;
* laminarity in the strong sense that every other cycle is wholly
  contained in one edge rather than straddling several edges; or
* a weak-square hole forced by every shallow crossing.

The weak containment relation “some vertex lies inside some edge” is
not useful: by (1), the forward arcs of every directed cycle cover the
entire circle `w` times.  Hence two distinct cycles contain vertices
of one another automatically.  A nesting proof must use whole-cycle
containment inside a single edge.

Executed diagnostics are in:

```
research/explore_gadget_cycles.py
research/z3_gadget_cycle_models.py
```

At code length `33`, the exact negative system (cube coverage at every
defect, no cube at any `2`-cut, no fourth at any `3`-cut, but no
positive square requirement) has two rotation classes.  Both have a
unique perfect matching, two `g=3` cycles, and winding one for each
cycle.  The A33 class has one WSQ hole; the other class has three.
Thus “at least one hole for a second cycle” is sharp at A33 in this
calibration, but remains unproved.

## 7. Terminal-edge residue lemma

Call a selected gadget edge *terminal* if every defect of its primitive
period code has an available tight span-one child.  The all-span-one
classification applies to that period code itself.  Hence:

* a terminal span-one edge has period code `(3)`; and
* every terminal edge of span greater than one has span six and period
  code a rotation of `133233`.

No WSQ assumption is needed for this statement.  A primitive period code
of span greater than one cannot be all `3`, and the local span-one
gadget equations force the alternating `1,2` defects at distance three.

Now consider a directed cycle all of whose edges are terminal and have
`g=3`.  Suppose for contradiction that its winding is two.  Equation
(1) implies `3|m`, so all vertices of the cycle have the same code-index
residue modulo three.

A span-one edge has no interior defect.  For a span-six edge, write its
period code as `P=(C,3)`, a rotation of `133233`.  The two defects in
`P` occupy one residue class modulo three.  Since `P[5]=3`, that class
is not residue two in the displayed orientation.  In the open gadget
arc

```
C,3,C,3,C
```

the defect offsets are therefore congruent to one or two modulo three,
never zero.  Thus no open edge arc contains another vertex of the same
cycle.

Every edge consequently joins consecutive cycle vertices in clockwise
order.  The open arcs are disjoint and make one traversal of the code
circle, so the winding is one, a contradiction.  Therefore an all-`g=3`
winding-two cycle must expose at least one nonterminal edge.

For a **fitting** terminal cycle, this excludes every larger winding as
well.  Section 2 of `critical_fitting_gadget_cycles.md` identifies winding
with the number of selected arcs crossing the common code origin.  A
terminal span-one crossing has endpoint `0,1`, or `2` and one of two
oriented factors; a terminal span-six `g=3` crossing has endpoint
`0,...,17` and one of eight oriented `Q21` factors.  These are exactly

```
2*3 + 8*18 = 150
```

lifted local assignments.  Pairwise equality on their overlapping code
positions leaves 132 compatible pairs and no compatible triple.  The
enumeration is exhaustive because endpoint range and oriented factor
determine every crossing assignment.  It is executed by

```
research/check_terminal_origin_crossings.py
```

Thus at most two fitting terminal edges cross one origin.  Every fitting
terminal cycle has winding at most two; the preceding winding-two
argument leaves:

> A fitting terminal all-`g=3` cycle has winding one.

This is the exact recursive alternative needed before invoking the
ascent/descent analysis of Section 3.

The terminal `g=2` orientation is also rigid.  Since `g=2` forces
`alpha=beta=1`, the only rotation of `133233` with final period-code
entry `2` is

```
P=331332.
```

The full clipped edge is

```
[1,33133,2,33133,2,33133,1].                 (10)
```

At offsets `3,6,9,12,15` from its leading run, (10) has the same-residue
defect chain

```
1,2,1,2,1.
```

The defects at offsets `6,9,12,15` have the forced local span-one
`g=3` gadgets.  The first defect, at offset `3`, has no span-one gadget:
the candidate `g=3` pattern would require leading value `2` rather than
the displayed `1`, while the candidate `g=2` pattern would require the
two displayed `3` values to be `2`.

Thus a terminal `g=2` edge has an exact exposed predecessor defect:
either that defect is uncovered, or its covering gadget is nontrivial
and continues the predecessor chain.

There is a sharp closure calculation.  If the endpoint at offset `18`
is identified cyclically with the exposed defect at offset `3`, the
code circumference is `15`.  At the first internal join, offset `6`,
the first-`2` cut has a cube with code span `h=3`.  The three clipped
blocks are

```
[capacity 2,3,3], [1,3,3], [1,3,3],
```

so the physical root has length ten.  The same cube exists at offsets
`r=0` and `r=1` of that length-two run.  This is the exact forbidden
cube in

```
A=133133233133233.
```

Hence the terminal `g=2` branch cannot close immediately: immediate
closure violates the no-cube condition, while nonclosure supplies a
strictly nontrivial predecessor gadget.  What remains is to prove that
an infinite sequence of these exposed predecessors must either close
or create a WSQ hole; Section 3 supplies the scale gap for that step.

## 8. Exact elimination of the one-residue `g=2` branch

The recursive predecessor gap at the end of Section 7 disappears once
the full negative hypothesis at `2`-cuts is used.

Assume that `3|m` and, after rotation, every defect of `A` occurs in
code-index residue zero modulo three.  Write

```
A=(b_0,3,3,b_1,3,3,...,b_(M-1),3,3),  m=3M. (11)
```

First, every `b_j` is in `{1,2}`.  If `b_j=3`, take the `3`-cut at the
end of the second spacer following `b_j`.  The terminal length-three
suffix and the preceding three full run blocks form four copies of
`2223`; equivalently, the code power criterion with exponent four and
code span one holds.  Its physical root has length four.  This is a
proper fourth power and contradicts the no-fourth hypothesis.

Here is the residue calculation for a primitive cube gadget ending at
`b_v`.  Its ambient code span is denoted by `s`.

If `s>1` and `3` does not divide `s`, the two join entries lie in the
two fixed spacer residues and hence both equal `3`.  For every internal
offset `1<=j<s`, the three equal entries at offsets

```
j, s+j, 2s+j
```

occupy all three residues modulo three.  Two of them are fixed spacer
entries, so their common value is `3`.  Thus the primitive period code
is `3^s`, which is a proper power because `s>1`.  This is impossible.

If `s=3h`, both joins lie in the `b` residue.  At an endpoint
`b_v=2`, their common value is

```
g=alpha+b_v >= 3,
```

whereas every `b` entry is at most two.  Hence this case is impossible
as well.  The only cube gadget covering `b_v=2` therefore has `s=1`.
Its displayed code is

```
[alpha,3,3,2],  alpha=1.                    (12)
```

The leading-capacity condition gives `b_(v-1)>=1`.  If
`b_(v-1)=2`, the capacity in (12) is strict by one.  Shift the cube
one symbol to the left.  In the exact code criterion this changes the
terminal offset from `r=2` to `r=1`; the required leading capacity
becomes `b_(v-1)>=2`, while the two join entries remain `3`.  Thus a
cube ends at the cut after the first `2` of the run `b_v=2`, contrary
to the no-cube hypothesis at `2`-cuts.  Consequently

```
b_v=2  implies  b_(v-1)=1.                  (13)
```

In particular, the cyclic word `b` contains no factor `22`.

There is an even shorter local obstruction to `11`.  Suppose

```
b_(v-2)=b_(v-1)=1.                          (14)
```

At the cut before the first `2` of run `b_v`, use exponent three,
terminal offset `r=0`, and ambient code span three.  The root code is

```
(b_(v-1),3,3)=(1,3,3),
```

and its physical length is

```
(1+1)+(3+1)+(3+1)=10.
```

The second root copy agrees because `b_(v-2)=1`; the first copy needs
only the leading-capacity inequality `b_(v-3)>=1`, which always holds.
All spacer comparisons are `3=3`.  Thus (14) creates a period-ten cube
at a `2`-cut.  For `M>1`, code span three is proper because `3<3M`.
Therefore

```
b contains no cyclic factor 11.              (15)
```

The exceptional circumference `M=1` is direct.  If `b_0=1`, its
defect has no primitive proper cube gadget: span one would require
leading capacity two, and span two has the nonprimitive period code
`33`.  If `b_0=2`, its span-one cube has strict leading capacity and
shifts to the forbidden offset `r=1`.  The case `b_0=3` was already
excluded by the fourth-power calculation.

Equations (13) and (15) force `b` to alternate cyclically.  Hence `M`
is even and `b` is a power of `12`.  Since `A` is primitive, `b` is
primitive, so only one copy remains.  Up to rotation,

```
b=12,  A=133233.                             (16)
```

This proves the complete one-residue classification under cube
coverage at defects, no cubes at `2`-cuts, and no fourth powers at
`3`-cuts.  No winding, predecessor-chain, or bounded enumeration is
needed.  In particular, a `g=2` edge would itself expose `11` at its
leading boundary and is excluded by the period-ten obstruction.

The executed identity checks for (12)--(15) are in

```
research/check_one_residue_obstructions.py
```

## 9. Complete classification when every defect has a fitting terminal edge

Assume now that every defect has a fitting terminal edge in the sense
of Section 7.  A perfect matching need not be assumed: it is forced in
this branch.

### 9.1 Terminal `g=2` is locally forbidden

The terminal `g=2` factor (10) begins

```
1,3,3,1,3,3,2.
```

At the first-`2` cut of the final displayed run, the ambient code-span
three cube criterion holds: the two complete marker triples are
`(1,3,3)`, and the leading triple needs only a capacity of one in its
first entry.  Its physical root length is ten.  Thus a terminal `g=2`
edge gives a forbidden cube at a `2`-cut without any cyclic closure
assumption.  Every terminal selected edge is consequently `g=3`.

Define a canonical target map on the defects.  If a defect has a
span-one edge, select that edge.  Otherwise select a fitting terminal
span-six edge; all span-six choices at a fixed endpoint have the same
target, eighteen code positions earlier.

These selected edges are fitting.  If any span-six edge exists then
properness gives `m>6`, and the fitting inequality
`3<=m+i-1` holds for every span-one endpoint `i`.  If no span-six edge
exists, the assumed fitting terminal edge at every defect is itself
span one.

This map is injective.  Two selected span-one edges cannot have the
same target, and neither can two selected span-six edges.  A collision
between the span-one edge ending at `j+3` and a span-six edge leading
at `j` is also impossible.  In a terminal `g=3` span-six factor, all
six internal defects occupy residue one or residue two relative to
`j`, never residue zero.  In particular the entry at `j+3` is `3`,
not a defect.  Since the defect set is finite, the injective target map
is bijective.  It is the required fitting perfect matching.

By Section 7, each selected cycle has winding one.  Equation (1) then
gives `3|m`.  Every edge preserves its canonical code-index residue
modulo three.

A terminal span-one edge has two open entries, both equal to `3`.  A
terminal span-six edge has six open defects, spaced three positions
apart, and all six occupy one of the other two residues.  It has no
open defect in its endpoint residue.  Since the forward arcs of a
winding-one cycle partition the code circle, there cannot be two
selected cycles in the same residue.  Hence there are at most three
cycles.

### 9.2 Macro counting

For a selected cycle `r`, let

```
L_r = number of its vertices,
x_(r,s) = number of its span-six edges whose six internal
          defects belong to cycle s,
x_r = sum_(s != r) x_(r,s).
```

Its span-one edges contribute code displacement three and its span-six
edges contribute displacement eighteen.  Winding one gives

```
m = 3L_r+15x_r.                               (17)
```

The arcs of cycle `r` partition the circle.  Every vertex of another
cycle `s` lies in a span-six arc of `r`, and every such arc contains
exactly six vertices of `s`.  Therefore

```
L_s = 6x_(r,s)  for r != s.                   (18)
```

With two cycles, write `x=x_(0,1)` and `y=x_(1,0)`.  Equations
(17)--(18) give

```
L_0=6y, L_1=6x,
6y+5x=6x+5y,
```

so `x=y`, `L_0=L_1=6x`, and

```
m=33x.                                        (19)
```

With three cycles, put `L_s=6y_s`.  Equation (18) says
`x_(r,s)=y_s` for each `r!=s`.  Equation (17), divided by three, is

```
m/3 = 6y_r+5 sum_(s!=r) y_s.
```

Comparing two residues gives `y_0=y_1=y_2=:y`.  Thus every ordered pair
of distinct residues occurs as the host/inside pair of exactly `y`
long edges, and

```
L_r=6y, x_r=2y, m=48y.                        (20)
```

The three-cycle numbers are incompatible with the geometry.  Orient a
long edge forward from its leading vertex to its endpoint, and suppose
its host residue is `r` and its internal-chain residue is `s`.  Put

```
delta=(s-r) mod 3 in {1,2}.
```

The six internal vertices are at offsets

```
delta, delta+3, ..., delta+15.
```

The last of these vertices is the leading vertex of the long edge that
bridges this chain to the next chain of cycle `s`: all five gaps inside
the chain are span one, while the macro count leaves exactly one
span-six edge between consecutive chains.  Hence the successor long
edge starts at forward displacement

```
15+delta, namely 16 or 17.                    (21)
```

Successor is a permutation of the finite set of long edges, so the sum
of all displacements (21) is an integer multiple of `m`.  In the
three-cycle case there are `3y` ordered residue pairs with
`delta=1` and `3y` with `delta=2`.  The sum is

```
3y*16+3y*17=99y,
```

which is not divisible by `m=48y`.  Thus three terminal cycles are
impossible.

### 9.3 The two-cycle macro is primitive only at length 33

In the two-cycle case, successor alternates between the two residues.
The total successor displacement over all `2x` long edges is

```
x*16+x*17=33x=m.
```

Every successor orbit has positive winding, so there is exactly one
orbit.  Two successive long-edge starts of the same residue are
therefore separated by exactly `33`.

Values flip across every selected `g=3` edge.  Between corresponding
long-edge starts a cycle traverses six edges, so the leading value is
unchanged.  The internal-chain offset, the leading value, and the first
internal value uniquely determine one of the eight oriented `Q21`
factors.  Consequently the complete code is `33`-periodic.  Primitivity
forces `x=1`.

There are then only eight compatible overlays of the two oriented
`Q21` factors, giving four rotation classes:

```
representative                         failed WSQ run
113323313323313323233133233133233      3
123313323313323313233133233133233      2
131332331332331332233133233133233      20
133213323313323313323133233133233      6
```

At each displayed run, the code-square equation fails for every
`1<=h<33`.  The complete capacity/mismatch certificates and the
eight-to-four overlay enumeration are produced by

```
research/enumerate_terminal_two_cycle_macros.py
```

Thus two terminal cycles contradict square coverage.

With one terminal cycle, a span-six edge would contain defects of a
second cycle.  Hence every edge has span one, and Section 4 gives
`A=133233` up to rotation.

Combining the cases:

> If every defect has a fitting terminal edge, the exact
> square/no-cube/cube/no-fourth profile forces `A=133233` up to
> rotation.

The remaining task is not a terminal-macro classification.  It is to
show that a nonterminal selected edge can be descended or replaced
without losing the common fitting matching hypotheses.

## 10. Finite halving rank and the obstruction to lifting Section 9

There is a sound unpointed rank for the cube hierarchy.  The following
alignment argument repairs the phase problem in a naive repeated use of
Section 2.

Let

```
U^3=[a,a+3p)
```

be a globally maximal primitive cube.  At every `3`-cut in its third
copy choose a cube witness.  Global maximality and Section 2 put every
chosen root below `p/2` and its whole cube inside `U^3`.  Let `q` be
maximal among the chosen root lengths, and write a corresponding child
as

```
V^3=[x-3q,x),  x=a+2p+r,  0<r<p.
```

Now take a `3`-cut `y` in the third copy `[x-q,x)` of `V`.

* If `y>=a+2p`, it is already in the parent third copy and its selected
  witness has root at most `q`.
* If `y<a+2p`, put `y'=y+p`.  Since

  ```
  y >= a+2p+r-q
  ```

  and `q<p/2`, the translated cut `y'` lies in the parent third copy.
  Let its selected root be `s<=q`.  Translate that cube back by `p`.
  The lower endpoint stays inside `U^3`, because

  ```
  y-3s >= a+2p+r-q-3q
       =  a+2p+r-4q
       >  a.
  ```

  Period `p` of `U^3` therefore constructs an `s`-root cube ending at
  `y`.

Thus every `3`-cut in the third copy of `V` has a witness of root at
most `q`, even when that third copy straddles the boundary between the
second and third copies of `U`.  Applying Section 2 relative to `V`
gives, at every nontrivial internal defect,

```
2s+gcd(q,s)<q, and hence s<q/2.               (22)
```

Choose one bounded witness at every such cut and repeat the same
construction.  Positive integer root lengths fall by more than a
factor of two at each nonterminal generation.  Hence every gadget
reached below the globally maximal parent can be assigned a finite
*unpointed halving rank*: rank zero means that all defects of its
primitive period code have span-one children, and a nonterminal rank
is one plus the largest rank reached by the bounded child selection.
The depth is at most logarithmic in the initial physical root length.

The marker-coordinate argument (6c) applies at every one of these
generations as well.  If the current primitive period code has `u`
markers and the selected internal child root has `v` markers, then

```
2v+gcd(u,v) <= u,
```

so the marker count drops to at most `(u-1)/2`.  A hierarchy beginning
with `u` markers consequently has depth at most `floor(log2(u+1))`.
This strengthens finiteness of the hierarchy but does not repair either
pointed loss below.

This rank does not yet justify induction using Section 9.  There are
two precise losses.

First, the cube translated from `y'` to `y` is guaranteed to be a
factor of `U^3`, but fitting is pointed at the single deleted-copy
origin.  Translation by `-p` can move its beginning to the left of
`1-N`.  A fitting witness at the canonical representative of `y` need
not remain fitting when translated into this common lift.  Therefore
the rank-zero leaves do not automatically supply the simultaneous
fitting terminal target map required in Section 9.  The replacement
at the exposed first-copy cut can be a *larger* unrelated cube: the
small terminal child exists only in the later local copy and is not a
circular witness at that ambient phase.

Second, weak-square coverage is not inherited by a primitive period
code.  A first-copy `2`-cut of a terminal `Q21` leaf can have no square
wholly inside the displayed leaf prefix while still being squareful in
the ambient word: a larger square may cross the leaf or parent
boundary.  Such a crossing square is a *first-copy WSQ mask*.  Replacing
a nonterminal parent by its terminal descendants can delete precisely
that mask, so the failed-WSQ certificates in the two-cycle macro table
cannot be applied before controlling these crossing squares.

The remaining induction lemma must therefore do more than descend cube
periods.  It must show that every loss of fitting or every first-copy
WSQ mask either supplies a fitting terminal replacement, creates a cube
at a `2`-cut, or moves to a strictly smaller pointed rank.  The
unpointed halving rank alone does not establish any of those three
alternatives.

This is not a hypothetical distinction.  The exact symbolic search

```
python research/z3_q21_left_context.py --max-left 80
```

finds a tight nonperiodic left context of length `56` that realizes the
entire first-copy `2/3` profile of the standard terminal `Q21` root,
while explicitly excluding a preceding literal `Q21` copy.  No such
context exists at lengths `1` through `55`.  The first exposed terminal
cube witnesses at physical phases two and four are then replaced by
roots of lengths four and twenty, respectively, as recomputed by
`research/z3_q21_early_predecessors.py`.  Requiring that the proposed
period-twenty predecessor cube and its generated continuation themselves
obey the profile makes the branch unsatisfiable in
`research/z3_q21_predecessor_node.py`; that extra generated-context
condition, not local terminality, is load-bearing.
