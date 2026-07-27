# Cube-record monotonicity between normalized tower levels

The raw proper-cube bound cannot be constant across nested levels.  This
note gives the correct normalization, proves the exact earliest-record
alternative, and records a genuine orbit relocation showing why deletion
of the last cube symbol does not by itself force an intermediate prefix.

## 1. The inherited bound

For a primitive binary proper-profile fixed word `Q`, let

```
R(Q)=max { r : a proper root-r cube occurs in Q^Z }.
```

If `n=|Q|` and `r` is such a cube root, then

```
2r+gcd(n,r)<n.                                   (1)
```

The cube factor has periods `r` and `n`.  At or above the Fine--Wilf
threshold

```
3r>=n+r-gcd(n,r),
```

it would acquire the gcd period on a factor containing a complete
length-`n` conjugate of `Q` and a complete primitive root-r block.  Since
`r<n`, one of those blocks would have a proper divisor period.  This
contradicts primitivity, proving (1).

Now take nested normalized levels

```
A=T[0:p],              B=T[0:N],
B begins A^3 3.
```

The cube `A^3` ends at phase `3p` of `B`, and `p<N`, so it is a proper
cube of the larger circular profile.  Therefore

```
R(A)<p/2,              R(B)>=p.                  (2)
```

Thus `R(A)=R(B)` is impossible.  The finite-memory statement that could
be useful is instead

```
R(B)=p: no new proper cube root longer than the inherited root A.  (3)
```

When the tower levels are selected from successive origin-zero cube
records, this says that while moving from the promotion of `A` to the
promotion of `B`, no new record lies strictly between `p` and `N`.
Without that record-level selection, `R(B)=p` is the intrinsic circular
statement and the orbit-record phrasing is only an implication, not an
equivalence.

## 2. Earliest larger record: prefix or relocation

Assume `T[e]=cn(T[0:e])` at every generated cut in the interval.  Let
`q>p` first occur as a primitive maximizing cube-root record at cut `v`.
Write

```
T[v-3q:v]=Y^3,              a=v-3q.              (4)
```

The next orbit label is three.  Immediately before the final symbol of
the cube was appended, deletion gives the exact suffix

```
T[a:v-1],
```

of length `3q-1` and period `q`.  This is the strongest conclusion
available from the earliest endpoint alone.

There are two exhaustive origin cases.

### Origin zero

If `a=0`, put `Q=T[0:q]=Y`.  Equation (4) gives

```
T[0:3q]=Q^3,             T[3q]=3.                (5)
```

Because these are absolute prefixes of the autonomous orbit word, for
every `0<=d<2q` the state at cut `q+d` is

```
Q T[0:d].
```

The actual orbit equality makes its next value `T[q+d]=T[d]`.  Equation
(5) identifies `T[0:2q]=Q^2`, so the orbit from `Q` appends two complete
copies of `Q` and then three.  Exact value three at the cube endpoint
makes `Q` primitive.  Thus an origin-zero record `p<q<N` is an
intermediate normalized prefix.

### Positive origin

If `a>0`, equation (4) is only a contexted maturation:

```
T[0:a] Y^3 3.                                   (6)
```

The local word `Y` may itself be normalized, but it starts at position
`a`, not at the absolute tower origin.

There is a sharp overlap restriction with the inherited prefix cube.  The
old `p`-periodic interval is `[0,3p)`.  If `a<3p`, its overlap with the
deleted `q`-periodic shadow is

```
O=3p-a.                                          (7)
```

For `q!=p`, Fine--Wilf and primitivity force

```
O<p+q-gcd(p,q),
```

or equivalently

```
a>2p-q+gcd(p,q).                                 (8)
```

If `a>=3p`, the two periodic intervals are disjoint and there is no
overlap inequality.  Equations (7)--(8) are exhaustive: once the overlap
misses the threshold, deletion gives no mechanism moving the internal
origin `a` to zero.

Consequently the desired monotonicity (3) is equivalent to excluding the
positive-origin relocation branch (6) for a normalized lower level.  The
existing record-root descent does not do this for one record.  It excludes
an unbounded family at one earlier fixed origin, while the origins of
successive relocated records may move to the right.

## 3. Executed smallest promoted-orbit relocation

`research/check_cube_record_finite_memory.py` recomputes every value below
with both implementations in `curling.py`.

Exhaust all primitive binary words `A` beginning in two for
`1<=|A|<=7`, retain those with exact cube maturation

```
cn(A^3)=3,
```

and follow the genuine orbit from `A^3 3` to its first one.  The first
larger cube-root records found are:

| `|A|` | `A` | record cut | root | origin |
|---:|---|---:|---:|---:|
| 4 | `2232` | 63 | 21 | 0 |
| 4 | `2322` | 63 | 21 | 0 |
| 7 | `2322232` | 76 | 21 | 13 |

There is no positive-origin example for a smaller `|A|` in this exhaustive
scan.  The length-seven example is the smallest by promoted-root length.

For

```
A=2322232,            p=7,
```

the promoted seed has length `22`.  At cut `76` the exact value is three,
with sole maximizing cube-root length `q=21` and origin `a=13`.  The
primitive root is

```
Y=223222323222322232232,
```

and the actual orbit word satisfies

```
T[13:76]=Y^3.
```

At the preceding cut `75`, the value is two and the maximizing square-root
lengths are `3` and `21`; appending the actual next symbol completes the
root-`21` cube.  At cut `76`, root `21` is the sole maximizing cube root,
and the next actual label is three.  Thus this is an exact internal
square-to-cube maturation, not a factor inserted by hand.

The deleted periodic shadow `[13,75)` overlaps the inherited prefix cube
`A^3=[0,21)` in only

```
O=8
```

symbols.  Here

```
gcd(7,21)=7,
p+q-gcd(p,q)=21,
```

so the overlap misses Fine--Wilf by thirteen symbols.  The old promotion
marker at position `21` is copied by the new period to positions `42` and
`63`.

The internal root `Y` is itself a normalized replay word, but no absolute
prefix `T[0:n]` with `7<n<76` is normalized; the checker tests every one.
The lower word `A` is not normalized, since its exact phase-zero value is
one.  Hence this is not a counterexample to (3) under the full nested-tower
hypotheses.  It is a counterexample to deriving (3) from earliest-record
deletion, genuine orbit history after promotion, and overlap with `A^3`
alone.  Any proof must use `pc_A=A` to rule out the relocation origin
`a=13`; that use is not supplied by the finite-memory argument.

## 4. Q21 audit

For the primitive fixed word

```
P=223222322232322232223,
```

the global proper cube-root bound is four.  The checker follows every
phase-zero rotation through its postpromotion orbit to the first one.  The
maximum cube-root lengths reached are

```
shift 0:0, 1:10, 3:0, 4:1, 5:3,
7:0, 8:21, 9:7, 11:0, 13:0,
14:2, 15:0, 17:0, 18:6, 19:1.
```

Every value in this list is at most the inherited root length `21`.  The
long shift-eight branch has successive cube-root records `1,4,21`, at
positive origins `64,62,55`.  This supports (3) at the only fully audited
binary fixed profile, but it does not prove the exclusion of a larger
relocated record.
