# The forced Q21 two-cycle

This note isolates the finite lemma needed to close the Q21 branch under
the hypothesis that every primitive cube root has length at most 21.  It
uses a strict relaxation of exact fixedness: square existence and
fourth-power exclusion are not used in the transition classification.

Put

```
U = 223232223222322322232,
B = 223222323222322232232.
```

Both words have length 21.

## 1. The symbolic phase equations

For a binary word `A`, a cut `c`, and `1 <= r <= 21`, write

```
C(c,r) :=
  A[c-3r:c-2r] = A[c-2r:c-r] = A[c-r:c].
```

Thus `C(c,r)` is the explicit conjunction of the `2r` coordinate
equalities saying that a root-`r` cube ends at `c`.

Let `L` be the final 63 symbols preceding a displayed generated word `D`,
and put `A=LD`.  At displayed phase `j`, retain only the equation

```
H_D(j) :=
  (D[j] = 3) <-> OR_{r=1}^{21} C(63+j,r).              (1)
```

Exact fixedness under the global root bound 21 implies (1).  The reverse
implication at a 2-phase is the no-cube condition; the forward implication
at a 3-phase is cube existence.  No positive square equation, no
no-fourth equation, and no constraint involving a root above 21 is used
below.

Every cube in (1) reads at most 63 preceding symbols.  Therefore the truth
of every `H(j)` is determined by a 63-symbol left suffix.  Replacing an
arbitrary earlier history by 63 symbolic bits loses no information used by
(1).

For a current root `P`, a 3-phase `t`, and a proposed predecessor length
`q`, introduce a symbolic root `Q` of length `q` and the displayed word

```
D(P,t,q) = Q^3 P^3[t:].
```

The start of `P^3` is at coordinate `3q-t`, so impose the overlap equations

```
D[3q-t:3q] = P[:t].                                    (2)
```

All symbols of `Q^3` and the remainder of `P^3` are generated symbols.
Consequently every displayed coordinate of `D` satisfies (1), with
`A=LD(P,t,q)`.

Equations (1)--(2) are a finite Boolean formula: `q+63` binary variables
and a finite list of coordinate equalities.  The script
`certify_q21_two_cycle.py` constructs this formula directly.  It also
shrinks every rejected branch to the phase sets in the next table.

## 2. Exhaustive transition certificate

For `P=U,t=4`, the following sets of `H`-phases are inconsistent with
(2).  A dash means that (2) itself is inconsistent.

```
q   inconsistent H-phases
1   -
2   -
3   3,4,6,7,8
4   63
5   7,16
6   9,19
7   12,18,19,20,79
8   14,21,22,23,82
9   25,26,85
10  28,29,88
11  19,31,32,91
12  34,35,94
13  7,37,38,40,97
14  25,40,41,100
15  26,43,44,46,103
16  28,33,46,47,49,106
17  31,38,49,50,52,109
18  15,38,39,52,53,112
19  39,42,44,46,55,56,115
20  14,27,35,37,41,58,59,118
```

For `P=B,t=8`, the corresponding certificate is

```
q   inconsistent H-phases
1   -
2   -
3   -
4   63
5   -
6   -
7   8,14,15,20
8   12
9   11,28
10  15,31,84
11  8,27,32,87
12  30,35,90
13  27,33,38,93
14  36,41,96
15  22,39,44,46,99
16  33,42,47,102
17  35,36,38,45,50,52,105
18  14,37,48,53,108
19  26,32,40,42,56,58,111
20  13,17,34,41,59,114
```

These tables exhaust `1 <= q < 21`.  They do not select one satisfying
model and infer uniqueness from it: every entry is an UNSAT subformula of
the coordinate equations (1)--(2).

At `q=21`, the same equations have one root assignment.  The following
sequential forcing tables expose that assignment bit by bit.  Each row
states: assuming all preceding rows, the overlap equations and the listed
`H`-phases force the displayed root bit.  Empty phase sets are bits forced
by overlap alone.

For `U,t=4`, the forced root is `B`:

```
bit=value   forcing H-phases
17=2        -
18=2        -
19=3        -
20=2        -
0=2         64
16=3        121
7=2         40,41
13=2        61,62
1=2         43,62
2=3         23
3=2         45,62
4=2         25,62
5=2         47,62
6=3         6
8=3         29
9=2         30,62
10=2        31,62
11=2        32,62
12=3        12
14=2        17
15=2        36,62
```

For `B,t=8`, the forced root is `U`:

```
bit=value   forcing H-phases
13=2        -
14=2        -
15=3        -
16=2        -
17=2        -
18=2        -
19=3        -
20=2        -
0=2         64
12=3        117
1=2         43,62
2=3         23
3=2         24,62
4=3         25
5=2         26,62
6=2         27,62
7=2         28,62
8=3         8
9=2         30,62
10=2        13
11=2        32,62
```

Expanding any row uses only (1): each positive phase chooses one of the 21
displayed cube equations `C(j,r)`, and each negative phase rejects all 21.
The executable certificate checks every disjunct and every binary root
assignment.  Reversing any forced bit makes the listed phase subformula
UNSAT.

It follows that generated predecessor cubes obey the forced transitions

```
U at phase 4  <-59-  B,
B at phase 8  <-55-  U.                                (3)
```

The displacements are `3*21-4=59` and `3*21-8=55`.

## 3. Geometry of the two-cycle

Place a predecessor `U^3` at `[0,63)`.  Equation (3) places the intervening
`B^3` at `[55,118)` and the next `U^3` at `[114,177)`.

The first overlap has length eight and the second has length four:

```
(U^3)[-8:] = B[:8],
(B^3)[-4:] = U[:4].
```

The intervals have no gap.  Their union forces the length-114 bridge

```
W =
223232223222322322232223232223222322322232223232223222322322232322232223223222322232322232223223222322232322232223
```

The script `check_q21_two_cycle.py` constructs the word by overlapping the
three cubes and verifies that its length is 114.  Two predecessor
transitions reproduce the same root `U` translated by 114, so iteration of
(3) forces consecutive copies of `W`.

After four iterations of the two-step cycle, the state immediately before
the next `U[0]=2` ends in `W^4`.  Hence its curling number is at least four,
contradicting the displayed value two.  The independently executed
reference implementation reports

```
cn(W^4) = 4.
```

At the `U^3` endpoint, the corresponding suffix is four copies of the
63-shifted bridge.  The same executed audit reports

```
cn(rot_63(W)^4) = 4,
```

which also contradicts the selected value-three endpoint.

## 4. Ambient conclusions

In a bi-infinite or circular fixed-profile lift, (3) can be iterated four
times, so the Q21 branch is impossible.

For a one-sided fixed-origin tower, the same conclusion holds whenever a
selected U/B node lies at least four complete 114-symbol cycles beyond the
seed boundary.  If such nodes occur at unbounded distances from the seed,
choose one beyond that bound and apply the same finite suffix argument.

This lemma does not assert that an arbitrary single U/B node near the
initial seed is impossible: its generated ancestry can terminate inside
the arbitrary seed.  A global application must supply either the
bi-infinite/circular lift or an unbounded family of fixed-origin nodes.
