# Exact top-component automaton

This note proves the deterministic binary form of a maximal
`H_(M-1)` component in a primitive circular fixed profile, for `M>=4`,
and identifies every phase at which the component can exit.  It does
not by itself produce a lower-maximum fixed profile.

## 1. The valuation word

Put

```
nu(n)=v_M(n)=max {h>=0 : M^h divides n},
B_n=0^M 1^(1+nu(n)),
W_N=B_1 B_2 ... B_N.
```

Starting from `0^M`, consider the deterministic rule

```
append 1  iff the current word ends in Y^M for some nonempty Y;
append 0  otherwise.                                      (A)
```

The exact output before its first overflow is

```
W_(M^(M-1)).
```

Equivalently, if

```
A_(-1)=0,
A_h=A_(h-1)^M 1,
```

then

```
A_h=W_(M^h),
|A_h|=(M^(h+2)-1)/(M-1).                                  (1)
```

The valuation identity behind (1) is

```
nu(s M^h+d)=nu(d)                 for 1<=d<M^h,
nu((s+1)M^h)=h+nu(s+1).                                  (2)
```

Thus each group of `M^h` consecutive blocks has the same first
`M^h-1` run lengths; only its final 1-run records the valuation of the
group number.  Grouping `M` such blocks proves

```
W_(M^(h+1))=W_(M^h)^M 1.
```

## 2. Arithmetic rigidity of a repeated suffix

Write

```
a_i=1+nu(i)
```

for the length of the `i`-th 1-run.  The following observation is the
load-bearing use of `M>=4`.

**Valuation-period lemma.**  Suppose that, for some `q>=1`,

```
a_i=a_(i+q)
```

on an interval of at least `(M-2)q` consecutive positive indices.  Then

```
q=M^h
```

for an integer `h>=0`.

Proof.  Write `q=M^h u`, where `M` does not divide `u`.  If `u>1`, then

```
(M-2)q=(M-2)u M^h >= M^(h+1).
```

The comparison interval therefore contains an index `z` divisible by
`M^(h+1)`.  At that index,

```
a_z>=h+2,
a_(z+q)=h+1,
```

because `(z+q)/M^h` is not divisible by `M`.  This contradicts the
displayed period equation.  Hence `u=1`.

Now consider a nonunary power suffix `Y^e`, where `e` is `M` or
`M-1`.  Every completed 0-run has length `M`.  Translation by
`|Y|` carries transitions to transitions throughout the internal root
copies.  Hence every root copy crosses the same positive number `q` of
0-runs.  Equality of the middle copies gives the run-code comparisons
in the valuation-period lemma:

* for `e=M`, the middle `M-2` copies give `(M-2)q`
  consecutive comparisons;
* for `e=M-1` ending at the same offset in a 0-run, all `M-1`
  copies give `(M-2)q` consecutive comparisons.

Thus every nonunary root used below has

```
q=M^h                                                   (3)
```

0-runs per copy.

For this value of `q`, divide the run code into consecutive `q`-blocks.
By (2), every coordinate of a `q`-block is independent of the block
number except the coordinate occupied by a multiple of `q`.  At that
coordinate the value is

```
h+1+nu(s),
```

where `s` is the block number.  This single distinguished coordinate
will decide both the continuation and exit questions.

## 3. Exact continuation rule

Let

```
U_(n,j)=W_(n-1) 0^M 1^j,
1<=j<=1+nu(n).
```

Then, while `j<M`,

```
U_(n,j) ends in an M-th power  iff  j<=nu(n).             (4)
```

First prove necessity.  Let a nonunary root contain `q=M^h` 0-runs.
Among `M` consecutive `q`-blocks, exactly one distinguished block
number is divisible by `M`.  Its longer 1-run cannot occur strictly
inside one root copy, because translation by the root length would
require the same longer run in every copy.  It must be split between
the two endpoints of the whole power.  Consequently the terminal run
index satisfies

```
M^(h+1) divides n.                                       (5)
```

If `Y` begins in `0`, its internal joins are `1|0`
transitions, and their terminal 1-runs have length `h+1`; hence
`j=h+1`.  If `Y` begins in `1`, write its initial 1-prefix length as
`s>=1`.  Every internal join lies inside a 1-run of length

```
s+j=h+1,
```

so `j<h+1`.  Both cases give

```
j<=h+1<=nu(n),
```

where the final inequality follows from (5).  A unary root requires
`j>=M` and is excluded in (4).

For sufficiency, suppose `j<=nu(n)` and put `h=j-1`,
`q=M^h`.  Then `M q=M^j` divides `n`.  In the final `M`
consecutive `q`-blocks, the first `M-1` distinguished 1-runs have
length `h+1=j`.  The final distinguished run is longer, but
`U_(n,j)` contains exactly its first `j` symbols.  All `M` binary
blocks are therefore identical, explicitly constructing an `M`-th
power suffix.

At the start of every block, the suffix `0^M` supplies the first `1`.
Equation (4) supplies exactly `nu(n)` further `1` symbols.  At
`j=1+nu(n)<M`, (4) excludes another `1`, so rule (A) starts the next
`0^M` block.  This proves the claimed valuation word through
`n=M^(M-1)`.

At that final block,

```
nu(M^(M-1))=M-1,
```

so `W_(M^(M-1))` ends in `1^M`.  The unary root of length one forces
one further `1`, creating `1^(M+1)`.

## 4. Exact zero-phase exits

Fix

