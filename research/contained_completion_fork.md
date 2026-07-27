# Hard constraints at the contained symbol-two completion fork

This note treats the remaining ordinary fork

```
H=C^3 3  bad,
E=C^3 2  terminal,
```

where `C` is primitive, `C[0]=2`, `pc_C=C`, and `min(C)=2`.  Put

```
D=C^3[1:],
F=D3,
B=D2.
```

The three-word seam gives `B=rot(C)^3` terminal.  Every nontrivial
maximizing root of `H` is shorter than `|C|`, so it is also a suffix
root of `F`; hence `cn(F)=cn(H)`.  The status of `F` is not determined
by this local containment.

## 1. A shifted wrong completion is never a whole power

### Lemma 1

Let `W` be a primitive nonempty word, let `m>=2`, and let `x` be a
symbol different from `W[0]`.  Then

```
(W^m)[1:] x
```

is not a nontrivial whole power.

### Proof

Put `n=|W|` and suppose

```
(W^m)[1:] x=V^k,
```

where `V` is primitive, `k>=2`, and `r=|V|`.  The total length is
`mn`, so `r` divides `mn` and `r<=mn/2`.

The common prefix `(W^m)[1:]` has length `mn-1` and periods `n` and
`r`.  With `g=gcd(n,r)`, the Fine--Wilf threshold is reached:

```
n+r-g <= mn-1.
```

For `m=2`, this follows from `r<=n` and `g>=1`.  For `m>=3`, it follows
from `r<=mn/2`, since

```
n+mn/2-1 <= mn-1.
```

Fine--Wilf gives period `g` to the common prefix.  This prefix contains
a complete conjugate of the primitive word `W`, so `g=n`.  Therefore
`n` divides `r`; write `r=dn`.

The first length-`r` block of the proposed power is `d` copies of the
left rotation

```
W[1:]W[0].
```

If `d>1`, this root block is not primitive, contrary to the choice of
`V`.  Hence `d=1` and `r=n`.

Period `n` now compares the last length-`n` block

```
W[1:]x
```

with the preceding block `W[1:]W[0]`.  It forces `x=W[0]`, contrary
to the hypothesis.  This proves the lemma.

For the completion fork, Lemma 1 gives

```
F=(C^3)[1:]3
```

is not a nontrivial whole power.  Therefore a proof may not treat a
bad `F` as an immediate reset.  Under the current minimum-endpoint-rank
selection, a bad word of the same length need not be an immediate
whole power; this lemma does not by itself determine the status of `F`.

## 2. The value-three completion casts an exact periodic shadow

### Lemma 2

Assume

```
u=cn(C^3 3)=3.
```

Let `Z` be a primitive maximizing root of length `p<|C|`.  Write

```
Z=V3,             T=3V.
```

In the circular lift of `C`, with phase zero at `C[0]=2`,

```
C[-3p:0]=2 V T^2.                                (1)
```

The interval

```
[1-3p,0)
```

is an exact maximal period-`p` run of length `3p-1`.  Its internal cut
`-p` has label three.

Let `q` be any primitive cube-root length at cut `-p`, supplied by
`pc_C(-p)=3`, and put `g=gcd(p,q)`.  Then `q!=p` and

```
min(2p-1,3q)<p+q-g.                              (2)
```

Consequently exactly one of the numerical orientations holds:

```
q<p  =>  2q+g<p,
q>p  =>  q>=p+g.                                 (3)
```

### Proof

The last `3p` symbols of `C^3 3` are `Z^3`.  Removing the appended
final symbol leaves

```
Z^3[:-1]=V(3V)^2=VT^2
```

as the length-`3p-1` circular suffix before phase zero.  If the
preceding symbol were `3`, then `T^3` would end at phase zero, contrary
to `pc_C(0)=C[0]=2`.  Binarity forces that preceding symbol to be `2`,
which proves (1).

At the right boundary of the displayed period-`p` run, the actual
symbol is `C[0]=2`, while period `p` requires
`C[-p]=T[0]=3`.  At the left boundary, the actual symbol in (1) is
`2`, while the period mate at the start of the first displayed `T` is
`3`.  Thus neither boundary extends, proving the exact run assertion.

Equation (1) also gives `C[-p]=3`, so exactness supplies a cube at that
cut.  A selected cube root is primitive: a proper-power root repeated
three times would give exponent at least six at a cut of exact value
three.  Root length `p` cannot even supply a square at cut `-p`, because
the two preceding length-`p` blocks begin in the distinct symbols `2`
and `3`.  Hence `q!=p`.

The overlap of the period-`p` run with the `q`-cube ending at cut `-p`
has length

```
L=min(2p-1,3q).
```

If `L>=p+q-g`, Fine--Wilf gives period `g` to an overlap containing a
complete conjugate of the longer primitive root.  Since `p!=q`, one has
`g<max(p,q)`, contradicting primitivity.  This proves (2).

