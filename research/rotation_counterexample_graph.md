# Rotation exclusions from terminating suffixes

This note works in the binary critical normal form.  Let `P` be a
primitive word of length `p` over `{2,3}` whose proper circular curling
profile is `P`.  For a phase `j`, write

```
R_j=P[j:p]P[0:j].
```

The additional replay hypothesis used here is:

> Every rotation `R_j`, started as a finite word, appends two copies of
> itself and reaches `R_j^3`.

This property holds for the critical replay words under consideration.
The exclusion lemma below records exactly where it is used.

The hypothesis is not a formal consequence of circular fixedness without
the critical minimum-two condition.  The primitive word `121` has proper
circular profile `121`, but its executed first six finite outputs are

```
1,2,1,2,2,2,
```

so it replays one copy and does not reach its cube.  Any general replay
lemma used here must therefore retain the binary minimum-two hypotheses
or invoke the stronger critical synchronization equations.

## 1. Circular witness spans

At phase `i`, put `k=P[i]`.  Define `lambda(i)` to be the least powered
length `kq` among proper circular roots of length `q<p` attaining the
profile value `k`.  Thus a suffix of `P^Z` of length `lambda(i)` is a
`k`-power ending at phase `i`.

For a starting phase `j`, define its deletion-visibility radius

```
D(j)=min_{0<=t<p} (p+t-lambda(j+t mod p)).       (1)
```

If `1<=d<=D(j)`, then at every cut in the first replayed copy the suffix
word

```
R_j[d:p] R_j[0:t]
```

is long enough to contain a circular witness attaining the prescribed
value `R_j[t]`.

## 2. Multi-symbol suffix exclusion

Assume `R=R_j` is a shortest counterexample rotation.  In particular
`R[0]=2`.  Let `1<=d<p` satisfy `d<=D(j)`, and put

```
Q=R[d:p].
```

The word `Q` has length below `p`, so its orbit terminates.

For `0<=t<p`, suppose inductively that `Q` has appended `R[0:t]`.  Its
current length is `p-d+t<2p`.  Equation (1) puts a proper circular
`R[t]`-witness wholly inside the current word, giving the lower bound

```
cn(Q R[0:t])>=R[t].
```

Any suffix power of this finite word has root length below `p`, because
its exponent is at least two and the whole word has length below `2p`.
It is therefore a proper circular power at the same phase, giving the
reverse inequality.  This proves, by induction on `t` with base `t=0`,
that `Q` appends the first copy of `R`.

The same values are forced through a second copy.  At those cuts the
finite word has length below `3p`.  If its curling number exceeded the
prescribed binary value, the excess exponent would be at least three.
Its root length would consequently be strictly below `p`, and the same
power would raise the proper circular profile, a contradiction.  The
witness used in the first copy is still present, so the lower bound also
persists.  Hence, after `2p` common outputs, the two states are

```
high: R^3,
low:  R[d:p] R^2.                               (2)
```

The high value is three.  The low value is exactly two: it has the proper
phase-zero square witness, while any cube root would have length at most

```
(3p-d)/3<p
```

and would contradict the circular value `R[0]=2`.

After the low state in (2) appends this `2=R[0]`, the same
length-below-`3p` argument forces the next `d-1` values to be
`R[1:d]`.  It reaches

```
R[d:p] R^2 R[0:d]
    = (R[d:p]R[0:d])^3
    = R_(j+d)^3.                                 (3)
```

Since the orbit from the shorter seed `Q` terminates, the state in (3)
terminates.  The replay hypothesis says that the rotation `R_(j+d)`
reaches exactly this state, so that rotation terminates as well.

Therefore, if `C` is the set of phases whose rotations are shortest
counterexamples,

```
j in C and 1<=d<=D(j)  implies  j+d mod p not in C.   (4)
```

The one-symbol deletion normal form independently gives `j+1 not in C`
even when `D(j)=0`.  It also gives `C` only at phases carrying the symbol
two.

## 3. Exact limitation of the rotation argument

Condition (1) is load-bearing.  A general proper suffix need not follow
the circular replay until the cube.  For the executed length-21 fixed
profile, at phase zero the exact radius is `D(0)=11`.  Deletions
`1,...,11` first differ only at the cube, with values `3` versus `2`.
Deletion `12` first differs after two outputs, again `3` versus `2`, and
deletion `14` differs immediately, with values `2` versus `1`.

For that profile the radii at the fifteen symbol-two phases range from
seven to thirteen.  Applying only the exclusions (4) permits a set `C`
of size two; examples of permitted phase pairs are `{7,15}`, `{7,17}`,
and `{7,18}`.  Thus terminating suffixes impose substantial sparsity on
counterexample rotations but do not, by themselves, force `C` to be
empty.  A complete rotation proof needs an additional transition law for
the post-promotion orbit or a stronger reason that the remaining isolated
phases terminate.
