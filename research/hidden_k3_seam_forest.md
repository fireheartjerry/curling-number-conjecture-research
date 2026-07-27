# The maximal cubic seam in a surviving hidden `k=3` transition

This note continues `internal_k3_hidden_audit.md`.  It treats its sole
surviving Euclidean form and connects that form to the maximal-run and
square-ancestry formulations.  The conclusion is local: it does not
exclude a later scale-increasing rescue cube.

## 1. Setup

Let `U,V` be primitive binary words with exact proper circular profiles,
and suppose a late internal reset transition has the surviving form

```
U=A B A,
V=U^2 U[:h]=A B A A B A A B,
0<a:=|A|<h:=|A B|,
p:=|U|=h+a,
q:=|V|=3p-a,
A[0]=2,
B[0]=3.                                           (1)
```

Put

```
C=A B,
```

so that

```
U=C A,
V=C A C A C.                                      (2)
```

All cuts below are circular cuts of `V`.

## 2. Binary fixed profiles contain no `333`

### Lemma 1

A primitive binary fixed profile contains no circular factor `333`.

### Proof

Suppose a maximal circular run of `3` symbols has length at least three.
It is followed by `2`, because otherwise the whole circular word consists
of `3` symbols.  At the cut immediately before that following `2`, the
last three symbols form the root-one cube `333`.  The proper circular
profile at that cut is therefore at least three, contrary to its displayed
label two.

If the whole circular word consists of `3` symbols, a word of length
greater than one is not primitive.  The length-one word has no proper
root length and hence cannot have proper circular profile three.  These
cases exhaust the possibility.

## 3. The old root supplies a tight wrapping cube in the new root

Let

```
L=lcs(A,C),
```

the length of the longest common suffix of `A` and `C`.

### Lemma 2

One has

```
0<=L<a,
L<=1.                                             (3)
```

In the periodic lift of `V`, the maximal period-`p` run containing the
displayed old-root cube has interval length exactly

```
3p+L.                                             (4)
```

It ends at cut `a`, and its root-`p` cube endpoints are exactly

```
a-L,a-L+1,...,a.                                  (5)
```

Thus the old root produces either a singleton cubic-run endpoint
(`L=0`) or two adjacent cubic-run endpoints (`L=1`).

### Proof

Use a lift in which one copy of `V` occupies `[-q,0)`.  The prefix of
the next copy through cut `a` is `A`.  Equations (1)--(2) give the exact
word identity

```
V A
  =C A C A C A
  =(C A)^3
  =U^3.                                           (6)
```

Hence a root-`p` cube ends at cut `a`.

For `0<=t<=a`, the period-`p` interval in (6) extends `t` symbols to
the left if and only if

```
suffix_t(C)=suffix_t(A).                          (7)
```

Indeed, the `t` new symbols immediately before the displayed word are
the final `t` symbols of the preceding `V`, hence of its terminal `C`.
Their period-`p` comparison partners are the final `t` symbols of the
first displayed `U=C A`, hence of `A`.  These are all and only the new
equalities required for the left extension.

If (7) held at `t=a`, shifting the length-`3p` window left by `a` would
put a proper root-`p` cube at cut zero.  But

```
V[0]=C[0]=A[0]=2,
```

contradicting `pc_V(0)=2`.  Therefore `L<a`.

For every `1<=t<=L`, shifting the cube left by `t` gives a root-`p`
cube at cut `a-t`.  Exact fixedness forces

```
A[a-t]=V[a-t]=3.
```

Thus the final `L` symbols of `A` are all `3`.  Since the following
letter is `B[0]=3`, the inequality `L>=2` would exhibit the circular
factor `333`, contradicting Lemma 1.  Hence `L<=1`.

There is no right extension.  The first new comparison would identify
the symbol at cut `a` with the symbol one old-root period earlier.
Those two symbols are

```
V[a]=B[0]=3,
V[a-p]=V[2p]=C[0]=2,                              (8)
```

where the second index is reduced modulo `q=3p-a`.  Equation (8)
fails.  On the left, (7) and the definition of `L` show that extension
stops after exactly `L` symbols.  The maximal run therefore has length
`3p+L`.  A period-`p` run of that length has exactly the cube endpoints
listed in (5).

## 4. Relation to the terminal forest

At cut `2p`, the prefix `U^2` gives a root-`p` square and

```
V[2p]=C[0]=2.                                     (9)
```

At cut `a`, equation (6) gives its root-`p` cube maturation and
`V[a]=3`.  Lemma 2 proves that this maturation belongs to a maximal
cubic run with only zero or one symbol of left overhang and no right
overhang.

If `L=1`, the two endpoint labels in (5) are both `3`; Lemma 1 makes
the following label `2`.  This is exactly the equal-root double-component
bridge of `run_stack.md`.  If `L=0`, the root-`p` run has the minimum
possible cubic length and supplies a singleton entrance unless an
unrelated cube root extends the high component.

Consequently the surviving hidden transition has no unbounded seam mask
at the old-root scale.  The remaining obstruction is a different scale:

* if `p` is a globally maximal cube-root length in `V`, the maximal-run
  child argument puts every selected internal marker child below half
  scale;
* if it is not globally maximal, an increasing child cube crosses the
  left endpoint of the run and survives only through the strict
  Fine--Wilf threshold escape.

The first alternative is a one-generation descent.  The second can
increase again and is not excluded by (1)--(9).  Thus (4) sharpens the
location of the residual ascent but does not make root length a
well-founded rank.

## 5. Targeted standard-theorem audit

Two standard repetition theorems do not strengthen the reset estimate
enough to close this branch.

The Crochemore--Rytter Three Squares Lemma states: if

```
u^2 is a proper prefix of v^2,
v^2 is a proper prefix of w^2,
u is primitive,
```

then

```
|u|+|v|<=|w|.
```

See Lemma 4.2 in Berstel, Perrin and Reutenauer, *Combinatorics on
Words*, and Bannai--Mieno--Nakashima, *Lyndon Words, the Three Squares
Lemma, and Primitive Squares*, arXiv:2006.13576.  Applied to three
common-origin reset squares, it gives Fibonacci growth of root lengths.
The unequal-root Fine--Wilf reset estimate already gives more:

```
p_(i+1)>2p_i
```

throughout the late cubic regime.  Hence the Three Squares Lemma adds no
new incompatibility.

The runs theorem of Bannai, I, Inenaga, Nakashima, Takeda and Tsuruta,
*The "Runs" Theorem*, arXiv:1406.0263, gives fewer than `n/(k-1)` runs
of exponent at least `k` and total exponent less than
`n(k+1)/(k-1)`.  For `k=3` these are linear bounds.  A hidden reset
tower has geometrically increasing root lengths, so only logarithmically
many selected cubic seams occur inside a prefix ending at its largest
level.  Such a family is fully compatible with both linear bounds.

These theorems control how many repetitions a finite word may contain.
They do not use the self-label equation at the endpoint of each run, and
therefore do not exclude the crossing-rescue alternative in Section 4.
