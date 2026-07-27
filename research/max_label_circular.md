# Maximum labels in a primitive circular fixed profile

This note audits a proposed descent for a hypothetical profile with maximum
four.  The original ordinary weighted-profile quotient loses one aligned
copy at its left boundary.  The corrected output is a pointed,
one-defect quotient; it does not prove that the maximum is at most three.

## 1. Adjacent equal-label witnesses

Let two consecutive cuts carry the same label `A>=3`.  Choose primitive
maximizing `A`-roots of lengths `p` and `q` at the two cuts and put
`g=gcd(p,q)`.

If `p=q`, the two powers transport the same periodic run across the
appended symbol.  If `p<q`, then

```
q > (A-1)*p + g.
```

If `p>q`, then

```
p >= (A-1)*q + g.
```

For `p<q`, the overlap is the whole old `A*p`-letter power.  If
`A*p >= p+q-g`, Fine--Wilf gives period `g`.  When `g<p`, this contradicts
primitivity of the old root.  When `g=p`, the overlap contains a complete
conjugate of the new length-`q` root and gives it period `p`, contradicting
its primitivity.  Thus the Fine--Wilf threshold fails, giving the first
inequality.  For `p>q`, the overlap has length `A*q-1`; the same two
divisibility cases give

```
A*q-1 < p+q-g,
```

which is the second inequality.  These arguments do not assume that a
least square root is maximizing.

For the max-four entrance

```
E = 2 3 3 3 3 4,
```

the least maximizing roots at the first three `3` cuts are nonunary.  The
fourth `3` cut has the unary root.  Adjacent nonunary root lengths either
transport unchanged or jump by more than a factor of two.

The tempting claim that one maximal cubic run must cover all four `3`
cuts cannot be proved from the local entrance equations, even with
circular primitivity.  Executed SMT and an independent exact checker give
the primitive length-80 circular word

```
23333444232234222333223423333442344442233223423333442344442233223423333442344442
```

whose cuts `0,...,5` are the displayed entrance and have exact profile and
maximizing-root sets

```
2/{21}, 3/{21}, 3/{21}, 3/{21}, 3/{1}, 4/{1}.
```

The period-21 maximal run covers the first three cube cuts and the
period-one run covers the fourth.  This is only a local circular
falsifier: the other 74 cuts are not required to be fixed.  Thus a proof
must use full global profile coverage, not merely entrance equations and
primitivity.

The shorter finite marker construction

```
3323323323333433233233233334
```

realizes the same split with period three versus period one along an exact
finite orbit segment.  It equals `Y^2` for
`Y=33233233233334`, so it is not itself a primitive circular example.

## 2. Hierarchical entry into threshold components

For `j>=3`, put

```
H_j = { positions d : Q[d] >= j }.
```

Let `C` be a circular component of `H_(j-1)`, and let `d` be the first
position of `H_j` inside `C`.  Then

```
Q[d]=j,
Q[d-j .. d)=(j-1)^j,
Q[d+1]<j.
```

Indeed, the rise bound gives `Q[d]=j`.  Every symbol of a primitive
maximizing `j`-root is at least `j-1`.  Its whole `j`-power therefore lies
inside `C` before `d`; because `d` is the first `H_j` position of `C`, it
is constant `j-1`.  Primitivity makes its root length one.  Exactness of
the value `j` makes the terminal run length exactly `j`.

At the next cut, a label at least `j` cannot use root one, since there is
only one trailing `j`.  A root of length at least two would require at
least `2j>j+1` symbols all in `H_(j-1)` and would cross the left boundary
of `C`.  This contradicts the root-symbol condition.  Hence the first
`H_j` child of each `H_(j-1)` component is a singleton.

Later `H_j` children in the same component need not be singletons.  This
qualification blocks a false induction purporting to show maximum at most
four.

## 3. Return-word quotient: off-by-one correction

Assume `Q` is a primitive circular fixed profile with maximum four.  List
cyclically all cuts `e_i` immediately after occurrences of

```
E=233334,
```

and define the raw return word

```
R_i = Q[e_(i-1) .. e_i).
```

Let `U_i` be the identity, or color, of the exact raw word `R_i`.  Define
the weight of a token by

```
w(U_i)=R_i[0].
```

Every occurrence of `E` is the first `4` in its `H_3` component, so the
component-entry lemma gives

```
w(U_i) in {2,3}.
```

