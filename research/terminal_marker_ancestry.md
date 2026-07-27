# Terminal-marker ancestry: exact split, finite short macros, and a local
# all-long cycle

This note records the exact consequences of the terminal suffix

```
T_U=U^3 3 2,
U in {2,23,223,2223}.
```

It also gives a primitive circular countermodel to closing the ancestry
from the marker cuts alone.  The countermodel is not a circular fixed
profile: the missing equations at the cuts between its marker nodes are
load-bearing.

All finite and circular values quoted below are recomputed by
`research/check_terminal_marker_ancestry.py`.

## 1. The short-or-parent dichotomy

For each of the four roots, direct finite calculation gives

```
cn(T_U)=1,
```

and the only nonempty proper border of `T_U` is its final/initial
one-letter word `2`.

Let a longer state end in `T=T_U` and have a power suffix of exponent at
least two and primitive root length `q`.

If `2q<=|T|`, that power is already a suffix of `T`, contradicting
`cn(T)=1`.  Hence a root with `q<|T|` satisfies `2q>|T|`.  The overlap
of the last two root copies gives a border of `T` of length `|T|-q`.
The border calculation forces

```
q=|T|-1.                                             (1)
```

Put `R=T[1:]`.  In the short case the state ends in `R^k`, where `k`
is the exponent of the selected root.

If `q>=|T|`, equality of the final two root blocks copies the complete
terminal word.  If the current marker ends at cut `c`, another occurrence
of the same `T` ends at

```
c-q.                                                 (2)
```

Thus every rescue is either the unique short root (1), or a long
marker-parent edge (2).

## 2. A low loss and its incoming high cube

Suppose a maximal copied episode loses at a marker cut `c`: its selected
root has length `q>=|T|`, its parent marker is

```
p=c-q,
```

and the exact labels at the two cuts are

```
P[p]=3,  P[c]=2.                                     (3)
```

Fixedness at `p` supplies a primitive cube root of length `r`.  The same
border argument applied to this cube gives

```
r=|T|-1,  or  r>=|T|.                                (4)
```

There is also a strict scale bound

```
q<3r.                                                 (5)
```

If `q>=3r`, the complete `r`-cube ending at `p` lies in the first
length-`q` block of the square ending at `c`.  Translation by the
square period `q` would copy that cube to a cube ending at `c`,
contradicting the exact value two in (3).

The long incoming-cube branch has a pointed defect.  If `r>=|T|`, the
cube copies `T` to the cuts `p-r` and `p-2r`.  The final letters before
all three marker cuts are `2`.  If the symbol at `p-3r-1` were also
`2`, the cube could be shifted one symbol left and would end at `p-1`.
The terminal construction gives exact value two at `p-1`, so

```
P[p-3r-1]=3.                                         (6)
```

Under the singleton-`3` hypothesis, the next symbol is two.  The two
copied marker endpoints `p-2r,p-r` consequently also have label two.
At the first of them only one generated root block is present; at the
second, the root-`r` square is present; and at `p` the third copy
promotes the value to three.  This is the exact pointed state that an
all-long ancestry must carry.  Treating `p-3r` as another marker boundary
would erase (6) and incorrectly create a shifted cube at the preceding
two-cut.

## 3. Complete finite audit of the short incoming cube

Assume the first branch of (4).  Write

```
r=|T|-1,
R=T[1:].
```

The high parent ends in `R^3`.  By (5), a long loss edge has

```
|T|<=q<3r.
```

Its copied word is forced:

```
Z=suffix_q(R^3).
```

The second square copy begins at the high parent, so `Z[0]=3`.  The low
child ends in `Z^2`, whose finite curling number must be exactly two.
These conditions leave the following candidates.  An `overflow` is an
offset `j` with

```
cn(R^3 Z[:j])>Z[j];
```

it is an unconditional contradiction because adding older context cannot
lower a curling number.  A `mask` is an offset where the finite value is
smaller than the prescribed label; an external power crossing the left
edge of `R^3` is then still required.

```
U=2:
  q=6   overflow={}  masks={}
  q=10  overflow={}  masks={}

U=23:
  every candidate has an overflow

U=223:
  q=13  masks={1,4,5,6,7}
  q=16  masks={1,3,4,7,9,10}
  q=19  masks={1,3,4,6,7,10,12,13}
  q=23  masks={1,4,5,6,7,14,16,17}
  q=26  masks={1,3,4,7,9,10,17,20}

U=2223:
  q=16  masks={1,6,7}
  q=20  masks={1,5,11}
  q=24  masks={1,5,6,9,15}
  q=29  masks={1,6,7,20}
  q=33  masks={1,5,11,24}
  q=37  masks={1,5,6,9,15}
```

