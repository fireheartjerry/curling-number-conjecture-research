# Coupling after the minimum-hitting-time pure-power split

This note continues `research/minimal_deleted_hitting_time.md`.  It
records the exact one-step alternatives after the immediate divergence.
It does not prove termination.

## 1. Setup and the wrong append

Let `A` be selected by minimum deleted-orbit hitting time.  Put

```
A=Y^k,                   r=|Y|,
L=A[1:]=Y[1:]Y^(k-1),
cn(A)=k,                 cn(L)=k-1,
```

where `Y` is primitive and `k>=2`.  The actual first successors are

```
H=A k,                   B=L (k-1).
```

The word `H` is bad.  If `k>=3`, then `B` is the next state on the
terminating orbit from `L`, so

```
tau(B)=tau(L)-1.
```

Define the wrong high-context append

```
W=A (k-1).
```

Then `W[1:]=B`.  The word `W` must terminate: if it were bad, it would
belong to the deletion class with deleted hitting time `tau(B)`, which
is strictly below the minimum used to select `A`.  Thus, for `k>=3`,

```
A k       is bad,
A (k-1)  terminates.                              (1)
```

This conclusion does not follow from the same argument when `k=2`,
because `cn(L)=1` already gives `tau(L)=0`; there is no lower
nonnegative hitting time after appending the `1`.

## 2. Appending one term raises `cn` by at most one

### Lemma 1

For every nonempty word `S` and every integer `x`,

```
cn(S x) <= cn(S)+1.                               (2)
```

### Proof

Suppose `S x` ends in `Z^q`, where

```
Z=z_0 z_1 ... z_(s-1),       z_(s-1)=x.
```

After deleting the final symbol, the last `(q-1)s` symbols are

```
(z_(s-1) z_0 ... z_(s-2))^(q-1).
```

This is a suffix of `S`, so `cn(S)>=q-1`.  Apply this to a maximizing
power in `S x` to obtain (2).

In the coupled square,

```
C=H[1:]=L k,
B=W[1:]=L (k-1),
```

Lemma 1 gives

```
cn(C)<=k,                  cn(B)<=k,
cn(H)<=k+1,                cn(W)<=k+1.             (3)
```

## 3. Exact same-scale-or-drop lemma

### Lemma 2

Let `V` be primitive of length `r`, let `m>=2`, and let `x` be an
integer.  Consider either

```
E=V^m x,
D=V[1:] V^(m-1) x.
```

If one of these words ends in a primitive `q`-th power with root length
`s` and `q>=2`, then exactly one of the following applies.

1. `s=r` and `x=V[0]`.
2. `s!=r` and

   ```
   (q-1)s+gcd(r,s)<=r,                            (4)
   ```

   in particular `s<r`.

If `x=V[0]`, then

```
D=(rot_left(V))^m.                                (5)
```

For `r>1`, the suffix of `E` beginning after its first symbol is also
`(rot_left(V))^m`; for `r=1`, `E` is the unary `(m+1)`-power.

### Proof

Delete the final `x` from the selected `q`-power.  The remaining factor
has length `q s-1` and periods `s` and `r`: in `E` it lies in `V^m`,
and in `D` it lies in the length-`mr-1` factor
`V[1:]V^(m-1)` of `V^Z`.

Put `g=gcd(r,s)`.  If `s!=r` and

```
q s-1 >= r+s-g,
```

Fine--Wilf gives period `g` to the factor.  The threshold makes the
factor long enough to contain a complete conjugate of the longer of
the primitive length-`r` and length-`s` roots.  Since
`g<max(r,s)`, that conjugate would have a proper period, a
contradiction.  Threshold failure over the integers is exactly (4),
and (4) implies `s<r`.

If `s=r`, compare the final length-`r` root block with the preceding
one.  Its final symbol `x` occupies the phase of `V[0]`, so equality
requires `x=V[0]`.  Direct rotation gives (5) and the final statements.

## 4. The three first-symbol cases

Put `y=Y[0]` and `R=rot_left(Y)`.  Apply Lemma 2 with
`x=k` and `x=k-1`.

### Case I: `y=k`

The high deleted successor is the exact rotation power

```
C=R^k,                    cn(C)=k.                (6)
```

The equality for `cn(C)` uses (3).  Every powered suffix in `B` or `W`
whose displayed root is primitive and whose exponent is at least two
has root length strictly below `r` and obeys (4).

The high value has only two possibilities:

```
cn(H) in {k,k+1}.                                  (6a)
```

