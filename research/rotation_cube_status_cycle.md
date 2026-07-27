# Rotation-cube status coupling

This note studies the status cycle forced by a critical binary reset.  It
does not assume that a bad word has been found computationally.  A word is
**bad** if its orbit never reaches curling number one and **terminal**
otherwise.

## 1. Literature boundary

The following searches were made before the derivation:

* `curling number rotten sequence rotations conjugates cube`;
* `"curling number" rotation word cube conjugate`;
* `delete first letter power append first letter conjugate power lemma`;
* `combinatorics on words word a w^3 h power prefix last letter Fine Wilf`;
* `primitive word cube factor of another power Fine Wilf theorem overlap`.

The reusable published results are:

1. Chaffin--Linderman--Sloane--Wilks (CLSW), *On Curling Numbers of
   Integer Sequences*, JIS 16 (2013), Article 13.4.3, Theorem 7:
   prefixing one symbol can leave the curling number unchanged or raise it
   by one.
2. Fine--Wilf, *Uniqueness theorems for periodic functions*, Proc. AMS 16
   (1965), 109--114: a word of length at least
   `p+q-gcd(p,q)` having periods `p,q` also has period `gcd(p,q)`.
3. CLSW Section 4.3 and OEIS A216730 treat rotten finite-tail words.
   Their comparisons concern finite tail lengths after prefixing `2` or
   `3`; they do not classify rotations of a hypothetical nonterminating
   cube.

The searches found no published theorem matching the short prefix window
proved in Section 4.  It is recorded as not found in the searched
literature, not as an unconditional priority claim.

## 2. Setup and indexing

Let `P` be a primitive word of length `n>=3` over `{2,3}` whose proper
circular curling profile equals `P`.  The profile value `P[j]` is taken at
the cut immediately before the symbol `P[j]`.

For indices modulo `n`, put

```
Q_j = P[j:] P[:j],
A_j = Q_j^3,
D_j = A_j[1:],
a_j = Q_j[0].
```

Let `f_j` be the bad/terminal status of `A_j`.

## 3. Exact deleted-cube rotation

### Lemma 1

For every `j`,

```
cn(A_j)=3,
cn(D_j)=a_j,
D_j a_j=A_(j+1).                                  (1)
```

Consequently `D_j` has status `f_(j+1)`.

### Proof

The displayed cube gives `cn(A_j)>=3`.  If `A_j` had an `e`-power suffix
with `e>=4` and root length `r`, then

```
r <= 3n/e < n.
```

This would be a proper circular `e`-power at the cut immediately before
`Q_j[0]`, contradicting that the profile value there is at most three.
Thus `cn(A_j)=3`.

The exact circular profile supplies an `a_j`-power with root length below
`n` at the same cut.  Its powered length is at most `3(n-1)`, so it is
visible in the length-`3n-1` word `D_j`.  Hence

```
cn(D_j)>=a_j.
```

If `a_j=2` and `cn(D_j)>=3`, a maximizing root has length at most
`(3n-1)/3<n`.  If `a_j=3` and `cn(D_j)>=4`, a maximizing root has length
at most `(3n-1)/4<n`.  Either root would raise the proper circular profile
at this cut above `a_j`.  Therefore `cn(D_j)=a_j`.

Write `Q_j=a_j R`.  Direct concatenation gives

```
D_j a_j
 = R(a_j R)(a_j R)a_j
 = (R a_j)^3
 = A_(j+1).
```

Since `a_j` is two or three, `D_j` does not currently have curling number
one.  Its first orbit step is `A_(j+1)`, so the two words have the same
bad/terminal status.

## 4. Full locked-versus-external prefix classification

The next lemma does not use circular fixedness.

### Lemma 2

Let `Q=R x` be a primitive word of length `n>=3`.  Let `H` be any word,
of length `t`, and define

```
V=Q^3 H,
U=x Q^3 H.
```

Suppose `cn(U) != cn(V)`.  Put `k=cn(U)`, write the primitive maximizing
whole-power factorization as `U=Y^k`, and put

```
r=|Y|,                    g=gcd(n,r).
```

Exactly one of the following alternatives holds:

```
locked:    r=n, k>=4, H=R(xR)^(k-4);
external:  r>2n+g.                                  (2)
```

### Proof

