# Restricted adjacent-`2/3` Hamming minimization

This note assumes that the current counterexample reduction has produced at
least one adjacent-completion source

```
A a bad,                  A b terminal,
{a,b}={2,3},              cn(A)=a,
```

in which both `2` and `3` already occur in `A`.  This is the provenance
supplied by the ordinary or reverse adjacent-completion fork.  It excludes
both a new marker outside the alphabet and the weaker mistake of forgetting
which completion was the actual successor.

## 1. The restricted minimum is nondegenerate

Let `D_23` consist of provenanced descendants of such sources.  Concretely,
a member consists of a source `(A,a,b)` and a common output word `G` such
that

```
P=A a G,                  Q=A b G,
P is bad,                 Q is terminal,
```

and, for every proper prefix `G[:t]`, the next letter `G[t]` is the common
curling number of the two states.  In particular, with `i=|A|`,

```
|P|=|Q|>0,
P[j]=Q[j] for j!=i,
{P[i],Q[i]}={2,3},
```

Choose a member minimizing `tau(Q)`.

### Lemma 1 (immediate mismatch)

```
cn(P)!=cn(Q).                                      (1)
```

### Proof

Suppose both curling numbers equal `c`.  Badness of `P` gives `c>=2`.
Therefore `tau(Q)>=1`.  The actual successors

```
P c,                 Q c
```

still differ only at coordinate `i`, where the two values remain `2` and
`3`.  The first successor is bad.  The second is terminal with hitting time
`tau(Q)-1`.  This is a member of `D_23` with smaller terminal hitting time,
contrary to the selection.  This proves (1).

Unlike unrestricted Hamming minimization, this argument cannot be collapsed
by changing the defect to a fresh symbol.  Membership retains the actual
adjacent-completion source; both defect values already occur in `A`, and
appending common outputs never changes the defect coordinate.  The minimum
may equal zero, but then (1) already holds because `cn(Q)=1` and badness
gives `cn(P)>=2`.

## 2. The larger power must cross the defect

Put

```
h=cn(P),                 ell=cn(Q).
```

### Lemma 2 (defect-crossing)

If `h>ell`, every maximizing `h`-power suffix of `P` contains coordinate
`i`.  If `ell>h`, every maximizing `ell`-power suffix of `Q` contains
coordinate `i`.

### Proof

Consider `h>ell` and write a maximizing factorization as

```
P=X U^h.
```

If coordinate `i` lay in `X`, the suffix `U^h` would be unchanged in `Q`.
It would give `cn(Q)>=h`, contradicting `ell<h`.  Thus the powered suffix
contains `i`.  The other orientation exchanges `P` and `Q`.

The selected maximizing root may be taken primitive.  If it were a proper
power, expanding that proper power through all copies would produce an
exponent strictly larger than the curling number.

## 3. Cutting to the crossing power does not transport status

Let `s` be the starting coordinate of one of the powered suffixes in Lemma
2 and put

```
P_s=P[s:],                 Q_s=Q[s:].
```

The two words still differ at exactly one `2/3` coordinate, and the
larger-curling-number side is now a whole power.  However, suffix deletion
is not an orbit operation and need not preserve the adjacent-completion
source certificate.  Even if the retained prefix before the defect still
contains both symbols, its curling number need not make the same side the
actual successor.  The four status combinations

```
(bad,terminal), (terminal,bad), (bad,bad), (terminal,terminal)
```

are all logically open.

If exactly one of `P_s,Q_s` is bad, let `T_s` be the terminal one.  If the
cut pair also has a valid adjacent-completion source certificate, the
restricted minimum gives only

```
tau(T_s)>=tau(Q).                                  (2)
```

For the endpoint rank

```
R(P,Q)=|P|+tau(Q)
```

the exact cut difference is

```
R_s-R(P,Q)=tau(T_s)-tau(Q)-s.                     (3)
```

Equation (2) does not determine the sign of (3).  If the certificate is
lost, or if both cut words have the same status, there is no new member of
`D_23` at all.

There is a related tie-break conflict.  Appending one common output
preserves `R` and increases word length by one, so a minimum-`R`,
maximum-length selection proves the immediate mismatch.  A cut with equal
rank moves in the opposite length direction and is allowed by that same
maximum-length tie-break.  A minimum-length tie-break would handle the cut
but not the common extension.

