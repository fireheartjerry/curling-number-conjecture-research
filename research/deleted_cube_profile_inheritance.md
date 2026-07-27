# The deleted-cube map in the all-long `q=r-1` branch

This note records exactly what the proposed descent

```
Q  ->  B
```

does and does not inherit.  It isolates a square-mask obstruction to the
naive claim that three aligned occurrences transfer the complete critical
profile.

## 1. Exact normal form

In the one-high/two-low all-long marker geometry, put

```
q=r-1,             N=q+2r=3r-1.
```

Let `B` be the primitive length-`r` cube root ending at the high cut,
oriented so that this cut is zero.  The equality-component formula in
`research/terminal_marker_ancestry.md` gives

```
Q = B[1:] B B.                                      (1)
```

Thus `Q` is `B^3` with the first symbol of its first copy deleted.  In
the unary-marker branch,

```
B[0]=2,   B[1]=3,   B[-5:]=22232.                  (2)
```

The last symbol of `B` is therefore the deleted symbol `2`.  In the
periodic lift of `Q`, the final symbol immediately before cut zero
restores the omitted symbol, so a literal `B^3` ends at cut zero.

For a phase `j` of `B`, its three aligned occurrences in `Q` are the
cuts

```
c_k(j) = j-1+kr mod N,       k=0,1,2.              (3)
```

Every one of these cuts carries the letter `B[j]`.  Notice that the
`3r` pairs `(j,k)` cover the `3r-1` cuts of `Q`, with one duplication.

## 2. A rigorous inherited upper bound

### Lemma 1

Assume `B` is primitive.  For every phase `j`,

```
pc_B(j) <= pc_Q(c_2(j)).                            (4)
```

Consequently, if `pc_Q=Q`, then

```
pc_B(j) <= B[j] in {2,3}.                           (5)
```

### Proof

Take a proper circular `e`-power of `B` at phase `j`, with root length
`s<r`.  The proper-power span bound applied to the primitive word `B`
gives

```
es < r+s-gcd(r,s) < 2r.                            (6)
```

Place the same factor ending at the last aligned occurrence
`c_2(j)=2r-1+j`.  Its start is strictly greater than

```
(2r-1+j)-2r = j-1,
```

so its integer start is at least zero.  Its endpoint is at most
`3r-2=N-1`.  The whole factor therefore lies in the displayed word
`Q=B[1:]B^2`, which is a factor of `B^Z`.  It is also a proper circular
power of `Q`, with the same exponent and root length.  Maximizing over
the proper powers of `B` proves (4).  Equation (5) follows from
`pc_Q(c_2(j))=Q[c_2(j)]=B[j]`.

This lemma rules out inherited *overshoot*.  The only possible failure
of fixedness in `B` is an absent required square or cube.

## 3. Cube inheritance under the maximal-run hypotheses

The all-long hierarchy supplies more than (1): the displayed `B^3` is
a maximal period-`r` run, and `r` is chosen maximal among the primitive
cube-root lengths under consideration.

### Lemma 2

Assume:

1. `B` is primitive;
2. `Q=B[1:]B^2` has `pc_Q=Q`;
3. the `B^3` ending at cut zero is a maximal period-`r` run;
4. no primitive cube root in `Q^Z` has length greater than `r`.

Then

```
B[j]=3  implies  pc_B(j)=3.                        (7)
```

### Proof

Fix `j` with `B[j]=3` and use the late aligned cut
`c=2r-1+j`, which is never cut zero.  Fixedness of `Q` supplies a
primitive cube root of length `s` at `c`.  Hypothesis 4 gives `s<=r`.

The case `s=r` would give a second length-`3r` factor of period `r`.
On a circle of circumference `3r-1`, two such factors admit lifts whose
endpoint displacement has absolute value at most `(3r-2)/2`; their
overlap is therefore longer than `r`.  Equal period and an overlap of
at least one full period align the roots, so their union is one
period-`r` run.  Since the endpoints differ, this strictly extends the
maximal run ending at zero, contradicting hypothesis 3.  Hence `s<r`.

Suppose the `s`-cube ending at `c` crossed the left boundary of the
displayed interval `[0,N)`.  Its intersection with that interval would
be `[0,c)`, of length

