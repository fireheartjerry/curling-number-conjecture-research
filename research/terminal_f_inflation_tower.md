# The infinite terminal-`F` inflation tower

This note is conditional on an infinite repetition of the terminal-`F`
branch isolated in `contained_completion_commutative_square.md`.  It
uses the exact orbit transitions at every level.  No assertion about a
generic squareful word is used.

## 1. Tower hypotheses

For every integer `i>=0`, let `Y_i` be primitive, put

```
n_i=|Y_i|,
A_i=Y_i^3,
D_i=A_i[1:].
```

Assume the ordinary boundary data

```
A_i is bad,                 D_i is terminal,
cn(A_i)=3,                  cn(D_i)=2,
Y_i[0]=2.
```

Put

```
H_i=A_i3,
F_i=D_i3.
```

Assume the terminal-`F` branch

```
H_i=2F_i is bad,            F_i is terminal,
cn(H_i)=cn(F_i)>=2.
```

Run `H_i` and `F_i` through their common outputs until their first
unequal curling numbers.  Let `G_i` be the complete word of common
outputs before that cut and let

```
delta_i=|G_i|.
```

The terminal-`F` inflation lemma gives the next ordinary boundary:

```
A_(i+1)=H_i G_i=Y_(i+1)^3,
D_(i+1)=F_i G_i=A_(i+1)[1:],                      (1)
```

and the exact scale separation

```
n_(i+1)>2n_i+gcd(n_i,n_(i+1)).                    (2)
```

These hypotheses describe the branch under audit.  They do not assert
that such a tower exists.

## 2. Exact nesting and one common bad orbit

### Lemma 1

For every `i>=0`,

```
A_(i+1)=A_i 3 G_i,
D_(i+1)=D_i 3 G_i=F_i G_i,
F_(i+1)=F_i G_i 3.                                (3)
```

Consequently each of the three families `(A_i)`, `(D_i)`, and `(F_i)`
is strictly increasing under the prefix order.  All `A_i` are states
on one fixed bad orbit.

### Proof

The first identity in (3) is the first identity in (1) after substituting
`H_i=A_i3`.  Delete the first symbol from it.  Since `A_i[1:]=D_i`,
the result is

```
D_(i+1)=D_i3G_i.
```

The definition `F_i=D_i3` gives the middle identity in (3).  Appending
the defining final `3` of `F_(i+1)` gives the last identity.

The scale inequality (2) makes `n_(i+1)>n_i`, so all three length
increases are strict.  The actual first orbit step from `A_i` appends
its value `3` and reaches `H_i`.  Every symbol of `G_i` is then an
actual output from the bad orbit of `H_i`.  Thus the first identity in
(3) places `A_(i+1)` later on the same deterministic bad orbit as
`A_i`.  Induction on `i` places every `A_i` on the orbit from `A_0`.

### Corollary 2 (the defect tape)

The cofinal nested families `(D_i)` and `(F_i)` have the same
right-infinite limit

```
T=lim_i D_i=lim_i F_i.
```

The nested bad states have the limit

```
W=lim_i A_i=2T,                                    (4)
```

and `W` is the complete right-infinite orbit word from `A_0`.

Put

```
e_i=|D_i|=3n_i-1.
```

Then the recursion of `T` is exact at every cut at or after `e_0`
except the cuts `e_i`:

```
T[e_i]=3,                    cn(T[:e_i])=2,         (5)
T[t]=cn(T[:t])     for e_i+1<=t<e_(i+1).           (6)
```

### Proof

The inclusions

```
D_i < F_i <= D_(i+1)
```

follow from (3), so the two chains are cofinal and have the same union.
Since `A_i=2D_i`, taking unions gives (4).  Lemma 1 places nested states
of unbounded length on the single orbit from `A_0`; their union is
therefore its complete infinite extension.

At length `e_i`, the prefix of `T` is `D_i`, while its next symbol is
the final `3` used to form `F_i`.  This proves (5).  For
`e_i+1<=t<e_(i+1)`, write

```
q=t-(e_i+1).
```

The prefix at that cut is

```
T[:t]=F_i G_i[:q].
```

The next symbol `T[t]=G_i[q]` is, by definition of `G_i`, the curling
number of that state on the terminal orbit from `F_i`.  This proves
(6).  The intervals in (6), together with the exceptional endpoints
in (5), exhaust every integer cut `t>=e_0`.

Thus `T` is not an orbit word.  It is an exact orbit tape with the
sparse forced substitutions `2 -> 3` at the cuts `e_i`.  The leading
symbol in `W=2T` protects every one of those substitutions and makes
`W` the genuine bad orbit word.

