# Moving-boundary normal form at a bad driven deletion

This note is conditional on the existence of a bad word.  It sharpens the
context-loss branch of `tau_min_context_dynamics.md`; it does not eliminate
that branch.

## 1. Literature boundary

Chaffin--Linderman--Sloane--Wilks (CLSW), Section 4.3, define a binary
word `S` to be rotten when one of

```
tau(2 S)<tau(S),        tau(3 S)<tau(S)
```

holds, and doubly rotten when both inequalities hold.  Their Conjecture 22
states that no doubly rotten word exists.  Their search found none through
length 34.

That conjecture does not control the event here.  In the present event,

```
A=aD is bad,       D terminates,       E=D k is bad.
```

Thus prefixing `D` by `a` raises its hitting time from a finite value to
infinity, rather than lowering it, and `E` is a right extension rather than
a prefix extension.  Even Conjecture 22 would merely say that at least one
of the two binary prefixes of a *terminating* word does not have smaller
finite tail length.  It supplies no inequality for the displayed pair.

Direct searches for `"doubly rotten" curling`, `"rotten sequences"
curling number`, `"prefix decreases tail" curling number`, and `A216730`
found no later theorem beyond CLSW and the OEIS records that cite it.

Source:

* B. Chaffin, J. P. Linderman, N. J. A. Sloane, A. R. Wilks,
  *On Curling Numbers of Integer Sequences*, JIS 16 (2013), Article
  13.4.3, Section 4.3 and Conjecture 22.

## 2. Essential suffix after context loss

Call `W` essential if `W` is bad but `W[1:]` terminates.  Define

```
tau_0=min { tau(W[1:]) : W is essential }.
```

Choose an essential `A` attaining `tau_0`, and among all such choices
choose one of minimum length `N`.  The minimum-hitting-time lemma gives

```
A=Y^k,
cn(A)=k,
cn(A[1:])=k-1,
```

where `Y` is primitive and `k>=2`.  Put

```
D=A[1:],                 E=D k.
```

Assume the context-loss event: `E` is bad.  Among the suffixes of `E`
which are bad, choose one of minimum length and call it `C`.

### Lemma 1 (exact moving-boundary dichotomy)

The word `C` is essential, and exactly one of the following holds:

1. `tau(C[1:])>tau_0`;
2. `C=E`, `|C|=N`, and `tau(C[1:])=tau_0`.

#### Proof

The set of bad suffixes of `E` is nonempty because it contains `E`.
Minimality of `C` makes `C[1:]` terminating, so `C` is essential.
The definition of `tau_0` gives

```
tau(C[1:])>=tau_0.                                (1)
```

If equality holds in (1), the minimum-length tie-break used to select
`A` gives `|C|>=N`.  On the other hand `C` is a suffix of `E` and
`|E|=|D|+1=|A|=N`, so `|C|<=N`.  Hence `|C|=N`, and the only
length-`N` suffix of `E` is `E` itself.  This proves alternative 2.
If equality does not hold in (1), both values are integers and alternative
1 follows.  The alternatives are disjoint.

The point is directional: a genuine inward boundary move forces the
remaining terminating hitting time to rise strictly.  It does not produce
a well-founded descent.

## 3. The equal-rank plateau is a fixed-length power shift

Suppose alternative 2 of Lemma 1 holds.  Then `E` is another
minimum-`tau`, minimum-length essential word.  Applying the same
minimum-hitting-time lemma to `E` gives a primitive word `Z` and an
integer `ell>=2` such that

```
E=Z^ell,
cn(E)=ell,
cn(E[1:])=ell-1.                                  (2)
```

Write

```
r=|Y|,             s=|Z|.
```

### Lemma 2 (rotation or strict root descent)

Under (2), exactly one of the following holds:

1. `s=r`, `ell=k`, `Y[0]=k`, and

   ```
   Z=rot_left(Y),          E=rot_left(Y)^k;
   ```

2. `s<r` and

   ```
   (ell-1)s+gcd(r,s)<=r.                           (3)
   ```

#### Proof

The word `E` has the form

```
Y[1:] Y^(k-1) k.
```

Apply the same-scale-or-drop lemma from
`immediate_power_coupling.md`, Section 3, to the primitive maximizing
power `Z^ell` which occupies all of `E`.  If `s=r`, that lemma forces
the appended symbol `k` to equal `Y[0]` and identifies `Z` with the
left rotation of `Y`.  Comparing the two whole-word lengths,

```
kr=|A|=|E|=ell s,
```

then gives `ell=k`.  If `s!=r`, the lemma gives (3) and also gives
`s<r`.  These cases are exhaustive and disjoint.

### Corollary 3 (no infinite minimum-rank shift plateau)

Consider a chain of essential minimum pairs of the same length `N`,

```
W_i=Y_i^(k_i),
W_(i+1)=W_i[1:] k_i,
tau(W_i[1:])=tau_0,
```

where every `Y_i` is primitive.  Such a chain is finite.

#### Proof

Put `r_i=|Y_i|`, so `N=k_i r_i`.  Lemma 2 says that an edge either
strictly lowers `r_i`, or preserves both `r_i` and `k_i` and rotates
`Y_i` left by one position.  On every preserving edge, the first symbol
of `Y_i` is `k_i`.

For `m` consecutive preserving edges starting at `i`, the first `m`
successive cyclic symbols of `Y_i` are therefore all `k_i`.  There
cannot be `r_i` such edges: that would make every symbol of `Y_i`
equal to `k_i`.  The resulting whole word is unary, and the elementary
unary-orbit calculation in `immediate_power_coupling.md`, Section 5,
shows that it is not bad.  Hence each fixed-root-length regime contains
at most `r_i-1` preserving edges.

Strict-drop edges can occur only finitely often because

```
r_0>r_1>r_2>...>=1
```

along those edges.  Combining the finite number of strict drops with
the finite preserving run between consecutive drops proves the claim.
A crude bound is fewer than `N^2` edges.

Therefore repeated context loss cannot stay forever on the original
minimum hitting-time plateau.  If it continues after the finite
rotation/descent chain, the shortest new essential suffix has strictly
larger deleted hitting time.

## 4. Executed obstruction to the proposed endpoint rank

The tempting rank

```
R(W)=|W|-1+tau(W[1:])
```

is invariant during synchronized autonomous steps, but it need not
decrease across the local reset/shift equations.  After the required
A094004 calibration (`a(3)=5`, `a(8)=66`, `a(22)=142`), both independent
curling-number implementations were executed on

```
Y=2322232,       k=3,       A=Y^3,
D=A[1:],         E=D 3.
```

The program reported:

```
word       length       cn       tau
A            21         3         60
D            20         2          4
E            21         2         59
E[1:]        20         2         59
A 3          22         2         59
```

It also checked that `cn(E)=cn(A 3)` and that `A 3` is not a
nontrivial whole power.  Consequently

```
R(A)=24,             R(E)=79.                    (4)
```

This is a terminating surrogate, not a context-loss counterexample:
`E` reaches one.  It proves that neither (4)'s desired reverse inequality
nor a descent of `|A|+tau(D)` follows from the local word equations,
the shared next output, and the prohibition on consecutive whole-power
states.  Any successful rank must use the actual infinite status, not
only those local equations.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_moving_boundary_context_loss.py
```

## 5. Exact remaining gap

Lemmas 1--2 give the complete normal form at the first moving-boundary
event:

```
strict tau rise
    or
same-length whole-power shift
        -> rotation at one scale
        or strict primitive-root descent.
