# A one-exception dichotomy for a crossing weak-square mask

This note combines the globally longest fitting square from
`max_square_terminal_forest.md` with a square hole in the period word of
its last cube.  It gives a strict fitting scale drop, a same-period lock,
or one explicit threshold-minus-one geometry.

The squareful-word literature does not supply this inheritance step.
Saari's minimal-square midpoint lemma compares a square with the shortest
square at its midpoint; it does not force a square in the primitive
period word of an ambient cube.  The calculation below instead keeps the
distinguished fitting occurrence and its exact coordinates.

## 1. Setup

Let `P` be a primitive binary proper-circular fixed profile with the full
first-copy fitting property.  Let `p` be the largest root length among
all fitting squares at `2`-cuts, and choose one such occurrence

```
U^2=[a,c),                 c=a+2p.                (1)
```

Let `h=c-d` be the last `3`-cut before `c`.  Then

```
1<=d<=3.                                           (2)
```

Choose a fitting cube `V^3` of root length `q` ending at `h`.  The
strict-half-scale lemma gives

```
p>2q+gcd(p,q),              q<p/2,                (3)
V^3=[c-d-3q,c-d) subset U^2.                       (4)
```

The root `V` is primitive.  Fix `0<=t<q` such that the circular phase
`t` of `V` has no proper square root; that is, no root of length
strictly below `q` gives a square ending at that phase of `V^Z`.
Assume the corresponding displayed label is `2`.

The cut at phase `t` in the second copy of `V` is

```
y=c-d-2q+t=a+D,
D=2p-d-2q+t.                                      (5)
```

Full fitting supplies a fitting ambient square of some root length `s`
at `y`.  Global maximality of `p` gives

```
s<=p.                                             (6)
```

Every such root is primitive, since an imprimitive root used twice would
give a proper fourth power at this exact `2`-cut.

## 2. Child-boundary alternative

The equality

```
s=q                                               (7a)
```

is impossible.  Write the child cube as

```
V^3=[B,B+3q).
```

The selected hole in its second copy is

```
y=B+q+t.
```

If a root-`q` square ended at `y`, its two root blocks would both be
`rot_t(V)`.  The following `q` symbols

```
[y,y+q) subset [B,B+3q)
```

are a third copy of the same conjugate.  Hence a root-`q` cube would
end at `y+q=B+2q+t`.  This is phase `t` in the third copy of `V`, so
its displayed ambient label is again `V[t]=2`.  The cube contradicts
that exact low value.

If `s<q`, then its occurrence at the lifted cut `y` crosses the left
boundary of `V^3`, and

```
2s>q+t.                                           (7)
```

Indeed, the prefix of `V^3` before `y` has length `q+t`.  If
`2s<=q+t`, the whole square lies in `V^3`.  It is then a factor of
`V^Z` ending at phase `t`, with proper root `s<q`, contrary to the
choice of `t`.

Thus every mask is either a strict child-scale crossing root satisfying
(7), or a genuine child-scale ascent `s>q`.  There is no equal-scale
mask.

## 3. Parent-scale alternative

There are three exhaustive possibilities:

```
s<p;                                             (DROP)

s=p and D>=p;                                    (LOCK)

s=p, D=p-1, p=2q+2, gcd(p,q)=1, d=3, t=0.        (ESC)
```

In `(DROP)`, `s` is a strictly shorter fitting square root.  In `(LOCK)`,
the mask square and the parent square belong to one common
period-`p` interval.

Proof.  Equation (6) leaves `s<p` or `s=p`.  Suppose `s=p`.
The mask square has interval

```
[y-2p,y).
```

Since `D<2p`, it starts strictly before `a`.  Its overlap with the
parent square (1) is `[a,y)`, of length `D`.  When `D>=p`, two
period-`p` intervals overlap in at least one full period, so their union
is period `p`.  This is `(LOCK)`.

It remains to enumerate `D<p`.  Put

```
H=p-2q.
```

Equation (3) gives

```
H>=gcd(p,q)+1>=2.                                  (8)
```

By (5),

```
D-p=H-d+t.                                        (9)
```

The bounds `d<=3`, `t>=0`, and `H>=2` make (9) negative only when

```
H=2, d=3, t=0.
```

Then `D=p-1`.  Equation (3) also forces `gcd(p,q)=1`, and `H=2`
is `p=2q+2`.  This is exactly `(ESC)`.  No other integer case exists.

## 4. Exact residual

The only mask that is neither a strict fitting root-length drop nor
locked into the parent's period is therefore

