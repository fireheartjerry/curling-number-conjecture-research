# Fitting repair for the cube-halving rank

This note repairs the first, pointed loss recorded in Section 10 of
`gadget_cycle_structure.md`.  It does not repair weak-square
inheritance.

Let `P` be a primitive binary circular fixed profile of length `n`,
assume its `3`-runs are singletons, and assume the full first-copy
fitting condition.  A fitting cube ending at its canonical cut
`c in {0,...,n-1}` has an occurrence

```
I=[c-3p,c) subset [1-n,n).                         (1)
```

Every cube root is primitive.  Tightness at a singleton `3` makes its
displayed cube a maximal period-`p` run.

## 1. Containment restores fitting

**Lemma 1.**  Let a proper circular power occurrence

```
J=[x-eq,x)
```

be contained in the fitting interval `I` in (1), where
`x in [1-n,n)`.  Then that occurrence is a first-copy fitting witness
at its circular phase.

Proof.  If `x>=0`, it is already at the canonical cut `x`, and

```
x-eq >= c-3p >= 1-n.
```

This is exactly `eq<=n+x-1`.  If `x<0`, translate `J` by one period
`n`.  It ends at the canonical cut `x+n` and starts at least

```
(1-n)+n=1>1-n.
```

Thus the translated occurrence satisfies the fitting inequality.

The point is that fitting need not survive an arbitrary translation,
but it does survive every translation whose resulting occurrence was
first proved to lie inside one common fitting parent.

## 2. First generation below a maximal fitting cube

Choose `p` maximal among all fitting cube-root lengths and choose the
fitting occurrence `U^3=I`.  At a `3`-cut `x` in the third copy of
`U`, choose a fitting cube root of length `q`.  Global maximality gives
`q<=p`.

The maximal-cube overlap lemma from Section 2 of
`gadget_cycle_structure.md`, applied to the occurrence ending at the
lifted cut `x`, gives

```
2q+gcd(p,q)<p,             q<p/2,                (2)
```

and puts the whole `q`-cube inside `I`.  Lemma 1 then shows that this
contained occurrence is fitting, independently of which period
translate originally supplied the fitting witness.

Thus all first-generation children of a globally maximal fitting cube
can be chosen simultaneously fitting and below half scale.

## 3. Recursive fitting rank

The alignment argument of Section 10 of
`gadget_cycle_structure.md` now preserves fitting.  Here is the exact
induction step.

Let a fitting child `V^3=[x-3q,x)` lie in a fitting parent `U^3`
of period `p`, and choose `q` maximal among the bounded fitting roots
selected at the `3`-cuts in the third copy of `U`.  Let `y` be a
`3`-cut in the third copy of `V`.

If `y` also lies in the third copy of `U`, the selected witness there
has length `s<=q`.  If `y` lies in the second copy of `U`, translate
the cut to `y'=y+p` in the third copy.  Its selected witness has
length `s<=q`; period `p` of `U^3` translates that cube back to `y`.
The calculation

```
y-3s >= start(U^3)+2p+r-q-3q
       = start(U^3)+2p+r-4q
       > start(U^3)                                (3)
```

uses the location `x=start(U^3)+2p+r`, `0<r<p`, and `q<p/2`.
Therefore the translated cube remains inside `U^3`.  Lemma 1 makes
it fitting at phase `y`.

Applying the maximal-run overlap lemma relative to `V^3` now gives

```
2s+gcd(q,s)<q,             s<q/2.                (4)
```

Choose a maximal bounded child at the next generation and repeat.
All occurrences remain inside the original interval `I`, so Lemma 1
applies at every generation.  Positive integer root lengths decrease
by more than a factor two.  Hence the cube hierarchy below a globally
maximal fitting cube has a finite rank whose every selected edge is
first-copy fitting.

## 4. Remaining obstruction

This repairs the claimed possibility that a translated terminal cube
can fall to the left of the distinguished fitting origin: equation
(3) first contains it in the original fitting parent, after which
Lemma 1 canonicalizes it.

It does not make the primitive period code of a child squareful.
A `2`-cut in that code can still be covered in the ambient word only
by a longer square crossing the child boundary.  Therefore the
failed-WSQ certificates in the terminal two-cycle classification
still cannot be invoked.  The residual induction problem is precisely
to classify those crossing fitting square masks.
