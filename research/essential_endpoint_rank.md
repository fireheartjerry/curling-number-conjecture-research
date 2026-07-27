# The conserved endpoint rank for essential bad words

This note is conditional on the existence of a nonterminating curling
orbit.  It records a second normalization of the bad/terminating
one-symbol-deletion pair.  Unlike minimum deleted hitting time, it charges
an inward movement of the left boundary by its exact depth.

Call a finite word `W` **essential** when `W` is bad and `W[1:]`
terminates.  Write

```
tau_W=tau(W[1:]),
R(W)=|W|+tau_W.
```

The class of essential words is nonempty whenever a bad word exists: a
bad word of minimum length is essential.  Choose an essential `A`
minimizing `R(A)`, and, among the minimizers, choose one of maximum length.
Put

```
N=|A|,       tau_0=tau(A[1:]),       R_0=N+tau_0.
```

The maximum-length tie break exists because every minimizer has length at
most `R_0`.

## 1. Conservation forces immediate divergence

### Lemma 1

The curling numbers of `A` and `A[1:]` differ at their first cut.

### Proof

Suppose they agree and equal `c`.  Since `A` is bad, `c>=2`, so
`tau_0>0`.  Put `A'=A c`.  The word `A'` is the next state on the bad
orbit, while

```
A'[1:]=A[1:] c
```

is the next state on the terminating deleted orbit.  Hence `A'` is
essential and

```
tau(A'[1:])=tau_0-1,
R(A')=(N+1)+(tau_0-1)=R_0.
```

This contradicts the maximum-length tie break.  Therefore the first
values differ.

The standard one-symbol prefix theorem now gives a primitive word `Y` and
an integer `k>=2` such that

```
A=Y^k,
cn(A)=k,
cn(A[1:])=k-1.
```

Thus the conserved-rank selection reaches the same whole-power reset form
as minimum hitting time, but by a different well-order.

## 2. Rank is conserved until the next disagreement

### Lemma 2

Let `C` be essential and suppose the autonomous orbits of `C` and
`C[1:]` share a word `P` of `delta` outputs before their next
disagreement.  Then `C P` is essential and

```
tau((C P)[1:])=tau(C[1:])-delta,
R(C P)=R(C).
```

### Proof

Every proper prefix of `P` is generated identically on both sides.  The
high side stays on a bad orbit.  The low side stays on its terminating
orbit and spends one unit of its hitting time per output.  Appending
`delta` symbols increases the word length by `delta` and decreases the
deleted hitting time by `delta`, proving both identities.

## 3. Exact cost of moving the boundary inward

At the immediate reset from Lemma 1 put

```
D=A[1:],       E=D k.
```

Assume the driven deletion `E` is bad.  Choose a shortest bad suffix `C`
of `E`, and put

```
j=|E|-|C|=N-|C|.
```

Minimality of the suffix makes `C` essential.

### Lemma 3 (depth cost)

```
tau(C[1:]) >= tau_0+j.                            (1)
```

### Proof

Global minimality of `R_0` gives

```
|C|+tau(C[1:])=R(C)>=R_0=N+tau_0.
```

Substitution of `|C|=N-j` yields (1).

Thus deleting `j` additional symbols from the left boundary must inject
at least `j` additional steps into the new terminating deleted orbit.  The
minimum-`tau` selection detects only a strict rise; the endpoint rank
records its exact linear cost.

## 4. Equality at the global rank cannot regrow the endpoint

Suppose equality holds in (1), so `R(C)=R_0`.  Let `P` be the common
output through the first disagreement of `C,C[1:]`, put
`delta=|P|`, and write the resulting reset as

```
C P=Z^ell,
```

with `Z` primitive and `ell>=2`.  Lemma 2 gives

```
R(C P)=R(C)=R_0.
```

The maximum-length tie break at rank `R_0` therefore gives

```
|C P|<=N,
delta<=j.                                         (2)
```

In particular, a same-rank boundary move cannot spend more generated
symbols before its next reset than the number of symbols it removed.  If
`j=0`, then `delta=0`: the context-loss word `E` is itself already a
whole-power reset.

Equation (2) does not control a strict rank increase.  Executed finite
promotions in `moving_boundary_context_loss.md` show that such an increase
can finance substantial root growth.

## 5. Compactness consequence for a strict staircase

All words obtained by repeatedly following a bad branch and deleting
leftmost context use only symbols already present in the original bad
seed.  Indeed, a newly appended symbol absent from the current seed would
make the next curling number one.  Hence one fixed finite alphabet contains
the entire moving-boundary construction.

On a fixed finite alphabet there are only finitely many words of bounded
length, and each terminating deletion has one fixed hitting time.
Consequently any family of essential words with unbounded endpoint rank
also has unbounded word length.

For a terminal-hidden promotion

```
C=Z^(ell-1) Z[:h],       1<=h<=|Z|,
```

put `m=|C|`, `s=|Z|`.  Then

```
(ell-1)s<m<=ell s.
```

If `M` bounds the finite alphabet of appended exponents, then `ell<=M`
and

```
s>=m/ell>=m/M.                                    (3)
```

Therefore an unbounded strict-rank staircase cannot be hidden forever at
bounded reset-root scale: along any unbounded-length terminal-hidden
subfamily, the hidden primitive roots are themselves unbounded.  The
remaining problem is not scale escape but origin escape: the roots begin
inside the currently retained seed, so their full self-replay profiles are
not automatically visible.

