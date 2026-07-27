# Halving children and crossing low-square masks

This note tests the missing bridge after the marker-count halving theorem in
Section 2 of `gadget_cycle_structure.md`.  The strongest natural local bridge
is false even under all of the binary critical hypotheses.  The exact
length-21 profile contains both a strict-drop mask and a strict-ascent mask
crossing the left boundary of one globally maximal cube.  Both overlaps miss
the Fine--Wilf threshold by exactly one.

The result is a reusable obstruction, not a counterexample to the Curling
Number Conjecture and not a classification of all crossing masks.

## 1. The proposed bridge and its exact failure

Consider a primitive binary circular word `P` with exact proper profile
`pc_P=P`, singleton `3`-runs, and the full first-copy fitting property.  Let

```
U^3=[L,L+3p)
```

be a tight primitive cube whose root length `p` is globally maximal among
proper circular cube roots.  The high phases inside `U` have the strict
halving descendants proved in `gadget_cycle_structure.md`.  The tempting
bridge is:

> every phase of `U` labelled `2` has a proper square internal to `U^Z`, or
> at least every ambient rescue square at a missing phase remains within the
> displayed `U^3` and supplies an attached smaller-scale object.

The following executed model refutes both alternatives.

## 2. Exact Q21 countermodel

Use the rotation

```
P = 223222322232322232223,          |P|=21.
```

Executed exhaustive proper-root enumeration establishes all of the following:

1. `P` is primitive and `pc_P=P`.
2. Every `3`-run is a singleton.
3. Every phase has a first-copy fitting witness of its displayed exponent.
4. The complete cube-root table at the six `3`-cuts is

   ```
   cut 2:  {4}
   cut 6:  {1}
   cut 10: {1}
   cut 12: {4}
   cut 16: {1}
   cut 20: {1}.
   ```

   Thus four is the global maximum cube-root length.

At cut twelve there is the tight maximal cube

```
[0,12) = (2232)^3.
```

Its primitive root is

```
U=2232,                    pc_U=(1,2,3,1).
```

Consequently the low phases zero and three of `U` have no proper circular
square.  Put these holes in the second copy of `U^3`, at lifted cuts four and
seven.

### Phase zero: a crossing strict drop

At cut four, the complete set of ambient proper square-root lengths is

```
{3}.
```

The square and its primitive root are

```
[-2,4) = (232)^2.
```

It begins before the parent cube at zero.  Its maximal period-three run is

```
[-3,5).
```

The parent maximal period-four run is `[0,12)`.  Their overlap has length
five, whereas the Fine--Wilf threshold is

```
4+3-gcd(4,3)=6.
```

Thus the overlap is threshold minus one.  This is a genuine strict scale drop
`3<4`, but it is not attached to the displayed parent interval.

### Phase three: a crossing strict ascent

At cut seven, the complete set of ambient proper square-root lengths is

```
{7}.
```

The square and its primitive root are

```
[-7,7) = (2232223)^2.
```

Its maximal period-seven run is `[-7,9)`.  Its overlap with the parent run
`[0,12)` has length nine, while the Fine--Wilf threshold is

```
4+7-gcd(4,7)=10.
```

Again the overlap is threshold minus one.  Here the only rescue is a strict
ascent `7>4`.

Both masks and the parent cube satisfy their first-copy fitting inequalities
in this rotation.  The failure is therefore not caused by circular
normalization or by loss of the distinguished fitting origin.

## 3. Sharp general overlap fact

Let two distinct maximal runs of least periods `p` and `q` overlap.  If the
overlap contains a complete conjugate of each primitive period root, then its
length is strictly less than

```
p+q-gcd(p,q).                                    (1)
```

Indeed, at or above this length Fine--Wilf gives the overlap period
`gcd(p,q)`.  A complete conjugate of a primitive root of length `p` or `q`
then has a proper period unless `p=q`.  If `p=q`, two overlapping
period-`p` runs belong to one maximal run, contrary to distinctness.

Equation (1) is sharp in the exact fixed-profile setting: both Q21 masks above
attain its integer maximum, threshold minus one.  Hence no argument using only
primitivity, maximal-run geometry, global maximality of the cube period,
first-copy fitting, and Fine--Wilf can force containment or a common period.

## 4. Corrected search obligation

The halving theorem remains valid for high phases.  What fails is closure of
its terminal period word under low witnesses.  A viable induction must retain
one of the following additional structures:

1. the whole circular endpoint graph, so threshold-minus-one masks can be
   charged around a complete cycle;
2. the exact terminal Q21 exception, followed by a proof that every other
   threshold-minus-one pattern creates a profile violation; or
3. an orbit-provenance condition stronger than exact circular profile and
   first-copy fitting.

It is unsafe to reuse either of these statements:

```
a globally maximal cube has a squareful primitive period word;
a strict-drop rescue square stays inside the displayed maximal cube.
```

Both are refuted by the executed model.

## 5. Reproduction

Run:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_halving_square_mask_bridge.py
```

The first command calibrates the repository convention against
`a(3)=5`, `a(8)=66`, and `a(22)=142`.  The second command exhaustively lists
all proper circular square, cube, and fourth-power roots used above, checks
the complete profile and fitting equations, extends the three displayed
periodic intervals maximally, and verifies both threshold-minus-one
equalities.
