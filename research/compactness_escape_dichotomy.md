# Compactness dichotomy and the escaping-root obstruction

This note audits the late-shift/minimal-subshift route under the
hypothesis of a counterorbit.  It proves the compactness statement that
the route actually supplies and gives two countermodels to the proposed
periodicity conclusion.  It does not construct a counterorbit.

## 1. Cut notation

For a two-sided word `x` and a cut immediately before `x_t`, write

`Pow(x,t,e,p)`

when `x[t-e p:t]` consists of `e` consecutive copies of one word of
length `p`.  Define

`rho(x,t)=min {p>=1 : Pow(x,t,x_t,p)}`

and put `rho(x,t)=infinity` if the displayed set is empty.  The exponent
in this definition must be the label `x_t`.  A merely square suffix does
not prove the lower half of an exact profile at a cut labelled `3` or
higher.

Suppose that a counterorbit exists, and concatenate its seed and all its
appended labels into a one-sided word `w`.  At every sufficiently late
cut `t`,

`w_t = cn(w[0:t]) >= 2`.                                    (1)

By Lemma 1 of `research/reductions.md`, all appended labels belong to a
finite set.  Let `A` be that set and let `K=max A`.

The late orbit closure `Omega` consists of the two-sided limits of
centered words `w[t_j+.]` along sequences `t_j -> infinity`.  Equivalently,
`x` belongs to `Omega` when there are such cuts for which, for every
fixed radius `L`, the interval `w[t_j-L:t_j+L]` eventually equals
`x[-L:L]`.  A diagonal subsequence proves that `Omega` is nonempty and
compact; shifting the realizing cuts by any fixed integer proves that it
is shift invariant.

## 2. The upper half is closed

### Lemma 1

For every `x in Omega`, every `p>=1`, and every integer `e>x_0`,

`not Pow(x,0,e,p)`.                                         (2)

### Proof

Fix `x`, `p`, and `e`.  Choose realizing cuts `t_j` whose centered words
converge to `x`.  For all sufficiently large `j`, the center symbol is
`w_(t_j)=x_0`, and the full interval of length `e p` to its left agrees
with `x[-e p:0]`.  If the latter interval were an `e`-th power, then the
prefix `w[0:t_j]` would have a suffix of exponent `e>x_0`.  Its curling
number would then be at least `e`, contradicting (1).  This proves (2).

The same proof after shifting `x` gives (2) at every cut.

## 3. Exact compactness dichotomy

Let `X` be any minimal nonempty subshift contained in `Omega`.  Every
point of `X` is uniformly recurrent: for a cylinder determined by a
factor of a point, minimality says that its shift preimages cover `X`;
a finite subcover bounds the gap between successive occurrences of that
factor.

For `R>=1`, set

`E_R={x in X : rho(x,0)<=R}`.

Each `E_R` is clopen.  Indeed, it is the finite union, over `a in A` and
`1<=p<=R`, of the cylinders specifying `x_0=a` and
`Pow(x,0,a,p)`.  The sets `E_R` are increasing.

### Theorem 2 (compactness dichotomy)

Exactly one of the following alternatives holds.

1. There is an `R` such that, for every `x in X` and every cut `t`,
   `rho(x,t)<=R`.  Together with Lemma 1, this makes every `x in X` a
   bi-infinite exact self-profile: the greatest suffix exponent at cut
   `t` is exactly `x_t`.
2. There is a uniformly recurrent `x in X` with `rho(x,0)=infinity`.
   For every sequence of radii `L_j -> infinity`, realizing orbit cuts
   can be selected so that they agree with `x` on radius `L_j`, and
   their least maximizing-root lengths `p_j` satisfy

   `p_j > L_j/K`.                                           (3)

### Proof

If every point of `X` belongs to some `E_R`, the increasing family
`(E_R)` is an open cover of compact `X`.  A finite subcover has a largest
index `R`, so `X=E_R`.  Shift invariance gives the same bound at every
cut.  The witnessed `x_t`-power supplies the lower bound, while Lemma 1
forbids every larger exponent.  This proves alternative 1.

If the cover fails, choose `x` outside every `E_R`.  Then
`rho(x,0)=infinity`, and minimality makes `x` uniformly recurrent.
Choose a realizing orbit cut agreeing with `x` on radius `L_j`; its
center label is `a=x_0<=K`.  Let `p_j` be the least length of a
maximizing root at that orbit state.  If `p_j<=L_j/K`, its complete
`a`-power suffix has length

`a p_j <= K p_j <= L_j`.

It therefore lies inside the matched left window and transfers to an
`a`-power at cut zero of `x`.  This contradicts
`rho(x,0)=infinity`, proving (3).  The alternatives are mutually
exclusive by their definitions.

This theorem is the full conclusion available from compactness alone.
In particular, "bounded square witnesses" must be replaced by "bounded
label-matched witnesses" in alternative 1.

## 4. Minimality does not make the escape branch periodic

Let

`tau(0)=012`, `tau(1)=02`, `tau(2)=1`,

