# First-top-marker rescue and the unequal-period split

This note combines the top-component automaton with the square required
immediately after a first maximum marker.  It gives a scale split, not a
contradiction.

Let `P` be a primitive circular fixed profile of length `p`, with
minimum `2` and maximum `M>=4`.  Put

```
L=M-2,       A=M-1,       H=M,
E=L A^M H.
```

The first `H` in every `H_A` component is preceded by `E` and is
isolated among the `H` positions.  Call the cut immediately after this
`H` a marker cut.

## 1. Every surviving marker copies an earlier marker

Let `e` be a marker cut.  Its profile value is below `M`; suppose it is
at least two, and choose a primitive maximizing root of length `q`.
The powered suffix contains at least two equal `q`-blocks.

Then

```
q>=|E|=M+2.                                        (1)
```

Indeed, equality of the last two root blocks copies the terminal `H`
from position `e-1` to `e-q-1`.  If `q<=M+1`, the copied position lies
among the preceding `L A^M` positions of the displayed marker, none of
which is `H`.

By (1), the entire final occurrence of `E` lies in the last root block.
Block equality copies it to the preceding root block.  Consequently

```
P[e-q-|E| : e-q] = E.                             (2)
```

Thus `e-q` is itself a first-top marker cut.  Choosing one maximizing
root at every marker defines a parent map on the finite marker set.
Every component of this directed functional graph contains a cycle.

Equation (2) aligns the marker suffix, but not the left boundary of the
earliest powered block.  This is precisely the pointed-return defect:
for a square, `e-2q` need not be a marker.

## 2. Exit ranks give a favorable edge on every parent cycle

The exact component theorem in `top_component_automaton.md` encodes
`A` by zero and `H` by one.  Every `H_A` component containing `H`
starts with the same deterministic word

```
W_N = product_(1<=n<=N) 0^M 1^(1+v_M(n)).
```

It has a finite exit type `(n,r)` and length below `M^M-1`.
In particular, two such components have a common deterministic prefix
until the shorter one exits.  At every legal exit, the next symbol of a
strictly longer component is `A`, while the shorter component has a
symbol at most `L`.

Orient a parent-cycle edge from the parent marker `e-q` to its child
`e`.  Record the length of the two top components after their common
marker prefix.  A finite directed cycle has an edge on which the child
length is at least the parent length.

If the inequality is strict, let `d` be their first continuation
mismatch.  The root equality at `e` and the common continuation give a
`q`-periodic interval

```
[-2q,d)
```

after translating `e` to coordinate zero.  At cut `d`, the child label
is `A`, while the corresponding parent label at `d-q` is at most `L`.
This is the favorable orientation of the first exit mismatch.

If the two component lengths are equal, their common match passes
through the complete top components.  One must then compare the
lower-level return data after the exits.  Equality of top exit types
alone does not make the whole return words equal.

## 3. Unequal-period rescue lemma

The following statement is independent of the particular ruler word.

Suppose a word has an interval `[-2q,d)` of period `q`.  Suppose its
cut at `d` has exact value `A>=3`, witnessed by a primitive `A`-root of
length `r`.  Assume the length-`q` root of the square is primitive.
Put

```
g=gcd(q,r).
```

If `q!=r`, at least one of the following strict inequalities holds,
according to which powered interval supplies the shorter overlap:

```
q > (A-1)r + g,                                   (3)
```

or

```
r > q + d + g.                                   (4)
```

Proof.  The `q`-periodic interval and the `r`-periodic `A`-power both
end at `d`.  Their overlap length is

```
O=min(2q+d, A r).
```

If

```
O>=q+r-g,
```

Fine--Wilf gives period `g` on the overlap.  The threshold contains a
complete root of each relevant length.  If `g<q`, a length-`q`
conjugate has the proper divisor period `g`; if `g=q<r`, a length-`r`
conjugate has period `q`.  The symmetric alternatives cover `g=r<q`.
Each contradicts primitivity.  Therefore the threshold fails.

If `O=Ar`, threshold failure rearranges to (3).  If
`O=2q+d`, it rearranges to (4).  The cases exhaust the definition of
`O`.

For the top-component mismatch, `A=M-1`, so (3) is

```
q>(M-2)r+g.
```

Thus a deficient marker edge either retains the same period `r=q`, or
introduces a rescue period separated from `q`: it is smaller by a
factor greater than `M-2`, or it is larger than `q+d`.

The equal-period branch extends the `q`-periodic interval to the left
through the `A`-power, but in the square case it still leaves a pointed
prefix of length `d`; it does not by itself supply a square ending at
the parent marker.

## 4. Executed finite evidence and exact limitation

`z3_max4_threshold_probe.py` enforces the normalized marker

```
233334
```

and the one required square immediately after it.  After removing:

* all fourth-power equivalences,
* the prohibition on fifth powers, and
* the condition that fourth roots use only high symbols.

the remaining global condition is only that every cut labelled `3` or
`4` has a cube suffix.  That relaxed primitive system is unsatisfiable
at the tested lengths

```
42, 43, 50, 52, 60, 80,
```

but it is satisfiable at lengths `90` and `100`.  Thus even the tempting
claim that global high-cut cube coverage plus one rescued marker forces
periodicity is false.  The exact fourth-power equations remain
load-bearing.

