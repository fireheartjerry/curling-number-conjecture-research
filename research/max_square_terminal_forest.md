# The longest square and its last cube

This note proves a strict one-generation descent in a binary critical
profile.  It also records exactly why that descent is not yet a
well-founded forest and how the minimum-seed terminal-prefix constraint
enters.

Let `P` be a primitive word of length `n` over `{2,3}` with exact proper
circular profile

```
pc_P(j)=P[j]                                           (1)
```

at every phase.  A root is always a proper circular root, so its length
is below `n`.  Let `p` be the greatest root length of a square ending at
any phase labelled `2`.  Every such root word is primitive: if it were
an `h`-th power with `h>=2`, its square would have exponent at least
four, contradicting (1).  The same argument makes every cube root at an
exact `3`-phase primitive, since a nontrivial power used three times
would have exponent at least six.

## 1. A cube has a same-scale low midpoint

### Lemma 1

Suppose a root-`q` cube ends at a phase `a` with

```
P[a]=3,       P[a+1]=2.                              (2)
```

Then

```
P[a-q]=2,                                            (3)
```

and a root-`q` square ends at phase `a-q`.  In particular `q<=p`.

### Proof

The first two blocks of the displayed cube form a root-`q` square ending
at `a-q`.  Equation (1) therefore gives

```
P[a-q] in {2,3}.
```

Assume `P[a-q]=3`.  The cube is `q`-periodic on
`[a-3q,a)`.  Every equality needed to shift this cube one position to
the right is already in that interval except

```
P[a]=P[a-q].
```

The assumed value supplies this last equality, so a root-`q` cube ends
at `a+1`.  This contradicts `P[a+1]=2` in (2).  Hence (3) holds.  The
already displayed square is consequently a maximizing square at a
`2`-phase, and the definition of `p` gives `q<=p`.

This lemma is the bridge that allows a maximum over low square roots to
bound high cube roots.  Merely observing that a cube contains a square
does not give that bound, because the cube endpoint itself is labelled
three.

## 2. The last high phase of a longest square

Choose a root-`p` square ending at a phase `c`, so `P[c]=2`, and let
`U` be its length-`p` root.  Let `a=c-d` be the closest preceding
phase labelled `3`.

There is no circular factor `2222`: such a factor would give an
exponent-four suffix at the following cut, contradicting (1).  Therefore

```
1<=d<=3.                                             (4)
```

The phase `a` lies in the final copy of `U`.  To see this, first note
that `p>=2`.  If `p=1`, choose any final `3` of a `3`-component; it is
followed by `2`.  Lemma 1 makes every one of its cube roots a root-one
square at a low cut, hence the root is one.  At the following low cut,
the assumed global bound also forces a root-one square.  Lemma 1 says
the symbol one place before the high phase is `2`, whereas that latter
square would require it to equal the high symbol `3`, a contradiction.

If `d>p`, every symbol of `U=P[c-p:c]` is `2`.  Since `p>=2`, this makes
`U` a nontrivial power, contrary to its primitivity.  Thus

```
d<=p.                                                (5)
```

Let a root-`q` cube end at `a`; such a root exists by (1).  Lemma 1
applies because `a` is the last high phase and gives `q<=p`.

### Lemma 2 (strict half-scale last cube)

With the preceding notation, every root-`q` cube ending at `a` satisfies

```
p>2q+gcd(p,q).                                       (6)
```

Consequently

```
q<p/2,
3q+d<=2p,                                           (7)
```

so the entire child cube is contained in the displayed `U^2`.

### Proof: exclusion of equal scales

Suppose `q=p`.  The root-`p` cube on `[c-d-3p,c-d)` and the root-`p`
square on `[c-2p,c)` overlap in `2p-d>=p` symbols by (5).  Two
period-`p` intervals with an overlap of at least `p` symbols have a
period-`p` union.  Their union contains the length-`3p` suffix ending at
`c`, so a root-`p` cube ends at the phase labelled `2`.  This
contradicts (1).  Hence `q<p`.

### Proof: contained child

Assume first that