## 3. Terminal replay intervals and tail lengths

Write

```
t_i=tau(D_i),                 f_i=tau(F_i).
```

### Lemma 3

For every `i>=0`,

```
delta_i=3n_(i+1)-3n_i-1,                         (7)
f_i=delta_i+t_(i+1).                              (8)
```

Moreover,

```
n_(i+1)>=2n_i+2,
delta_i>=3n_i+5,
f_i>=delta_i.                                     (9)
```

In particular `f_i` tends to infinity.

### Proof

Take lengths in `D_(i+1)=F_iG_i`.  The two sides have lengths

```
3n_(i+1)-1
```

and

```
3n_i+delta_i,
```

respectively.  Their equality gives (7).

The terminal orbit from `F_i` appends the `delta_i` common outputs and
reaches `D_(i+1)`.  The high orbit remains bad throughout this common
segment, so none of the common curling numbers is one.  The remaining
number of steps to the first one is therefore `t_(i+1)`, which proves
(8).

The gcd in (2) is at least one.  Since all quantities are integers,
(2) gives `n_(i+1)>=2n_i+2`.  Substitute this bound in (7):

```
delta_i
 >=3(2n_i+2)-3n_i-1
 =3n_i+5.
```

Equation (8) and nonnegativity of `t_(i+1)` give the last inequality in
(9).  The recurrence for `n_i` makes `n_i` unbounded, so the same is
true of `delta_i` and `f_i`.

### Lemma 4 (no fixed terminal orbit accumulates the intervals)

The orbit from `F_i` reaches `D_(i+1)` after exactly `delta_i` common
steps.  Its next appended symbol is `2`, whereas both `F_(i+1)` and
every longer prefix of `T` have `3` in that position.  Hence no later
state after `D_(i+1)` on the orbit from `F_i` equals `F_j` for any
`j>=i+1` or `D_j` for any `j>=i+2`.

### Proof

Equation (1) gives the state `D_(i+1)` after the common replay.
Its curling number is `2` by the tower hypotheses, so its actual next
state is `D_(i+1)2`.  Equation (3) gives

```
F_(i+1)=D_(i+1)3.
```

The two states differ at the first position after `D_(i+1)`.  Every
later orbit state extends `D_(i+1)2`, because orbit evolution only
appends symbols.  The word `F_(i+1)` itself has the incompatible `3`.
Every `F_j` with `j>=i+2` and every `D_j` with `j>=i+2` extends
`F_(i+1)=D_(i+1)3`, by Lemma 1.  Words with those two incompatible
symbols at the same coordinate cannot be equal.

Lemmas 3--4 explain why the divergent sequence `f_i` does not give a
single finite terminal seed whose first one is postponed without
bound.  The seeds `F_i` are different.  Each terminal orbit shadows
exactly one inter-defect interval and then leaves the nested tape
permanently.

## 4. Exact endpoint-rank transport

Define the ordinary and promoted endpoint ranks

```
R_i=|A_i|+tau(D_i)=3n_i+t_i,
P_i=|H_i|+tau(F_i)=3n_i+1+f_i.
```

### Lemma 5

Every inflation step has the exact rank identity

```
P_i=R_(i+1).                                      (10)
```

Its comparison with the preceding ordinary rank is

```
R_(i+1)-R_i=1+f_i-t_i.                            (11)
```

### Proof

Use (7)--(8):

```
P_i
 =3n_i+1+delta_i+t_(i+1)
 =3n_(i+1)+t_(i+1)
 =R_(i+1).
```

Subtract the definition of `R_i` to obtain (11).

Thus the first mismatch does produce an ordinary boundary at exactly
the rank of the promoted essential pair `(H_i,F_i)`.  It does not
produce an ordinary boundary at the preceding rank `R_i` unless the
additional equality `f_i=t_i-1` holds.

If `(A_0,D_0)` was selected by globally minimum endpoint rank and
maximum bad-word length among the minimizers, then

```
R_i>R_0                    for every i>=1.         (12)
```

Indeed every `(A_i,D_i)` is essential, so global minimality gives
`R_i>=R_0`.  Lemma 1 and (2) give `|A_i|>|A_0|`.  Equality of ranks
would contradict the maximum-length tie-break.  Therefore an infinite
terminal-`F` tower cannot stay at the selected rank.  The exact local
equality (10) transports each promoted rank to the next ordinary
boundary while the tower escapes to unbounded lengths and hence to
unbounded absolute ranks.

## 5. The compactness outcome is maximizing-root escape

