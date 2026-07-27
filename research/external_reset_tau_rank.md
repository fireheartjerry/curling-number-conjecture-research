# External reset timing and the sibling-tail obstruction

This note works in the all-terminal deletion branch of the reset-tower
reduction.  It separates an exact timing identity from the still unproved
local ancestry lemma.

## 1. Notation

For a finite word `W` whose orbit reaches a word of curling number one,
let

```
tau(W)=min {m>=0 : cn(orbit^m(W))=1}.
```

For a late cubic reset root `U`, put

```
p=|U|,
D_U=(U^3)[1:],
A_U=D_U 2=rot_left(U)^3,
E_U=D_U 3.
```

The reset equations give

```
cn(U^3)=3,       cn(D_U)=2,
tau(D_U)=1+tau(A_U).                              (1)
```

## 2. Exact timing across one external edge

Let `U,V` be consecutive reset roots on the same counterorbit, with
lengths `p,q`, and assume the transition is external:

```
q>3p.
```

There is no reset strictly between the endpoints `U^3` and `V^3`.
Immediately after the first endpoint, the driven deletion state is
`E_U`.  It consequently follows its autonomous orbit through all
intervening equality cuts and reaches `D_V`.

The length difference is

```
|D_V|-|E_U|=(3q-1)-3p=3(q-p)-1.
```

Therefore

```
tau(E_U)=3(q-p)-1+tau(D_V)
        =3(q-p)+tau(A_V).                         (2)
```

The same identity one edge earlier says

```
tau(E_P)=3(p-|P|)+tau(A_U).                       (3)
```

Thus the only discontinuity not accounted for by an exact linear time
shift is the sibling replacement

```
A_U=D_U 2   --->   E_U=D_U 3.                    (4)
```

## 3. Full critical fitting alone does not order the siblings

The word

```
U=223222322322232223232
```

is primitive, starts in `2`, has exact proper circular profile `pc_U=U`,
and its finite orbit emits two copies of `U` and reaches `U^3`.
Consequently all first-copy replay/fitting equations hold.  Its reset
values are the required exact values three and two.

Nevertheless, with the ordering explicitly fixed as

```
(tau(D_U 2), tau(D_U 3)),
```

executed code gives

```
(1,2).
```

The complete output words through the first one are respectively

```
3,1
3,2,1.
```

Hence

```
tau(E_U)>tau(A_U).                                (5)
```

This is not a generic common-prefix example: it satisfies the complete
critical circular and finite replay equations.  What it lacks is literal
external ancestry.  There is no `p>=1` for which it begins `P^3 3` with
`P=U[:p]`.

All values in this section are recomputed by both implementations in
`curling.py` in `check_external_reset_tau_rank.py`.

## 4. The first surviving ancestry hypothesis

The exact external-created configuration has more than critical fitting.
For a primitive earlier root `P`, it has

```
U begins P^3 3,                                   (6)
```

the prefix `P^3 3` is an actual orbit state, every following symbol up to
`U` is its actual curling-number output, and the deleted state

```
(P^3)[1:]3
```

autonomously generates `A_U`.  The latter assertion records that there is
no intervening reset.

Literal (6) is already load-bearing.  Exhaustive SAT enumeration of
binary critical roots through length 60 found six marker-bearing models,
all rotations of the length-21 word.  In every one, executed code gives

```
cn(E_U)=2,       cn(E_U 2)=1.                     (7)
```

Their sibling-tail pairs, always ordered `(tau(A_U),tau(E_U))`, are

```
(60,1), (7,1), (5,1), (3,1), (11,1), (3,1).
```

This is a finite check, not a proof of (7).

A length-140 partial SAT model beginning in the length-21 marker violates
the desired sibling order:

```
(tau(A_U),tau(E_U))=(1,2).
```

It is not an exact counterexample.  Equations were imposed only through
cut 64, and the very first omitted cut fails: at cut 65 its prescribed
symbol is three while its exact proper-circular and first-copy-fitting
values are both one.  Thus partial marker ancestry is insufficient, while
the next actual-orbit equation removes this particular model.

Actual parent-orbit ancestry, without the complete child replay equations,
is also insufficient.  Let

```
P=223232223222322322232.
```

This is an exact critical length-21 rotation.  The high state `P^3 3` and
its first-symbol deletion emit the same actual 16-symbol word

```
2223222322322232.
```

Set

```
U=P^3 3 2223222322322232.
```

Executed code gives `|U|=80`; `U` is primitive and has the static endpoint
values `cn(U^3)=3`, `cn((U^3)[1:])=2`.  Nevertheless its sibling pair is

```
(tau(A_U),tau(E_U))=(7,10),
```

and `cn(E_U 2)=2`.  It is not an exact external child: the first child
replay/profile equation fails at phase 38, where the prescribed symbol is
two but the exact value is three, with unique root length 21.  Thus this
model satisfies the actual parent continuation but fails child
criticality at one explicit parent-scale cube.

