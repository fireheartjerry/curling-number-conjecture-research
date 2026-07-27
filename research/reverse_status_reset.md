# Reverse-status resets forced by a terminating superword

This note is conditional on the existence of a bad word.  It records the
normal form obtained when a *terminal* left extension contains a *bad*
suffix.  The direction is the reverse of the minimum-deleted-hitting-time
reset.  In fact every bad word has a one-step-terminal power superword, so
the reverse-status pair below does not require a restart-cycle hypothesis.

## 1. Literature boundary

CLSW Section 4.3 studies rotten terminal words: prefixing a terminal binary
word may lower its finite tail length.  Conjecture 22 asserts that no binary
word is doubly rotten.  Those statements compare three *finite* hitting
times and do not treat a terminal prefix extension of a nonterminating
suffix.  Searches for `curling number prefixing nonterminating sequence`,
`rotten sequence bad suffix`, `doubly rotten curling number`, and `prefix
extension termination curling number` found no published reverse-status
normal form.

## 2. Every bad word lies below a one-step-terminal power

### Lemma 0 (power-superword cure)

If `W` is bad, there is an integer `q>=2` such that

```
T=W^q,                 tau(T)=1,
```

and `W` is a suffix of `T`.

### Proof

Let `M` be the largest positive symbol occurring in `W`, taking `M=1` if
there is no positive symbol, and choose `q>M`.  The displayed suffix
factorization `T=W^q` gives

```
cn(T)>=q>M.
```

Put `c=cn(T)`.  Every symbol of `T` occurs already in `W`, so the positive
integer `c` is absent from `T`.  After appending `c`, its final occurrence
is unique.  A suffix power of exponent at least two would contain an
occurrence of `c` at the end of each of its final two root copies, which is
impossible.  Hence `cn(T c)=1`.  Since `cn(T)>=q>=2`, the first curling
number one occurs after exactly one append, and `tau(T)=1`.

This construction does not assert that a suffix of `T` has hitting time at
most one; Section 5 records an explicit failure of that inference.

## 3. An adjacent reverse-status pair

Call a word bad when its autonomous orbit never has curling number one,
and terminal otherwise.  Suppose a terminal word `T` has a bad suffix
`W`.  Delete the symbols of the prefix `T[:-|W|]` one at a time.  The
initial word in this finite chain is terminal and the final word is bad,
so at some adjacent pair there are a symbol `a` and a word `B` such that

```
A=aB is terminal,              B is bad.          (1)
```

Among every pair satisfying (1), choose one minimizing `tau(A)`.

### Lemma 1 (reverse whole-power reset)

There are a primitive word `Y` and an integer `k>=3` such that

```
A=Y^k,
cn(A)=k,
cn(B)=k-1.                                        (2)
```

### Proof

The suffix relation gives `cn(A)>=cn(B)>=2`, so `tau(A)>0`.  If the two
curling numbers were equal to `c`, their successors would be

```
A c = a (B c),              B c.
```

The first word is terminal with hitting time `tau(A)-1`; the second is bad
because it is the actual successor of `B`.  This is another pair of the
form (1) with a smaller terminal hitting time, contrary to the choice of
`A`.

Deleting one initial symbol can lower the curling number by at most one.
Hence the strict inequality has the form

```
cn(A)=cn(B)+1=k.
```

Let `A=X Y^k` be a maximizing factorization.  If `X` were nonempty, the
same suffix `Y^k` would remain after deleting the first symbol, giving
`cn(B)>=k`.  Thus `X` is empty and `A=Y^k`.  If `Y=Z^e` for `e>=2`, then
`A=Z^(ek)` would have curling number at least `ek>k`.  Therefore `Y` is
primitive.  Since `B` is bad, `cn(B)=k-1>=2`, so `k>=3`.

## 4. The driven high completion must terminate

### Lemma 2 (adjacent completion fork)

With the notation of Lemma 1,

```
B (k-1) is bad,              B k is terminal.      (3)
```

### Proof

The first word in (3) is the actual successor of the bad word `B`, so it
is bad.  The actual successor `A k` of the terminal word `A` has hitting
time `tau(A)-1`, and its first-symbol deletion is `B k`.  If `B k` were
bad, the pair

```
A k = a (B k),              B k
```

would satisfy (1) with a smaller terminal hitting time.  This contradicts
the minimal choice.  Hence `B k` is terminal.

The reset therefore creates two adjacent last-symbol completions of one
common prefix with opposite status:

```
B (k-1)       bad,
B k           terminal.                            (4)
```

This is not the fresh-marker degeneracy of an unrestricted Hamming-one
selection: both final symbols are forced consecutive curling values and
come from the primitive whole-power split (2).

## 5. Exact root separation at the fork

Put

```
u=cn(B (k-1)),             v=cn(B k).
```