```
c >= 2r-1 >= r+s-gcd(r,s).
```

This intersection has periods `r` and `s`.  Fine--Wilf would give
period `gcd(r,s)<r` to an interval containing a complete copy of the
primitive word `B`, a contradiction.  The cube consequently lies
inside `[0,N)`, where `Q` is a factor of `B^Z`, and gives a proper cube
of `B` at phase `j`.

Lemma 1 bounds `pc_B(j)` above by `B[j]=3`; the inherited cube gives
the reverse bound, proving (7).

Thus, under the actual maximal-cube setup, every `3`-phase descends.
Only square coverage at `2`-phases remains.

## 4. Why three aligned square witnesses do not descend

At the late occurrence `c_2(j)`, a root-`r` square is built into (1).
The other two aligned occurrences can be rescued by squares that cross
the deleted seam.  Such squares need not give any square in `B^Z`.

The smallest local example, under the boundary conditions
`B[0]=B[-1]=2` and `B[1]=3`, is

```
B = 232,              Q = B[1:]B^2 = 32232232.
```

At phase `j=0`,

```
pc_B(0)=1,             B[0]=2,
```

but all three aligned cuts have exact value two:

```
c_0=7: root 3,
c_1=2: root 2,
c_2=5: roots 3 and 5.
```

Also `pc_Q(0)=3`, witnessed by the structural root-`3` cube.  This is
not a full fixed word `Q`; it is a counterexample to the proposed
*local inference from the three aligned cuts*.

The first example carrying the complete unary terminal suffix in (2)
is

```
B = 2322232,
Q = 32223223222322322232.                        (8)
```

At the final phase `j=6`,

```
pc_B(6)=1,             B[6]=2,
```

while the aligned cuts of `Q` all have exact value two, with the three
canonical mask roots

```
c_0=5:   r-1  = 6,
c_1=12:  2r-1 = 13,
c_2=19:  r    = 7.                               (9)
```

Put `C=rot_left(B)`.  Then `Q=C^2C[:-1]`, and the seam condition is
`C[-2:]=22`.  For a general word `C=A22`, the same mask at phase
`r-2` of `C` (equivalently, phase `r-1` of `B=2A2`) has root words

```
2A,             2A22A,             22A,
```

of lengths `r-1`, `2r-1`, and `r`, respectively.  Equation (9) is
therefore a word identity, not a numerical accident.  It is precisely
the all-long marker-parent macro.

The complete executed profiles for (8) also expose the next obligation.
The two later aligned occurrences of phase `j=1`, whose target letter is
`3`, have value only two.  A hypothetical fully fixed `Q` must add
smaller cube witnesses there.  Lemma 2 then transfers a cube to phase
one of `B`.  This is the scale-descending part of the construction; the
phase-six square hole survives it.

## 5. Exact remaining inheritance statement

The descent `Q -> B` presently proves:

```
pc_B(j) <= B[j]                    for every j;
pc_B(j)  = 3                       whenever B[j]=3,
```

under Lemma 2's maximal-run hypotheses.  Hence

```
pc_B(j) is either B[j], or B[j]=2 and pc_B(j)=1.   (10)
```

The weakest additional circular property needed for full profile
inheritance is therefore exactly

```
every 2-phase of B has a proper square.            (11)
```

It is not enough for the three corresponding phases of `Q` to be
squareful: (8)--(9) disprove that inference.

Even (11), together with Lemmas 1--2, only gives `pc_B=B`.  To contradict
minimality of a *critical synchronized* root, one must additionally
inherit the pointed first-copy fitting condition

```
B[j]s <= r+j-1
```

after choosing an origin of `B`.  A circular power obtained in Lemma 1
need not satisfy this inequality.  Thus there are two exact remaining
loads:

1. eliminate the seam-crossing square masks at the `2`-holes, or turn
   each mask into a strictly shorter critical candidate;
2. prove that the surviving powers can be chosen simultaneously
   first-copy fitting.

Calling `B` a smaller critical root before both points are supplied is
circular.  The gap-four pair-parent analysis is a concrete attack on
the first load: the canonical roots in (9) are its `q=r-1` all-long
branch.

