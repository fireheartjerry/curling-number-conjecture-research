# Shortest deletion: exact maturation and the first post-break root

This note assumes a hypothetical counterexample.  It proves an exact
normal form and one additional root bound, then records why that bound is
not by itself an ordinal descent.

## 1. Whole-word maturation at first divergence

Choose a counterexample seed `S=aU` of minimum length.  The autonomous
orbit of `U` reaches curling number one.  Compare the two orbits until
their first different output.  Immediately before that output their states
are

```
A=aL,   L,
```

because all earlier appended outputs agreed.  Write

```
k=cn(A),   ell=cn(L).
```

Every powered suffix of `L` is also a powered suffix of `A`, so
`k>=ell`.  The outputs differ, hence `k>ell`.

Choose a maximizing `k`-root `Y` of `A` and put `r=|Y|`.  If its powered
suffix had length `kr<=|L|`, that same suffix would occur in `L`, giving
`ell>=k`.  Therefore

```
kr>|L|=|A|-1.
```

Since `kr<=|A|`, the two integer inequalities force

```
kr=|A|,   A=Y^k.
```

The root `Y` is primitive: if `Y=Z^d` for `d>=2`, then `A` ends in
`Z^(dk)`, contradicting `cn(A)=k`.

Deleting the first symbol gives

```
L=Y[1:r] Y^(k-1).
```

Thus `L` ends in `Y^(k-1)`, so `ell>=k-1`.  Combining this with
`ell<k` gives the exact local value

```
ell=k-1.
```

The first mismatch is therefore not an arbitrary context effect.  It is
the maturation of the whole global state from exponent `k-1` after one
symbol is deleted to exponent `k` when that symbol is restored.

## 2. Root bound immediately after maturation

The counterorbit appends `k` to `A=Y^k`.  Put

```
C=Y^k k.
```

Because the orbit is assumed never to reach one, `cn(C)=c>=2`.  Let `Z`
be a primitive maximizing `c`-root of `C`, and put `p=|Z|`.

Then

```
p<=r.
```

To prove this, suppose `p>r`.  The terminal `Z^2` has length `2p`.
Delete its last symbol, which is the newly appended `k`.  The remaining
factor `F` has length `2p-1`, lies entirely in `Y^k`, and has both periods
`p` and `r`:

* it has period `p` because it is `Z Z[0:p-1]`;
* it has period `r` because it is a factor of the `r`-periodic word
  `Y^k`.

Put `g=gcd(p,r)`.  Since `p>r`,

```
2p-1 - (p+r-g) = p-r+g-1 >= 1.
```

The Fine--Wilf theorem therefore makes `g` a period of `F`.  The first
`p` symbols of `F` are the whole word `Z`, so `g` is a period of `Z`.
But `g<=r<p` and `g` divides `p`, making `Z` a proper power.  This
contradicts the choice of a primitive maximizing root.  Hence `p<=r`.

There is also an exact equality condition.  If `p=r`, comparing the last
symbol of the two terminal root copies gives

```
k=Y[0].
```

Thus the first post-break step has an exhaustive alternative:

1. every maximizing root is shorter than `Y`; or
2. a length-`r` root survives, and the appended exponent is exactly the
   first symbol needed to begin another copy of `Y`.

## 3. Why this is not yet ordinal descent

Root length can grow again after the strict local drop.  Exhaustive
computation gives the primitive root

```
Y=2232,   r=4,   k=2.
```

It satisfies

```
cn(Y^2)=2,
cn(delete_first(Y^2))=1.
```

After the high branch appends `2`, the state is `Y^2 2`.  Its exact
curling number is two and its maximizing roots have lengths `{1,4}`, in
accordance with the lemma.  Continuing its actual orbit, the first
sixteen `(time,state length,cn,maximizing roots)` records are

```
(0,9,2,{1,4})   (1,10,3,{1})    (2,11,2,{4})
(3,12,3,{4})    (4,13,2,{2})    (5,14,2,{2})
(6,15,2,{1})    (7,16,3,{1})    (8,17,2,{6})
(9,18,2,{6})    (10,19,2,{1,4}) (11,20,3,{1})
(12,21,2,{4,10}) (13,22,2,{4,10})
(14,23,3,{4})   (15,24,2,{3}).
```

The least maximizing root has therefore grown from one to six, already
larger than `r`; later maximizing roots have lengths ten and twenty-one.
The orbit reaches curling number one only at time 56 from `Y^2 2`.

`research/search_pure_power_postbreak.py` recomputes this trace and
exhaustively checks the post-break bound for every primitive binary `Y`
of length at most ten and `2<=k<=4`.  The proof above is unbounded; the
enumeration is only a calibration and a counterexample to monotonicity.

The unresolved issue is now precise.  Minimality supplies termination of
`Y` only when `r<|S|`, but `Y` is a prefix of the pure-power state rather
than a suffix whose orbit remains coupled.  The post-break root bound
creates a one-step descent, while later hidden roots can cross the old
origin and grow beyond `r`.  A valid ordinal would have to charge those
origin crossings; root length alone cannot do it.

## 4. Every later root growth consumes older context

There is an exact stack-like rule behind the last observation.  Suppose a
state `W` has exact curling number `c` and ends in a primitive maximizing
power