```

Corollary 3 eliminates an infinite same-rank plateau.  What remains is an
unbounded staircase in which each genuine inward boundary move raises the
new terminating deletion time, while the later normalization orbit may
increase the word length before the next context loss.  No published
rotten-sequence result bounds that staircase, and the executed example
shows that its jumps cannot be bounded by the local reset scale alone.

## 6. Every moved boundary returns to a reset

The strict-rise branch of Lemma 1 can also be normalized exactly.  Let

```
C=aB
```

be the shortest bad suffix selected there, put `t=tau(B)`, and run the
autonomous orbits of `C` and `B` in parallel.  Let `delta` be the least
time at which their curling numbers differ.

### Lemma 4 (promotion equations)

The time `delta` exists and satisfies

```
0<=delta<=t.
```

If `P` is the common output word of length `delta`, then there are a
primitive word `Z` and an integer `ell>=2` such that

```
C P=Z^ell,
B P=(C P)[1:],
cn(C P)=ell,
cn(B P)=ell-1,                                   (5)
tau(B P)=t-delta.                                (6)
```

In particular, if `tau_0` is the global minimum from Section 2, then

```
delta<=t-tau_0.                                  (7)
```

The endpoint quantity is transported exactly:

```
|C P|-1+tau(B P)=|C|-1+t.                        (8)
```

#### Proof

If the two outputs agreed for all times before the autonomous orbit of
`B` reached one, then at time `t` the bad orbit from `C` would also have
curling number one.  Hence a first disagreement exists no later than
time `t`.

Before that disagreement, deletion commutes with every common append,
so the two states are exactly `C P` and `B P=(C P)[1:]`.  The latter
is still on the terminating orbit from `B`, giving (6).  At the first
disagreement, suffix monotonicity and the one-symbol prefix bound make
the two values consecutive.  The strict-deletion whole-power lemma then
gives all assertions in (5), including primitivity of `Z`.

The word `C P` is essential.  Therefore global minimality of `tau_0`
gives `tau(B P)>=tau_0`.  Substitute (6) to obtain (7).
Equation (8) follows by substituting
`|C P|=|C|+delta` and (6).

Thus a moved boundary does return, in finite time, to the same
whole-power/all-terminal reset normal form.  The obstruction is that the
reset may return at a much larger physical scale.

## 7. Overlap geometry of a promotion

Retain the old reset

```
A=Y^k,       N=|A|,       r=|Y|,
```

and write the shortest new bad suffix as

```
C=E[j:],     E=A[1:] k,     j>=0.
```

Let the promoted reset from Lemma 4 be

```
C P=Z^ell,       s=|Z|,       |P|=delta.
```

The first

```
L=N-j-1
```

symbols of `C P` are the factor `A[j+1:]`.  Hence this overlap has
periods `r` and `s`.

### Lemma 5 (promotion scale separation)

If `r!=s`, then

```
N-j-1 < r+s-gcd(r,s).                            (9)
```

The promoted length and deleted hitting time obey

```
|C P|=N-j+delta,
tau((C P)[1:])=tau(C[1:])-delta.                 (10)
```

#### Proof

Equation (10) is Lemma 4 with `|C|=N-j`.

Suppose (9) failed.  Fine--Wilf applied to the length-`L` overlap would
give it period `gcd(r,s)`.  The Fine--Wilf threshold is at least
`max(r,s)`, so the overlap contains a complete conjugate of each of the
primitive roots `Y` and `Z`.  If the gcd is smaller than either root
length, that conjugate has a proper period, contradicting primitivity.
Since `r!=s`, the gcd is smaller than at least one root length, and the
same period on a complete conjugate of the other root handles the
divisibility case.  This contradiction proves (9).

Equation (9) permits external root growth; it does not force descent.

## 8. Executed countermodel to lexicographic root descent

The calibrated checker also executed the following complete finite
promotion:

```
Y=2322,        k=3,        A=Y^3,
D=A[1:],       E=D 3,
C=E[1:].
```

Its initial data were:

```
word             length       cn       tau
A                   12         3         53
D                   11         2          4
E                   12         2         54
C                   11         2         54
C[1:]               10         2         56
```

The orbits of `C` and `C[1:]` then produced the same 52 executed
outputs.  At the next cut the high state was

```
(222322232232223222323)^3
```

with executed curling number `3`, while its deletion had executed
curling number `2` and remaining hitting time `4`.  Thus the promotion
returns exactly to the old deleted rank

```
tau=4,
```

but the primitive reset-root length grows from `4` to `21`.  The
boundary had moved inward by one symbol, its new terminating time rose
from `4` to `56`, and 52 synchronized steps spent that excess before
the larger reset.

This is not a counterexample to the curling-number conjecture: both high
words terminate.  It is an exact countermodel to any proposed proof that
uses only

```
(tau, essential-suffix length, current reset-root length),
```

the promotion equations, and global-minimum inequality (7) to deduce
root descent after plateau rotations.  This example satisfies (7) with
equality and returns to the same minimum `tau`, yet its root grows by a
factor greater than five.  A valid descent theorem must exploit the
nontermination of the high states beyond the promoted reset, not just
the finite moving-boundary geometry.

## 9. Visible promotions are essential self-replayers

Use the notation of Lemma 4:

```
C=aB,          |C|=m,
C P=Z^ell,     |P|=delta,       |Z|=s.
```

### Lemma 6 (visible-root return to the reset tower)

If `s>=m`, then:

1. `Z` is an actual state on the bad autonomous orbit from `C`;
2. `Z[1:]` is the simultaneous state on the terminating autonomous
   orbit from `B`;
3. `Z` is bad, `Z[1:]` terminates, and

   ```
   tau(Z[1:])=tau(B)-(s-m);                       (11)
   ```

4. the deterministic orbit from `Z` reaches `Z^ell`.

Moreover,

```
delta>=(ell-1)m.                                  (12)
```

#### Proof

Because `s>=m`, the prefix `Z` of `C P` is

```
Z=C P[:s-m].
```

The first `s-m` symbols of `P` were common autonomous outputs of `C`
and `B`.  Therefore `Z` is the corresponding state on the bad orbit
from `C`, while deleting its first symbol gives

```
Z[1:]=B P[:s-m],
```

the corresponding state on the terminating orbit from `B`.  This proves
the first three assertions, including (11).

The later state `C P=Z^ell` lies on the same deterministic orbit, so
starting at the intermediate state `Z` produces exactly the intervening
symbols and reaches `Z^ell`.  This proves the self-replay assertion.

Finally,

```
m+delta=|C P|=ell s>=ell m,
```

which rearranges to (12).

Thus every promotion has the same hidden/visible split as the fixed-origin
reset forest:

* `s<m`: the new reset root is hidden inside the moved essential word;
* `s>=m`: an actual bad, terminating-deletion self-replayer is installed,
  and the route has literally returned to the visible all-terminal reset
  tower.

For a globally minimum deleted hitting time, (7) and (12) give the
additional necessary condition

```
tau(B)-tau_0 >= delta >= (ell-1)m.                (13)
```

on every visible promotion.  This is a real cost, but it is not bounded:
the terminating hitting-time injection at a context loss can be much
larger than the moved word length in calibrated finite examples.

### Lemma 7 (last-copy visibility)

The useful visibility threshold is in fact weaker than `s>=m`.  If

```
m<=(ell-1)s,                                     (14)
```

then `Z^(ell-1)` is an actual bad orbit state reached from `C`, its
first deletion is terminating, and

```
cn(Z^(ell-1))=ell-1,
Z[0]=ell-1.                                      (15)
```

Starting from that state, the orbit produces one full copy of `Z` and
reaches `Z^ell`.

If (14) fails, then the promotion appends less than one root length:

```
delta<s.                                         (16)
```

#### Proof

The final reset deletion is

```
(Z^ell)[1:]=Z[1:] Z^(ell-1)
```

and has curling number `ell-1` by (5).  Its suffix `Z^(ell-1)` displays
an `(ell-1)`-power.  Suffix monotonicity gives the matching upper bound,
so its curling number is exactly `ell-1`.

Under (14), the length-`(ell-1)s` prefix `Z^(ell-1)` occurs at or after
the starting cut `m` and before the first disagreement at the final cut
`ell s`.  It is therefore an actual state on the bad orbit from `C`;
its deletion is the corresponding still-terminating state on the orbit
from `B`.  The next generated symbol is the first symbol of the last
copy of `Z`, namely `Z[0]`.  The orbit rule and the exact value just
proved give `Z[0]=ell-1`.  The remaining generated symbols up to the
reset are exactly the rest of that displayed last copy of `Z`.

If (14) fails, then `m>(ell-1)s`.  Using
`m+delta=ell s` gives

```
delta=ell s-m<s,
```

which is (16).

Thus every strict-rise promotion is either:

* **replay-visible:** it installs the canonical last-copy state
  `Z^(ell-1)`, forces the pointed label `Z[0]=ell-1`, and generates a
  full root copy before the reset; or
* **terminal-hidden:** the moved word already reaches into the last
  root copy, and fewer than `s` symbols are appended before the reset.

The replay-visible branch is exactly the critical-root/self-replay object
studied in the all-terminal reset analysis.  Only the terminal-hidden
promotion remains specific to the moving-boundary branch.

### Corollary 8 (exact terminal-hidden carrier)

In the terminal-hidden case there is an integer `h` with

```
1<=h<=s
```

such that

```
C=Z^(ell-1) Z[:h],
P=Z[h:],
delta=s-h,                                        (17)
tau(C[1:])=tau((Z^ell)[1:])+s-h.                 (18)
```

If `h<s`, then for every `u` with `h<=u<s`, the actual high and
deleted states at that phase agree in curling number, and their common
output is `Z[u]`.

For `ell=2`, every promotion is terminal-hidden.  In the strict-rise
branch one has

```
tau_0=0,       h<s,
cn(Z)=1,
cn((Z^2)[1:])=1.                                 (19)
```

Consequently `Z` is primitive and robust in the CLSW sense, while
`C=Z Z[:h]` and its deletion synchronously generate the missing suffix
`Z[h:]` before the bad square reset.

#### Proof

Terminal-hidden means

```
(ell-1)s<m<=ell s.
```

Put `h=m-(ell-1)s`.  Since `C` is the length-`m` prefix of
`Z^ell`, its displayed form in (17) follows.  The equality
`C P=Z^ell` then gives the displayed form of `P` and
`delta=s-h`.  Equation (18) is (6).

When `h<s`, the cuts indexed by `u=h,...,s-1` occur strictly before
the first disagreement.  The next symbol in the displayed final root
copy is `Z[u]`, so both autonomous orbit rules have that common value.

If `ell=2`, replay visibility would put the actual bad orbit at the
state `Z^(ell-1)=Z`, whose curling number is one by (15).  This is
impossible, so the promotion is terminal-hidden.  Its final deleted
state has curling number one by (5), hence its remaining hitting time is
zero.  Global minimality forces `tau_0=0`.  In the strict-rise branch
`tau(C[1:])>tau_0`; equations (17)--(18) therefore force `h<s`.
The word `Z` is a suffix of `(Z^2)[1:]`, so suffix monotonicity and the
displayed square give both equalities in (19).  Exact curling number one
for the longest proper suffix of the primitive square is precisely CLSW
robustness.

## 10. Endpoint-rank selection

There is a stronger alternative to the minimum-`tau` selection.  For an
essential word define

```
R(W)=|W|+tau(W[1:]).
```

Choose `A` minimizing `R(A)`, and among all minimizers choose one of
maximum length `N`.  This maximum exists because `|W|<=R(W)`.

### Lemma 9 (minimum endpoint rank)

The selected pair diverges immediately, so `A=Y^k` is again a primitive
whole-power reset.  If its driven deletion `E=A[1:]k` is bad and

```
C=E[j:]
```

is its shortest bad suffix, then

```
tau(C[1:])>=tau(A[1:])+j.                        (20)
```

If `C` normalizes after `delta` common outputs to the reset `C P`, then

```
R(C P)=R(C)>=R(A).                               (21)
```

If equality holds in (21), then

```
delta<=j.                                        (22)
```

#### Proof

Suppose the first outputs of `A` and `A[1:]` agreed.  Their common
successor pair would still be essential, would have the same value of
`R`, and its high word would have length `N+1`.  This contradicts the
maximum-length tie-break.  Immediate divergence and the whole-power form
follow as before.

The word `C` is essential.  Minimality of `R(A)` gives

```
N-j+tau(C[1:])=R(C)>=R(A)=N+tau(A[1:]),
```

which is (20).  Equation (21) is the endpoint transport (8).  Under
equality, maximum length of `A` among the rank minimizers gives

```
|C P|=N-j+delta<=N,
```

which is (22).

Thus inward boundary depth has an exact price in terminating time.
At the minimum rank, normalization cannot spend more synchronized steps
than the number of additionally deleted symbols.

This still does not close the branch.  At equality the reset length
changes by

```
|C P|-N=delta-j<=0,
```

but a later rank-minimal excursion from a shorter reset can grow back up
to `N`.  Since the alphabet is finite, an infinite chain confined to
rank `R(A)` and lengths at most `N` would eventually repeat a reset word.
Ruling out such a restart cycle requires more than a numerical
lexicographic rank.

## 11. Unbounded-rank split

### Lemma 10 (finite alphabet and terminal-hidden compactness split)

Along any context-switch chain descended from one bad seed, every symbol
belongs to the finite alphabet of that seed.  If the essential endpoint
ranks are unbounded, then the essential word lengths are unbounded.

Let `M` be the largest positive symbol in the original alphabet.  Along
an unbounded terminal-hidden subsequence,

```
ell<=M,
s>=m/M,
```

so the promoted primitive-root lengths are unbounded as well.

After passing to a subsequence, exactly one of the following can be
assumed:

1. `delta=s-h` is unbounded, giving arbitrarily long paired exact
   profile arcs in (17);
2. `delta` is bounded.  Then one can fix an exponent `ell`, a defect
   length `d`, and a defect word `Q` such that

   ```
   C=Z^(ell-1) Z[:-d],
   Q=Z[-d:],
   P=Q,
   ```

   for primitive roots `Z` of unbounded length.

   Here `d=0` means `C=Z^ell` and `Q=P` is empty.

#### Proof

If a bad state appends a curling number not already present in the
state, that newly appended final symbol is unique.  Its next curling
number is one, contradicting badness.  Hence bad-orbit alphabets never
grow, and taking suffixes can only shrink them.

Over a fixed finite alphabet there are only finitely many words of
bounded length, and each terminating deletion has one fixed finite
hitting time.  Their endpoint ranks form a finite set.  Thus unbounded
ranks force unbounded lengths.

Every reset exponent is a positive appended value on a bad orbit, hence
is an element of the original alphabet and is at most `M`.  The
terminal-hidden inequalities

```
m<=ell s
```

give `s>=m/ell>=m/M`.

Finally, either the integer sequence `delta` is unbounded or it has a
bounded subsequence.  In the bounded case, finiteness of the alphabet
and the bounds on `ell` and `delta` permit a further subsequence with
constant `ell`, `d=delta`, and missing suffix word `Q`.  Substituting
`h=s-d` in (17) gives the displayed form.

The unbounded-profile branch feeds the critical-profile machinery, while
the bounded branch is a finite endpoint-defect type.  Compactness alone
does not finish either branch: witness root lengths in the long arcs may
escape, and the fixed endpoint defect can coexist with roots of
unbounded length.

## 12. Literature check and exact bounded-defect countermodels

CLSW define robustness in Section 3.1 and prove in Theorem 6 that a
primitive word `Z` of curling number one is robust exactly when no
proper suffix of `Z^2` has curling number two.  Their Theorems 9--15
classify several *non-robust* conjugate forms.  They do not classify
partial robust-square carriers

```
Z Z[:h]  ->  Z^2.
```

Searches for `"robust" "curling number" sequence primitive`,
`"robust sequences" "curling numbers"`, and `A218875` found no later
theorem about these partial states.

The calibrated executable found the full terminal-hidden profile

```
Z=232223,       h=2,       C=23222323.
```

Both `C` and `C[1:]` synchronously output the executed word `2223`;
they then reach `Z^2` and `(Z^2)[1:]`, of executed curling numbers two
and one.  The deleted carrier has hitting time four.  The high carrier
has hitting time 58.  This `C` is exactly the length-eight record start
listed in CLSW Table 2 and calibrated by A094004.

Therefore all terminal-hidden square equations, including the complete
phase profile and the exact low hitting-time budget, have a finite
binary model.  Only the demanded infinite future fails.

There is also an unbounded symbolic bounded-defect family.  For every
`a>=0`, put

```
Z_a=2^a 3 3 2,
C_a=Z_a Z_a[:-1].
```

Then

```
cn(Z_a)=1,
cn((Z_a^2)[1:])=1,
cn(C_a)=cn(C_a[1:])=2,
C_a 2=Z_a^2.                                     (23)
```

Here is a direct proof.  The factor `33` occurs only once in `Z_a`, so
`Z_a` is primitive.  A square suffix of `Z_a` must copy its final
`332` into the initial run of twos; root lengths one and two fail by
direct comparison, and every longer root gives that impossible copy.
The same argument in `(Z_a^2)[1:]` uses the two `33` markers, whose
distance is exactly `|Z_a|`: a proper square root would have to equal
that full distance, which cannot fit twice after the first-symbol
deletion.  Root lengths one and two fail there by the same final-symbol
comparisons; every root of length at least three contains the final
`33` marker and hence forces the full marker distance.

Both `C_a` and its deletion end in exactly two consecutive threes.
If either had a suffix exponent at least three, the endpoints of the
last three root copies would be a three-term arithmetic progression
among the at most four positions occupied by a `3`.  Their positive
differences from the last position are

```
1, a+3, a+4,
```

which contain no pair `d,2d`.  Hence their exact curling number is two.
Appending the final `2` completes `Z_a^2`; robustness rules out a
larger proper suffix exponent there.

The checker exhaustively recomputed both independent implementations for
`0<=a<=100`.  Thus a bounded missing suffix, even of length one, does
not bound the reset-root length and cannot be eliminated by local
robustness or marker counting alone.

## 13. Canonical same-rank restart transitions

Retain the minimum endpoint rank `R_0` of Section 10.  Consider a chain
which remains at rank `R_0` and in which every driven deletion is bad, so
the shortest-bad-suffix construction can be repeated.  At its `i`-th
reset write

```
W_i=Y_i^(k_i),              n_i=|W_i|,
E_i=W_i[1:] k_i,
C_i=E_i[j_i:],
W_(i+1)=C_i P_i,            delta_i=|P_i|.
```

Here `C_i` is the shortest bad suffix of `E_i`, and `P_i` is the common
output through the first disagreement of `C_i,C_i[1:]`.  Put

```
b_i=j_i+1,                  Q_i=k_i P_i.
```

The first symbol of `Q_i` is the reset output from `W_i`; the rest is
generated only after restarting from the shorter word `C_i`.

### Lemma 11 (exact sliding-window equation)

Every such edge obeys

```
W_(i+1)=W_i[b_i:] Q_i,                         (24)
n_(i+1)-n_i=|Q_i|-b_i=delta_i-j_i.             (25)
```

#### Proof

Since `E_i=W_i[1:] k_i`, deleting its first `j_i` symbols gives

```
C_i=W_i[j_i+1:] k_i=W_i[b_i:] k_i.
```

Appending `P_i` gives (24).  Taking lengths in (24), and using
`|Q_i|=delta_i+1` and `b_i=j_i+1`, gives (25).

The map is canonical on this branch.  A word has only one suffix of each
length, so its shortest bad suffix is unique; both autonomous orbits and
their first disagreement are deterministic.

## 14. A repeated reset creates a periodic splice tape

There are only finitely many rank-`R_0` essential words over the fixed
seed alphabet: each has length at most `R_0`.  Hence an infinite
same-rank restart chain repeats a reset word.  Restrict to one resulting
cycle

```
W_0 -> W_1 -> ... -> W_m=W_0.                  (26)
```

Let

```
B=sum_(i=0)^(m-1) b_i,
Q=Q_0 Q_1 ... Q_(m-1).
```

### Lemma 12 (restart-tape periodicity and overflow)

For the cycle (26),

```
|Q|=B.                                          (27)
```

The right-infinite splice tape

```
T=W_0 Q Q Q ...
```

has period `B`.  For every `q>=1`, the finite untruncated tape

```
T_q=W_0 Q^q
```

satisfies

```
cn(T_q)>=q.                                     (28)
```

If the cycle alphabet is finite and `M` is its greatest positive symbol,
then for every `q>M`,

```
tau(T_q)=1.                                     (29)
```

#### Proof

Sum (25) around the cycle.  The left side telescopes to
`n_m-n_0=0`, so

```
sum |Q_i|=sum b_i=B,
```

which is (27).

For `0<=i<=m`, put

```
B_i=sum_(h<i) b_h,        A_i=sum_(h<i) |Q_h|.
```

Repeated use of (24) gives the exact window identity

```
W_i=(W_0 Q_0 ... Q_(i-1))[B_i:n_0+A_i].        (30)
```

For `i=m`, equations (26)--(27) turn (30) into

```
T[0:n_0]=W_0=T[B:B+n_0].                        (31)
```

Thus `T[x]=T[x+B]` for `0<=x<n_0`.  If `x>=n_0`, both positions lie
in the tail `Q^omega`, which has period `|Q|=B`.  Therefore `T` has
period `B` at every nonnegative position.

Finally, `T_q` ends in the displayed suffix `Q^q`.  The definition of
curling number then gives (28).

For `q>M`, put `c=cn(T_q)`.  Equation (28) gives `c>M`, so `c` does
not occur in `T_q`.  After appending `c`, the final occurrence of `c`
is unique.  Any suffix power of exponent at least two would contain `c`
at the end of each of its last two root copies, which is impossible.
Thus `cn(T_q c)=1`.  Since `cn(T_q)>=q>1`, the first one occurs after
exactly one append, proving (29).

Thus a bounded restart cycle really does force suffix powers of
unbounded exponent in the accumulated, untruncated tape.  Indeed, after
enough cycles that tape terminates after one more append.  This fact does
not contradict the badness of the retained windows: the tape is assembled
from different autonomous orbits.  In an edge, only `k_i` is generated
from `W_i`; the word `P_i` is generated from `C_i`, after the prefix of
length `b_i` has been discarded.  Curling number can increase when that
discarded context is retained.

## 15. Executed exact obstruction to composing the splice

After the A094004 calibration, both independent curling-number
implementations were executed on

```
W=323232,             D=W[1:]=23232,
E=D 3=232323,         C=E[1:]=32323.
```

They returned

```
cn(W)=3,              cn(D)=2,
cn(E)=3,
cn(C)=2,              cn(C[1:])=2.
```

Both `C` and `C[1:]` therefore generate the common one-symbol word

```
P=2.
```

At its end,

```
C P=W,                C[1:] P=D,
cn(C P)=3,            cn(C[1:] P)=2.
```

The executed terminating times were

```
tau(D)=3,             tau(C[1:])=4,
```

so the depth cost is exact and both endpoint ranks equal nine:

```
|W|+tau(D)=|C|+tau(C[1:])=9.                    (32)
```

Consequently every finite equation in Lemmas 11--12 is realized by the
formal self-loop

```
323232 -> 323232:
delete 32, append Q=32.
```

Nevertheless, the undeleted ancestor after the first prescribed output
has

```
cn(3232323)=3,
```

whereas the restarted suffix `C=32323` has curling number two.  The
autonomous orbit of the ancestor therefore appends another `3`, not the
`2` prescribed by the splice.  The checker also recomputed

```
cn(323232 (32)^q)=3+q
```

for `0<=q<=100`; the formula for every `q>=0` also follows directly
as follows.  The displayed block of length two gives curling number at
least `3+q`.  A root of length at least two cannot occur more than
`3+q` times in a word of length `2(3+q)`, while a root of length one
cannot occur twice because the final two symbols are `3,2`.

All high words in this model terminate, so it is not a counterexample to
the conjecture and it does not realize the global badness hypothesis.
It proves the exact limitation of the periodic-tape argument: the reset
equations, first-disagreement values, endpoint-rank conservation, and
finite alphabet do not make the splice tape an orbit.  Excluding an
actual rank-`R_0` restart cycle requires a new use of nontermination which
transfers autonomous outputs across discarded left context.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_endpoint_restart_cycle.py
```

