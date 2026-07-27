# Consecutive reset roots: external replay or internal period

This note continues `tau_min_context_dynamics.md` in its branch where
every fixed-first-symbol deletion state terminates.  It proves an exact
split between consecutive reset roots.  It also records why the existing
`A V A` quotient lemmas cannot be imported into the `k=2` special case
without additional hypotheses.

## 1. Orbit coordinates

Let `T` be the right-infinite word traced by the hypothetical bad orbit,
with the finite initial seed occupying `T[0:N_0]`.  Thus, for every
`n>=N_0`,

```
T[n]=cn(T[0:n]).
```

At a reset endpoint suppose

```
T[0:k p]=U^k,
|U|=p,
U primitive,
cn(T[1:k p])=k-1.                                (1)
```

The last equality is the strict first-deletion value at a reset.  If
`p>=N_0`, then `U=T[0:p]` is itself an orbit state.

## 2. Every sufficiently late reset exponent is three

Assume `p>=N_0`.  Since the orbit from the state `U` reaches the displayed
prefix `U^k`, it emits the remaining `k-1` copies of `U`.  Therefore

```
cn(U^a U[:j])=U[j]       (1<=a<k, 0<=j<p).       (2)
```

In particular, at `a=k-1` the suffix consisting of `k-1` copies of the
conjugate `U[j:]U[:j]` gives

```
U[j]>=k-1.                                       (3)
```

At `j=0`, the word `U^(k-1)` is also a suffix of `T[1:k p]`.
Equations (1)--(2) consequently give

```
U[0]=cn(U^(k-1))<=k-1.
```

Together with (3),

```
U[0]=k-1.                                        (4)
```

The high replay in (2) also gives the exact proper circular profile

```
pc_U(j)=U[j]             (0<=j<p).                (5)
```

For the lower bound, a proper circular witness is visible in the first
two replay copies.  For the upper bound, let a proper root of length
`r<p` persist at phase `j`.  If its periodic interval reached length
`p+r-gcd(p,r)`, Fine--Wilf would give the proper gcd period to a complete
conjugate of primitive `U`.  Hence the whole witness has length below
`2p` and is visible at the corresponding cut of the replay through
`U^3`; (2) supplies the upper bound.  The case `k=2` is already excluded
by (3)--(4): it would give `U[0]=1`, although `U` is a state on a bad
orbit.

If `k>=4`, equations (3) and (5) say that every phase of the primitive
periodic word `U^Z` ends in a proper cube.  Reversing the word makes it
everywhere `(phi+1)`-repetitive.  Saari's everywhere-repetition theorem,
used with the bounded root lengths below `p`, makes this periodic word
have a period strictly below `p`, contradicting primitivity.  This is
the same argument spelled out in Section 3 of
`critical_seed_induction.md`.  Therefore every reset whose primitive
root is itself an orbit state has

```
k=3,             U[0]=2,             pc_U=U.      (6)
```

Since reset-root lengths are unbounded, (6) applies to every sufficiently
late reset.

## 3. Exact split for two consecutive resets

Take consecutive reset endpoints

```
T[0:k p]=U^k,             T[0:ell q]=V^ell,
```

where `U,V` are primitive and the second reset is later.  Put

```
g=gcd(p,q).
```

The reset-root comparison from `tau_min_context_dynamics.md` gives either

```
q=p, U=V, ell>k,                                  (7)
```

or

```
q>(k-1)p+g.                                       (8)
```

Assume the unequal-root case (8).  Equality `q=k p` is impossible,
because then

```
V=T[0:q]=U^k
```

would not be primitive.  There are exactly two alternatives.

### External alternative

```
q>k p.                                            (9)
```

The root `V=T[0:q]` occurs strictly after the old reset endpoint and
strictly before its own reset endpoint.  Since the two reset endpoints
are consecutive, every intervening first-deletion comparison is an
equality step.  Hence the autonomous orbits of

```
V,             V[1:]
```

emit the same word `V^(ell-1)` up to the next reset.  The first word is
bad and the second reaches the terminating deletion state

```
V[1:]V^(ell-1).
```

Thus `V` is a full deletion-critical self-replayer.  If the old root is
already in the late regime (6), then

```
T[0:3p+1]=U^3 3,
```

so (9) also gives the literal nested prefix

```
V begins U^3 3.                                  (10)
```

Applying Section 2 to `V` gives

```
ell=3,             V[0]=2,             pc_V=V.   (11)
```

### Internal alternative

```
(k-1)p+g<q<k p.                                  (12)
```

Write

```
q=(k-1)p+h.
```

Then

```
g<h<p,             gcd(p,h)=g,                   (13)
V=U^(k-1)U[:h].                                  (14)
```

Because `V^ell` begins with two copies of `V` and

```
2q>k p,
```

comparison on the overlap `[q,kp)` gives

