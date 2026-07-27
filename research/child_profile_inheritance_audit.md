# Child-profile inheritance, DROP attachment, and LOCK winding

This note audits the proposed descent from a contained primitive cube
to its period word.  Exact proper-profile inheritance does work once
positive witnesses are internal.  High phases obtain those internal
witnesses from the cube-halving hierarchy.  Two pointed losses remain:
the inherited witnesses need not be first-copy fitting relative to the
child origin, and a weak-square `DROP` need not remain in the attached
parent interval.  A `LOCK` can cross the distinguished fitting origin.

## 1. Negative profile equations inherit automatically

Let `P` have exact proper circular profile, and suppose the primitive
word `V` of length `q` occurs as

```
V^3=[b,b+3q)
```

in a periodic lift of `P`.  At the cut

```
x_t=b+2q+t,              0<=t<q,
```

the displayed ambient label is `P[x_t]=V[t]`.

### Lemma 1 (proper powers of a primitive child have span below `2q`)

If a proper circular `e`-power of root length `r<q` occurs in `V^Z`,
then

```
er<q+r-gcd(q,r)<2q.                               (1)
```

Proof.  The powered interval has periods `q` and `r`.  If its length
met the Fine--Wilf threshold `q+r-gcd(q,r)`, it would have period
`gcd(q,r)`.  The threshold is at least `q`, so the interval would
contain a complete conjugate of `V`.  That conjugate would have the
strictly shorter period `gcd(q,r)<q`, contrary to primitivity.  The
second inequality in (1) uses `r<q` and `gcd(q,r)>=1`.

### Lemma 2 (negative inheritance)

At every phase,

```
pc_V(t)<=V[t].                                      (2)
```

Proof.  Suppose a proper circular power of `V` had exponent greater
than `V[t]` at phase `t`.  Place its endpoint at `x_t` in the third
copy above.  Lemma 1 puts its start strictly after

```
x_t-2q=b+t>=b,
```

and its endpoint is below `b+3q`.  Thus the entire forbidden power is
a factor of the displayed ambient `V^3`.  It ends at an ambient cut
whose exact value is `P[x_t]=V[t]`, a contradiction.

Consequently, if every phase `t` with `V[t]=2` has an internal proper
square and every phase with `V[t]=3` has an internal proper cube, then

```
pc_V=V.                                             (3)
```

The positive witnesses give the reverse inequalities, phase by phase,
and Lemma 2 supplies the upper bounds.

## 2. High-phase positive inheritance does hold in the halving hierarchy

Under the singleton-`3` hypotheses of
`fitting_cube_halving_rank.md`, use its globally maximal fitting parent
and recursively aligned child selection.  For every `3`-cut in the
third copy of a selected child `V`, that construction supplies a cube
of root length `s` satisfying

```
2s+gcd(q,s)<q
```

and places its whole occurrence inside the displayed `V^3`.  It is
therefore a proper circular cube witness in `V^Z` at the corresponding
phase.  Every high phase of `V` has the positive half of (3).

Thus the only positive proper-profile question is the low-phase
weak-square condition.  If all low phases have internal squares, the
child is an exact proper-circular fixed profile by Lemma 2.

## 3. Exact profile inheritance is not first-copy fitting inheritance

For a witness of exponent `e` and root length `r` at child phase `t`,
first-copy fitting relative to the distinguished origin of `V` is

```
er<=q+t-1.                                          (4)
```

Containment in the displayed third copy gives only

```
er<=2q+t.
```

Even the high-phase bound `s<q/2` does not imply
`3s<=q+t-1` at early phases.

`research/check_child_profile_fitting_loss.py` executes the primitive
word

```
V=32223222322,                q=11.
```

At phase zero its unique proper cube-root length is four, its proper
profile value is exactly three, and the literal circular suffix is

```
(2322)^3.
```

It even satisfies the hierarchy's strict scale inequality

```
2*4+gcd(11,4)=9<11.
```

Its powered span and first-copy capacity are respectively

```
12 and 10.
```

Hence this internal high witness is not first-copy fitting.  The
executed output is

```
{'V': '32223222322', 'length': 11, 'primitive': True,
 'phase': 0, 'proper_profile_at_phase': 3, 'cube_roots': (4,),
 'cube_root_word': '2322', 'cube_suffix': '232223222322',
 'powered_span': 12, 'deleted_first_copy_capacity': 10,
 'first_copy_fitting': False}
```

This word is a local fitting-loss certificate, not a claim that `V`
itself satisfies all fixed-profile equations.  It proves that the
inequalities used in the containment hierarchy cannot by themselves
promote (3) to the full first-copy fitting property.

## 4. A DROP need not remain attached

Retain the notation of `weak_square_mask_dichotomy.md`.  The parent
square is

```
I=[a,a+2p),
```

and a `DROP` mask of root `s<p` ending at the child hole
`y=a+D` has interval

```
J=[a+D-2s,a+D).
```

The exact attachment criterion is

```
J subset I  iff  2s<=D.                            (5)
```

No established inequality forces (5).  If `D>=p` and `2s>D`, the
overlap `[a,a+D)` has periods `p` and `s` and contains a complete
length-`p` parent root.  Primitivity forces Fine--Wilf threshold
failure,

```
D<p+s-gcd(p,s).                                    (6)
```

Conditions `s<p`, `2s>D`, and (6) are compatible.

