# The contained completion fork: periodic shadow and status square

This note starts from the sole ordinary symbol-two branch left in
`symbol_two_status_seam.md`.  It gives two exact reductions.  The first
turns a promoted cube root into a pointed periodic run inside the fixed
profile.  The second turns the bad/terminal completion fork into either a
strict terminal-tail delay or a shorter completion defect.  The shorter
defect can terminate at a reverse-status boundary, so the reductions do
not yet close the conjecture.

The literature search already recorded in `literature_search_log.md`,
section *Two-sided completion at the symbol-two rotation seam*, found no
published theorem for this completion square.  The word arguments below
use only Fine--Wilf and the previously proved exact local values.

## 1. Setup

Let `C=2R` be a primitive word of length `n` with

```
pc_C=C,                 min(C)=2.
```

Put

```
A=C^3=2D,
Q=R2,
B=D2=Q^3,
H=A3=2F,
E=A2=2B,
F=D3.                                                   (1)
```

In the ordinary completion fork the known statuses are

```
A,H are bad,
D,E,B are terminal.                                    (2)
```

Write `u=cn(H)`.  The preceding symbol-two analysis gives

```
u in {2,3}.                                             (3)
```

Choose a primitive maximizing root of `H` of length `p`.  Then

```
p<n,
(u-1)p+gcd(n,p)<=n.                                    (4)
```

## 2. The exact periodic shadow

Work in the periodic lift of `C`, with the distinguished low cut at
coordinate zero.  Let

```
V=C[1-p:0],                 |V|=p-1,
T=V3.                                                   (5)
```

The final root of the maximizing power in `H` is exactly `T`.  Hence

```
H ends in (V3)^u,
C^3 ends in (V3)^(u-1)V.                               (6)
```

Deleting the initial `V` of the second word in (6) gives the literal
identity

```
C^3 ends in (3V)^(u-1).                                (7)
```

Thus the promoted root leaves an `(u-1)`-power shadow at the original
low cut.  Since that cut has exact proper circular value two, (7) gives
another direct proof of `u<=3`.

### Lemma 1 (the cubic shadow is a maximal pointed run)

If `u=3`, put

```
x=C[-3p].
```

Then

```
C[-3p:0]=x V (3V)^2,          x!=3,                 (8)
```

and the interval

```
[1-3p,0)
```

is a maximal period-`p` run.  Its right and left failed continuation
symbols are respectively `2` and `x`, while the period would require
`3` at both places.

#### Proof

Equation (6) with `u=3` gives

```
C[1-3p:0]=(V3)^2V=V(3V)^2.
```

If `x=3`, then the final length `3p` factor before cut zero would be

```
(3V)^3,
```

contradicting `pc_C(0)=2`.  Thus `x!=3`.  At the right endpoint the
periodic continuation is also `3`, whereas `C[0]=2`.  These two failed
comparisons prove maximality of the displayed period-`p` interval.

The root `3V` is primitive because it is conjugate to the selected
primitive root `V3`.

### Lemma 2 (the internal high has a separated cube scale)

Retain `u=3`.  The middle cut of the square `(3V)^2` is cut `-p`, and

```
C[-p]=3.                                              (9)
```

Let `q` be any primitive cube-root length attaining the exact value
three at that cut, and put `g=gcd(p,q)`.  Then `q!=p` and exactly one of

```
q<p:       2q+g<p,                                    (10a)
q>p:       p+g<=q                                     (10b)
```

holds.

#### Proof

The period-`p` run in Lemma 1 and the `q`-cube ending at cut `-p`
overlap in

```
L=min(2p-1,3q)
```

symbols.  If `q=p`, the overlap has at least one complete root and the
two period-`p` factors merge.  Their union contains a period-`p` cube
ending at cut zero, contradicting its exact value two.

Suppose `q!=p`.  If

```
L>=p+q-g,
```

Fine--Wilf gives period `g` on an overlap containing a complete
conjugate of the longer primitive root.  This gives that root a proper
period, a contradiction.  Therefore

```
min(2p-1,3q)<p+q-g.                                  (11)
```

For `q<p`, the factor `2p-1` already reaches the Fine--Wilf threshold,
so (11) forces

```
3q<p+q-g,
```

which is (10a).  For `q>p`, the factor `3q` reaches the threshold, so
(11) forces

```
2p-1<p+q-g,
```

whose integral form is (10b).

Lemma 2 identifies the exact existing obstruction: the descending
branch more than halves, while the ascending branch is a genuine
cap-ascent and can revisit a previous scale through the shallow geometry
already isolated in `circular_low_hole_transition.md`.

## 3. The commutative status square