The omitted `q` values have an executed overflow certificate.  The two
unmasked `U=2` words are

```
q=6:   Z=322232,
q=10:  Z=3222322232.
```

Starting from `(2232)^3`, both words replay autonomously at every
intermediate cut.  These are the two short-parent macros visible in the
length-21 branch.  Every other non-overflowing short macro leaves at
least one explicit crossing-context mask, so the short split alone does
not finish the ancestry.

There is a useful maximum-cube corollary.  Every surviving `U=223` or
`U=2223` row has at least one mask whose required label is `3`.  At such
an offset `j`, an ambient cube root `s` must cross the entire finite
suffix `R^3 Z[:j]`; otherwise the finite computation would already see
the cube.  Therefore

```
3s>3r+j,
s>r.                                                  (7)
```

If the short incoming root `r` was chosen globally maximal among all
primitive cube roots, (7) is impossible.  Under that extra maximality,
the complete short branch reduces to

```
U=2, q in {6,10}.
```

This conclusion uses the executed finite table.  It does not eliminate a
short child below a larger ambient cube; in that case the high mask is an
explicit ancestry edge back to a larger scale.

## 4. Exact local all-long cycle

The following primitive circular word has length 41:

```
W=33223223223322332232232233223322322322332.
```

Take `U=223`, so

```
T=22322322332,  |T|=11.
```

The complete set of occurrences of `T` ends at cuts

```
0,13,27.
```

Their exact proper circular profiles and maximizing roots are

```
cut 0:   value 3, roots {14},
cut 13:  value 2, roots {13},
cut 27:  value 2, roots {14,27}.
```

The high cut has the cube

```
(23322322322332)^3
```

and the first low cut has the square

```
(3322322322332)^2.
```

Both roots are long.  The root-14 cube ends successively at the marker
cuts `13,27,0`; the root-13 square at cut 13 has the high marker cut 0
as its parent in the preceding circular lift.  Thus these equations form
one complete high-cube/low-loss ancestry cycle.

At every one of the three markers, the two preceding terminal cuts have
the required exact values:

```
cut e-2: value 3,
cut e-1: value 2.
```

After rotating by two symbols, the word begins with `2`; the high and
low cuts become `39,11,25`.  The selected witnesses satisfy the
first-copy fitting inequalities

```
3*14<=41+39-1,
2*13<=41+11-1,
2*14<=41+25-1.
```

This certificate disproves any contradiction based only on terminal
words, the short/long dichotomy, exact labels at the marker ancestry
nodes, incoming cubes, and fitting of the selected roots.

It does not satisfy `pc_W=W`: 16 of its 41 off-ancestry phases disagree.
Those intermediate phase equations are precisely what distinguishes an
actual generated fixed-profile cycle from the local all-long model.
Any further finite automaton must retain the complete generated return
between marker nodes, not only the marker type, label, exponent, and root
length.

## 5. The first positive refinement kills the length-41 macro

For this particular all-long geometry the first missing intermediate
equation is already decisive.  Keep only the word equalities

```
root-14 cube at cut 0,
root-13 square at cut 13,
root-14 square at cut 27,
T ending at cut 0,
```

together with the exact labels at the three marker histories.  Equality
closure has thirteen coordinate components.  The terminal word and
marker labels fix twelve of them.  The only free component is

```
{1,15,29}.
```

Its two assignments give exactly

```
32223223223322322232232233223222322322332,
33223223223322332232232233223322322322332.
```

Both words have proper circular value one at cut `1`.  Therefore adding
the first positive fixed-profile requirement at that cut is inconsistent:
whether its symbol is `2` or `3`, a square is required and none exists.
The 41-phase refinement stops at its first new phase; no later charge is
needed for this macro.

The checker tests every proposed root `1<=s<41` and records a forced
coordinate mismatch between the two length-`s` blocks ending at cut
`1`.  It also exhausts the geometric intersection types.  Write the
three forward marker intervals as

```
A: H -> L1,  length 13,
B: L1 -> L2, length 14,
C: L2 -> H,  length 14.
```

For a proposed square root `s`, classify the start `1-2s` and midpoint
`1-s`.  The exhaustive classes are:

```
(C,H):   s=1
(C,C):   s=2..7
(B,C):   s=8..14
(A,L2):  s=15
(A,B):   s=16..20
(H,B):   s=21
(C,B):   s=22..27
(L2,B):  s=28
(B,L1):  s=29
(B,A):   s=30..34
(L1,A):  s=35
(A,A):   s=36..40.
```

Every class is discharged by the explicit mismatch table emitted by the
checker.  This is a complete finite elimination of the length-41 local
cycle after one generated-phase equation, not a general elimination of
all-long cycles of arbitrary geometry.

## 6. General equality-component quotient

