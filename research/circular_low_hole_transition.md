# The circular low-hole transition below a maximal square cap

This note removes first-copy fitting from the weak-square-mask
dichotomy.  In a primitive exact circular binary profile, choose the
first low root-`p` square in its maximal period-`p` run, where `p` is
globally maximal among low square roots.  Every missing low square in
the last-cube period word is filled by an ambient square of root
strictly below `p`.

The conclusion is a strict drop of the ambient square cap.  It is not
yet a strict descent of exact child profiles: the smaller mask is a
square crossing the child boundary, not a contained cube root.

## 1. A circular cube scale is also a low-square scale

Let a root-`r` cube end at a `3`-cut `z` in a primitive exact circular
binary profile.  Its first two copies give a root-`r` square ending at
`z-r`.

If that midpoint is labelled `2`, `r` is already a low square-root
length.  If it is labelled `3`, the equality

```
P[z-r]=P[z]=3
```

extends the cube one symbol to the right.  Exactness forces
`P[z+1]=3`.  A binary exact profile contains no circular `333`, so
`P[z+2]=2`.  Lemma 1 of `max_square_terminal_forest.md`, applied to
the shifted cube ending at `z+1`, puts a root-`r` square at the low
midpoint `z+1-r`.

Therefore every circular cube-root length occurs as a circular
low-square-root length.  If

```
p=max {r : a root-r square ends at a 2-cut},       (1)
```

then every cube root has length at most `p`.

## 2. Canonical maximal-cap occurrence

Choose a root-`p` square in (1), and let `K` be its maximal
period-`p` run in the bi-infinite periodic lift.  The run `K` is
finite.  Otherwise the entire lift would have period `p<n`, contrary
to primitivity of the length-`n` profile.

Among the low cuts `c` for which

```
I=[c-2p,c) subset K
```

choose the leftmost one in the linear order of `K`.  Put `a=c-2p`.
Let `h=c-d` be the last high cut before `c`; the no-`2222` equation
gives

```
1<=d<=3.
```

Choose a root-`q` cube ending at `h`.  Section 1 gives `q<=p`.
Lemma 2 of `max_square_terminal_forest.md` then gives

```
p>2q+gcd(p,q),             q<p/2,                 (2)
V^3=[c-d-3q,c-d) subset I.                         (3)
```

No fitting inequality occurs in this selection.

## 3. An internal low hole and its ambient mask

Let `0<=t<q` be a phase of the primitive child root `V` which is
labelled `2` but has no proper circular square in `V^Z`.  At the
corresponding cut in the second copy,

```
y=c-d-2q+t=a+D,
D=2p-d-2q+t,                                      (4)
```

the ambient exact profile supplies a square.  Let `s` be the root
length of any such ambient square.

Global maximality in (1) gives

```
s<=p.                                             (5)
```

The equality `s=q` is impossible.  Writing
`V^3=[B,B+3q)`, the hole is `y=B+q+t`.  A root-`q`
square ending at `y`, followed by the displayed next conjugate of
`V`, would make a root-`q` cube end at `B+2q+t`.  That cut is the same
low phase `t` in the third copy, a contradiction.

If `s<q`, the mask must cross the left child boundary:

```
2s>q+t.                                           (6)
```

Otherwise it would be a proper internal square of `V` at phase `t`.
Thus the child-relative alternatives are exactly

```
s<q and the mask crosses V^3,
or
q<s<=p.                                           (7)
```

## 4. Equal-cap masks are impossible

Assume `s=p`.  The arithmetic in Section 3 of
`weak_square_mask_dichotomy.md` has only two alternatives.

First suppose `D>=p`.  The mask square and `I` overlap in at least one
full period.  Their union belongs to the same maximal period-`p` run
`K`.  Its mask endpoint is

```
y=a+D<c
```

and is a low cut carrying a root-`p` square.  This contradicts the
choice of `c` as the leftmost such low cut in `K`.

It remains to have `D<p`.  Put `H=p-2q`.  Equation (2) gives

```
H>=gcd(p,q)+1>=2,
D-p=H-d+t.
```

The bounds `d<=3` and `t>=0` leave exactly

```
p=2q+2, gcd(p,q)=1, d=3, t=0, D=p-1.             (8)
```

For odd `q>=3`, Section 5 of
`weak_square_mask_dichotomy.md` eliminates (8) by literal period
transport and endpoint labels.  None of that proof uses fitting.

