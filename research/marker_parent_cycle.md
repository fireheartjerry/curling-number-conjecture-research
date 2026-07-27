# A marker-parent cycle does not force one more copy

This is an exact countermodel to a return-marker argument, not a circular
fixed profile.

Let

```
E=233334
```

and use the length-31 token cycle

```
U=0010200100101001020010200100101.
```

Its proper circular curling profile is identically two.  Substitute the
three raw returns

```
Phi(0)=2 E,
Phi(1)=22323223323 E,
Phi(2)=2233 E.
```

The resulting primitive raw cycle has length 316.  It contains exactly
31 occurrences of `E`, one at the end of each declared return, and every
symbol immediately after an `E` is `2`.

`check_marker_parent_cycle.py` exhaustively recomputes the proper circular
curling number at all 31 cuts immediately after `E`.  Every value is
exactly two.  Therefore every such cut has a square root ending in `E`,
and the previous root boundary is another `E` cut.

Choose the least maximizing root at every marker cut and map that marker
to the marker one root length earlier.  The resulting finite parent graph
contains the two-cycle

```
marker 21 --(root 134)--> marker 8
marker  8 --(root 182)--> marker 21.
```

At both nodes the left boundary of the displayed square is itself another
`E` cut.  Nevertheless the proper circular curling number is two, not
three.  Closing a parent cycle aligns marker boundaries but not root
words: the two edges use different return blocks and different raw
lengths.  Consequently finite-cycle closure cannot turn an `a`-power
into an `(a+1)`-power without an additional invariant forcing the same
root block around the cycle.