Because `V` is a suffix of `U`, every powered suffix of `V` is a powered
suffix of `U`.  CLSW Theorem 7 gives

```
cn(V) <= cn(U) <= cn(V)+1.
```

The two values differ, so `cn(V)=k-1`.  A maximizing factorization of
`U` must use the entire word: if a nonempty prefix preceded the
maximizing suffix, that suffix would remain in `V` and give `cn(V)>=k`.
Thus `U=Y^k`.  The root `Y` is primitive, since an imprimitive `Y` would
give an exponent above the maximal value `k`.

The internal factor `Q^3` has periods `n` and `r`.  Suppose first that

```
r<=2n+g.
```

Then `n+r-g<=3n`, so Fine--Wilf applied to the length-`3n` factor `Q^3`
makes `g` a period of `Q^3`.  The integer `g` divides `n`.  If `g<n`,
the length-`n` word `Q` is a power of its length-`g` prefix, contrary to
primitivity.  Therefore `g=n`, so `n` divides `r`.

The threshold assumption now gives `r<=3n`, leaving

```
r=n, r=2n, or r=3n.
```

Put `C=xR`.  The word `U` begins with `C^3 xH`.  If `r=2n`, its
primitive root `Y`, the first `2n` symbols of `U`, is `C^2`.  If `r=3n`,
the same argument gives `Y=C^3`.  Both words are imprimitive.  Hence
`r=n`, `Y=C`, and `U=C^k`.  Comparing `C^3 xH` with `C^k` gives

```
xH=C^(k-3),
H=R C^(k-4).
```

Since `U` is longer than `C^3`, one has `k>=4`.  This is the locked
alternative.  If the Fine--Wilf threshold is not met, its strict
negation is `r>2n+g`, the external alternative.  The alternatives are
disjoint and exhaustive.

### Corollary 3 (short prefix window)

Under the hypotheses of Lemma 2, suppose `0<=t<=n+1`.  If
`cn(U) != cn(V)`, then

```
t=n-1,                  H=R.                       (3)
```

In the external alternative, `r>=2n+g+1`.  Since

```
t=k r-3n-1,
```

one obtains

```
k=2  =>  t>=n+2g+1>=n+3,
k>=3 =>  t>=3n+3g+2>=3n+5.                        (4)
```

Both bounds exceed `n+1`.  In the locked alternative,
`t=(k-3)n-1`.  Only `k=4` lies in the stated window, giving `t=n-1`
and `H=R`.

### Sharp fixed-profile exception

Assume in addition that `Q=R3` is a rotation of the circular fixed
profile.  For `H=R`,

```
3 Q^3 R = (3R)^4,
Q^3 R   = R(3R)^3.                                 (5)
```

The second word has a cube suffix.  Any fourth-power suffix has root
length below `n` and would raise the circular profile at the cut before
the final `3` above three.  Thus its curling number is exactly three.
The first word has a fourth-power suffix; any fifth-power suffix has root
length below `n` and is excluded at the same cut.  Therefore the values
in (5) are exactly

```
4 and 3.
```

## 5. Consequence for a status transition at a `3`

Suppose `a_j=3` and put `Q=Q_(j+1)`.  Then `Q` ends in `3`, and Lemma 1
gives

```
A_j 3 = 3 A_(j+1).                                (4)
```

Since `cn(A_j)=3`, the left side of (4) has status `f_j`.  Hence

```
f_j     = status(3 Q^3),
f_(j+1) = status(Q^3).                            (5)
```

Corollary 3 with `H` empty, together with `cn(Q^3)=3`, gives

```
cn(3Q^3)=cn(Q^3)=3.                               (6)
```

Suppose the two statuses in (5) differ.  As long as their curling numbers
agree, their states retain the form

```
3 Q^3 H_t,
  Q^3 H_t,
```

where `H_t` is the common length-`t` output.  A first unequal pair of
curling numbers must occur: otherwise the terminal member would reach
curling number one at the same time as the bad member.

At the first unequal cut, write the states as `3W` and `W`.  Lemma 2
gives the exhaustive split

```
locked:
  t=(k-3)n-1,
  H_t=Q[:-1] (3Q[:-1])^(k-4),
  root length n;

external:
  root length r>2n+gcd(n,r).
```

In both alternatives,