For `q=1`, equation (8) gives `p=4`.  Section 1 bounds every circular
cube root by four.  The necessary next-label rule is therefore
determined by the preceding 16 symbols: some root-`1..4` square must
end at every cut, a root-`1..4` cube exists exactly at a displayed
`3`, and no root-`1..4` fourth power exists.
`research/check_max_fitting_root_four.py` exhausts the resulting
functional graph and finds no directed cycle.  A circular profile
would supply a directed cycle, so this unary case is impossible as
well.

Consequently every ambient mask at the selected child hole satisfies

```
s<p.                                              (9)
```

Combining (7) and (9), the exhaustive transition is

```
s<q<p/2, with a left-crossing mask;                (10a)
q<s<p, with a child-scale ascent but cap drop.     (10b)
```

## 5. Why (9) is not yet exact-child descent

The mask ends at `y`, strictly inside the displayed child cube.  It
does not contain all of `V^3`, regardless of whether its left endpoint
lies in `I`.  Replacing the parent by the mask therefore does not
produce the same kind of attached cube-child object.

The executed local word-equation model in
`research/check_drop_attachment_loss.py` realizes (10b):

```
p=7, q=2, s=5, D=8,
[0,14)=(3232332)^2,
[6,12)=(23)^3,
[-2,8)=(23323)^2.
```

The mask crosses the parent left boundary and does not contain the
child cube.  Both finite curling-number implementations give exact
values two, three, and two at the three distinguished suffix cuts.
The same checker now proves that this model cannot be embedded in the
present globally maximal circular setup.  The high cut immediately
before the hole is cut seven.  Cube roots

```
1,2,3,4,6,7
```

each fail an explicit equality between their final two root blocks,
using only displayed coordinates.  Root five is the sole local
possibility, but the mask-square equality

```
P[7]=P[2]=3
```

extends such a cube from cut seven to the low cut eight.  Hence no
cube root at most the global bound seven can supply the exact high
value.  The attachment-loss word is a countermodel only to the raw
period-overlap inference, not to the full circular transition.

An induction can now use only one of two additional lemmas:

1. a cap-drop closure which turns the root-`s` crossing square into a
   contained primitive cube whose period profile is exact; or
2. a global compatibility equation excluding both (10a) and (10b).

Neither conclusion follows from the current overlap equations.

## 6. Canonical re-rooting at the high immediately before a mask

There is nevertheless a canonical next cap.  Let a primitive root-`s`
mask square end at a low cut `c`,

```
S^2=[c-2s,c),
```

and assume `s>1`.  The primitive binary root `S` contains a `3`.
Let `z=c-delta` be the last high cut before `c`.  Then

```
1<=delta<=min(3,s).                                (11)
```

Choose a cube root `u` ending at `z`.  The equality `u=s` is
impossible.  Indeed, period `s` of the mask square gives every equality

```
P[k]=P[k-s],               z<=k<c,
```

because `delta<=s`.  A root-`s` cube ending at `z` would consequently
extend one symbol at a time to a root-`s` cube ending at the low cut
`c`.

There are exactly two remaining cases.

If `u<s`, Lemma 2 of `max_square_terminal_forest.md`, with `s` in
place of its square root and `delta` in place of its last-high distance,
gives

```
s>2u+gcd(s,u),                                     (12)
```

and contains the whole `u`-cube in the mask square.

If `u>s`, this is a strict scale ascent.  Since the high cut `z` is
followed by a low cut, Lemma 1 of that note puts a root-`u` square at
the low midpoint `z-u`.  In either case, choose the leftmost low
root-`u` square in its maximal period-`u` run as the next canonical
cap.  Its lifted endpoint is at most

```
z-u<c.                                             (13)
```

Thus canonical re-rooting has the exact alternative

```
root drops below half,
or root strictly ascends while the lifted endpoint decreases. (14)
```

All roots remain bounded by the original global cap `p`, by Section 1.
Consecutive ascent steps are therefore finite.  What is not automatic
is that a later ascent to a previously used numerical root returns to
the same maximal period run.

## 7. Exact criterion for a prior-cap revisit

Let an earlier canonical root-`r` square be

```
I=[a,c),
```

with `c` the leftmost low root-`r` square endpoint in its maximal
period-`r` run.  Suppose a later re-rooting cube of the same root `r`
ends at `z<c`.  Its intersection with `I` is `[a,z)` whenever
`z>a`.

If

```
z-a>=r,                                           (15)
```

the cube and square have a period-`r` overlap of at least one full
root, so they belong to one period-`r` run.  The cube's low midpoint
square ends at `z-r<c` in that same run, contradicting the defining
leftmostness of `c`.

Therefore every surviving same-scale revisit must have the shallow
geometry

```
z-a<r.                                            (16)
```

