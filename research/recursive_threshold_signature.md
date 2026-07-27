# Recursive threshold signatures at colored exits

This note proves the exact monotonicity of the nested threshold components
copied by an exit rescue.  Component lengths and component words become
constant on a parent cycle.  Separator colors have one exceptional
transition: a tight exponent-two edge.  Even after all lengths and
separators are constant, the length-21 exact profile realizes an unequal
bottom-level parent cycle.

## 1. Nested suffix components

Let `P` be a primitive circular fixed profile with maximum `M`, and let
`d` be the cut immediately after a symbol

```
e=P[d-1]<=M-2
```

which exits a maximal `H_(M-1)` component.  For every

```
e+1<=k<=M-1,
```

let `C_k(d)` be the maximal nonempty suffix immediately before this
terminal `e` whose symbols lie in

```
H_k={x:P[x]>=k}.
```

Write

```
ell_k=|C_k(d)|,
sigma_k=P[d-ell_k-2]<k.                            (1)
```

The components are nested:

```
ell_(e+1)>=ell_(e+2)>=...>=ell_(M-1).              (2)
```

Choose a primitive maximizing rescue root of length `r` and exponent

```
a=P[d]>=2
```

at cut `d`.  Equality of its last two root blocks copies the terminal
`e` to position `d-r-1`.

The component `C_(e+1)(d)` contains no occurrence of `e`.  Therefore

```
r>=ell_(e+1)+1.                                    (3)
```

Put `d'=d-r`.  For every level in (2), the complete word

```
C_k(d) e
```

is a suffix of the last root block and is copied ending at `d'`.
Consequently `d'` is another exit of color `e`, and

```
C_k(d) is a suffix of C_k(d'),
ell_k(d')>=ell_k(d).                               (4)
```

Thus the vector of nested component lengths is componentwise
nondecreasing under the parent map.

## 2. Loose levels are copied exactly

Suppose

```
r>=ell_k+2.                                        (5)
```

The separator `sigma_k` in (1) then lies inside the last root block, so
block equality copies it immediately before the copied occurrence of
`C_k(d)`.  The copied separator is below `k`; hence the parent
`H_k` component cannot extend farther left.  Therefore

```
C_k(d')=C_k(d),
ell_k(d')=ell_k(d),
sigma_k(d')=sigma_k(d).                            (6)
```

Any strict increase in (4) can occur only at a *tight* level

```
r=ell_k+1.                                         (7)
```

Because of (2)--(3), tight levels form an initial plateau of the longest
low-threshold suffix components.

At a tight level the last root block is exactly `C_k(d)e`.  The copied
terminal `e` is the original separator, so

```
sigma_k(d)=e.                                      (8)
```

If `a>=3`, a third equal root block precedes the parent copy and also
forces

```
sigma_k(d')=e.                                     (9)
```

For `a=2`, there is no third block.  The parent separator lies outside
the powered factor and is not determined.

Hence a tight square is the only edge on which the nested separator
signature can change.

## 3. Consequence on a parent cycle

Fix an exit color `e` and choose one rescue root at every such exit.
The resulting parent map acts on a finite set.  On a directed cycle,
(4) gives a cyclic chain of componentwise nondecreasing integer vectors,
so every inequality is equality.  At every level,

```
ell_k(d')=ell_k(d),
C_k(d')=C_k(d).                                    (10)
```

All loose separators are equal by (6), and all tight separators are
equal by (9) unless the edge is a square.

Thus lexicographic component-length ranks do become constant.  They do
not become strictly descending.  The recurrent state consists of
identical nested component words connected by unequal return roots, with
tight square edges as the only unpointed separator transition.

## 4. The M=6 adversary and its first failed coordinate

The formal marker-cycle model in
`research/check_exit_marker_cycle_model.py` has `M=6` and returns

```
2,4,5^6,6,e,             e in {2,3,4}.
```

Its executed threshold signatures are:

```
e=2: (ell_3,ell_4,ell_5)=(8,8,7),
     (sigma_3,sigma_4,sigma_5)=(2,2,4);

e=3: (ell_4,ell_5)=(8,7),
     (sigma_4,sigma_5)=(2,4);

e=4: ell_5=7, sigma_5=4.
```

Every least-root parent cycle has constant vectors and constant
separators.  Its unequal square roots are `130` and `180`.

The first failed full-profile coordinate is not a length-vector change.
For exit color two, the adjacent `H_3` component begins

```
4,5^6,6.
```

Its first `H_4` symbol is the initial `4`.  The exact threshold-entry
lemma would require it to be preceded inside that `H_3` component by

```
3^4.
```

Those four symbols are absent.  Executed proper-profile enumeration
reports the same obstruction at raw cut one:

```
prescribed 4, actual 2.
```

For exit color three, the first `H_5` symbol has only one preceding `4`
instead of the required `4^5`.  The exit-color-four signature has the
valid formal top entrance `4,5^6,6`.

This identifies the missing datum: component lengths and separator colors
do not record the exact fixed-profile equations at the component's
internal threshold entrances.

## 5. Exact bottom-level countermodel

The stronger hope that constant component signatures force equal rescue
lengths or global periodicity is false even with every curling-profile
equation imposed.

The primitive word

```
Q=223222322232322232223
```

has exact proper circular profile `Q`.  Every `3` is an isolated
`H_3` component, followed by the exit color `2`.  At the cut after the
marker `32`, choose the least primitive maximizing root.

`research/check_q21_exit_parent_cycle.py` executes every proper power and
finds the parent cycle

```
1 -> 18 -> 12 -> 8 -> 4 -> 1
```

with rescue-root lengths

```
4,6,4,4,3.
```

Every component length is one and every separator color is two throughout
the cycle, yet the root lengths are unequal and the word is primitive.
One edge has exponent three and the other recurrent edges have exponent
two.

Therefore recursive threshold signatures rigorously align the nested
components, but at the bottom they reproduce the exact `Q21` square-mask
cycle.  A complete descent still needs the first-copy fitting/WSQ
mechanism that distinguishes an actual critical replay from an arbitrary
proper circular fixed profile.
