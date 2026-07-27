# The remaining symbol-two rotation seam

This note starts after `general_rotation_status.md`: status is already known
to be constant across every rotation phase whose label is at least three.
It normalizes the two possible status changes at a phase labelled two.  It
does not yet exclude them.

## 1. Literature boundary

The literature-first queries and negative result are recorded in
`literature_search_log.md`, section *Two-sided completion at the symbol-two
rotation seam*.  The reusable inputs are CLSW Theorems 7--10, Fine--Wilf,
and the periodic-prefix formula proved in `general_rotation_status.md`.
No located source gives the diagonal completion classification below.

## 2. Setup

Let `P` be a primitive word of length `n>=2` with exact proper circular
profile

```
pc_P=P,                 min(P)=2.
```

Fix a phase `j` labelled two and rotate it to the origin.  Write

```
C=2R,                   Q=R2,
A=C^3,                  D=A[1:].                  (1)
```

Thus `Q` is the next rotation.  Direct cancellation gives

```
D2=Q^3,
A2=2Q^3.                                            (2)
```

Let `f_j` and `f_(j+1)` be the bad/terminal statuses of `A` and `Q^3`.

## 3. Exact local values

### Lemma 1

The four base words satisfy

```
cn(A)=3,
cn(D)=2,
cn(Q^3)=3,
cn(A2)=3.                                           (3)
```

Moreover the next profile label obeys

```
P[j+1] in {2,3}.                                    (4)
```

### Proof

The displayed outer cube gives the first lower bound in (3).  A suffix
power of `A` with exponent at least four has primitive root length less
than `n`, because its powered length is at most `3n`.  It would be a proper
circular power at the phase whose exact value is two.  Hence `cn(A)=3`.

An attaining proper square for that phase has root length below `n` and
powered length below `2n`, so it is visible in the length-`3n-1` word `D`.
Thus `cn(D)>=2`.  An exponent at least three in `D` has root length at most
`(3n-1)/3<n`, again contradicting the exact phase value two.  Hence
`cn(D)=2`.

Put `b=P[j+1]`.  If `b>=4`, take an attaining proper `b`-root at the next
phase.  Looking one root copy earlier at the phase occupied by the final
symbol `2` shows a proper `(b-1)`-power there.  Exactness at that symbol
would give `2>=b-1`, a contradiction.  This proves (4).  The
periodic-prefix formula then gives

```
cn(Q^3)=max(3,b)=3.
```

Equation (2) makes `Q^3` a cube suffix of `A2`, so `cn(A2)>=3`.  Appending
one symbol to `A` raises a curling number by at most one, so only value four
could be larger.  If a fourth-power suffix of `A2` omitted its first
symbol, it would contradict `cn(Q^3)=3`.  Otherwise it would occupy all of
`A2`; its root length `(3n+1)/4` is strictly below `n`.  Deleting the final
symbol leaves a proper circular cube at the phase of value two, another
contradiction.  Hence `cn(A2)=3`.

All four exact values and their independent reference evaluations are
regression-tested in `explore_symbol_two_rotation_seam.py`.

### Lemma 2 (post-promotion reset)

Put

```
H=A3,                    u=cn(H).
```

Then

```
u<=3.                                                  (5)
```

If `H` is bad, then `u` is two or three.  Every primitive maximizing root
of `H` has length `p<n`, and

```
(u-1)p+gcd(p,n)<=n.                                  (6)
```

### Proof

The one-symbol rise bound gives `u<=4`.  A fourth-power root would have
length at most `(3n+1)/4<n`.  Deleting the final `3` would leave a proper
circular cube in `A` at the phase of exact value two, excluding value four.

If `u>=2` and a primitive maximizing root had length `p=n`, the final
symbols in its last two copies would require the two distinct completions
`2` and `3` to agree.  If `p>n`, deleting the final symbol from its
`u`-power leaves a factor of `C^3` with periods `p,n` and length `up-1`.
Since `p>=n+1`, this length reaches the Fine--Wilf threshold
`p+n-gcd(p,n)` and contains a complete length-`p` root.  The resulting
proper gcd period contradicts root primitivity.  Therefore `p<n`.

Compare the primitive maximizing `p`-root of `H=A3` with the displayed
primitive length-`n` cube root of `A2`.  The two words have common prefix
`A` and distinct final symbols.  The exact two-completion Fine--Wilf lemma
from `immediate_power_coupling.md`, Lemma 3, excludes equal roots and gives
(6) in the `p<n` branch.  The opposite branch would require
`2n+gcd(p,n)<=p`, already excluded.

## 4. Ordinary status boundary

Suppose

```
f_j=bad,                 f_(j+1)=terminal.          (7)
```

Then `D` is terminal: its exact first step is `D -> D2=Q^3`.  The bad
cube's first step is `A -> H=A3`.

If this pair `A,D` is selected by globally minimum `tau(D)` among all bad
words with terminal first-symbol deletion, then

```
A3 is bad,                A2 is terminal.           (8)
```

Indeed `A3` is the actual successor of the bad word.  If `A2` were bad,
its deletion `Q^3` would be terminal and

```
tau(Q^3)=tau(D)-1,
```

contradicting the minimum choice.  Thus an ordinary boundary produces the
same-prefix completion fork

```
C^3 3       bad,
C^3 2       terminal,                              (9)
```

where the bad completion has value `u in {2,3}`, a primitive maximizing
root `p<n`, and the exact scale bound (6); the terminal completion has
value three and contains the next rotation cube as its suffix.

## 5. Reverse status boundary

Suppose instead

```
f_j=terminal,             f_(j+1)=bad.             (10)
```

Then `D` is bad and `A=2D` is terminal.  If `A,D` is selected with minimum
`tau(A)` among all terminal one-symbol extensions of bad suffixes, Lemma 2
of `reverse_status_reset.md` applies with exponent three and gives

```
D2=Q^3       bad,
D3           terminal.                            (11)
```

This is the dual same-prefix completion fork.  Here `cn(D)=2`, the bad
completion `D2` is the next rotation cube and has value three, while the
terminal completion has value at most three by the one-symbol rise bound.

## 6. Exact remaining obligation

Every nonconstant cyclic status list has at least one boundary of each
orientation.  `general_rotation_status.md` places all of them at labels
two.  Sections 4--5 show that, after the respective well-founded
selections, they become the two forks

```
ordinary:  C^3 3 bad       / C^3 2 terminal,
reverse:   D 2   bad       / D 3   terminal,
D=(C^3)[1:].                                      (12)
```

The missing theorem must compose these opposite forks or transport a
strict rank between them.  A root-length drop at the ordinary bad
completion is not enough by itself: later left context can create a larger
root.  Nor may the two minimizations be silently identified; one minimizes
deleted-branch hitting time, the other terminal-prefix hitting time.  Any
closure must retain both origins and prove the comparison it uses.

The calibrated finite audit finds all three possible immediate values
`cn(C^3 3)=1,2,3` even under all-cut square coverage, and Q21 realizes each
of them at different symbol-two phases.  Therefore no proof may assume that
the promoted completion has a fixed immediate value.