At cut `e_(i-1)`, put `k=w(U_i)` and choose a primitive maximizing proper
root of raw length `p`.  Then `p>=6`: if `p<6`, square equality would copy
the unique terminal `4` of `E` to one of the preceding five positions of
`E`.

Consequently `E` is a suffix of the last root block.  Equality of the `k`
root blocks places an identical `E` at the cuts

```
e_(i-1), e_(i-1)-p, ..., e_(i-1)-(k-1)p.
```

The earlier assertion that this list contains every root boundary was off
by one.  The left boundary

```
e_(i-1)-k*p
```

need not end in `E`.  The chosen raw root is a concatenation of complete
return words between each pair of displayed marker cuts, but the raw
`k`-power supplies only `k-1` equal token blocks.

Conversely, every token power concatenates identical raw return-word
tokens and hence is an exact raw power.  A proper token root spans fewer
than all return words, so its positive raw length is below `|Q|`.
Therefore only

```
w(U_i)-1 <= proper_cn_U(cut before U_i) <= w(U_i).
```

The lower bound is the trivial bound one when `w(U_i)=2`.  Equality with
`w(U_i)` requires an additional aligned token power; it does not follow
from the displayed raw maximizing root.  Thus `U` is a strictly shorter
**one-defect weighted profile**, not necessarily a weighted fixed profile.
The unmatched initial partial return is load-bearing.

The token word `U` is still primitive.  If `U=V^h` as a token word,
concatenating the identical raw token blocks would make `Q` the
corresponding raw `h`-power.

### Exact pointed-return equation

The unmatched boundary has a rigid one-token form.  The following statement
is valid for any nonoverlapping marker word, not only `E=233334`.

Let `e` be a marker cut, let the raw curling number there be `k>=2`, and
let a primitive maximizing root `P` of length `p` end in the marker.
Write `Z=A V` for the nonempty token word coding the interval

```
[e-p,e).
```

The copied terminal marker makes `e-p` a marker cut.  Put `b=e-kp`.

* If `b` is also a marker cut, the token word ends in `Z^k`.
* If `b` is not a marker cut, let `a<b` be the preceding marker cut.
  Then the token word from `a` through `e` has the exact form

  ```
  D V Z^(k-1),
  ```

  where the raw return word `Phi(A)` is a proper suffix of `Phi(D)`.

For the second case, let `f` be the first marker cut after `b`.  The first
raw root block `[b,b+p)` is equal to every later `P` block.  Hence its
first marker after `b` occurs at the same positive offset as the first
marker after `e-p`, namely after the raw return `Phi(A)`.  The actual
return from `a` to `f` is `Phi(D)=C Phi(A)`, where
`C=Q[a:b]` is nonempty.  The later marker gaps in the first `P` block code
`V`, and the remaining `k-1` complete `P` blocks code `Z^(k-1)`.  These
pieces give the displayed equation.

Thus every deficient cut replaces the first token `A` of the missing
copy by a token `D` with

```
|Phi(D)|>|Phi(A)|.
```

The directed defect graph `A -> D` is acyclic when ordered by raw return
length.  This is a genuine finite rank, but it is not yet a descent of the
whole circular profile: different cuts may use different defect edges,
and aligned cuts can terminate all defect paths.  The Q21 and length-37
examples below realize exactly that behavior.

### Longest-return alignment does not propagate

Let `L` be a return color of maximum raw length.  In the pointed equation,
`L` cannot be the source `A` of a defect, because a defect would require a
strictly longer target `D`.  Therefore every chosen raw maximizing root
whose aligned token word `Z` begins with `L` has its power start at a
marker and supplies the full ordinary token power `Z^k`.

This is a statement about the first token of a chosen root, not about the
token following the current cut.  No surjectivity property makes every
occurrence of `L` such a root start.  Alignment consequently does not
propagate down the length order.

The executed Q21 quotient has return lengths `4,3,2`.  Its two chosen
roots beginning with the length-four color are aligned, while its four
defects are two copies each of the strict edges

```
3 -> 4,  2 -> 4.
```

The length-37 quotient has return lengths `7,15`; its chosen root beginning
with the length-fifteen color is aligned, while two other cuts use the
edge `7 -> 15`.  Thus even an aligned occurrence of every longest color
does not force its shorter suffix colors to align.