The bad orbit from `A_0` uses a finite alphabet.  To prove this, suppose
an appended curling number were absent from the current state.  That new
final symbol would occur only once, so the next state would have curling
number one.  This is incompatible with badness.  Induction confines all
appended symbols to the finite alphabet of `A_0`.

Let

```
c_i=|A_i|=3n_i.
```

At the genuine bad-orbit cut `c_i`, the next label is `3`.

### Lemma 6 (the maximizing root is forced to escape)

At the cut `c_i`, the only root length of a suffix cube of `A_i` is
`n_i`.  Consequently its least maximizing-root length tends to
infinity.

### Proof

The displayed factorization `A_i=Y_i^3` supplies the root length
`n_i`.  Suppose a suffix cube has root length `p`.  If

```
3p<=|A_i|-1=|D_i|,
```

that entire suffix cube also lies in `D_i`, contradicting
`cn(D_i)=2`.  A suffix cannot be longer than the word, so `3p<=|A_i|`.
The two integer inequalities force

```
3p=|A_i|=3n_i,
```

and hence `p=n_i`.  Equation (2) makes `n_i` tend to infinity.

### Theorem 7 (exact compactness escape point)

There is a two-sided limit word `x` obtained from centered shifts of the
actual bad orbit word `W` at a subsequence of the cuts `c_i` such that

```
x[0]=3,
```

but no cube of any finite root length ends at cut zero of `x`.
Moreover, at every integer cut `s`, no suffix power of exponent strictly
larger than `x[s]` ends at that cut.

### Proof

The alphabet of `W` is finite and `c_i` tends to infinity.  For radius
one, choose an infinite subsequence on which the centered radius-one
windows agree.  From it choose an infinite subsequence on which the
radius-two windows agree.  Continue for every positive integer radius
and take the diagonal subsequence.  Each fixed coordinate stabilizes,
defining a two-sided word `x`.  The center symbols are the next labels
at the cuts `c_i`, so `x[0]=3`.

Assume a cube of root length `p>=1` ends at cut zero of `x`.  The
length-`3p` window to the left of the center stabilizes along the
diagonal subsequence.  For every sufficiently late selected index, the
same cube is a suffix of `A_i`.  Lemma 6 then gives `p=n_i`.  The left
side is fixed while `n_i` tends to infinity, which is impossible.
Therefore no finite-root cube ends at the center.

Fix an integer cut `s`, a root length `p>=1`, and an exponent
`q>x[s]`.  If a `q`-th power of root length `p` ended at cut `s` of
`x`, the finite window containing that power and its following label
would stabilize along the selected centered shifts.  At every
sufficiently late corresponding cut `c_i+s` of `W`, the same power
would end and the next orbit label would be `x[s]`.  This would make the
curling number at least `q>x[s]`, contradicting the orbit rule for
`W`.  This proves the upper constraint at every cut.

This realizes the maximizing-root escape mechanism described in
`compactness_escape_dichotomy.md`: the finite orbit cuts have exact
label-matched witnesses, but every such witness crosses a window whose
size tends to infinity.  The limit retains the center label `3` and the
closed upper power constraints, while losing the required lower cube
witness.  The theorem does not assert that `x` is uniformly recurrent
or that it belongs to a preselected minimal subshift.  It is not an
orbit word and is not a counterexample to the Curling Number Conjecture.

The geometry of the escape is explicit here.  At cut `c_i`, the
protecting first symbol of `A_i=2D_i` is `3n_i` positions to the left,
and Lemma 6 says the maximizing cube occupies all of `A_i`.  Both the
protecting symbol and the left edge of the unique cube move to negative
infinity in the centered limit.

## 6. Outcome of the three proposed compactness closures

1. A fixed finite terminal orbit with arbitrarily delayed first one does
   not arise.  Lemma 4 proves that each fixed orbit leaves the nested
   tape at the next defect, while Lemma 3 assigns the unbounded hitting
   times to different seeds.
2. An ordinary boundary does arise at the exact promoted rank, by
   (10).  It is not at the preceding rank without an additional tail
   equality, and no later ordinary boundary has the globally selected
   base rank under (12).
3. The infinite tower forces the recognized compactness escape
   alternative in Theorem 7.  Compactness loses the load-bearing cube
   rather than producing a finite terminal orbit or a same-base-rank
   recurrence.

Hence an infinite terminal-`F` inflation tower is an exact
moving-defect/maximizing-root-escape configuration.  Excluding it
requires a relation between successive full orbit profiles or terminal
tails that is stronger than prefix nesting, endpoint-rank transport,
and compactness.
