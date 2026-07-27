# Minimum deleted-orbit hitting time forces immediate divergence

This note gives a sound replacement for the invalid attempt to transfer
minimum seed length from a shortest counterseed to a later replay root.
It is a reduction, not a termination proof.

## Definitions

Call a finite nonempty word `A` **bad** if its orbit never reaches
curling number one.  For a word `B` whose orbit does reach one, define

```
tau(B)=min { t>=0 : cn(B_t)=1 },
```

where `B_0=B` and `B_(t+1)=B_t cn(B_t)`.

Let

```
C={ A : A is bad and A[1:] reaches one }.
```

If a bad word exists, `C` is nonempty: choose a bad word of globally
minimum length.  Its length is at least two, because every one-letter
word has curling number one, and its first-symbol deletion has smaller
length and therefore reaches one.

## Lemma 1 (hitting-time descent)

Choose `A` in `C` minimizing `tau(A[1:])`.  Then

```
cn(A) != cn(A[1:]).                              (1)
```

### Proof

Put `B=A[1:]` and suppose both words have the same curling number `c`.
Because `A` is bad,

```
c=cn(A)>=2.
```

In particular `cn(B)` is not one, so `tau(B)>0`.  Append the common
value and put

```
A'=A c,
B'=B c.
```

The word `A'` is the next state on the bad orbit of `A`, hence is bad.
The word `B'` is the next state on the terminating orbit of `B`, and

```
tau(B')=tau(B)-1.
```

Deletion commutes with this common append:

```
A'[1:]=B'.
```

Thus `A'` belongs to `C` and has strictly smaller deleted-orbit hitting
time than `A`, contradicting the choice of `A`.  This proves (1).

This proof also covers `tau(B)=0`: in that case `cn(B)=1`, whereas
`cn(A)>=2`, so (1) holds without the descent step.

## Lemma 2 (immediate whole-power normal form)

For the word `A` selected in Lemma 1 there are a primitive nonempty word
`Y` and an integer `k>=2` such that

```
A=Y^k,
cn(A)=k,
cn(A[1:])=k-1,
A[1:]=Y[1:]Y^(k-1).                             (2)
```

### Proof

Put

```
k=cn(A),        ell=cn(A[1:]).
```

Every suffix power of `A[1:]` is also a suffix power of `A`, so
`k>=ell`.  Theorem 7 of
Chaffin--Linderman--Sloane--Wilks (CLSW), *On Curling Numbers of Integer
Sequences*, JIS 16 (2013), Article 13.4.3, says that prefixing one
symbol raises a curling number by at most one.  Hence

```
ell<=k<=ell+1.
```

Lemma 1 makes the values unequal, so

```
k=ell+1.                                          (3)
```

For completeness, the whole-power argument isolated in the proof of
CLSW Theorem 8 is included next.  It also recovers (3) directly in the
present notation.  Lemma 1 and suffix monotonicity give

```
k>ell.
```

Choose a maximizing `k`-root `Y` of length `r`; thus `A` ends in
`Y^k`.  If

```
k r<=|A|-1,
```

the same complete suffix power would lie in `A[1:]`, giving
`ell>=k`, a contradiction.  Since the power is a suffix of `A`,

```
k r<=|A|.
```

The two integer inequalities force

```
k r=|A|,
```

so the maximizing power occupies all of `A` and `A=Y^k`.  Deleting the
first symbol gives the final identity in (2).  It displays a
`(k-1)`-power suffix of `A[1:]`, whence

```
ell>=k-1.
```

Together with `ell<k`, this gives `ell=k-1`.

Finally, if `Y=Z^d` for an integer `d>=2`, then

```
A=Z^(dk)
```

would have curling number at least `dk>k`, contradicting the definition
of `k`.  Thus `Y` is primitive.

The local conclusions in this lemma are therefore published
consequences of CLSW Theorems 7--8.  The extra ingredient here is the
dynamical `tau`-minimal selection in Lemma 1, which forces the strict
CLSW case to occur at time zero.

## Corollary 3 (the long replay-root branch is avoidable)

Starting from a shortest bad seed and waiting for its first divergence
from the deleted orbit can produce a replay root longer than the seed.
That later root is an orbit state and does not inherit shortest-seed
minimality.

Lemmas 1--2 give a different well-founded choice.  Minimize the
terminating deleted orbit's remaining hitting time first.  The selected
pair cannot share even one output, so its whole-power maturation occurs
at time zero.  There is no longer replay state to which minimality must
be transferred.

The reduction does not say that `Y` is bad.  Even if `Y` terminates, the
power `Y^k` may be protected by its left context.  Thus (2) isolates the
remaining power-context obstruction rather than proving the conjecture.

## Source

Chaffin, Linderman, Sloane and Wilks, *On Curling Numbers of Integer
Sequences*, Journal of Integer Sequences 16 (2013), Article 13.4.3,
Theorems 7--8:
<https://cs.uwaterloo.ca/journals/JIS/VOL16/Sloane/CNC.pdf>.

## Lean 4 statement

With orbit and deletion definitions supplied by the final formalization,
the central selection lemma can be stated as follows.

```lean
theorem min_deleted_hitting_time_diverges_immediately
    (A : List Int)
    (hA_nonempty : A ≠ [])
    (hA_bad : ∀ t : Nat, CurlingNumber (orbit A t) ≠ 1)
    (hdel_terminates :
      ∃ t : Nat, CurlingNumber (orbit A.tail t) = 1)
    (hminimal :
      ∀ C : List Int,
        C ≠ [] →
        (∀ t : Nat, CurlingNumber (orbit C t) ≠ 1) →
        (∃ t : Nat, CurlingNumber (orbit C.tail t) = 1) →
        firstOneTime A.tail ≤ firstOneTime C.tail) :
    CurlingNumber A ≠ CurlingNumber A.tail
```

The natural-language proof above identifies the exact successor pair
used in the contradiction:

```
C=A ++ [CurlingNumber A].
```
