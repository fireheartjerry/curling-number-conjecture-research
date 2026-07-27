# Post-promotion root bounds

This note uses zero-based indexing.  A cut at phase `0` is immediately
before `P[0]`.  Let `p=|P|`, let `P[0]=2`, and let

```
A_h = P^3 D,             D = 3H,
|H| = h < p,             e=|D|=h+1.
```

Every symbol of `H` is assumed to have been appended by the
curling-number orbit.  When a maximizing suffix is written `Y^k`, its
root `Y` may be taken primitive: if `Y=Z^a` with `a>=2`, the same
suffix is `Z^(ak)`, contradicting maximality of `k`.

## 1. The first symbol after promotion

Assume additionally that `P` is primitive and its proper circular
curling profile is `P`, with `P[0]=2`.  Put `A=P^3 3`.  If
`cn(A)=k>=2` and a primitive maximizing root has length `r`, then

```
r < p,
(k-1)r + gcd(p,r) <= p,
k <= 3.
```

For `r=p`, the last two length-`p` blocks would be

```
P[1:p] P[0]     and     P[1:p] 3,
```

which differ in their last symbol.  Hence `r!=p`.

Suppose `r>p`.  Delete the final appended `3` from `Y^k`.  The
remaining factor has length `kr-1`, lies in `P^3`, and has periods `p`
and `r`.  If

```
kr-1 >= p+r-gcd(p,r),
```

Fine--Wilf makes that factor `gcd(p,r)`-periodic.  Its length contains
a complete copy of `Y`; since `gcd(p,r)` divides `r` and is smaller
than `r`, this contradicts primitivity of `Y`.  Therefore

```
kr-1 < p+r-gcd(p,r),
```

whose integer rearrangement is

```
(k-1)r + gcd(p,r) <= p.
```

The latter inequality itself contradicts `r>p`.  Thus `r<p`.  In this
remaining case, if the Fine--Wilf threshold were met, the
`gcd(p,r)`-periodic factor would contain a complete length-`p`
conjugate of `P`.  Since `gcd(p,r)<p` divides `p`, that conjugate would
be a proper integral power, contrary to primitivity of `P`.  This
proves the same displayed inequality when `r<p`.

Finally, delete only the last symbol of `Y^k` and take its last
`(k-1)r` symbols.  They are a `(k-1)`-power of the conjugate

```
Y[r-1] Y[0:r-1]
```

and end at phase `0` of `P`.  Because `r<p`, this is a proper circular
root.  The profile value there is `P[0]=2`, so `k-1<=2`.  In
particular, if `k=3`, then

```
2r+gcd(p,r) <= p,
```

and hence `r<p/2`.

## 2. Exact form of a root crossing `p`

Now take any actual state `A_h` above and suppose `cn(A_h)=k>=2`.
Let a primitive maximizing root have length `q>=p`.

The case `q=p` is impossible.  The last two length-`p` blocks are

```
P[e:p] P[0:e]     and     P[e:p] D.
```

Their equality would imply `D=P[0:e]`, contrary to
`D[0]=3!=2=P[0]`.

Write `q=p+s`, so `s>=1`, and put `g=gcd(p,s)=gcd(p,q)`.  Delete all
`e` symbols of `D` from `Y^k`.  The remaining factor has length
`kq-e`, lies in `P^3`, and has periods `p` and `q`.  Fine--Wilf at
length `p+q-g` would make a full copy of `Y` `g`-periodic, contrary to
its primitivity.  Consequently

```
kq-e < p+q-g,
(k-1)q+g <= p+h.                         (1)
```

Since `q>p` and `h<p`, (1) excludes `k>=3`.  Thus `k=2`, and

```
s+g <= h.                                (2)
```

In particular `s<e`.

Compare the two copies of the length-`q` root directly.  The second
copy is

```
Y = P[e-s:p] D.
```

For `0<=t<e`, comparison with the first copy gives

```
D[t] = P[(t-s) mod p].                    (3)
```

For `0<=j<p+s-e`, comparison of the initial portions gives

```
P[(e-2s+j) mod p] = P[e-s+j].             (4)
```

Set

```
delta = e-s = h+1-s.
```

Equation (3) is the exact splice formula

```
D = P[p-s:p] P[0:delta].                  (5)
```

Equation (4), written on the bi-infinite periodic lift of `P`, is

```
P[i] = P[i+s]   for delta-s <= i < p-s.   (6)
```

Thus the lifted factor `P[delta-s:p]`, of length `p-delta+s`, has
period `s`.  Formula (2) is also the sharp Fine--Wilf escape interval

```
1 <= s,
s+gcd(p,s) <= h < p.
```

## 3. Orbit history eliminates the escape interval

Although (2)--(6) are locally consistent, they are incompatible with
the earlier states of the same orbit.

Because `e<=p`, one has `delta<=p-s`.  Hence the period-`s` factor in
(6) has length

```
p-delta+s >= 2s.
```

Let

```
R=P[p-s:p].
```

The last `2s` symbols of that factor are therefore `R^2`.  Equation
(5) says that the first `s` symbols of `D` are exactly `R`.

Inequality (2) gives `h>=s+1`, so the intermediate orbit state
`A_(s-1)` exists before `A_h`.  It is

```
A_(s-1) = P^3 R.
```

The final `2s` symbols of `P^3` are `R^2`, so this state ends in
`R^3`.  Therefore

```
cn(A_(s-1)) >= 3.                          (7)
```

On the other hand, the next symbol actually appended after
`A_(s-1)` is `D[s]`.  Equation (3) gives

```
D[s] = P[0] = 2.
```

By the deterministic orbit rule this says

```
cn(A_(s-1)) = 2,                           (8)
```

contradicting (7).  Therefore no maximizing root at any
post-promotion state `A_h`, `h<p`, has length at least `p`.

The orbit-history hypothesis is essential to this last contradiction.
The executed local example

```
P=233,  D=323,  P^3D=233233233323
```

has curling number `2` with sole maximizing root length `4=p+1` and
saturates `s+gcd(p,s)=h=2`.  But it is not an orbit segment:

```
cn(P^3 3)=3,
```

whereas its prescribed next symbol `D[1]=P[0]` is `2`.

`research/check_post_promotion_escape.py` recomputes these numerical
values, exhaustively audits the indexed square equations on small
ternary words, checks all ternary post-promotion orbits through
`p=9`, and checks every phase-zero rotation of the length-21 replay
word.
