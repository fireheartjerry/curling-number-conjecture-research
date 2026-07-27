# The symbol-two rotation seam

This note assumes a primitive word `P` of length `n` with

```
pc_P=P,          min(P)=2.
```

It classifies the only rotation-status boundary not excluded by
`general_rotation_status.md`.  It does not prove that the remaining
cases are impossible.

Necessarily `n>=3`: length one has no proper power root, while at length
two every proper square root has length one and would force the two
symbols equal, contrary to primitivity.

## 1. The three-word fork

Fix a phase labelled `2`, rotate it to the front, and write

```
C=2R,             Q=R2,
D=Q^3[:-1]=R2R2R.
```

Thus `C` and `Q` are consecutive rotations of `P`.  Put

```
H=2D3=C^3 3,
E=2D2=2 Q^3,
B=D2=Q^3.                                      (1)
```

The cube `C^3` has curling number three, so `H` is its actual successor
and has the status of `C^3`.  The word `B` has the status of the next
rotation cube.

The next label is automatically at most three.  Indeed, let
`b_0=Q[0]=C[1]` and choose a proper root of the attaining `b_0`-power
ending at cut one.  Its last root symbol is `C[0]=2`.  Deleting that
last symbol leaves `b_0-1` complete copies of the conjugate root ending
at cut zero, so

```
2=pc_C(0)>=b_0-1,          b_0<=3.              (2a)
```

Consequently, put

```
b=max(3,Q[0])=3.
```

The periodic-prefix formula gives `cn(B)=b`.  Also

```
cn(E)=cn(B)=3.                                 (2b)
```

For (2b), prefixing the initial `2` can raise the curling number by at
most one.  If it raised it, the maximizing power would consume all of
`E`; the locked/external prefix classification applied to `2Q^3`
would have either a nonempty locked tail `R...` or an external root
longer than `2n`, while the exponent is at least four and
`|E|=3n+1`.  Both are impossible.

Let `e` be the status of `E`.  If `H` and `B` have opposite statuses,
then exactly one of the following holds:

```
completion fork:  status(H) != e = status(B);
prefix seam:      status(H) = e != status(B).    (3)
```

This insertion of `E` is exhaustive because status has only the two
values bad and terminal.

## 2. Completion fork: every nontrivial root is contained

Write

```
u=cn(H).
```

Since appending one symbol raises a curling number by at most one and
`cn(C^3)=3`,

```
1<=u<=4.                                         (4)
```

For completeness, the append bound follows by deleting the new final
symbol from an `e`-power suffix: the remaining word ends in `e-1`
copies of a conjugate root, so the old curling number is at least
`e-1`.

If `u=1`, the `H` side is an immediate terminal reset.  Suppose `u>=2`,
and let `p` be any primitive maximizing root length in `H`.  Put
`g=gcd(n,p)`.  Then

```
(u-1)p+g<=n,              p<n.                   (5)
```

Indeed, delete the final `3` from the suffix `p`-power.  The resulting
factor has length `up-1` and periods `p` and `n` inside `C^3`.  If

```
up-1>=n+p-g,
```

Fine--Wilf gives period `g`.  The factor contains a complete conjugate
of `C`.  If `g<n`, this contradicts primitivity of `C`.  If `g=n`, then
`n` divides `p`; (4) and `p<=|H|/u<2n` force `p=n`.  But period `n`
would equate the final symbol `3` of `H` with the symbol `C[0]=2` one
period earlier.  Thus the threshold is not met, and its integral strict
negation is (5).

The `E` side has the primitive maximizing root `q=n`, supplied by its
suffix `B=Q^3`.  The roots `p,q` are unequal because the two completions
have distinct final symbols.  Deleting those final symbols and applying
Fine--Wilf once more gives the same contained inequality

```
(u-1)p+gcd(p,n)<=n.                              (6)
```

Thus the completion side of (3) is an immediate reset or a strict
root descent below the ambient period.  It has no external root.

