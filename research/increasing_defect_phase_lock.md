# Increasing defects: phase locking and exclusion of the crossing rescue

This note continues `bounded_defect_carriers.md`.  It treats the unresolved
orientation `d>a` using the complete proper-circular equation of the child
root, rather than only the two displayed border equations.

## 1. Setup and cut convention

Use zero-based cuts.  Let

```
U=C A,                    p=|U|,
V=C A C A C,              q=|V|=3p-a,
a=|A|,                    h=|C|=p-a.
```

Assume that `U,V` are primitive binary words and

```
pc_U=U,       pc_V=V.
```

The next internal defect is a border

```
D=V[:d]=C[:d]=C[-d:],
a<d<h,
C[d]=3.
```

Put

```
D=A E,       e=|E|=d-a.
```

The pointed old defect gives `E[0]=C[a]=3`.  The two exact word
identities which locate every cut used below are

```
V A=(C A)^3=U^3,
V D=U^3 E.                                             (1)
```

For `0<=t<=e`, define

```
S_t=U^3 E[:t]=V V[:a+t].                              (2)
```

Fixedness of `V` and actual replay from the visible state `V` give

```
cn(S_t)=E[t]       for 0<=t<e,
cn(S_e)=V[d]=3.                                        (3)
```

Every numerical instance of (3) in this note is evaluated in
`check_increasing_defect_phase_lock.py`; equation (3) itself is the
symbolic fixed-profile hypothesis.

Choose a primitive maximizing cube root `R` at `S_e`, and write

```
r=|R|.
```

The co-terminal primitive square `D^2` and cube `R^3` give the split
proved in `bounded_defect_carriers.md`.  The only residual case is

```
r>d.                                                   (4)
```

The post-promotion escape theorem gives

```
r<p.                                                   (5)
```

## 2. Exact phase lock through all emitted symbols

Since `e<d<r`, the final `e` symbols of `R` are exactly `E`.  Write

```
R=F E,             |F|=r-e,
W=E F.                                                   (6)
```

### Lemma 1 (rotating square)

For every `0<=t<=e`, put

```
Y_t=E[t:] F E[:t].                                    (7)
```

Then `Y_t` is a conjugate of `R`, has length `r`, and

```
S_t ends in Y_t^2.                                    (8)
```

At `t=e`, the same occurrence has matured to

```
S_e ends in R^3.                                      (9)
```

### Proof

The displayed final cube is

```
R^3=F E F E F E.
```

Deleting the last `e-t` symbols leaves

```
F E F E F E[:t].
```

Its final `2r` symbols start `r-e+t` symbols into the first displayed
copy of `F E`.  They are

```
E[t:] F E F E[:t]
  =(E[t:] F E[:t])(E[t:] F E[:t])
  =Y_t^2.
```

No symbol outside the displayed cube is used.  At `t=e`, no deletion
has occurred and (9) is the selected cube.

Thus all cuts in (2), not just the final cut, carry one fixed conjugacy
class of square witnesses.  In particular, whenever `E[t]=2`, (3) and
(8) make `Y_t` a maximizing square root.

## 3. What the full binary profile adds

### Lemma 2 (the final run has at most one-symbol wings)

The maximal period-`r` run containing the cube in (9) extends at most one
symbol to the left and at most one symbol to the right of the displayed
`R^3`.

### Proof

A primitive binary fixed profile has no circular factor `333`: three
consecutive symbols `3` would give a root-one cube at the following cut,
whose required label is the following symbol `2`; a circular all-`3`
word is nonprimitive.

If the period-`r` run extended two symbols left, root-`r` cubes would
end at the three consecutive cuts `d-2,d-1,d`.  Fixedness would label
all three cuts `3`, giving the forbidden factor.  The right-hand
argument uses the consecutive cube endpoints `d,d+1,d+2`.

Consequently, if

```
0<=t<=e-2,       E[t]=3,
```

and `s` is any primitive maximizing cube-root length at cut `a+t`, then
`s!=r`.  The root-`r` square from Lemma 1 and the root-`s` cube are
co-terminal.  Put `g=gcd(r,s)`.  Their common suffix has length
`min(2r,3s)`.  Fine--Wilf at length `r+s-g` would make a complete
conjugate of one primitive root have the proper period `g`.  Threshold
failure gives the exhaustive alternatives

