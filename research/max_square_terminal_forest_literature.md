# Literature audit for the maximal-square forest route

Search date: 2026-07-23.

The searches below were performed before extending the local
longest-square lemma to the fitting ancestry graph.  They were not
searches for a complete solution of the Curling Number Conjecture.

## Queries

The exact search strings were:

```
arXiv 0912.2382 Curling Number Conjecture definition weakly curling number theorem
arXiv 1212.6102 On Curling Numbers of Integer Sequences theorem weak curling number
Fine Wilf theorem periodicity words sharp threshold gcd periods primary source
runs maximal repetitions overlap cubes squares combinatorics on words theorem Crochemore Ilie Tinta
site:arxiv.org combinatorics words three squares lemma Crochemore Rytter statement
site:arxiv.org runs overlap lemma periods p q maximal repetitions cubes squares
site:hal.science critical factorization theorem local period word statement
site:arxiv.org Fine Wilf graph threshold minus one periods p p-1 central words
site:arxiv.org "overlapping runs" period lemma sum periods primitive word
site:arxiv.org "two runs" overlap periods Fine Wilf lemma
site:arxiv.org "cubic runs" overlap combinatorics words
site:arxiv.org "maximal repetitions" "overlap" periods
```

The direct primary-source pages and PDFs were then opened.

## Sources and exact reusable statements

### Chaffin--Sloane (2009)

