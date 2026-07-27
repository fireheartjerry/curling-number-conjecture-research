# Arbitrary-alphabet rotation-cube status theorem

This note removes the binary-alphabet hypothesis from the status theorem in
`rotation_cube_status_cycle.md`.  A word is **bad** when its orbit never has
curling number one, and **terminal** otherwise.

## 1. Literature boundary

The literature was searched before the derivation for:

* arbitrary-alphabet curling-number prefix and deletion theorems;
* curling numbers of rotations and conjugate powers;
* primitive-word powers after deleting one letter;
* everywhere cube-repetitive periodic words;
* the exact overlap equation arising from a square reset.

The reusable published inputs are:

1. Chaffin--Linderman--Sloane--Wilks, *On Curling Numbers of Integer
   Sequences*, Journal of Integer Sequences 16 (2013), Article 13.4.3,
   Theorem 7: prefixing one term changes a curling number by zero or one.
   The proof does not depend on the value of the prefixed term or on a binary
   alphabet.
2. Fine--Wilf, *Uniqueness theorems for periodic functions*, Proceedings of
   the AMS 16 (1965), 109--114: a word of length at least
   `p+q-gcd(p,q)` with periods `p,q` has period `gcd(p,q)`.
3. Kalle Saari, *On the Frequency and Periodicity of Infinite Words*,
   PhD dissertation, TUCS Dissertations 83 (2008), Theorem 5.3:
   every everywhere `(phi+1)`-repetitive sequence is ultimately periodic.
   The corresponding journal paper is *Everywhere alpha-repetitive
   sequences and Sturmian words*, European Journal of Combinatorics 31
   (2010), 177--192, DOI `10.1016/j.ejc.2009.01.004`.

No located source states the rotation-status theorem proved below.  The
claim is therefore recorded only as not found in the searched literature.

## 2. Setup

Let `P` be a primitive word of length `n` with exact proper circular
curling profile

```
pc_P(j)=P[j]>=2
```

at every phase, and assume `min(P)=2`.  Thus the alphabet of `P` consists
of positive integers.  At a phase labelled at least three one necessarily
has `n>=2`.

For indices modulo `n`, put

```
Q_j=P[j:]P[:j],
A_j=Q_j^3,
D_j=A_j[1:],
a_j=P[j].
```

Let `f_j` be the bad/terminal status of `A_j`.

Every proper powered suffix of a primitive period-`n` word whose root has
length `q<n` has powered length

```
L<n+q-gcd(n,q)<2n.                                (1)
```

Otherwise Fine--Wilf gives a period `gcd(n,q)<n` to a complete conjugate
of `P`, contradicting primitivity.

## 3. Exact cubes and deletions

### Lemma 1

If `a=a_j>=3`, then

```
cn(A_j)=a,
cn(D_j)=a,
D_j a=A_(j+1).                                   (2)
```

Consequently

```
f_j=status(a A_(j+1)),
status(D_j)=f_(j+1).                              (3)
```

### Proof

The word `A_j` ends in the displayed cube of root length `n`.  By (1),
its last `2n` terms also contain every proper circular powered suffix at
this phase, whose maximum exponent is `a`.  A maximizing primitive root
longer than `n` is impossible: its square has length at least twice its
root length, so Fine--Wilf with ambient period `n` gives that root the
proper period `gcd(n,q)`.  Thus

```
cn(A_j)=max(3,a)=a.
```

The length of `D_j` is `3n-1`, so (1) shows that it contains a proper
`a`-power and `cn(D_j)>=a`.  If `cn(D_j)=e>a`, a primitive maximizing
root has length

```
q<3n/(a+1)<=3n/4<n.
```

It would be a proper circular `e`-power at this phase, contradicting
`pc_P(j)=a`.  Hence `cn(D_j)=a`.

Write `Q_j=aR`.  Direct concatenation gives

```
D_j a=R(aR)(aR)a=(Ra)^3=A_(j+1),
A_j a=a(Ra)^3=a A_(j+1).
```

The exact curling numbers in (2) make these the first orbit steps and
prove (3).

## 4. Periodic-prefix formula and initial coupling

### Lemma 2

Let `Q` be any primitive word of length `n`.  For `j>=2` and
`0<=t<n`,

