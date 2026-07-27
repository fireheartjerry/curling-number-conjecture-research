# Dynamics after the minimum-hitting-time pure-power reset

This note continues `research/minimal_deleted_hitting_time.md`.  It
classifies every later step of the bad high orbit relative to deletion
of its fixed first symbol.  The conclusion is an exact dichotomy:
either the deleted state itself becomes bad, or the high orbit contains
an infinite nested tower of whole-word powers with nondecreasing,
eventually unbounded primitive-root lengths.  The dichotomy does not by
itself eliminate either branch.

## 1. Driven deletion

Let

```
H_0=a B_0
```

be selected so that

* the orbit of `H_0` never reaches curling number one;
* the orbit of `B_0` reaches one;
* `tau(B_0)=tau_0` is minimum among all pairs with those two
  properties.

Write the bad high orbit as

```
H_(t+1)=H_t f_t,          f_t=cn(H_t),
H_t=a B_t.
```

Deletion commutes with the actual high append, so

```
B_(t+1)=B_t f_t.
```

Also put

```
g_t=cn(B_t).
```

The proof of CLSW Theorem 7 is alphabet-independent and gives

```
f_t in {g_t,g_t+1}.                              (1)
```

Indeed every suffix power of `B_t` is a suffix power of `aB_t`, while
an exponent at least `g_t+2` in `aB_t` would leave at least
`g_t+1` complete root copies inside `B_t`.

## 2. Equality steps and reset steps

Suppose `B_t` reaches one.

If

```
f_t=g_t,
```

then the driven update is also the autonomous update of `B_t`.
Consequently

```
tau(B_(t+1))=tau(B_t)-1.                         (2)
```

If

```
f_t=g_t+1,
```

the strict-deletion case in the proof of CLSW Theorem 8 gives a
primitive word `Y_t` such that

```
H_t=Y_t^(f_t).                                   (3)
```

For completeness, (3) follows from the same one-integer span argument
used in `research/minimal_deleted_hitting_time.md`: a maximizing
`f_t`-power which did not occupy all of `H_t` would lie wholly in
`B_t` and force `g_t>=f_t`.

Call (3) a **reset**.  It is a whole-state power at the fixed left
origin, not merely a periodic suffix.

Minimality of `tau_0` says that every terminating `B_t` satisfies

```
tau(B_t)>=tau_0.                                  (4)
```

Therefore, if every `B_t` terminates, resets occur infinitely often.
Otherwise, after the last reset, equations (2) and (4) would make the
nonnegative integer `tau(B_t)` decrease below `tau_0`.

This proves the exhaustive alternative:

1. some `B_t` is bad, so deletion of the fixed leading symbol has
   become inessential; or
2. all `B_t` terminate and the bad high orbit has infinitely many
   reset states of the form (3).

## 3. Nested reset roots cannot decrease

Take two reset times `s<t` and write

```
H_s=U^k,      |U|=p,
H_t=V^ell,    |V|=q,
```

where `U,V` are primitive and `k,ell>=2`.  Since both are states on one
orbit, `H_s` is a proper prefix of `H_t`.

The case `q<p` is impossible.  The complete word `H_s` has periods `p`
and `q`, and

```
|H_s|=k p>=2p>=p+q-gcd(p,q).
```

Fine--Wilf would give period `gcd(p,q)<p` to the first length-`p` block
`U`, contradicting its primitivity.

If `q=p`, the first length-`p` blocks of the two words agree, so

```
U=V.
```

The later word is longer and both lengths are multiples of `p`, hence

```
ell>k.                                             (5)
```

Finally suppose `q>p` and put `d=gcd(p,q)`.  If

```
k p>=p+q-d,
```

Fine--Wilf gives period `d` to `H_s`.  When `d<p`, this makes `U`
imprimitive.  When `d=p`, the displayed inequality implies
`|H_s|>=q`, so the first complete length-`q` root `V` lies in this
`p`-periodic prefix; because `p` properly divides `q`, this makes `V`
imprimitive.  Both alternatives are impossible.  Threshold failure is