```
3W=Y^k,
cn(3W)=k,
cn(W)=k-1,                                        (7)
```

where `Y` is primitive and begins in `3`.

The first common output is the initial `3` in (6).  Every locked word
`H_t` begins with `Q[0]`; hence the locked alternative requires
`Q[0]=3`, an adjacent `33` in the circular profile.  If every `3`-run is
a singleton, only the external alternative remains.

In that singleton case, (4) sharpens according to orientation:

* if `3Q^3` is bad and `Q^3` is terminal, then `t>=n+3`; if the lower
  value at divergence is at least two, then `t>=3n+5`;
* if `3Q^3` is terminal and `Q^3` is bad, the lower value `k-1` is at
  least two, so `t>=3n+5`.

If `3W` is bad and `W` terminal, (7) is an ordinary essential reset.  If
`3W` is terminal and `W` bad, it is a reverse-status reset.  The
terminal hitting time has decreased by `t` common steps.  A singleton-`3`
ordinary boundary therefore has terminal lower-branch hitting time at
least `n+3`.  A singleton-`3` reverse boundary has terminal
prefixed-state hitting time at least `3n+6`, and its preceding terminal
rotation cube has hitting time at least `3n+7`.

This is the rigorous propagation furnished by a `3`-transition.  It
produces a whole-power reset whose primitive root starts in `3`; it does
not force a rotation transition at a symbol `2`.

## 6. Endpoint-rank audit

For a bad word `E` with terminal deletion, define the essential endpoint
rank

```
R(E)=|E|+tau(E[1:]).
```

Assume the original critical reset `A_0=P^3` was chosen with globally
minimum endpoint rank and, among rank minimizers, maximum length
`N=3n`.

### Ordinary boundary

Suppose `f_j` is bad, `f_(j+1)` is terminal, and `a_j=3`.  Both

```
A_j
and
E=3A_(j+1)=A_j 3
```

are essential.  Lemma 1 and the first orbit step of `A_j` give

```
R(A_j)
 =3n+tau(D_j)
 =3n+1+tau(A_(j+1))
 =R(E).                                            (8)
```

If this common value were the global minimum, `E` would be a rank
minimizer of length `N+1`, contradicting the maximum-length choice of
`A_0`.  Therefore every bad-to-terminal symbol-`3` boundary lies on a
strictly higher endpoint rank than `A_0`.

Let `3W,W` be its first unequal pair and let `3W=Y^k`, `r=|Y|`.  Common
evolution conserves (8):

```
R(3W)
 =kr+tau(W)
 =3n+1+tau(A_(j+1))
 =R(A_j).                                         (9)
```

For singleton `3`-runs the external alternative gives

```
R(A_j)>=kr,
r>2n+gcd(n,r).
```

The strict root increase is therefore financed by a strict endpoint-rank
excursion; it is not an endpoint-rank descent.

### Reverse boundary

For a terminal word `T` with bad deletion, define the reverse endpoint
quantity

```
R_rev(T)=|T|+tau(T).
```

If `f_j` is terminal, `f_(j+1)` is bad, and `a_j=3`, then the common
successor pair is

```
3A_(j+1) terminal,
 A_(j+1) bad.
```

The reverse quantity is conserved from `A_j` through the first unequal
cut:

```
R_rev(A_j)
 =3n+tau(A_j)
 =kr+tau(Y^k).                                    (10)
```

In the singleton case `k>=3` and `r>=2n+gcd(n,r)+1`, so

```
R_rev(A_j)>=kr>=6n+6.                             (11)
```

A maximum-length tie break at a globally minimum reverse rank would
exclude a symbol-`3` boundary from being the selected pair, because its
first common successor is longer at the same reverse rank.  There is no
proved comparison between `R_rev` and the forward rank `R(A_0)`.

### Fixed-rank consequence and limitation

At one fixed forward or reverse rank `B`, every reset root obeys
`2r<=B`.  Along any chain of singleton-`3` external transitions to which
Lemma 2 can be reapplied, root lengths more than double.  Such a chain has
fewer than

```
1+floor(log_2(B/r_0))
```

vertices and cannot form a directed cycle.

This observation does not close the rotation status cycle.  The root `Y`
at (7) is not proved to inherit the circular fixed profile, the
singleton-`3` condition, or another consecutive-rotation status pair.
Different rotation boundaries need not have the same endpoint rank, and
the terminal-to-bad orientation uses `R_rev` rather than `R`.  Thus the
strict root increase is not currently iterable around the cycle.