The stage-one contradiction is not universal.  There is, however, an
exact quotient for an arbitrary one-high/one-low all-long cycle.

Put the high marker at cut zero.  Let its incoming cube root have length
`r`, let the loss square from the high marker to the first low marker have
length `q`, and suppose one circuit has length

```
N=q+2r.
```

The three cube-copy endpoints are

```
q, q+r, 0 mod N.
```

Let `B` be the length-`r` cube root ending at zero.  The cube and square
equalities imply, for every `0<=i<N`,

```
P[i]=B[(i-q) mod r].                                  (8)
```

Here the right side describes a length-`N` segment of the periodic word
`B^Z`; it does not assert that the circular word `P` has period `r`.
When `q<r`, consistency across the circular seam adds exactly

```
B[j]=B[q+j],  0<=j<r-q.                              (9)
```

When `q>=r`, there is no extra equality on `B`.

To prove (8), the cube gives the formula on `[q,N)`.  The square ending
at `q` identifies `P[i]` with `P[2r+i]` for `0<=i<q`.  If the latter
index is still below `q`, apply the same equality once more.  Since
`q<3r`, at most two applications reach `[q,N)`, and adding `2r` does
not change the displayed residue modulo `r`.  This proves (8).

The first cube copy occupies the lifted interval `[-3r,-2r)`.  If
`q>=r`, it maps into nonnegative phases and (8) matches it without a new
condition.  If `q<r`, its wrapped part gives exactly (9).  These cases
exhaust the first copy.

Consequently the marker-power equality relation has

```
min(r,q) coordinate components.                       (10)
```

For `q>=r`, the `r` coordinates of `B` are independent.  For `q<r`,
(9) identifies positions along each residue class modulo `q`, leaving
exactly `q` components.

This yields a necessary-and-sufficient finite test for a proposed first
square root `s`.  Let

```
phi(x) = the component of B[((x mod N)-q) mod r].
```

Color the base components with the forced values from

```
B[0]=2,
B[-q mod r]=3,
suffix_|T|(B)=T,
P[-3r-1]=3.                                          (11)
```

The last color is the pointed defect (6).  Add, for every `0<=j<s`, the
component equality

```
phi(1-2s+j)=phi(1-s+j).                              (12)
```

A binary word satisfying the marker equalities and this square exists
if and only if no component produced by (12) contains both a forced `2`
and a forced `3`.  This is exact for the positive word equations.  To
require a primitive word and the exact profiles, add:

* for every proper divisor period of `N`, one inequality between the
  corresponding components;
* for each two-cut and every candidate cube root, one mismatch clause;
* for each three-cut and every candidate fourth-power root, one mismatch
  clause.

Thus the full first-phase condition is a finite Boolean formula on
`min(r,q)` component colors.  It is not a constant-size automaton: the
component count grows with the long roots.

There is a useful immediate rejection.  If (12) merges the exposed
component `phi(-3r-1)` with the terminal component `phi(-1)`, then it
forces the root-`r` cube to shift left and end at cut `-1`, contradicting
the required value two there.  This is exactly what kills every proposed
root in the length-41 macro.  It need not happen in general.

## 7. Stage-one survivors and refinement charge

The following three primitive circular words satisfy every marker-history
equation and also the first positive profile equation:

```
U=2, r=7, q=6, N=20:
32223223222322322232

U=223, r=22, q=21, N=65:
32232233232232232233223223223323223223223322322322332322322322332

U=2223, r=29, q=15, N=73:
3222322232223322223222322233232223222322233222232223222332322232223222332
```

At cut one their exact values are two, with roots `2,12,15`,
respectively.  Hence no general lemma can kill an all-long cycle at the
first off-marker phase.

Incremental SMT refinement gives:

```
N=20: cuts 1,2,3 SAT; adding cut 7 is UNSAT.
N=65: cuts 1,2 SAT; adding cut 3 is UNSAT.
N=73: cuts 1,...,10 SAT; adding cut 11 is UNSAT.
```

The formulas and models are produced by
`research/z3_terminal_component_refinement.py`; the displayed numeric
profiles are independently recomputed by
`research/check_terminal_marker_ancestry.py`.

There is a finite charge for one fixed geometry.  Start with the
`min(r,q)` components in (10).  A newly required positive power either
is already implied by the current quotient, in which case one more phase
becomes covered, or it merges at least two components.  A branch can
therefore make at most `N` coverage advances and `min(r,q)-1` component
merges before all positive phase equations have been processed.  Negative
cube/fourth clauses can only delete branches.

This proves termination of the refinement for fixed `(r,q)`.  It does
not give a uniform global rank: both `N` and `min(r,q)` are unbounded,
and a context mask can replace the geometry by a larger one.  A global
proof still needs a charge that survives those scale replacements.
