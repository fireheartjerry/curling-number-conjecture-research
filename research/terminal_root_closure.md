# Terminal-root square rescue

This note isolates the finite leaves produced by the aligned
third-copy halving argument.  It proves the exact predecessor-square
dichotomy at each leaf and records the remaining closure problem.

## 1. Terminal roots

In the binary fixed-profile setting there are no factors `2222` or
`333`: either would put a fourth power or a cube at a cut labelled at
most `3` or `2`, respectively.

After the componentwise third-copy descent, a terminal primitive cube
root has no internal `3`, except that a root ending at the first cut of
a common double component may have its final symbol `3`.  Consequently
the possible roots are

```
U in {2, 23, 223, 2223}.                         (1)
```

The all-`2` case is primitive only at length one.  In the final-`3`
case the preceding run of `2` symbols has length at most three.

For each root in (1), define the marker

```
T_U=U^3 3 2.                                     (2)
```

The last two symbols are the terminal `33` component and its following
`2` in the final-`3` cases.  For `U=2`, (2) is the unary terminal cube
followed by its `3,2` marker.

## 2. Exact marker data

The four markers are

```
U=2:       T=22232,          |T|=5
U=23:      T=23232332,       |T|=8
U=223:     T=22322322332,    |T|=11
U=2223:    T=22232223222332, |T|=14.
```

Each marker has curling number one as a standalone word, and its only
nonempty proper border is its final/initial symbol `2`.

These are finite statements, not pattern extrapolations.
`research/check_terminal_markers.py` compares both curling-number
implementations, tests every possible square-root length, and tests
every proper border length for all four words.

## 3. Short-or-marker-parent dichotomy

### Lemma 1

Let `T` be one of the four markers, put `L=|T|`, and let a longer word
`S` end in `T`.  If `S` has a square suffix with root length `q`, then

```
q=L-1  or  q>=L.                                  (3)
```

In the first case,

```
S ends in (T[1:])^2,                              (4)
```

so the `L-2` symbols immediately preceding the displayed occurrence of
`T` are exactly `T[1:-1]`.  In the second case, the square copies the
whole marker `T` to an occurrence ending `q` positions earlier.

### Proof

If `q<L`, period `q` on the square suffix gives

```
T[0:L-q]=T[q:L].
```

Thus `T` has a border of length `L-q`.  The border computation in
Section 2 leaves only `L-q=1`, proving `q=L-1`.

Put `V=T[1:]`.  The length-one border says `T[0]=T[-1]`, so the final
`L` symbols of `V^2` are

```
T[-1] T[1:]=T.
```

This proves (4), including the asserted preceding factor.  If `q>=L`,
shifting the final `L` symbols back by the square period copies all of
`T`, which is the marker-parent alternative.

The standalone value `cn(T)=1` shows directly that no square suffix is
contained wholly inside the marker.  Lemma 1 is stronger: it classifies
every external square, regardless of the earlier context.

## 4. The `U=2` Q21 macro

For `T=22232`, the short root is

```
T[1:]=2232
```

of length four.  This is the period-four child used by the length-21
fixed profile

```
Q=232223222322322232223.
```

There are four circular occurrences of `T` in `Q`.  Direct root
enumeration gives

```
end cut 1:   square roots 4,11
end cut 7:   square root  6
end cut 11:  square roots 4,10
end cut 18:  square roots 4,7.
```

Thus the other predecessor periods are `6,7,10,11`; each is at least
`|T|` and copies a complete marker, exactly as Lemma 1 predicts.  This
is the concrete terminal macro which a closure proof is allowed to
produce.

## 5. Leftmost-loss lemma in a common fitting window

The long-parent alternative in Lemma 1 is well founded when all of the
rescues under discussion fit in one fixed left window.  This is the
pointed hypothesis which is absent from an arbitrary circular lift.

### Lemma 2

Fix integers `a<b` and a word `Z` on `[a,b)`.  Assume that at every cut
`t` with `a<t<b` used below,

```
cn(Z[a:t])=Z[t] in {2,3}.                       (5)
```

Thus every maximizing witness in (5) begins at or after the same fixed
left endpoint `a`.

Let `W`, of length `h>3u`, occur ending at at least one of those cuts,
and assume

```
cn(W)=1.
```

