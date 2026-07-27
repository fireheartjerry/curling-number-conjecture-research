# Minimum hitting time for a one-symbol defect (blocked normalization)

This note records an attempted second dynamical normalization following
`research/immediate_power_coupling.md`.  The unrestricted minimization
in Section 2 is vacuous for the reason in Section 2.1.  Therefore the
general Hamming-one route is blocked.  Only the provenance-rich adjacent
completion pair in Section 1 remains useful.

## 1. Existence of a bad/terminating one-defect pair

The minimum-deleted-hitting-time normal form supplies

```
A=Y^k                         bad,
L=A[1:]                       terminating,
cn(A)=k,       cn(L)=k-1.
```

The actual high successor

```
H=A k
```

is bad.  The wrong successor

```
W=A (k-1)
```

terminates.  Indeed,

```
W[1:]=L (k-1)
```

is the actual next state on the terminating orbit from `L`, so its
first-one hitting time is `tau(L)-1`.  If `W` were bad, it would be a
bad word with terminating first deletion of hitting time below the
minimum used to select `A`.

Thus `H,W` are equal-length words which differ in exactly one position,
their last position, with one bad and the other terminating.

## 2. Hamming-one hitting-time selection

Let `D` be the class of ordered pairs `(P,Q)` such that

* `P` and `Q` have the same positive length;
* they differ in exactly one coordinate;
* `P` is bad;
* `Q` reaches curling number one.

Section 1 proves that `D` is nonempty.  Choose `(P,Q)` in `D` minimizing
`tau(Q)`.

### 2.1 Fatal degeneracy of this selection

The minimum is always zero and carries no information.  Given any bad
word `P`, replace its final symbol by an integer `z` which occurs nowhere
else in `P`.  The resulting Hamming neighbor `Q` has curling number one:
any powered suffix of exponent at least two would have to contain an
earlier copy of its final symbol `z`.  Thus `tau(Q)=0`.

Consequently the construction below may specialize merely to

```
P cn(P)   bad,       P 1   terminating,
```

which is true for every bad `P` and supplies no new structure.  The
selection cannot be used as a global rank unless one preserves extra
provenance, such as the adjacent labels `k,k-1` arising from the strict
first-deletion split in Section 1.

### Lemma 1

```
cn(P) != cn(Q).                                  (1)
```

### Proof

Suppose both values equal `c`.  Since `P` is bad, `c>=2`; hence
`tau(Q)>0`.  The successors

```
P'=P c,       Q'=Q c
```

still differ in exactly the original coordinate.  The first is a state
on the bad orbit of `P`, while the second is the actual next state on
the terminating orbit of `Q`, with

```
tau(Q')=tau(Q)-1.
```

This gives an element of `D` with smaller terminating hitting time,
contradicting the selection.

## 3. Relocating the defect to the final position

Put

```
h=cn(P),        ell=cn(Q).
```

By Lemma 1, `h!=ell`.  The actual successor

```
P h
```

is bad.  The wrong successor

```
P ell
```

must terminate.

To prove the second assertion, observe that

```
Q ell
```

is the actual next state on the terminating orbit from `Q`, with hitting
time `tau(Q)-1`.  The words

```
P ell,       Q ell
```

still differ in exactly the old coordinate.  If `P ell` were bad, they
would contradict the minimum choice in Section 2.

Consequently

```
P h       bad,
P ell     terminating,                           (2)
```

and these two words differ only in their final symbol.  This turns an
arbitrarily located one-symbol context defect into a co-terminal
completion defect.

## 4. Root-scale separation at the relocated defect

Suppose the two words in (2) have curling numbers at least two after the
displayed completions.  Choose primitive maximizing roots of lengths
`p,q` and exponents `u,v`:

```
P h ends in U^u,       |U|=p,
P ell ends in V^v,     |V|=q.
```

The root lengths are unequal.  Equal lengths would force both distinct
last symbols `h,ell` to equal the same copied position in the common
prefix `P`.

Put `g=gcd(p,q)`.  Deleting the final symbols leaves two co-terminal
periodic suffixes in the common word `P`.  Fine--Wilf gives the exact
separation:

```
p<q  =>  (u-1)p+g<=q,
q<p  =>  (v-1)q+g<=p.                             (3)
```

For example, in the first orientation the `q`-periodic shadow has length
at least `2q-1`, which reaches the Fine--Wilf threshold.  If the
`p`-periodic shadow also reached that threshold, the common suffix would
give period `g<q` to a complete conjugate of the primitive length-`q`
root.  Threshold failure is the first inequality in (3).  The other
orientation is symmetric.

If the terminating completion in (2) already has curling number one,
there is no second power root to compare; it is an immediate reset
instead.

## 5. Remaining gap

The formal implications in Sections 2--4 are valid, but Section 2.1
shows that their hypotheses can be achieved in a trivial way and hence
do not advance the conjecture.  This route is marked blocked.

The nontrivial object that survives is the adjacent completion pair

```
A k       bad,
A (k-1)  terminating,
```

with `A=Y^k`, supplied by Section 1.  Any continuation must retain that
adjacency and shared pure-power provenance.  Forgetting either datum
collapses back to the fresh-marker degeneracy above.
