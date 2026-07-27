# Circular terminal-prefix drop

This note isolates the circular lemma created by minimal-seed rotation.
It proves two terminal-square branches and records the exact branch that
remains.  It does not prove the full terminal-prefix lemma.

## 1. Circular hypotheses

Let `P` be a nonconstant word of length `n` over `{2,3}`, with
`P[0]=2`.  At a circular cut `j`, let `Cube(j,s)` mean that the
length-`3s` factor ending at the cut is an `s`-root cube, where
`1<=s<n`.  The retained profile equation is

```
P[j]=3  iff  Cube(j,s) holds for some 1<=s<n.       (1)
```

No square requirement away from the selected terminal cut, no
first-copy fitting equation, and no fourth-power exclusion are used in
Sections 3--4.

If a hypothetical minimal critical word has final letter `2`, put

```
T=P[:-1].
```

Minimality gives `cn(T)=1`.  A circular square attaining the terminal
value must cross the distinguished origin.

## 2. Exact terminal-square normal form

Suppose a root-`q` square ends at the terminal cut and

```
2q>|T|=n-1.
```

Put

```
h=n-1-q,
e=2q-(n-1).
```

Then there are nonempty words `X,Y`, with `|X|=h` and `|Y|=e`, such
that

```
T=X Y X,
Y T=(Y X)^2,                                      (2)
suffix_e(P)=Y.                                    (3)
```

Equation (2) is obtained by intersecting the wrapping square with the
length-`n-1` window.  Equation (3) is the same wrapped part read in the
periodic lift.  Since `X` is a suffix of `T`, `cn(T)=1` also gives
`cn(X)=1`.

There is a useful length restriction.  Write `x=|X|` and `y=|Y|`.  If
`y>x+1`, put `z=y-(x+1)` and `A=X2`.  Equation (3) gives

```
Y=suffix_z(Y) A.
```

The letter immediately before the final copy of `A` in `Y` equals the
last letter of `A`, because these positions are `x+1` apart.  Hence
`T=X Y X` ends in

```
(2 X)^2.
```

This contradicts `cn(T)=1`.  Therefore every terminal-square drop has

```
y<=x+1.                                           (4)
```

The equality case in (4) is the `q=r-1` deleted-cube seam.

## 3. The equality case is impossible

### Lemma 1 (early-cut root bound)

Assume (1), `P=T2`, `P[0]=2`, and `cn(T)=1`.  If a proper circular
cube of root length `s` ends at phase `j`, with `0<=j<n`, then

```
s<=j.                                              (5)
```

In particular, no cube ends at phase zero, and a cube ends at phase one
if and only if the final letter of `T` is `2`.

### Proof

Equation (1) and `P[0]=2` first imply that `P` is primitive: a proper
word period would give a proper-root cube at every cut and would make
every displayed letter `3`.

Put `g=gcd(n,s)`.  The Fine--Wilf argument expanded in Theorem 1 below
gives

```
2s+g<n,
```

so `2s<=|T|`.  Represent phase `j` after one complete copy of `P`.  The
context through that cut is

```
T 2 P[:j].
```

The endpoint of `T` is `j+1` positions before the cube endpoint.  If
`s>=j+1`, the length-`2s` factor ending at the endpoint of `T` lies
wholly in the cube: its start is `s-(j+1)` positions to the right of
the cube start.  It is an `s`-root square and, by `2s<=|T|`, it is a
suffix of `T`.  This contradicts `cn(T)=1`, proving (5).

At phase one, (5) leaves only `s=1`.  The three letters before that cut
are the final letter of `T` followed by `22`, which proves the last
assertion.

### Theorem 1

Assume (1), `P[0]=2`, and

```
Y=X2,
P=X Y^2,
T=P[:-1]=X Y X,
cn(T)=1.
```

Then these hypotheses are inconsistent.

### Proof

Put

```
x=|X|,
y=x+1,
n=3y-1.
```

First, `P` is primitive.  If `P=V^k` with `k>=2`, then the proper root
`V` gives a cube at every circular cut.  Equation (1) would make every
letter of `P` equal to `3`, contrary to `P[0]=2`.

The factor of length `3y` ending at cut `y` is a literal cube `Y^3`.
To check its coordinates, use two consecutive copies of `P`.  The
suffix

```
P[y-1:]=Y^2
```

has length `2y`, and

```
P[:y]=X2=Y.
```