Choose the leftmost such occurrence of `W` whose endpoint is below
`b`.  There are exactly two alternatives:

1. its exact value is three and every maximizing cube root `r` satisfies
   `r>h/3>u`;
2. its exact value is two and every maximizing square root `q` satisfies

```
h/2 < q < h,                                   (6)
```

   while `h-q` is a nonempty proper border of `W`.

In particular, if no cube root longer than `u` is allowed, alternative
2 holds; if `W` has no proper border, a cube root longer than `u` is
forced.

### Proof

Suppose the value is three and let `r` be a maximizing cube root.  If
`3r<=h`, the cube is a suffix wholly contained in `W`, contradicting
`cn(W)=1`.  Hence `3r>h>3u`, which is alternative 1.

It remains to consider value two.  Let `q` be a maximizing square root.
If `2q<=h`, that square
is wholly contained in `W`, again contradicting `cn(W)=1`.  Thus
`2q>h`.

Suppose `q>=h`.  The two equal length-`q` blocks of the square copy the
final length-`h` word `W` to an occurrence ending `q` positions
earlier.  Its left endpoint is still at or after `a`: the complete
square begins at or after `a`, and `q>=h`.  This contradicts the choice
of the leftmost occurrence.  Therefore `q<h`.

The final `h` symbols lie in a word of period `q`.  Their first `h-q`
symbols equal their final `h-q` symbols, so `h-q` is the asserted
proper border.  This proves (6) and the lemma.

Lemma 2 is an exact rank: the endpoint of a long rescue decreases until
the first occurrence in the fixed window, where a proper border is
forced.  It does not claim that the rank survives when a translated
witness crosses the fixed left boundary.

## 6. Propagation-or-ascent dichotomy

### Lemma 3

Fix a reference scale `u`.  Suppose an ambient state
ends in a word `A` with

```
|A|>3u,       cn(A) in {2,3}.
```

If `cn(A)=3`, its ambient exact value is three.  If `cn(A)=2`, either
its ambient exact value is two, or the ambient state has a cube root
strictly longer than `u`.  A cube root longer than `u` displayed
inside `A` is also such a strict ascent.

### Proof

Suffix monotonicity makes the ambient value at least `cn(A)`.  The
ambient alphabet is `{2,3}`, so equality is forced when `cn(A)=3`.

If `cn(A)=2` but the ambient value were three, take a maximizing cube
root `r` at that cut.  If `r<=u`, then
`3r<=3u<|A|`, so the cube is wholly contained in `A`.  This would give
`cn(A)>=3`, a contradiction.  Therefore `r>u`.

The final assertion follows because every displayed cube suffix of `A`
is also a cube suffix of the ambient state.

Thus an executed standalone trace whose states all have length above
`3u` either follows its standalone next symbol, or exposes a cube root
strictly above the reference scale.

## 7. Exact terminal transition graph

Let the displayed terminal cube be `U^3`, put `u=|U|`, and suppose the
marker and every loss rescue below lie in one common fitting window.

Apply Lemma 2 first to the marker `T_U`.  Section 2 gives
`cn(T_U)=1`, `|T_U|=3u+2>3u`, and the sole border length one.
Lemma 2 either already exposes a cube root longer than `u`, or the
leftmost marker occurrence has the forced square suffix

```
(T_U[1:])^2.                                    (7)
```

Every state in the following table has length above `3u`.  Lemma 3 says
that any departure from a displayed append exposes a cube root longer
than `u`.  If no such departure occurs, root sets in the final column
are the complete maximizing root-length sets at the displayed cube.

```
U       first forced branch                         outcome
2       append 2232                                 cube roots {4}
23      append 223; reach loss W_17, borders {1}    see below
223     append 223; reach loss W_23, borders {2}    see below
2223    append 2232223222332                         cube roots {13}
```

For `U=23`, Lemma 2 at `W_17` forces square-root length
`17-1=16`.  Starting from `(W_17[1:])^2`, the forced append word is
`2223222`, after which the complete cube-root set is `{1,4}`.

For `U=223`, Lemma 2 at `W_23` forces square-root length
`23-2=21`.  Starting from `(W_23[2:])^2`, the forced append word is
again `2223222`, after which the complete cube-root set is `{1,4}`.