```
p=2q+2,       q odd,       d=3,       t=0,
s=p,          D=p-1.                               (10)
```

Here the second-copy hole is the cut at the start of the second `V`,
the child cube ends three phases before the parent square, and the two
period-`p` square intervals overlap in exactly `p-1` symbols.  This is
the sharp Fine--Wilf-minus-one geometry; period gluing cannot be invoked
without an additional endpoint-label equation.

Consequently the weak-square inheritance problem is reduced, at this
globally maximal fitting square, to:

1. iterate the strict fitting roots in `(DROP)`;
2. absorb `(LOCK)` into the maximal period-`p` run; and
3. discharge the single arithmetic configuration (10).

The note does not prove that iterations of `(DROP)` remain attached to
the same child phase, so it is not yet a complete classification.

## 5. The escape is impossible for every nonunary child

Assume `(ESC)` and `q>=3`.  Normalize `a=0`.  Then

```
p=2q+2,       c=2p=4q+4,
h=c-3=4q+1,
start(V^3)=h-3q=q+1.                              (11)
```

Since `gcd(p,q)=1`, the integer `q` is odd.

### 5.1 The child root is forced alternating

For `0<=j<=q-3`, period `p` of the parent square compares the first
and third child copies:

```
V[j]
 = P[q+1+j]
 = P[3q+3+j]
 = V[j+2].                                        (12)
```

The last two comparisons instead reach the known terminal labels:

```
V[q-2]=P[c-3]=3,
V[q-1]=P[c-2]=2.                                  (13)
```

Equations (12)--(13), together with odd `q`, give the exact word

```
V=(23)^((q-1)/2) 2.                               (14)
```

### 5.2 The last internal high has only two possible rescue scales

The last internal high phase of `V` is `q-2`.  In the third copy it is
the cut

```
x=start(V^3)+2q+(q-2)=c-5.                        (15)
```

Choose a fitting cube root of length `r` there.  The following phase is
low, so its same-scale midpoint square is fitting.  Maximality of `p`
among fitting square roots gives

```
r<=p.                                             (16)
```

The displayed `V^3` is a maximal period-`q` run.  It cannot extend
right because its endpoint label is `3`, whereas the period mate is
the low first symbol `V[0]=2`.  It cannot extend left because a
one-symbol left extension would shift the same `q`-cube to the low cut
`h-1`, where `P[h-1]=V[q-1]=2`.

Suppose first that `r<=q`.  Maximal-run overlap puts the `r`-cube
inside `V^3` and gives

```
r<q/2.                                            (17)
```

If this cube starts after the second `V|V` join, it lies in a strictly
alternating factor.  Its period `r` is then even.  The following symbol
has the same parity and extends the cube one step to the right, producing
a cube at the next low cut, which is forbidden.

If it starts before that join, (17) puts its start after the first join.
It therefore contains exactly one occurrence of `22`, namely the second
`V|V` join.  A cube `R^3` cannot contain exactly one occurrence of a
fixed bigram: an occurrence internal to a root copy appears in all three
copies, while an occurrence across a root join appears at both joins.
This is also impossible.  Hence

```
r>q.                                              (18)
```

The overlap of the `r`-cube with the maximal `q`-run is `[start(V^3),x)`,
of length `3q-2`.  Fine--Wilf and primitivity force threshold failure:

```
3q-2 < q+r-gcd(q,r),
r>2q-2+gcd(q,r).                                  (19)
```

Combining odd `q`, (16), and (19) gives exactly

```
r=p-1=2q+1,       or       r=p=2q+2.              (20)
```

The value `r=2q` is excluded separately by
`gcd(q,2q)=q`: the overlap has length at least `2q`, so a complete
length-`2q` root would have period `q` and would be imprimitive.

### 5.3 Both scales contradict the endpoint equations

If `r=p`, the period-`p` cube ending at `c-5` overlaps the parent
period-`p` square ending at `c` in `2p-5>=p` symbols.  Their union is
period `p` and contains a period-`p` cube ending at the low cut `c`,
contrary to its exact value two.

Let `r=p-1`.  The escape already supplies the period-`p` mask square
ending at

```
y=p-1.
```

Starting from the high symbol at `x=c-5=2p-5`, three literal period
transports give

```
P[x]
 = P[x-p]                 by the parent square
 = P[x-2p]=P[-5]          by the mask square
 = P[-5+(p-1)]=P[p-6]     by the r-cube.            (21)
```

For `q>=5`, the final position lies in the first child copy at even
offset

```
(p-6)-(q+1)=q-5.
```

Equation (14) gives `P[p-6]=2`, while `P[x]=3`, contradicting (21).