All numerical profiles and root sets in this note are recomputed by
`research/check_deleted_cube_profile_inheritance.py`.

## 6. Exact normal form for a short repair of the terminal hole

The canonical terminal hole is phase `j=r-1` of `B`.  Its early aligned
cut is

```
c_0=r-2.
```

The root `r-1` in (9) is always available.  Suppose this cut also has a
shorter square root

```
1 <= a < r-1.                                     (12)
```

If `2a<=r-2`, that square lies wholly in the displayed factor of
`B^Z`, and phase `r-1` is not a hole.  Hence an actual seam mask has

```
2a>r-2.
```

Put

```
d=r-1-a.                                          (13)
```

Then `1<=d<=a`.  Define the three blocks

```
A=B[:d],
C=B[d:2d],
M=B[2d:r-1].
```

The equality of the two root-`a` blocks at cut `r-2` is exactly

```
M A = C M.                                        (14)
```

To verify the indexing, the first root block crosses the deleted seam.
Using `B[-1]=B[0]`, it is

```
B[2d:r] B[1:d] = M B[-1] B[1:d] = M A.
```

The second block is the positive factor

```
B[d:r-1]=C M.
```

This proves (14).

Equation (14) is the standard conjugacy equation.  It says that the
length-`d` words `A` and `C` are conjugate, and that `M` is the
corresponding conjugacy bridge.  More explicitly, there are words
`U,V` and an integer `h>=0` such that, in one of the two orientations,

```
A=VU,   C=UV,   M=(UV)^h U,
```

where `U` or `V` may be empty.  This is the usual solution of
`XA=CM`: repeatedly cancel the shorter of `M` and `C`; the positive
length decreases at each cancellation, and the terminal equality is a
cyclic split of `A` and `C`.

There is also an exact equality-component count.  Before adding the
short root, the deleted-cube equations have `r-1` components: the `r`
phases of `B`, with phases zero and `r-1` identified.  Adding the
root-`a` square at `r-2` leaves exactly

```
d=r-1-a                                           (15)
```

components.  Equation (14) shows that every letter of `B` is determined
by the `d` positions of `A`, so there are at most `d`.  Conversely,
take `d` distinct formal letters for `A`; the cancellation solution of
(14) assigns each position of `C` and `M` one of those letters without
identifying two letters of `A`.  Hence all `d` classes remain distinct.

Thus every noncanonical terminal repair has a strict quotient-scale
descent

```
r -> d=r-1-a < r.                                (16)
```

The canonical root `a=r-1` is the exceptional case: it adds no equality
to the base quotient and leaves all `r-1` components.  It is exactly
the all-long pair-parent edge, so (16) does not silently dispose of the
hard branch.

## 7. Directed repair graph and its precise limitation

For a fixed deleted-cube geometry, let a repair state be the equality
relation on its quotient phase classes generated by all power witnesses
selected so far.  A proposed exponent-`e`, root-`s` witness at cut `c`
adds the relations

```
c-\ell s+x  ~  c-s+x,
2<=ell<=e,  0<=x<s.                              (17)
```

There are three exhaustive outcomes.

1. Every relation in (17) was already present.  Then the power was
   already forced; at a purported square hole this supplies the missing
   `B`-square.
2. Some relation merges two quotient classes.  The component count
   strictly decreases.  At the terminal seam, (15) gives the exact new
   count for a short early repair.
3. The merge either joins a forced `2` class to a forced `3` class, or
   makes a cube equality hold at a class whose target is forced `2`.
   The repair is incompatible with the exact profile.

Consequently a directed cycle in the *phase projection* of the repair
graph is not a recurrence unless it also returns with the same equality
relation.  A return with the same relation is outcome 1; every unresolved
return is charged to a strict component merge, and there are at most
`r-2` such charges in the `q=r-1` quotient.  This is a finite rank for a
fixed geometry, not a uniform descent for the conjecture: the canonical
`r-1` mask makes no merge, and a strict quotient word of length `d` has
not yet been proved to inherit the critical fitting equations.

The need for a multilevel repair graph is already visible at length
fifteen.  Put

```
B = 232332233232332,
Q = B[1:]B^2
  = 32332233232332232332233232332232332233232332.
```