In all four rows a cube root strictly longer than `u` is produced.
Therefore every terminal cube with root in (1), under the common-window
hypotheses, has a strict cube-scale ascent.  If the terminal cube was
globally maximal, this is an immediate contradiction.  For a terminal
descendant below a larger parent, the ascent is allowed and must be
charged to an ancestor or to a separate endpoint rank.

The transition graph has no unclassified numerical branch:

```
T_U --leftmost/border 1--> (T_U[1:])^2

U=2 ----------------------> larger cube 4
U=2223 -------------------> larger cube 13
U=23 ----> W_17 --border 1/root 16--> larger cube 4
U=223 ---> W_23 --border 2/root 21--> larger cube 4.
```

The long rescue periods have not been bounded or enumerated.  Lemma 2
eliminates all of them at once by strict decrease of their copied
occurrence endpoints.  The exact remaining global obstruction is a
window exit: a canonical fitting witness translated to the chosen lift
may begin before `a`.  In that event the endpoint rank used in Lemma 2
is unavailable.  No terminal overlap case remains once common fitting
has been established.

All finite data in Sections 2, 4, and 7 are recomputed by
`research/check_terminal_markers.py` using both curling-number
implementations.

## 8. The ascent contains a later unary terminal leaf

The strict scale ascent in Section 7 has additional pointed geometry.
It is not merely an allowed cube somewhere below a larger ancestor.

The exposed root is

```
B_4  = 2232
```

in the `U=2` row,

```
B_13 = 2232223222332
```

in the `U=2223` row, and is the conjugate

```
B'_4 = 3222
```

in the `U=23,223` rows.  At phase two of `B_4` and `B_13`, and at
phase zero of `B'_4`, the same circular boundary identity holds:

```
B[phase-3:phase+2] = 22232.                     (8)
```

Here the slice is circular.  The first three symbols give a unary cube,
and the last two symbols are its `3,2` marker.  Consequently the
certified cut is itself a terminal unary cube.

Let `c` be the endpoint of the selected terminal `U`-cube occurrence.
For `U=2` and `U=2223`, the exposed `B`-cube ends at

```
e=c+2+|B|.
```

Its phase-two unary child ends at

```
e-|B|+2=c+4.                                    (9)
```

For `U=23` and `U=223`, let `s` be the endpoint of the selected loss
occurrence `W_17` or `W_23`.  The exact copy of the original leaf inside
that loss ends at `s-5`.  The exposed `B'_4` cube ends after seven
appends, at `s+7`; its phase-zero unary child therefore ends at

```
(s+7)-4=s+3=(s-5)+8.                           (10)
```

Equations (9)--(10) show that a completed terminal episode maps the
particular copied leaf used by the episode to a later unary terminal
leaf: the endpoint increment is exactly four or eight.  This remains true
when Lemma 2 first moves to an earlier copied marker or loss: coordinates
in (9)--(10) are measured from that selected copied occurrence.

The full exposed cubes certify more unary leaves than those single
targets.  Measuring every endpoint from the selected typed source leaf,
the complete list of `22232` markers whose five symbols lie wholly in
the exposed cube is

```
source U      exposed root                 unary endpoint offsets
2             2232                         0, 4
23 or 223     3222                         4, 8
2223          2232223222332                -18, -9, -5, 4, 8.
```

The negative offsets in the last row are genuine companion markers in
the first and second copies of the exposed root; they are not inferred
by circular continuation outside the displayed cube.  The checker
enumerates every root phase and requires the complete five-symbol marker
to lie inside the cube before recording it.

Hence the exposed root cannot be dismissed merely because its length is
below a global ancestor scale.  It advances the distinguished endpoint
inside its own exposed cube.  To turn this into a global well-founded
rank one still has to prove that the interval through the new unary
marker remains in the same common fitting window.  If it does, repeated
terminal completion strictly increases the selected leaf endpoint; if
it does not, the precise remaining branch is a right-window exit.

## 9. Complete unary short-branch interruptions

The unary leaf admits a sharper finite graph.  Let its cube end at cut
`c`, so its marker `22232` ends at cut `c+2`.  Put

```
V=2232,       A_k=V^2 (2232)[0:k],       0<=k<=4.
```

The standalone values at `A_0,A_1,A_2,A_3,A_4` are, respectively,

```
2,2,3,2,3.
```

At `A_4` the unique maximizing root has length four and the suffix is
`V^3`; this is the completed `c -> c+4` transition from Section 8.