```
s<r  and  2s+g<r,
s>r  and  s>r+g.                                    (10)
```

For the first line, `2r<3s` would make threshold failure read
`r+g<s`, contrary to `s<r`; hence the common length is `3s`, producing
the displayed inequality.  For the second line the common length is
`2r`, producing its displayed inequality.

This is the exact use of all the intervening equations `pc_V=V`:

* every `2` in `E` is covered by the same rotating maximizing square;
* every `3` at distance at least two from the final cut must use a
  genuinely different scale satisfying (10);
* the final root can explain at most the final two consecutive `3`
  labels.

The standard Three Squares Lemma is compatible with this conclusion but
does not improve it.  Reversing co-terminal squares makes them
common-prefix squares.  Bannai--Mieno--Nakashima, Lemma 1, states that
if roots `u>v>w` give three common-prefix squares and `w` is primitive,
then `|u|>=|v|+|w|` (arXiv:2006.13576).  It bounds a scale ascent in
(10), but supplies no prefix-state closure.

## 4. Fine--Wilf location of the rescue

Deleting all of `E` from the final cube leaves a suffix of `U^3` of
length

```
3r-e
```

with periods `r` and `p`.  Put `g_p=gcd(p,r)`.  If this length reached
`p+r-g_p`, Fine--Wilf would give period `g_p<r` to a complete conjugate
of primitive `R`.  Therefore

```
3r-e<p+r-g_p,
2r+g_p<p+e.                                        (11)
```

In particular `r<h`: since `e=d-a<h-a=p-2a`,

```
2r < p+e < 2(p-a)=2h.
```

The apparent crossing alternative is

```
2r>p.
```

Put

```
delta=2r-p.
```

Equation (11) gives

```
0<delta<e.                                         (12)
```

The next lemma shows that (12) is not a new carrier.  It is impossible.

## 5. Copied-tail completion lemma

### Lemma 3

Let `U` be a word of length `p`.  Let positive integers `a,e,r` satisfy

```
a+e<r<p,
2r>p,
0<delta:=2r-p<e.                                  (13)
```

If

```
U^3 U[a:a+e]
```

ends in an `r`-root cube, then `U` has period

```
g=gcd(p,a,r).                                      (14)
```

Because `0<a<p`, this period is proper.

### Equality-graph proof

Put

```
b=p-r,
c=e-delta.
```

Then

```
p=2b+delta,
r=b+delta,
e=c+delta,
a+c<b.                                            (15)
```

Fold the three copies of `U` modulo `p`, and fold the appended copy
`U[a:a+e]` back to its source coordinates.  Comparing adjacent copies
of the final `r`-cube gives exactly these two edge families on
`Z/pZ`:

```
j  ~  j+b mod p          for c<=j<p,              (16)
a+y ~  b+y               for 0<=y<e.              (17)
```

To check (16), use the cube comparison whose endpoint lies before the
appended tail.  Its endpoint coordinate ranges from `e-2r` through
`-1`.  Since

```
e-2r=c-p,
```

reduction modulo `p` gives exactly `c,c+1,...,p-1`.  A backward
root shift by `r` is a forward shift by `p-r=b`.

For (17), the `y`-th appended symbol is `U[a+y]`; the symbol one root
earlier is at coordinate `-r+y`, which reduces to `b+y`.  The bound
`b+e<p` follows from `c<b`, so no second reduction is hidden.

The following interval-repair fact is the arithmetic core.

> **Interval-repair fact.**  Under (15), the graph (16)--(17) has as
> its connected components exactly the residue classes modulo
> `gcd(p,a,b)`.

Here is a contraction proof.  First adjoin the `c` omitted edges

```
j~j+b,       0<=j<c.                              (18)
```

The resulting `b`-edge graph has the residue classes modulo
`g_0=gcd(p,b)=gcd(b,delta)` as its components.  In this quotient,
the `e=c+delta` consecutive edges (17) contain, for every residue
`y mod g_0`, the edge

```
y ~ y+a mod g_0,
```