```
1<=n<M^(M-1),        0<=r<M,
P_(n,r)=W_n 0^r.
```

This is a zero phase: its next automaton symbol is `0`.  It can be an
`H_(M-1)` component exit only when its internal curling number is at
most `M-2`.  The exact criterion is

```
cn(P_(n,r))<=M-2

iff

r<=M-2,
no base-M digit of n equals M-1,
and [r>0 or nu(n)<=M-3].                         (EXIT)
```

Here only the threshold test is needed: the zero-phase part of Section
3 excludes every `M`-th power, so

```
cn(P_(n,r))>=M-1
```

is equivalent to the existence of an `(M-1)`-th-power suffix.

There are two unary ways to obtain such a suffix:

```
r=M-1,                                    root 0;
r=0 and nu(n)>=M-2,                       root 1.    (6)
```

It remains to classify nonunary roots.  Put `e=M-1`.  If `r>0`
and a root ended in `0` but began in `1`, every internal root join
would complete a 0-run of length `r<M`, contrary to the constant
0-run length `M`.  Hence the root begins in `0`; its joins lie at
the same offset `r` in 0-runs.

If `r=0`, a nonunary root also begins in `0`.  To verify this last
assertion without an endpoint assumption, suppose instead that it
begins with `s>=1` ones.  Its terminal 1-run is the complete run of
length `a_n`.  Every one of the `e-1=M-2` internal joins has the
corresponding complete run length `s+a_n>a_n`.  After (3), translation
by `q=M^h` either preserves the valuation of index `n` or replaces it
by the valuations of `M-2` consecutive quotient indices.  If `q` does
not divide `n`, all corresponding valuations equal `nu(n)`, a direct
contradiction.  If `q` divides `n`, among `M-2>=2` consecutive
predecessor quotients at least one is not divisible by `M`; when the
terminal quotient is not divisible it has the same valuation, and when
the terminal quotient is divisible it has larger valuation.  Neither
case makes all predecessor runs strictly longer.  Thus the assumed
initial `1` is impossible.

The `e` roots therefore give `e` identical `q`-blocks of complete
1-run lengths.  By (2), this happens exactly when the `M-1`
consecutive distinguished block numbers are all nonzero modulo `M`.
Their residues must be

```
1,2,...,M-1.
```

Equivalently,

```
floor(n/M^h) = M-1 modulo M,                            (7)
```

which says that the base-`M` digit of `n` in position `h` is
`M-1`.

Conversely, if that digit is `M-1`, the final `M-1` `q`-blocks are
identical and form a nonunary `(M-1)`-th power.  Appending `r`
zeros preserves the power by conjugation: if the common root is
`D=UV`, where `U=0^r`, then

```
D^(M-1) U = U (VU)^(M-1).
```

Combining (6) and (7) proves `(EXIT)`.

## 5. Uniform bound and the remaining global problem

Once

```
n >= (M-1)M^(M-2),
```

the leading base-`M` digit of `n` is `M-1`.  Every zero phase then
has an internal `(M-1)`-th power, so no component exit is possible.
Continuing the deterministic word reaches the forbidden
`1^(M+1)` overflow.  Therefore every genuine maximal
`H_(M-1)` component exits at one of the phases in `(EXIT)` before this
no-return interval.

The corresponding block prefix has the exact length

```
|W_((M-1)M^(M-2))|
 = (M-1)M^(M-2)(M+1)
   + sum_(k=1)^(M-2) (M-1)M^(M-2-k)
 = M^M-1.
```

In particular every top component has length strictly below `M^M-1`.
This is a uniform bound depending only on `M`.

The cuts in `(EXIT)` are exact *candidate* exits: an external
`(M-1)`-root may still cross the left component boundary.  Turning
the bounded exit words into a synchronized lower-maximum quotient
requires controlling precisely those crossing roots; boundedness alone
does not remove the pointed-return defect.

`research/check_top_component_automaton.py` independently enumerates
every suffix-root length.  It checks every continuation and every exit
phase through the overflow for `M=4` and `M=5`.

## 6. Exit cuts are not synchronizing

The finite exit alphabet does not by itself repair the pointed-return
defect.  Put

```
a=M-1,       b=M-2,
E=b a^M M.
```

For `1<=r<=M-2`, the phase `(n,r)=(1,r)` satisfies `(EXIT)`.
Choose the lower gap to consist only of the exit symbol `b`.  The exact
return word from just after one entrance marker to just after the next is

```
R_r=a^r E.
```

These legal return words satisfy

```
R_(r+1)=a R_r,
R_(r+1) R_r^(a-1)=a R_r^a.                       (8)
```

Thus the raw word on the left of the second equation ends in an
`a`-th power with root `R_r`, but that power starts one symbol inside
the longer return `R_(r+1)`.  At the return-token level there are only
`a-1` complete copies of `R_r`; the exit cut at the power start is not
synchronized.

Equation (8) gives a chain

```
R_1 -> R_2 -> ... -> R_(M-2)
```

in which the block index `n=1` is unchanged and the zero offset
increases.  Reversing the zero-offset order makes this a finite descent,
but it terminates at `R_(M-2)` without contradiction: the aligned word

```
R_(M-2)^a
```

satisfies the terminal `a`-power equation.  Hence neither the finite
component bound nor the base-`M` exit vector alone constructs a shorter
fixed profile or excludes the aligned sinks of the pointed-return graph.
Any successful quotient must retain additional information from the
lower gap or prove a global incompatibility between its aligned sinks.