Only `A_0,A_1,A_3` can be raised contextually from two to three.  If a
cube root `q<|A_k|` causes that raise, then `3q>|A_k|`, since otherwise
the cube would already be visible in `A_k`.  Hence `q` is a period of
all of `A_k`, and `|A_k|-q` is a proper border.  Exhausting the proper
borders and discarding nonprimitive roots gives:

```
k   |A_k|   primitive cube roots     terminal-leaf endpoint offsets
0      8    7:2322232, 4:2232        0
1      9    7:3222322, 4:2322        0
3     11    4:2223                   adjacent 33 at offset 4
```

For `k=0,1`, each listed root has a complete `22232` marker in its
third copy at endpoint offset zero.  Thus every proper short cube
interruption at those two cuts terminalizes back to the source unary
leaf.  The same phase in the second root copy is another complete
terminal marker.  If the cube root has length `q`, this supplies a
second unary leaf at endpoint `c-q`.  Hence a local return also creates
a strict backward endpoint edge of length four or seven; it is not an
isolated zero-displacement event.

The complete cube gives the stronger companion table

```
interrupting q=4 at k=0 or 1:   endpoints c-4, c
interrupting q=7 at k=0 or 1:   endpoints c-14, c-7, c
interrupting q=4 at k=3:        terminal endpoints c-4, c,
                                adjacent-double endpoint c+4.
```

In the `k=3` row the first two copies of `2223` are followed by the
initial `2` of another root copy and therefore have complete terminal
markers.  The third is followed by the ambient appended `3`, producing
the stated double.

For `k=3`, the root `2223` ends exactly at its final `3`.  Its circular
continuation would be `2`, but the actual ambient label at the cube
endpoint is `3`.  Therefore the unary cube at offset four is followed
by `33`, not by the terminal marker `32`.  This is precisely the
adjacent-double branch; treating the root circularly at that boundary
would incorrectly classify it as a later terminal leaf.

The other border candidates at `k=1,3` have root length eight and are
squares of a length-four word.  Cubing either candidate would give
exponent six, contradicting the binary exact profile, so they are not
admissible maximizing cube roots.

If an interrupting root has `q>=|A_k|`, it copies the entire state
`A_k`, including its distinguished unary leaf, to an earlier endpoint.
Consequently every unary short branch has exactly four outcomes:

1. a completed terminal edge `c -> c+4`;
2. a short cube returning to the same terminal leaf;
3. a copy-parent edge to an earlier unary leaf, supplied either by a
   long copied state or by the second copy of a short return cube; or
4. the adjacent-`33` boundary at the last precompletion cut.

The finite table and every standalone value are executed in
`research/check_terminal_markers.py`.

## 10. Origin-crossing long edges and winding

The long edge at the marker itself has an exact pointed lift.  Normalize
the distinguished deleted window to start at `1-n`, let the unary leaf
endpoint satisfy `0<=c<n`, and let an exponent `e in {2,3}` rescue the
marker at cut `c+2` with root `q>=5`.  Fitting says

```
c+2-eq >= 1-n.                                  (11)
```

The copied unary marker starts at `c-q-3`.  Its distance from the start
of the powered suffix is

```
(c-q-3)-(c+2-eq)=(e-1)q-5 >= 0.                (12)
```

Thus the copied marker, not only the copied endpoint, remains wholly in
the same fitting window.  Put `d=c-q`.

If `d>=0`, the endpoint rank strictly decreases in the distinguished
lift.  If `d<0`, put `f=d+n`; this is an origin-crossing edge from phase
`c` to phase `f`.  Substitution of `q=c+n-f` into (11) gives the exact
phase constraints

```
2f >= n+c-1       when e=2,
3f >= 2n+2c-1     when e=3.                    (13)
```

Hence every failure of strict endpoint descent is an explicitly fitting
edge crossing the distinguished origin and landing in the high part of
the next circular lift.

For a directed cycle of long marker-parent edges, write

```
c_(i+1)=c_i-q_i+epsilon_i n,
epsilon_i in {0,1}.
```

Summing around the cycle gives

```
sum_i q_i = w n,       w=sum_i epsilon_i >=1.   (14)
```