At its pointed `E_U 2` state, the maximizing square roots have lengths
two and 17.  Their internal `3,2` markers occur at phases 78 and 63, with
incoming cube-root sets `{1}` and `{21}`, respectively.  The second marker
is exactly the externally appended parent marker `3|P|=63`.  This realizes
both scales in the Case-II normal form of Section 7.

## 5. Why the local `2,1` statement would close the external branch

Assume (7) for an externally created critical root `U`, and suppose an
outgoing external edge exists.

Put

```
C=U^3 3,       E=C[1:].
```

At the first cut after the `U` reset, (7) gives `cn(E)=2`.
The undeleted value is either two or three by the one-symbol prefix
inequality.  It cannot be three: a difference `3` versus `2` is itself a
reset, so the whole word `C` would be a primitive cube, whereas

```
|C|=3|U|+1
```

is not divisible by three.  Hence both sides append two.

Now put

```
H=U^3 3 2.
```

Its deletion is `E2`, whose curling number is one by (7).  Since the high
orbit is assumed to avoid one, the one-symbol prefix inequality forces a
reset of values two versus one.  Hence `H` would be a whole square.

This is impossible directly.  Write `n=|U|` and

```
r=|H|/2=(3n+2)/2.
```

The square assumption first forces `n` even.  Its prefix `U^3`, of length
`3n`, has periods `n` and `r`.  If `g=gcd(n,r)`, then

```
g=gcd(n,n/2+1)<=2
```

and

```
3n >= n+r-g.
```

Fine--Wilf gives period `g` to `U^3`, hence to `U`.  Literal ancestry
gives `n>=4`, so `g<n`, contradicting primitivity.

Therefore (7) would exclude every outgoing external transition.

## 6. Exact remaining gap

The load-bearing unproved statement is:

> If `U` is a late critical cubic reset root created by an actual external
> transition from a critical parent `P`—including all prefix-orbit and
> deleted-orbit coupling equations—then
> `cn((U^3)[1:]3)=2` and
> `cn((U^3)[1:]32)=1`.

Proper-circular fixedness and full first-copy fitting do not imply this,
by Section 3.  A literal marker plus finitely many subsequent equations
does not imply it, by the length-140 near-model.  Actual parent continuation
without child criticality does not imply it, by the length-80 model above.
No exact counterexample satisfying both complete child criticality and all
external-ancestry equations is currently known.

## 7. Minimal failure normal forms under an outgoing external edge

There is a useful exact split of a failure of the local statement.  Assume
that `U` has an outgoing external edge, so there is no reset immediately
after the `U^3` endpoint.  Put

```
n=|U|,       C=U^3 3,       E=C[1:].
```

The high and deleted values at this cut agree.  The first
post-promotion-root bound gives `cn(C)<=3`, so there are two cases.

### Case I: the common value is three

Choose a primitive maximizing cube root `Z` of `E`, of length `r`.
The same suffix is present in `C`.  The post-promotion bound gives

```
r<n/2.
```

Writing indices modulo `n`, direct comparison of the three root blocks
gives

```
Z=U[n-r+1:n] 3,
U[n-r]=U[n-2r]=3.                                (8)
```

Thus the artificial marker has a parent marker at phase

```
t=n-r.
```

Since `pc_U(t)=3`, choose a primitive incoming cube root of length `rho`
at that phase.  If `r>=3rho+1`, the equality of the last two `Z` blocks
copies that entire incoming cube to the cut immediately before the
artificial `3`.  That cut is phase zero of `U`, whose exact proper
circular value is two.  Hence

```
r<=3rho.                                         (9)
```

The equality case is the sharp shorter deletion-critical cube described
by the marker-ancestry normalization.  Inequality (9) alone is not a
descent because `rho` may be at least `r/3`.

### Case II: the first common value is two, but the next deleted value
is not one

Put

```
G=E2=(U^3)[1:]32.
```

No reset means that the undeleted state `U^3 32` has the same value as
`G`.  Choose a primitive maximizing root of `G`, of length `r`.  The
post-promotion escape theorem, applied to the actual two-symbol history
`3,2`, gives

```
2<=r<n.
```

The last root block ends in `32`.  Equality with the preceding block
therefore gives the pointed internal marker

```
U[n-r:n-r+2]=32.                                 (10)
```

Again put `t=n-r` and choose a primitive incoming cube root of length
`rho` at the exact three-cut `t`.  If

```
r>=3rho+2,
```

translation by the terminal square period copies the whole incoming cube
to the cut immediately before the artificial `3`.  This would give
`cn(D_U)>=3`, contrary to the reset equation `cn(D_U)=2`.  Consequently

```
r<=3rho+1.                                       (11)
```

The additive one in (11) is real: the copied square block ends two
symbols after its parent three-cut, so `r=3rho` or `3rho+1` does not copy
the complete incoming cube.