Leftmostness alone cannot exclude (16).
`research/check_cap_revisit_shallow.py` executes the literal local
configuration

```
root-7 cube   [-16,5)=(2222223)^3,
root-7 square [0,14)=(2222332)^2.
```

The intervals overlap in five symbols, below the seven-symbol gluing
threshold.  Both roots are primitive and distinct.  The two independent
finite curling-number implementations give value three at cut five and
value two at cut fourteen.  The executed record is

```
{'indexed_word': (-16, '2222223222222322222233222223322'),
 'cube': ((-16, 5), 7, '2222223'),
 'square': ((0, 14), 7, '2222332'),
 'overlap': 5, 'period_gluing_threshold': 7,
 'same_numerical_cap': True, 'same_period_run_forced': False,
 'curling_values': {5: 3, 14: 2}}
```

This is not a circular fixed profile.  It is an exact countergeometry
to the proposed inference “a repeated cap value revisits the prior
run.”  A complete nested-chain proof must show, using the intervening
hole geometry, that (16) cannot occur; the numerical cap and
leftmost-run choice do not show it.

## 8. Exact normal form of a cap ascent

The ascent line in (14) has a useful complete word equation.  Retain
the mask square `S^2` of root length `s`, let its last high be
`z=c-d`, and suppose the cube root at `z` is

```
u=s+k,                 k>0.
```

The overlap

```
[c-2s,z)
```

has length `2s-d` and periods `s` and `s+k`.

If

```
k>=s-d,                                           (17)
```

then

```
u>=2s-d.                                          (18)
```

This is the near-doubling ascent.

Assume instead that `k<s-d`.  Write the final square root as

```
S=P[c-s:c].
```

For every `0<=i<s-d-k`, period `s` and period `s+k` on the overlap
give

```
S[i]
 =P[c-2s+i]
 =P[c-s+k+i]
 =S[i+k].                                         (19)
```

Thus the prefix `S[:s-d]` has period `k`.  The next comparison fails
with prescribed endpoint labels.  Lemma 1 of
`max_square_terminal_forest.md` applied to the ascending cube gives

```
P[z-u]=2.
```

Period `s` of the square identifies that symbol with
`S[s-d-k]`.  The last-high definition gives

```
S[s-d]=P[z]=3,
S[s-d+1:s]=2^(d-1).                               (20)
```

Therefore every non-doubling ascent has the exact break form

```
S[:s-d] has period k,
S[s-d-k]=2,
S[s-d]=3,
S[s-d+1:s]=2^(d-1).                               (21)
```

The break in (21) is at the first coordinate not covered by the
period-`k` prefix equations; extending (19) one more step would
identify `2` with `3`.

Hence an ascent chain cannot be treated as arbitrary slow root growth:
each edge either nearly doubles as in (18), or carries the explicit
short-period-prefix break (21).  A complete revisit proof may now
restrict its shallow branch to successive copies of these break
markers.  No compatibility theorem for a cycle of such markers is
proved here.

## 9. Two consecutive slow ascents nearly double

The standard Three Squares Lemma does not directly apply to two
successive cap ascents.  Its squares must have the specified
common-prefix or nested L-root-interval geometry; an ascent square
crosses the preceding cap's left boundary.  The exact statement and
scope are recorded in `max_square_terminal_forest_literature.md`.
For the present two-break configuration, a direct Fine--Wilf argument
is stronger.

Retain a slow ascent from `s` to `s+k`, so

```
0<k<s-d.
```

Put

```
L=s-d,
C=S[:L],
B=suffix_k(C),
E=3 2^(d-1).
```

Section 8 gives

```
S=C E,                  C has period k.            (22)
```

Reading the final root block of the ascending cube through the overlap
gives its exact root word

```
Q=B E C,                 |Q|=s+k.                  (23)
```

Now suppose the next cap transition is another slow ascent, from
`|Q|=s+k` to `s+k+l`, and let its last-high distance be `d'`.
If

```
d'>L,
```

then `s<d+d'<=6`; this is a bounded cap.  Assume `d'<=L` and put

```
h=L-d'=s-d-d'.
```

The last high of `Q` is the symbol

```
C[h]=3.
```

The second slow-ascent equations say that the prefix of `Q` ending
immediately before this high has period `l`, and that its unextended
period mate is low:

```
C[h-l]=2                                           (24)
```

whenever `h>=l`.

The factor `C[:h]` has period `k`, by (22), and period `l`, by the
second ascent.  Put `g=gcd(k,l)`.  Suppose it met the Fine--Wilf
threshold:

```
h>=k+l-g.                                         (25)
```

