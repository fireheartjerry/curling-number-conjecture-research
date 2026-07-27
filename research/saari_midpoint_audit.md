# Saari midpoint audit for replay squares

This note records a local word lemma and an obstruction to using it to
identify the curling numbers at the two early-square cuts.  It is a
reduction/audit, not a proof of the Curling Number Conjecture.

## 1. The local minimal-square midpoint lemma

Let a right-infinite word begin in the minimal square `u^2`, where
`r=|u|`; "minimal" means that no shorter prefix is a square.  At the
beginning of the second copy of `u`, let `v^2` be the minimal square and
put `s=|v|`.  Then

`2s>r`,

and `u` and `v` are prefix-comparable.  More explicitly:

* if `s>=r`, then `u` is a prefix of `v`;
* if `s<r`, then `v` is a prefix of `u` and
  `u=v v[:r-s]`, with `0<r-s<s`.

Indeed, the word beginning at the second `u` begins in both `u` and
`v^2`.  If `2s<=r`, then `v^2` is a prefix of `u`.  It would also be a
prefix of the first copy of `u`, contradicting the minimality of `u^2`.
Thus `u` is a prefix of `v^2`.  The two displayed cases follow by
comparing `r` and `s`.

This is the mechanism used in Saari's Lemma 5.8.  It is entirely local
and does not require periodicity.  In a primitive periodic word, iterating
the midpoint map on phases eventually reaches a directed cycle.  The
lemma constrains each edge of that cycle to a move between
prefix-comparable roots, with the next root longer than half the current
root.

## 2. Shortest roots are not maximizing roots

For the executed length-21 word

`Q=223222322232322232223`,

the shortest proper square-root lengths at its 21 circular cuts are

`(4,4,1,3,3,1,1,7,4,1,1,4,4,2,2,1,1,6,6,1,1)`.

The least maximizing-root lengths are

`(4,4,4,3,3,1,1,7,4,1,1,4,4,2,2,1,1,6,6,1,1)`.

They differ at cut 2: the shortest square has root length 1, while the
maximizing cube has root length 4.  The minimal-square midpoint map has
cycles

`(0,17,11,7)` with root lengths `(4,6,4,7)`,

and

`(1,18,12,8,4)` with root lengths `(4,6,4,4,3)`.

Both cycles wind once around the period.  These values were produced by
executed exhaustive checks of every proper root length.  They show that
one may not replace a maximizing root by Saari's minimal root at a
label-3 cut.

## 3. Exact algebra at the two early-square cuts

Use the early-square notation

`a=r-s-h>0`,

where `Y` has length `r` and period `s`, and let `delta<s` be the first
index satisfying

`Y[r-s+delta] != Y[delta]`.

Put

`V=Y^2 Y[:delta]`,

`A_short=Y[a:] V`,

`A_long=Y[a:] Y Y[:s] V`.

For all `j<delta`, the definition of `delta` gives

`Y[r-s+j]=Y[j]`.                                      (1)

Suppose `delta>=a`.  Then `A_short` ends in

`(Y[delta:]Y[:delta])^3`.                              (2)

To check (2), the suffix of length `3r` starts at offset `delta-a`
inside the initial copy `Y[a:]`, and direct concatenation gives three
copies of the rotation `Y[delta:]Y[:delta]`.

Define the length-`r+s` word

`W=Y[r-s+delta:] Y Y[:delta]`.

Equation (1) gives both

`A_long=A_short W`                                    (3)

and

`A_long` ends in `W^2`.                                (4)

For (3), after deleting the common prefix `Y[a:]`, the only required
identity is

`Y[:s]Y[:r-s+delta]=Y Y[:delta]`;

this is precisely the period-`s` equality through the `delta` matching
positions before the first mismatch.  The same identity, read at the
suffix of length `2(r+s)`, proves (4).

Thus the two cuts are exactly a midpoint pair for the nonminimal square
`W^2`: their distance is `r+s`.  At the short cut there is already the
smaller cube (2), while at the long cut there is also a smaller
root-`r` square.  Consequently `W` need not be the minimal square root,
so Saari's midpoint map need not connect the two cuts.

## 4. Executed counterexample to curling-number equality

The following instance satisfies all of the structural hypotheses above:

`s=3`, `r=7`, `h=3`, `a=1`,

`Y=2232232`,

`delta=1`.

The word `Y` is primitive and has period 3,
`gcd(r,s)=1<s`, and

`Y[r-s+delta]=Y[5]=3 != 2=Y[1]=Y[delta]`.

Also

`rot_1(Y^2Y[:3])=23223222322322232`

is primitive.  Executed reference code gives

`A_short=232232223223222322322`,

`cn(A_short)=3`,

with maximizing root `2322322` of length 7, and

`A_long=2322322232232223223223222322322`,

`cn(A_long)=2`.

The complete list of square roots at the long cut has lengths
`1,3,7,10`; none is a cube root.  Both cuts have shortest square-root
length 1 because both words end in `22`.  Hence the two exact curling
numbers are the two prescribed, unequal labels, while the minimal-square
data at the cuts agree trivially.

The full self-replay equations reject this particular primitive word at
another phase.  The example nevertheless proves that the two early cuts,
periodicity of `Y`, primitivity, and the gcd inequality do not force their
curling numbers or their maximizing roots to agree.  Any contradiction in
this branch must use additional replay phases.