The script `research/check_drop_attachment_loss.py` supplies a literal
binary realization.  With integer coordinates it has

```
parent: [0,14)=(3232332)^2,        p=7;
child:  [6,12)=(23)^3,             q=2;
hole:   y=8, d=2, t=0,             D=8;
mask:   [-2,8)=(23323)^2,          s=5.
```

All three roots are primitive.  The phase-zero period word `V=23` has
no proper circular square.  The mask is a strict scale drop, but

```
[-2,8) not subset [0,14),
```

and it does not contain the child cube.  Both independent finite
curling-number implementations, executed after the A094004 calibration,
give the exact distinguished suffix values

```
cut 8 -> 2,       cut 12 -> 3,       cut 14 -> 2.
```

The complete executed record is

```
{'indexed_word': (-2, '23323233232323322'),
 'parent': ((0, 14), 7, '3232332'),
 'child': ((6, 12), 2, '23'),
 'mask': ((-2, 8), 5, '23323'), 'D': 8,
 'mask_crosses_parent_left': True, 'mask_contains_child': False,
 'curling_values': {8: 2, 12: 3, 14: 2}}
```

This is a local word-equation countergeometry, not a complete circular
fixed profile.  It shows that an attachment theorem needs another
global fixed-profile equation; it cannot follow from the current
Fine--Wilf, primitivity, endpoint-value, and strict-drop hypotheses.
The augmented checker also proves that it cannot embed when seven is a
global cube-root bound: every root `1..7` at its pre-hole high cut is
either rejected by a displayed coordinate mismatch or, for root five,
extends to the following low cut.  Thus it is not a counterexample to
the full globally maximal circular setup.

In particular, choosing a minimal attached hole by parent root length
does not yet give a well-founded descent.  The smaller mask in this
configuration is not another object in the same attached class, so
minimality supplies no contradiction.

## 5. LOCK can wind around the fitting origin

In `LOCK`, `s=p` and `p<=D<2p`.  Put

```
L=2p-D.
```

The mask and parent squares have period-`p` union

```
[a-L,a+2p),                     0<L<=p.            (7)
```

If `D=p`, then `L=p` and (7) is a root-`p` cube ending at the parent
low cut.  Exactness excludes this.  Every surviving `LOCK` therefore
satisfies

```
p<D<2p,             0<L<p.                         (8)
```

It is a proper left extension of the parent period run, not a scale
drop.

The parent fitting condition says only `a>=1-n`.  It does not imply
`a-L>=1-n`.  The allowed boundary value `a=1-n`, together with any
`L>0`, makes (7) cross the distinguished fitting origin.  Canonicalizing
the mask by adding one period `n` restores its own fitting inequality
but moves it to the next lift.  Therefore the common period interval
has winding number one in the pointed endpoint graph.

Absorbing `LOCK` into a maximal period run is sound in the universal
periodic lift.  It does not preserve a single first-copy slab, and it
does not provide a well-founded pointed rank.  Eliminating these winding
extensions requires a global no-wrap equation or a rank that includes
and strictly controls winding; neither is established here.

## 6. Exact children can restart a purely circular induction

There is no need to inherit first-copy fitting after a child has passed
the positive low-phase test.

Let `A` be the current primitive exact circular profile in the
singleton-`3` branch, or in any branch where the corresponding
internal-high-witness lemma has been established.  Choose a globally
maximal proper cube root `V` in `A`; its length satisfies

```
|V|<|A|.
```

The maximal-run argument supplies the internal high witnesses of
Section 2.  If every low phase of `V` also has an internal proper
square, equation (3) makes `V` a primitive exact circular profile.
Discard `A`, regard `V^Z` as the new ambient lift, and choose a globally
maximal proper cube root in `V`.  Every bound used in the next
containment step is then a bound among circular roots of `V`; no witness
is transported through the deleted-copy origin of `A`.

The ambient word length strictly decreases whenever this restart
occurs.  Root lengths inside two successive ambients need not be
monotone, but each is proper in its own ambient and the ambient lengths
are positive integers.

The circular Q21 two-cycle certificate has exactly this character.  If
a terminal physical root of length `21` is globally maximal among cube
roots in the current circular ambient, every predecessor cube root at
the two certified phases has length at most `21`.  Section 4 of
`q21_two_cycle_lemma.md` can then iterate its forced two-cycle in the
bi-infinite lift; no fitting inequality is invoked.

The word “globally” is load-bearing.  If a Q21 root is retained merely
as a nonmaximal descendant of an older ambient, a crossing predecessor
root longer than `21` is outside the finite transition certificate.
One must first prove the child exact and restart with a global maximum,
or separately exclude that ascent.

The remaining fitting ledger is therefore precise:

1. Later high-phase cube witnesses and their negative exclusions require
   only circular exactness.
2. Before a child is known exact, a missing low-phase square must be
   supplied by its current ambient profile.  Circular exactness supplies
   an ambient mask, but it need not lie inside the displayed child cube.
3. First-copy fitting is needed only by arguments which additionally
   require a common pointed slab, an origin-crossing count, or the
   fitting terminal matching of Section 9 in
   `gadget_cycle_structure.md`.

The Q21 certificate removes fitting from that one terminal subbranch.
It does not by itself prove that every terminal circular configuration
enters the globally maximal Q21 subbranch.  Establishing that terminal
alternative, or eliminating the low-hole masks before it, remains the
bridge needed for a complete circular restart proof.