```
U[h:p]=U[:p-h].                                  (15)
```

Thus `h` is a period of the finite word `U`.  The actual symbol after
the old reset is `k`.  The same `q`-periodic comparison, now at coordinate
`kp`, gives

```
U[p-h]=T[kp]=k.                                  (16)
```

Put `m=floor(p/h)` and write `p=m h+r`, `0<=r<h`.  Equation (15) makes
the suffix `U[r:p]` an exact `m`-th power of a length-`h` block.  This
suffix lies at the end of `T[1:kp]`, whose exact curling number is `k-1`
by (1).  Therefore

```
floor(p/h)<=k-1,
h>p/k.                                           (17)
```

Equations (12)--(17) are the complete internal-overlap normal form.

In the late regime (6), put

```
a=p-h.
```

Equation (15) says that `U` has the border

```
U[:a]=U[p-a:p],                                  (18)
```

while (16) says

```
U[a]=3.                                          (19)
```

This border is necessarily anchored inside the initial seed:

```
1<=a<N_0.                                        (20)
```

Indeed, if `a>=N_0`, then `T[0:a]=U[:a]` is an orbit
state and (19) gives

```
cn(U[:a])=T[a]=3.
```

But (18) makes this word a suffix of `U`, whereas (6) gives
`cn(U)=U[0]=2`.  Suffix monotonicity would give
`cn(U)>=3`, a contradiction.

Consequently every late internal transition is not merely within the
Fine--Wilf interval.  It has the bounded-defect form

```
h=p-a,
q=3p-a,
V=U^3 with its final a symbols deleted,
1<=a<N_0,
U[:a]=U[-a:],
T[a]=3.                                          (21)
```

Only the finitely many `3`-labelled cuts inside the initial seed can
supply this defect.

## 4. The special `k=2` border and the `A V A` audit

For `k=2`, equation (17) says `h>p/2`.  Put

```
a=p-h,              b=2h-p.
```

Both are positive.  Equation (15) gives nonempty words `A,B` with

```
|A|=a,       |B|=b,
U=A B A,
B[0]=U[p-h]=2.                                  (22)
```

Moreover `cn(T[1:2p])=1`, and `U` is a suffix of that word, so

```
cn(U)=1,       cn(A)=1.                          (23)
```

If `p>=N_0`, (23) contradicts the fact that `U` is an orbit state on a
bad orbit.  Hence a `k=2` reset can occur only while its primitive root
is shorter than the initial seed.

This visibility hypothesis is load-bearing.  The reset state `U^2`
itself has length `2p>=N_0`, but its root may satisfy

```
p<N_0<=2p.                                        (24)
```

Then `cn(U)=1` is still a valid consequence of the strict deleted value,
but the orbit never visits `U` as a complete state.  In particular the
identity

```
T[p]=cn(T[0:p])
```

is unavailable: position `p` lies inside the prescribed initial seed,
not in the generated part of the orbit.  Thus there is no contradiction
in this hidden-root case.

The same warning applies to the next internal root
`V=U U[:h]`, whose length lies strictly between `p` and `2p`.  If the
orbit is started at `U^2`, both `U` and `V` are hidden inside the initial
state even though their later power endpoints are visible.  Therefore the
zero compatible examples found by
`search_orbit_compatible_hidden_k2.py` through its finite search range are
not explained by (23); that computation probes the genuinely residual
seed-anchored case.  The argument here proves only that such hidden
`k=2` roots are confined below the one fixed length `N_0`, so they cannot
form the unbounded tail of an infinite reset tower.

The form (22) superficially resembles the setup of
`ava_fixed_inheritance.md`, but that lemma cannot be applied.  Its
hypotheses additionally require:

```
U=A V A with 0<|V|<|A|,
V a suffix of A,
U[0]=U[1]=2,
a binary alphabet,
and the exact proper circular cube/fourth-power profile.
```

None of the length inequality, suffix relation, first-two-symbol
condition, binary restriction, or circular-profile condition follows
from (22)--(23).  The older quotient lemmas therefore do not discharge
the `k=2` internal case; the direct orbit-state contradiction above is
the sound late-reset exclusion.

## 5. Remaining branch

After finitely many initial resets, every consecutive unequal-root
transition is between exact fixed-profile roots satisfying (6), and its
new length obeys

```
q>2p+g.                                          (25)
```

If `q>3p`, the new root contains the smaller critical marker
`U^3 3` and is the full self-replayer in (10)--(11).  If `q<3p`, it has
the exact internal form

```
q=3p-a,
1<=a<N_0,
U[:a]=U[-a:],
T[a]=3.                                          (26)
```

The equality `q=3p` is excluded by primitivity of `V`.  Thus the infinite
reset tower has been reduced to an infinite sequence of the two
incompatible mechanisms (10) and (26).  Neither mechanism is eliminated
by Fine--Wilf alone.