Then `h>=k,l`, so every coordinate below is defined.  Fine--Wilf makes
`C[:h]` period `g`.  Period `k` of the full word `C` gives

```
C[h-k]=C[h]=3.
```

But `h-k` and `h-l` are both in `C[:h]` and are congruent modulo `g`.
The period-`g` conclusion identifies them, contradicting (24).
Therefore (25) is impossible, and

```
h<k+l-g.
```

For the root length after the two ascents this gives

```
s+k+l > 2s-d-d'+g >= 2s-5.                       (26)
```

If either ascent was in the near-doubling branch (17), the same lower
bound follows immediately.  Hence every pair of consecutive ascent
edges starting above the bounded cap `5` satisfies

```
new_root-5 > 2(old_root-5).                       (27)
```

Under the original global cap `p`, a consecutive ascent run has
logarithmic length.  It must end in a half-scale descent or at the
global cap.  Equation (27) does not yet exclude repeated alternation
between such finite ascent runs and half-scale descents; that recurrent
case is exactly where the shallow revisit geometry (16) can re-enter.

## 10. Exhaustive removal of the residual global caps at most five

Section 1 shows that if the global low-square cap is `p`, every cube
root is also at most `p`.  For `p<=5`, the preceding 20 symbols
therefore impose the following necessary transition rule at every cut:

1. some square of root `1,...,5` ends there;
2. the next displayed symbol is `3` exactly when a cube of one of those
   roots ends there; and
3. no fourth power of one of those roots ends there.

`research/check_max_circular_root_five.py` enumerates all

```
2^20=1,048,576
```

binary suffix states.  It retains the unique necessary successor only
when both source and target satisfy the square/fourth conditions, then
performs a three-color traversal of the complete functional graph.  The
executed result is

```
{'root_max': 5, 'window': 20, 'states': 1048576,
 'locally_admissible': 614692, 'retained_edges': 396764,
 'directed_cycles': 0}
```

The graph is a supergraph: it omits every constraint involving roots
above five rather than assuming extra negative equations.  A circular
profile with global cap at most five would give a directed cycle in
this graph.  None exists.

Thus every surviving circular cap chain has

```
p>=6,                                             (28)
```

so the shifted doubling quantity `p-5` in (27) is positive.  This
removes all bounded residues left out of the two-ascent argument.  It
does not remove a recurrent chain which alternates half-descents and
finite ascent runs under a larger global cap.

## 11. Two slow ascents are locally realizable

The contradiction in Section 9 occurs only when the two short periods
meet the Fine--Wilf threshold.  The complementary branch is not merely
an artifact of the inequalities.  The executed checker
`research/check_two_ascent_local_model.py` constructs the indexed word

```
(-58,
 233232232233232223323223223323222332322322332322322332322332)
```

with the exact local ancestry

```
6 --(+3, d=1)--> 9 --(+7, d'=1)--> 16.
```

Both edges are slow:

```
3<6-1,                 7<9-1.
```

The three primitive roots are

```
232233,
223323223,
2332322322332322.
```

The checker verifies every displayed square and cube equality.  It
also evaluates the finite curling number by two independent
implementations at all five distinguished cuts and obtains, in
increasing cut order,

```
cn(-26)=2, cn(-10)=3, cn(-9)=2, cn(0)=3, cn(1)=2.
```

Thus exactness at the distinguished cuts does not eliminate the
two-break branch.  The word is not asserted to be a circular fixed
profile.  Its role is narrower: any ascent-run contraction must retain
the endpoint/marker information; root lengths and the local break
equations alone admit consecutive slow ascents.

## 12. Every individual ascent expands a shifted scale

The exact negative profile equation strengthens the slow branch of
Section 8.  Recall that its prefix

```
C=S[:L],                 L=s-d,
```

has period `k`, where the new root is `u=s+k`.  If `L>=4k`, then
`C[:4k]` is four consecutive copies of `C[:k]`.  This is a proper
fourth power occurring inside the displayed parent square.  Its
ambient endpoint has profile value at most three, so the fourth power
contradicts exactness.  Therefore

```
s-d<4k.                                           (29)
```

For a slow ascent, (29) gives

```
4u>5s-d>=5s-3,
4(u-3)>5(s-3).                                   (30)
```

For a near-doubling ascent, Section 8 gives

```
u>=2s-d,
u-3>=2(s-3).                                      (31)
```

Consequently every ascent starting above three strictly multiplies
the shifted scale `s-3` by more than `5/4`; a near-doubling edge
multiplies it by at least two.  This bounds each maximal ascent run
logarithmically edge by edge, independently of the two-edge estimate
(27).  It still does not orient a descent/ascent wrap cycle: the sum
of the intermediate roots in a geometrically growing run need not be
smaller than the enclosing cap.

