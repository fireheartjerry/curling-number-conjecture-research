# Hidden-power descent for an early square replay defect

This note audits the proposed theorem that autonomous generation of one
copy forces replay from the resulting square.  As literally stated, its
claimed equivalence with full replay is false.  After adding the
counterorbit hypothesis that every symbol is at least two, the existing
overlap reduction gives a strict
descent in one quotient case and in one subcase of the other.  The sole
remaining subcase is an exact smaller fixed-origin square-to-cube
maturation, not a smaller early defect.

## 1. The claimed equivalence fails when the symbol `1` is allowed

Take

`P=(2,1,1)`.

The word is primitive.  Both implementations in `curling.py` were
executed on every word below and returned

| word | curling number |
|---|---:|
| `P=211` | `2` |
| `P P[:1]=2112` | `1` |
| `P P[:2]=21121` | `1` |
| `P^2=211211` | `2` |
| `P^2 P[:1]=2112112` | `2` |

Thus

`cn(P P[:d])=P[d]` for `0<=d<3`

and `cn(P^2)=2`, but replay from `P^2` already diverges at `d=1`.
The target word ends in `(1,1,2)^2`.  This root has length
`|P|=3`; it is the unavoidable square of the circular rotation of `P`,
not a proper circular root.

Therefore this example refutes the stated equivalence between

1. absence of a new *proper* circular power; and
2. full replay from `P^2`.

It does not refute the first assertion by itself.  To make the two
assertions equivalent, the proposed theorem needs the additional
hypothesis

`P[d]>=2` for every `d`.

That hypothesis is available in the counterorbit application.

## 2. Strengthened setup and maximality audit

Assume from now on that `P[d]>=2` for every `d`.  Put `p=|P|`,

`A_d=P P[:d]`, `B_d=P^2 P[:d]`,

and assume

`cn(A_d)=P[d]` for `0<=d<p`, `cn(P^2)=2`.

Suppose `h`, `1<=h<p`, is the first target mismatch.  The argument in
`square_early_divergence.md` gives a primitive target maximizing root
`Y` of length `r`, a positive integer `s`, and

`p=2r+s`, `a=r-s-h>0`,

such that

`B_h` ends in `Y^3`,

`P=rot_a(Y^2Y[:s])`,

`Y[s:r]=Y[:r-s]`,

`P[h]=2`, `cn(B_h)=3`.

The last two equalities use maximality, not just the displayed cube:
`P[h]=cn(A_h)` is an assumption, and `cn(B_h)=3` is the exact
first-divergence conclusion.  Any later displayed cube below is used
only as a lower bound until a source-replay equality supplies the exact
curling number.

Write

`r=q s+u`, `0<u<s`.

The exact source value at `A_h`, together with the terminal
`s`-periodic suffixes, gives `q in {1,2}`.

For the descent statements below, use the following enlarged class.
A *contexted early replay defect of block length* `b` consists of two
states in one common generated word, separated by an appended
length-`b` block `R`, whose terminal shadows contain respectively
`R^m` and `R^(m+1)` for some `m>=1`.  Their next curling-number streams
agree for `j` steps and differ at `j<b`.  Only the common stream up to
that first mismatch is required to be an actual orbit continuation.
The original pair `P,P^2` belongs to this class with `b=p` and `m=1`.
The descended pairs below belong to the same class.  Minimization over
this enlarged class is well founded, but the Fine--Wilf parametrization
used here was proved only for the original autonomous-square pair.  A
complete descent proof would also have to prove a structural lemma for a
minimal *contexted* defect; that closure is not assumed below.

## 3. Quotient two gives a strict smaller early defect

Assume

`r=2s+u`, `u<h<=s`.

Let `D=Y[:s]` and

`d_*=h-u`.

For `0<=j<=u`, define

`U_j=A_(d_*+j)`,

`V_j=A_(d_*+s+j)`.

Direct substitution into

`P=rot_(s+u-h)(Y^2D)`

gives:

* `U_j` ends in `D^2D[:j]`;
* `V_j` ends in `D^3D[:j]`;
* for `0<=j<u`,
  `cn(U_j)=cn(V_j)=D[j]`;
* at `j=u`,
  `cn(U_u)=D[u]=2` and `cn(V_u)=D[0]`.

The suffix `D^3D[:u]` in `V_u` contains a cube of the rotation of
`D` by `u`.  Hence `cn(V_u)>=3`, and the exact source equation gives
`D[0]>=3`.

Moreover,

`P[d_*:d_*+s]=D`,

so `V_0` is obtained from `U_0` by appending one exact copy of `D`.
The two resulting label streams agree for `u` symbols and then differ:

`D[u]=2 < D[0]`.

Because `u<s<r`, this is a strictly smaller early replay defect, measured
by the copied-block length.  This is a genuine descent; no claim that a
displayed witness is maximizing is needed.

## 4. Quotient one: descent or a fixed-origin obstruction

Assume

`r=s+u`, `1<=h<u<s`.

Put

`a=u-h`, `D=Y[:s]`, `R=rot_a(D)`.

The word `P` begins and ends in the same primitive length-`s` block
`R`.  Therefore