## 3. Prefix seam: locked or external

Assume the prefix alternative in (3).  Run `E` and `B` in parallel
until their first unequal curling numbers.  Their states then have the
form

```
U=2 Q^3 G=Y^k,
V=  Q^3 G=U[1:],
cn(U)=k,          cn(V)=k-1,                     (7)
```

where `Y` is primitive, `r=|Y|`, and `Y[0]=2`.  The universal
prefix classification gives exactly:

```
locked:    r=n,  k>=4,  G=R(2R)^(k-4);
external:  r>2n+gcd(n,r).                        (8)
```

Both alternatives sharpen in the fixed-profile orbit.

### 3.1 Locked branch

The locked branch reaches its first mismatch at

```
k=4,             G=R.                            (9)
```

For `0<=t<n-1`, the required common output `R[t]` is generated on the
`B` side by

```
cn(Q^3 Q[:t])=max(3,R[t]).
```

Hence every symbol of `R` is at least three.  Equivalently, the
distinguished `2` is the unique occurrence of `2` in `P`.  After the
whole `R` has been appended, the two exact states are

```
U=(2R)^4,                cn(U)=4,
V=R(2R)^3,               cn(V)=3.                (10)
```

Any nominal locked exponent above four would already have encountered
the mismatch (10), so it cannot be the first mismatch.

In fact the unique-`2` conclusion is impossible in an exact proper
circular profile.  The next profile value satisfies

```
P[1]<=P[0]+1=3,
```

by the one-symbol rise argument: an attaining `e`-power at cut one,
with its final symbol deleted, ends in `e-1` copies of the corresponding
conjugate root at cut zero.
If `P[0]=2` were the unique `2`, then `min(P)=2` would give
`P[1]>=3`, hence `P[1]=3`.  Choose a proper circular cube root
`1<=r<n` ending at cut one.  The final symbol of that cube is
`P[0]=2`, so period `r` gives

```
P[-r mod n]=P[0]=2.
```

Since `0<r<n`, the phase `-r mod n` is nonzero.  This is a second
occurrence of `2`, a contradiction.  Therefore the locked branch
cannot occur.

### 3.2 External branch

The external branch has

```
k=3.                                             (11)
```

To prove this, first suppose `k>=3`.  The external inequality makes
`2r>3n+1`, so the common replay passes through `Y^(k-1)`.  Its exact
curling number is `k-1`, while the next required common output is
`Y[0]=2`; hence `k-1=2`.

It remains to exclude `k=2`.  If `r>=3n+1`, the replay passes through
the single word `Y`.  Since `V=Y^2[1:]` has curling number one and ends
in a complete copy of `Y`, one has `cn(Y)=1`, whereas the next required
output is `Y[0]=2`.

If `r<3n+1`, put

```
s=r-2n,             h=n+1-s.
```

Then `2<=s,h<=n-1`.  From `E=(2R)^3 2`, the first root copy and the
initial overlap give, with `A=(2R)[:s]` and `B_0=(2R)[s:]`,

```
Y=A B_0 A B_0 A,
suffix_(2n)(Y)=(B_0 A)^2.
```

The complete second `Y` remains a suffix of `V=Y^2[1:]`, so
`cn(V)>=2`, again contradicting `cn(V)=1`.

Consequently (11) is the only external exponent.  Its common extension
has length

```
|G|=3r-3n-1.                                    (12)
```

Because the two starting statuses are opposite, no common state before
the first mismatch can have curling number one.  Hence every symbol
replayed from `Y` below is at least two.

There are two pointed subcases.

* If `r>=3n+1`, every state `Y Y[:t]` and `Y^2Y[:t]` occurs in the
  common replay.  The first state forces a proper root realizing
  `Y[t]`; the second is long enough to expose every proper circular
  powered suffix.  Hence

  ```
  pc_Y=Y,          min(Y)=2.                     (13)
  ```