Equation (14) is the winding identity for the endpoint graph.  A cycle
cannot consist only of nonwrapping descent edges.  Equations
(11)--(14) do not by themselves eliminate a winding cycle: the
short-cube return in Section 9 has zero endpoint displacement and is a
real branch.

## 11. Q21 calibration and the exact uniqueness boundary

For the length-21 fixed profile with run code `133233`, the unary leaf
endpoints and their executed local transitions are

```
leaf 5  -- long square root 6 --> leaf 20
leaf 9  -- step-1 cube root 4 --> leaf 9
leaf 16 -- completed short path --> leaf 20
leaf 20 -- marker cube root 4 --> leaf 20.
```

This realizes all three non-double outcomes in Section 9.  In
particular, a short cube ascent can be an allowed ancestor which
terminalizes to the same leaf; scale ascent alone is not a well-founded
rank.  Its second root copy supplies the missing backward edges:

```
leaf 20 -- root-copy displacement 4 --> leaf 16,
leaf 9  -- root-copy displacement 4 --> leaf 5.
```

Thus `20 -> 16 -> 20` is the exact short-return/completed-path
two-cycle, while `9 -> 5 -> 20` feeds it.  The first-copy boundary of
each displayed cube is not automatically another terminal leaf; closing
that boundary is precisely where the terminal gadget overlay, rather
than a single-root argument, is needed.

The endpoint and winding equations alone do not prove that this
length-21 graph is unique.  The additional load-bearing hypothesis is
that every defect has a fitting terminal gadget, together with square
coverage, no cube at a `2`-cut, and no fourth power at a `3`-cut.  Under
exactly those hypotheses, Section 9 of
`research/gadget_cycle_structure.md` proves that the primitive run code
is `133233` up to rotation.  Thus Q21 is the unique fully terminal
cycle, but only after the complete defect-graph hypotheses have been
established.

The remaining globalization problem is now exact.  A nonterminal
halving node must be assigned either:

* a common-window terminal completion governed by Sections 7--10;
* an origin-crossing edge satisfying (13);
* or the adjacent-`33` boundary from Section 9.

It remains to prove that repeated origin crossings cannot keep replacing
nonterminal nodes without eventually entering the fully terminal
classification.  The local endpoint graph does not supply that claim.

## 12. The actual fixed two-copy window

For a critically synchronized word `P` of length `n`, the common window
needed above is not hypothetical.  Index the periodic lift by

```
Z[t]=P[t mod n],       1-n <= t < 2n.
```

The deleted synchronization equations for copies one and two say
exactly

```
cn(Z[1-n:t])=Z[t] in {2,3},       0<=t<2n.       (15)
```

Thus `[1-n,2n)` has a fixed left boundary and a generated part
`[0,2n)`.  The seed part `[1-n,0)` has no cut equation of the form
(15); this distinction is essential.

Every proper circular cube can be placed wholly in this slab.  If its
root length is `p<n` and it ends at canonical phase `j`, the proper-power
span lemma gives

```
3p < n+p-gcd(n,p) < 2n.
```

Place the occurrence at the second-copy endpoint `n+j`.  Its start is
an integer strictly above `j-n`, hence at least `1-n`, and its endpoint
is below `2n`.  A globally maximal cube and every child produced by
containment can therefore be assigned this same lift.  The alignment
translations used in the halving hierarchy remain inside the parent
cube and preserve the assignment.

A terminal child cut is strictly before its parent endpoint.  If it
were only one position before that endpoint, the child marker would
require the parent endpoint label to be `2`, whereas the parent cube
endpoint is labelled `3`.  Thus the complete two-symbol terminal marker
also remains in the slab.  Only the later forward continuation can
cross the right boundary.

There is a generated-window version of Lemma 2.  Let `W` have
`cn(W)=1` and length `h>3u`, and suppose a complete occurrence ends at
a generated cut.  Choose the least endpoint `t>=0` of such an occurrence
in the slab.

* If `Z[t]=3`, every cube root `r` there satisfies
  `3r>h`, hence `r>u`.
* If `Z[t]=2` and a maximizing square root has `q<h`, then
  `h-q` is a proper border of `W`.
* If `Z[t]=2` and `q>=h`, the square copies `W` to an occurrence ending
  at `d=t-q`.  Its start remains in the slab because

  ```
  (d-h)-(t-2q)=q-h>=0.
  ```

  Minimality of `t` forces `d<0`.  This is a seed-entry edge, not a
  further generated occurrence.