## 7. Executed length-21 and rank audits

After the mandatory A094004 calibration, the script
`check_rotation_cube_status_cycle.py` used both independent curling-number
implementations.

For

```
P=223222322232322232223
```

it verified primitivity, `pc_P=P`, all 21 instances of (1), and all 21
tail identities

```
tau(D_j)=1+tau(A_(j+1)).
```

All 21 rotation cubes terminate.  Their tail lengths, in phase order, are

```
2,11,3,2,5,3,3,2,60,7,3,2,3,2,3,1,3,2,7,5,3.
```

Thus this finite word has no actual status boundary and cannot serve as a
model of the hypothetical bad/terminal transition.  It does show that
ordinary tail length is not monotone around the rotation cycle: the
values range from one to sixty.

For each of the six phases labelled `3`, the script recomputed the locked
family for exponents four through six, including the sharp exception in
(5).  It also
exhausted 82,908 binary instances of Corollary 3 for every primitive root of
length three through seven and every binary `H` of length at most
`n+1`, with no violation.  This finite audit is supporting evidence; the
lemma rests on the proof in Section 4.

The separately calibrated `check_moving_boundary_context_loss.py`
recomputed an actual finite promotion with 52 common outputs whose
primitive reset-root length grows from four to 21 while the residual
deleted hitting time returns to four.  The boundary move injects deleted
hitting time 56, which finances the growth.  This is not a symbol-`3`
rotation boundary and both high words terminate; it is an exact
countermodel to any rank argument claiming that a long common excursion
or a return of the residual hitting time forces primitive-root descent.

## 8. Former inheritance gap

For singleton `3`-runs, a hypothetical status change at a `3` forces an
external maximizing root longer than `2n+gcd(n,r)`.  Depending on
orientation, at least `n+3` or `3n+5` common post-promotion outputs occur
before that reset.  The appended word `H_t` can create this new root
without making Fine--Wilf meet the threshold on the original `Q^3`.

The first unequal cut still has the exact whole-power form (7), but no
equation identifies `Y` with a rotation of `Q`, transfers its complete
circular profile to a shorter object, or forces its first symbol to be
`2`.  Section 9 bypasses that missing inheritance for status transitions:
the common replay itself is enough to exclude every terminal-to-bad
transition at a symbol `3`, and the opposite orientation has an exact
overlap obstruction.  Complete profile inheritance remains unavailable and
must not be used elsewhere.

## 9. Exact status theorem at a symbol `3`

The status convention is:

```
bad       := no state in the forward orbit has curling number one;
terminal  := some state in the forward orbit has curling number one.
```

Badness is inherited by every future state on an orbit.  A terminal state
passes terminal status to the states before its first hit of curling number
one, because those states retain the remaining finite path to that hit.
Throughout this section let `P,Q,A_j,D_j,a_j,f_j` be as in Sections 2--5, fix a phase with
`a_j=3`, write

```
Q=R3,                 n=|Q|,
E=3Q^3,               F=Q^3,
m=|E|=3n+1.
```

By (5), `status(E)=f_j` and `status(F)=f_(j+1)`.  Equation (6) gives the
exact initial values

```
cn(E)=cn(F)=3.                                    (12)
```

### Lemma 4 (binary bad-orbit alphabet)

Every curling number on a bad orbit starting from a binary word belongs to
`{2,3}`.

### Proof

Assume there is a first appended value `c>=4`.  Before that append, the
current word contains only `2` and `3`, so `c` has not occurred in it.  In
the word obtained by appending `c`, any suffix power of exponent at least
two would contain another occurrence of its final symbol `c` in the
preceding root copy.  There is no such occurrence.  The new word therefore
has curling number one, contradicting badness.

### Lemma 5 (first mismatch and replay visibility)

Suppose `E` and `F` have different statuses.  There is a finite word `G`
such that

```
U=EG,                 V=FG=U[1:]                 (13)
```

are the first paired states having different curling numbers.  If

```
k=cn(U),              r=|Y|,
```

then Lemma 2 gives the exact equations

```
U=Y^k,                cn(V)=k-1,                 (14)
```