If it is `k+1`, prefixing the first symbol of `H` to `C` has raised the
curling number strictly.  The same whole-power argument used in
`minimal_deleted_hitting_time.md` forces

```
H=Z^(k+1),
|Z|=(k*r+1)/(k+1)<r,
r=1 mod (k+1).                                    (6b)
```

Thus a strict same-side value rise is itself a smaller-root whole-power
maturation.

### Case II: `y=k-1`

The low successor is the exact rotation power

```
B=R^k,                    cn(B)=k.                (7)
```

Again (3) makes the value exact.  Every powered suffix in `C` or `H`
whose displayed root is primitive and whose exponent is at least two
has root length strictly below `r` and obeys (4).

The terminating wrong successor obeys

```
cn(W) in {k,k+1}.                                  (7a)
```

If its value is `k+1`, the identical strict-prefix argument gives

```
W=Z^(k+1),
|Z|=(k*r+1)/(k+1)<r,
r=1 mod (k+1).                                    (7b)
```

### Case III: `y` is neither `k` nor `k-1`

Every powered suffix with primitive displayed root and exponent at least
two in all four words

```
H, W, C, B
```

has root length strictly below `r` and obeys (4).

The same-scale high and low alternatives are mutually exclusive.  This
is a genuine local rank drop, but it is not yet a global rank: after the
drop, a longer power can be supplied by left context at a later state.

## 5. Existing-symbol consequence

If an orbit avoids one at both a state `S` and its successor
`S c`, where `c=cn(S)`, then the integer `c` already occurs in `S`.
Indeed, a square suffix of `S c` must copy its final symbol `c` to an
earlier position.

Consequently every curling number appended by a bad orbit belongs to
the finite alphabet of its initial word.  In the present normal form,

```
k occurs in Y.                                    (8)
```

If `tau(L)>=2`, then `B` also avoids one, so the same argument gives

```
k-1 occurs in Y.                                  (9)
```

The second assertion need not hold when the low branch reaches one at
`B`.

The root `Y` cannot be unary.  By (8), a primitive one-letter `Y` would
have to be the word `(k)`.  Then the first three states on the high
orbit would be

```
k^k,       k^(k+1),       k^(k+1) (k+1).
```

Their curling numbers at the first two states are respectively `k` and
`k+1`.  The last appended symbol `k+1` has no earlier occurrence, so
the third state has curling number one.  This contradicts badness.
Therefore

```
r>=2.                                             (10)
```

## 6. Distinct final completions force root-scale separation

### Lemma 3

Let `P` be a word and let `a!=b`.  Suppose

```
P a ends in U^u,       |U|=p,       u>=2,
P b ends in V^v,       |V|=q,       v>=2,
```

where `U,V` are primitive.  Then `p!=q`.  Put `g=gcd(p,q)`.
If `p<q`, then

```
(u-1)p+g<=q.                                      (11)
```

If `q<p`, then

```
(v-1)q+g<=p.                                      (12)
```

### Proof

For `p=q`, period `p` would require both distinct final symbols `a`
and `b` to equal the same symbol of the common prefix `P`, which is
impossible.

Delete the two final symbols.  The common prefix has co-terminal
suffixes of lengths `u p-1` and `v q-1`, with periods `p` and `q`.
Suppose `p<q`.  The second suffix has length at least `2q-1`, which
is at least the Fine--Wilf threshold `p+q-g`.  If the first suffix
also met that threshold, their common co-terminal factor would have
period `g` and would contain a complete conjugate of the primitive
length-`q` root.  This would give that root the proper period `g<q`.
Therefore

```
u p-1<p+q-g,
```

which is (11).  Interchanging the two words proves (12).

Apply this to the bad actual successor `H=A k` and the terminating
wrong successor `W=A (k-1)`.  If `cn(W)=1`, the wrong successor is
already at a one.  Otherwise, for primitive maximizing roots of lengths
`s,t` and exponents

```
h=cn(H),                w=cn(W),
```

the roots are unequal and satisfy

```
s<t  =>  (h-1)s+gcd(s,t)<=t,
t<s  =>  (w-1)t+gcd(s,t)<=s.                     (13)
```

Thus the two sides cannot retain comparable distinct completion roots.
In Case III of Section 4 both roots are also below `r`; in Cases I and
II the only possible scale-`r` survivor is on the side whose appended
symbol matches `Y[0]`.

## 7. Executed obstruction to iterating the root drop

`curling.py` and its independent reference implementation were executed
on

```
k=3,             Y=2322232.
```

