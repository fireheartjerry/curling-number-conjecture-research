# Power-root separation across an adjacent transposition

This note isolates the word lemma used by the residual `32/23` branch of
`contained_completion_commutative_square.md`.  No specialized theorem for
this exact co-terminal geometry was located in the literature search
recorded in `literature_search_log.md`; the proof is a direct
Fine--Wilf application.

## Lemma 1

Let `P` be a finite word and let `a!=b`.  Suppose

```
Pab ends in U^u,       |U|=p,       u>=2,
Pba ends in V^v,       |V|=q,       v>=2,
```

where `U,V` are primitive.  Then

```
p!=q.                                                   (1)
```

Put `g=gcd(p,q)`.  The two possible scale orientations satisfy

```
p<q  =>  (u-1)p+g<=q+1,                                (2a)
q<p  =>  (v-1)q+g<=p+1.                                (2b)
```

### Proof

First suppose `p=q`.  If `p=1`, the final root-one square in `Pab`
forces `a=b`, a contradiction.  If `p>=2`, the final symbol of each
powered suffix is copied from exactly `p` positions earlier.  Those two
source positions are the same position of the common prefix `P`, while
the required copied symbols are respectively `b` and `a`.  This again
forces `a=b`.  Hence (1) holds.

Delete the last two symbols from both words.  The remaining common word
`P` has co-terminal periodic suffixes of lengths

```
up-2       with period p,
vq-2       with period q.                              (3)
```

Assume `p<q`.  The `q`-periodic suffix reaches the Fine--Wilf threshold:

```
vq-2 >= 2q-2 >= p+q-g,
```

because `q-p+g>=2`.  If the `p`-periodic suffix also reached that
threshold, their common co-terminal factor would have period `g`.  Its
length is at least `q`, so it contains a complete conjugate of the
primitive length-`q` root and gives that conjugate the proper period
`g<q`, a contradiction.  Therefore

```
up-2<p+q-g.
```

The integral rearrangement is (2a).  Interchanging the two powered words
proves (2b).

## Corollary 2 (the delayed curling defect)

In the `u=2` branch of the contained completion square, suppose

```
D32 is bad,               D23 is terminal.
```

The bad word has curling number at least two.  If `cn(D23)=1`, the
terminal branch has already reached its first one at this state.  If
`cn(D23)>=2`, choose primitive maximizing roots on both sides.  Their
lengths are unequal and obey (2a) or (2b).

The additive one in those inequalities is real: deleting a two-symbol
transposition leaves periodic shadows two symbols shorter, rather than
the one-symbol shadows in the ordinary completion lemma.  The scale
orientation can point either way, so Lemma 1 alone is not a
well-founded descent.

## Corollary 3 (a following high forces containment)

Retain the contained-completion notation

```
C=2R,       |C|=n,
D=(C^3)[1:],
Q=R2,
B=D2=Q^3,
```

and the residual bad/terminal pair

```
D32 is bad,               D23=B3 is terminal.       (4)
```

If

```
C[1]=Q[0]=3,                                      (5)
```

then every primitive maximizing root of the bad word `D32` has length
`p<n`.  If its exponent is `u`, then

```
(u-1)p+gcd(p,n)<=n+1.                             (6)
```

### Proof

Under (5),

```
B3=Q^3 Q[:1].
```

Its final length `3n` is the cube of the one-step rotation of `Q`, so
the terminal word in (4) has a displayed primitive cube root of length
`n`.  Apply Lemma 1 to a primitive maximizing `u`-root of length `p` on
the bad side and this primitive exponent-three root on the terminal
side.

Equality `p=n` is excluded by (1).  If `p>n`, equation (2b), with the
length-`n` root as the smaller root, gives

```
2n+gcd(p,n)<=p+1,
```

and hence `p>=2n`.  But

```
p<=|D32|/u<=(3n+1)/2<2n
```

for `n>=2`, a contradiction.  Thus `p<n`, and (2a) is exactly (6).

Consequently only the adjacent-low case `C[1]=2` can evade a contained
bad root after the delayed transposition.  Containment of the root still
does not imply inheritance of bad status by its pure power.