```
c-d-3q >= c-2p.                                      (8)
```

The child cube then has periods `p` and `q`.  Put `g=gcd(p,q)`.  If
`p<=2q+g`, its length `3q` meets the Fine--Wilf threshold

```
p+q-g.
```

It also has length at least `p`.  Fine--Wilf gives period `g` to the
child cube, and a complete length-`p` conjugate of `U` inside it
therefore has period `g<p`.  Since `g` divides `p`, that conjugate, and
hence `U`, is a nontrivial power.  This contradicts primitivity.
Therefore (6) holds in the contained case.

### Proof: crossing child and the sole threshold escape

Assume instead that the child cube starts before the square.  Their
intersection is

```
[c-2p,c-d)
```

of length `2p-d`.  It has periods `p` and `q` and contains a complete
length-`p` conjugate of `U` by (5).  If

```
2p-d >= p+q-g,
```

Fine--Wilf again makes that conjugate `g`-periodic, contradicting
primitivity.  Threshold failure is therefore necessary:

```
p-q+g<d.                                             (9)
```

Here `p-q>=1`, `g>=1`, and `d<=3`.  The only integer possibility is

```
d=3,       q=p-1,       g=1.                        (10)
```

It remains to discharge (10), rather than calling it an exceptional
case.  On the intersection of length `2p-3`, number coordinates from
zero.  Its periods are `p` and `p-1`.  For `0<=i<=p-4`, the two period
relations give

```
position i  = position i+p = position i+1.
```

Thus positions `0,...,p-3` are in one equality component.  Period
`p-1` then attaches every position `p-1,...,2p-4` to that component.
The only other component is the singleton position `p-2`.

The endpoint symbols contradict this equality graph.  Square period
`p` gives

```
P[c-p-3]=P[c-3]=3,
P[c-p-1]=P[c-1]=2.                                  (11)
```

The two left-hand positions have intersection coordinates `p-3` and
`p-1`, which belong to the same component.  Equations (11) would
therefore identify `3` and `2`.  This eliminates (10), so the crossing
case is impossible.

We have proved (6).  Since all quantities are integral and `g>=1`,

```
p>=2q+2.
```

Together with `d<=3`, this gives

```
2p-(3q+d) >= q+4-d > 0,
```

which proves containment and (7).

## 3. What this gives as a forest

The cube in Lemma 2 has a canonical same-scale square node: Lemma 1
places a root-`q` maximizing square at phase `a-q`.  Thus every globally
longest square occurrence has a child square occurrence of root length
strictly below half its own length.

There is a version using only first-copy fitting witnesses.  Let `p_f`
be the largest fitting square-root length at a low phase, and choose a
fitting root-`p_f` square.  At its last high phase choose a fitting cube
root `q`.  Lemma 1 places the root-`q` square at `b=a-q`.  Its fitting
inequality is automatic:

```
3q<=n+a-1  implies  2q<=n+b-1,                    (12)
```

where a negative `b` is normalized by adding `n`, which only enlarges
the right side.  Hence `q<=p_f`, and the proof of Lemma 2 applies without
using any nonfitting root.  The maximum fitting square therefore also
has a fitting child below half scale.

More generally, form the fitting square-ancestry graph.  Its vertices
are fitting square occurrences `(c,s)` at low cuts.  If the final
length-`s` root contains a high phase, let `a=c-d` be its last one and
choose any fitting cube root `q` there.  Direct an edge to the fitting
square occurrence

```
(a-q,q).                                             (13)
```

A primitive square root of length greater than one cannot be all `2`,
so every such vertex has an outgoing edge.  A root-one vertex whose
root symbol is `2` is terminal.

Every edge has one of two exact geometries:

```
q<s  =>  s>2q+gcd(s,q), and the q-cube is contained;
q>s  =>  q>s+gcd(s,q)-d, and the q-cube crosses the
         left boundary of the s-square.              (14)
```

