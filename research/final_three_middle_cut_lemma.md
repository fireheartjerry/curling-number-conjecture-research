# The final-3 middle-cut obstruction

This note isolates and proves the word lemma needed at the middle cut of
the final-3 canonical form.  It assumes the notation and conclusions of
`research/final_three_clsw_normal_form.md`.

Let

```
x=|X|,       a=|A|,       p=x+a,       n=3p-a,
Z=A X,       W=X A,       Q=X A X A X=W^2 X.
```

The canonical form supplies

```
0<a<x,
A is a suffix of X,
cn(X)=cn(Z)=1,
X[0] != A[0].
```

Let `q` be the `n`-periodic extension of `Q`, indexed by the integers.
Suppose an `r`-root cube ends at cut `p`.  Equivalently,

```
q(t)=q(t-r)       for p-2r <= t < p.              (1)
```

Assume also the positive-phase fitting inequality

```
p-3r >= 1-n.                                      (2)
```

Then these hypotheses are inconsistent.

## 1. Two elementary lift identities

Since `Q=W^2 X` and `X` is the length-`x` prefix of `W`, `Q` is the
length-`n=2p+x` prefix of the right-infinite periodic word `W^omega`.
Consequently, for every integer `t` with `-n<=t<0`,

```
q(t)=Q[n+t]=W[(x+t) mod p].                       (3)
```

Also, since `A` is the length-`a` suffix of `X`, putting `b=x-a` gives

```
W[u]=W[u+a]       for b<=u<x.                     (4)
```

Here and below, intervals of integer indices are left-closed and
right-open.

## 2. Roots shorter than `a`

First suppose `r<a`.

If `2r<=a`, the last two roots of the cube lie in the final copy of `A`
in the prefix `W=XA` ending at cut `p`.  Thus `A` has a square suffix.
This contradicts `cn(A)=1`, which follows from the facts that `A` is a
suffix of `X` and `cn(X)=1`.

It remains in this case to consider

```
2r>a.                                             (5)
```

The cube interval, of length `3r` and period `r`, and the suffix `A^2`,
of length `2a` and period `a`, have a common suffix of length

```
L=min(3r,2a).
```

Write `g=gcd(r,a)`.  If `3r<=2a`, then (5) gives

```
L=3r>r+a>=r+a-g.
```

If `3r>2a`, then `r<a` gives

```
L=2a>r+a>=r+a-g.
```

In both cases the Fine--Wilf theorem gives period `g` to the common
suffix.  Its length exceeds `a`, so its final length-`a` factor `A` also
has period `g`.  Since `r<a`, one has `g<a`; since `g` divides `a`, the
word `A` is a power with exponent `a/g>=2`.  This again contradicts
`cn(A)=1`.

## 3. Moving the cube left by `a`

Now suppose `r>=a`.  The interval

```
[x-2r,x)
```

is contained in the cube interval `[p-3r,p)`: its right endpoint is
`x=p-a<p`, and

```
(x-2r)-(p-3r)=r-a>=0.
```

It therefore consists of two equal length-`r` blocks.

If `2r<=x`, this is a square suffix of `X`, contradicting `cn(X)=1`.

If

```
x<2r<=p,
```

then `x-2r` lies in `[-a,0)`.  On `[-a,x)`, the periodic lift reads
exactly `AX=Z`: the negative part is the length-`a` suffix `A` of `Q`,
and the nonnegative part is the initial `X` of `Q`.  The displayed
square is therefore a square suffix of `Z`, contradicting `cn(Z)=1`.

Only

```
2r>p                                             (6)
```

remains.

## 4. The residual range `2r>p`

By (1) and (6), both `t=0` and `t=x` belong to the equality interval,
so

```
q(0)=q(-r),       q(x)=q(x-r).                   (7)
```

### 4.1. The range `r<=x`

Here (3) and the initial copy of `X` give

```
q(-r)=W[x-r]=q(x-r).
```

Together with (7), this implies `q(0)=q(x)`, or
`X[0]=A[0]`, a contradiction.

### 4.2. The range `x<r<=p`

Put

```
u=2x-r.
```

The inequalities `x<r<=x+a=p` give

```
b=x-a<=u<x.
```

Applying (3) at `-r` and `x-r` gives

```
q(-r)=W[p+x-r]=W[u+a],
q(x-r)=W[2x-r]=W[u].
```

Equation (4) equates the last two displayed letters.  Equation (7)
again gives `X[0]=A[0]`, a contradiction.  The endpoint `r=p` is
included: there `u=b`.

### 4.3. The range `r>p`

Write

```
e=r-p>0.
```

For every integer `t` in `[-p,0)`, inequality (6) strengthened by
`r>p` gives

```
p-2r<=t<p,
```

so (1) applies.  Moreover,

```
t-r >= -p-r > p-3r >= 1-n
```

by (2).  Thus both `t` and `t-r` lie in the single negative lift covered
by (3).  As `t` runs through `[-p,0)`, the residue

```
s=(x+t) mod p
```

runs through every residue modulo `p`.  Equations (1) and (3) yield

```
W[s]=W[(s-e) mod p]       for every s modulo p.   (8)
```

The fitting inequality (2), using `n=3p-a`, also gives

```
3e<=p-a-1=x-1,
```

so `0<e<p`.  Put `d=gcd(p,e)`.  Equation (8) makes all positions
congruent modulo `d` equal.  Since `d` is a proper divisor of `p`,

```
W=(W[0:d])^(p/d)
```

is a nontrivial power.

The word `Z=AX` is a cyclic conjugate of `W=XA`.  Cyclic conjugation
preserves being a nontrivial power: a cyclic word with period `d`
dividing its length retains that period after rotation.  Hence `Z`
would also be a nontrivial power, contradicting `cn(Z)=1`.

## 5. Exhaustion

The cases are exhaustive:

* `r<a` is split by `2r<=a` versus `2r>a`;
* `r>=a` is split by `2r<=x`, `x<2r<=p`, and `2r>p`;
* in the last range, `r<=x`, `x<r<=p`, and `r>p` are disjoint and
  exhaustive.

Every branch contradicts one of `cn(A)=1`, `cn(X)=1`, `cn(Z)=1`, or
`X[0]!=A[0]`.  Therefore no cube satisfying (1)--(2) can end at the
middle cut.

