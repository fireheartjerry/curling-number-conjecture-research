# Early divergence of an autonomous square self-generator

This note audits the early-divergence branch in
`golden_bad_cuts.md` and records two additional reductions.  It does not
exclude the branch.

## 1. Setup and the Fine--Wilf reduction

Let `P` be primitive, put `p=|P|`, and assume

`cn(P P[:d])=P[d]` for `0<=d<p`, and `cn(P^2)=2`.

In the counterorbit application every symbol of `P` is at least two.
Put

`A_d=P P[:d]`, `B_d=P^2 P[:d]`.

Suppose `h`, with `1<=h<p`, is the first index at which the two curling
numbers differ.  Suffix monotonicity makes `B_h` the high side.  Let its
value be `k` and let `r` be a primitive maximizing-root length.  The
common suffix `A_h` has length `p+h`, so

`k r>p+h`.                                                   (1)

The terminal `k r` letters also have period `p`.  If

`k r>=p+r-gcd(p,r)`,

Fine--Wilf makes a complete primitive `p`-block or a complete primitive
`r`-block have a proper divisor period.  The only nonproper possibility
is `p=r`, which cannot fit `k>=3` copies in `B_h`.  Consequently

`(p+h)/k<r<(p-gcd(p,r))/(k-1)`.                              (2)

Write

`s=p-(k-1)r`, `C=2p+h-k r`.

Then

`gcd(p,r)<s<r-h`, `0<=C<p`,

and the length-`p` factor beginning at `C` gives

`rot_C(P)=Y^(k-1)Y[:s]`,                                    (3)

where `Y` is the primitive maximizing root of length `r`.

Every symbol of `Y` occurs at a generated position in the final copy of
the displayed power and is preceded by `k-1` rotated copies of `Y`.
Thus every symbol of `Y` is at least `k-1`.  Equation (3) puts every
symbol of `P` in `Y`; since `P[0]=2`, this gives `k<=3`.  The strict
increase from a source label at least two gives

`k=3`, `cn(A_h)=P[h]=2`.                                    (4)

Hence

`p=2r+s`, `C=r+2s+h`, `gcd(r,s)<s<r-h`.                     (5)

Here `gcd(p,r)=gcd(r,s)`.

## 2. The hidden short period

Put

`a=p-C=r-s-h`.

The cube suffix of `B_h` gives two descriptions of `P`:

`P=rot_a(Y^2Y[:s])`

and, because `A_h=Y[a:]Y^2`,

`P=Y[a:]Y Y[:r-h]`.

Comparing them gives

`Y[:r-h]=Y[:s]Y[:a]`.                                      (6)

Also `P[:h]=Y[a:a+h]`, and comparing the final `r` letters of `A_h`
gives

`Y[r-h:r]=Y[a:a+h]`.                                       (7)

Since `s+a=r-h` and `a+h=r-s`, concatenating (6) and (7)
gives

`Y[s:r]=Y[:r-s]`.                                           (8)

Thus `s` is a period of `Y`.  This does not contradict primitivity:
`s` does not divide `r`, because `gcd(r,s)<s`.

Let

`r=q s+u`, with `0<u<s`.

The state `A_h` ends in `Y^2` and has curling number two.  If `q>=3`,
the final `3s` letters of its last copy of `Y` are three equal
length-`s` blocks.  Therefore

`q in {1,2}`.                                               (9)

There is a second useful constraint.  The suffix `Y[:r-h]` of `P` and
the prefix `Y[a:]` of the appended copy meet in the correct `s`-phase,
because `a` and `r-h` differ by `s`.  Hence, for
`0<=d<=s+h`, the state `A_d` has a terminal `s`-periodic suffix of
length

`r-h+d`.                                                    (10)

The labels at `d=0` and `d=s` are equal:

`P[s]=Y[a+s]=Y[a]=P[0]=2`.

Equation (10) at `d=s` therefore gives

`r-h+s<3s`, or `r<2s+h`.                                   (11)

If `h>s`, then `d=2s<s+h`, `P[2s]=P[0]=2`, while (10) has
length `r-h+2s>3s`, a contradiction.  Thus

`h<=s`.                                                     (12)

Equations (9)--(12) leave exactly:

* `q=1`: `r=s+u` and `1<=h<u`;
* `q=2`: `r=2s+u` and `u<h<=s`.