```
cn(Q^j Q[:t])=max(j,pc_Q(t)).                     (4)
```

### Proof

The suffix of length `jn` is `j` copies of the rotation of `Q` at phase
`t`.  Roots shorter than `n` have maximum exponent `pc_Q(t)` and, by
(1), are visible in the finite word.  A primitive maximizing root
longer than `n` is excluded by the Fine--Wilf argument in Lemma 1.  A
root of length `n` has exactly the displayed exponent `j`.  These cases
are disjoint and exhaustive, proving (4).

Fix a phase `j` with `a_j=a>=3`, and write

```
Q_(j+1)=R a,
C=aR,
E=a Q_(j+1)^3=C^3 a,
F=Q_(j+1)^3,
m=|E|=3n+1,
b=Q_(j+1)[0]=C[1],
c=max(3,b).                                      (5)
```

Equation (4) gives `cn(F)=c`.  The universal one-letter prefix
classification in `rotation_cube_status_cycle.md`, Lemma 2, with empty
tail shows that `cn(E)=cn(F)`: its locked alternative would require an
empty word of length `(k-3)n-1`, and its external alternative would give
a root longer than `2n` inside a word of length `3n+1` and exponent at
least four.  Therefore

```
cn(E)=cn(F)=c.                                    (6)
```

## 5. First mismatch

Suppose `E` and `F` have different statuses.  Their exact values in (6)
make them append a common word until a first pair with unequal curling
numbers.  Write that pair as

```
U=E G,
V=F G=U[1:].
```

The universal prefix classification gives a primitive word `Y`, with
`r=|Y|`, and an integer `k` such that

```
U=Y^k,
cn(U)=k,
cn(V)=k-1,
Y[0]=a,                                           (7)
```

and exactly one of

```
locked:
  r=n, k>=4, G=R C^(k-4);

external:
  r>2n+gcd(n,r).                                  (8)
```

### Lemma 3 (the locked case cannot be an orbit mismatch)

Under the hypotheses above, the locked alternative in (8) is
impossible.

### Proof

The locked common output `G` begins with the complete word `R=Q_(j+1)[:-1]`.
Rotation invariance gives
`pc_(Q_(j+1))(t)=Q_(j+1)[t]`.  For `0<=t<n-1`, Lemma 2 therefore gives

```
cn(Q_(j+1)^3 Q_(j+1)[:t])
  =max(3,Q_(j+1)[t]).
```

The minimum symbol of `P` is two, while the omitted last symbol of
`Q_(j+1)` is `a>=3`.  Hence some position `u<n-1` of `R` equals two.
If the orbit had appended `R[:u]`, its next value would be three by the
displayed formula, whereas the locked word requires the next output to
be `R[u]=2`.  This contradicts that `G` is the actual common orbit
output.

### Lemma 4 (external replay creates a forbidden high-minimum profile)

The external alternative in (8) is impossible when `k>=3`.

### Proof

Put `g=gcd(n,r)`.  The strict external inequality gives

```
r>2n+g,
m=3n+1<2r.                                       (9)
```

Since `k>=3`, `(k-1)r>=2r>m`.  Before the first mismatch, the paired
states therefore pass through

```
T=Y^(k-1),       T[1:].
```

The displayed power gives `cn(T)>=k-1`.  The same `T` is a suffix of
`V`, whose exact curling number is `k-1`; hence `cn(T)=k-1`.  The next
common output is the next symbol of `Y^k`, namely `Y[0]=a`.  Thus

```
k-1=a,           k=a+1.                          (10)
```

For every `0<=t<r`, all of the following cuts occur strictly after the
initial length `m` and strictly before the mismatch:

```
H_t=Y^(a-1)Y[:t],
J_t=Y^a Y[:t].
```

Indeed `a>=3`, so (9) gives `|H_t|>=2r>m`, and
`|J_t|<(a+1)r=|U|`.  Since the actual common output spells the
remaining prefix of `Y^k`,

```
cn(H_t)=cn(J_t)=Y[t].                             (11)
```

The word `J_t` ends in `a` copies of the rotation of `Y` at phase `t`.
Therefore (11) gives

```
Y[t]>=a.                                         (12)
```

Choose a maximizing root in `H_t`.  From (11)--(12), its length `q`
satisfies