```
q>(k-1)p+d.                                       (6)
```

Thus reset-root lengths never decrease.  An unequal transition obeys
the strict Fine--Wilf scale gap (6), while an equal-root transition
strictly raises the exponent.

## 3a. Hidden versus visible unequal reset roots

Retain two reset times from Section 3,

```
H_s=U^k,      |U|=p,
H_t=V^ell,    |V|=q,
```

with `s<t`, `q>p`, and `U,V` primitive.  Put

```
g=gcd(p,q).
```

Equation (6) gives

```
q>(k-1)p+g.                                      (6a)
```

There are two exhaustive cases.

### Visible case

Suppose `q>=kp`.  Equality is impossible: the first `q=kp` symbols of
`H_t` would give

```
V=U^k,
```

contradicting the primitivity of `V`.  Hence

```
q>kp.                                            (6b)
```

The first `q` symbols of `H_t` are `V`.  Since the earlier state `U^k`
has length `kp<q`, the orbit has already passed through the length-`q`
state

```
T[0:q]=V.
```

Thus `V` is itself an actual state of the bad high orbit.  In the
infinite-reset branch, where every driven deletion `B_j` terminates,
the word `V[1:]` is the corresponding terminating deletion state.
Moreover the deterministic orbit from `V` reaches the displayed later
state `V^ell`.  Thus a visible later reset root is itself a bad,
terminating-deletion, autonomous self-replayer.

### Hidden case

Suppose `q<kp`.  By (6a), there is an integer `h` such that

```
q=(k-1)p+h,       g<h<p.                         (6c)
```

The first `q` symbols of `H_t` agree with the earlier prefix `U^k`, so

```
V=U^(k-1) U[:h].                                 (6d)
```

Also `2q>kp`: after substituting (6c), this is

```
(k-2)p+2h>0.
```

Consequently the whole earlier state `U^k` is visible in the prefix
`V^2` of `H_t`.  Comparing the interval from `q` through `kp` in the
two descriptions gives

```
U[h:p]=U[0:p-h].                                 (6e)
```

Hence `h` is a period of `U`.  Since

```
gcd(p,q)=gcd(p,h)=g<h,
```

this period does not divide `p`; this is exactly the Fine--Wilf
difference-period escape.

The symbol at position `kp` of the global orbit is the value appended
after the reset state `U^k`, namely `k`.  In the second copy of `V` this
position has offset

```
kp-q=p-h.
```

Equations (6c)--(6d) therefore give the pointed constraint

```
U[p-h]=k.                                        (6f)
```

At the reset time `s`, strict deletion says

```
cn((U^k)[1:])=k-1.                               (6g)
```

An `h`-periodic word of length `p` ends in
`floor(p/h)` equal consecutive blocks of length `h`: partition its
terminal `floor(p/h)h` symbols into length-`h` blocks and apply (6e)
between adjacent blocks.  This power is a suffix of `(U^k)[1:]`.
Equation (6g) therefore implies

```
floor(p/h)<=k-1,
```

and hence

```
h>p/k.                                           (6h)
```

For `k=2`, put

```
A=U[:p-h],       B=U[p-h:h].
```

Here `p-h<h`, and (6e) gives the exact forms

```
U=A B A,
V=U U[:h]=(A B) A (A B).                         (6i)
```

The middle word `B` is nonempty because `h>p/2`, and (6f) says

```
B[0]=2.
```

Thus every hidden square-reset transition is an AVA lift: the old root
has outer block `A`, while the new root exchanges roles and has outer
block `AB`.

## 4. A bad-deletion transition can occur only just after a reset

Suppose `B_t` terminates and `B_(t+1)` is bad.  Equation (2) shows that
the step cannot be an equality step: an actual successor state on a
terminating orbit still reaches the same future one.  Hence it is a
reset,

```
H_t=Y^k,          k=f_t=g_t+1,
B_(t+1)=B_t k.                                    (7)
```