If primitivity is removed, the same relaxed system has periodic models.
For example, at length `42` the executed solver returns

```
(23333433324422)^3.
```

At length `80` it returns

```
(23333424)^10.
```

The periodic examples show that constant-period propagation is a real
branch, but the primitive relaxed models show that it is not the only
branch under cube coverage alone.  Equations (3)--(4) still allow
alternating large/small scales, so no well-founded rank has yet been
proved.

## 5. Clean and contaminated roots

An `M`-root is *clean*: every symbol in it belongs to `{M-1,M}`.
Indeed, at a cut through its final copy, the preceding `M-1` conjugate
copies give circular profile at least `M-1`, while maximality gives the
upper bound `M`.

Call a primitive `(M-1)`-root `R` *contaminated* if it contains a
symbol below `M-1`.  Suppose a state ends in

```
R^(M-1)
```

and follow the `|R|`-periodic continuation.  It must break before one
complete further copy of `R` has been appended.  Otherwise the state
would end in `R^M`, making the contaminated word `R` an `M`-root,
contrary to cleanliness.

At the first break, the pre-append state still ends in `M-1` copies of
a conjugate of `R`.  Its exact label is therefore at least `M-1`.  If
that label is `M`, choose a primitive clean `M`-root `S` of length `s`
and put `r=|R|`, `g=gcd(r,s)`.  The two co-terminal powers have
unequal periods: equality would make the clean root contain the same
low symbol as `R`.  Fine--Wilf threshold failure gives

```
s>(M-2)r+g,        or        r>(M-1)s+g.          (5)
```

The proof is the same overlap calculation as Section 3, now with
overlap length

```
min((M-1)r, M s).
```

The top-component bound makes every clean scale uniformly bounded:
the entire `M`-power lies in one `H_(M-1)` component, so

```
M s < M^M-1.                                      (6)
```

Only contaminated `(M-1)`-roots and lower-level return roots can be
unbounded.

The alternative first-break label `M-1` does not force another
contaminated root or a clean `M`-root.  The exact executed local
example

```
R=23,
cn(R^3)=3,
cn(R^3 3)=2
```

has the wrong continuation symbol `3` in place of the expected `2`
and drops immediately to the lower alphabet.  Both values and the
unique maximizing root length one after the break are recomputed by
the two independent implementations in `curling.py`.

Thus a complete state for this route must include the lower episode
between the contaminated break and the next top component.  At a
component exit the next clean maximum root may reset to the unary root
of the forced top entrance, so clean-root scale alone cannot be
monotone across levels.

The reset can also occur without leaving the top component.  For
`M=4`, the contaminated primitive root

```
R=233
```

has the executed exact sequence

```
cn(R^3)=3,        maximizing roots {3},
cn(R^3 3)=3,      maximizing roots {1},
cn(R^3 33)=4,     maximizing roots {1}.
```

The first appended `3` is again the wrong continuation in place of
`R[0]=2`.  Two unary `3` phases erase the contaminated scale and create
the unary clean maximum root.  Therefore a cross-level argument cannot
assert that every clean rescue exceeds the preceding contaminated
root; the deterministic zero runs provide exact downward resets.

There is an exact family for every `M>=4`.  Put

```
A=M-1,       L=M-2,       R=L A^(A-1).
```

Then `R` is primitive and contaminated, and

```
cn(R^A)=A,
cn(R^A A)=A,
cn(R^A A^2)=A+1=M.                                (7)
```

For the first equality, the displayed root gives the lower bound.
There are exactly `A` occurrences of `L`, so a powered suffix
containing `L` has exponent at most `A`; one avoiding `L` lies in the
terminal run `A^(A-1)`.  The same count proves the upper bounds after
the two appended `A` symbols, while their trailing unary runs have
lengths `A` and `A+1`.  At the last state the unique maximizing root
has length one.  Thus the reset from contaminated scale `M-1` to clean
scale one is uniform in the maximum.

There is a complementary family which realizes the *entire* forced top
entrance, not only its last two symbols.  Keep

```
A=M-1,       L=M-2,
```

and put

```
Q=A^A L.
```

For every `0<=t<=A`,

```
cn(Q^A A^t)=A,
```

while

```
cn(Q^A A^(A+1))=A+1=M.                            (8)
```

For the lower bound with `t<=A`, write `Q=UV` with `U=A^t`.
The conjugation identity

```
Q^A U = U(VU)^A
```

supplies an `A`-power suffix.  There are exactly `A` occurrences of
`L`; a powered suffix containing `L` has exponent at most `A`.  A
powered suffix avoiding `L` lies in the terminal unary run `A^t` and
also has exponent at most `A`.  This proves the first equality.  At
`t=A+1`, the terminal unary run gives exponent `A+1`; the same occurrence
count bounds every suffix containing `L` by `A`, proving the second
equality.

Thus the deterministic output from `Q^A` is

```
A^(A+1) M = (M-1)^M M,
```

which is exactly the mandatory entrance of a maximal `H_(M-1)`
component.  The long contaminated root has length `M` through the first
`A` outputs, ties the unary root at the last `A` cut, and is replaced by
the unary maximum root at the next cut.  Consequently the forced
entrance word itself supplies no monotone root-scale descent.

`research/check_top_marker_rescue.py` independently executes (8), and
all maximizing-root sets, for `M=4,5,6,7`.