Equations (8)--(11) are the minimal first-failure classification.  Case I
is a cube-marker parent edge; Case II is a pointed `3,2` square-parent
edge.  Both retain a root scale comparable to the incoming cube scale.
Eliminating an unbounded alternation of these two geometries is exactly
what is still missing from the local `2,1` lemma.

## 8. A distinguished phase-lock macro is impossible

One exact subcase of Case II can be eliminated.  Let `P` be a primitive
word of length `p`, with `P[0]=2`.  Assume that phase `h`, `0<h<p`, of
the circular word `P` has an `h`-root cube.

The usual proper-period bound first gives

```
2h+gcd(p,h)<p.                                    (12)
```

Indeed, otherwise the length-`3h` cube, which also lies in the
`p`-periodic circular lift, meets the Fine--Wilf threshold
`p+h-gcd(p,h)` and gives a complete conjugate of primitive `P` a proper
gcd period.  In particular `2h<p`.

Write

```
A=P[:h],       M=P[h:p-h],       B=P[p-h:p].
```

The three consecutive length-`h` blocks ending at phase `h` are

```
P[p-2h:p-h],       B,       A.
```

The cube equation makes all three equal.  In particular

```
B=A,
P[p-2h:p]=AA,
P=AMA.                                             (13)
```

Now suppose a proposed child root phase-locks to the suffix of `P`:

```
U=P^3 P[h:p].
```

At child phase

```
j=2p-h,
```

the circular length-`3p` suffix is

```
P[p-2h:p] P[h:p] P P[:p-h].
```

Using (13), this word is

```
AA MA AMA AM = (AAM)^3.                            (14)
```

Thus a proper root of length `p` gives a cube at phase `j` of `U`.
But

```
U[j]=P[p-h]=B[0]=A[0]=P[0]=2.                     (15)
```

Equations (14)--(15) contradict `pc_U(j)=U[j]`.  Therefore such a
phase-locked child cannot be critical.

The executed length-80 ancestry model in Section 4 is exactly this macro:
`p=21`, `h=4`, and the contradiction is the unique root-21 cube at child
phase 38.  The unresolved variants are those in which the post-promotion
phase and the incoming cube-root length are unequal, the phase lock crosses
the end of `P`, or the terminal pointed square has a scale different from
the length of the locked suffix.

There is also a shorter formulation which covers two alignments.  Suppose
the incoming cube at phase `h` has root length `rho`.

* If `h=rho`, its last two root blocks give
  `P[-rho:]=P[:rho]`.  This is the seam match (16) with
  `ell=rho`, and it lands at phase zero, labelled two.
* If `h=2rho`, its three root blocks give
  `P[-rho:]=P[:rho]=P[rho:2rho]`.  The match with
  `ell=rho` lands at phase `rho`; block equality makes
  `P[rho]=P[0]=2`.

Thus a suffix-phase-locked critical child is impossible whenever its
distinguished parent marker lies one or two incoming cube-root lengths
from the parent origin.  Section 8 is the first alignment `h=rho`; its
longer `ell=2h` calculation identifies an additional earlier forbidden
phase.

## 9. General backward-seam exclusion for a phase-locked child

The previous macro is a special case of a simpler seam statement.  Let
`P` have length `p`, let `0<h<p`, and put

```
U=P^3 P[h:p],       n=|U|=4p-h.
```

At the seam where the suffix `P[h:p]` begins, the right-infinite word is

```
P[h:p] P^3 = (P[h:p]P[:h])^3 P[h:p].
```

Consequently a `p`-root cube starts at the seam and ends, in the circular
child, at phase

```
j_0=2p+h.
```

Now fix `ell`, `0<=ell<p`, for which the two parent histories at phases
zero and `h` have a common length-`ell` suffix:

```
P[p-ell:p]=P^Z[h-ell:h].                         (16)
```

Equation (16) extends the cube across the seam by `ell` symbols to the
left.  Hence child phase

```
j=2p+h-ell
```

ends in a proper cube of root length `p`.  The prescribed child symbol at
that phase is

```
U[j]=P[(h-ell) mod p].                            (17)
```

It follows that a critical child must satisfy

```
P[(h-ell) mod p]=3
```

for every `ell` obeying (16).  Any matched backward seam that lands on a
two-phase rules out the child.

For example, the one-symbol condition

```
P[-1]=P[h-1]=2
```

uses `ell=1` and already gives a contradiction.  Section 8 uses
`ell=2h`; its incoming `h`-root cube supplies (16), and (13) makes the
landing phase a two.

In particular, if `P[-1]=2`, any phase-locked child that survives this
test must have

```
P[h-1]=P[h]=3.
```

Thus the selected marker belongs to an adjacent-`33` component.  The
bridge/separation alternatives in `adjacent_double_bridge.md` then apply;
the seam lemma removes the isolated-marker branch outright for a
parent ending in two.

This lemma is independent of how the phase lock was discovered.  To use it
globally, one still has to prove that an actual external continuation
contains a suffix-phase lock `P[h:p]`, or replace exact locking by the
first-defect normal form from `critical_seed_induction.md`.
