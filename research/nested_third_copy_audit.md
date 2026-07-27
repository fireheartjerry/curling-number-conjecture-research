# Boundary obstruction to iterated third-copy halving

The globally maximal cube lemma gives a valid one-generation
conclusion.  Let `U^3=[l,l+3p)` be a globally maximal primitive cube.
At a `3`-cut

```
x=l+2p+r,       0<r<p,
```

in the third copy of `U`, every cube root `q` is contained and satisfies
`q<p/2`.

It is tempting to take the maximum `q` over all such cuts and apply the
same argument recursively to the internal third-copy cuts of that child.
The required containment assertion is false.  The child's own third
copy is

```
[x-q,x),
```

and it lies in the third copy `[l+2p,l+3p)` of `U` if and only if

```
r>=q.                                              (1)
```

Neither `q<p/2` nor containment of the whole child cube in `U^3`
implies (1).

## Executed local falsifier

Take

```
U=2332323,       p=7.
```

At circular cut offset `r=1`, direct enumeration gives the unique
primitive cube root `q=2` and no fourth power.  In `U^3`, this is

```
323232
```

on coordinates `[9,15)`.  It is wholly contained in `[0,21)`, and
`2<7/2`.  Its third copy is `[13,15)=32`, which straddles the parent
second/third-copy boundary at coordinate `14`.  The internal `3`-cut
at coordinate `13` is consequently outside the collection of cuts in
the third copy of `U`.

The boundary branch is not automatically contradictory.  Since
`r<q`, the child period supplies a `q`-root square at the crossed
parent boundary: the length from the child's left endpoint to that
boundary is `3q-r>2q`.  In the executed example, the boundary phase is
labelled `2`, has a period-two square, and has no period-two cube.

Therefore the proposed recursion has an exact dichotomy:

1. `r>=q`, when the child's third copy remains in the collected region;
2. `r<q`, when the child straddles the parent boundary and supplies a
   square there.

Only the first branch supports the proposed nested maximum argument.
The second is precisely a first-copy square-coverage interaction and
requires a separate completion-defect analysis.

`research/check_nested_third_copy_flaw.py` recomputes every root and
coordinate in this example.