## 16. The net cycle is a conjugacy equation

Retain a restart cycle from Lemma 12, let `N=|W_0|`, and abbreviate
`W=W_0`.  The one-cycle tape has length `N+B` and has the same
length-`N` window `W` at offsets zero and `B`.  If `A` is its initial
length-`B` block, then

```
W Q=A W,                 |A|=|Q|=B.              (33)
```

### Lemma 13 (bounded block cure)

For every integer `s>=0`,

```
A^s W=W Q^s.                                    (34)
```

If `M` is the greatest positive symbol of the cycle alphabet, all words
in (34) with `s>M` are terminal with hitting time one.  Since `W` is
bad, there is an integer

```
s_*<=M
```

such that

```
A^(s_*) W          is bad,
A^(s_*+1) W        is terminal.                 (35)
```

Inside the single leftmost copy of `A` in the second word of (35), there
is an adjacent reverse-status boundary

```
a C       terminal,
C         bad.                                  (36)
```

#### Proof

Equation (34) follows from (33) by induction on `s`.  The base case
`s=0` is the identity `W=W`.  If it holds at `s`, then

```
A^(s+1)W=A(A^sW)=A(WQ^s)=(AW)Q^s=WQ^(s+1),
```

using (33) in its equivalent form `AW=WQ`.