## 13. Whole-cycle interval formulation

The failed nodewise lexicographic ranks can be bypassed only by using
all periodic intervals around a wrap circuit at once.  Index a
hypothetical nonterminal circuit cyclically.  Let `r_i>=2` be its cap
root, `c_i` its low cap, and `d_i` the distance to its last high.  The
selected cube at that high has the next root `r_(i+1)`.  In one lifted
turn,

```
c_(i+1)=c_i-d_i-r_(i+1),
sum_i(d_i+r_(i+1))=w n,             w>=1.          (32)
```

The incoming root-`r_i` cube ends at

```
b_i=c_i+r_i.
```

Thus its interval and the next high are

```
K_i=[b_i-3r_i,b_i),
b_(i+1)=b_i-r_i-d_i.                              (33)
```

Every `K_i` has period `r_i`.  The endpoint labels are

```
P[b_i]=3,
P[c_i]=2,
P[b_(i+1)]=3,
P[b_(i+1)+1:c_i+1]=2^(d_i).                       (34)
```

Equations (32)--(34), the square and cube period equalities, and the
necessary scale split

```
r_(i+1)>r_i
or
r_i>2r_(i+1)+gcd(r_i,r_(i+1))                     (35)
```

form a finite equality graph on the coordinates modulo `n`.  A
whole-cycle proof would show that this graph always connects a forced
`2` coordinate to a forced `3` coordinate.

The standard generalized Fine--Wilf theorem does not state this
conclusion.  It combines several periods carried by one common factor;
here different factors `K_i` carry different periods, and every
crossing ascent can miss the pairwise Fine--Wilf threshold.  The
Critical Factorization Theorem supplies a position whose local period
equals a word's global period, while the Runs Theorem and its Lyndon
roots count or charge maximal periodic intervals.  None of these
statements gives the directed endpoint-label identification in
(34).  A separate cyclic-cover lemma is required.

`research/check_cap_ancestry_cycle_graph.py` exhausts the bare
equality graphs for

```
2<=r_i<=12,       2<=number of nodes<=5,
```

including every winding compatible with (32) and every
`1<=d_i<=min(3,r_i)`.  It deliberately omits primitivity, square
coverage away from the selected caps, and every negative profile
equation, so it searches a necessary-condition superfamily.  The
executed counts are

```
nodes  root tuples  distance tuples  winding graphs  compatible
  2        12              90               90          0
  3        76           1,701            2,476          0
  4       315          19,791           33,416          0
  5     1,622         277,101          519,802          0
```

This is finite evidence for the whole-cycle statement, not its proof.
The unbounded number of nodes, roots, and windings remains open.

The same checker separately reconstructs the full cap-ancestry graph
of the exact fixed length-21 word `223222322232322232223`, without a
fitting filter.  It has 22 square vertices, 18 selected cube edges,
and no directed cycle.  Thus Q21 does not contradict the proposed
whole-cycle lemma; its ancestry paths terminate instead of wrapping.

## 14. Unrestricted exclusion of two-node wrap circuits

The two-node row of Section 13 admits a direct symbolic proof.  Let
the two roots be `a<b`.  The edge from `a` to `b` is an ascent, while
the return edge is a descent, so

```
b>2a+gcd(a,b).                                    (36)
```

Let the two last-high distances be `d_0,d_1`, and let the circular
ambient period be `n`.  If the circuit winds `w` times, (32) is

```
T:=a+b+d_0+d_1=w n,             n>b.             (37)
```

First classify the possibility `T>2b`, equivalently

```
a+d_0+d_1>b.                                     (38)
```

For `a>=4`,

```
a+d_0+d_1<=a+6<=2a+2<=b,
```

where the last inequality follows from (36), so (38) fails.  For
`a=2`, the distance bound gives

```
a+d_0+d_1<=7.
```

Equation (36) forces `b>=7`: an odd `b` has
`gcd(2,b)=1` and the first admissible odd value is seven; an even `b`
has gcd two and is at least eight.  Thus (38) fails again.

For `a=3`, (36) rules out `b=7` and `b=9`, while `b=8` is admissible.
If `b>=10`, (38) fails because

```
a+d_0+d_1<=9.
```

Consequently the only case with `T>2b` is

```
(a,b,d_0,d_1,T)=(3,8,3,3,17).                   (39)
```

