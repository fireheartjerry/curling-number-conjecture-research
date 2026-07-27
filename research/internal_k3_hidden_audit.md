# Consecutive internal cubic resets

This note independently audits the internal alternative in
`reset_root_transition_split.md`.  It assumes two consecutive late reset
roots

```
U, V,
|U|=p,
V=U^2 U[:h],
p/3<h<p,
h is a period of U,
U[p-h]=3,
U[0]=2,
pc_U=U,
pc_V=V,
```

with `U,V` primitive.  These hypotheses are consequences of the late
internal `k=3` branch.  No termination conclusion is assumed.

## 1. Exact Euclidean split

Put

```
p=m h+r,       0<=r<h.
```

The strict inequalities `p/3<h<p` give `m in {1,2}`.  The equality
`r=0` is impossible: period `h` would then make `U` a nontrivial
integral power.  Thus `0<r<h`.

Let

```
A=U[:r],       B=U[r:h].
```

Both words are nonempty.  Period `h` gives exactly one of the following
two forms.

```
m=1:  U=A B A,          h>p/2,          U[p-h]=B[0]=3;
m=2:  U=A B A B A,      p/3<h<p/2,      U[p-h]=B[0]=3.
```

In both cases `A[0]=U[0]=2`.  The equality case `h=p/2` belongs to
`r=0` and was already excluded; no divisibility endpoint is omitted.

## 2. The five-block branch is impossible

Assume the second form and put

```
C=A B,       |C|=h.
```

Then

```
U=C^2 A,
V=U^2 C=C^2 A C^2 A C.
```

Consider cut `2h` of the circular word `V`.  The length-`h` block
immediately before cut zero is the terminal displayed `C`, while the
first `2h` symbols of `V` are `C^2`.  Hence the length-`3h` factor
ending at cut `2h` is

```
C^3.
```

Its root length `h` is proper because `h<|V|`.  On the other hand,

```
V[2h]=A[0]=2.
```

Thus `pc_V(2h)>=3` while fixedness requires
`pc_V(2h)=V[2h]=2`, a contradiction.  Therefore every late internal
transition that can be followed by a fixed-profile root has the sole
remaining form

```
U=A B A,
V=A B A A B A A B.
```

Equivalently, with

```
C=A B,       |A|=a,       |C|=h,       p=h+a,
```

one has

```
U=C A,
V=C A C A C,             |V|=3p-a.       (1)
```

Here `0<a<h`, `A[0]=2`, and `B[0]=3`.

## 3. The next internal defect is a strict border of `C`

Suppose the next transition after (1) is internal as well.  Write

```
q=|V|=3p-a,
H=q-d,
```

where `H` is the next internal period and `d` its border length.  The
transition equations give

```
V[0:d]=V[H:q],              V[d]=3.       (2)
```

The five-block branch has just been excluded, so the next transition
also lies in the three-block branch and `H>q/2`.

The word `V` has period `p`.  Apply Fine--Wilf to its periods `p` and
`H`.  If the threshold were met and
`gcd(p,H)<p`, a complete copy of primitive `U` inside `V` would acquire
that smaller period.  If `gcd(p,H)=p`, then

```
p<H<q<3p
```

forces `H=2p`.  In that case `d=q-2p=h`, and the pointed equation in
(2) would read

```
3=V[h]=A[0]=2.
```

Thus the threshold must fail.  In particular,

```
d<p.                                             (3)
```

The case `d=h` is excluded by the same displayed symbol mismatch.
Suppose `h<d<p` and put `c=d-h`, so `0<c<a`.  Let

```
P=A[:c],       S=A[a-c:a].
```

The border equation (2), read in `V=C A C A C`, is

```
C P=S C.                                         (4)
```

Write `A=R S`, where `|R|=a-c`.  Comparing the first `a` symbols of
(4), and using that `C` begins in `A`, gives

```
R S=S R.                                         (5)
```

By the commuting-words theorem, `R` and `S` are powers of one primitive
word.  Hence the prefix of `A` of length `c` equals its suffix of length
`c`, so `P=S`.  Equation (4) becomes

```
C S=S C.
```

The same theorem now makes both `C` and `A` powers of the primitive root
of `S`.  Therefore `U=C A` is a nontrivial power, contradicting its
primitivity.  Hence `d>h` is impossible.

It follows that

```
0<d<h.
```

Now (2) reads

```
C[:d]=C[h-d:h].
```

Thus `d` is a proper border length of the strictly shorter word `C`.
The pointed equation remains

```
C[d]=3.                                          (6)
```

Finally `d!=a`.  If `d=a`, the border equation says that `C` ends in
`A`.  At cut zero of `V`, the preceding length-`3p` factor is then

```
A V=A C A C A C=(A C)^3.
```

This is a proper cube because `p<q`, but the cut has label
`V[0]=2`, contradicting `pc_V=V`.

Consequently every pair of consecutive surviving internal transitions
has the strict quotient

```
d is a border of C=U[:h],
0<d<h<p,
d!=p-h,
C[d]=3.                                          (7)
```