Appending one symbol can raise a curling number by at most one, even when
the appended symbol is not the current curling number.  To verify this,
if `Sx` ends in `R^e`, deleting `x` leaves a periodic suffix whose final
`(e-1)|R|` symbols are `e-1` copies of a conjugate of `R`.  Hence
`cn(S)>=e-1`.  Thus

```
2<=u<=k,                   1<=v<=k.                (5)
```

If `v=1`, the terminal branch dies at the fork.  Suppose `v>=2`, and
choose primitive maximizing roots of lengths `p,q` and exponents `u,v`
in `B(k-1)` and `Bk`, respectively.  Then `p!=q`: equal root lengths
would copy the same position of the common prefix `B` to the two distinct
last symbols.

Writing `g=gcd(p,q)`, deletion of the last symbol leaves co-terminal
periodic shadows in `B`.  Fine--Wilf gives the exhaustive separation

```
p<q  implies  (u-1)p+g<=q,
q<p  implies  (v-1)q+g<=p.                         (6)
```

For the first implication, failure of the displayed inequality makes the
overlap of the two shadows meet the threshold `p+q-g`; the overlap
contains a complete conjugate of the primitive length-`q` root, and period
`g<q` contradicts its primitivity.  The second implication exchanges the
two completions.

Equations (2)--(6) are the complete local reverse-reset normal form.  They
do not yet contradict the bad branch: the root-scale alternative (6) can
alternate direction.  A completion must couple this reverse reset to the
ordinary bad/terminal reset or prove that repeated adjacent forks carry a
well-founded rank.

## 6. One-step terminal superwords do not transfer their hitting time

The same-rank restart-cycle lemma constructs, for arbitrarily large `q`,
a terminal superword `T_q` containing the bad reset window as a suffix and
satisfying `tau(T_q)=1`.  This does **not** imply that the adjacent
reverse-status pair found while deleting the prefix of `T_q` has terminal
hitting time one.  Tail length is not monotone under suffix deletion.

The executed finite warning is

```
T=32323232,       tau(T)=1,
T[1:]=2323232,    tau(T[1:])=2,
T[2:]=323232,     tau(T[2:])=3.
```

Every displayed value was recomputed by both curling-number
implementations after the A094004 calibration.  The example is not a bad
word; it isolates the invalid inference from the hitting time of a
superword to the hitting time at an internal status boundary.

Consequently the additional condition

```
tau(A)=1                                           (7)
```

is only a conditional specialization.  Under (7), the actual successor
`A k` has curling number one.  Its suffix `B k` can have no larger curling
number, so

```
cn(A k)=cn(B k)=1,           B(k-1) is bad.         (8)
```

In particular the last symbol of `Y` is not `k`; otherwise `A k=Y^k k`
would end in the square `k k`, contradicting (8).  No current argument
derives (7) from a restart cycle or from the existence of a bad word.

## 7. Conditional rotation, descent, or the sole external square

Retain (7)--(8), put `p=|Y|`, and let

```
F=B(k-1),                 u=cn(F)>=2.
```

Choose a primitive maximizing `u`-root of length `q` in `F`, and put
`g=gcd(p,q)`.

If `q=p`, the final symbol must be the period-`p` continuation of
`B=Y[1:]Y^(k-1)`, namely `Y[0]`.  Thus

```
Y[0]=k-1,                 F=rot_left(Y)^k.          (9)
```

If `q!=p`, delete the final symbol of `F`.  The common word `B` has a
terminal period-`p` suffix of length `(k-1)p` and a terminal period-`q`
suffix of length `u q-1`.  Fine--Wilf and primitivity force the exhaustive
split

```
q>(k-2)p+g,
or
(u-1)q+g<=p.                                      (10)
```

To prove (10), their overlap has length

```
min((k-1)p, u q-1).
```

If this reached `p+q-g`, it would contain a complete conjugate of each
primitive root and would give one of them the proper period `g`.  Therefore
the minimum is below the threshold.  If its first argument is the minimum,
integer rearrangement gives the first alternative; if its second argument
is the minimum, integer rearrangement gives the second.

The complete `u`-power fits in `F`, whose length is `kp`, so

```
q<=kp/u<=kp/2.                                     (11)
```

For `k>=4`, the first alternative of (10) contradicts (11), because
`(k-2)p>=kp/2`.  The root therefore strictly descends and satisfies the
second alternative.  For `k=3`, a first-alternative root must have `u=2`;
otherwise (11) gives `q<=p`.  Hence the sole external case is

```
k=3,             u=2,             p+g<q<=3p/2.    (12)
```

Thus the one-step reverse reset has exactly three continuations: the
same-scale bad rotation (9), a strict root descent, or the cubic external
square (12).  Closing those continuations remains a global task; equations
(9)--(12) prevent an unrestricted root-scale alternation at every
`k>=4` reverse reset.