If `w>=2`, equations (37) and `n>b` imply `T>2b`, so (39) would be
necessary.  But `17=w n` has no factorization with integers `w>=2`
and `n>8`.  Hence every two-node circuit has

```
w=1,                  n=T.                       (40)
```

Normalize the small-root cap to `c_0=0`, and put

```
h_0=-d_0,
c_1=h_0-b.
```

The root-`b` cube selected at `h_0` is

```
J=[h_0-3b,h_0).                                   (41)
```

Outside (39), the classification above gives `n<=2b`.  The two
coordinates

```
h_0-n,                  c_1-n=h_0-b-n
```

both lie in `J`, differ by exactly `b`, and therefore are equal by
the period of (41).  Circularity identifies their values with the
values at `h_0` and `c_1`.  Those cuts are respectively high and low,
so this equality identifies `3` with `2`, a contradiction.

In the exceptional case (39), the coordinates are

```
h_0=-3,        c_1=-11,       n=17.
```

The same cube is `[-27,-3)`.  It contains

```
h_0-n=-20,              -12=(h_0-n)+8,
```

so its period eight equates them.  The first coordinate is congruent
to the high cut `h_0`.  The second lies strictly after the other high
cut

```
c_1-d_1=-14
```

and at or before its low cap `c_1=-11`; hence it is a forced low cut.
This is again `3=2`.

Thus no two-node cap-ancestry wrap circuit exists for any roots,
ambient length, or winding.  This proof uses the complete equality
intervals and their periodic translates, not a nodewise ray order.

## 15. The unrestricted cyclic equality lemma

The whole-cycle equality graph of Section 13 is inconsistent for
arbitrary roots and arbitrary winding.  The scale split (35) and the
special bound `d_i<=3` are not needed.  The only distance hypothesis
used here is

```
1<=d_i<=r_i.                                      (42)
```

Suppose, for contradiction, that the equality graph is
label-compatible.  Give value `3` to every equality component
containing a forced high coordinate and value `2` to every other
component.  Compatibility ensures that every forced low coordinate
has value `2`.  This defines an `n`-periodic binary word `P` satisfying
all selected cube equalities.

Take lifted caps

```
c_0>c_1>...>c_m=c_0-w n
```

extend the root indices cyclically, and put `e_i=c_i+r_i`.  For
`0<=i<m`, the cap recurrence gives

```
e_(i+1):=c_(i+1)+r_(i+1)=c_i-d_i.                (43)
```

Thus `e_(i+1)` is the selected high endpoint of the root-`r_(i+1)`
cube.  The integer coordinates in `[c_(i+1),c_i)` split into

```
[c_(i+1),e_(i+1)), {e_(i+1)},
(e_(i+1),c_i).                                   (44)
```

The first coordinate `c_(i+1)` is a forced low cap.  The middle
coordinate `e_(i+1)` is forced high, and every integer coordinate in
the last open interval is forced low.  As `i` ranges over a lifted
turn, the intervals `[c_(i+1),c_i)` partition `w n` consecutive
coordinates.

For a residue `x`, write `Rot(x)` for the length-`n` forward circular
rotation

```
(P[x],P[x+1],...,P[x+n-1]).
```

Order these binary words lexicographically with `2<3`.  Choose a
coordinate `x` with `P[x]=3` for which `Rot(x)` is lexicographically
minimal, and choose any one of its `w` lifts in `[c_m,c_0)`.  The
partition (44) and the forced labels leave two cases.

### Case 1: `c_(i+1)<x<e_(i+1)`

Put

```
r=r_(i+1),       e=e_(i+1),       y=x-r.
```

The coordinate `x` lies in the third copy of the cube

```
[e-3r,e).
```

The coordinate `y` lies at the same phase in the second copy, so the
cube equations give `P[y]=P[x]=3`.  Let `L=e-x`.  Since `x` is
strictly inside the third copy,

```
1<=L<r<n.
```

For every integer `0<=j<L`, the cube period gives

```
P[y+j]=P[x+j].
```

At the next coordinate,

```
P[y+L]=P[e-r]=P[c_(i+1)]=2,
P[x+L]=P[e]=3.                                   (45)
```

Hence `Rot(y)<Rot(x)`, contradicting the choice of `x`.

### Case 2: `x=e_(i+1)=c_i-d_i`

This endpoint lies inside the incoming root-`r_i` cube

```
[e_i-3r_i,e_i),          e_i=c_i+r_i,
```

because (42) places it in the middle copy.  Put

```
r=r_i,       y=x-r,       L=e_i-x=r+d_i.
```

The cube equations give

```
P[y+j]=P[x+j]             for 0<=j<L,             (46)
```