where `Y` is primitive, binary, and begins in `3`.

If

```
m <= (k-1)r,                                      (15)
```

then necessarily

```
k=4.                                              (16)
```

### Proof

If the curling numbers of the paired states agreed forever, both orbits
would append the same infinite word.  The terminal member would reach its
first value one after finitely many common steps, making the other member
terminal at the same step.  Hence the first mismatch (13) exists.

Before it, every common appended value is also appended by the bad member.
Lemma 4 makes every such value binary.  Thus `G`, `U`, and the primitive
root `Y` in (14) are binary.  Since `U` starts with the first symbol of
`E`, one has `Y[0]=3`.

Under (15), after exactly `(k-1)r-m` common appends the paired states are

```
T=Y^(k-1),             T[1:].
```

This cut is strictly before the mismatch because one complete root `Y`
remains.  The displayed power gives `cn(T)>=k-1`.  The same word `T` is a
suffix of `V`, so any larger powered suffix of `T` would contradict the
exact equality `cn(V)=k-1` in (14).  Therefore

```
cn(T)=k-1.                                        (17)
```

The two states still have equal curling numbers at this cut, and their
next common output is the next symbol of `Y^k`, namely `Y[0]=3`.  Combining
this with (17) gives `k-1=3`, proving (16).

The proof covers equality in (15): then `T=E` is the initial paired state.
If (15) fails, Lemma 5 makes no assertion.

### Theorem 6 (reverse symbol-`3` transitions do not exist)

For every phase with `a_j=3`,

```
not (f_j=terminal and f_(j+1)=bad).               (18)
```

No singleton-run assumption is used.

### Proof

Assume the excluded orientation.  At the first mismatch (13), `V` lies on
the bad orbit, so Lemma 4 and (14) give the exhaustive alternatives

```
k-1=2  or  k-1=3.                                 (19)
```

Apply the exhaustive split in Lemma 2.

* In the locked case, Lemma 2 gives `k>=4`.  Equation (19) gives `k<=4`,
  hence `k=4`.
* In the external case,

  ```
  r>2n+gcd(n,r).
  ```

  Since the gcd is positive, `r>=2n+2`, and therefore

  ```
  m=3n+1 < 2r <= (k-1)r.
  ```

  Lemma 5 gives `k=4`.

These two cases are disjoint and exhaustive, so in every case

```
U=Y^4,                V=(Y^4)[1:],
cn(U)=4,              cn(V)=3,              Y[0]=3.    (20)
```

Put `Z=Y[1:]3`, the left rotation of `Y`.  Since the bad state `V` has
the exact curling number three, its next state is

```
V3=Z^4.                                           (21)
```

The word `Z^4` is binary and has curling number `c>=4` from its displayed
fourth power.  Thus `c` is absent from `Z^4`.  The unique-final-symbol
argument in Lemma 4 gives

```
cn(Z^4 c)=1.
```

Consequently the orbit from `V` reaches curling number one after two more
appends, contradicting that `V` is bad.  This proves (18).

## 10. The opposite orientation and the role of singleton `3`-runs

### Theorem 7 (ordinary symbol-`3` overlap)

Suppose

```
f_j=bad,               f_(j+1)=terminal.          (22)
```

At the first mismatch the external alternative holds, and there is an
integer `s` satisfying

```
2<=s<=n-1,
r=2n+s,
h=n+1-s,
2<=h<=n-1.                                        (23)
```

For the rotation `C=3R`, one has

```
C[:h]=C[s:]3,
C[h-1]=C[h]=3.                                   (24)
```

In particular, if every circular `3`-run of `P` is a singleton, (22) is
impossible.

### Proof

Now `U` in (14) lies on the bad orbit.  Lemma 4 gives `k` in `{2,3}`.
The locked alternative has `k>=4`, so it is impossible.  In the external
alternative, if `k=3`, then

```
m=3n+1<2r=(k-1)r,
```

and Lemma 5 would give `k=4`.  Hence the exact first-mismatch values are

```
cn(U)=2,              cn(V)=1.                   (25)
```

If `r>=m`, condition (15) would hold because `k-1=1`, again giving
`k=4`.  Thus `r<m`.  Put `s=r-2n`.  The external inequality gives

```
s>gcd(n,r)=gcd(n,s)>=1,
```