These alternatives exhaust the rescue.  In particular, a long
translation never silently loses the word being ranked: either its
endpoint remains generated and contradicts minimality, or the complete
copied word is certified inside the finite seed part.

Seed entry is still a generated circular node after normalization.
The copied occurrence has

```
d-h >= 1-n,       -n<d<0.
```

After translation by `+n`, the same complete word begins at or after
one and ends at `f=d+n in (0,n)`.  Equation (15) therefore applies at
its normalized endpoint.  What was a left-window exit in one lift is
exactly the fitting origin-crossing edge of Section 10 in the next
lift.

The border replacement is preserved as well.  If `b=h-q` is the forced
border, the selected state ends in `(W[b:])^2` at the same generated
cut.  Every subsequent table step remains governed by (15) until one of
the following explicit exits occurs:

1. a contextual cube ascent;
2. a new unary leaf endpoint at `c+4` or `c+8`;
3. a seed-entry endpoint below zero;
4. a right-window endpoint at least `2n`; or
5. the adjacent-`33` branch.

For every hierarchy node just assigned to this slab, containment
translations preserve the fixed left boundary.  The phase-alignment
translation in Section 10 of `research/gadget_cycle_structure.md` stays
inside the parent cube, so it also stays in the slab.  What is not
automatic is that the forward terminal continuation remains below
`2n`; item 4 records that boundary case rather than assuming it away.

Item 4 also normalizes without losing the marker.  Reduce the new
endpoint modulo `n`, then choose its representative in `[n,2n)`.
Periodicity copies the complete unary marker to that representative,
which is a generated cut governed by (15).  Thus both left and right
window exits become wrap edges in the finite circular endpoint graph;
neither discards the ranked terminal occurrence.

This supplies the requested endpoint rank on every common-window node:
use its integer endpoint in `[0,2n)`, not its circular phase.  Copy
parents strictly decrease that endpoint until seed entry, while completed
terminal paths increase it by four or eight until right exit.  After
normalization, a circular cycle with copy lengths `q_i` and completion
increments `delta_j in {4,8}` satisfies the signed winding identity

```
sum_j delta_j - sum_i q_i = w n                (16)
```

for an integer `w`; every short cube return also supplies a backward
copy edge and belongs in the second sum.  Eliminating mixed cycles
satisfying (11), (13), and (16), outside the fully terminal Q21 case,
remains the global missing lemma.

## 13. Gap-four pairs are atomic under every local rescue

The unary marker has a useful overlap consequence which is stronger than
an endpoint potential.

### Lemma 4

Let two distinct complete unary markers `22232` occur in one linear lift,
and let their unary-cube endpoints differ by `g>0`.  Then

```
g>=4.                                           (17)
```

If three unary endpoints are `c,c+4,c+8`, the exact binary profile fails:
the word ending immediately before the next required `2` contains

```
(2223)^3,
```

so its curling number is at least three although that next label is two.
Consequently a chain of gap-four marker edges has at most two vertices.

### Proof

A unary marker whose cube ends at `c` occupies the five symbol positions
from `c-3` through `c+1`.  If a second marker ends at `c+g` with
`1<=g<=3`, the overlap equality says that `22232` has a border of length
`5-g`, namely length four, three, or two.  Section 2 gives the complete
proper-border set `{1}`, proving (17).

For endpoints `c,c+4,c+8`, the three overlapping markers force the
thirteen-symbol word

```
2223222322232 = (2223)^3 2.
```

At the cut between the displayed cube and its last symbol, the suffix
cube certifies curling number at least three while the displayed next
symbol is two.  This contradicts the exact profile equation at that cut.

### Lemma 5

Suppose unary leaves end at `c-4` and `c`, and consider any square or
cube rescue of the right marker, which ends at cut `c+2`.  If its root
length is `q`, then exactly one of the following holds:

1. `q=4`, the short root `2232`;
2. `q>=9`, and the powered suffix copies the complete gap-four pair to
   unary endpoints `c-4-q,c-q`.

Roots `5<=q<=8` are impossible.

### Proof

Lemma 1 gives `q=4` or `q>=5`.  For every `q>=5`, periodicity copies the
right marker to a unary marker ending at `c-q`.