Equality `q=s` is excluded by the equal-scale argument in Lemma 2.
The first line is the contained Fine--Wilf proof already given, with
`s` in place of `p`.  For the second line, the overlap has length
`2s-d` and periods `s,q`.  If it met the Fine--Wilf threshold, it would
have period `g=gcd(s,q)` and would be long enough to contain complete
conjugates of both roots.  If `g<s`, this makes the square root
imprimitive.  If `g=s<q`, it makes the cube root imprimitive.  It
therefore cannot meet that threshold, so

```
2s-d<s+q-gcd(s,q),
```

which is the displayed inequality.  The larger cube cannot be
contained because `3q>2s`.

Lift an edge without reduction modulo `n`.  Its endpoint changes from
`c` to

```
c-d-q<c.                                             (15)
```

Thus the ancestry is a genuine forest in the universal periodic lift.
A directed cycle after reducing phases modulo `n` is necessarily a
wrap cycle and satisfies

```
sum_edges (d+q)=w n,       w>=1.                    (16)
```

This identifies the precise recurrent objects which a globalization
must eliminate.

The graph is not recursively decreasing in root length.  At a
nonmaximal square node of length `s`, the required cube at the last high
phase can have root length greater than `s`; the global argument only
bounds it by `p_f`.  Q21 executes this ascent: square roots of length
three at its low cuts have last-high cube roots of length four.
Orienting every edge by decreasing root length gives an acyclic graph,
but does not give unique parents and does not show that every leaf is a
terminal unary cube.  Reusing Lemma 2 at a nonmaximal node would
therefore be circular.

The useful exact conclusion is:

```
global maximum square
    -> contained last cube below half scale
    -> same-scale low square node.                 (17)
```

A complete forest argument must add a ranked object which survives
possible later scale ascents.  Root length alone is not such an object.

## 4. The terminal-prefix constraint

For a minimum-length critical counterexample the separate minimality
argument gives

```
cn(P[:-1])<P[-1].                                    (13)
```

Fixedness gives the reverse weak bound `cn(P[:-1])<=P[-1]`; strictness
in (13) means that every proper circular witness attaining the final
phase value crosses the distinguished origin.

The desired terminal-prefix theorem would say that fixedness plus the
full first-copy fitting equations already imply

```
cn(P[:-1])=P[-1].                                    (14)
```

Equations (13) and (14) would contradict one another.  Lemma 2 narrows
the missing step but does not by itself prove (14).  If the final label
is two, (13) says every final-phase square root has powered span greater
than `n-1`, while phase zero has a fitting square of powered span at most
`n-1`.  These are adjacent origin-crossing and origin-internal square
episodes.  If the final label is three, every final-phase cube attaining
three likewise has span greater than `n-1`.

A globally longest square in this origin-crossing family contains the
strict half-scale child of Lemma 2.  To prove (14), one must transport a
power attaining the *same final phase* wholly into `P[:-1]`.  The child
cube in (17) ends at an earlier high phase, so containment alone does not
perform that transport.  Copy-parent iteration can wrap around the
distinguished origin, and after a wrap the root scale can rise again.
This is the exact recurrent-forest gap; first-copy fitting must be used
to eliminate the wrap cycles (16).  No strict rank accomplishing that
transfer is established here.

## 5. Executed calibrations

`research/check_max_square_terminal_forest.py` recomputes all root sets,
proper profiles, and finite curling numbers used in these calibrations.

For the exact critical length-21 word, the global low-square length is
ten, attained at cuts zero and one.  The last high phase has a root-one
cube, at distance one or two respectively, and the inequalities in
Lemma 2 hold.  All fifteen rotations beginning in `2` satisfy the full
first-copy fitting condition and the terminal-prefix equality (14).

For the length-64 bridge model, the global low-square length is 43 at
cut 42; its last high is one phase earlier and has cube-root length one.
The local Lemma 2 geometry holds.  This model has proper-profile
mismatches at cuts 1, 5, and 10, so it is an audit of the overlap
geometry, not a counterexample to the terminal-prefix theorem.

The same script checks the threshold-minus-one equality graph for every
`3<=p<=200`.  That finite check is a calibration of the symbolic
component proof above, not its justification.