## 4. Executed orbit-compatible near-models

All numbers in this section are recomputed by both curling-number
implementations in `check_restricted_hamming_rank.py`, after the A094004
calibration.  Every word here terminates; these examples refute local
timing or word-equation deductions, not a theorem which genuinely uses
infinite badness.

### 4.1 Provenance-light warning: orientation reversal and conserved rank

If one retains the established `2/3` coordinate but forgets the
actual-successor orientation, the adjacent pair

```
P=2232223222322,       Q=2232223222323
```

has executed values

```
cn(P)=3, tau(P)=53,
cn(Q)=2, tau(Q)=52.
```

The unique maximizing root of `P` is `2322`; its cube starts at coordinate
one and contains the final `2/3` defect.  Cutting to that cube gives

```
P_1=232223222322,       tau(P_1)=53,
Q_1=232223222323,       tau(Q_1)=62.
```

Thus the finite long/short orientation reverses, while the shorter-tail
endpoint rank is conserved:

```
13+52=65=12+53.                                  (4)
```

Both symbols occur repeatedly on both sides, so this is not the
fresh-marker construction.  Its common prefix has curling number three,
while its finite longer-tail side uses completion two.  It is therefore a
warning about the weaker unoriented class, not a countermodel to the full
actual-source certificate.

### 4.2 Pure-cube actual completion: a crossing-root rank increase

Put

```
Y=23222322232,          A=Y^3.
```

The executed value is `cn(A)=3`.  Hence

```
P=A3
```

is the actual `3`-completion, while

```
Q=A2
```

is the adjacent wrong completion.  Their executed data are

```
cn(P)=2, tau(P)=42,
cn(Q)=3, tau(Q)=3.
```

The word `Q` has two maximizing cube roots.  The shorter root `2322`
starts at coordinate `22`.  Cutting both words there preserves the finite
long/short orientation but changes the terminal endpoint from

```
34+3=37
```

to

```
12+53=65.                                         (5)
```

This is a rank increase of `28` caused by a maximizing power which crosses
the adjacent completion defect.  The other maximizing root has length
eleven and starts at coordinate one; its cut endpoint is `36`.  Therefore
the example refutes a root-independent or shortest-root descent, but it
does not refute an argument which proves that a specially selected
ambient root always works.

### 4.3 Reverse actual completion: no physical cut

For

```
A=(23)^3,               D=A[1:]=32323,
```

the executed values give `cn(A)=3` and `cn(D)=2`.  The reverse adjacent
completions are

```
D2=323232,              cn=3, tau=3,
D3=323233,              cn=2, tau=1.
```

The unique maximizing root of the actual completion `D2` is `32`, and its
cube occupies the whole word.  The defect-crossing power therefore begins
at coordinate zero and supplies no shorter endpoint at all.

This is also the exact symbolic obstruction in the hypothetical reverse
fork.  There one has

```
D2=rot(C)^3 bad,            D3 terminal,
cn(D)=2,                    cn(D2)=3.
```

If `cn(D3)<3`, the restricted pair already mismatches and the displayed
whole cube is a maximizing defect-crossing power beginning at zero.  Thus
minimum hitting time cannot turn this branch into a strict physical or
endpoint descent.  If `cn(D3)=3`, the two sides first move synchronously
and Lemma 1 applies only at their later mismatch.

## 5. Exact outcome

Provenanced `2/3` minimization rigorously forces an immediate
curling-number mismatch, and the larger maximizing power rigorously crosses
the inherited defect.  It does not force endpoint-rank descent.  The
reverse whole-cube branch can give no cut, while a proper suffix cut can
lose both status and the actual-source certificate.  The missing
implication is a status-transfer or root-selection theorem:

```
after cutting to a specified crossing power,
exactly one cut word remains bad and its terminal neighbor
has tau increase strictly smaller than the deleted depth.
```

The finite models show that this implication cannot follow from the
adjacent `2/3` word equation, actual-completion provenance, or finite tail
ordering alone.  Infinite badness remains load-bearing.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_restricted_hamming_rank.py
```
