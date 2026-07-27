# External-reset chains after contracting unary sources

This note connects the root-one external sources of
`terminal_source_gadget_bridge.md` to the gap-four-pair transition
alphabet of `terminal_root_closure.md`.  It keeps the distinguished
origin restriction explicit.  It does not eliminate the remaining
adjacent-`33` branch.

## 1. A selected unary external cube is exactly a gap-four pair

Work in a primitive singleton-`3` binary exact proper profile.  Let
`(c,1)` be a root-one/`2` external source, put

```
h=c-3,
```

and suppose the selected cube at `h` has root length one.  The external
source and selected cube give

```
P[h:h+4]   = 3222,
P[h-3:h]   = 222.                                (1)
```

There is no factor `2222`, because its following cut would have a
root-one fourth power while the binary profile label is at most three.
Thus `P[h+4]=3`.  The singleton-`3` hypothesis gives `P[h+5]=2`.
Combining these symbols yields

```
P[h-3:h+6] = 222322232.                           (2)
```

The length-nine word in (2) is the union of the two complete unary
markers

```
P[h-3:h+2] = 22232,
P[h+1:h+6] = 22232.                               (3)
```

Their unary-cube endpoints are `h` and `h+4`.  Hence a selected unary
external source is not a new terminal type: it is exactly the
gap-four-pair state of `terminal_root_closure`, Section 13.

## 2. Unary external edges cannot occur consecutively

The child square of the selected root-one cube ends at `h-1`.  Its
nearest preceding high cut is `h-4`, because (1) gives the intervening
three `2` symbols and the no-`2222` condition supplies the preceding
`3`.

If the next selected cube were also unary, it would produce a complete
unary marker with endpoint `h-4`.  Together with (3), the three unary
endpoints would be

```
h-4, h, h+4.
```

Lemma 4 of `terminal_root_closure.md` excludes three endpoints at
successive gap four: they force `(2223)^3` immediately before a cut
labelled `2`.  Therefore a directed extended-ancestry path has no two
consecutive selected unary external edges.

## 3. Finite transition alphabet and the critical origin

Contract the two markers in (3) to one pointed pair state.  Lemmas 5
and 6 of `terminal_root_closure.md` give the complete local transition
alphabet:

```
PAIR --root 4--> PAIR,
PAIR ----------> ADJACENT-33,
PAIR --q>=9----> translated PAIR.                 (4)
```

The third transition copies the complete length-nine pair, so it retains
its orientation and endpoint rather than merely transporting an
unlabelled square.  In the all-long circular quotient,
`gap_four_pair_quotient.md`, Lemma 1 gives the strict scale orientation
`q<r`; its large-deficit branch also exposes the shorter pointed border
word described there.  Thus an all-long pair-parent circuit cannot close
without leaving that quotient.  Every recurrent escape chain must use a
root-four return, an adjacent-double bridge, or a boundary loss in the
pointed border descent.

For a minimum critical word whose distinguished final symbol is `2`,
`gap_four_pair_quotient.md`, Lemma 6 forbids a complete pair at either of
the two final seam cuts `-1,0`.  Record in every pair state which open arc
contains the distinguished origin.  A translated pair-parent edge may
change that arc only by an explicit origin crossing; it may not rotate the
pair endpoint to the origin.  This is the origin bit which an escape-chain
transition must retain.

In Q21 the root-four return is stationary only after pair contraction.
In the physical lift it alternates the two root-four maximal cube
containers `[-10,2)` and `[-21,-9)`, which overlap in one symbol.  This is
the two-container macro audited in
`check_sink_scc_attachment_q21.py`.  The single-container attachment
statement remains false.  Equations (2)--(4) reduce selected unary resets
to the existing pair automaton, but they do not prove that every
nonunary reset is terminal or eliminate a mixed cycle using
`ADJACENT-33`.

The Q21 unary-source instances are recomputed by

```
python research/check_external_unary_pair_bridge.py
```

after the required A094004 calibration.