### Lemma 3 (deleting the leading two preserves the immediate value)

With (1)--(4),

```
cn(F)=cn(H)=u.                                        (12)
```

#### Proof

Every powered suffix of `F` is also a powered suffix of `H=2F`, so
`cn(F)<=u`.  Conversely the selected `u`-power in `H` has length

```
up<=3(n-1)<3n=|F|.
```

It therefore lies wholly in `F`, giving `cn(F)>=u`.

The unknown status of `F` gives the exhaustive square

```
                completion 3       completion 2
with prefix 2:  H bad              E terminal
without prefix: F ?                B terminal.        (13)
```

There are exactly two cases.

1. If `F` is terminal, then `H=2F` is another essential
   bad/terminal deletion pair.  Its endpoint rank relative to `A,D` is

   ```
   R(H,F)-R(A,D)=1+tau(F)-tau(D).                    (14)
   ```

   If `A,D` was selected by globally minimum deleted hitting time and
   `tau(F)=tau(D)`, the minimum-hitting-time immediate-divergence lemma
   would require `cn(H)!=cn(F)`, contradicting (12).  Under that
   selection one therefore has

   ```
   tau(F)>tau(D).                                    (15)
   ```

2. If `F` is bad, deletion of the common leading `2` propagates the
   same completion fork one symbol to the left:

   ```
   D3=F bad,             D2=B terminal.             (16)
   ```

Thus the contained root drop is not by itself a same-rank bad reset.
It either injects terminal hitting time or moves the completion defect
left.

### Lemma 4 (a terminal bottom-left corner inflates to a larger exact profile)

Assume the first case of the status square:

```
H=2F is bad,                 F is terminal.          (17)
```

Run the two autonomous orbits together until their first unequal
curling numbers.  If `G` is their common output before that cut, put

```
U=H G=Y^k,                  V=F G=U[1:],             (18)
```

where `Y` is primitive and `r=|Y|`.  Then

```
k=3,
r>2n+gcd(n,r),
pc_Y=Y,
Y[0]=min(Y)=2.                                      (19)
```

Consequently `(U,V)` is a new ordinary phase-two cube/deletion
boundary,

```
U=Y^3 bad,                  V=(Y^3)[1:] terminal,    (20)
```

and its endpoint rank is exactly the endpoint rank of `(H,F)`:

```
|H|+tau(F)=3r+tau(V).                               (21)
```

#### Proof: first mismatch and exclusion of the locked scales

The first unequal cut exists because the two statuses in (17) differ.
Since `V` is a suffix of `U`, the one-symbol prefix theorem gives

```
cn(U)=k,                    cn(V)=k-1,
```

and the maximizing `k`-power must occupy all of `U`; otherwise it
would remain a suffix of `V`.  This proves the form (18).

The factor `C^3` at the beginning of `U` has periods `n` and `r`.
Put `g=gcd(n,r)`.  If `r<=2n+g`, its length `3n` reaches the
Fine--Wilf threshold `n+r-g`.  Fine--Wilf then gives period `g` to
`C^3`.  Primitivity of `C` forces `g=n`, so `n` divides `r`; the
assumed bound leaves only

```
r=n,                       r=2n,                  r=3n.
```

For `r=2n` or `r=3n`, the first root block `Y` is respectively
`C^2` or `C^3`, contrary to primitivity of `Y`.  For `r=n`, the first
three copies of `Y` are `C^3`, so the next symbol required by the
period is `C[0]=2`; the actual symbol in `H=C^3 3` is `3`.  Thus none
of the three scales is possible, and

```
r>2n+g.                                             (22)
```

#### Proof: the mismatch exponent is three

Suppose first that `k=2`.  Then `cn(V)=1`.

If `r>=3n+1=|H|`, the common evolution reaches the state `Y` before
the mismatch at `Y^2`.  Its next common output is the first symbol
`Y[0]=H[0]=2`, so `cn(Y)=2`.  But `V=(Y^2)[1:]` has a complete copy
of `Y` as a suffix, giving `cn(V)>=cn(Y)=2`, a contradiction.

It remains to consider `r<3n+1`.  Write

```
r=2n+s.
```

Equation (22) gives `s>=1`.  The bound `r<3n+1` gives `s<=n`.
The equality `s=n` would make the first root `Y=C^3`, which is
imprimitive.  Hence `1<=s<n`.  Put

```
L=C[:s],                    M=C[s:].
```

The first `r` symbols of `U` give

```
Y=C^2L=LMLML.
```

Therefore `Y` ends in

```
MLML=(ML)^2,
```