Restricting to longest-color landmarks does not leave a weighted fixed
subsystem.  The return quotient between the four longest-color occurrences
in Q21 has length four and proper profile `1111`.  The corresponding
length-37 quotient has length two and profile `11`.  In the all-weight-two
length-31 model every one-symbol return has the same maximal raw length,
so the operation selects all 31 positions and gives the original
profile `2^31` without any strict descent.  These three cases exhaust the
two hoped-for outcomes: the subsystem is either shorter but loses
squarefulness, or remains fixed but is not shorter.

## 4. Executed regressions and weighted-profile obstructions

The binary length-21 fixed profile

```
223222322232322232223
```

is a weighted profile with the identity weight map.  Executed code gives
six `3` positions and least maximizing-root profile

```
(4,4,4,3,3,1,1,7,4,1,1,4,4,2,2,1,1,6,6,1,1).
```

Using all six `3` positions as return landmarks gives raw returns

```
223, 2223, 2223, 23, 2223, 2223
```

and token word `011211`, with every proposed token weight equal to two.
Exact execution gives proper token profile `211211`, so four cuts lose
one.  The copied terminal landmark occurs at the end of the preceding raw
root block, but that power starts inside the preceding return.  This is a
direct regression for the missing-boundary error.

The assertion that every weighted profile uses at most two token colors
is false.  The primitive ternary circular token word

```
0010200100101001020010200100101
```

has proper circular curling number exactly two at all 31 cuts.  Giving
all three colors weight two makes it a weighted profile.  Independent
executed code recomputed its complete profile and primitivity.  It is
dihedrally equivalent, up to color relabeling, to

```
0220202202122022020220212202122.
```

Thus the exact remaining max-four problem is not merely the binary
length-21 cycle.  More importantly, these weighted profiles cannot be
claimed as quotients of a max-four profile without resolving the
one-defect boundary.

The mixed-weight length-37 profile in
`mixed_weight_counterexample.md` gives a second exact regression.  Taking
its three weight-three positions as landmarks gives raw returns of lengths
`7,15,15`, token word `011`, and proposed weights `222`.  Its executed
proper token profile is `211`.

## 5. Conditional raw-lift equations

If the unmatched boundary is independently known to be a marker at every
cut, then the old weighted-lift formulation becomes valid.  For a weighted
token cycle `(U,w)`, a raw lift is a map `Phi` from token
colors to nonempty words such that

```
Phi(a)[0]=w(a),
Phi(a) ends in E,
```

and the synchronized concatenation

```
Q=Phi(U_0) Phi(U_1) ... Phi(U_(N-1))
```

has no additional `E` occurrences between the declared token boundaries.
The boundary equations are automatic: a token maximizing power maps to
an equal raw power.  The genuinely new conditions are all internal cuts
of every `Phi(a)`, where different left token contexts must nevertheless
give the same prescribed raw label.

`z3_q21_lift.py` encodes the special binary case with two raw return words,
and `search_q21_lift.cpp` is a heuristic falsifier.  No raw lift has been
found.  Failure of a bounded search is not a proof of nonexistence.

There is, however, an exact finite lower bound.  The unrestricted-color
SMT encoding gives:

* no weighted profile has token length below 21;
* every length-21 profile has exactly two colors, has six weight-three
  positions, and its weight word is a rotation of the length-21 binary
  fixed profile;
* no weighted profile has token length 22 through 30;
* a ternary all-weight-two profile first appears at length 31.

Every raw return has length at least six.  A weight-three return has length
at least seven, since a length-six return is exactly `E` and begins in
two.  Hence a raw lift below length 186 can only come from the length-21
binary profile, with

```
|Q| = 15*|R_2| + 6*|R_3|,
|R_2|>=6, |R_3|>=7.
```

`enumerate_q21_lifts.cpp` exhaustively tested every assignment of the
internal symbols of both return words for every length pair with raw
length below 186: 11,090 pairs of raw words.  It also tested the two
length-186 pairs `(6,16)` and `(8,11)`, another 19,926 raw-word pairs.
No aligned fixed lift occurred.  At token length 31 and raw length 186, every
return would have to equal the same six-letter word `E`, making the raw
word `E^31`, not primitive.  Thus the combined exact computation excludes
aligned raw lifts of length at most 186.  Because a genuine max-four
profile may use the one-defect branch, this does **not** exclude all
primitive max-four circular fixed profiles in that range.

The computation is a finite check inside the conditional aligned model.