Equation (7) is stronger than the raw scale gap.  It does not yet give
a monotone sequence of defect lengths: `d` may lie on either side of
the previous defect `a=p-h`.  A final argument must use the fixed-profile
power at the new `3`-cut, or show that iterating these unequal pointed
borders forces a period of the ambient root.

## 4. Cube-root scale at the next pointed defect

The two orientations in (7) have different root geometry.  Let `R^3`
be a primitive cube supplied by `pc_V(d)=V[d]=3`, and put

```
r=|R|,       delta=|d-a|,       g=gcd(p,r).
```

In the lift of `V^Z` with cut zero at the distinguished origin, the
inherited `p`-root cube is the exact interval

```
I=[-q,a),
```

because `V A=U^3`.  The new cube is

```
J=[d-3r,d).
```

The proper-power span bound for primitive `V` gives

```
2r+gcd(q,r)<q,
```

and in particular `r<q/2<3p/2`.

If `d<a`, then

```
r=p,       or       2r+g<p.                     (8)
```

Indeed, `r>p` makes `I` and `J` overlap in length
`3p-delta`.  Here `delta<a<p/2`, while `r<3p/2`, so the overlap meets
the Fine--Wilf threshold `p+r-g`; a complete conjugate of primitive
`U` would acquire period `g<p`.  Thus `r>p` is impossible.

For `r<p`, either `J` is contained in `I`, or its left endpoint lies
before that of `I`.  The latter overlap has length `3p-delta` and again
meets the threshold.  In the contained case the overlap is all of
`J`, of length `3r`; threshold failure is exactly

```
2r+g<p.
```

The remaining equality `r=p` can extend the inherited run to the left
and is not excluded by this argument.

If `d>a`, then

```
r<p,       2r+g<p+d-a.                          (9)
```

For `r>p`, the overlap length is

```
min(3p,3r-(d-a)).
```

If the minimum is `3p`, it exceeds the Fine--Wilf threshold because
`r<3p/2`.  If the minimum is the second term, then

```
2r+g>p+(d-a)
```

follows from `r>p` and `d-a<p`, so the threshold is again met.
Both alternatives contradict primitivity of `U`.

The equality `r=p` is also impossible.  The two `p`-periodic cubes
overlap in more than two complete roots, so their union is
`p`-periodic.  Extending the inherited cube from cut `a` toward cut
`d` would force

```
V[a]=V[a-p]=U[0]=2,
```

whereas the pointed old delimiter gives `V[a]=3`.

Finally take `r<p`.  If `3r<=d-a`, the new cube does not reach `I` and
(9) follows directly from `g<=r`.  Otherwise their overlap has length
`3r-(d-a)`.  Meeting the Fine--Wilf threshold would contradict
primitivity, so its strict failure is precisely (9).

Thus an upward defect move `a -> d` forces the new cube root below
one half of the old reset scale, up to the bounded additive defect.
A downward move has the same strict half-scale branch plus one
exceptional same-scale root `r=p`.  This does not yet order `a,d`, but
it isolates the only mechanism by which a bounded-defect cycle can
avoid repeated root-scale descent.

There is also an exact carrier interpretation of a downward move.
If `d<a`, write

```
A=D E,       |D|=d.
```

Since `C` ends in `D`, the prefix of `U` through cut `h+d` ends in

```
D^2,
```

and its following generated label is

```
U[h+d]=A[d]=T[d]=3.
```

The word `D` is primitive: otherwise the displayed `D^2` would have
exponent at least four at a cut whose exact value is three.  Hence a
downward defect exposes a primitive square-at-three maturation in the
strictly shorter visible carrier `C=T[:h]`.  Turning this into a
minimality contradiction requires closure of the minimized class under
such contexted maturations; it is not automatically another whole-state
reset.

For comparison, an upward move has `D=A E` and the terminal form

```
U ends in A E A.
```

The exact fixed profile of `U` alone does not exclude either
orientation: rotations of the binary length-21 profile realize both.
The fixed profile of the child `V`, or a closure theorem for the
downward carrier maturation, is load-bearing.

## 5. Literature and finite audit

The period and commuting steps above use the Fine--Wilf theorem and the
Lyndon--Schuetzenberger commuting-words theorem.  The primary curling
number papers do not state a nested-reset or iterated pointed-border
lemma of the form (7).  CLSW Theorems 7--8 supply the one-symbol
strict-deletion/whole-power reset used upstream; their later
non-robust-word normal forms concern a single extension and do not
classify this two-level fixed-profile lift.

The A094004 total-length calibration test in
`tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration`
was executed successfully before the finite audits below.  Direct
enumeration over the alphabet `{2,3,4}`, with period-block length at most
ten, found no pair for which both `pc_U=U` and `pc_V=V`.  It found one
fixed `U` satisfying the internal equations at the boundary of that
range,

```
U=232223222323222322232,
```

and its child fails fixedness.  Independently, all ten internal children
arising from rotations of the binary length-21 fixed profile fail the
child fixed-profile equation.  These are finite checks only; the proof
above, not the enumeration, excludes the five-block branch and proves
(7).