```
q<=((a-1)r+t)/Y[t]
 <=(ar-1)/a<r.                                   (13)
```

Thus it is a proper circular root and proves `pc_Y(t)>=Y[t]`.

Conversely, the Fine--Wilf bound (1), with `r` in place of `n`, says
that every proper circular powered suffix of primitive `Y` has length
strictly below `2r`.  Such a suffix is visible in `H_t`, whose length is
at least `2r`.  Equation (11) consequently gives
`pc_Y(t)<=Y[t]`.  Hence

```
pc_Y=Y,          min(Y)>=a>=3.                   (14)
```

It remains to recall why (14) is impossible.  If a primitive word `W`
has `pc_W=W` and minimum at least three, every cut of `W^Z` ends in a
cube with root shorter than `|W|`.  Reversing gives an everywhere
`(phi+1)`-repetitive sequence, since `3>phi+1`.  Saari's Theorem 5.3
makes it ultimately periodic.  In Saari's proof the resulting period is
the least period of a minimal local repetition; here it is shorter than
`|W|`, because each local cube already has such a shorter period.  An
eventual period of the purely `|W|`-periodic word is global, contradicting
the primitivity of `W`.  Applying this to `Y` contradicts (14).

## 6. Arbitrary-alphabet status theorem

### Theorem 5 (no terminal-to-bad transition at a label at least three)

For every phase with `a_j>=3`,

```
not (f_j=terminal and f_(j+1)=bad).               (15)
```

### Proof

Assume the excluded orientation.  At the first mismatch (7), `V` is on
a bad orbit, so `cn(V)=k-1>=2` and `k>=3`.  Lemma 3 excludes the locked
case and Lemma 4 excludes the external case.  The two alternatives in
(8) are exhaustive, giving a contradiction.

This proof does not require a bounded alphabet, a maximum-symbol
argument, or a singleton-run hypothesis.

## 7. Exclusion of the opposite transition

### Theorem 6 (no bad-to-terminal transition at a label at least three)

Suppose `a_j=a>=3` and

```
f_j=bad,
f_(j+1)=terminal.                                 (16)
```

Then a contradiction follows.

### Proof

Lemmas 3--4 exclude every first mismatch with `k>=3`.  Since unequal
curling numbers are positive, (7) leaves exactly

```
k=2,  U=Y^2,  V=U[1:],  cn(V)=1.                (17)
```

The remaining prefix-classification alternative is external.

If `r>=m`, the replay argument at the single-copy cut `Y` gives
`cn(Y)=1` from suffix maximality in `V`, while the next common output is
`Y[0]=a`; this would give `a=1`.  Hence `r<m`.

Put `s=r-2n`.  The external inequality gives

```
s>gcd(n,r)=gcd(n,s)>=1,
```

so `s>=2`.  The inequality `r<m=3n+1` gives `s<=n`; equality `s=n`
would violate `s>gcd(n,s)`.  Thus

```
0<s<n.                                            (18)
```

The first `r=2n+s` symbols of `E=C^3 a` form

```
Y=C^2 C[:s].
```

Put

```
A=C[:s],  B=C[s:].
```

Equation (18) makes both `A` and `B` nonempty.  Since `C=AB`,

```
Y=ABABA.
```

Its final `2n` symbols are

```
BABA=(BA)^2.                                      (19)
```

The deletion `V=(Y^2)[1:]` removes one symbol only from the first copy
of `Y`; its complete second copy remains a suffix.  Equation (19)
therefore supplies a square suffix of `V`, so `cn(V)>=2`.  This
contradicts `cn(V)=1` in (17), excluding (16).

### Corollary 7 (status-cycle location)

For every phase,

```
a_j>=3  implies  f_j=f_(j+1).                    (20)
```

Theorem 5 excludes the terminal-to-bad orientation and Theorem 6
excludes the bad-to-terminal orientation.  Hence every status boundary
in the cyclic list of rotation cubes occurs at a phase labelled two.

## 8. Consequence for the status route

There is no residual status seam at a phase labelled at least three.
Any nonconstant cyclic status assignment must change across at least two
phase labels equal to two.  A completion of the status route must now
analyze transitions at label two or show that the independent structure
of the fixed profile makes such a cyclic assignment impossible.