so `s>=2`.  The strict inequality `r<m=3n+1` gives `s<=n`.  Equality
`s=n` would contradict `s>gcd(n,s)`, proving the bounds in (23).

The high initial state has the exact form

```
E=3(R3)^3=C^3 3.
```

Since `r<m`, the primitive root `Y` is the first `r=2n+s` symbols of
`E`, so

```
Y=C^2 C[:s].
```

The word `U=Y^2` begins with `E`.  With `h=m-r=n+1-s`, comparison at the
end of `E` gives

```
E=Y Y[:h].
```

Because `h<n`, cancellation of the first two copies of `C` and then of
the prefix `C[:s]` gives

```
C[:s] C[:h]=C3
            =C[:s] C[s:]3,
```

and hence the first equality in (24).  Its final coordinate is
`C[h-1]=3`.

The common completion from `E` to `U` is exactly `G=Y[h:]`.  Its first
symbol is the initial common curling number in (12), namely three.  Since
`h<n`, that first symbol is `Y[h]=C[h]`.  This proves the adjacent pair in
(24).  A circular profile with only singleton `3`-runs has no such pair.

The singleton hypothesis enters only in the final sentence.  Equations
(23)--(24) remain valid when adjacent `3`'s are present.

### Corollary 8 (status-cycle location)

Every terminal-to-bad transition in the cyclic list

```
f_0,f_1,...,f_(n-1)
```

occurs at a phase labelled `2`.  If every circular `3`-run is a
singleton, every status transition in either orientation occurs at a
phase labelled `2`.

### Proof

The first assertion is Theorem 6.  For the second, Theorem 7 excludes the
other orientation at a label `3`.

## 11. Dependency and computation audit

The hypotheses `P` primitive, binary, and `pc_P=P` are the hypotheses of
the current critical self-replay branch.  In that branch, an ordinary
bad-to-terminal rotation boundary at the distinguished phase labelled
`2` supplies a nonconstant cyclic status list.  A nonconstant cyclic
binary status list has a terminal-to-bad boundary, and Corollary 8 locates
one at another label `2`.  This is the new downstream conclusion.

The unrestricted project has not proved that every hypothetical
counterorbit enters this critical self-replay branch.  Also, the critical
fixed-profile reduction does not guarantee singleton `3`-runs: a binary
fixed profile excludes circular `333`, but may still contain a `33`
component.  Theorem 6 is independent of that unresolved branch split;
the final sentence of Theorem 7 is conditional on the all-singleton
branch.

After the A094004 total-length calibration, the independent
implementations in `check_rotation_cube_status_cycle.py` executed:

* 677 finite exact first-mismatch replays for primitive binary roots of
  length at most nine and exponents at most six; none of the retained
  finite examples crossed the penultimate-copy cut;
* 3,489 exact `4`-versus-`3` whole-power/deletion pairs for primitive
  binary roots of length at most twelve, all of which executed the
  fourth-power rotation and fresh-marker termination in (21);
* 5,218 singleton-marker overlap instances through root length fourteen,
  including 152 instances satisfying the first equality in (24); every
  one had the forced marker `C[h-1]=3` and the singleton-forced value
  `C[h]!=3`.

These are bounded audits.  The unbounded conclusions rest on the proofs
above.

## 12. Arbitrary-alphabet supersession

`general_rotation_status.md` proves a strictly stronger version of
Theorem 6.  For a primitive exact circular fixed profile over any integer
alphabet with minimum two, a terminal-to-bad rotation-cube transition is
impossible at every phase labelled at least three.

The new proof does not use binary freshness.  A locked first mismatch would
have to replay the whole rotation prefix through a symbol `2` while its
outer cube forces curling number at least three.  An external mismatch with
exponent at least three replays a new primitive root `Y` far enough to force

```
pc_Y=Y,        min(Y)>=3,
```

contradicting Saari's Fundamental Periodicity Theorem.  The opposite status
orientation is consequently forced to an external `2`-versus-`1` reset and
the exact overlap

```
C[:h]=C[s:]a,
C[h-1]=a,
C[h]=max(3,C[1]).
```

For the binary phase `a=3`, this reduces to the adjacent-`33` conclusion of
Theorem 7.  Use the arbitrary-alphabet theorem in downstream arguments;
retain Sections 9--10 as the independently audited binary specialization.