The right side of (34) ends in `Q^s`, so its curling number is at least
`s`.  For `s>M`, its curling number is a positive symbol absent from the
word.  Appending that symbol makes its final occurrence unique, and the
next curling number is one.  Hence its hitting time is one.

The set of nonnegative `s` for which `A^sW` is bad is nonempty because
it contains zero, and it is contained in `{0,...,M}`.  Its largest
element is `s_*`, proving (35).  Starting with the terminal word
`A(A^(s_*)W)` and deleting the symbols of that displayed first copy of
`A` one at a time ends at the bad word `A^(s_*)W`.  A first status
change in this finite suffix chain gives (36).

This is the valid consequence of the one-step terminal splice.  It does
not imply that the terminal word in (36) has hitting time one: hitting
time is not monotone under deletion of a first symbol.

The standard conjugacy-equation theorem for words applies directly to
(33).  In the exact form used here, the solutions of `x z=z y` with
`|x|=|y|>0` have

```
x=U V,              y=V U,
z=U (V U)^n
```

for words `U,V`, with `V` nonempty, and an integer `n>=0`.  Applied to
`AW=WQ`, it gives

```
A=U V,              Q=V U,
W=U Q^n,             0<=|U|<B.                  (37)
```

This is Theorem 4 in J. Karhumäki, *Combinatorics on Words* lecture
notes, and is also the classical Lyndon--Schuetzenberger conjugacy
equation.

## 17. Commuting lock or a one-copy bordered escape

Write the reset and the primitive-root factorization of the cycle block
as

```
W=Y^k,       |Y|=r,       k>=2,
Q=R^e,       |R|=d,       e>=1,
```

where `Y,R` are primitive.  The reset also has

```
cn(W[1:])=k-1.                                   (38)
```

Put

```
h=|U|,       m=e n.
```

When `n>=1`, (37) says that `B=|Q|` is a period of `W`: the prefix and
suffix of `W` of length `N-B` are both `U Q^(n-1)`.  Also `W` ends in
`R^m`, so exactness of `cn(W)=k` gives

```
m<=k.                                             (39)
```

### Lemma 14 (cycle-period dichotomy)

Exactly one of the following holds.

1. `n=0`, in which case

   ```
   W=U,             N<B.
   ```

2. One has `n>=1` (and hence `B<=N`), and the cycle is
   **commuting-locked**:

   ```
   r divides B,
   A=Q=Y^(B/r).                                  (40)
   ```

3. One has `n=1` and

   ```
   W=U V U,
   0<h<r-gcd(r,B),
   Q=V U is primitive.                           (41)
   ```

   Thus the only noncommuting cycle with `B<=N` is an `AVA` word with
   primitive completion block.

#### Proof

If `n=0`, equation (37) gives `W=U`, and `h<B`, proving alternative 1.
Assume `n>=1`.  Then `W` has periods `r` and `B`.  Put

```
g=gcd(r,B).
```

If

```
N>=r+B-g,                                         (42)
```

Fine--Wilf makes `g` a period of `W`.  The primitive-root length `r` is
the least period of the whole power `Y^k`, so `g=r` and `r` divides
`B`.  Since `W` ends in the length-`B` block `Q`, this block is
`Y^(B/r)`.  Substitution in `AW=WQ` and right cancellation of `W`
give the same formula for `A`.  This is alternative 2.

Suppose (42) fails.  Then

```
B>(k-1)r+g.                                      (43)
```

If `n>=2`, equation (37) gives

```
B<=N/n<=k r/2<=(k-1)r,
```

contradicting (43).  Hence `n=1`.  Now `N=h+B`, so (43) is exactly

```
h<r-g.                                           (44)
```

The case `h=0` would give `B=N=kr`, hence `g=r`, contradicting (44).
Therefore `0<h<r`; since `W=UQ` and `Q` ends in `U`, the word `U` is
a nonempty proper border of both `W` and its primitive root `Y`.
Equation (37) becomes the `AVA` identity in (41).

