# Root-one ancestry sources versus terminal run-code gadgets

This note fixes the terminology at the interface between
`circular_low_hole_transition.md`, Section 18, and
`gadget_cycle_structure.md`, Sections 7--9.  It does not prove the
terminal-saturation lemma stated in Section 5 below.

## 1. Coordinates of an external root-one source

Assume the singleton-`3` run-code setting

```
W=Q(A)=product_i 2^(a_i)3,  A=(a_0,...,a_(m-1)),
a_i in {1,2,3},
```

with cyclic indices.  Assume also the exact proper circular profile and
the distinguished first-copy fitting condition used in the two cited
notes.

Let `(c,1)` be a fitting square-ancestry vertex whose one-symbol square
root is `2`.  An *external* outgoing edge is the case in which the
nearest preceding high cut is

```
h=c-3.
```

In physical coordinates this gives

```
W[h],W[h+1],W[h+2],W[h+3] = 3,2,2,2.          (1)
```

Let `i` be the run-code index of the `2`-run immediately before the
marker `W[h]=3`.  The three `2` symbols after that marker form the next
run.  A fourth `2` would be a proper fourth power at the following cut,
contrary to the profile alphabet `{2,3}`.  Hence

```
a_(i+1)=3.                                      (2)
```

Choose the fitting cube root `q` at high cut `h` which defines the
ancestry edge.  Its child is the fitting square vertex

```
(h-q,q).                                        (3)
```

Equations (1)--(3), including `a_(i+1)=3`, describe the *source* of the
edge.  They do not yet describe a terminal run-code gadget.

## 2. Exact selected-cube/run-code dictionary

There are two cases.

### 2.1 Unary selected cube

If `q=1`, the cube ending at `h` is the final `222` before the marker at
`h`.  Thus `a_i=3`.  Its root contains no `3` marker, so its code span is
zero.  The weighted defect graph only has spans `s>=1` and endpoints
`a_i in {1,2}`.  Therefore this selected cube has **no corresponding
tight gadget edge**.

This is the first reason that “external source” and “terminal gadget”
cannot be synonyms.

### 2.2 Nonunary selected cube

Suppose `q>1`.  Its root is primitive: a nontrivial power used three
times would give exponent at least six at a cut whose exact value is
three.  A primitive binary root of length greater than one is not unary,
so it contains at least one `3`.  Let

```
s = number of `3` markers in one root copy.
```

The general cube equation and the tightness lemma give

```
j=i-3s,
beta=a_i,
g=a_(i-s)=a_(i-2s),
alpha=g-beta=a_j>=1,
C=(a_(j+1),...,a_(j+s-1)),
```

and the clipped ambient code

```
[alpha,C,g,C,g,C,beta].                         (4)
```

The primitive circular run code of the physical cube root, in the
orientation selected by (4), is

```
R=(C,g),  |R|=s,                                (5)
```

and its physical length is

```
q=sum_(x in R)(x+1).                            (6)
```

Since `alpha>=1`, `beta>=1`, and `g<=3`, equation `g=alpha+beta`
forces

```
beta in {1,2}.
```

Thus `i` is a defect and (4) is a tight gadget edge of code span `s`
ending at `i`.  The source information (2) appends only one ambient
entry after its endpoint:

```
[alpha,C,g,C,g,C,beta | 3].                     (7)
```

The entry after the bar is outside the primitive period code `R`.
First-copy fitting of the selected ancestry cube is exactly
first-copy fitting of this gadget; in canonical run indices it is the
inequality

```
3s<=m+i-1.
```

## 3. What “terminal” adds

Section 7 of `gadget_cycle_structure.md` calls the selected gadget
terminal only when

```
every defect of R has an available tight span-one child
inside the periodic word Q(R).                   (8)
```

The source equation `a_(i+1)=3` in (2) makes no assertion about the
defects of `R=(C,g)`.  Therefore the external source proves the existence
of the tight gadget (4) only in the nonunary case; it does not prove
(8).

The terminal-edge residue lemma gives the complete possibilities once
(8) is separately known:

