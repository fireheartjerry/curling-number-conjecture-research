# The typed endpoint-rank graph for the contained completion fork

This note tests whether the remaining completion fork can be closed by
adding fixed type offsets to the natural terminal-endpoint rank.  It uses
three object types.

```
O=(aX bad, X terminal),
R_O=|aX|+tau(X).

C=(W3 bad, W2 terminal),
R_C=|W2|+tau(W2).

R=(aX terminal, X bad),
R_R=|aX|+tau(aX).
```

For a general reverse reset, the two completion symbols in type `C` are
`k-1` on the bad side and `k` on the terminal side.  The formulas below
use `3,2` for the ordinary symbol-two completion and retain the same type
for either orientation.

## 1. Exact transition deltas

### 1.1 `O -> C` at the cubic completion

At the selected ordinary boundary put

```
A=C^3 bad,       D=A[1:] terminal,
H=A3 bad,        E=A2 terminal,
F=D3,            B=D2.
```

The actual first step of `D` is `D -> B`, so

```
tau(B)=tau(D)-1.
```

If `F` is bad, then `(F,B)` is a type-`C` object with common prefix
`D`.  Since `|B|=|A|`,

```
R_C-R_O
 =(|B|+tau(B))-(|A|+tau(D))
 =-1.                                             (1)
```

This is the exact favorable mixed-type descent.

If `F` is terminal, `(H,F)` is another type-`O` object.  Its delta is

```
R_O(H,F)-R_O(A,D)
 =1+tau(F)-tau(D).                                (2)
```

For the minimum-rank, maximum-length selection, (2) is at least one.
Section 4 of `contained_completion_fork.md` also proves that the next
whole-power root in this branch has length

```
r>2|C|+gcd(|C|,r).
```

Thus this branch is a same-type rank increase coupled to scale inflation,
not a rank descent.

### 1.2 Deleting the first symbol of a type-`C` object

Write the common prefix as `W=aX`.  The parent object is

```
aX3 bad,                  aX2 terminal,
R_C=|X|+2+tau(aX2).                              (3)
```

The statuses of `X3` and `X2` give all possible exits.

If `X3` is bad and `X2` is terminal, the shorter type-`C` object has

```
Delta_(C->C)
 =tau(X2)-tau(aX2)-1.                             (4)
```

If `X3` is terminal, then

```
a(X3) bad,                 X3 terminal
```

is type `O`, with

```
Delta_(C->O)
 =tau(X3)-tau(aX2).                               (5)
```

If `X2` is bad, then

```
a(X2) terminal,            X2 bad
```

is type `R`.  Its terminal word is literally the terminal word of the
parent type-`C` object, so

```
Delta_(C->R)=0.                                  (6)
```

The cases are exhaustive because each of `X3,X2` has one of the two
statuses.  Two exits occur when `X3` is terminal and `X2` is bad.

### 1.3 The minimum reverse reset

For a type-`R` object selected with minimum terminal hitting time,
`reverse_status_reset.md` gives

```
A=aB=Y^k terminal,       B bad,
B(k-1) bad,              Bk terminal.
```

The last two words form a type-`C` object.  Since `|Bk|=|A|`,

```
Delta_(R->C)=tau(Bk)-tau(A).                     (7)
```

The reverse-reset proof establishes terminality of `Bk`, but it gives no
upper or lower bound on the difference in (7).  Minimality of `tau(A)`
does not apply to `Bk`, because deleting the first symbol of `Bk` does
not recover the bad word `B`.

## 2. Constant type offsets cannot orient the coarse graph

Consider a proposed integer-valued potential

```
Phi(T)=R_T+w_T,          T in {O,C,R},
```

with fixed integer offsets.  Strict descent on the exact zero edge (6)
requires

```
w_R<=w_C-1.                                      (8)
```

If the free timing difference (7) is zero, strict descent on `R->C`
requires

```
w_C<=w_R-1.                                      (9)
```

Adding (8) and (9) gives

```
0<=-2,
```

which is impossible.  A zero value in (4) is an even shorter
obstruction: a type offset cancels on a `C->C` self-edge.

These equations refute a proof using only the displayed transition
deltas and one constant offset per coarse type.  They do not prove that a
genuine bad word realizes a zero cycle.  A stronger argument may use the
infinite badness hypothesis to prove a missing strict inequality, refine
`C` by completion orientation or root provenance, or add a nonconstant
word statistic.

## 3. Executed timing countermodels to the missing inequalities

After the required A094004 calibration,
`check_typed_completion_rank_graph.py` recomputes all orbit steps with
both curling-number implementations.

### 3.1 A relaxed zero `C->C` self-edge

Put

```
W=22232223222322,       X=W[1:].
```

The executed tail lengths are

```
tau(W3)=52,       tau(W2)=2,
tau(X3)=52,       tau(X2)=3.
```

Therefore the two terminal endpoints on the `2` side are equal:

```
|W2|+tau(W2)=17=|X2|+tau(X2).
```

The two `3` sides are not bad; each reaches one after 52 steps.  This is
a finite near-model of the typed zero self-edge, not a counterexample to
the conjecture.  It shows that no argument inspecting a bounded initial
segment or only the terminal `2` column can make (4) strictly negative.

### 3.2 Reverse-reset timing has no static sign

For reset-shaped finite words `A=Y^3`, `B=A[1:]`, the checker verifies
`cn(A)=3` and `cn(B)=2`.  With the terminal completion `B3`, the values of

```
tau(B3)-tau(A)
```

are respectively

```
0, 1, 9
```

for

```
Y=(3),       Y=(2,3,2,2),       Y=(2,2,3,2).
```

Here `B` is terminal rather than bad, so these are timing countermodels
to a local sign inference, not type-`R` counterexamples.  Any proof that
(7) is negative must use the badness of `B` in a genuinely global way.

### 3.3 Exact-profile sibling tails point both ways

Across the fifteen symbol-two rotations of the exact Q21 profile, the
executed differences

```
tau(D3)-tau(D2)
```

range from `-59` to `52`.  Hence exact proper-profile and first-copy
fitting equations do not order the two completion tails.  The status
hypotheses or a finer ancestry invariant are load-bearing.

## 4. Consequence for the remaining proof

The scalar descent (1) is real, but it lands in type `C`.  The first
reverse exit from `C` is the zero edge (6), and the known reverse reset
returns to `C` with the uncontrolled difference (7).  Therefore the
three coarse endpoint ranks cannot close the completion fork by fixed
offsets.

The smallest viable refinement must retain at least one of:

1. the orientation and values of the two completion symbols;
2. the primitive reset root and whether the terminal endpoint is its
   actual successor;
3. the origin position of the changed symbol inside the next whole-power
   reset; or
4. a theorem using infinite badness to give a strict sign to (4) or (7).

Without such information, the relaxed typed graph contains a zero
`C->R->C` cycle and a zero `C->C` self-loop.

