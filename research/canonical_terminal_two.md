# The canonical terminal-2 residual

This note specializes the terminal-prefix branch to a minimum-length
critical word whose final symbol is `2`.  It gives an exact canonical word
equation, a bounded audit of the resulting family, and a proved
first-divergence restriction.  It does not yet eliminate the residual
family.

The direct curling-number literature used here is Chaffin, Linderman,
Sloane and Wilks, *On Curling Numbers of Integer Sequences*, Journal of
Integer Sequences 16 (2013), Article 13.4.3.  Their Theorem 9 is the
canonical `XYX` theorem for a curling-one word made non-robust by a
proper suffix.  Their Theorem 10 proves uniqueness.  The period-difference
lemma used below is Lemma 8.1.1 of Lothaire, *Algebraic Combinatorics on
Words*, as restated, for example, as Lemma 1.3 in J. Simpson, *On
Palindromic Periodicities*, Australas. J. Combin. 92 (2025):

> If a word has periods `p>q`, then its prefix and suffix of length
> `|w|-q` have period `p-q`.

The literature queries and source scope are recorded in
`research/literature_search_log.md` and
`research/max_square_terminal_forest_literature.md`.

## 1. Rotation removes the one-symbol defect

Let

```
P=T2,                     cn(T)=1,
```

where `P` is a primitive binary critical word with exact proper circular
profile and full first-copy fitting.  Put

```
Q=2T.
```

Thus `Q` is the right rotation of `P`, so it is primitive and has the same
proper circular profile.  All positive phases of `Q` inherit fitting
witnesses; phase zero is the sole possible fitting failure.

### Lemma 1

```
cn(Q)=1.
```

### Proof

Suppose `Q` has a suffix `Z^m`, `m>=2`.  If this suffix omits the initial
symbol of `Q`, it is a square suffix of `T`, contradicting `cn(T)=1`.
It must therefore occupy all of `Q`.

If `m>=3`, deleting the initial symbol of `Z^m` leaves the final
`m-1>=2` complete copies of `Z` inside `T`, again contradicting
`cn(T)=1`.  Hence `m=2`, so `Q=Z^2`.  This contradicts the primitivity
of `Q`.  No exponent at least two is possible, proving the lemma.

## 2. Exact use of the terminal crossing square

Let a root-`q` circular square end at phase zero of `Q`.  It cannot fit in
`Q`, by Lemma 1, so

```
2q>n,                     n=|Q|.
```

Put

```
b=2q-n.
```

If `b=0`, then `Q` itself is a square, contradicting primitivity.  Hence
`b>0`.  Let `V` be the length-`b` suffix of `Q`.  The circular square,
read in the lift ending after `Q`, is the linear identity

```
VQ=R^2,                   |R|=q.                  (1)
```

Set

```
a=n-q.
```

The equality `b+a=q` and cancellation in (1) give words `A,V` with

```
R=VA,
Q=AVA,
|A|=a,                    |V|=b.                 (2)
```

Applying the proof of CLSW Theorem 9 to this specified square, rather
than merely its existential conclusion, gives

```
cn(A)=1,
V is a proper suffix of A.                        (3)
```

For completeness, the last assertion can also be recovered from their
proof.  Both `A` and `V` are suffixes of `Q`.  If `A` were a suffix of
`V`, write `V=CA`.  Then

```
Q=AVA=ACA A
```

would have a square suffix `A^2`, contradicting Lemma 1.  Thus `V` is a
proper suffix of `A`.

Consequently

```
b<a,
q=a+b<2n/3,               n=2a+b.                (4)
```

Writing `A=DV`, where `D` is nonempty, exposes the full geometry:

```
Q=DV VDV,                 R=VDV.                 (5)
```

The outer root-`q` square is `(VA)^2`.  At its midpoint the two displayed
copies of `V` form an inner root-`b` square.  This inner square ends at
cut `q`; the symbol at that cut is the first symbol of `A`, hence is `2`.

## 3. Candidate maximum-root lemma

Every exhaustive canonical-word audit performed so far satisfies:

> **Candidate lemma.** If `Q=AVA`, `V` is a nonempty proper suffix of
> `A`, and `cn(Q)=1`, then no proper circular square root is longer than
> `|VA|`.

There is a useful equivalent overlap formulation.  Put `p=|VA|` and
suppose a longer root has length `r=n-s>p`, so `0<s<a`.  Shifting one
of its two root blocks by the ambient period `n` shows that a length-`n`
conjugate of `Q` has period `s`.  The canonical equalities are