For `q=5,6,7`, its endpoint is at distance `1,2,3`, respectively, from
the existing left endpoint `c-4`; Lemma 4 excludes these cases.  For
`q=8`, the three endpoints

```
c-8, c-4, c
```

form the forbidden gap-four chain of Lemma 4.

The union of the two existing markers occupies exactly the nine
positions from `c-7` through `c+1`.  When `q>=9`, this union lies in the
last root block of the powered suffix.  Translation by `-q` therefore
copies both complete markers, giving the stated pair.

Lemma 5 makes a gap-four pair an atomic object: every long rescue moves
the pair together.  The remaining short root also has an exact finite
classification.

### Lemma 6

Under the hypotheses of Lemma 5, follow the `q=4` short root unless an
ambient cube raises one of the standalone value-two states
`A_0,A_1,A_3` of Section 9.

* A root-seven interruption at `A_0` or `A_1` is impossible.
* A root-four interruption at `A_0` or `A_1` returns to the existing
  pair.
* Completing the short path is impossible.
* The root-four interruption at `A_3` produces the adjacent-`33`
  boundary at endpoint `c+4`.
* Every remaining admissible interrupting root copies the complete
  gap-four pair to an earlier pair.

Thus the local transition alphabet of a gap-four pair is:

```
root-four return,
adjacent-33 boundary,
or pair-parent copy.
```

### Proof

The companion table in Section 9 is measured from the right leaf `c`.
A root-seven interruption certifies a unary leaf at `c-7`.  Its distance
from the existing left leaf `c-4` is three, contradicting Lemma 4.

A root-four interruption certifies leaves at `c-4,c`, so it returns to
the existing pair.  Successful completion would certify the new leaf
`c+4`, producing the forbidden chain `c-4,c,c+4`.  At `A_3`, Section 9
instead gives the adjacent-double endpoint `c+4`.

It remains to audit roots which cross the left boundary of `A_k`.  At
`A_0`, root length eight is the nonprimitive word `(2232)^2`; its cube
would give exponent six.  At `A_1` and `A_3`, the proper root-length-eight
candidates are likewise squares, and are excluded for the same reason.

For a root reaching left of `A_k`, every length at least `9+k` contains
the entire nine-symbol pair and hence is a pair-parent copy.  The only
roots which miss exactly the first symbol of the pair are therefore

```
k=1, q=9:    223222322,
k=3, q=11:   22322232223.
```

Their cubes have the following executed internal profile violations:

```
root 223222322:
    cut 10 has cn 3 > label 2
    cut 11 has cn 4 > label 3
    cut 19 has cn 3 > label 2
    cut 20 has cn 4 > label 3

root 22322232223:
    cut 12 has cn 3 > label 2
    cut 23 has cn 3 > label 2.
```

For the first root, the last violation is at the existing left unary
endpoint `c-4`.  For the second, the last violation is at cut `c-5`,
inside the existing left marker.  If the displayed cube crosses the
seed boundary of the fixed slab, translate the prefix ending at that
violating cut by `+n`; the complete violating suffix then begins in the
generated part and equation (15) applies.  Suffix monotonicity contradicts
the displayed label in either case.

At `A_0`, the first root which contains the complete pair is the
length-nine word

```
222322232.
```

Its cube is also locally impossible: the executed violations are at
cuts `11,12,20,21`, with values/labels
`(3,2),(4,3),(3,2),(4,3)`.  This last fact is not needed to obtain the
pair-parent alternative, but excludes a root-nine cube interruption;
a root-nine square remains a legitimate pair-parent witness.

All smaller roots have already appeared in the exhaustive proper-border
table of Section 9, and all larger roots contain the pair.  This
exhausts the cases.

The data in Lemmas 4--6, including all curling values in the violation
table, are recomputed by `research/check_terminal_markers.py` using both
implementations.

Contracting a gap-four pair turns the Q21 unary two-cycle into one
stationary pair object: completion from its left leaf lands at its right
leaf, while the right-leaf root-four return exposes the same pair.  The
new rank therefore removes the artificial distinction between those two
leaf-level edges, but it does **not** orient the stationary pair or
eliminate a cycle made from pair-parent copies and adjacent-double
bridges.  Such a mixed cycle is the exact remaining square-anchored
obstruction; equations (13) and (16) alone do not orient it.
