# Record-depth origins along canonical ancestors are not monotone

This note tests a refinement of the failed consecutive-root stack:
restrict attention to strict records along one canonical copy-parent ray.
Even on the guaranteed monochromatic `2`-ray, neither root-length records
nor complete-powered-depth records move their left endpoints toward the
absolute origin.

For an appended vertex `v`, let

```
e(v)=cn(T[0:v+1]),
p(v)=the least primitive maximizing-root length,
parent(v)=v-p(v),
L(v)=v+1-e(v)p(v),
D(v)=e(v)p(v).
```

Thus `[L(v),v+1)` is the complete canonical power and `D(v)` is its
powered depth.

## Root-length record moves right

The exact orbit from

```
22322232
```

has the following two consecutive vertices on one canonical `2`-ray:

```
v=11: parent 7,  e=3, p=4, L=0, D=12,
v=17: parent 11, e=2, p=6, L=6, D=12.
```

The second span is a strict ray record, `6>4`, but its powered interval
starts six positions farther right.  The old cube is replaced by a
larger-root square of the same total depth.  Therefore record root length
does not orient the ancestor origin.

## Powered-depth record moves right

The exact orbit from

```
23222322
```

contains the canonical `2`-ray segment

```
v     e   p    L    D
10    2   4    3    8
13    2   3    8    6
17    2   4   10    8
21    3   4   10   12
```

The last vertex sets a strict powered-depth record, `12>8`, but the new
record origin is `10`, strictly to the right of the preceding record
origin `3`.  A scale drop and same-scale rebirth moved the periodic run
right before it matured from a square to a cube.

These examples are actual deterministic orbit segments, not static word
models.  They refute both candidate ranks

```
left endpoint of successive ray-span records,
left endpoint of successive powered-depth records.
```

The only unconditional well-founded coordinate is the absolute vertex
position under backward parent iteration.  It decreases for the tautological
reason that every parent is earlier, but the examples show that the
periodic origin attached to a later record can move right.  Hence that
coordinate alone cannot turn unbounded record depth into an origin-zero
tower.

`check_record_depth_ancestor.py` recomputes every displayed curling number,
all maximizing roots, canonical parents, and the two record failures.