It remains to bound `e`.  The suffix `Q=R^e` of `W` has periods `r`
and `d` and length `e d`.  By (39),

```
r=N/k<=N/e=d+h/e<2d.
```

If `e>=3`, then

```
e d>=3d>r+d-gcd(r,d).
```

Fine--Wilf would force the primitive terminal blocks `Y` and `R` to
have the same length and content.  Then `r` divides `B=e d`, putting
the cycle in alternative 2.  Hence a noncommuting cycle has
`e<=2`.

Suppose `e=2`.  If `k=2`, the positive border length `h` means that the
square `Q=R^2` is a suffix of `W[1:]`.  This gives

```
cn(W[1:])>=2,
```

contradicting (38), whose right side is one.

If `k>=3`, then

```
2d=B=kr-h>(k-1)r>=2r,
```

so `d>r`.  The word `Q=R^2`, as a suffix of `W`, has periods `d` and
`r` and length `2d`.  It meets the Fine--Wilf threshold because

```
2d>=r+d-gcd(r,d).
```

The resulting gcd period is proper for at least one of the primitive
terminal blocks `Y,R`, a contradiction.  Therefore `e=1`, completing
alternative 3.

The syntactic `AVA` conclusion alone does not import the existing
canonical-`AVA` theorems.  Line by line:

* the setup of `ava_fixed_inheritance.md` assumes its ambient `Q` is a
  primitive binary word with curling number one, whereas the present
  `W=Y^k` is a nonprimitive whole power with curling number `k>=2` over
  an arbitrary finite alphabet;
* that setup assumes its middle block is a nonempty proper suffix of its
  outer block and has smaller length, whereas (41) proves only that the
  present outer block `U` is a short proper border of `Y`;
* its load-bearing hypotheses are exact circular cube indicators, the
  exclusion of proper fourth powers, and first-copy fitting.  No one of
  those profile statements follows from (33)--(40);
* `canonical_terminal_two.md` additionally requires a terminal-`2`
  rotation with a curling-one deletion, neither of which is supplied
  here;
* the present completion block is primitive, but no curling-one or
  circular-profile statement about it follows.

Therefore (41) is a genuine reduction to a bordered reset, not a closure
by the prior `AVA` machinery.  Lemma 14 itself uses no bad/terminal
status or hitting-time inequality: after the cycle equation is obtained,
its only dynamical input is the exact reset statement
`W=Y^k`, `cn(W)=k`, `cn(W[1:])=k-1`.

The calibrated executable
`research/check_cycle_conjugacy_classification.py` exhaustively checked
Lemma 14 for every binary exact reset of length at most 18 and every
cycle period at most the reset length.  It found 1,386 locked cases and
326 bordered cases among 1,712 candidates, with no violation.  This
bounded audit checks the edge cases; it is not part of the proof.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_cycle_conjugacy_classification.py
```

## 18. Orbit provenance makes every cycle positive and pointed

Lemma 14 used only the net word equation after it was formed.  The
individual restart edges retain one further piece of dynamical
information.  In the notation of Section 13,

```
Q_i=k_i P_i,
```

where `k_i=cn(W_i)` is the first output at the reset and every symbol of
`P_i` is an output of the bad autonomous orbit from `C_i`.  Thus the
concatenated cycle block `Q=Q_0...Q_(m-1)` is not an arbitrary conjugacy
block.

### Lemma 15 (positive pointed cycle)

Every symbol of `Q`, and consequently every symbol of `W`, is an integer
at least two.  At the chosen initial reset

```
Q[0]=k.                                           (45)
```

The three cases of Lemma 14 therefore have the following more precise
forms.

1. In the over-window case `n=0`,

   ```
   W=U,             Q=V W,       V nonempty,
   V[0]=k.                                         (46)
   ```

2. In the commuting-locked case,

   ```
   Q=Y^(B/r),       Y[0]=k.                       (47)
   ```

3. In the bordered case, put `h=|U|` and write the two border
   factorizations of the primitive reset root as

   ```
   Y=U C=D U.
   ```

   Then

   ```
   0<h<r-gcd(r,B),
   Y[h]=C[0]=k,
   V=C Y^(k-2) D,
   A=Y^(k-1) D,
   Q=C Y^(k-1),                                  (48)
   ```

   and the last word in (48) is primitive.

#### Proof

Every reset exponent `k_i` is at least two.  Each word `C_i` is bad, so
no state on its autonomous orbit has curling number one.  The symbols of
`P_i` are curling numbers of those states and are therefore also at least
two.  This proves the assertion for `Q`.

In (37), if `n=0`, then `W=U` is a suffix of `Q=VU`.  If `n>=1`, every
symbol of `W=UQ^n` occurs in `Q`, because `Q=VU` itself contains `U`.
Hence every symbol of `W` is at least two in all three cases.

The first cycle block is `Q_0=k_0P_0`; at the chosen initial reset
`k_0=k`.  This proves (45).  In the `n=0` case, (37) gives `W=U`,
`Q=VU=VW`, and `V` is nonempty because `B>N`; (45) gives `V[0]=k`.
This proves (46).  In the locked case, (40) and (45) give (47).

It remains to expand the bordered case.  Here `W=UQ` and `0<h<r`.
Since `W=Y^k`, its length-`h` prefix and suffix are respectively the
length-`h` prefix and suffix of `Y`; both equal `U`.  There are therefore
nonempty words `C,D` with `Y=UC=DU`.  Deleting the first `h` symbols
from `W=Y^k` gives

```
Q=C Y^(k-1).
```

Since `Q=VU`, right cancellation of its final `U` and the equality
`Y=DU` give

```
V=C Y^(k-2)D.
```

The corresponding prefix block is

```
A=UV=U C Y^(k-2)D=Y^(k-1)D.
```

Finally, (45) applied to `Q=C Y^(k-1)` gives `C[0]=Y[h]=k`, and
Lemma 14 already proves that `Q` is primitive.

The pointing condition is substantial but is not by itself a
contradiction.  After the A094004 calibration, the executable checker
found 157 pointed bordered local models among the 326 binary bordered
models of reset length at most 18.  One exact local model reported by
both independent curling-number implementations is

```
W=323323,       A=32332,       Q=23323,
WQ=AW,          Q[0]=cn(W)=2,  cn(W[1:])=1.
```

It satisfies the complete algebraic and pointed reset conditions, but it
is not asserted to arise from an actual same-rank restart cycle.  Thus
the remaining exclusion must use more of the internal edge
factorizations than positivity and the first output alone.

## 19. Complete reduction of a one-edge restart cycle

Suppose the restart cycle has one edge, so `W_1=W_0=W`.  Retain

```
W=Y^k,       |Y|=r,       b=j+1,       Q=kP.
```

Length equality in Lemma 11 gives `|Q|=b`.  Also `b<=|W|`, because the
selected suffix `C=E[j:]` is nonempty.  Hence the over-window case of
Lemma 14 cannot occur.

### Lemma 16 (locked one-edge cycle)

If the one-edge cycle is commuting-locked, then

```
Q=Y,
C=Y^(k-1)Y[0],
P=Y[1:],
Y[0]=k,                                         (49)
```

and

```
Y[u]>=k-1             for every 1<=u<r.          (50)
```

#### Proof

Write `Q=Y^e`.  Lemma 15 gives `Y[0]=k`.  The carrier at the moved
boundary is

```
C=W[b:]k=Y^(k-e)Y[0],
|C|=(k-e)r+1.
```

If `e>=2`, then

```
|C|<=(k-1)r.
```

The promotion `C P=Y^k` is therefore replay-visible in the sense of
Lemma 7.  That lemma forces `Y[0]=k-1`, contradicting `Y[0]=k`.
Consequently `e=1`, and all identities in (49) follow.

For `1<=u<r`, immediately before the common orbit appends `Y[u]`, its
high state is

```
H_u=Y^(k-1)Y[:u].
```

Write `Y=A B` with `|A|=u`.  The exact identity

```
(A B)^(k-1) A=A (B A)^(k-1)
```

shows that `H_u` ends in a `(k-1)`-power.  The common output equation
gives `cn(H_u)=Y[u]`, proving (50).

### Lemma 17 (bordered one-edge cycle enters the critical profile)

If the one-edge cycle is bordered, let `h=|U|` and write

```
Y=U G=D U.
```

Then necessarily

```
k=3,
Y[0]=2,
Y[h]=3,
pc_Y(u)=Y[u]             for every phase u.       (51)
```

Here `pc_Y` is the proper circular curling profile defined in
`critical_seed_induction.md`.

#### Proof

In the bordered case `b=B=kr-h`.  Lemma 15 gives

```
Q=G Y^(k-1),       G[0]=Y[h]=k.
```

The moved carrier is therefore

```
C=W[b:]k=U k=Y[:h+1],
P=G[1:]Y^(k-1).                                 (52)
```

The inequality `h<r-gcd(r,B)=r-gcd(r,h)` implies `h+1<r`, so the
primitive reset root `Y` is an actual state reached on the bad orbit
from `C`; deleting its first symbol gives the simultaneous state on the
terminating orbit from `C[1:]`.  This also follows directly from (52):
the first `|G|-1` outputs complete `C` to `Y`.

The remaining common output in (52) is `Y^(k-1)`.  Therefore, for every
`1<=a<=k-1` and `0<=u<r`, the two synchronized states have exact
curling equations

```
cn(Y^a Y[:u])=Y[u],
cn(Y[1:]Y^(a-1)Y[:u])=Y[u].                     (53)
```

They first disagree at `Y^k` and its deletion, with exact values `k`
and `k-1`.  Equations (53) are precisely the hypotheses of Sections
1--3 of `critical_seed_induction.md`.  That derivation proves that
`Y[0]=k-1`, that `pc_Y=Y`, and that the minimum profile symbol is two.
Thus `k-1=2`, so `k=3`.  Lemma 15 supplies `Y[h]=k=3`, proving (51).

The reductions in Lemmas 16--17 are sharp at the level of all finite
local equations.  After the A094004 calibration, the executable
`research/check_one_edge_restart_cycles.py` verifies:

* the locked model `Y=32`, `k=3`, `Q=32`, whose reset has hitting time
  three;
* a bordered model built from the length-21 critical profile

  ```
  Y=232223222323222322232,       h=11,       k=3.
  ```

  Its reset has length 63, its cycle block has length 52, and its moved
  carrier has length 12.  Both independent curling-number
  implementations verify all 51 common outputs, the final `3/2`
  divergence, and the common endpoint rank 67.  The reset and carrier
  nevertheless terminate, with respective hitting times 11 and 62.

Thus even the complete one-edge local transition grammar has exact
finite models in both surviving cases.  An actual cycle can only be
excluded by using the demanded nontermination of its high states.  In
the bordered branch that remaining question has now been transferred,
without loss, to the already isolated primitive circular fixed-profile
problem plus the extra border marker in (51).

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_one_edge_restart_cycles.py
```