If `q<p` and `3q>2p-1`, equation (2) would give `q>=p+g`, a
contradiction.  Therefore `L=3q`, and (2) rearranges to
`2q+g<p`.  If `q>p`, then `L=2p-1`, and (2) rearranges over the
integers to `q>=p+g`.  This proves (3).

The ascent in (3) is genuine.  In the exact length-21 profile, executed
examples are

```
p=3 -> q=4,
p=2 -> q=4.
```

Thus Lemma 2 is not a monotone root descent.  A completion-fork proof
must discharge the ascending internal cube by status/origin information,
not by the local overlap alone.

## 3. Executed audit and exact remaining dichotomy

After the required A094004 calibration,
`check_contained_completion_shadow.py` exhausts every primitive binary
word beginning in `2` through length fourteen for Lemma 1 and recomputes
the two length-21 shadows in Lemma 2.  Every curling number is compared
between the two independent implementations; every displayed root set is
then enumerated directly from its defining block equalities.

The status split which remains is:

```
F terminal:
    H=2F bad / F terminal is a new essential prefix pair.

F bad:
    F=D3 bad / B=D2 terminal is a shorter common-prefix
    right-completion fork.
```

In the first branch, minimum endpoint rank gives only a strict rank
increase for the new essential pair.  In the second branch, `F` is not
a whole-power reset by Lemma 1.  Neither statement orders the two
branches, so a proof still needs a rank relating ordinary essential
prefix pairs to right-completion forks, or an origin argument excluding
the ascent in Lemma 2.

## 4. Exact rank/scale split by the status of `F`

Return to the selected ordinary endpoint pair

```
A=C^3 bad,                 D=A[1:] terminal,
rho=|A|+tau(D),
```

and its contained completion fork.  Since `cn(D)=2`,

```
B=D2,
tau(B)=tau(D)-1.                                (4)
```

Let `u=cn(H)` and choose a maximizing root of `H` of length `p<n`.
The powered suffix has length at most `3p<3n`, so it omits the leading
symbol in `H=2F`.  Therefore

```
cn(F)=cn(H)=u.                                  (5)
```

There are two status branches.

### Lemma 3 (terminal `F` forces external scale inflation)

If `F` is terminal, run

```
H=2F bad,                 F terminal
```

through their common outputs `G` up to their first unequal curling
numbers.  Then

```
H G=Y^k,
F G=(H G)[1:],
cn(H G)=k,
cn(F G)=k-1
```

for a primitive root `Y` of length `r` and an integer `k>=2`.  Moreover,

```
r>2n+gcd(n,r).                                  (6)
```

The new essential endpoint has the exact rank

```
|Y^k|+tau(Y^k[1:])
 =|H|+tau(F).                                   (7)
```

Under the minimum-`rho`, maximum-length selection of the ordinary
boundary, this rank is strictly greater than `rho`.

### Proof

Equation (5) gives at least one common output.  Since the two statuses
are opposite, a first unequal cut occurs before the `F` orbit reaches
one.  The one-symbol prefix theorem gives the displayed whole-power
reset.

The prefix `C^3` of `H G=Y^k` has periods `n` and `r`.  Suppose (6)
failed.  Its length `3n` would reach the Fine--Wilf threshold

```
n+r-gcd(n,r).
```

Fine--Wilf gives the gcd period to a factor containing complete roots of
both lengths.  Primitivity forces `n` to divide `r`.  If `r=dn` with
`d>1`, the primitive root `Y` begins in the proper power `C^d`, which is
impossible.  Thus `r=n`.  Period `n` would make the symbol immediately
after the prefix `C^3` equal to `C[0]=2`, whereas that symbol in `H` is
the wrong completion `3`.  This contradiction proves (6).

Every output in `G` spends one unit of `tau(F)`, so (7) follows by
cancelling `|G|`.  Global minimum rank excludes a smaller rank, while
equality would give the longer essential word `H G`, contradicting the
maximum-length tie break.  Hence the inequality in rank is strict.

### Lemma 4 (bad `F` gives a mixed-type endpoint descent)

If `F` is bad, then

```
F=D3 bad,                 B=D2 terminal
```

is a right-completion fork of the same length.  Its terminal endpoint is

```
|B|+tau(B)=rho-1,                                (8)
```

and its common-prefix version is

```
|D|+tau(B)=rho-2.                                (9)
```

### Proof

The statuses are the branch hypothesis and the three-word-fork
terminality of `B`.  Substituting `|B|=|A|` and (4) gives (8);
subtracting the final completion symbol gives (9).

Lemmas 3--4 expose the obstruction to a scalar proof.  The terminal-`F`
branch increases ordinary endpoint rank while more than doubling the
root scale.  The bad-`F` branch decreases the numerical endpoint but
changes from an ordinary deletion pair to a right-completion pair.
Closing the fork requires a well-founded rank on the union of these
object types (and on the reverse prefix pair which can leave a
right-completion chain); ordinary endpoint rank alone cannot compare
them.