Benjamin Chaffin and N. J. A. Sloane,
[*The Curling Number Conjecture*](https://arxiv.org/abs/0912.2382),
arXiv:0912.2382.

Section 1 defines the curling number as the maximum `k` in a suffix
factorization `S=XY^k`, and the orbit by appending that value.  The paper
reports computations for binary starts.  It supplies no theorem about
overlaps of a globally longest square with the last cube in its root,
no distinguished-origin fitting condition, and no terminal-prefix
transport result.

Scope for this route: problem definition and binary calibration only.

### Chaffin--Linderman--Sloane--Wilks (2012)

Benjamin Chaffin, John P. Linderman, N. J. A. Sloane, and Allan R.
Wilks, [*On Curling Numbers of Integer
Sequences*](https://arxiv.org/abs/1212.6102), arXiv:1212.6102.

Lemma 4 states:

> If `S` has curling number `k`, then among the representations
> `S=XY^k`, the shortest `Y` is primitive and unique; when `k>1`, that
> `Y` has curling number below `k`.

Theorem 5 states the suffix form of Fine--Wilf:

> If powers `X^i` and `Y^j` have a common suffix of length at least
> `|X|+|Y|-gcd(|X|,|Y|)`, then `X` and `Y` are powers of one word of
> length `gcd(|X|,|Y|)`.

Theorem 6 states:

> For primitive `S` of curling number `k`, if `S` is non-robust because
> `S^(k+1)` has a proper `(k+1)`-power suffix, then that suffix already
> occurs in `S^2`.

Scope for this route:

* Lemma 4 supports choosing a primitive shortest maximizing root, but
  the local proof in `max_square_terminal_forest.md` proves primitivity
  directly for every square root at an exact `2`-cut.
* Theorem 5 is exactly the overlap threshold used in the contained and
  crossing branches.
* Theorem 6 concerns proper high-power suffixes of `S^(k+1)`.  A fitting
  ancestry wrap cycle changes endpoints and root lengths, so it does
  not give a same-phase terminal-prefix witness and does not close the
  route.

### Fine--Wilf graphs

Stuart A. Rankin,
[*Fine-Wilf Graphs and the Generalized Fine-Wilf
Theorem*](https://arxiv.org/abs/0906.1780), arXiv:0906.1780.

The paper restates the sharp two-period theorem:

> A word with periods `r,s` and length at least
> `r+s-gcd(r,s)` has period `gcd(r,s)`.

It also records the sharpness classification:

> At length `r+s-gcd(r,s)-1`, the non-gcd-periodic extremal equality
> pattern is unique up to relabelling and has exactly two equality
> classes/symbols.

Scope for this route: the first statement is load-bearing.  The second
confirms that the crossing case `d=3,q=p-1` really is the unique
threshold-minus-one geometry; the note nevertheless proves its two
components explicitly and kills it with endpoint labels `3` and `2`.
The generalized multi-period theorem controls equality components, not
which component receives an orbit label, so it does not orient a wrap
cycle by itself.

### Three Squares Lemma and its overlapping variant

Hideo Bannai, Takuya Mieno, and Yuto Nakashima,
[*Lyndon Words, the Three Squares Lemma, and Primitive
Squares*](https://arxiv.org/abs/2006.13576), arXiv:2006.13576.

Lemma 1 (the Three Squares Lemma) states:

> If `u^2,v^2,w^2` are three prefixes of one string, `w` is primitive,
> and `|u|>|v|>|w|`, then `|u|>=|v|+|w|`.

Corollary 2 gives an overlapping/nested version:

> For three successively nested squares satisfying specified
> L-root-interval start conditions, if the smallest root is primitive,
> the same inequality `|u|>=|v|+|w|` holds.

Scope for this route: these results bound the number of successively
nested primitive squares, but the fitting ancestry graph has two edge
types.  A descending edge is nested; an ascending edge crosses the
parent square's left boundary.  A modulo-period wrap cycle necessarily
contains the latter type, so the hypotheses of the Three Squares Lemma
do not persist around the cycle.  The theorem can bound a contained
subchain but cannot eliminate recurrence or prove terminal-prefix
transport.

### Runs theorem

Hideo Bannai, Tomohiro I, Shunsuke Inenaga, Yuto Nakashima, Masayuki
Takeda, and Kazuya Tsuruta,
[*The "Runs" Theorem*](https://arxiv.org/abs/1406.0263),
arXiv:1406.0263.

The paper defines a run as a maximal periodic interval of length at
least twice its least period and proves:

> A word of length `n` contains fewer than `n` runs.

It also proves that the sum of exponents of all runs is below `3n`.

Scope for this route: the finite critical slab therefore contains only
linearly many maximal periodic intervals.  This is a cardinality bound,
not a well-founded rank.  Periodicity of the ambient circular word lets
one ancestry path revisit translated occurrences of the same run
indefinitely, so neither bound excludes a wrap cycle.

## Net disposition

The literature supplies the sharp overlap engine and finite counting
bounds.  It does not supply the missing directed statement:

```
full first-copy fitting
    + exact binary profile
    + a distinguished terminal strict drop
  => no fitting square-ancestry wrap cycle.
```

The strict half-scale child and the lifted forest/wrap identity in
`max_square_terminal_forest.md` are therefore novel deductions beyond
the cited statements.  The remaining terminal-prefix step cannot be
replaced by a generic runs count, the Three Squares Lemma, or
Fine--Wilf alone.

## Addendum: canonical terminal-2 overlap

Additional exact queries:

* `"border" "conjugate" "period" lemma word square`;
* `"periodic conjugate" border word theorem`;
* `combinatorics words if a conjugate has period p border square suffix lemma`;
* `word A V A V suffix A circular square longest square lemma`.

No located source states the candidate lemma in
`research/canonical_terminal_two.md`: if `Q=AVA`, `V` is a proper suffix
of `A`, and `cn(Q)=1`, then the crossing root `VA` is globally longest.
The bounded equality-graph evidence for that statement must therefore not
be cited as a published theorem.

One standard result located and used in the proved first-mismatch analysis
is the period-difference lemma.  J. Simpson, *On Palindromic
Periodicities*, Australasian Journal of Combinatorics 92 (2025), Lemma 1.3,
states:

> Let `w` be a word having two periods `p` and `q` with `p>q`.  Then the
> suffix and prefix of length `|w|-q` both have period `p-q`.

The paper attributes this to Lemma 2.1 of an earlier source and Lemma
8.1.1 of Lothaire.  Its scope is exactly the common length-`2a` suffix
with periods `r>a` and `a` in the canonical first-mismatch calculation.
It does not eliminate the resulting period `r-a`; the low-cut exponent
bound and the first-copy fitting inequality are both additionally needed.