while the first unpaired coordinates are

```
P[y+L]=P[e_i-r]=P[c_i]=2,
P[x+L]=P[e_i]=3.                                   (47)
```

If `L<n`, equations (46)--(47) give
`Rot(y)<Rot(x)`, and `P[y]=P[x]=3`, contradicting minimality.

If `L>=n`, equation (46) for `0<=j<n` makes the two length-`n`
rotations identical.  Identical rotations agree at offset
`L mod n`; periodicity then gives

```
P[y+L]=P[x+L],
```

contradicting (47).  This discharges the second case.

Every coordinate labelled `3` falls into one of the two cases, while
at least one such coordinate exists because every `e_i` is forced
high.  Both cases are impossible.  Therefore the cyclic equality
graph always identifies a forced low component with a forced high
component.

Equivalently, no cap-ancestry wrap circuit satisfying (32)--(34) and
`n>max_i r_i` exists, for any number of nodes, roots, distances
satisfying (42), or winding.  The proof is a strict descent among the
finitely many circular rotations; it places no uniform bound on the
length of an undirected equality certificate.  The executed
countermodels in `research/check_cap_path_bound_counterexample.py`
show shortest certificate lengths five and seven, so such a bound
cannot be replaced by the previously sampled four-edge templates.

## 16. Exact global consequence and remaining terminal-prefix gap

Apply Section 15 to the fitting square-ancestry graph of
`max_square_terminal_forest.md`, Section 3.  That graph has finitely
many vertices: a vertex is a phase modulo `n` together with a proper
root length below `n`.  Every directed cycle would lift to data
(32)--(34), with `d_i<=r_i`, and is therefore excluded by Section 15.
Hence the fitting square-ancestry graph is acyclic.

Every vertex of root length greater than one has an outgoing edge:
its primitive binary root contains a high symbol, and the last such
symbol selects the child cube and its low midpoint square.  It follows
that every maximal directed path ends at a root-one square whose root
symbol is `2`.

This does **not** prove the terminal-prefix theorem and does not by
itself exclude a minimum critical counterexample.  An ancestry edge
changes the square endpoint from `c` to

```
c-d-q.
```

The root-one leaf therefore occurs at a generally different phase
from the distinguished final cut.  Its local square supplies no
power attaining the original final-phase value inside the finite
prefix.  The equality transport used in Section 15 proves only that a
wrap cycle is impossible; it does not reverse the ancestry edges or
transport a maximizing power back to the original endpoint.

The exact remaining implication would have to show that an
origin-crossing final-phase witness cannot have its associated
ancestry path terminate at such an unrelated root-one leaf, or else
show that the leaf transports a fitting witness of the required
exponent back to the distinguished final phase.  Neither statement is
contained in the cube equalities proved here.  The exact length-21
circular profile supplies a useful warning: its unrestricted cap
ancestry graph is acyclic, as checked in Section 13, while the profile
itself exists.  Thus cap acyclicity is strictly weaker than exclusion
of all exact circular profiles.

## 17. Pointed fitting slack is not the missing rank

Fix the distinguished first-copy left boundary

```
O=1-n.
```

For a lifted square vertex `(c,s)`, define its fitting slack by

```
lambda(c,s)=c-2s-O=n+c-1-2s.                     (48)
```

Thus the square is first-copy fitting exactly when `lambda>=0`.
For an ancestry edge, let `h=c-d` be the selected high cut, let `q`
be the cube root there, and let

```
c'=h-q=c-d-q
```

be the lifted child-square cap.  The child slack is

```
lambda(c',q)
 =n+h-1-3q
 =lambda(c,s)+2s-3q-d.                            (49)
```

The middle expression in (49) is exactly the fitting slack of the
selected cube.  Thus fitting of a selected cube transports without
loss to its midpoint child square.

Equation (49) does not give a one-directional rank.  On a contained
descent, `3q+d<=2s`, so the slack is nondecreasing.  On an ascent
`q>s`, it strictly decreases.  Moreover, replacing the lifted child
cap `c'` by its canonical representative `c'+n` increases its slack
by `n`.  A modulo-`n` ancestry graph therefore discards precisely the
wrap count needed by a pointed argument.

The exact Q21 profile shows that even a boundary-tight maximal parent
can terminate at an unrelated root-one leaf.  For

```
P=223222322232322232223,       n=21,
```

the fitting root-ten square at cap zero has

```
lambda(0,10)=0.
```

Its last high is at the lifted cut `-1`; the selected cube has root
one, so the child square is

```
(c',q)=(-2,1),             lambda(-2,1)=16.       (50)
```