```
Q[0:a]=Q[p:n],
Q[a:a+b]=Q[a-b:a].                                (6)
```

For every tested parameter tuple `(a,b,s,c)`, the equality graph generated
by (6) and the period-`s` conjugate identifies two adjacent equal suffix
blocks of `Q`; this contradicts `cn(Q)=1`.  A symbolic proof that the
graph always contains such a suffix square is not supplied here, so the
candidate lemma is not used as a proved fact below.

The executable audit `research/audit_canonical_ava.py` enumerates the
normal form directly.  Through total length 36 it checked 68,041
primitive curling-one words beginning in `22`; in every one the outer
root was globally longest.  This is finite evidence, not a proof.

## 4. What the exact profile says at a first mismatch

The earlier draft of this section incorrectly asserted that root-`a`
squares end at both cuts `j` and `a+j`.  The correct unconditional
statement is that root-`a` squares end throughout the interval

```
a-b <= c <= a+j,                                   (7)
```

when `V[0:j]=A[0:j]`.  In particular a root-`a` square ends at the
middle cut `a+j`, but it need not end at cut `j`.  The stronger
consequences below use the exact cube profile rather than the false
second square.

Assume that `V` is not a prefix of `A`, and let `j` be its first
mismatch:

```
0<=j<b,
V[0:j]=A[0:j],
V[j] != A[j].                                      (8)
```

### Lemma 2 (the cube indicator is inherited by `A`)

For every `0<=c<a`,

```
A[c]=3
  iff
a proper circular cube of A ends at cut c.         (9)
```

### Proof

The word `A` is primitive because `cn(A)=1`.

Suppose first that a proper root-`s` circular cube of `A` ends at cut
`c`.  Fine--Wilf applied to the cube and the ambient period `a` gives
the proper-power bound

```
2s+gcd(a,s)<a.
```

In particular `2s<a`.  If `s>=c`, the length-`2s` square inside the
cube ending at cut zero would be a suffix of `A`, contrary to
`cn(A)=1`.  Hence `s<c`.

It follows that

```
3s<a+c.
```

The boundary from the final copy of `A` in `Q` to the initial copy has
preceding context `AA[0:c]`, of length `a+c`.  The whole cube lies in
this context, so the same cube ends at cut `c` of `Q`.  Exactness of
the profile of `Q` gives `A[c]=3`.

Conversely, suppose `A[c]=3`.  Exactness supplies a proper root-`s`
cube of `Q` ending at cut `c`.  The case `c=0` does not occur because
`A[0]=Q[0]=2`, so `0<c<a`.

The proper-power bound in the primitive length-`n` word `Q` gives
`2s<n`.  If `s>=c`, the length-`2s` factor ending at cut zero is
contained in the cube and has period `s`.  It is then a square suffix
of the finite word `Q`, contrary to `cn(Q)=1`.  Hence

```
s<c.                                               (10)
```

The context from cut `-a` through cut `c` is `AA[0:c]` and has period
`a`.  If the cube began before cut `-a`, this full context, of length
`a+c`, would also have period `s`.  From (10),

```
a+c >= a+s-gcd(a,s),
```

so Fine--Wilf would give it period `gcd(a,s)<a`.  It contains a
complete copy of `A`, and the gcd divides `a`, so `A` would be a
nontrivial integral power.  This contradicts primitivity.  The cube is
therefore contained in `AA[0:c]`; it is a proper circular cube of `A`.
This proves (9).

### Corollary 3 (orientation and boundary crossing)

The first mismatch has the orientation

```
A[j]=2,                    V[j]=3.                 (11)
```

Every cube of `Q` ending at the middle cut

```
E=a+j
```

begins before the displayed `a`-periodic context

```
AA A[0:j],
```

whose length is `2a+j`.

### Proof

If `A[j]=3`, Lemma 2 supplies a proper cube of `A` ending at phase
`j`.  Its span is less than `2a`, so the matched prefix in (8) copies
it to cut `E`.  Exactness would then give `V[j]=3`, contrary to (8).
Since the alphabet is `{2,3}`, (11) follows.

If a cube ending at `E` were contained in `AAA[0:j]`, its root would
be shorter than `a`, because the context has length less than `3a`.
It would therefore be a proper circular cube of `A` ending at phase
`j`.  Lemma 2 would give `A[j]=3`, contradicting (11).  Hence it
crosses the left boundary of that context.

### Lemma 4 (scale gap)

Let `r` be a root length of a cube at `E`, and put

```
g=gcd(a,r),                 G=gcd(n,r).
```

Then either `r=a`, or