because `b=0 mod g_0` and `e>delta>=g_0`.  They therefore merge the
`g_0` classes to the classes modulo `gcd(g_0,a)`.

It remains to justify that adjoining (18) did not change a component.
Write

```
s=a+delta.
```

For every `0<=x<c`, (16) at `b+delta+x` and (17) at
`delta+x` give the explicit path

```
x
 ~ b+delta+x
 ~ a+delta+x
 = x+s.                                             (19)
```

All indices in this path are legal: `delta+x<delta+c=e`, while
`b+delta+x<p` follows from `x<c<b`.

We now prove, by strong descending induction on `x` from `c-1` to
`0`, the statement

```
Q(x):  x~x+a.
```

Fix `x<c` and assume `Q(z)` for every integer `z` with
`x<z<c`.

* If `x+s>=c`, put `z=x+s`.  Equation (15) gives

  ```
  delta<z<c+s=c+a+delta<b+delta.
  ```

  Hence both starts `z` and `z+b` lie in the range of (16), and its
  two retained edges give

  ```
  z ~ z+b ~ z+2b-p=z-delta=x+a.
  ```

  Prepending (19) proves `Q(x)`.

* If `x+s<c`, then `x<x+s<c`, so the induction hypothesis gives
  `Q(x+s)`.  Also `x+a<x+s<c`, so (19) is available with `x+a`
  in place of `x`.  The resulting path is

  ```
  x ~ x+s ~ x+s+a=x+a+s ~ x+a,
  ```

  where the first and last connections are (19), the last traversed
  backwards, and the middle connection is `Q(x+s)`.  This proves
  `Q(x)`.

These two cases are exhaustive.  For each `0<=x<c`, append (17) at
`x` to `Q(x)`:

```
x ~ x+a ~ b+x.
```

Thus the endpoints of every omitted edge (18) were already connected,
so adjoining (18) does not change any component.

After this repair, the component modulus is

```
gcd(g_0,a)=gcd(p,b,a)=gcd(p,r,a),
```

which proves the interval-repair fact and Lemma 3.

`check_increasing_defect_phase_lock.py` independently constructs the
uncontracted equality graph directly from the three cube copies.  It
exhausts all `182780` admissible parameter tuples through `p=80` and
finds exactly the residue classes in (14).  This finite audit is not
used as the proof.

## 6. The crossing rescue is impossible

Apply Lemma 3 to the actual words.  Equations (1) and (6) give

```
S_e=U^3 U[a:d],
e=d-a.
```

Hypotheses (4)--(5) give `a+e=d<r<p`; (11) gives (12).  Lemma 3 makes
`U` have the proper period `gcd(p,a,r)`, contradicting the stipulated
primitivity of the reset root.

Therefore the increasing-defect rescue satisfies the strict bound

```
d<r<p/2.                                           (20)
```

The equality `2r=p` is also impossible: Lemma 1 at `t=0` would make

```
U=W^2,
```

contrary to primitivity.

No binary or fixed-profile property is used in Lemma 3.  Binary
fixedness is used in Lemma 2; the orbit history and `pc_V=V` are used
to obtain (1)--(4); primitivity and Fine--Wilf are used in (11).

## 7. Exact residual when `2r<p`

Put

```
sigma=p-2r>0,
K=U[:sigma].
```

Lemma 1 at `t=0` is now wholly inside the last copy of `U`, so

```
U=K W^2,       W=E F,       W[0]=3.               (21)
```

The longer factor inherited from the final cube is

```
U^3 ends in F W^2,       |F W^2|=3r-e.            (22)
```

There are two exact subcases.

### Contained predecessor

If

```
3r-e<=p,
```

then (22) lies in the last `U`.  Since `|K|=p-2r`,

```
K ends in F,
U=J F W^2,
|J|=p+e-3r.                                       (23)
```

### One-boundary predecessor

If

```
3r-e>p,
```

put

```
lambda=3r-e-p.
```

Since `2r<p`,

```
0<lambda<|F|,
|F|-lambda=sigma.
```

Alignment of (22) across the preceding `U|U` boundary gives

```
K=F[lambda:],
F[:lambda]=F[-lambda:].                            (24)
```

