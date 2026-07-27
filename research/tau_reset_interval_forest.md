# Tau-minimal deletion pairs and whole-prefix reset intervals

This note is conditional on the existence of a nonterminating curling
orbit.  It separates two reductions:

1. a purely dynamical reduction to an immediate first-symbol deletion
   mismatch;
2. the interval geometry of repeated mismatches along one fixed
   nonterminating orbit.

It does not prove that the resulting reset tower is finite.

## 1. Tau-minimality forces immediate divergence

Let

```
C={A : the orbit of A is nonterminating and the orbit of A[1:] terminates}.
```

The set is nonempty after choosing a nonterminating seed of minimum
length.  For `A in C`, let `tau(A)` be the first time at which the
outputs of `A` and `A[1:]` differ.

### Lemma 1

There is an `A in C` with `tau(A)=0`.

### Proof

The terminating deleted orbit eventually outputs `1`, while the
nonterminating orbit never does, so `tau(A)` is finite.  Choose `A` with
minimum `tau(A)`.  If the first outputs agree and equal `c`, replace the
pair by

```
A c,          A[1:] c=(A c)[1:].
```

The first word remains on the nonterminating orbit, the second remains on
the terminating orbit, and the divergence delay decreases by one.  This
contradicts minimality unless `tau(A)=0`.

## 2. Exact pure-power form at the immediate mismatch

Write `A=aB`, and put

```
k=cn(A),          ell=cn(B).
```

### Lemma 2

At a tau-zero pair there is a primitive nonempty word `Y` such that

```
A=Y^k,
B=Y[1:]Y^(k-1),
ell=k-1.                                             (1)
```

Moreover,

```
cn(Y^(k-1))=k-1,
cn(Y)<=k-1,                                         (2)
```

and every proper suffix of `Y^k` has curling number at most `k-1`.

### Proof

Every powered suffix of `B` is a powered suffix of `A`, so `k>=ell`.
The outputs differ, hence `k>ell`.

Choose a maximizing root of `A`, of length `r`.  If its powered span
`kr` were at most `|B|`, it would also be a suffix power of `B`,
contrary to `ell<k`.  The state lengths differ by one, so

```
kr=|A|.
```

Thus the maximizing power is all of `A`; call its root `Y`.  Deleting
the first symbol gives the second equation in (1).  This word ends in
`Y^(k-1)`, so `ell>=k-1`.  Together with `ell<k`, this gives
`ell=k-1`.

If `Y` were a nontrivial power, `Y^k` would have exponent strictly above
`k`, contradicting the definition of `k`.  Thus `Y` is primitive.

The suffix `Y^(k-1)` has curling number at least `k-1` from its displayed
power and at most `cn(B)=k-1` by suffix monotonicity.  This proves the
first assertion in (2); its suffix `Y` gives the second.  Finally every
proper suffix of `Y^k` is a suffix of the longest proper suffix `B`, so
its curling number is at most `cn(B)=k-1`.

### Corollary 3 (the exact terminal-square branch)

If `k=2`, then

```
cn(Y)=cn(Y[1:]Y)=1,
Y is primitive and robust,
Y^2 is a nonterminating state with cn(Y^2)=2.        (3)
```

Here robust has the definition of Chaffin--Linderman--Sloane--Wilks:
no proper suffix of `Y^2` has curling number at least two.

### Proof

Equation (2) gives `cn(Y)=1`, while (1) gives
`cn(Y[1:]Y)=1`.  The latter is the longest proper suffix of `Y^2`, so
every proper suffix has curling number one.  This is exactly robustness
for a primitive word of curling number one.  The remaining assertions
are inherited from the tau-zero pair.

The general statement in Lemma 2 is the structural case counted in the
proof of Theorem 8 of Chaffin--Linderman--Sloane--Wilks, *On Curling
Numbers of Integer Sequences*: a one-symbol deletion drop at value `k`
forces a primitive whole power `Y^k`, and the longest proper suffix has
value `k-1`.  Their Theorem 7 is the one-symbol inequality used below.

## 3. Driven deletion along the high orbit

Let `T` be the one-sided word formed by a fixed nonterminating seed and
its orbit outputs.  At a generated cut `t`, put

```
H_t=T[:t],
B_t=H_t[1:],
h_t=cn(H_t),
b_t=cn(B_t).
```

