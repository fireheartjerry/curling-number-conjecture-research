# A globally maximal wrapping cube forces a half-scale marker cube

This note supplies the audited coordinates for the wrapping lemma used
in the adjacent-`33` and singleton-cube branches.  It is a strict
one-generation descent, not a recursive classification theorem.

## Theorem (wrapping-marker descent)

Let `P` be a primitive binary circular word of length `p` satisfying

`pc_P(d)=P[d] in {2,3}`

at every cut.  Let `V^3` be a proper circular cube ending at a 3-cut,
where `V` is primitive of length `r`, and suppose `r` is largest among
all primitive cube-root lengths at all cuts of `P`.

Rotate the physical cube interval to `[0,3r)`.  Suppose it wraps the
circle.  Then there is a unique integer `ell` such that

`p=3r-ell,             1<=ell<r`.                         (1)

The root has the border and marker equations

`V[0:ell]=V[r-ell:r],   V[ell]=3`.                         (2)

At the occurrence of this marker in the third copy of `V`, namely the
cut

`E=2r+ell`,                                               (3)

there is a primitive cube root `S` of length `s` satisfying

`3s<=E,`

`2s+gcd(r,s)<r`.                                         (4)

In particular, `S^3` is wholly contained in the displayed `V^3` and
`s<r/2`.

### Proof

The factor `V^3` has periods `r` and `p`.  Put `g=gcd(p,r)`.  If

`3r>=p+r-g`,

Fine--Wilf gives period `g` on a factor containing a complete
length-`p` conjugate of `P`.  Since `r<p`, one has `g<p`, contradicting
the primitivity of `P`.  Therefore

`2r+g<p`.                                                (5)

The wrap is less than one full extra circle: equation (5) gives
`3r<2p`.  Hence `ell=3r-p` is positive and unique.  Equation (5) also
gives `ell<r-g<r`, proving (1).

The physical suffix of `V^3` of length `ell` occupies the same circular
positions as its prefix of length `ell`.  This is the first equation in
(2).  The cube ends at circular phase `ell`; its endpoint cut is labelled
three.  Since `ell<r`, that label is the root symbol `V[ell]`, proving
the second equation in (2).

The same root symbol occurs in the third copy at physical position
`E=2r+ell`.  Fixedness at this 3-cut supplies a proper cube `S^3`
ending there.  Replace its root by its primitive root if needed.  A
nonprimitive selected root would only increase its witnessed exponent,
and profile value three excludes that possibility.  Global maximality
of `r` gives

`s<=r`.                                                  (6)

Assume first that `3s>E`.  The child cube starts left of zero, and its
intersection with `[0,3r)` is `[0,E)`.  This intersection has periods
`s` and `r` and length

`E=2r+ell>r+s-gcd(r,s)`

by (6) and `ell>0`.  Fine--Wilf makes a complete conjugate of `V`
periodic with period `gcd(r,s)`.  Primitivity of `V` forces `s=r`.

With `s=r`, the child and outer `r`-cubes overlap and their union is an
`r`-periodic factor of length `4r-ell`.  It also has circular period
`p=3r-ell`, and

`4r-ell >= p+r-gcd(p,r)`.

Fine--Wilf gives the proper period `gcd(p,r)` to a complete conjugate of
`P`, contradicting primitivity.  Thus

`3s<=E`,                                                 (7)

so the child cube lies wholly inside `[0,3r)`.
Since `E<3r`, equations (6)--(7) also exclude `s=r`; hence `s<r`.

The child factor has periods `s` and `r`.  Suppose

`2s+gcd(r,s)>=r`.

Then its length `3s` reaches the Fine--Wilf threshold
`r+s-gcd(r,s)` and is at least `r`.  Fine--Wilf gives the proper period
`gcd(r,s)<r` to the length-`r` conjugate of `V` contained in the child
factor.  This contradicts primitivity of `V`.  Therefore (4) holds.
Its final inequality implies `2s<r`, completing the proof. ∎

## Why one generation does not close the classification

The child `s` is not globally maximal, so the theorem cannot simply be
iterated with `s` in place of `r`.  A later child root may lie strictly
between `s` and `r`.  A recursive proof needs an additional invariant
that survives restriction to the child interval or a theorem that the
first-copy square witnesses stay inside the child.

The two executed near-models in
`check_double_three_near_fixed.py` locate both missing global directions.

* In the length-35 word, a globally largest wrapping root has
  `(p,r,ell)=(35,13,4)`.  The forced internal marker has a cube root
  `s=4`, and `2s+gcd(13,4)<13`.  Every cut is squareful, every 3-label
  has a cube, and no fourth power occurs.  Four 2-labels nevertheless
  acquire forbidden cubes.  One of those later cubes has root length
  `9`, strictly between the descended scale `4` and the old scale `13`;
  local scale descent does not bound subsequent roots.
* In the length-41 word, the corresponding data are
  `(p,r,ell)=(41,16,7)`.  Formula (3) points exactly to cut `33`, one of
  the four 3-labels with no cube.  Every cut is squareful and every
  negative no-cube/no-fourth constraint is satisfied.

Thus the marker descent plus first-copy square coverage does not derive
either the positive cube equations or the negative no-cube equations.
In a true fixed profile both are available, but a proof still has to
show that the resulting hierarchy is well founded.  The strict
one-generation bound (4) alone does not provide that closure.