There is a further exact restriction.  The high and newly bad deleted
states must have the same next curling number:

```
cn(H_(t+1))=cn(B_(t+1)).                          (8)
```

To prove this, suppose the values differed.  The strict-deletion
whole-power argument would make `H_(t+1)` a nontrivial whole power.
But `H_t` is already the whole power in (7), and

```
H_(t+1)=H_t k
```

is its one-symbol extension.  The following elementary lemma shows that
two such consecutive whole powers force the bad high orbit to reach
one.

### Consecutive whole-power lemma

Suppose

```
W=U^c,            W z=V^d,
```

where `c,d>=2` and `U,V` are primitive.  Put

```
N=|W|,            p=|U|,       q=|V|.
```

The common length-`N` prefix has periods `p` and `q`.  It meets the
Fine--Wilf threshold.  To verify this without omitting the parity case:

* if `N` is even, then `N+1=dq` is odd, so `d>=3`;
  consequently `p<=N/2` and `q<=(N+1)/3`;
* if `N` is odd, then `N=cp` is odd, so `c>=3`;
  consequently `p<=N/3` and `q<=(N+1)/2`.

In either case

```
N>=p+q-gcd(p,q).
```

Fine--Wilf gives the gcd period.  Primitivity of both roots forces

```
p=q=gcd(p,q).
```

Since `p` divides both `N` and `N+1`, one has `p=1`.  Thus `W` is a
unary word, say `W=x^N`; its exact curling number is `N`.  In an orbit,
the appended symbol `z` is therefore `N`.  For `Wz` to remain unary one
must have `x=N`, so

```
Wz=N^(N+1).
```

Its next curling number is `N+1`; appending that new, unequal final
symbol produces a state of curling number one.  Hence a bad orbit cannot
contain two consecutive whole-power states.  This proves (8).

Therefore a transition in which deletion itself becomes bad is not an
arbitrary loss of control.  It is the one-symbol replacement

```
a B_t  ->  B_t k
```

at a reset, followed by at least one step on which the leading context
`a` is dynamically irrelevant.

## 5. Equal-root returns have a finite budget

No value appended by a bad orbit can be absent from its initial state.
If an appended value `c` occurred for the first time at the new final
position, that final symbol would be unique.  The resulting state would
have curling number one, contradicting badness.

Let `M` be the greatest positive integer occurring in `H_0`.  Every
later curling number, including every reset exponent, is at most `M`.
Equation (5) consequently permits at most `M-1` reset occurrences with
one fixed root length.  In the infinite-reset branch the primitive-root
lengths are therefore unbounded.

For a binary `{2,3}` orbit, one root length can occur at most twice:
the only possible strictly increasing reset exponents are `2,3`.
Any further return would make the whole state at least a fourth power,
whose curling number is at least four.  Appending that new value would
leave it unique and force curling number one at the next state.

## 6. Exact remaining gap

The reset tower is strongly constrained but not yet contradictory.
Unequal root lengths may grow forever according to (6), and nested
primitive square prefixes can realize the `k=2` difference-period
escape indefinitely at the level of ordinary word equations.

The other branch is also genuine as a logical possibility: a driven
deleted state `B_t` may become bad even though `B_0` terminates.  In
that event the fixed leading context `a` is no longer responsible for
nontermination, but `B_t[1:]` need not terminate, so the
minimum-`tau` argument cannot simply be restarted without first locating
a new essential left boundary.

Any completion of this route must therefore prove one of:

* driven deletion stays terminating and the global self-label equations
  prohibit the unbounded reset tower; or
* every transition where `B_t` becomes bad yields a new essential
  boundary with a strictly smaller well-founded parameter.

Ordinary Fine--Wilf growth alone proves neither statement.

## Source

Chaffin, Linderman, Sloane and Wilks, *On Curling Numbers of Integer
Sequences*, Journal of Integer Sequences 16 (2013), Article 13.4.3,
Theorems 7--8:
<https://cs.uwaterloo.ca/journals/JIS/VOL16/Sloane/CNC.pdf>.