Prefixing one symbol raises a curling number by at most one.  The proof
of CLSW Theorem 7 does not depend on that symbol being `2` or `3`, so

```
h_t in {b_t,b_t+1}.                                  (4)
```

If equality holds, then

```
B_(t+1)=B_t h_t
```

is the actual next state of the autonomous orbit of `B_t`.  If the
second value in (4) holds, call `t` a reset.

### Lemma 4 (every reset is a whole-prefix power)

At a reset there is a primitive word `U_t`, of length `p_t`, such that

```
H_t=U_t^(h_t),
b_t=h_t-1,
t=h_t p_t.                                         (5)
```

### Proof

Apply the proof of Lemma 2 to the pair `H_t,B_t`; termination is not
used in that word-equation argument.

Consequently, while `B_t` is known to terminate, equal steps in (4)
lower its remaining tail length by one.  Before that autonomous tail
can output `1`, either the high orbit would also output `1`, or another
reset occurs.  The unresolved event is that the incorrectly driven word
`B_t h_t` after a reset need not remain terminating.

## 4. Scale separation for nested reset intervals

Let two reset cuts `N_i<N_j` have

```
T[:N_i]=U_i^(k_i),      |U_i|=p_i,
T[:N_j]=U_j^(k_j),      |U_j|=p_j.                (6)
```

### Lemma 5

Either the reset roots have the same length, in which case

```
p_j=p_i,             U_j=U_i,             k_j>k_i,       (7a)
```

or they have unequal lengths and satisfy

```
p_j>p_i,
p_j>(k_i-1)p_i+gcd(p_i,p_j).                       (7b)
```

In particular, an unequal-root reset following an exponent at least
three has root length greater than twice the old root length.

### Proof

The common prefix `T[:N_i]` has periods `p_i` and `p_j`.

If `p_j<p_i`, its length `N_i=k_i p_i>=2p_i` reaches the Fine--Wilf
threshold.  The resulting gcd period makes the primitive word `U_i`
imprimitive.  Hence `p_j>=p_i`.

Suppose `p_j=p_i`.  The two roots are the same word `U`, since both are
the length-`p_i` prefix of `T`.  The later endpoint condition gives
`k_jp_i>k_ip_i`, hence `k_j>k_i`.  This is (7a).

Now suppose `p_j!=p_i`.  The preceding paragraph gives `p_j>p_i`.

Put `g=gcd(p_i,p_j)`.  If

```
k_i p_i>=p_i+p_j-g,
```

Fine--Wilf gives period `g` to the common prefix.  When `g<p_i`, this
makes `U_i` imprimitive.  When `g=p_i`, the same inequality says the
prefix contains all of `U_j`, which then has the proper divisor period
`p_i`.  Both cases contradict primitivity.  Threshold failure is the
second inequality in (7b).

This is a fixed-origin interval forest: every reset power occupies
`[0,N_i)`.  Root length is a strict rank only along unequal-root reset
edges, and it grows there, so (7b) alone does not make the forest well
founded.  Same-root reset edges must be handled separately.

## 5. Hidden and visible transitions

Keep two unequal-root resets as in (6), and abbreviate

```
U=U_i,  p=p_i,  k=k_i,  V=U_j,  q=p_j.
```

### Lemma 6 (exact hidden-root normal form)

If the next root ends before the old reset endpoint, `q<kp`, then

```
q=(k-1)p+h,
0<h<p,
h is a period of U,
h>p/k,
V=U^(k-1)U[:h],
U[p-h]=k.                                          (8)
```

If `q>=kp`, the transition is visible: the new primitive root contains
the complete old reset power `U^k`.

### Proof

Lemma 5(7b) gives `q>(k-1)p`, so write `q=(k-1)p+h` with
`0<h<p`.  The word `U^k`, being a prefix of the `q`-periodic later
reset, has period `q`.  Comparing its prefix and suffix of length
`kp-q=p-h` gives

```
U[:p-h]=U[h:p],
```

which says that `h` is a period of `U`.  The first `q` symbols of
`U^k` give the displayed formula for `V`.

If `h<=p/k`, the final copy of `U` contains a suffix which is a
`k`-th power of its final length-`h` block.  This suffix also belongs
to

```
B_(N_i)=U[1:]U^(k-1),
```

contradicting its exact curling number `k-1`.  Hence `h>p/k`.

