# Separation of context-masked maximum phases

This note sharpens equations (18)--(20) of
`critical_seed_induction.md`.  It is a reduction, not a termination
proof.

Let `P` be a primitive circular fixed profile of length `p`, with
maximum symbol `M>=4`.  Let `Y` be the primitive maximum-root word
supplied by (18), put `q=|Y|`, and use coordinates in which the source
cut is zero.  Thus

```
Y[0]=M-1,
Y uses only {M-1,M},
cn(Y^(M-1))=M-1,
cn(Y^M)=M.
```

For `0<=t<q`, put

```
L_t=Y^(M-1)Y[:t].
```

A position `t` is *masked* when

```
Y[t]=M,       cn(L_t)=M-1.
```

At the corresponding circular cut the fixed profile still has value
`M`, so it has a primitive proper `M`-root.  Let `r_t` be the length of
any such root.

## 1. The equal-scale alternative is terminal

Equation (20) gives, for every masked phase,

```
r_t=q,
```

or, with `g=gcd(q,r_t)`,

```
r_t>(M-2)q+t+g.
```

In particular,

```
r_t>=q.                                             (1)
```

Suppose `r_t=q`.  The `q`-periodic `M`-power ending at phase `t`
extends through the actual continuation `Y[t:q]`.  At every cut
`u` with `t<=u<q`, the suffix of length `Mq` is therefore a
`q`-periodic `M`-power.  Fixedness and maximality of `M` give

```
Y[t:q]=M^(q-t).                                     (2)
```

Thus a root of length `q` can mask only a phase in the terminal
`H_M` component of `Y`.

The run in (2) has length at most `M-1`.  Indeed,
`Y^(M-1)` ends in the same run, so a run of length at least `M`
would give `cn(Y^(M-1))>=M`, contrary to (18).  Hence

```
q-t<=M-1.                                          (3)
```

## 2. Distinct masked components have separated scales

Take masked phases `t<u` in distinct components of

```
{v: Y[v]=M}.
```

Choose primitive circular `M`-root lengths `r` and `s` at the two
phases, and put

```
delta=u-t,       g=gcd(r,s).
```

By (1),

```
0<delta<q<=min(r,s).                               (4)
```

The lengths cannot be equal.  If `r=s`, the two `r`-periodic
`M`-powers overlap in length `Mr-delta`, which is at least one full
root.  Their union is `r`-periodic.  For every cut `v` from `t`
through `u`, the length-`Mr` suffix lies in this union and is an
`M`-power.  Fixedness would give `Y[v]=M` throughout, contrary to the
choice of distinct components.

Assume first that `r<s`.  The overlap of the two powered intervals
ends at `t`.  If its left endpoint came from the later interval, its
length would be

```
Ms-delta.
```

By (4) and `M>=4`,

```
Ms-delta > r+s-g.
```

Fine--Wilf would give the overlap period `g`.  If `g<r`, a complete
length-`r` conjugate of the primitive `r`-root would have the proper
divisor period `g`; if `g=r`, a complete length-`s` conjugate of the
primitive `s`-root would have period `r`.  Both cases contradict
primitivity.  Therefore the overlap has length `Mr`.  The same
Fine--Wilf alternatives force threshold failure:

```
Mr<r+s-g,
```

and consequently

```
s>(M-1)r+g.                                       (5)
```

Now assume `r>s`.  The later, shorter powered interval starts later,
so the overlap has length `Ms-delta`.  Fine--Wilf threshold failure
gives

```
r>(M-1)s-delta+g.
```

Using `delta<s` from (4) gives the simpler strict bound

```
r>(M-2)s+g.                                       (6)
```

Equations (5)--(6) show that root lengths chosen in distinct masked
`H_M` components are distinct, and the larger is more than `M-2`
times the smaller.

If `c` distinct `H_M` components of `Y` contain a masked phase, sorting
their chosen root lengths and using that every proper circular root is
shorter than `p` gives

```
p>(M-2)^(c-1) q.                                  (7)
```

This is an exponential lower bound on the ambient critical profile.
It does not rule out a profile having only one masked component.

## 3. Exact local stress test

For `M=4`, the primitive word

```
Y=34344434443444
```

has length `14` and satisfies, by executed exhaustive curling-number
code,

```
cn(Y^3)=3,
cn(Y^4)=4,
cn(Y^3Y[:t])=3       for every 0<=t<14.
```

Its ten `4` positions are all masked and occupy four components:

```
{1}, {3,4,5}, {7,8,9}, {11,12,13}.
```

Therefore the autonomous equations (18)--(19) alone do not imply one
masked phase or one masked component.  Any embedding of this particular
`Y` into a circular fixed profile would require four pairwise separated
root scales and, by (7), ambient length greater than

```
2^3 * 14 = 112.
```

The executed regression is in `check_max_label_mask_separation.py`.