Modulo 21 this is the vertex `(19,1)`, whose canonical slack is 37
and which has no outgoing ancestry edge.  Its endpoint is not the
original cap zero.  Thus neither boundary tightness nor nonnegative
slack forces a return to the distinguished phase.

`research/check_cap_ancestry_pointed_slack.py` reconstructs all 22
Q21 fitting-square vertices and all 18 edges, checks (49) edge by
edge, and verifies (50).  It finds four root-one leaves, at canonical
caps 5, 9, 15, and 19.  The surviving terminal-prefix problem must
retain more than `(root length, endpoint, fitting slack, wrap count)`;
it needs a word-equation provenance that links the original
origin-crossing power to the leaf, or a reason that the critical
origin forbids the Q21-type leaf termination.

There is also a primitive local model with genuinely negative initial
slack:

```
P=222332223,       n=9.
```

Executed proper-profile computation gives

```
pc_P=(2,1,2,3,2,2,1,2,3).
```

At the three distinguished cuts the displayed labels are exact.  A
root-five square ends at cut zero with slack `-2`; its last high is
cut `-1`, where a root-one cube is maximizing; and its child is the
root-one square at cut `-2`, with slack four.  The child is a terminal
ancestry leaf.  Thus negative origin slack can be discharged into an
unrelated root-one leaf while preserving primitivity, both power
equations, and exactness at every cut on the selected path.

This local word is not a complete fixed profile: the executed
mismatch set is `{1,4,6}`.  Therefore it does not refute the desired
critical-origin theorem.  It proves that such a theorem must use
off-path full-profile or replay/fitting equations; the path equations,
endpoint labels, primitivity, and pointed slack do not suffice.
`research/check_negative_slack_leaf_countermodel.py` is the complete
audit.

## 18. Continuing through root-one leaves forces an external-source cycle

The stopped fitting ancestry graph can be extended at every root-one
leaf.  Let `(c,r)` be a fitting square vertex.

If `r>1`, its primitive binary root is not the constant word of
`2` symbols.  It therefore contains a `3`, so the last high before
`c` has distance `d<=r`, as in the original graph.

If `r=1`, write `x` for the one-symbol square root.  There are two
cases.

1. If `x=3`, then the cut immediately before `c` is high, so `d=1=r`.
2. If `x=2`, the root-one square and the low cap give three
   consecutive `2` symbols ending at `c`.  A fourth consecutive `2`
   would be a fourth power, contradicting the exact profile alphabet
   `{2,3}`.  Hence the immediately preceding symbol is `3`, and

   ```
   d=3>r=1.                                      (51)
   ```

At the selected high cut, full first-copy fitting supplies a fitting
cube root `q`.  Its midpoint square is fitting at the child cap
`c-d-q`, by the equality of cube and child slack in (49).  Thus every
vertex of the extended finite graph has an outgoing edge.

Every finite directed graph with positive outdegree at every vertex
has a directed cycle: start at any vertex and follow outgoing edges;
some vertex repeats, and the segment between its first two
occurrences is a cycle.  If every edge on such a cycle had `d<=r`,
Section 15 would contradict the cycle.  Therefore every extended
fitting ancestry cycle contains an edge of type (51).  In particular:

```
every surviving cycle contains a root-one square with root symbol 2
and the anchored local boundary 3 2 2 2.          (52)
```

This converts the unrestricted cap-cycle gap into a terminal-root
classification problem.  It does not classify the cycles satisfying
(52).

For Q21, the extended graph has 22 vertices, 22 edges, and exactly one
directed cycle:

```
(5,1) -> (19,4) -> (15,1) -> (8,4) -> (5,1).
```

The corresponding last-high distances are

```
(3,3,3,2),
```

and a one-turn lift of the cap endpoints is

```
5, -2, -6, -13, -16=5-21.
```

The first and third edges are precisely the root-one/`2` external-source
edges in (51).  Their selected root-four cubes happen also to be terminal
span-one gadgets with period code `(3)`; that terminality is an additional
Q21 property, not a consequence of (51).  The exact dictionary and a local
nonterminal countermodel are in
`research/terminal_source_gadget_bridge.md`.
`research/check_extended_cap_ancestry_q21.py` recomputes the exact Q21
profile, fitting roots, unique cycle, lifted coordinates, and both
`3 2 2 2` boundaries.

Consequently a completion along this route must use the critical
origin to exclude all external-source cycles of type (52), or prove that
their exact profile and fitting equations force the Q21 cycle and
then discharge that macro by an independent pointed
argument.  The lexicographic lemma has removed every cycle without a
root-one external edge.
