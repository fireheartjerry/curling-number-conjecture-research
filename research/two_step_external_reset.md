# Two-step death target after an externally nested reset

This note isolates the exact local statement which would eliminate an
external edge in the all-terminal reset tower.  The first half remains a
classification target; the second half is an unconditional word-equation
lemma.

## 1. Orbit coordinates

Let `U` be a primitive late reset root of length `q`, so the bad high state
is `U^3` and its fixed-first-symbol deletion is

```
D=(U^3)[1:].
```

The reset equations give

```
cn(U^3)=3,       cn(D)=2.
```

The autonomous successor of `D` is `D 2`; the actually driven successor is

```
E=D 3=(U^3)[1:] 3.
```

For every externally created reset root found by the exact solver, the
executed values are

```
cn(E)=2,         cn(E 2)=1.                       (1)
```

The solver hypotheses here are the complete proper circular fixed profile,
the full replay/fitting equations, and a literal prefix `P^3 3` for a
primitive parent `P`.  Through length 60 the only models occur at length 21;
the six externally marked rotations all satisfy (1).  This is finite
evidence, not a proof of (1).

If (1) is proved from those hypotheses, the bad high orbit has only one
possible escape.  At `U^3 3` the high and deleted states must both output
two: a strict deletion step there would make `U^3 3` a whole power, contrary
to the consecutive whole-power lemma because `U^3` is already a reset.
After the common append, the deleted state `E 2` has value one.  Hence the
high state

```
U^3 3 2
```

would have to be a whole power.  The next lemma rules this out.

## 2. A primitive cube followed by `3,2` is not a whole power

### Lemma

Let `U` be a primitive nonempty word beginning in the symbol `2`.  Then

```
U^3 3 2
```

is not a nontrivial whole power.

### Proof

Put `q=|U|` and suppose, for contradiction, that

```
U^3 3 2=V^k,       k>=2,
```

where `V` is primitive and `r=|V|`.  The total length is

```
N=3q+2=k r,
```

so

```
r<=N/2=(3q+2)/2.                                  (2)
```

The common prefix `U^3` of length `3q` has periods `q` and `r`.  For
`q>=2`, equation (2) gives

```
q+r-gcd(q,r) <= q+r <= (5q+2)/2 <=3q.
```

Fine--Wilf therefore makes this common prefix have period
`d=gcd(q,r)`.  Its first length-`q` block is the primitive word `U`, so
`d=q`.  Thus `q` divides `r`.

If `r>q`, then `r>=2q`.  Equation (2) makes this impossible for `q>=3`.
For `q=2`, it forces `r=4`; but then the first root `V`, being the first four
symbols of `U^3`, is `U^2` and is not primitive.  Hence `r=q`.

Since `r` divides `N=3q+2`, the equality `r=q` implies `q` divides two.
The case `q=2` has `U=(2,x)` with `x!=2` by primitivity.  The last
length-two block of `U^3 3 2` is `(3,2)`, whereas its first length-two block
is `(2,x)`, so the word cannot have period two.  The case `q=1` has
`U=(2)` and gives the word `(2,2,2,3,2)`, whose length five admits no
nontrivial whole-power exponent except five; it is not unary.  These cases
contradict the assumed power representation.

Thus `U^3 3 2` is not a nontrivial whole power.

## 3. Exact remaining local lemma

The load-bearing target is now:

> If a primitive binary late reset root `U` has its complete proper
> circular fixed profile, full first-copy replay/fitting equations, and was
> created by an external edge (so `U` begins in `P^3 3` for a primitive
> parent `P`), then (1) holds.

The literal ancestry is essential.  Executed enumeration of all 15 fitted
length-21 rotations, without the parent-marker restriction, contains
examples with `tau(E)>tau(D 2)` and examples in which `cn(E)` is three.
Consequently no proof may use only fixedness and fitting.