* If `r<3n+1`, the same `s,h` satisfy

  ```
  (2R)[:h]=(2R)[s:]2,
  (2R)[h-1]=2,
  (2R)[h]=max(3,(2R)[1]).                        (14)
  ```

  All phases `t>=h` obey `pc_Y(t)=Y[t]`.  At every phase, the common
  state `Y^2Y[:t]` gives `Y[t]>=2` and
  `pc_Y(t)<=Y[t]`; equality is forced whenever `Y[t]>=3`.  Thus the
  only unresolved phases before `h` are possible low holes
  `Y[t]=2, pc_Y(t)=1`.

  This branch has a further exact period restriction.  Since
  `r=2n+s`, the first root copy in `U=Y^3`, read from its known prefix
  `E=(2R)^3 2`, is

  ```
  Y=(2R)^2(2R)[:s].                               (14a)
  ```

  Removing the last symbol from the first equation in (14) gives

  ```
  (2R)[:n-s]=(2R)[s:],
  ```

  so `s` is a proper finite-word period of `2R`.  The external
  inequality also says `s>gcd(n,s)`.  Necessarily

  ```
  n<3s,             n!=2s.                       (14b)
  ```

  Indeed, if `3s<n`, the prefix of length `3s` is three copies of
  `(2R)[:s]`, and period `s` makes the following profile label equal
  to `(2R)[0]=2`; this is a cube at a cut labelled two.  If `3s=n`,
  the whole primitive word is a cube.  If `2s=n`, it is a square.
  Thus the remaining short branch has exactly one of the two
  nondivisorial period quotients

  ```
  n/2<s<n,
  n/3<s<n/2.                                      (14c)
  ```

  The possible early low holes in fact all fill.  Put `P=2R` and
  `A=P[:s]`, so (14a) is `Y=P^2A`.  For an integer
  `0<=t<h=n+1-s`, one has `t<=n-s`.  Period `s` gives

  ```
  A P[:t]=P[:s+t].                                (14d)
  ```

  At phase `t` of the circular word `Y`, use the occurrence ending
  after one complete copy of `Y` in `Y^2`.  Its preceding finite state
  is

  ```
  Y P[:t]
    =P^2 A P[:t]
    =P^2 P[:s+t].                                 (14e)
  ```

  Suppose `Y[t]=P[t]=2`.  If `t<n-s`, period `s` gives
  `P[s+t]=P[t]=2`, so exactness of `pc_P=P` supplies a proper square
  root `q<n` at phase `s+t`.  At the endpoint `t=n-s`, the source
  phase is phase zero; there `P[0]=2` supplies such a root.  The
  occurrence in (14e) is a prefix of the periodic lift of `P`; since
  `2q<2n`, that square lies wholly in (14e).  It is also a proper
  square for `Y`, because `q<n<r`.  Hence `pc_Y(t)>=2`.  The previously
  proved upper bound
  `pc_Y(t)<=Y[t]=2` gives equality.  Early phases with label at least
  three were already exact, and every phase `t>=h` was already exact.
  Therefore the short subcase also satisfies

  ```
  pc_Y=Y,          min(Y)=2.                     (14f)
  ```

  The exhaustive audit
  `research/check_short_seam_low_hole_transport.py` checks the identity
  and every transported proper square root for all binary `P` beginning
  in `2` through length fourteen.  This bounded audit is a check of the
  symbolic transport, not its proof.

### 3.3 Endpoint-rank conservation in the ordinary orientation

Assume the ordinary orientation

```
status(H)=status(E)=bad,
status(B)=terminal.                               (15)
```

Put `A=C^3` and `D=A[1:]`.  The exact local values from
`symbol_two_rotation_seam.md`, Lemma 1, give `cn(D)=2` and `D2=B`.
Thus `A` is bad, `D` is terminal, and

```
tau(D)=1+tau(B).
```

During the prefix seam, `G` is exactly the common output word from
`E,B` to `U,V`.  No proper prefix of this replay can contain a curling
number one on the `B` side, because the same output would occur on the
bad `E` side.  Hence