At the `2`-hole `j=2`, `pc_B(2)=1`.  The three aligned cuts
`1,16,31` have exact value two with root sets

```
{3,5}, {9}, {15}.
```

The least early and middle roots are therefore `3` and `9`.  They are
neither the canonical pair `14,29` nor a complementary pair summing to
`r-1=14`.  Moreover `Q` has no profile overshoot at any cut:

```
pc_Q(c) <= Q[c]  for every c.
```

It has many undercovered `3`-cuts, so it is not a fixed profile.  This
word is an executed adversary to a two-level claim such as “every
noncanonical seam mask immediately makes a cube at a `2`-cut.”  The
component rank must follow the newly required positive witnesses through
further levels; negative no-overshoot alone does not close the branch.

## 8. Complete no-merge power classification

The base `q=r-1` quotient can be written over `r-1` distinct formal
letters.  Let

```
E=x_1 x_2 ... x_(r-2),
```

where `x_0,x_1,...,x_(r-2)` are pairwise distinct.  Since phases zero
and `r-1` of `B` are the same component, the quotient template of
`Q=B[1:]B^2` is

```
W_r = E x_0 x_0 E x_0 x_0 E x_0.                (18)
```

A power predicate is *no-merge* precisely when it is already a literal
power in this formal template.  The complete list is:

### Cubes

```
cut 0, root r.                                    (19)
```

There is no other no-merge cube.

### Squares

```
root r:       cut 0 and every cut 2r-1,...,3r-2;
root r-1:     cuts r-2,r-1;
root 1:       cuts r,2r;
root 2r-1:    cuts 2r-2,2r-1.                    (20)
```

There is no other no-merge square.

To prove exhaustiveness, first consider a powered factor containing one
of the formal letters `x_i` with `i>0`.  That letter occurs exactly at
the positions

```
i-1, i-1+r, i-1+2r.
```

The two forward gaps are `r,r`, and the circular closing gap is `r-1`.
Equality of two root blocks therefore restricts a square-root
displacement to the four oriented sums

```
r, r-1, 2r, 2r-1.
```

For a displacement `s`, write a position `t` as *good* when
`W_r[t]=W_r[t-s]`.  Directly from (18), the cyclic good-position runs
for the four candidates are:

```
s=r:       the single run r-1,...,3r-2, of length 2r;
s=r-1:     the single maximal run 3r-2,0,...,r-2,
           of length r, plus the isolated position 2r-2;
s=2r-1:    the single maximal run 3r-2,0,...,2r-2,
           of length 2r;
s=2r:      no run of length 2r.
```

A root-`s` square ending at `c` needs the full length-`s` interval
`c-s,...,c-1` to be good.  Reading the eligible subintervals of those
runs gives exactly the three nonunary square rows in (20).

Three equal root blocks containing an `x_i` require its three
occurrences to occupy the three copies.  The only two possible
orientations are `s=r` and `s=2r-1`.  The latter is excluded by the
proper-power span bound:

```
3(2r-1) < (3r-1)+(2r-1)-gcd(3r-1,2r-1)
```

is impossible.  For `s=r`, a cube needs a length-`2r` good interval.
The first row above has exactly one such interval, ending at cut zero.

If a powered factor contains no `x_i` with `i>0`, it is contained in
one of the two displayed runs `x_0x_0`.  This gives the two root-one
squares and no cube.  These cases exhaust the template.

The consequence for the repair graph is sharp:

> Every required cube away from the high cut zero strictly merges base
> quotient components.

Likewise, every required square outside the explicit structural cuts in
(20) strictly merges components.  This is stronger than a root-length
descent, but it still does not canonically order the merged components
as a smaller critical word.

The length-six quotient in the terminal `r=14,a=7` adversary makes that
last point concrete.  Equation (14) gives

```
A=232223,   C=323222,   M=3.
```

The circular profile of `A` is

```
1,1,2,2,2,3,
```

so neither `A` nor its conjugate class is supplied as a smaller fixed
profile by the word equation alone.  No rotation beginning in `2`
carries the complete unary pair suffix inherited from the length-14
word.  Additional full-profile and pointed-fitting equations would have
to be transferred; the equality quotient itself does not do so.