Thus `F` has the proper border `F[:lambda]` and the proper period
`sigma`.

Equations (21)--(24) are the strongest unconditional smaller object
currently obtained.  They do not by themselves form another reset
root or maturation carrier:

* `W` is a suffix root, not a prefix of the orbit word;
* `K` is a prefix state only when `sigma>=N_0`;
* even when visible, `K` has next label `W[0]=3` and its orbit emits
  `W^2` to reach `U`, but no exact proper-circular profile for `K` or
  `W` follows.

If `sigma>=N_0`, (21) does at least give a strictly shorter visible
bad state

```
K=T[:sigma],       cn(K)=3,
K W^2=U,           cn(U)=2,                       (25)
```

and `K[1:]` terminates in the fixed-deletion branch.  Relation (25) is
a closed orbit episode, but not a self-replaying carrier: its repeated
block `W` is not anchored at the left origin.  If `sigma<N_0`, even
this state is hidden in the initial seed.

## 8. Two consecutive increasing moves cannot both hide their prefix

The residual square has a useful one-generation inheritance bound.  Let
the next reset root be

```
V=U^3[:-a],       q=|V|=3p-a.
```

Suppose the following defect move is again increasing.  Applying
Sections 1--7 with `V` as the old root gives

```
V=K' Z^2,
z=|Z|,
sigma'=|K'|=q-2z>0,                               (26)
```

where `Z` is primitive.  The complete factor `Z^2` lies in the
`p`-periodic word `U^3`, so it has periods `z` and `p`.

If `z>p`, put `g=gcd(p,z)`.  Its length meets the Fine--Wilf threshold:

```
2z >= p+z-g
```

because `z>p`.  Fine--Wilf would make `Z^2` have period `g`.  Since
`g<=p<z`, its length-`z` prefix `Z` would have the proper period `g`,
contradicting the primitivity of `Z`.  Therefore

```
z<=p,
sigma'=q-2z >= p-a.                               (27)
```

In fact equality cannot occur in an increasing-defect residual.  Writing
`U=C A` with `|A|=a` gives

```
V=C A C A C=C(AC)^2.
```

If `z=p`, comparison of the final two root blocks in (26) makes
`Z=AC`.  But the phase-lock construction gives `Z=E'F'`, where the
new nonempty defect tail begins in

```
Z[0]=E'[0]=3,
```

whereas

```
(AC)[0]=A[0]=2.
```

This contradiction strengthens (27) to

```
z<p,
sigma'>p-a.                                        (28)
```

All late defects satisfy `a<N_0`.  Once `p>=2N_0`, (28) gives
`sigma'>=N_0`.  Consequently two consecutive increasing defect moves
cannot both produce a hidden prefix: regardless of whether the first
`sigma` lies in the seed, the residual prefix supplied by the second
move is a visible orbit state.

This does not yet orient a defect sequence which alternates increasing
and decreasing moves.  It does reduce the hidden-prefix recurrence to
isolated increasing moves; a completion still needs to combine the
visible state in (28), or the carrier supplied by the intervening
decrease, with the reset/tau rank.

## 9. Executed adversaries to stronger local claims

The checker supplies three exact emitted-phase models.  They satisfy
the displayed border geometry and every value in (3) on the interval
`a,...,d`, but fail the complete profiles away from that interval.

1. `p=17,a=1,d=3,r=5` has emitted values `(3,2,3)` and
   `d<r<2d`.  Hence neither `r=d` nor `r>=2d` follows from the local
   equations.
2. `p=23,a=1,d=4,r=7` has emitted values `(3,2,2,3)`.  At the two
   internal low cuts the maximizing root sets are `{7}` and `{4,7}`.
   Phase locking does not imply uniqueness.
3. `p=26,a=1,d=5,r=8` has emitted values `(3,2,2,3,3)`.  The
   root-eight cube ends at both final cuts, so the one-symbol wing in
   Lemma 2 is sharp.

In the first model the shorter suffix root is

```
W=32322,
pc_W=(2,1,2,2,2).
```

Thus even the exact local emitted segment does not make `W` a smaller
fixed profile.  The missing global equations `pc_U=U` and `pc_V=V`
are load-bearing.