The actual output `k` at position `kp` lies inside the later
`q`-periodic reset.  Translation left by `q` identifies it with
position

```
kp-q=p-h
```

in the first copy of `U`, proving the last equation in (8).  The
visible alternative is the definition `q>=kp`.

### Corollary 7 (a hidden square reset exposes a half-scale low node)

For `k=2`, put

```
a=p-h,             0<a<p/2.
```

There are nonempty words `A,B` with

```
U=A B A,
V=A B A A B,
|A|=a,
B[0]=2.                                             (9)
```

The factor `A^2` ends at generated cut `p+a`, and its displayed next
symbol is `2`.  Therefore its exact curling number at that cut is two,
and `A` is primitive.

### Proof

Period `h=p-a` gives the border `A` of length `a`; because
`h>p/2`, the two border occurrences are disjoint and leave a nonempty
middle word `B`.  Formula (8) gives

```
V=U U[:h]=A B A A B.
```

The position `p-h=a` in `U` is the first position of `B`, so (8) gives
`B[0]=2`.  The central `A^2` ends after the first appended `A`, at cut
`p+a`, and is followed by that `B[0]`.

For every sufficiently large reset this cut lies beyond the finite
seed, so its displayed symbol is the actual curling number of the
prefix.  The square supplies the lower bound two and the orbit label
supplies the matching upper bound.  If `A` were a nontrivial power,
the same factor would have exponent at least four, a contradiction.

This is the interval-forest leverage in a hidden transition: growth of
the whole-prefix root creates an internal primitive low square at less
than half the old scale.  The local last-high lemma gives either a
contained cube below half of `|A|` or an explicit ascent crossing the
left edge of `A^2`.  It does not by itself exclude that ascent.

## 6. Long replay roots give a block of synchronized rotations

Return to the shortest-seed deletion construction.  Let the minimum seed
be `S=P[:n]`, and suppose its first-divergence replay root `P` has length
`p>n`.  Before the first divergence, the high and low orbit states at
every length `j` with `n<=j<p` are

```
P[:j],             P[1:j].
```

Hence

```
cn(P[:j])=cn(P[1:j])=P[j].                         (10)
```

Every tail phase `j>=n` therefore has a maximizing proper circular
witness whose powered span is at most `j-1`.

Assume the standard critical conclusion that `P` has its exact proper
circular profile and its original first-copy fitting witnesses.  For
`0<=ell<=p-n`, let

```
R_ell=P[p-ell:]P[:p-ell]
```

be the right rotation by `ell`.

### Lemma 8

Every `R_ell`, `0<=ell<=p-n`, satisfies the full first-copy fitting
condition at every phase.

### Proof

At a nonwrapped phase `j<ell` of `R_ell`, the corresponding phase of
`P` is `i=p-ell+j>=n`.  Equation (10) supplies a witness of powered
span at most

```
i-1=p-ell+j-1<=p+j-1.
```

At a wrapped phase `j>=ell`, the corresponding phase is `i=j-ell`.
The original fitting witness for `P` has span at most

```
p+i-1=p+j-ell-1<=p+j-1.
```

These ranges exhaust the phases of the rotation.

Thus the long-root branch supplies a contiguous block of
`p-n+1` critically fitted rotations, not just the one predecessor
rotation.  The statement does not use last-symbol minimum-seed
strictness.

## 7. Direct-limit caveat

An infinite all-terminal reset tower can make any one fixed copied defect
arbitrarily far from the finite seed: place the defect in the second or
third copy of a sufficiently later visible reset root.  Every finite
halving descendant then has enough left context to be first-copy fitting.
This removes a finite boundary mask.

It does not give a uniform fitting bound over all levels.  A sequence of
defects may choose new root lengths comparable to the current reset scale,
so the required left context can escape to infinity with the level.
Any direct-limit argument must therefore prove a uniform scale bound or
an internal compactness statement before applying a finite terminal-gadget
classification.  Pointwise eventual fitting is insufficient.

The exact survivors are now separated:

* same-root transitions increase the reset exponent while retaining the
  primitive root;
* visible transitions install a complete older reset power inside a
  strictly larger primitive root;
* hidden transitions satisfy (8), and at exponent two expose the
  half-scale low square (9).

Controlling same-root exponent increases and eliminating infinite
alternation between the two unequal-root mechanisms remain the
interval-forest gaps.