## 20. First divergence from the periodic splice

The splice tape can be compared with the genuine autonomous orbit up to
their first unequal output.  Let

```
q_0 q_1 q_2 ... =Q^omega.
```

Repeating the restart cycle gives a periodic sequence of moving high
windows `F_t` such that

```
F_0=W,
cn(F_t)=q_t,
F_t is a suffix of W q_0 ... q_(t-1).             (54)
```

Every `F_t` is essential and has endpoint rank `R_0`.  Since `W` was
chosen of maximum length among the rank-`R_0` essential words,

```
|F_t|<=N.                                         (55)
```

Let `d` be the primitive-root length of `Q`.  The whole tape
`T=WQ^omega` has least period `d`: Lemma 12 gives period `B`, the tail
has least period `d|B`, and shifting two positions forward by a large
multiple of `B` transfers the tail's period `d` back across `W`.

### Lemma 18 (crossing-root dichotomy)

There is a least time `L` at which the autonomous orbit from `W`
disagrees with `Q^omega`.  If

```
H=W q_0 ... q_(L-1),
c=cn(H),
q=q_L=cn(F_L),
```

then

```
c>q>=2.                                           (56)
```

For every primitive root `Z` of a maximizing `c`-power suffix of `H`,
put `p=|Z|`.  Then

```
p<=d,
c p>|F_L|.                                       (57)
```

Thus the first extra power is exactly one of:

1. an **outer crossing**, with `p=d`;
2. a **proper crossing**, with `p<d`.

If a primitive maximizing `q`-root in `F_L` has length `s` and `p!=s`,
then the co-terminal overlap also obeys

```
q s<p+s-gcd(p,s).                                (58)
```

#### Proof

As long as the two output streams agree, their untruncated state is the
displayed prefix of `T`, and (54) follows from the sliding-window
construction.  They cannot agree forever.  If `M` is the greatest
symbol of `Q`, then at time `(M+1)B` the untruncated word ends in
`Q^(M+1)`, so its curling number is at least `M+1`, while the prescribed
next symbol is `q_0<=M`.  Hence `L<=(M+1)B`.

At time `L`, suffix monotonicity in (54) gives `c>=q`; minimality of
`L` and disagreement give the strict inequality in (56).

The suffix `Z^c` is a factor of the `d`-periodic tape and therefore has
periods `p` and `d`.  If `p>d`, then

```
c p>=2p>=p+d-gcd(p,d).
```

Fine--Wilf would give the complete primitive root `Z` the proper period
`gcd(p,d)<p`, a contradiction.  Hence `p<=d`.  If `cp<=|F_L|`, the
entire `c`-power would be a suffix of `F_L`, contradicting
`cn(F_L)=q<c`.  This proves (57).

Finally, the displayed `q`-power of root length `s` in `F_L` is a
suffix of the crossing `c`-power and hence has periods `s` and `p`.  If
the reverse of (58) held, Fine--Wilf would give a proper gcd period to
one of the two complete primitive roots; the cases `p<s`, `s<p`, and
one length dividing the other are all covered because the threshold is
at least `max(p,s)`.  This proves (58).

### Corollary 19 (bordered cycles are underprofiles)

In the bordered case,

```
Q=W[h:]=G Y^(k-1)
```

is a suffix of `W[1:]` and ends in `Y^(k-1)`.  Therefore

```
cn(Q)=k-1.                                        (59)
```

Together with Lemmas 14--15, the complete endpoint data are

```
Q primitive,
Q[0]=k,
cn(Q)=k-1.                                       (60)
```

Thus phase zero is an exact first-copy fitting hole for its prescribed
value `k`: no circular `k`-power ending there fits even in the full
length-`B` word `Q`.  The reset root `Y` supplies a specific nonfitting
witness of span

```
k r=B+h,
```

whose left overhang is exactly the border length `h`.

Moreover its proper circular profile satisfies

```
pc_Q(u)>=Q[u]             for every phase u.      (61)
```

If the first divergence time in Lemma 18 satisfies

```
L>=2B-h,                                          (62)
```

then

```
pc_Q=Q
```

at every phase, and the first divergence must be an outer crossing with
root length `B`.

#### Proof

Since `h>=1`, the word `Q=W[h:]` is a suffix of `W[1:]`; suffix
monotonicity and (38) give `cn(Q)<=k-1`.  Its displayed terminal
`Y^(k-1)` gives the reverse inequality, proving (59).  Primitivity and
the first symbol in (60) are Lemmas 14--15.

Here `d=B` because `Q` is primitive.  At every occurrence of phase `u`,
a maximizing root in `F_t` has length at most

```
|F_t|/Q[u]<=N/2=(B+h)/2<B.
```

It is therefore a proper circular witness for
`pc_Q(u)>=Q[u]`, proving (61).

Any proper circular power of primitive-root length `p<B` has total
length strictly below

```
B+p-gcd(B,p)<2B.                                  (63)
```

Indeed, at or above the first threshold Fine--Wilf gives a proper gcd
period to its primitive root.  If `p` divides `B`, the threshold is
`B`; a length-`B` factor would instead make the primitive word `Q`
itself have period `p`, which is also impossible.

For every time `t>=B-h`, the untruncated common state has length

```
N+t=B+h+t>=2B.
```

Before divergence it therefore contains every proper circular power at
that phase by (63).  Its exact curling number `Q[t mod B]`, together
with (61), forces equality of the proper profile at that phase.
Under (62), the `B` pre-divergence times

```
B-h,...,2B-h-1
```

cover every phase, so `pc_Q=Q`.  A proper crossing at time `L` would
then give

```
pc_Q(L mod B)>=c>Q[L mod B],
```

a contradiction.  Lemma 18 leaves only the outer root `p=B`.

The dichotomy itself does not yet improve the endpoint rank.  The two
calibrated one-edge models from Section 19 realize both crossing types:

* for `W=323232`, `Q=32`, the first disagreement is at time one,
  where the untruncated value is three, the restarted value is two, and
  the crossing primitive root has length `2=|Q|`;
* in the bordered length-21-profile model, the first disagreement is at
  time nine, again with values three and two, but its unique maximizing
  root has length 10, strictly below `|Q|=52`; its cube has length 30
  and crosses the restarted window of length 20.

Both assertions are recomputed by
`research/check_one_edge_restart_cycles.py`.  The second model preserves
endpoint rank 67 throughout the restarted branch.  At the crossing, the
untruncated ancestor has endpoint expression 74, while the length-30
crossing cube has endpoint expression 34; executed code gives that cube
hitting time two.  Thus the tempting smaller-rank crossing word is
terminal in the exact model.  A proper crossing alone cannot turn it
into a rank-minimal **bad** essential word.  The remaining load-bearing
fact is again that every genuine high state is bad, whereas all
displayed local models terminate.

### Corollary 20 (late bordered divergence is exactly `3>2`)

Under the late-divergence hypothesis (62), put

```
u=t mod B,
a(t)=floor((N+t)/B).
```

For every `t>=B-h`, the formal untruncated splice prefix satisfies

```
cn(W (Q^omega)[:t])=max(Q[u],a(t)).              (64)
```

The first divergence therefore has the exact form

```
2B-h<=L<3B-h,
c=3,
q_L=Q[L mod B]=2.                               (65)
```

If

```
R=Q[u:]Q[:u],       u=L mod B,
s=L-(2B-h),
```

then `R` is a primitive rotation of `Q`, `R[0]=2`,
`pc_R=R`, `0<=s<B`, and the actual pre-append state has the exact form

```
H=D R^3,           |D|=s,       cn(H)=3,         (66)
```