For `q=3`, the same three intervals give the shorter explicit chain

```
P[8]=P[0]=P[-8]=P[6].                              (22)
```

Here the first and final positions are respectively phases one and two
of copies of `V=232`, so (22) equates `3` with `2`.

Therefore `(ESC)` is impossible for every `q>=3`.  The only surviving
arithmetic case is the unary child

```
q=1,             p=4,             d=3,             t=0. (23)
```

The argument using the last internal high has no phase to select when
`q=1`; (23) is instead excluded by the finite local certificate below.

## 6. The unary escape has no periodic binary replay

The argument in this section does not assume that all `3`-components
are singletons.

### 6.1 Every fitting cube scale is bounded by the maximum low-square scale

A primitive binary fixed profile has no circular factor `333`.  If
three consecutive displayed symbols were `3` and the next displayed
symbol were `2`, the cut carrying that `2` would have the root-one cube
`333`.  If the next displayed symbol were also `3`, then the cut after
those four symbols would have the root-one fourth power `3333`,
regardless of whether its displayed binary label were `2` or `3`.
Both alternatives contradict the exact proper circular profile.

Let a fitting root-`r` cube end at an arbitrary `3`-cut `z`.  Its first
two copies give a root-`r` square ending at `z-r`.  If
`P[z-r]=2`, this is a fitting low square: the fitting inequality is

```
3r<=n+z-1  implies  2r<=n+(z-r)-1.                 (24)
```

If `P[z-r]=3`, period `r` shifts the cube one symbol to the right,
because the only new equality is

```
P[z]=P[z-r]=3.
```

Exactness forces `P[z+1]=3`; a value `2` there would already be
contradicted by the shifted cube.  The absence of `333` then gives
`P[z+2]=2`.  Lemma 1 of `max_square_terminal_forest.md`, applied to
the shifted cube ending at `z+1`, puts a root-`r` square at a low cut.
This midpoint square is fitting: it ends at the lifted cut `z+1-r`.
If that cut is nonnegative, its fitting inequality follows from

```
3r<=n+z-1 < n+z;
```

if it is negative, adding `n` to canonicalize its phase only enlarges
the available first-copy suffix.  This argument does not assume that
canonical fitting of the shifted cube itself survives an origin wrap.

Thus every fitting cube root is no larger than the global maximum `p`
of fitting low-square roots.  In the unary escape (23), every cut
therefore has the following necessary local properties:

```
some square of root 1,2,3,or 4 ends at the cut;
a cube of one of those roots ends iff the displayed label is 3;
no fourth power of one of those roots ends.         (25)
```

For a low cut, the square in (25) is supplied by full fitting and the
definition of `p=4`.  For a high cut, full fitting supplies a cube,
the preceding paragraph bounds its root by four, and its final two
copies supply the square.  Exactness excludes a small cube at a
`2`-cut and excludes every small fourth power at either label.

### 6.2 Exhaustive 16-symbol transition graph

The script `research/check_max_fitting_root_four.py` enumerates all
binary words

```
w in {2,3}^16.
```

For each `1<=r<=4` and `e in {2,3,4}`, it tests the literal equality
of the final `er` symbols with `e` copies of the final `r` symbols.
A state is locally admissible when it has at least one tested square
and no tested fourth power.  It has the unique necessary successor

```
suffix_15(w) 3,    if a tested cube exists,
suffix_15(w) 2,    otherwise.                      (26)
```

An edge is retained only when the successor is itself locally
admissible.  This graph is a supergraph of the 16-symbol windows of
every binary fixed replay satisfying (25): it deliberately imposes no
conditions on roots above four.  Therefore omitting such conditions
cannot create a false nonexistence result.

The executed output is

```
{'states': 65536, 'locally_admissible': 37780,
 'admissible_edges': 23904, 'directed_cycles': 0,
 'maximum_path': 8}
```

The program checks acyclicity by a three-color depth-first traversal
of the complete functional graph.  It raises an assertion on a gray
revisit.  Only after that traversal succeeds does a memoized recursion
compute the maximum path length.

If a finite circular profile `P` satisfying (25) existed, the
successive length-16 windows of `P^Z` would follow (26) and return to
their initial window after `|P|` steps.  They would therefore give a
directed cycle in the enumerated graph.  The exhaustive graph has no
directed cycle.  This contradiction excludes (23).

The repository calibration

```
python -m unittest \
  tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
```

was executed immediately before this certificate and passed.  The
certificate itself uses literal suffix-power equalities rather than
calling the curling-number implementation.