```
Z^c,   |Z|=p.
```

After appending `c`, let a primitive maximizing root have length `q>p`.
Then

```
2q-1>cp.
```

If instead `2q-1<=cp`, delete the newly appended final symbol from the
terminal square of the `q`-root.  The remaining factor has length `2q-1`,
lies inside `Z^c`, and has periods `q` and `p`.  With
`g=gcd(p,q)`, the inequality `q>p` gives

```
2q-1-(p+q-g)=q-p+g-1>=1.
```

Fine--Wilf makes `g` a period of the whole `q`-root contained at the
start of this factor.  Since `g<=p<q`, this contradicts primitivity.

In cut coordinates, if the old state has length `t`, the old power starts
at `t-cp`, while the last two copies of the new root start at
`t+1-2q`.  The strict inequality above gives

```
t+1-2q < t-cp.
```

Thus any increase in primitive maximizing-root length crosses strictly to
the left of the active terminal power.  The decrease from `r` to a
post-maturation root and every later increase therefore behave like
pushes and pops of nested suffix contexts.  The finite example in Section
3 shows the remaining obstruction: after a short root is chosen, its
active left endpoint moves right, so a later growth can consume context
that was previously abandoned.  The inequalities do not yet prevent
infinitely many such resets.

## 5. Laminarity of consecutive canonical powers

The preceding argument has a symmetric shrinking form.  Let a state `W`
have length `t`, exact curling number `c>=2`, and a chosen primitive
maximizing root of length `p`.  Its complete terminal power occupies

```
I=[t-cp,t).
```

Append `c`.  Suppose the next exact curling number is `d>=2`, and choose a
primitive maximizing root of length `q`.  Its complete power occupies

```
J=[t+1-dq,t+1).
```

To compare intervals at the same right endpoint, extend the old interval
by the newly appended position:

```
E=[t-cp,t+1).
```

For unequal roots the alternatives are exactly laminar:

```
q>p  implies  J strictly contains E,
q<p  implies  J is strictly contained in E.
```

The growth implication follows from Section 4:

```
2q-1>cp,
dq>=2q>cp+1.
```

For the shrinking implication, suppose instead that `dq>=cp+1`.
Deleting the appended final symbol from `J` leaves a `q`-periodic factor
of length `dq-1>=cp` containing the whole old word `Z^c`.  Therefore
`Z^c` has periods `p` and `q`.  Put `g=gcd(p,q)`.  Since `q<p` and
`c>=2`,

```
cp >= 2p >= p+q-g.
```

Fine--Wilf makes `g` a period of the first complete length-`p` copy `Z`.
Here `g<=q<p` and `g` divides `p`, contradicting primitivity of `Z`.
Consequently `dq<=cp`, which puts the complete new interval strictly
inside `E`.

The equal-root case is the only exception:

```
q=p, d<=c     implies J is strictly contained in E;
q=p, d=c+1   implies J=E when p=1,
                       J strictly contains E when p>1.
```

The inequality `d<=c+1` is the one-step rise bound.  The second branch is
real: direct computation on `W=32323` gives `c=2` with root length two,
and after appending `2` the word `323232` has `d=3` with the same root
length two.

One useful boundary consequence needs no extra hypothesis.  If `I` starts
at the left edge of the available state, the growth branch `q>p` is
impossible, because it would force `J` to start strictly before that edge.
If a new unequal-root power also lands at the same left edge, the
shrinking branch is impossible as well.  Hence two consecutive
left-anchored canonical powers satisfy

```
q=p=1,   d=c+1.
```

Indeed, equality of their left endpoints gives `cp+1=dq`; after `q=p`
this becomes `(d-c)p=1`.

## 6. A later return to the same origin forces scale growth

Suppose a primitive `p`-root gives a complete maximizing power `Y^c`
on an interval `[a,t)`, where `c>=2`.  At a later cut `t+h`, suppose a
primitive `q`-root gives a power whose left endpoint is again exactly
`a`.  The old word `Y^c` is then a prefix of the new `q`-periodic word, so
it has periods `p` and `q`.

If `q<p`, its length satisfies

```
cp>=2p>=p+q-gcd(p,q),
```

and Fine--Wilf makes `gcd(p,q)<p` a period of `Y`, a contradiction.
Thus `q>=p`.

If `q>p`, the same contradiction would follow from
`cp>=p+q-gcd(p,q)`.  Consequently threshold failure is necessary:

```
q>(c-1)p+gcd(p,q).
```

Therefore a nontrivial return to one fixed left endpoint is always a
strict root growth.  When `c>=3`, it grows by more than a factor two.
More generally, if the old fixed-origin periodic prefix has length
`ceil(phi^2 p)`, where `phi=(1+sqrt(5))/2`, the identical calculation
gives

```
q>ceil(phi*p)+gcd(p,q).
```

This isolates the tower that survives the consecutive-power laminarity
lemma.  Shrinking roots move the active origin right.  Any lineage that
later returns to an abandoned origin must come back at a strictly larger
scale, and golden-length lineages grow by a factor greater than `phi`.
What is not established is that all future large roots belong to one
fixed-origin lineage; the active suffix can repeatedly relocate to the
right before growing across different older contexts.