Their concatenation is `Y^3`.

The displayed letters at cuts `y` and `1` are equal.  If `x>=2`, both
are `X[1]`.  If `x=1`, both are the appended `2` in `Y=22`.  Equation
(1) at cut `y` therefore makes the common letter `3`, and equation (1)
at cut `1` requires a proper circular cube ending at cut `1`.

Let `s<n` be a root length of such a cube and put `g=gcd(n,s)`.  The
proper circular power-span argument gives

```
2s+g<n.                                           (6)
```

Here is the full periodicity justification for (6).  If

```
3s>=n+s-g,
```

Fine--Wilf gives period `g` to the cube.  If `s=g`, then `g` divides
`n`, and a complete length-`n` conjugate in the cube is an exact power
of a length-`g` word.  If `s>g`, divisibility gives `s>=2g`, so the
Fine--Wilf threshold is at least `n+g`; the `g`-periodic factor then
contains a complete conjugate and its first `g` following letters.
In both cases `P` has circular period `g<n`, contradicting the
primitivity proved above.  Threshold failure is (6).

Represent cut `1` after one full copy of `P`.  The finite context through
that cut is

```
P P[:1]=T 2 2.                                    (7)
```

Suppose first that `s>=2`.  Move the endpoint of the `s`-root cube in
(7) two letters to the left and take the preceding `2s` letters.  This
factor remains inside the cube because

```
2s+2<=3s.
```

It has period `s`, so it is an `s`-root square.  Inequality (6) gives
`2s<=n-2<|T|+1`, so this square is wholly a suffix of `T`.  This
contradicts `cn(T)=1`.

It remains to take `s=1`.  The cube at the end of `T22` makes the final
letter of `T` equal to `2`, hence `X[-1]=2`.  The suffix of `T` beginning
at the last letter of its first displayed copy of `X` is

```
2 X 2 X=(2X)^2.
```

This again contradicts `cn(T)=1`.  No root length remains, so the cube
required at cut `1` cannot exist.  This contradicts (1) and proves the
theorem.

The proof uses only four pieces of profile information: `P[0]=2`,
cube-label equivalence at cuts `y` and `1`, the structural cube at cut
`y`, and `cn(T)=1`.

### Lean 4 statement

The word-level statement to formalize is:

```lean
theorem no_canonical_terminal_drop
    (X : List (Fin 2)) (hX : X ≠ [])
    (P : List (Fin 2))
    (hP : P = X ++ (X ++ [0]) ++ (X ++ [0]))
    (hfirst : P.head? = some 0)
    (hcubeProfile :
      ∀ j : Fin P.length,
        P[j] = 1 ↔
          ∃ s : Nat, 0 < s ∧ s < P.length ∧
            CircularPower P j 3 s)
    (hcurl :
      CurlingNumber (P.dropLast) = 1) :
    False
```

`CircularPower` and `CurlingNumber` are to be instantiated by the final
formalization's definitions.

## 4. The published `XYX` proper-suffix branch is impossible

Chaffin--Linderman--Sloane--Wilks Theorem 9 gives the canonical form

```
Q=X Y X,       cn(Q)=1,       Y is a proper suffix of X
```

when the prefix which raises `Q` is itself a proper suffix of `Q`.
In the terminal-square setting there is also the seam equation

```
suffix_|Y|(Q2)=Y.                                  (8)
```

### Theorem 2

Assume (1), `P[0]=2`, `P=Q2`, `cn(Q)=1`, the displayed `XYX`
factorization above, and (8).  These hypotheses are inconsistent.

### Proof

Since `Y` is a suffix of `X`, the final `|Y|-1` letters of `X` are
`Y[1:]`.  Equation (8) consequently gives

```
Y=Y[1:]2.
```

Comparing positions from left to right forces every letter of `Y` to be
`2`.  If `|Y|>=2`, then `Q`, which ends in `X` and hence in `Y`, ends in
`22`; this contradicts `cn(Q)=1`.  Thus

```
Y=2.
```

Now

```
P=X 2 X 2=(X2)^2.
```

The proper root `X2` gives a cube at every circular cut of `P`.
Equation (1) forces every displayed letter to be `3`, contradicting
`P[0]=2`.

### Lean 4 statement

