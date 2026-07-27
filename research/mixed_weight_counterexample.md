# Mixed weighted profiles need not have injective weights

Let a weighted circular profile be a primitive circular token word `U`
with a weight map `w` into `{2,3}` such that the proper circular curling
number at the cut before `U[c]` is `w(U[c])`.

The following ternary word refutes injectivity even when both weights occur:

```
U = 0020010010100100020010010100100020010,
w(0)=w(1)=2, w(2)=3.
```

Direct enumeration over every cut, every proper root length `1<=p<37`,
and exponents through four gives

```
pc(U)=2232222222222222232222222222222232222.
```

This is exactly the positionwise weight word.  The word has token counts
`(25,9,3)`, no proper circular period, cube cuts exactly

```
(2,{1}), (17,{1}), (32,{1}),
```

and no fourth-power cut.  Thus the three occurrences of token `2` have
weight three, while the two distinct tokens `0,1` both have weight two.

The least square-root profile is

```
(15,1,1,7,7,1,7,7,1,3,3,2,2,1,5,3,1,1,22,22,1,22,22,1,
 3,3,2,2,1,5,3,1,1,15,15,1,15).
```

The model factors as `A A B`, where

```
A=002001001010010,   |A|=15,
B=0020010,           |B|=7.
```

`research/check_mixed_weight_counterexample.py` independently recomputes
all of these facts.  `research/z3_mixed_weighted_bool.py` produced the
model from the exact power equations.  The same encoding is unsatisfiable
for lengths `32` through `36`; this is bounded evidence only.

A second independently checked model occurs at length 40:

```
0101101000211011010110100021101000211011
```

with the same weight map.  Therefore the failure at length 37 is not an
isolated encoding artifact.

## Correction to the all-weight-two raw-lift grammar

For the maximum-four return quotient with marker `E=233334`, all return
weights equal to two do imply that every `4` is a selected terminal marker:
the first `4` of its `H_3` component is followed by `2`, so that component
ends and contains no later `4`.  It does **not** imply

```
Q = product_i 2^(a_i) 33334.
```

Between selected markers a return may contain arbitrarily many alternating
`2`-runs and `3`-runs before its terminal `E`.  A `2`-run can have length
three.  A marker-landmark cube need not contain any `4`: the concrete
return fragment

```
233233233233334
```

has suffix `(332)^3` at the cut before the first `3` of its terminal
`E`.  Direct computation gives curling number three there with maximizing
root length three.  Hence unique-`4` alignment cannot be applied to that
cube.