Here tail length means the number of orbit extensions before the first
current state of curling number one.  The complete output was:

```
word   length   cn   tail length   maximizing-root lengths
A        21      3       60                  7
L        20      2        4                  4,7
H        22      2       59                  2
W        22      3        3                  7
C        21      2       59                  2
B        21      3        3                  7
```

Here `Y[0]=k-1`, so Case II occurs: the low branch retains the
root-`7` rotation power, while the high branch drops to root `2`.
Nevertheless the high successor and its deletion have tail length
`59`, while the low rotation power has tail length `3`.

Thus the strict physical-root drop in Case II does not control
termination time, nor does it automatically create a new deletion pair
with smaller `tau`.  Any iteration must retain the coupled status
information in (1), not only the new root length.

## 8. Root length two is impossible for the selected bad power

### Lemma 4

In the minimum-hitting-time normal form, `|Y|` is not two.

### Proof

Section 5 says that `k` occurs in `Y`.  A primitive word of length two
containing `k` is therefore either

```
Y=(a,k)  or  Y=(k,a),       a!=k.
```

Both orbits can be evaluated uniformly in the arbitrary integer `a`.

First take `Y=(a,k)`.  Appending the initial value gives

```
(a k)^k  ->  (a k)^k k.
```

The new state has curling number exactly two.  The terminal `k k`
supplies the lower bound.  Lemma 2, with `r=2` and mismatching
completion `x=k!=a=Y[0]`, says that every primitive powered suffix has
root length below two and satisfies

```
(q-1)*1+1<=2.
```

Thus its exponent is at most two.

If `k>=3`, append `2`.  If `a!=2`, the final `2` has no earlier
occurrence and the resulting curling number is one.  If `a=2`, a
square root would have odd length `s`: its final `2` must match one of
the earlier even-indexed `2` symbols in `(2 k)^k`.  The two symbols
immediately before the final `2` are `k k`.  Translating the earlier
of these two positions left by odd `s` reaches an even-indexed `2`,
contradicting `2!=k`.  The square must fit, so
`s<=k+1<=2k-1`, and the compared position lies inside the displayed
periodic prefix.  Hence the curling number is one.

If `k=2`, the first two appended `2` symbols make a terminal run of
three `2` symbols.  Lemma 1 bounds its curling number by three, so it
is exactly three.  Append `3`.  For `a!=3`, this is a new final symbol.
For `a=3`, the word is `3232223`; its previous `3` symbols are four
and six positions before the final one, and neither distance can fit
twice in the length-seven word.  In both cases the curling number is
one.  Thus the successive values are

```
k>=3:  k,2,1,
k=2:   2,2,3,1.                                  (14)
```

Now take `Y=(k,a)`.  The first append gives

```
(k a)^k k = k (a k)^k.
```

Its curling number is exactly `k`: the displayed root-two power gives
the lower bound, Lemma 1 gives the upper bound `k+1`, and exponent
`k+1` cannot fit a root of length two; a root of length one cannot
square because the last two symbols are `a,k`.

Append `k`.  The terminal `k k` gives curling number at least two.
If a primitive root of length `s>=2` supplied exponent at least three,
its final `k` would match an earlier even-indexed `k` in `(k a)^k`,
so `s` would be odd.  Translating the penultimate final `k` left by
this odd distance reaches an odd-indexed `a`, a contradiction.  The
fit bound `3s<=2k+2` keeps that compared position inside the displayed
prefix.  Hence the value is exactly two.

For `k>=3`, append `2`.  When `a!=2`, the final symbol is new.  When
`a=2`, any square root length `s` must be odd because the previous
`2` symbols occupy odd indices of `(k 2)^k`.  The final block begins
in `k k 2`; shifting its earlier `k` left by odd `s` reaches an
odd-indexed `2`, a contradiction.  The fit bound
`2s<=2k+3` keeps the position inside the prefix.  The resulting value
is one.

For `k=2`, the appended values create a terminal run of three `2`
symbols and then append `3`.  If `a!=3`, the `3` is new.  If `a=3`,
the only previous `3` close enough to be a square mate is four
positions earlier, but the two candidate length-four blocks are
`2323` and `2223`, which differ.  The resulting value is one.  The
successive values are

```
k>=3:  k,k,2,1,
k=2:   2,2,2,3,1.                                (15)
```

Both orientations reach one, contradicting the choice of `A` as bad.
Together with (10), every selected bad root satisfies

```
|Y|>=3.                                           (16)
```
