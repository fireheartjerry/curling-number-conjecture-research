# Two-level equations in the normalized fixed-profile tower

This note records what two nested levels of the residual cube tower force.
It does not exclude the tower.  Its point is to keep the shared-orbit
equalities, the proper-profile equations, and the boundary divergence in
one coordinate system.

## 1. Hypotheses and notation

Let `T` be the right-infinite word supplied by a normalized autonomous
counterorbit.  Take two consecutive or nonconsecutive tower roots

```
A=T[0:p],             B=T[0:N],             p<N.
```

Assume both are primitive, both have proper circular fixed profile, and
the local orbit from either root emits two further copies of that root and
then the cube delimiter.  Thus

```
pc_A=A,               pc_B=B,
A[0]=B[0]=2,
T[0:3p+1]=A^3 3,
T[0:3N+1]=B^3 3.
```

In particular `N>=3p+1`.  Put

```
U_t=T[0:t].
```

Every displayed curling-number equality below is a direct instance of the
two assumed local orbit recurrences.  The concrete finite audit in
Section 6 recomputes its numerical instances with both implementations in
`curling.py`.

## 2. Exact synchronization followed by delayed maturation

For `0<=t<2p`, the common continuation is

```
U_t=A^floor(t/p) A[0:(t mod p)]
```

and the two contexts satisfy

```
cn(A U_t)=cn(B U_t)=A[t mod p].                 (1)
```

For the small context, this is the replay of the two copies following
`A`.  For the large context, `t<2p<N`, so it is the initial part of the
first copy following `B`.  Both continuations are the same prefix of `T`.

At the first boundary after those two copies, the values separate:

```
cn(A A^2)=cn(A^3)=3,
cn(B A^2)=2.                                    (2)
```

The second equality follows from the large replay:

```
cn(B U_(2p))=T[2p]=A[0]=2.
```

One old-root copy later, the large context matures the same displayed
cube:

```
cn(B A^3)=3.                                    (3)
```

Indeed `3p<N`, so the next label in the large replay is
`T[3p]=3`.  Equations (2)--(3) are the exact delayed-maturation normal
form: the suffix `A^2` is maximal at the first large boundary, and the
suffix `A^3` is maximal one copy later.

The same facts appear intrinsically in the larger circular profile:

```
pc_B(2p)=B[2p]=2,       with the proper root-p square A^2,
pc_B(3p)=B[3p]=3,       with the proper root-p cube A^3.      (4)
```

The restriction `p<N` makes both witnesses proper for `B`.

## 3. The exact last-suffix seam

Let

```
ell=lcs(A,B)
```

be the length of the longest common suffix.  Then

```
ell<p.                                             (5)
```

If `ell>=p`, the word `B` ends in `A`; consequently `B A^2` ends in
`A^3`, contradicting the second equality in (2).

The mismatch immediately before the common suffix persists when the same
word is appended to both contexts.  Hence, for every `t>=0`,

```
lcs(A U_t, B U_t)=ell+t.                          (6)
```

At the divergence in (2), the exact common suffix therefore has length

```
2p+ell<3p.                                        (7)
```

The high cube is forced to cross the seam by exactly `p-ell` symbols.

There is only one primitive maximizing cube-root length at the high side:

```
Roots_3(A^3)={p}.                                 (8)
```

A cube root has length at most `p`.  A root shorter than `p` would be a
proper circular cube ending at phase zero of `A`, contradicting
`pc_A(0)=A[0]=2`.  The root of length `p` is displayed.  A nonprimitive
root would turn the suffix into a power of exponent greater than three,
contradicting the first equality in (2).

By contrast, `B A^2` contains the root-`p` square and contains no cube
suffix of any root length, because its exact value in (2) is two.  Thus
the first cross-level disagreement is not a disagreement about the
existence of the outer period.  It is precisely the missing third copy
across the seam.

## 4. Phase-zero square roots must coalesce

Let `r_t` and `s_t` be the least primitive maximizing-root lengths of
`A U_t` and `B U_t`, respectively, whenever the common value in (1) is
at least two.  Put

```
k_t=A[t mod p].
```

If `r_t!=s_t`, the two-context Fine--Wilf lemma gives all three strict
inequalities

