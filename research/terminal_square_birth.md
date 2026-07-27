# Retrospective birth of a tower root's terminal square

This note studies the square suffix that witnesses the phase-zero value of
a normalized tower root.  The result is exact, but it does not manufacture
an intermediate normalized prefix.  It identifies why tracing the two
copies backward through the copy-parent graph loses most of the copied
block.

## 1. Terminal-square episode

Let `T` be an actual one-sided orbit word on the cuts under discussion:

```
T[e]=cn(T[0:e]).
```

Let

```
B=T[0:N],                  cn(B)=2,
```

and choose a primitive maximizing square root `Y` of length `r`.  Write

```
C=N-2r,          D=N-r,
T[C:D]=T[D:N]=Y.                                  (1)
```

Let `L` be the left endpoint of the maximal `r`-periodic interval ending
at `N` and containing the displayed square.  Thus `T[L:N]` has period
`r`, while either `L=0` or

```
T[L-1]!=T[L-1+r].
```

Put

```
delta=C-L.                                        (2)
```

Since the square in (1) lies in this run, `delta>=0`.  Since the value at
`N` is exactly two, the same root does not occur three consecutive times
at that cut.  Therefore

```
0<=delta<r.                                       (3)
```

Define the birth cut of this transported square episode by

```
beta=L+2r=N-delta.                                (4)
```

The root-`r` square exists at every cut

```
beta<=e<=N.                                       (5)
```

At no one of these cuts does root `r` support an exponent greater than
two.  Indeed

```
2r<=e-L<=N-L=2r+delta<3r.                        (6)
```

If an `r`-cube ended at such a cut, it would extend the same
`r`-periodic interval to the left of `L`, contrary to maximality; when
`L=0`, the cube does not fit.

It follows from the actual orbit equality that

```
root r is maximizing at cut e
    iff T[e]=2,                 beta<=e<=N.       (7)
```

For the forward implication, root `r` supplies only a square by (6), so a
larger actual value excludes it from the maximizing set.  For the reverse
implication, its displayed square attains the exact value two.

## 2. Which copied symbols had a block parent at birth?

The eventual second copy consists of positions

```
v=D+j,                       0<=j<r,
```

and its retrospective block parent is

```
u=C+j=v-r.
```

Equation (1) gives `T[u]=T[v]` for every `j`.  At the moment position `v`
has been appended, however, the prefix cut is `e=v+1`.  A root-`r`
square is then available exactly when

```
v+1>=beta,
```

or, after substituting (4),

```
j>=r-delta-1.                                    (8)
```

Consequently only the final `delta+1` symbols of the second copy had a
span-`r` square parent available at their birth.  The equality of the
earlier `r-delta-1` symbol pairs is retrospective: it becomes part of a
square only after later symbols have been appended.

Even among the final `delta+1` positions, (7) says that span `r` is a
maximizing copy-parent only at cuts labelled two.  At a higher-labelled
cut it is merely a nonmaximal square.  If the canonical graph chooses the
least maximizing root, a two-labelled cut can still choose a shorter
parent than `r`.

This proves that a terminal square does not in general give a length-`r`
chain of copy-parent edges between its two copies.  It supplies at most
`delta+1<=r` candidate edges, and higher curling-number events delete
some of those candidates from the maximizing graph.

The root at the birth cut is the conjugate

```
Z=Y[r-delta:r] Y[0:r-delta].                     (9)
```

The birth square is `Z^2`.  Transport from `beta` through `N` rotates
this root one symbol at each cut and ends at the original terminal root
`Y`.  Thus the correct object to trace is a short transported episode of
rotations, not the birth history of all symbols in the eventual two
copies.

## 3. Interaction with an earlier tower promotion

Now let a smaller normalized level `A=T[0:p]` satisfy

```
T[0:3p+1]=A^3 3
```

and put `s=3p+1`.  The terminal square of `B` is wholly after the old
promotion exactly when `C>=s`.  Its transported episode is born after the
promotion exactly when

```
beta>s.
```

Neither condition changes (7)--(9).  In particular, even when both
terminal copies are generated after `A` promotes, their equality does not
give copy-parent edges for the first `r-delta-1` target symbols.  The full
prefix-orbit equations at those earlier target cuts can be governed by
unrelated shorter powers.

If a cut `e` in the birth window has value `k>=3`, let `q` be a primitive
maximizing `k`-root there.  There is an exact alternative:

```
q<r/2,
```

or the complete `q^k` suffix crosses `L`.          (10)

To prove this, suppose the power starts at or after `L` and `q>=r/2`.
It lies in the `r`-periodic run and has length at least `3q`.  This meets
the Fine--Wilf threshold `q+r-gcd(q,r)`.  A complete primitive root of
one of the two periods then has the proper gcd period unless `q=r`.
The equality case would require an `r`-cube inside an interval whose
length is below `3r` by (6).  Both outcomes contradict the hypotheses.

Thus every interruption of the terminal-square parent episode is either
a half-scale reset or a power crossing the episode's left boundary.  This
is the same decrease/rescue alternative already present in the fixed
profile ancestry graph.  The birth construction does not orient it toward
the absolute origin, so it does not by itself produce a prefix
`Q=T[0:q]`, much less prove the full replay equation `pc_Q=Q`.

## 4. Executed dynamic model

`research/check_terminal_square_birth.py` evaluates every curling number
in this section with both implementations in `curling.py`.

Take

```
P=223222322232322232223,
U=2232,
W=U^3 3.
```

The orbit from the promoted state `W` appends the remaining eight symbols
of `P` exactly.  The word `P` is primitive and is a full normalized replay
root: its local orbit appends two copies of `P` and the next value at
`P^3` is three.

At phase zero, `P` has maximizing square-root lengths `4` and `10`.
For the least root `r=4`, the terminal copies are

```
2223 2223
```

at positions `[13,17)` and `[17,21)`.  The maximal period-four interval
starts at `L=11`, so

```
C=13,       delta=2,       beta=19.
```

For the four target positions in the second copy, the executed status is:

| target `v` | candidate parent `v-4` | root `4` square available at cut `v+1` | root `4` maximizing |
|---:|---:|---|---|
| 17 | 13 | no | no |
| 18 | 14 | yes | yes |
| 19 | 15 | yes | no |
| 20 | 16 | yes | yes |

The exact values at cuts `19,20,21` are respectively `2,3,2`.  At the
middle cut, the transported period-four square exists, but a root-one
cube supplies the larger value and removes span four from the maximizing
parent graph.

No prefix `P[0:q]` with `4<q<21` is a normalized replay root; the checker
tests every such `q` through two complete replay copies and the cube
boundary.  This is a genuine orbit model, not a static word comparison:
it satisfies the entire post-promotion path into `P` and the entire replay
of `P`.

The smaller word `U` is not itself a normalized replay root.  Therefore
this finite model is not a countermodel to the full two-level tower
hypothesis.  It isolates the exact place where that unused lower-level
hypothesis would have to enter: it must control the high interruption and
the retrospective portion of the terminal square.  Merely knowing the
old marker `U^3 3`, the actual intervening orbit, and every replay equation
of the larger root does not create an intermediate normalized prefix.
