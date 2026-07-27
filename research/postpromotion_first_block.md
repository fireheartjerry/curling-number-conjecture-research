# Post-promotion roots before one full block

This note assumes a primitive word `P` of length `p` satisfying the
proper circular fixed-profile equation and `P[0]=2`.  It records exact
constraints on the orbit state

```
A_h = P^3 D,       D=3H,       |H|=h<p.
```

No termination statement is claimed here.

## Crossing-root normal form

Put `e=|D|=h+1<=p`.  Suppose `cn(A_h)=k>=2`, and choose a primitive
maximizing root of length `q>=p`.

The equality case `q=p` is impossible.  The last `e` symbols of the two
terminal length-`p` blocks would give `D=P[:e]`, contradicting
`D[0]=3` and `P[0]=2`.

Write

```
q=p+s,       s>=1,       g=gcd(p,s).
```

Delete `D` from the terminal `k`-power.  The remaining prefix of that
power has length `kq-e`, lies in `P^3`, and has periods `p` and `q`.
If `k>=3`, then

```
kq-e >= p+q-g.
```

It also contains a complete length-`q` root.  Fine--Wilf therefore gives
that root the proper period `g<q`, contrary to its primitivity.  Hence

```
k=2.
```

For `k=2`, the same argument shows that the Fine--Wilf threshold must
fail:

```
2q-e < p+q-g.
```

After substituting `q=p+s` and `e=h+1`, the integral form is

```
s+g <= h.                                      (1)
```

Comparing the two copies of the terminal `q`-root gives the complete
indexed equations.  Put

```
delta=e-s=h+1-s.
```

Then, with indices of `P` read modulo `p`,

```
D[t] = P[t-s]                         (0<=t<e),
P[i] = P[i+s]             (delta-s<=i<p-s).       (2)
```

In particular,

```
D=P[p-s:] P[:delta],       P[p-s]=3.               (3)
```

Thus every symbol emitted before the first scale crossing is already a
prefix of a circular rotation of `P`; the crossing square supplies the
missing alignment certificate rather than merely a numerical period
bound.

## Actual orbit history excludes the crossing

Equation (2) says that the lifted circular factor

```
P^Z[delta-s:p]
```

has period `s`.  It has length `p-delta+s` and ends at phase zero.  If
that length were at least `3s`, phase zero would have a proper cube of
root length `s<p`, contradicting the fixed-profile value `P[0]=2`.
Consequently

```
p-delta+s < 3s,
delta >= p-2s+1,
s+h >= p.                                      (4)
```

Combining (1) and (4) yields

```
p-h <= s <= h-g,
2h >= p+g.
```

The inequalities alone confine a crossing to the second half, but the
actual orbit history excludes that remaining interval.  Put

```
R=P[p-s:p].
```

The period-`s` factor ending at phase zero has length at least `2s`, so
`P^3` ends in `R^2`.  Equation (3) says that the first `s` symbols of `D`
are exactly `R`.  Inequality (1) gives `e>=s+2`, so `D[s]` exists and

```
D[s]=P[0]=2.
```

The actual orbit would therefore pass at time `s-1` through

```
A_(s-1)=P^3 R,
```

which ends in `R^3`.  Its curling number is at least three, whereas the
next symbol prescribed by the same actual history is `D[s]=2`.  This
contradicts the orbit rule.  Hence:

> If the orbit from `P^3 3` avoids one for its first `p` outputs, every
> primitive maximizing root at every one of those cuts has length
> strictly below `p`.

The use of the intervening orbit states is essential.  The local final-cut
inequalities alone are sharp: executed exact code gives the primitive
word `P=233`, `p=3`, `s=1`, `D=323`, for which
`P^3D=233233233323` has exact curling number two and unique maximizing
root length four.  Its required intermediate orbit history fails.