while the restarted splice prescribes the symbol two.  The true orbit
therefore leaves the periodic tape by

```
D R^3  ->  D R^3 3.                              (67)
```

#### Proof

Corollary 19 gives `pc_Q=Q`.  For a suffix power of the word in (64),
Lemma 18's Fine--Wilf argument leaves only a primitive root shorter than
`B` or the root length `B`.  Once the word has length at least `2B`,
all shorter-root powers are visible and their greatest exponent is
`pc_Q(u)=Q[u]`.  The length-`B` rotation repeats exactly `a(t)` times
at the suffix.  Both witnesses are present, proving (64).

A primitive proper circular fixed profile has minimum symbol two by the
Saari periodicity argument in `critical_seed_induction.md`, Section 3.
At `t=2B-h`, the outer count first becomes three.  It cannot exceed any
profile symbol before then, since all symbols are at least two.  During
the next `B` phases a symbol two occurs, and (64) then gives the first
strict comparison `3>2`.  The outer count does not become four until
`t=3B-h`, proving (65).

At phase `u`, the length-`B` word immediately preceding the cut is the
rotation `R=Q[u:]Q[:u]`.  Equation (65) makes the last `3B` symbols
exactly `R^3`; the unmatched earlier prefix has length

```
N+L-3B=L-(2B-h)=s.
```

Rotation preserves primitivity and the proper circular profile, and
`R[0]=Q[u]=2`.  These observations prove (66)--(67).

Thus every sufficiently delayed bordered restart cycle feeds directly
into the already isolated, but still unresolved, contexted critical-cube
promotion.  The only bordered alternative outside that machinery is an
early proper-profile crossing before time `2B-h`.

## 21. Locked cycles diverge within one primitive root

In the commuting-locked case write

```
Q=Y^e,       |Y|=r,       W=Y^k,       Y[0]=k.
```

Let `pc_Y(u)` be the proper circular profile of the primitive word `Y`.

### Lemma 21 (exact locked prefix formula)

For every `t>=0`, put

```
u=t mod r,
a(t)=k+floor(t/r).
```

The formal periodic prefix has exact curling number

```
cn(W (Y^omega)[:t])=max(pc_Y(u),a(t)).           (68)
```

Consequently the first true-orbit/splice divergence satisfies

```
L<=r.                                             (69)
```

More explicitly, `L` is the least `t` in `{0,...,r}` for which

```
max(pc_Y(t mod r),a(t))>Y[t mod r].               (70)
```

If no phase has `pc_Y(u)>Y[u]`, then the divergence is purely outer:

* if `u` is the first index in `{1,...,r-1}` with `Y[u]<k`, then

  ```
  L=u,       c=k>Y[u];
  ```

* if no such index exists, then

  ```
  L=r,       c=k+1>Y[0]=k.                       (71)
  ```

In the second subcase, genuine badness forces the symbol `k+1` to occur
in `Y`.

#### Proof

The word in (68) is a prefix of the `r`-periodic tape and has length
`kr+t>=2r`.  The Fine--Wilf argument of Lemma 18 says that a primitive
maximizing root has length at most `r`.  Every proper-root power has
length below `2r`, so all of them are visible and their maximum exponent
is `pc_Y(u)`.  The length-`r` rotation occurs exactly `a(t)` times at
the suffix.  These are exhaustive root lengths and both witnesses are
present, proving (68).

At `t=0`, equation (68) equals `cn(W)=k=Y[0]`.  At `t=r`, its outer
term is `k+1>Y[0]`.  Thus the first disagreement occurs no later than
`r`, and (68), together with the suffix lower bound from the restarted
window, proves (69)--(70).

If `pc_Y<=Y` phasewise, then for `t<r` the only possible strict excess
in (68) is the outer value `k>Y[t]`.  If no such phase occurs, the first
excess is the value `k+1` at `t=r`, proving (71).

Finally, a bad orbit cannot append a symbol absent from its current
alphabet: that symbol would be unique at the end and force curling
number one next.  The locked tape and `W` use exactly the alphabet of
`Y`, so the last assertion follows.

Thus a locked restart cycle never hides its first context amplification
deep in the splice.  Within one primitive-root traversal it either
exposes a strict proper-profile overlabel or promotes the number of
outer root copies.  The finite model `Y=32`, `k=3` realizes the first
outer subcase at phase one; its termination shows that the exact
post-promotion badness, not the prefix formula, remains the unresolved
condition.

## 22. The over-window case has the same two exits

Assume `n=0`, so

```
N<B,
W=U,
A=W V,
Q=V W.
```

Let `R` be the primitive root of `Q` and put `d=|R|`.

### Lemma 22 (over-window period split)

Exactly one of the following scale regimes holds.

1. If `d<=N/2`, then

   ```
   d=r,
   Q=Y^(B/r),
   B/r>k,
   Y[0]=k.                                       (72)
   ```

   Thus this is a commuting over-window cycle, and the exact prefix
   formula and `L<=r` conclusion of Lemma 21 apply.

2. If `d>N/2`, then

   ```
   pc_R(u)>=R[u]          for every phase u.      (73)
   ```

   If the first true/splice divergence occurs before

   ```
   3d-N,
   ```

   it is necessarily a proper crossing with root length below `d`.
   Otherwise

   ```
   pc_R=R,
   3d-N<=L<4d-N,
   c=3>q_L=2,                                    (74)
   ```

   and, for a rotation `S` of `R` beginning in two, the true orbit
   leaves the splice in the contexted-cube form

   ```
   D S^3  ->  D S^3 3,       |D|<d.              (75)
   ```

#### Proof

The word `W=Y^k` is the length-`N` suffix of the `d`-periodic word `Q`,
so it has periods `r` and `d`.  Suppose `d<=N/2`.  Then

```
N=kr>=r+d-gcd(r,d),
```

and Fine--Wilf makes `gcd(r,d)` a period of `W`.  Since `r` is its least
period, `r` divides `d`.  The last length-`d` block of both `Q` and `W`
is therefore

```
R=Y^(d/r).
```

Primitivity of `R` forces `d=r`.  Hence `Q=Y^(B/r)`.  Since `B>N=kr`,
its exponent is greater than `k`; Lemma 15 gives `Y[0]=Q[0]=k`.
This proves (72).  Although this word equation is commuting, it belongs
to the `n=0` alternative because its cycle block is longer than `W`.

Now suppose `d>N/2`.  A maximizing root in any restarted window `F_t`
has length at most

```
|F_t|/q_t<=N/2<d.
```

It is therefore a proper circular witness.  Since the output word
`Q=R^(B/d)` runs through every phase of `R`, this proves (73).

Before time `3d-N`, the formal untruncated prefix has length below
`3d`, so a root of length `d` occurs at most twice.  It cannot witness
the strict inequality `c>q_L>=2`.  Lemma 18 therefore makes every such
early divergence a proper crossing.

Assume instead `L>=3d-N`.  During the `d` pre-divergence times

```
2d-N,...,3d-N-1,
```

the common untruncated word has length at least `2d`.  Every proper
circular power has length below `2d`, by the same Fine--Wilf argument
as (63).  Exact agreement and (73) therefore give `pc_R=R` at every
phase.  From that point onward the exact prefix formula is

```
cn(W(Q^omega)[:t])
  =max(R[t mod d], floor((N+t)/d)).
```

The outer count first reaches three at `t=3d-N`.  A primitive fixed
profile has minimum symbol two, so within the next `d` phases the first
outer excess is exactly `3>2`, proving (74).  The rotation and context
calculation in Corollary 20, with `d` in place of `B`, gives (75).

Thus the over-window branch introduces no third asymptotic mechanism.
It either collapses to the locked prefix formula, exposes an early
proper-profile defect, or reaches the same contexted critical-cube
promotion as a late bordered cycle.

The calibrated checker now also records the commuting over-window word
equation

```
W=323232,       Q=A=32323232,       |Q|>|W|.
```

This is a finite algebraic model, not a restart transition.  It is
included to audit the necessary `n>=1` qualifier in alternative 2 of
Lemma 14: without that qualifier the over-window and commuting
alternatives would not be disjoint.

The bounded phase audit
`research/check_periodic_prefix_formula.py` independently recomputes both
sides of the periodic-prefix formulas for all 1,966 primitive binary
periods of length at most 10, covering 37,534 general prefixes and
112,602 locked-form prefixes.  It found no phase or maximality mismatch.
This is a convention audit, not part of the unbounded proofs.

Reproduction:

```
python -m unittest tests.test_curling.CurlingNumberTests.test_a094004_total_length_calibration
python research/check_cycle_conjugacy_classification.py
python research/check_periodic_prefix_formula.py
```

## 23. A `2`-exit either lies inside an edge or forces zero deleted time

At the exact `3>2` exits in Corollary 20 and Lemma 22, the restarted
value two is either the initial output of a reset block `Q_i` or a
symbol inside its common word `P_i`.

### Lemma 23 (reset-phase `2` collapse)

If that phase is a reset-block start, then

```
R_0=N=|F_L|,
tau(W[1:])=tau(F_L[1:])=0,
cn(W)=cn(F_L)=2.                                  (76)
```

If it is not a reset-block start, then

```
cn(F_L)=cn(F_L[1:])=2.                            (77)
```

#### Proof

At a reset-block start, `F_L` is a whole-power reset and its deletion
has exact curling number one less.  Since `cn(F_L)=2`, its deletion has
curling number one and hence hitting time zero.  Endpoint rank gives

