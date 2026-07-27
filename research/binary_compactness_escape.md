# Binary compactness escape via the Thue--Morse word

This note closes a possible loophole in
`compactness_escape_dichotomy.md`.  The escaping-root alternative is not
excluded when the recurrent alphabet is exactly `{2,3}`.

Let

```
t(n) = the parity of the number of `1` bits in n
```

be the one-sided Thue--Morse word.  Equivalently it is the fixed point of

```
mu(0)=01,  mu(1)=10.
```

Take the centered limits at

```
c_m = 2^(2m).
```

For every fixed coordinate, the limit is the two-sided word `x` given by

```
x(-k)=t(k-1)       (k>=1),
x(j)=1-t(j)        (j>=0).                         (1)
```

Indeed, for `0<=j<c_m`, the leading binary digit gives
`t(c_m+j)=1-t(j)`.  For `1<=k<=c_m`, the low `2m` bits of
`c_m-k` are the bitwise complement of those of `k-1`; because `2m` is
even, `t(c_m-k)=t(k-1)`.  Thus every fixed centered window at `c_m`
eventually equals (1).

The primitive substitution `mu` is uniformly recurrent.  Hence every
point of its two-sided orbit closure, including `x`, is uniformly
recurrent.  Recode

```
1 -> 2,    0 -> 3.                                 (2)
```

The recoded center has label `2`.

## No square ends at the center

It is enough to prove that no nonempty prefix of `t` is a square.  Suppose

```
t[0:2p] = U U.                                    (3)
```

If `p=2q` is even, both halves in (3) start on substitution-block
boundaries.  The injectivity of the two codewords `01` and `10` decodes
(3) to

```
t[0:2q] = V V.
```

Repeated decoding therefore reduces to the case that `p=2q+1` is odd.
For `0<=j<=q`, equality in (3) at the even position `2j` and the
identities

```
t(2n)=t(n),     t(2n+1)=1-t(n)
```

give

```
t(j+q)=1-t(j).                                    (4)
```

For `0<=j<q`, equality at the odd position `2j+1` gives

```
t(j+q+1)=1-t(j).                                  (5)
```

Equations (4)--(5) make

```
t(q)=t(q+1)=...=t(2q).
```

But (4) with `j=q` also gives `t(2q)=1-t(q)`, a contradiction.  This
includes `q=0`, where the last equation directly contradicts itself.
Thus (3) is impossible for every `p>=1`.

By (1), a square of root length `p` ending at cut zero of `x` would say

```
t[p:2p] = t[0:p],
```

which is exactly the forbidden square prefix (3).  Therefore no square
of any root length ends at that cut:

```
rho(x,0)=infinity.                                (6)
```

## The closed upper constraints still hold

Thue's overlap-freeness theorem for the Thue--Morse word says that its
language contains no overlap `a V a V a`; in particular it contains no
cube.  The same is true in its two-sided orbit closure and after the
one-to-one recoding (2).  Consequently:

* at a cut labelled `2`, there is no power of exponent greater than `2`;
* at a cut labelled `3`, there is no power of exponent greater than `3`.

These are exactly the closed upper constraints inherited from an orbit
in the binary `{2,3}` branch.  They coexist with uniform recurrence,
binary alphabet, a recurrent center labelled `2`, and the complete loss
of every lower square witness in (6).

This word is not an orbit word: many of its cuts have no label-matched
lower witness.  It is a counterexample only to the proposed compactness
step that binary recurrence plus the closed upper constraints should
prevent maximizing roots from escaping.

The executable `check_binary_compactness_escape.py` checks the formulas,
absence of square prefixes, and absence of cubes on growing finite
windows.  The finite checks calibrate the construction; the arguments
above prove the unbounded statements.