```
s=1:  R=(3);
s>1:  s=6 and R is a rotation of (1,3,3,2,3,3). (9)
```

The corresponding physical root lengths from (6) are four and
twenty-one.  Consequently a nonunary external edge selects a terminal
gadget exactly in one of the classified cases (9), not merely because
its source root is the symbol `2`.

The accurate terminology is therefore:

* `(c,1)` with root symbol `2` and distance three is a
  **root-one/`2` external source**;
* its selected nonunary cube gives a **tight gadget** by (4)--(6);
* that gadget is **terminal** only if it satisfies (8).

## 4. Executed examples

For the standard Q21 word, the two external sources are `(5,1)` and
`(15,1)`.  Executed enumeration gives selected cube root four at high
cuts two and twelve.  In run code

```
A=(2,3,3,1,3,3),
```

the corresponding gadgets end at defects zero and three.  Both have
span one and period code `(3)`, so both happen to be terminal.

That implication is false with only the local edge equations and fitting.
The primitive code

```
A=(1,3,2,3,2,3)
```

expands, after moving the distinguished physical origin one symbol, to

```
W=32322232232223223222.
```

At high cut two and source cut five, executed proper-profile computation
gives values three and two.  The boundary is `3,2,2,2`, and the selected
root-seven cube is first-copy fitting.  It gives the fitting ancestry edge

```
(5,1) -> (15,7).
```

Its tight gadget has span two and period code `(3,2)`.  The defect in
that period code has no tight span-one child, so the gadget is
nonterminal.

This word is a countermodel only to a *local* terminality inference.  Its
proper profile is not equal to the word at every phase, so it does not
refute a bridge lemma using the complete fixed-profile hypotheses.
Every value and root set in this section is recomputed by

```
python research/check_terminal_source_gadget_bridge.py
```

after the required A094004 calibration.

## 5. Exact remaining global lemma

For an ambient run code `A`, put

```
D(A) = {i : a_i in {1,2}},
T_A(i) = set of first-copy fitting tight gadgets ending at i
         which are terminal in the sense of (8).
```

Section 18 of `circular_low_hole_transition.md` proves that every
extended fitting ancestry cycle contains a root-one/`2` external source.
Section 9 of `gadget_cycle_structure.md` starts from

```
T_A(i) is nonempty for every i in D(A).           (10)
```

The weakest single implication which connects those two existing results
without strengthening the Section 9 conclusion is the following pointed
global statement.

> **Terminal-source saturation lemma.**  
> Under the primitive singleton-`3` exact-profile and full first-copy
> fitting hypotheses, if the extended fitting square-ancestry graph has a
> directed cycle containing a root-one/`2` external source, then (10)
> holds in the same distinguished lift.

Together with Section 18, this lemma supplies the hypothesis of Section
9, which then forces `A` to be a rotation of `133233`.

A logically weaker direct completion, because it omits the intermediate
terminal-edge conclusion, is:

> **Anchored-cycle classification lemma.**  
> Under the same hypotheses, the existence of an extended fitting
> ancestry cycle containing a root-one/`2` external source forces `A` to
> be a rotation of `133233`.

Either lemma is genuinely global.  A proof must handle all of the
following losses:

1. a selected unary cube has no gadget at all;
2. a selected nonunary cube can give a nonterminal gadget, as in Section
   4;
3. the selected external-source gadget must be attached to a contained
   hierarchy below a globally maximal fitting cube; the containment lemma
   in `fitting_cube_halving_rank.md` preserves fitting once that attachment
   is established; and
4. first-copy weak-square coverage can be supplied by a larger square
   crossing a descendant boundary, so it is not inherited by the
   primitive period code.

The unpointed halving rank proves finite descent inside a displayed cube.
The contained fitting-rank repair resolves the translation part of item
3 for a hierarchy below a globally maximal fitting cube.  It still does
not prove terminal-source saturation: it neither attaches every ambient
defect to one such hierarchy nor resolves the crossing weak-square masks
in item 4.