## 3. Exact quotient-two shadow

Assume `r=2s+u`, `u<h<=s`, and put

`D=Y[:s]`, `d_*=h-u=s-a`.

Periodicity (8) says `Y=D^2D[:u]`.  At the following two families of
states, direct substitution in (10) gives the displayed suffixes:

`U_j=A_(d_*+j)` ends in `D^2D[:j]`,

`V_j=A_(d_*+s+j)` ends in `D^3D[:j]`, for `0<=j<=u`.

For `0<=j<u`, both cuts lie in the same `s`-periodic prefix segment of
`P`, so the exact, not merely lower-bound, labels are

`cn(U_j)=cn(V_j)=D[j]`.                                     (13)

At `j=u` the two exact labels are

`cn(U_u)=D[u]=2`,

`cn(V_u)=D[0]`.                                             (14)

Every `V_j` ends in the cube of the rotation of `D` by `j`.
Equations (13)--(14) therefore imply

`D[0],...,D[u-1]>=3`, and `D[u]=2`.                         (15)

The word `D` is primitive.  If `D=E^m`, `m>=2`, then the
rotation of `D` by `u` is an `m`-power.  Since `U_u` ends in the square
of that rotation, it ends in a `2m`-power, contradicting
`cn(U_u)=2`.

More geometrically, put

`R=rot_u(D)`.

Then `U_u=A_h` ends in `R^2`, has curling number two, and its next
`s` orbit labels are exactly `R`.  The resulting state is
`V_u=A_(s+h)`, which ends in `R^3` and has exact curling number
`D[0]>=3`.  The square and cube have the same origin.  Thus quotient
two does not immediately contradict replay; it converts the original
early death at root length `r` into a strictly smaller, contexted,
fixed-origin square-to-cube maturation at primitive root length `s`.

## 4. Exact quotient-one shadow

Assume `r=s+u`, `1<=h<u`, and put

`a=u-h`, `D=Y[:s]`, `R=rot_a(D)`.

The word `P` begins and ends in the same length-`s` block `R`.  Indeed,
its terminal `s+a` letters are `D D[:a]`, and its first `s` letters
are `D[a:]D[:a]`.  Consequently

`A_s=P R` ends in `R^2`,

and the exact replay equation gives

`cn(P)=cn(A_s)=R[0]=2`.                                    (16)

The word `D`, and therefore `R`, is primitive: otherwise `R^2` is a
power of exponent at least four, contradicting (16).

Compare the orbit states `P` and `A_s`.  Their next labels agree with
`R[t]` for `0<=t<h`.  After that point, the source continues with the
rotation of `D` by `u`, whereas the target continues with `D`.
Let

`delta=min{j: D[j] != D[(u+j) mod s]}`.

This set is nonempty; equality for every `j` would give `D` period
`gcd(s,u)` and would make `Y=D D[:u]` imprimitive.  Put

`H=min(s,h+delta)`.

The two label streams agree for exactly `H` steps unless `H=s`; in the
latter case the target reaches a suffix `R^3` and its next curling
number is at least three, whereas the source value at the corresponding
square state is two.  For `H<s`, both states have the identical terminal
shadow

`R R[:H]`

of length `s+H`.  Any maximizing power on the high side of their first
mismatch must cross the left edge of that shadow.  Thus, if its exponent
is `k` and its primitive root length is `rho`,

`k rho>s+H`.                                                (17)

This is a strict reduction from the original root length `r=s+u` to a
contexted replay defect at the primitive root length `s`.  The unresolved
point is orientation: unlike the original `A_d`/`B_d` comparison, neither
of these two states is a suffix of the other.  At an early mismatch
`H<s`, (17) alone does not determine which side has the larger curling
number.

## 5. Executed finite falsification search

`search_early_square.cpp` enumerates the reduced parametrization above,
constructs `Y` and `P`, and executes every source replay equality, the
boundary value `cn(P^2)=2`, and the target comparison.  The executable
uses the same exhaustive repeated-suffix definition as `curling.py`.

The executed binary search (`MAX_SYMBOL=3`) found no exact source
self-generator in the reduced family for `s<=18`.  The executed search
over symbols `{2,3,4}` found none for `s<=11`.  These are finite
falsification checks only.

