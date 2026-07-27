# Quotient by maximum-label entrance markers

Let `P` be a primitive circular fixed profile, let

```
M=max(P),
```

and suppose `M>=4`.  The top-component analysis produces the entrance
marker

```
E_M = (M-2) (M-1)^M M.                          (1)
```

It ends at the first `M` phase in a component of positions whose values
are at least `M-1`, and it contains exactly one occurrence of `M`.

This note audits the quotient by consecutive occurrences of the complete
word `E_M`.  The quotient is useful, but it is not an ordinary
lower-maximum circular fixed profile.

## 1. Return tokens and their weights

Put a boundary immediately after every occurrence of `E_M`.  Enumerate
the boundaries cyclically as

```
b_0,b_1,...,b_(N-1).
```

Let `G_i` be the integer word from `b_i` up to `b_(i+1)`, including the
terminal copy of `E_M`.  Two tokens are declared equal only when their
full integer words are equal.  Let `T` be the resulting circular word of
exact return-token identities.

The marker in (1) has no nonempty proper border.  Every proper suffix
starts with `M-1` or `M`, whereas every nonempty prefix starts with
`M-2`.  Its occurrences therefore do not overlap, and the return-token
decomposition is unambiguous.  Also,

```
T is primitive.                                (2)
```

Indeed, if `T=U^d` for `d>=2`, concatenating the exact integer return
words represented by `U` writes a rotation of `P` as an integral
`d`-th power, contrary to the primitivity of `P`.

Give the token following boundary `b_i` the weight

```
w(G_i)=P[b_i].
```

The top-component structure gives

```
2<=w(G_i)<=M-1.                                 (3)
```

Different exact return tokens can have the same weight.

## 2. Exact off-by-one lemma

Fix a boundary `b=b_i`, put `a=P[b]`, and choose a primitive maximizing
`a`-root `Y` of integer length `q`.  Thus `P^Z` ends in `Y^a` at `b`.

The last symbol of `Y` is the terminal `M` of `E_M`.  If `q<|E_M|`, its
copy one root-length earlier would put a second `M` inside the displayed
copy of `E_M`, which is impossible.  Therefore

```
q>=|E_M|=M+2.                                   (4)
```

Equality of adjacent `Y` copies transports the complete final `E_M`, not
only its terminal `M`.  Consequently

```
b-q, b-2q, ..., b-(a-1)q
```

are all entrance-marker boundaries.  The interval of length `q` between
two consecutive listed boundaries is a concatenation `B` of one or more
whole return tokens.  Equality of the integer `Y` blocks transports every
complete internal occurrence of `E_M`; uniqueness of the return
decomposition then makes the corresponding token block exactly `B` at
each aligned interval.  Hence the token word ends in

```
B^(a-1).                                        (5)
```

There are only `a-1` certified token copies.  The start `b-aq` of the
earliest integer copy of `Y` is not certified to be a marker boundary:
the equality `Y^a` does not include the symbols immediately preceding
that start.

Let `c_i` be the proper circular curling number of the exact token word
`T` at boundary `b_i`.  Equation (5) gives `c_i>=a-1`.  Conversely, a
proper token `k`-power expands, by concatenating exact return words, to a
proper integer `k`-power at the same boundary of `P^Z`.  The original
profile value is exactly `a`, so `c_i<=a`.  Thus

```
w(G_i)-1 <= c_i <= w(G_i),                      (6)
```

or equivalently

```
c_i is w(G_i)-1 or w(G_i).                      (7)
```

Claiming `c_i=w(G_i)` silently assumes that `b-aq` is another entrance
boundary.  That is precisely the missing off-by-one assertion.

## 3. What the unmatched first copy contains

The earliest copy of `Y` is a pointed partial return, not necessarily a
whole return token.  Let `H` be the consecutive return word containing
the point `b-aq`, and let `G` be the first token of the aligned block
`B`.

The suffix of `H` beginning at the point agrees with a prefix of `G`.
It ends no later than the terminal entrance marker of `G`.  It need not
equal all of `G`: an occurrence of `E_M` can straddle the unmatched start,
because the symbols to its left are not part of the equality `Y^a`.
Such a straddling marker is absent at the aligned starts, which immediately
follow an `E_M`; the unbordered property prevents two aligned markers from
overlapping but does not control the unmatched left context.

Therefore the defect case `c_i=w(G_i)-1` does not automatically give a
strict descent between the lengths of two complete return words.  The
only unconditional object is a return word with a distinguished interior
point and a suffix-prefix equality.  Any induction using a return-length
descent must first exclude these straddling markers.

## 4. Executed local countermodel to a clean quotient

The off-by-one occurs under the local marker and root hypotheses.  Take

```
M=4,
E_4=233334,
Y=2E_4=2233334,
P=22 Y Y.
```

The executed word `P` is primitive.  At the circular cut after its final
term, its exact value is two and its sole maximizing proper root has
length seven, namely `Y`.  The two occurrences of `E_4` end at the two
marker boundaries.  Their consecutive return words are distinct:

```
222233334,
2233334.
```

Both successors have weight two.  Encoding the two exact return types as
distinct token symbols gives the primitive two-token word whose proper
circular profile is `(1,1)`, not `(2,2)`.  Thus the original square
certifies only one complete repeated return gap.  Collapsing the two
tokens to their common weight gives `(2,2)`, destroying both injectivity
and primitivity.

This word is a local countermodel, not a global fixed profile; it shows
that neither equality in (6) nor injectivity of the weight map follows
from the marker-copy equation itself.

## 5. Consequence for induction on `M`

The exact quotient has a lower maximum at the level of weights, but it is
a defective weighted fixed profile:

```
pc_T(i) in {w(T[i])-1,w(T[i])},
2<=w(T[i])<=M-1.                                (8)
```

It is not an ordinary fixed profile because its symbols are exact return
identities, while its profile values are numerical weights.  Replacing a
return identity by its weight is not sound: distinct return words with
the same first symbol become equal and can create token powers that do
not lift to integer powers of `P`.

Accordingly, (8) does not support induction on the maximum label in the
ordinary Curling Number Conjecture.  A valid induction would need one of
the following additional mechanisms:

1. prove that the weight map is injective on the return types that occur;
2. prove that every unmatched start `b-aq` is actually a marker boundary,
   eliminating the `-1` case;
3. formulate and prove termination for pointed, weighted return words,
   while showing that their dynamics lift back to the deterministic
   integer orbit.

None of these conclusions follows from the present quotient equations.