```
R_0=|F_L|.
```

Every rank-`R_0` essential word has length at most the selected maximum
`N`, while `N<=R_0` from the definition of endpoint rank.  Therefore

```
R_0=|F_L|<=N<=R_0.
```

All quantities are equal.  Thus the selected reset deletion also has
hitting time zero, and its exact value `k-1` is one, proving (76).

At every noninitial position of a block `Q_i=k_iP_i`, the symbol is a
common output produced before the first disagreement of the high word
and its deletion.  Both exact curling numbers are therefore that
symbol, which is two at the exit.  This proves (77).

Thus a late contexted cube promotion that occurs at a reset marker
already lies in the global zero-deleted-time square branch.  Every other
late cube promotion retains a synchronized curling-two deletion at the
crossing window.  This is a status refinement only; neither alternative
has yet been shown impossible.

## 24. A late bordered cycle has reset exponent at most three

Retain the bordered notation of Corollaries 19--20:

```
Y=U C,        |Y|=r,        |U|=h,
W=Y^k,        Q=C Y^(k-1),  |Q|=B=kr-h.
```

In the late branch, Corollary 19 proves the exact proper circular
profile

```
pc_Q=Q.
```

### Lemma 24 (bordered exponent bound)

Under these hypotheses,

```
k is either 2 or 3.                               (78)
```

#### Proof

At the distinguished phase zero, the length-`kr` circular suffix is
the reset power `Y^k`; its span is `B+h`.  Fix an integer

```
1<=a<=r.
```

The length-`(k-1)r` suffix ending at circular cut `-a` is contained in
that displayed `Y^k`, because

```
(k-1)r+a<=kr.
```

It has period `r` and length exactly `(k-1)r`, so it is a
`(k-1)`-power of its length-`r` terminal block.  The root is proper for
`Q`, since

```
r<B=kr-h
```

follows from `k>=2` and `0<h<r`.  Exactness of `pc_Q=Q` therefore gives

```
Q[-a mod B]>=k-1             for 1<=a<=r.         (79)
```

The `r` phases in (79) are precisely the symbols in the final copy of
`Y` in `Q=C Y^(k-1)`.  Hence every symbol of `Y` is at least `k-1`.
The prefix `C` is a suffix of `Y`, and `Q` contains a complete copy of
`Y`, so `Q` and `Y` have the same set of symbols.  Thus

```
min(Q)>=k-1.                                      (80)
```

The Saari periodicity argument cited and proved applicable in
`critical_seed_induction.md`, Section 3, says that every primitive
proper circular fixed profile has minimum symbol two.  Applying it to
the primitive word `Q` gives `min(Q)=2`.  Equation (80) yields
`k-1<=2`, while a reset has `k>=2`.  Therefore `k` belongs to
`{2,3}`, proving (78).

This removes every reset exponent at least four from the late bordered
branch.  It does not distinguish the residual nonfitting-square case
`k=2` from the nonfitting-cube case `k=3`.

### Corollary 25 (CLSW normal form in the square case)

If the residual exponent in Lemma 24 is `k=2`, then there is a nonempty
word `E` such that

```
C=E U,
Y=U E U,
Q=E U U E U,
cn(C)=1,
2h<r.                                             (81)
```

#### Proof

Corollary 19 gives `cn(Q)=1`.  The word `C` is a suffix of `Q`, so
suffix monotonicity gives `cn(C)<=cn(Q)=1`; hence `cn(C)=1`.

Both `U` and `C` are suffixes of `Q`: the former because
`Q=C Y` and `Y=D U`, and the latter because

```
Q=C Y=C U C.
```

If `|U|>=|C|`, suffix comparability would make `C` a suffix of `U`.
Then `Y=U C`, and hence `Q`, would end in `C^2`, contradicting
`cn(Q)=1`.  Therefore `|C|>|U|`.  Suffix comparability now makes `U`
a proper suffix of `C`, so write `C=E U` with `E` nonempty.
Substitution gives the two displayed word forms.  Finally,

```
r=|U|+|C|>2|U|=2h.
```

This is the constructive content of Chaffin--Linderman--Sloane--Wilks,
Theorem 9, applied to the non-robust curling-one word `Q`: the proper
suffix `U` completes `Q` to the square

```
U Q=(U C)^2.
```

Their proof is word-theoretic and the argument above shows explicitly
that it applies without a binary-alphabet restriction.

### Lemma 26 (the forced seam cube in the `k=3` case)

If the residual exponent in Lemma 24 is `k=3`, put

```
R=C U,         |R|=r.
```

Then

```
Q=R^2 C,       B=3r-h,       Q[2r]=C[0]=3.       (82)
```

Every primitive root length `s` of a circular cube ending at cut `2r`
satisfies exactly one of

```
s<r:
    r>2s+gcd(r,s);                                (83)

s>r:
    s>r+gcd(r,s),
    2s+gcd(B,s)<B.                                (84)
```

In particular `s=r` is impossible.  The cube in (83) is wholly
contained in the displayed `R^2`; the cube in (84) crosses its left
boundary.

#### Proof

Equation (82) follows by substituting `Y=U C` in
`Q=C Y^2`.  Since `2r<B`, exactness of `pc_Q=Q` at cut `2r` supplies
a proper circular cube there.  A maximizing cube root is primitive:
if it were a nontrivial power, its third power would have exponent at
least six at a cut whose exact profile value is three.

Let `s` be the length of such a primitive root and put

```
g=gcd(r,s),       g_B=gcd(B,s).
```

The general proper-power Fine--Wilf bound in the primitive
length-`B` word `Q` gives

```
3s<B+s-g_B,
```

or equivalently the second inequality in (84).

Suppose first that `s<r`.  If `3s>2r`, the complete interval
`[0,2r)=R^2` lies inside the `s`-periodic cube.  It then has periods
`r` and `s`, and its length meets the Fine--Wilf threshold

```
2r>=r+s-g.
```

This would give the primitive word `R` the proper period `g`, a
contradiction.  Hence `3s<=2r`, so the cube is contained in `R^2`.
If the reverse of (83) held, its length would meet the threshold

```
3s>=r+s-g.
```

Fine--Wilf would again give a complete length-`r` conjugate of `R`
the proper period `g`.  This proves (83).

Suppose next that `s>r`.  The proper-power bound gives

```
s<B/2<3r/2<2r.
```

The interval `R^2` lies inside the `s`-cube and has both periods `r`
and `s`.  If `s<=r+g`, its length `2r` would meet the Fine--Wilf
threshold `r+s-g`, again contradicting primitivity of `R`.  This
proves the first inequality in (84).

Finally suppose `s=r`.  The three length-`r` blocks immediately before
cut `2r` would be

```
Y, R, R,
```

because the length-`r` suffix of `Q` is `Y` and its prefix of length
`2r` is `R^2`.  A cube would force `Y=R`, hence `U C=C U`.
The commutation theorem would make the nonempty words `U,C` powers of
one common word, making `Y=U C` imprimitive.  This contradiction
excludes equality and completes the dichotomy.

At the actual pre-divergence orbit time `t=2r`, the corresponding bad
state is

```
H_(2r)=Y^3 R^2,
cn(H_(2r))=3.
```

Thus (83)--(84) are not merely circular-profile witnesses: one of
these two separated cube scales occurs in a genuine bad orbit state.
Neither scale alternative alone transfers badness to the cube suffix.

## 27. The contained seam cube does not inherit a residual restart

The strict decrease in (83) is not by itself a closed recursion.  The
calibrated executable `research/search_k3_seam_prefix_models.py`
exhausts binary primitive bordered roots in increasing length and finds
the first finite orbit-prefix model at

```
r=4,       h=1,
Y=2322,    U=2,       C=322,
Q=32223222322,
W=Y^3=232223222322.
```

Both independent curling-number implementations verify

```
cn(W)=3,             cn(W[1:])=2,
```

and verify that the actual orbit from `W` outputs all nine symbols

```
Q[0:2r+1]=322232223
```

through the forced seam.  The seam state is

```
Y^3 (C U)^2=23222322232232223222.
```

Its exact curling number is three, and its only maximizing root has
length one.  Thus it realizes the contained alternative (83) with the
child root word `2`.

That child is not a smaller residual object:

```
pc_(2)=(1),
```

and its cube has tail length one.  The executed tail lengths of the
reset, its deletion, and the seam state are respectively

```
53, 4, 45.
```

Thus all three states terminate; no bad status descends to the
root-one cube.

The model deliberately stops one equation short of the full late
branch.  Its circular profile is

```
(3,2,2,2,3,2,2,2,3,2,3),
```

which agrees with `Q` at ten of eleven phases and fails only at the
last phase: `Q[10]=2` but a root-`4` circular cube ends there.  Hence
the full fixed-profile hypothesis excludes this finite model.  What the
model refutes is the local inference

```
contained seam cube + genuine orbit prefix
    => smaller fixed-profile or bad restart.
```

Any valid recursion must use the distant phase-ten negative equation
or the infinite badness hypothesis; the seam equations and actual
orbit provenance through the seam do not suffice.

The same executable found no crossing-root orbit-prefix model with
`s>r` among all binary primitive bordered roots of length at most
sixteen.  This is bounded evidence only, not an exclusion of (84).
