# Adjacent `33`: exact four-cut normal form and complementary near-models

This note sharpens Section 5 of `run_stack.md`.  It does not eliminate
adjacent `33` from a binary proper-profile fixed point.  It proves the
complete local alternative and records two global near-models showing
that its two missing global obligations are independent.

## Lemma 1 (the four-cut bridge-or-separation alternative)

Let `Q` be a primitive binary circular word satisfying `pc_Q=Q`.  Suppose,
in cut coordinates,

`Q[c-1],Q[c],Q[c+1],Q[c+2]=2,3,3,2`.

Choose cube roots of lengths `p` and `q` ending at cuts `c` and `c+1`.
Put `g=gcd(p,q)`.

Every such root word is primitive.  Moreover, exactly one of the
following numerical alternatives applies:

1. `p=q`.  If `U` is the length-`p` root ending at `c`, then `U` starts
   in `32`, ends in `2`, and

   `U^3 3 = 3 rot(U)^3`.                                  (BRIDGE)

   The maximal period-`p` run is exactly

   `[c-3p,c+1)`.

   Its left boundary forces another double component:

   `Q[c-3p-1],Q[c-3p]=3,3`.                               (PRED)

2. `q>p`, in which case

   `q>2p+g`.

3. `p>q`, in which case

   `p>=2q+g`.

At the two neighboring 2-cuts, cut `c-1` has some proper square and no
proper cube, while cut `c+2` has the root-one square `33` and no proper
cube.

**Proof.**  If a selected cube root were a proper power `V^e` with
`e>=2`, its cube would be a `V`-power of exponent `3e>=6`.  Since
`|V|` is still a proper root length, this contradicts profile value
three.  The selected roots are primitive.

The two cube intervals overlap in

`L=min(3p,3q-1)`

symbols.  If `p!=q` and `L>=p+q-g`, Fine--Wilf gives period `g` on an
overlap containing a full conjugate of the longer primitive root.  That
conjugate would have the proper divisor period `g`, a contradiction.
Thus `L<p+q-g`.  If `q>p`, then `L=3p`, which rearranges to
`q>2p+g`.  If `p>q`, then `L=3q-1`, which rearranges over the integers
to `p>=2q+g`.

Now let `p=q`.  The two cubes give period `p` on
`[c-3p,c+1)`.  A left extension would contain a period-`p` cube ending
at the 2-cut `c-1`; a right extension would contain one ending at the
2-cut `c+2`.  Both are excluded by `pc_Q=Q`, so this interval is the
exact maximal run.

The cube ending at `c` has last symbol `Q[c-1]=2`.  The extension by
`Q[c]=3` to the cube ending at `c+1` says that the first symbol of `U`
is `3`.  Failure of the next right extension, together with
`Q[c+1]=3`, says that the second symbol of `U` is `2`.  Hence `U`
starts in `32` and ends in `2`.  Writing `U=3V` gives

`U^3 3=(3V)^3 3=3(V3)^3`,

which is (BRIDGE).

At the left boundary, the symbol inside the run in the congruence class
of `Q[c-1]` is `2`.  Nonextension and binarity force the outside symbol
`Q[c-3p-1]` to be `3`.  The first symbol of the run is the first symbol
of `U`, also `3`, proving (PRED).

Finally, the asserted conditions at `c-1` and `c+2` are their exact
profile equations.  The last two symbols before `c+2` are the displayed
adjacent `33`, so root length one supplies its square. ∎

## Lemma 2 (one-component bridge normal form)

Under the hypotheses of Lemma 1, suppose the displayed pair is the only
cyclic `33` component of `Q` and its two cube-root sets intersect.
For every common root length `p`,

`|Q|=3p+1`,

and, after rotating to the start of the bridge,

`Q=U^3 3`.

**Proof.**  Lemma 1 sends the component to the predecessor component
whose first cut is `c-3p-1`.  Uniqueness makes these cuts congruent
modulo `n=|Q|`, so `n` divides `3p+1`.

The proper period-`p` factor has length `3p+1`.  Since `Q` is primitive,
Fine--Wilf bounds that length strictly below `n+p-gcd(n,p)`.  If
`3p+1=kn` with `k>=2`, then

`n <= (k-1)n < p-gcd(n,p) < n`,

a contradiction.  Therefore `k=1`, giving `n=3p+1`.  The bridge
identity from Lemma 1 then occupies the whole circle and has the stated
rotation. ∎

This normal form explains the period-21 calibration
`Q=U^3 3` of length 64.  Its only remaining defects are positive
first-copy coverage equations, not a missing bridge descent.

## Complementary global near-models

The executed checker `check_double_three_near_fixed.py` recomputes every
proper root involved below.

The length-35 primitive word

`Q35=33222322233222322232223322232223222`

has profile

`F35=33222333333222322233223322232223222`.

Every cut is squareful, every `3`-label has a cube, and no fourth power
occurs.  Its only failures are four `2`-labels that acquire cubes, at
cuts `6,7,8,19`.  Its three double components are all equal-root
bridges, with common periods `4,13,4`.  The period-13 cube persists
leftward across the three erroneous cuts `6,7,8`; the no-cube equation
at the immediately preceding 2-cut is exactly the condition needed to
make (PRED) fire.

The length-41 primitive word

`Q41=33222322232232223322232223223222332223222`

has profile

`F41=33222322232222223222232223222222322223222`.

Every cut is squareful, every `2`-label excludes cubes, and no fourth
power occurs.  Its only failures are missing cubes at four `3`-labels,
cuts `12,17,28,33`.  At the normalized exact double component, the cube
root sets are `(1)` and `(16)`, realizing the separated branch while
both neighboring 2-cuts are exact.

Consequently maximal bridges, (SEP), full square coverage, and all
negative power exclusions do not imply the missing positive cube
coverage at every 3-cut.  Conversely, full square and cube coverage
plus absence of fourth powers do not imply the no-cube equations at
2-cuts.  Any adjacent-`33` elimination must use both directions of the
global equality `pc_Q=Q`; neither can be reconstructed from the other
local data.
