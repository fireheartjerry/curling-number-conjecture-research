# Least-root phase transport

Let `T` be an actual orbit word with seed length `N`, and suppose

```
T[0:3q] = Q^3
```

for a primitive word `Q` of length `q`.  At a generated cut `d`, write
`rho(d)` for the least primitive maximizing-root length.

## Exact three-copy transport

For every `N<=d<q`, the same exponent and the same least root occur at

```
d, q+d, 2q+d.
```

Indeed, the maximizing power at `d` has powered length at most `d`, so
it is wholly contained in the suffix `T[0:d]` copied at both later cuts.
If a later cut had a shorter maximizing root `s<rho(d)`, its powered
length would be less than the powered length at `d`, hence at most `d`.
It too would lie in the common copied suffix and contradict the
leastness of `rho(d)`.

At the delimiter cut `3q`, the least maximizing root is exactly `q`.
The displayed `Q^3` supplies it.  A root shorter than `q` would be a
proper circular cube at phase zero, contrary to the fixed-profile value
`Q[0]=2`; a longer cube root cannot fit in a word of length `3q`.

Thus a fixed-origin cube copies the complete decorated phase

```
(symbol, least maximizing root),
```

not only the symbol stream.

## Two-level spike geometry is not enough

The executed finite survivor

```
Q=2232,                         |Q|=4,
R=223222322232322232223,        |R|=21
```

has the `Q` spikes at cuts `12,33,54` and the `R` spike at cut `63`.
The exact square/cube/fourth-root spectra are

```
cut 12: squares {4},       cubes {4},  fourths {}
cut 33: squares {4,11},    cubes {4},  fourths {}
cut 54: squares {4,11,21}, cubes {4},  fourths {}
cut 63: squares {4,10,21}, cubes {21}, fourths {}
```

In particular the copied least root is exactly four at all three
internal spikes and exactly 21 at the outer spike.  Since `R` begins
`Q^3 3` and `Q[0]=2`, the sharp structural separation is already

```
|R| >= 3|Q|+1.
```

At the third internal spike the `Q`-cube lies wholly in the final
`R`-block, while the outer `R`-root is only a square.  Their coexistence
does not meet a Fine--Wilf threshold and forces no fourth power.

## The full-window length-21 survivor

For the phase-zero rotation

```
P = 223232223222322322232,
```

the first 21 outputs after `P^3 3` are

```
H = 222322232232223222323,
```

which is `P` rotated left by five positions.  More strongly, the proper
least-root profile of `P` is

```
L_P = 4,1,1,4,4,2,2,1,1,6,6,1,1,4,4,4,3,3,1,1,7,
```

and the least roots at the 21 post-promotion cuts are

```
2,2,1,1,6,6,1,1,4,4,4,3,3,1,1,7,4,1,1,4,4,
```

exactly the same rotation of `L_P`.

The undecorated output prefix has possible starting phases

```
length 1:  0,1,3,5,6,7,9,10,11,13,14,16,17,18,20
length 3:  5,9,16,20
length 7:  5,16
length 10: 5.
```

The decorated `(symbol,least-root)` prefix has candidates `{5,6}` after
one cut and the unique candidate `{5}` after two cuts.  Hence symbol
recurrence alone hides the phase, while the least-root decoration almost
immediately determines it.

Across all 15 rotations of the same fixed profile beginning in `2`, an
orbit survives more than two post-promotion outputs only if its first
decorated post-promotion pair equals `(P[x],L_P[x])` at a phase `x`
immediately following a `3`.  The non-surviving candidate branches
follow that decorated rotation until either curling number one occurs
or a first target-high masking event occurs.  Executed first masking
events include

```
expected (symbol,root) = (2,4), actual = (3,10),
expected (symbol,root) = (2,7), actual = (3,7),
expected (symbol,root) = (2,6), actual = (3,6).
```

At all three events the actual word ends in a primitive cube `Y^3`.
After appending the forced `3`, the autonomous suffix `Y^3 3` outputs
`2,1`; the global context does the same in these finite branches.
This is evidence for a phase-switch descent, not a proof: the three
roots `Y` are not themselves circular fixed profiles, because the old
length-21 spike crosses their internal third copies.

All numerical statements in this note are recomputed in
`check_fixed_origin_delimiters.py` and
`check_critical_seed_induction.py`.

