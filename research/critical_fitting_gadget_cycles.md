# Critical fitting on singleton-3 gadget cycles

This note records the exact translation of the deleted-seed condition
into run-code coordinates.  It also gives two executed countermodels
showing that fitting does not by itself exclude a `g=2` edge or a cycle
of winding greater than one.

## 1. Physical and run-code coordinates

Let

```
Q(A)=product_(r=0)^(m-1) 2^(a_r) 3
```

for a cyclic code `A=(a_0,...,a_(m-1))`, and put `N=|Q(A)|`.  Choose
phase zero inside run zero, at offset `delta` from that run's beginning;
the critical root begins at that phase.  Thus the lifted start of run
zero is `-delta`, and

```
start(r+m)=start(r)+N.
```

A tight cube gadget ending at canonical run index `i`, with code span
`s`, begins in lifted run

```
j=i-3s.
```

Its physical cube is first-copy fitting precisely when its left endpoint
is at or to the right of physical coordinate `1-N`.

### Lemma 1 (exact code fitting inequality)

The gadget is first-copy fitting if and only if

```
3s <= m+i-1.                                      (1)
```

### Proof

The possible lifted beginnings are run beginnings.  The run beginning
one code period before run zero is

```
start(-m)=-N-delta < 1-N.
```

The next run beginning is

```
start(-m+1)=-N-delta+(a_0+1).
```

Since `0<=delta<a_0`, this is at least `2-N`, hence is strictly to the
right of `1-N`.  Monotonicity of lifted run beginnings now gives

```
start(j)>=1-N  iff  j>=-m+1.
```

Substitution of `j=i-3s` gives (1).  Notice that the offset `delta`
cancels, so the result does not require phase zero to be the first symbol
of its ambient 2-run.

## 2. Winding is the number of origin crossings

Select one fitting gadget at each vertex of a directed gadget cycle.
For its edge ending at canonical index `i`, (1) gives

```
-m < i-3s < i.
```

Consequently the canonical target is

```
i-3s+w_i m,    w_i in {0,1},
```

where `w_i=1` exactly when the lifted gadget arc crosses the code origin.
Telescoping the target indices around the directed cycle gives

```
3 sum s = m sum w_i.
```

The left side divided by `m` is the cycle winding.  Therefore:

> For fitting selected edges, the winding equals the number of selected
> gadget arcs crossing the common first-copy origin.

In particular, winding greater than one means that at least two distinct
selected gadgets simultaneously straddle that origin.  This is the
extra linear information absent from a purely circular gadget graph.

## 3. Fitting alone does not exclude winding two

The primitive code

```
A=233133133233133
```

has the fitting selected cycle

```
0 -(s=1)-> 12 -(s=1)-> 9 -(s=1)-> 6
  -(s=6,g=2)-> 3 -(s=1)-> 0.
```

Its span sum is ten, so `3 sum s=30=2m`.  Every defect is selected and
every first-2 cut has a proper square.  Direct binary enumeration finds
the obstruction required by the exact profile: both first offsets of
run nine end a proper period-ten cube, even though they are labelled
`2`.

Thus the fitting inequality, positive gadget coverage, and square
coverage do not eliminate a `g=2` winding-two cycle.  The global
no-cube constraint at all `2`-cuts is load-bearing.

There is a complementary primitive code

```
A=122133122133233122133233
```

with a fitting winding-two selected gadget cycle and no proper cube at
any `2`-cut.  It instead has uncovered defects and weak-square holes.
Thus the negative constraint alone does not eliminate winding two
either.

`research/check_critical_fitting_gadget_cycles.py` reconstructs both
cycles from the exact tight-gadget graph and directly enumerates every
claimed square and cube root.  The precise remaining target is a coupled
statement: a fitting cycle of winding greater than one must force at
least one of a forbidden cube at a `2`-cut, a weak-square hole, or an
uncovered defect.