so `cn(Y)>=2`.  The complete final copy of `Y` in `V` again gives
`cn(V)>=2`, contradicting `cn(V)=1`.  Thus `k>=3`.

The state `T=Y^(k-1)` occurs after the initial prefix because
`|T|>=2r>3n+1`.  It is also a suffix of `V`, whose exact value is
`k-1`.  Hence

```
cn(T)=k-1.
```

The next common output is `Y[0]=2`, so `k-1=2` and `k=3`.

#### Proof: inheritance of the complete profile

For `0<=t<r`, the common orbit visits

```
J_t=Y^2Y[:t]
```

before the mismatch at `Y^3`, and therefore

```
cn(J_t)=Y[t].                                       (23)
```

The displayed state ends in two copies of the rotation of `Y` at
phase `t`, so (23) gives `Y[t]>=2`.

Every proper circular powered suffix of the primitive word `Y` has
powered length strictly below `2r`: otherwise Fine--Wilf with periods
`r` and its proper root would give a proper period to a complete
conjugate of `Y`.  Such a suffix is visible in `J_t`.  Equation (23)
therefore gives

```
pc_Y(t)<=Y[t].                                      (24)
```

If `Y[t]>=3`, a maximizing root in `J_t` has length at most

```
(2r+t)/Y[t] < r,
```

so it is a proper circular root and (24) is an equality.

It remains to supply proper squares at phases with `Y[t]=2`.  If
`r>=3n+1`, the common evolution visits

```
K_t=Y Y[:t]
```

for every `t`.  Its maximizing square root has length at most
`(r+t)/2<r`, so it is proper and gives `pc_Y(t)>=2`.

Suppose instead that `r=2n+s<3n+1` and put

```
h=3n+1-r=n+1-s.
```

The prefix equality between `U=Y^3` and `H=C^3 3`, after cancelling
the first `C^2`, is

```
C[:s] C[:h]=C 3.
```

Cancelling the prefix `C[:s]` gives

```
C[:h]=C[s:]3.                                      (25)
```

Removing the last symbol from (25) gives

```
C[:n-s]=C[s:],
```

so `s` is a finite-word period of `C`.  The common orbit visits
`K_t` for every `t>=h`; the preceding argument supplies a proper
square at every such low phase.

For `0<=t<h`, one has `t<=n-s`, and period `s` gives

```
C[:s]C[:t]=C[:s+t].
```

Since `Y=C^2C[:s]` and `Y[:t]=C[:t]`,

```
K_t=Y Y[:t]=C^2C[:s+t].                           (26)
```

If `t<n-s` and `Y[t]=C[t]=2`, the period equation gives
`C[s+t]=C[t]=2`.  Exactness of `pc_C=C` supplies a proper square
root `q<n` at phase `s+t`.  Its powered length is below `2n`, so the
same square lies wholly in the displayed periodic prefix (26).  At
the endpoint `t=n-s`, the source is phase zero; `C[0]=2` supplies
the proper square, and (26) is `C^3`.  In every case
`q<n<r`, so the transported square is proper for `Y`.

Thus every low phase has `pc_Y(t)>=2`; together with (24) and the
high-phase equality, this proves `pc_Y=Y` and
`Y[0]=min(Y)=2`.

Finally, let `delta=|G|`.  The terminal orbit from `F` takes exactly
`delta` common steps to reach `V`, so

```
tau(F)=delta+tau(V).
```

Also `|U|=|H|+delta=3r`.  Substitution gives (21).

Lemma 4 is a transition, not a closure.  Under the minimum endpoint
rank used for `(A,D)`, (12) and the maximum-length tie break imply that
the terminal-`F` pair has a strictly larger rank than `(A,D)`.
Equation (21) preserves that new rank while increasing the profile
period by more than a factor two.  It therefore does not justify a
maximum-period contradiction at the original rank; an infinite tower
may move through strictly larger ranks.

## 4. Exhaustive endpoint of repeated left propagation

Let

```
X_i=A[i:],          U_i=X_i3,          V_i=X_i2
```

for `0<=i<=|A|`.  The initial status pair is

```
(status(U_0),status(V_0))=(bad,terminal),
```

while `U_|A|=(3)` and `V_|A|=(2)` are both terminal.  Let `j>=1` be
the first index at which the status pair is not `(bad,terminal)`.
Write

```
X_(j-1)=a X_j.
```

Then at least one of the following holds:

```
U_(j-1)=a U_j is bad and U_j is terminal;          (17a)
V_(j-1)=a V_j is terminal and V_j is bad.          (17b)
```

This enumeration is exhaustive: failure of `(bad,terminal)` says
either that its first coordinate became terminal or that its second
coordinate became bad.