```
r>a+j+g,
2r+G<n.                                            (12)
```

In the second branch, writing `r=a+d` gives

```
d>j+g,
2d+G<b.                                           (13)
```

### Proof

Corollary 3 gives `3r>2a+j`.  The common suffix of the cube and the
displayed `a`-periodic context has length `2a+j` and periods `a` and
`r`.  If it reached the Fine--Wilf threshold `a+r-g`, it would give
period `g` to a complete copy of primitive `A`.  This is impossible
when `g<a`; threshold failure is the first inequality in (12).

If `g=a`, then `a` divides `r`.  The proper-power bound for a cube in
the primitive length-`n` word is the second inequality in (12), which
implies `r<n/2<3a/2`.  The only positive multiple of `a` in this range
is `r=a`.  Substituting `r=a+d` and `n=2a+b` into `2r+G<n` gives
(13).

### Lemma 5 (part of the same-scale branch)

Put `z=a-b`, so `A=DV` with `|D|=z`.  If the exceptional cube root is
`r=a`, then

```
j<=z.                                              (14)
```

### Proof

Assume `j>z`.  For each `1<=t<=j-z`, the root-`a` cube ending at `E`
also ends at `E-t`.  For an explicit verification, when the cube is
shifted left by one symbol at offset `u`, put `k=j-u`.  The sole new
period-`a` equality is

```
Q[E-3a-u]=Q[E-a-u].
```

Modulo `n`, these positions are `b+k` and `k`.  Since
`z<=k<j<b`, the first position is in the middle `V`, at offset `k-z`.
Therefore

```
Q[b+k]=V[k-z]=A[k]=Q[k].
```

Here `V=A[z:a]`, and the second equality uses `V[k]=A[k]` for `k<j`.
At `t=j-z`, a proper root-`a` cube ends at middle offset `z`.  Its
label is

```
V[z]=A[z]=V[0]=A[0]=2,
```

where `z<j` supplies the matched-prefix equality.  This contradicts
the exact profile.  Thus (14) holds.

In the critical application the cube at `E` is a first-copy fitting
witness.  This eliminates the strict branch (13).  Indeed fitting gives

```
3(a+d)<=n+E-1,
3d<=b+j-1.
```

Put `ell=b+j-3d`, so `1<=ell<b<a`.  In the lift ending at `E`, the
cube starts at phase `ell`, and the suffix

```
W=V A A A[0:j]
```

lies inside it.  The word `W` has period `a` directly from the displayed
copies and period `a+d` from the cube.  Its length exceeds the
Fine--Wilf threshold:

```
|W|-(a+(a+d)-gcd(a,d))=b+j-d+gcd(a,d)>0.
```

Thus `W`, and in particular its complete copy of `A`, has period
`gcd(a,d)<a`.  This contradicts the primitivity of `A`.

The sole residual is therefore the same-scale branch

```
r=a,                       j<=a-b.                (15)
```

The negative profile at cut `j` says that no proper cube of `Q` ends
there; the root-`a` cube at `E` supplies only a root-`a` square at `j`,
so this negative fact does not alone contradict (15).

At the boundary case `j=a-b`, write

```
A=D D C,
V=D C,
D[0]=2,
C[0]=3.
```

The inherited exact profile of `A` requires a cube at cut `2|D|`,
where the literal square `D^2` ends.  The complete audited split for
that smaller maturation, including the exclusion of an equal root and
the two unequal-root normal forms, is Lemma 7 of
`research/ava_fixed_inheritance.md`.  For `j<a-b`, Lemma 8 there gives
the two exact residual word equations.  Neither residual has yet been
eliminated.

## 5. Exact countermodel to overstrong local claims

The executed audit gives

```
Q=2223232223,
A=2223,
V=23.
```

It is primitive, has `cn(Q)=1`, begins in `22`, has a square at every
circular cut, and its outer root of length six is globally longest.
Its cube-indicator profile is correct at nine of ten cuts.  The sole
failure is cut five: the displayed symbol is `3`, but no cube ends
there.  The longest-square/last-cube construction uses a root-one child,
and the word has exactly one canonical `AVA` decomposition.

Therefore none of the following is sufficient by itself:

```
canonical AVA form,
all-cut square coverage,
global maximality of the outer root,
the strict half-scale last-cube child,
uniqueness of the AVA decomposition.
```

The missing load-bearing condition is cube existence at the middle copy
of `V`.  Any completion must use that condition to eliminate the
upward mismatch (11), including the residual branches after Lemma 5,
rather than claim that the maximum-root forest already supplies a
second `AVA` decomposition.