```lean
theorem no_proper_suffix_terminal_drop
    (X Y Q P : List (Fin 2))
    (hX : X ≠ []) (hY : Y ≠ [])
    (hQ : Q = X ++ Y ++ X)
    (hYSuffixX : IsProperSuffix Y X)
    (hP : P = Q ++ [0])
    (hSeam : P.takeLast Y.length = Y)
    (hfirst : P.head? = some 0)
    (hcubeProfile :
      ∀ j : Fin P.length,
        P[j] = 1 ↔
          ∃ s : Nat, 0 < s ∧ s < P.length ∧
            CircularPower P j 3 s)
    (hcurl : CurlingNumber Q = 1) :
    False
```

## 5. Remaining final-`2` branch

By (4), after Theorems 1--2 the unclosed case has

```
1<=y<=x,
Y=V2,
V=suffix_(y-1)(X),
Y is not a suffix of X.                            (9)
```

Thus the exact remaining obstruction is a one-letter conjugacy defect:
`V` is a genuine proper suffix of `X`, but the contextual prefix which
creates `(YX)^2` is `V2`, not `V`.  Theorem 9 cannot be applied by
silently replacing `V2` with `V`.  A completion must use (1) to repair
the missing `2`, or derive a second `XYX` decomposition and invoke
Theorem 10.

## 6. Executed bounded audit

`research/z3_circular_terminal_prefix.py` encodes only:

1. every cut has a proper square, optionally;
2. equation (1);
3. `P[0]=2`;
4. a selected terminal target power;
5. strict failure of that target power in `P[:-1]`.

With squarefulness at every cut it returned `UNSAT` for every
`2<=n<=50`.  With squarefulness omitted away from the terminal cut it
again returned `UNSAT` for every `2<=n<=50`.  No fitting equation,
fourth-power exclusion, or explicit primitivity clause was present.

`research/z3_critical_prefix_drop.py` independently uses the full
critical synchronization encoding and returned `UNSAT` for every
`2<=n<=80`.  Every SAT path in both scripts is audited against both
curling-number implementations in `curling.py`; no SAT model was found
in these runs.

These are bounded checks and are not used in Theorems 1--2.

## 7. Literature search log

The public searches were performed before the proofs above were
developed further.  Exact queries were:

```
site:arxiv.org everywhere squareful words binary infinite word theorem
site:arxiv.org squareful words every position begins with square binary classification
site:arxiv.org runs periodicity Fine Wilf adjacent squares word equations theorem
site:arxiv.org 1212.6102 curling numbers integer sequences
Kalle Saari squareful words theorem minimal squares ultimately periodic pdf
site:arxiv.org Kalle Saari squareful optimal squareful six minimal squares
"Everywhere α-repetitive" Saari theorem pdf
site:doria.fi Saari squareful words thesis
```

Sources and scope:

* Chaffin, Linderman, Sloane and Wilks, *On Curling Numbers of Integer
  Sequences*, arXiv:1212.6102, Theorem 5 states the Fine--Wilf
  common-suffix form used in Section 3.  Theorem 9 states that if
  `cn(S)=1`, `cn(TS)>1`, and `T` is a proper suffix of `S`, then
  `S=XYX`, `cn(X)=1`, `T` is a suffix of `Y`, and `Y` is a proper
  suffix of `X`.  Theorem 10 proves uniqueness of this canonical
  decomposition.  Theorem 9 does not apply to the unresolved defect
  (9), because `V2`, rather than `V`, is the prefix producing the
  wrapping square.
* Currie, Rampersad and Shallit, *Infinite words containing squares at
  every position*, arXiv:0803.1189, Theorems 6--7 construct binary
  infinite words with a square beginning at every position while
  avoiding every exponent above any prescribed `alpha>2`.  Therefore
  bare everywhere-squarefulness cannot supply the needed cube.
* Peltomäki and Whiteland, *A square root map on Sturmian words*,
  arXiv:1509.06349, records Saari's classification of optimal
  squareful words: an aperiodic optimal squareful word has six minimal
  squares, while fewer than six forces ultimate periodicity.  Our
  periodic circular word need not be optimal, so that classification
  does not imply the terminal-prefix conclusion.
* Crochemore, *On the runs conjecture*, arXiv:0802.2829, uses the
  Fine--Wilf consequence that powers of two primitive roots cannot
  overlap beyond the sum of their root lengths.  This supports the
  span calculation in Section 3, but it does not encode the
  letter/cube equivalence (1).

No located theorem repairs the one-letter defect (9).  Theorems 1--2
are additional word arguments beyond the cited results.