The first alternative is a forward essential boundary.  If `A,D`
minimizes the global endpoint rank

```
rho=3n+tau(D),
```

then its depth gives the exact lower bound

```
tau(U_j)>=tau(D)+j-2,                               (18)
```

because

```
|U_(j-1)|=3n-j+2
```

and `|U_(j-1)|+tau(U_j)>=rho`.

The second alternative is a reverse terminal-prefix/bad-suffix
boundary.  Its natural rank is the separate reverse rank from
`reverse_status_reset.md`; no proved comparison turns (17b) into a
contradiction with (18).  This is the exact endpoint of the
left-propagation argument.

## 5. The delayed `32/23` defect when `u=2`

If `u=2`, the first two actual successors on the bad side and the
corresponding terminal successors are

```
H=A3          -> J=A32                 (bad),
E=A2          -> E3=A23                (terminal),
D -> B=D2     -> B3=D23                (terminal).   (19)
```

Deleting the common leading `2` from the first pair in (19) gives

```
J[1:]=D32,
(E3)[1:]=D23=B3.                                  (20)
```

Hence exactly one of the following occurs:

```
D32 is terminal, so J=2(D32) is essential;
D32 is bad, so the surviving defect is
    D32 bad / D23 terminal.                        (21)
```

Because `D -> B -> B3` is an actual two-step terminal orbit segment,

```
tau(B3)=tau(D)-2.                                  (22)
```

If `A,D` has minimum endpoint rank and maximum length among its rank
minimizers, the terminal case of (21) satisfies

```
tau(D32)>=tau(D)-1=tau(B3)+1.                      (23)
```

Indeed endpoint minimality first gives
`tau(D32)>=tau(D)-2`; equality would make the longer essential word
`J` have the same endpoint rank as `A`, contradicting the length
tie-break.

Thus the `u=2` branch also has an exact alternative: a strict
terminal-tail delay, or an adjacent transposition defect `32/23`.
The latter is not a one-letter completion pair and is the additional
load left by the square case.

## 6. The periodic provenance alone does not order the two terminal tails

No comparison between `tau(D3)` and `tau(D2)` follows from the static
conditions

```
D=(C^3)[1:],       C primitive,       pc_C=C,       C[0]=2.
```

The calibrated Q21 audit realizes both strict orientations.  Its most
separated rows are

```
tau(D3)-tau(D2)=52,
tau(D3)-tau(D2)=-59.
```

Every orbit step in this audit is recomputed by both curling-number
implementations in `research/check_contained_completion_shadow.py`.
These finite examples are not hypothetical completion forks—the promoted
words terminate—so they do not exclude an inequality which uses the
additional load-bearing assumption that `C^3 3` is bad.  They do exclude
any rank argument based only on the periodic form of `D` and the exact
circular profile.

## 7. The exact status-sensitive comparison that does survive

Assume the terminal branch of the commutative square:

```
H=A3=2F is bad,             F=D3 is terminal,
B=D2 is terminal.
```

The actual first terminal step `D -> B` gives

```
tau(B)=tau(D)-1.                                    (27)
```

There are two useful normalizations of the original essential pair
`(A,D)`.

### Endpoint-rank normalization

Suppose `(A,D)` minimizes

```
R(A,D)=|A|+tau(D)
```

over all essential deletion pairs, with maximum bad-word length among
the minimizers.  Since `(H,F)` is also essential and `|H|=|A|+1`,
minimality followed by the length tie-break gives

```
|H|+tau(F) > |A|+tau(D).
```

All quantities are integers, so

```
tau(F)>=tau(D)=tau(B)+1.                           (28)
```

In particular the badness of `H`, together with terminality of `F` and
the global endpoint selection, forces the strict comparison
`tau(F)>tau(B)`.  The Q21 timing rows in Section 6 do not contradict
(28), because their promoted `H` words are terminal and hence are not
eligible essential competitors.

### Deleted-hitting-time normalization

Suppose instead `(A,D)` is selected with globally minimum `tau(D)`.
The essential competitor `(H,F)` first gives

```
tau(F)>=tau(D).
```

Equality would make `(H,F)` another minimum-hitting-time pair.  Lemma 1
of `minimal_deleted_hitting_time.md`, applied to that pair, would then
give `cn(H)!=cn(F)`, contrary to (12).  Therefore

```
tau(F)>=tau(D)+1=tau(B)+2.                         (29)
```

These derivations are lower bounds only; they do not yield an upper
bound on `tau(F)` in terms of `tau(B)`.  Lemma 4 instead transports the
larger terminal delay exactly to the inflated cube boundary
`(Y^3,(Y^3)[1:])`.