```
tau(B)=|G|+tau(V).
```

Using `|A|=3n`, `|E|=3n+1`, and `|U|=|E|+|G|`, one obtains the exact
conservation law

```
|A|+tau(D)
 = |E|+tau(B)
 = |U|+tau(V).                                   (16)
```

In the external branch `U=Y^3` and `V=U[1:]`.  The bad/terminal
statuses in (15) propagate along the two common orbits, so `U` is bad
and `V` is terminal.  Thus (16) is conservation of the essential
endpoint rank.

In the external branch, equation (13) in the long subcase and (14f)
in the short subcase both give `pc_Y=Y`, `min(Y)=2`; the prefix
classification gives `Y[0]=2`.  Applying
the exact symbol-two local values to `Y` shows that `Y^3[1:]` first
appends `2` to become the next rotation cube.  Therefore

```
Y^3 bad,       Y^3[1:] terminal                 (17)
```

is another ordinary phase-two cube/deletion boundary with the same
rank (16).  Every external root satisfies
`r>2n+gcd(n,r)>n`.  Consequently, among ordinary fixed-profile
boundaries of minimum rank, a maximum-period tie break excludes every
external prefix seam: it would produce the strictly longer root `Y`
at the same rank.

Equations (3)--(17) are exhaustive for a status boundary at a
symbol-two phase.  The locked branch is excluded above.  The remaining
global work in the ordinary orientation is the contained completion
fork.  The separate reverse orientation still uses its own terminal
rank and is not identified with (16).

## 4. Equal-rank external inflation is finite

Let `tau(S)` be the number of orbit appends before the first state of
curling number one.  Suppose the symbol-two boundary comes from

```
A=C^3 bad,               D=A[1:] terminal.
```

Define its pointed endpoint rank by

```
rho(A,D)=|A|+tau(D).                              (15)
```

If (3) chooses the prefix seam, then `E=A2` is bad and `B=D2` is
terminal.  Since `cn(D)=2`, `B` is the actual successor of `D`, and

```
rho(E,B)
 =|E|+tau(B)
 =3n+1+tau(B)
 =3n+tau(D)
 =rho(A,D).                                      (16)
```

Let `t=|G|` be the common-output length before the external mismatch.
Then

```
U=Y^3 bad,                V=U[1:] terminal.
```

The word `V` is reached from `B` after exactly `t` actual steps.  No
earlier common state can have curling number one, because that would
make `E` terminal.  Therefore

```
tau(B)=t+tau(V)
```

and

```
rho(U,V)
 =|U|+tau(V)
 =|E|+t+tau(V)
 =rho(E,B)
 =rho(A,D).                                      (17)
```

In both external subcases, equations (13) and (14f) make `Y` another
primitive exact profile with minimum two.  Also `Y[0]=2`, so `(U,V)`
is another ordinary rotation-cube boundary of the same type.
Its period satisfies

```
r>2n+gcd(n,r)>2n.                                (18)
```

Repeated external inflations preserve the finite integer rank `rho`,
strictly more than double the period, and obey

```
3r=|U|<=rho.                                     (19)
```

Hence only finitely many are possible; more explicitly, after `j`
inflations the period exceeds `2^j n` while it remains at most
`rho/3`.  Under the minimum-rank/maximum-period selection below, none
is possible.

There is a sharper selection consequence.  Among all ordinary
phase-two cube/deletion boundaries of this type, choose one minimizing
`rho`, and among rank minimizers choose one with maximum period length
`n`.  Every external branch produces another member of the same class:
`pc_Y=Y`, `Y[0]=min(Y)=2`, `Y^3` is bad, and `Y^3[1:]` is terminal.
Equation (17) gives the same rank, while (18) gives `|Y|>n`,
contradicting the tie break.  Therefore the selected boundary has no
external prefix seam at all.

Thus the ordinary prefix alternative is eliminated at the selected
boundary.  The contained completion fork remains.