```
k_t r_t>ell+t,
k_t s_t>ell+t,
ell+t<r_t+s_t-gcd(r_t,s_t).                     (9)
```

For completeness, if one powered suffix fit in the common suffix, it
would be a witness in both contexts.  Comparing least root lengths in
both directions would give `r_t=s_t`.  If neither fits, the common suffix
has both periods.  Meeting the Fine--Wilf threshold would make one of the
two complete primitive terminal roots have the smaller gcd period.

The decorations cannot remain different for a whole old-root copy.  At
`t=p`, both states have value two:

```
A U_p=A^2,              B U_p=B A.              (10)
```

Let `r_0` be the least maximizing square-root length of `A`.  Its square
lies inside `A`, so

```
2r_0<=p.
```

Both words in (10) end in the entire word `A`, and hence both contain
that root-`r_0` square.  Their least roots at time `p` are at most `r_0`;
the squares belonging to either least root lie inside the shared terminal
copy of `A`.  Transporting each witness to the other context and using
leastness in both directions proves

```
r_p=s_p.                                         (11)
```

Consequently the first time at which the least root decorations agree is
at most `p`; before that first agreement, every pair obeys (9).  This is a
genuine two-level restriction, but it is not persistent: a later
maximizing root can again cross the growing common suffix.

## 5. What the two levels still fail to control

The smaller prefix occupies the beginning of `B`, whereas a phase-zero
square certifying `cn(B)=2` is a suffix of `B`.  The equations give no
upper or lower bound forcing that suffix square either to avoid or to
overlap the earlier prefix

```
A^3 3.
```

It may lie wholly inside the intervening word

```
B[(3p+1):N].
```

If it overlaps that prefix, the amount of overlap is presently
uncontrolled.  Equations (1)--(11) supply no equality between its root and
the prefix cube `A^3`.  At `t=p` the canonical roots coalesce because a
whole copy of `A` is shared.  At `t=2p` the unique high cube crosses the
unshared seam, so this coalescence does not constrain the low context's
additional roots.  A proof from two levels needs a mechanism that carries
the phase-zero square of `B` backward through the actual intervening orbit
segment, or else proves that one of its copies overlaps `A^3 3` far enough
to force a forbidden proper cube.  Prefix nesting and the two boundary
values alone do not provide that mechanism.

## 6. Executed local seam model

The checker `research/check_critical_seed_induction.py` recomputes every
value in this section using both exact curling-number implementations.
Take

```
A=223222322232322232223,       p=21,
C=A[1:].
```

The word `A` is primitive and has `pc_A=A`.  The following checkpoints
are executed:

| `t` | `cn(A U_t)` and maximizing roots | `cn(C U_t)` and maximizing roots | exact common suffix |
|---:|---|---|---:|
| 0 | `2`, roots `(4,10)` | `2`, roots `(4,10)` | 20 |
| 21 | `2`, roots `(4,10,21)` | `2`, roots `(4,10)` | 41 |
| 42 | `3`, root `(21)` | `2`, roots `(4,10,21)` | 62 |
| 63 | `4`, root `(21)` | `3`, root `(21)` | 83 |

Here `U_t` is the length-`t` prefix of `A^3`.  Thus the shifted context
realizes synchronization, the cube-versus-square break, and the later
static cube endpoint.  It does not follow the required intervening replay
after the break: its next mismatch with that prescribed continuation is
also found by the checker.  It is therefore a seam model, not a nested
tower level.

There is also a prefix-and-suffix countermodel to any argument using only
those two pieces.  Put

```
D=A^3 3 99 C.
```

The symbol `99` occurs once.  A repeated suffix power crossing it would
copy that occurrence into another root block, requiring another `99`.
Therefore every repeated suffix power lies strictly after the delimiter,
and

```
cn(D U_t)=cn(C U_t),             0<=t<=3p.       (12)
```

The checker exhausts all 64 indicated static cuts, including the cube
endpoint at `t=3p`.  These cuts are not one orbit after the first
post-break mismatch.  The word begins in the required prefix `A^3 3`, but
it is not a proper-profile fixed word and it is not a second prefix of the
same autonomous orbit.  It proves that the full fixed-profile equations in
the actual intervening orbit segment are load-bearing; the prefix cube,
phase-zero suffix square, and seam geometry cannot be treated as
independent local constraints.