and let `v=tau^omega(0)`.  Currie, Harju, Ochem, and Rampersad,
*Some further results on squarefree arithmetic progressions in infinite
words*, Theoretical Computer Science 799 (2019), 140--148,
DOI `10.1016/j.tcs.2019.10.006`, Lemma 2, states precisely that this
word `v` is squarefree (and additionally avoids `010` and `212`).

The substitution is primitive: `tau^3(a)` contains every one of
`0,1,2` for each letter `a`.  A direct uniform-recurrence proof is as
follows.  Every factor `F` of `v` occurs in some `tau^n(0)`.
Primitivity supplies `q` for which every `tau^q(a)` contains `0`;
hence every `tau^(n+q)(a)` contains `F`.  Decompose `v` into consecutive
blocks `tau^(n+q)(v_i)`.  Twice the maximum block length bounds the gap
between occurrences of `F`.

Take the two-sided subshift generated by `v` and recode its letters by

`0 -> 2`, `1 -> 3`, `2 -> 4`.                              (4)

Every resulting two-sided point is uniformly recurrent and squarefree.
It is aperiodic, because a periodic two-sided word contains the square
of a period block.  At every cut it satisfies all upper constraints
(2): any exponent at least two is already forbidden.  It nevertheless
has no lower witness at any cut, including its syndetically recurrent
cuts labelled `2`.

Thus uniform recurrence, minimality, the full family of closed upper
exactness constraints, and recurrent occurrences of label `2` do not
force periodicity or preserve a lower square witness.

## 5. Exact roots can escape through a single locally consistent transition

The loss above is realized by explicit finite exact transitions.  Fix a
two-sided recoded Hall--Thue point `x` with `x_0=2`.  For `L>=1`, put

`U_L=x[-L:0]`, `R_L=5 U_L`, and `S_L=R_L^2`.                (5)

The marker `5` does not occur in `U_L`.

### Lemma 3

The repeated-suffix maximum of `S_L` is `2`, and `R_L` is its unique
maximizing root.  Its length is `L+1`.

### Proof

The displayed factorization in (5) supplies exponent two.

Consider a suffix `Y^e` with `e>=3`.  If `Y` contains `5`, then `Y^e`
contains at least three markers, while `S_L` has exactly two.  If `Y`
does not contain `5`, the suffix lies after the final marker and is a
factor of `U_L`; its first two copies form a square, contradicting the
squarefreeness of `U_L`.  Hence no exponent at least three is possible.

Now consider a square suffix with root length `p`.  If its root contains
`5`, its two copies contain both markers of `S_L`.  Therefore the square
is all of `S_L`, so `p=|R_L|`.  If its root contains no `5`, the square
lies in `U_L`, again a contradiction.  A root longer than `R_L` cannot
fit twice in `S_L`.  These cases exhaust whether the root contains the
marker and whether `p` is smaller than, equal to, or larger than
`|R_L|`.

Appending the next symbol `x_0=2` to `S_L` is therefore locally
consistent with the orbit rule.  Moreover,

`S_L[-L:]=U_L`.

Consequently, the centered finite word `S_L x[0:L]`, cut between its two
displayed factors, agrees with `x[-L:L]`, while its unique maximizing
root has length `L+1`.  The roots leave every fixed observation window
and the squarefree limit retains no trace of them.

The executable checker `research/check_compactness_escape.py` enumerates
every root length independently with both curling-number implementations.
After the A094004 calibration test passed at starting lengths `3`, `8`,
and `22`, it checked (5) at radii `8,13,21,34,55`; the reported unique
maximizing-root lengths were respectively `9,14,22,35,56`.

These approximants satisfy one exact orbit transition, not the
neighboring transitions.  That distinction is the remaining source of
possible leverage in a genuine counterorbit.

## 6. Even an anchored unbounded tower is not periodicity

The stronger fallback conclusion "escape creates an anchored tower of
large powers" would still not imply periodicity.  The construction in
`research/recurrent_tower.md` uses

`mu(0)=01`, `mu(1)=0`, `h=mu^3`,

`A=h(0)=01001`, `B=h(1)=010`, and `Q_0=B`.  If
`h(Q_n)=A R_n`, define `Q_(n+1)=R_n A`.  The proofs there establish:

- `Q_n^3` is a prefix of `Q_(n+1)` for every `n`;
- every `Q_n` is primitive;
- the nested limit belongs to the Fibonacci minimal subshift and is
  uniformly recurrent and aperiodic.

Hence a fixed cut can carry an unbounded tower of primitive cubes in a
uniformly recurrent aperiodic word.

## 7. Exact remaining gap

The compactness route can only be completed by using compatibility
between many neighboring orbit transitions,

`w_t=cn(w[0:t])`,

not by minimality or return words alone.  A return transfers a power
certificate only when the entire repeated suffix lies in the returned
finite window.  In alternative 2, inequality (3) is exactly the failure
of that condition.  The Hall--Thue construction shows that this failure
can coexist with every closed upper constraint and with recurrent label
`2`; the Fibonacci construction shows that extracting an anchored cube
tower would not itself finish the argument.

A new lemma would therefore have to relate the escaping maximizing roots
at different actual orbit cuts--for example by a proved nesting,
transport, or copy-parent constraint forced by all intervening exact
labels.  No such conclusion follows from compactness, minimality, or
ordinary return-word theory.