`P[:s]=R`,

`P` ends in `R`,

`A_s` ends in `R^2`.

The exact source equations give

`cn(P)=cn(A_s)=R[0]=2`.

Compare the source-label streams at the states `P` and `A_s`.  They
agree for their first `h` entries.  Afterwards the comparison is between

`D[(u+j) mod s]` and `D[j]`.

Let `delta` be the least phase where these two circular streams differ,
and put

`H=min(s,h+delta)`.

If `H<s`, the states separated by the smaller copied block `R` have an
early replay defect at offset `H`.  Since `s<r`, this is again strict
descent in copied-block length.

If `H=s`, however, the two states replay a whole copy of `R`.  At the
boundary,

`cn(A_s)=2`,

while `A_(2s)` ends in `R^3`, so

`cn(A_(2s))=P[2s]>=3`.

This is an exact fixed-origin square-to-cube maturation of the smaller
root `R`.  It is not an early replay defect.  Consequently, minimizing
only among early defects does not contradict this case.

The equality condition in this obstruction is explicit:

`D[(u+j) mod s]=D[j]` for `0<=j<s-h`.

Equivalently, with `e=s-u`,

`R[j]=R[(j+e) mod s]` for `h<=j<s`.

Thus `R` has cyclic period `e` everywhere except across one prefix
interval of length `h`.  The missing edge is exactly where the outer
cube promotes: `R[0]=2`, whereas `R[e]=P[2s]>=3`.

## 5. Consequence for a minimal-hidden-power proof

At the level of the original autonomous-square parametrization, copied
block length strictly decreases in:

1. the quotient-two branch;
2. the quotient-one branch with `H<s`.

To turn those reductions into a contradiction, one must show that a
minimal contexted defect satisfies a comparably strong overlap
parametrization.  That closure is an additional missing lemma.

Even with such a closure lemma, the quotient-one branch with `H=s` is
not eliminated, because the
strictly smaller object is a legitimate full-copy maturation rather than
an early defect.  Enlarging the minimized class to include legitimate
boundary promotions does not help: ordinary suffixes such as
`22 -> 222` are then minimal elements.

Any successful continuation must use the remaining source phases to show
that the smaller maturation cannot be masked by its left context, or must
attach an additional well-founded parameter that strictly decreases
through the fixed-origin obstruction.  Root length, overhang, and cut
alone do not supply that decrease.

## 6. Exact failure of closure for minimal contexted defects

The enlarged contexted class from Section 2 is not closed under the
autonomous-square Fine--Wilf parametrization.  There is an exact
source-high defect at the smallest possible copied-block length.

Start the executed orbit at

`S_0=22322232`.

Its first eight executed labels, checked by both implementations in
`curling.py`, are

`2,2,3,2,3,2,2,2`.

At orbit times `i=3` and `i+2=5`, put

`U=22322232223`,

`R=23`,

`V=U R=2232223222323`.

The terminal relations are exact:

`U` ends in `R`, and `V` ends in `R^2`.

The two states initially have the same curling number:

`cn(U)=cn(V)=2=R[0]`.

After both append that common first symbol, executed code gives

`cn(U 2)=3`,

`cn(V 2)=2`.

Thus this is a contexted early replay defect with block length `b=2`
and first mismatch `h=1`.  No positive `h<b` is possible for `b=1`,
so it is minimal in copied-block length among all defects using the
definition in Section 2.

The maximizing witnesses, also exhaustively enumerated by code, are:

| state | exact curling number | maximizing primitive root |
|---|---:|---|
| `U` | `2` | `2223`, length `4` |
| `V` | `2` | `23`, length `2` |
| `U2` | `3` | `2232`, length `4` |
| `V2` | `2` | `32`, length `2` |

In fact

`U2=(2232)^3`.

At the mismatch the two states share only the terminal shadow

`R R[:1]=232`

of length three.  The source-high cube has length twelve and begins at
the left edge of `U2`; it is inherited entirely from the source context.
The target context destroys it.

This exact orbit episode rules out the desired closure lemma for the
broad contexted class: a minimal contexted defect need not have the
target-high orientation, and its high witness need not be controlled by
the copied block.  Restricting the class to target-high defects would
retain the quotient-two child but would discard the possible source-high
child in the quotient-one `H<s` branch.

The obstruction persists even if one requires the pair to lie inside a
genuine autonomous self-generator.  Take the executed length-21 word

`Q=223222322232322232223`.

It generates a full copy of itself and has `cn(Q^2)=2`.  At offsets
`i=11`, `j=13`, again put `R=Q[11:13]=23`, and define

`U=Q Q[:11]`,

`V=Q Q[:13]=U R`.

Executed values are

`cn(U)=cn(V)=2`,

`cn(U2)=3`,

`cn(V2)=2`.

The unique maximizing primitive roots at these four cuts have lengths
`4,2,4,2`, respectively, with root words

`2223, 23, 2232, 32`.

Thus the identical minimal `b=2,h=1` source-high context defect is
ancestrally certified inside an autonomous word satisfying even the
desired full target replay.  Requiring an enclosing autonomous
self-generator does not repair closure.
