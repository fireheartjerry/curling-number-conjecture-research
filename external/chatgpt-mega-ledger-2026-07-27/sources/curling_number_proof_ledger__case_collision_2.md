# Curling Number Conjecture — Proof Ledger

**Project:** Jerry Li / ChatGPT collaborative attack  
**Last updated:** 2026-07-24  
**Purpose:** Preserve every substantive reduction, proved lemma, computational check, falsified sublemma, and remaining gap. This ledger is deliberately conservative: claims are separated into proved, externally dependent, checked, conjectural, or refuted.

## 0. Definitions and conventions

For a finite nonempty word/sequence `S`, the curling number `cn(S)` is the largest integer `k >= 1` for which `S = X Y^k` with `Y` nonempty and `X` possibly empty. The deterministic orbit appends `cn(S)` at each step.

When a suffix power attaining `cn(S)=K` is chosen with shortest root length `P`, call `P` the **shortest witness period**. A time is a **strict record time** when this shortest witness period exceeds every earlier shortest witness period. We write a strict record witness as

`S = X Y^K`, `|Y| = P`, with `Y` primitive.

In the binary hard core, the orbit symbols are in `{2,3}` and no `1` or `4` has yet appeared.

## 1. Basic reductions

### 1.1 New-symbol reset
If `cn(S)=k` and the symbol `k` has not appeared earlier in `S`, then `cn(Sk)=1`.

**Reason:** any suffix repetition ending at the newly appended `k` would require another occurrence of `k` at the corresponding earlier position.

**Status:** PROVED.

### 1.2 Finite recycled alphabet in a counterexample
In a counterexample, every appended value must already occur in the finite seed. Thus appended values are bounded.

**Status:** PROVED from 1.1.

### 1.3 A counterexample tail is not eventually periodic
An eventually periodic infinite tail would yield arbitrarily high curling numbers at period-aligned endpoints, contradicting bounded appended values.

**Status:** PROVED.

### 1.4 Witness periods in a counterexample are unbounded
If shortest witness periods were eventually bounded by `P` and curling numbers bounded by `M`, the next output would be determined by a finite suffix state of length `MP`; deterministic state repetition would force eventual periodicity, contradicting 1.3.

**Status:** PROVED.

### 1.5 High-symbol root constraint
If a sufficiently late prefix ends in `Y^k` and the final copy of `Y` is generated, then every symbol of `Y` is at least `k-1`.

**Status:** PROVED by examining the orbit immediately before each symbol of the final copy is generated, where `(conjugate(Y))^(k-1)` is already a suffix.

### 1.6 Infinitely many generated 2s
A counterexample cannot eventually have every output at least 3; then every sufficiently long prefix ends in a cube and a one-sided local-period theorem at exponent threshold `phi^2 < 3` forces ultimate periodicity.

**Status:** EXTERNALLY DEPENDENT; requires exact statement/citation of Mignosi–Restivo–Salemi.

## 2. Period-transition and record-overlap lemmas

### 2.1 Adjacent transition gap for witness periods
Suppose `cn(S)=k` with shortest primitive witness period `p`, and after appending `k`, `cn(Sk)=ell >= 2` with shortest primitive witness period `q`; let `d=gcd(p,q)`. If `p != q`, then

`(ell-1)q <= p-d` or `q >= (k-1)p+d+1`.

Special case `k=ell=3`: `q=p`, or `q<p/2`, or `q>2p`.

**Status:** PROVED via Fine–Wilf overlap, subject to index audit.

### 2.2 Adjacent shortest cube-period gap
If the shortest period of a cube ending at position `i` is `p`, and that of a cube ending at `i+1` is `q`, then

`p=q` or `q>2p` or `p>2q`.

**Status:** PROVED via four explicit Fine–Wilf/extension cases, subject to formal index audit.

### 2.3 Master record-scale dichotomy
For a strict record witness `S=X Y^K`, `|Y|=P`, and a symbol `y_i=ell` in the final generated copy of `Y`, let `q_i<P` be the shortest witness period that generated it and `d_i=gcd(P,q_i)`. Then

`(ell-1)q_i <= P-d_i-1`

or

`(K-2)P+i <= q_i-d_i-1`.

**Status:** PROVED by Fine–Wilf overlap, subject to full endpoint audit.

## 3. Elimination of strict record exponents K >= 4

### 3.1 Circular short-cube theorem
A primitive circular word of length `P` has some cut at which no cube of period less than `P/2` ends.

**Status:** EXTERNALLY DEPENDENT. Claimed derivation from the one-sided local-period theorem of Mignosi–Restivo–Salemi applied to the bi-infinite periodic extension. Exact theorem statement and source still require rigorous verification.

### 3.2 Consequence for record witnesses
At a strict record witness with exponent `K>=4`, every cut of the primitive root `Y` has a cube ending there with period `<P/2`, by the master inequality and the high-symbol root constraint. This contradicts 3.1.

Therefore no strict record witness has exponent `K>=4`.

**Status:** EXTERNALLY DEPENDENT on 3.1; otherwise proved.

### 3.3 Refuted overstrengthening
The proposed equality-graph theorem saying cube-equality graph components are exactly residue classes modulo `gcd(P,q_0,...,q_{P-1})` is false.

Counterexample: `P=12`, `q_2=1`, and `q_i=4` for `i!=2`; graph has two components despite gcd 1. The induced component coloring is nevertheless period 4, so this does not refute 3.1.

**Status:** REFUTED.

## 4. Binary K in {2,3} record-scale normal form

### 4.1 Record cubes are autonomous
For a strict record cube `S=X Y^3`, the second branch of the master dichotomy is impossible. Hence, for each position `i`, the complete witness generating `y_i` lies inside `Y^2 y_0...y_{i-1}` and does not reach `X`.

Therefore

`cn(Y^2 y_0...y_{i-1}) = y_i` for every `0<=i<P`,

so `Y^2 -> Y^3` independently of left context.

**Status:** PROVED, subject to audit of the master dichotomy and maximality preservation after deleting `X`.

### 4.2 Promotion necklaces
A primitive binary word `Y` satisfying `cn(rotation_i(Y)^2)=Y_i` at every circular position is a promotion necklace. Every fully generated strict record cube root is one.

**Status:** PROVED from 4.1.

### 4.3 Record-square bridge theorem
For a fully generated strict record square `S=X Y^2`, `|Y|=P`, let `a=y_0` and let `q<P` be the shortest witness period generating the first symbol of the final copy. Then:

- `a q > P`;
- `q>P/2`;
- writing `r=P-q` and the period-q root as `R=AB` with `|B|=r`, the root has exact form `Y=BAB`.

**Status:** PROVED, subject to index/maximality audit.

### 4.4 Square-record scale bound
If `R_prev` is the previous global record period, then the bridge period `q<=R_prev`, so

`P < 2 R_prev`.

**Status:** PROVED from 4.3.

### 4.5 External-witness prefix bound
At position `i` of a record-square root, if its generating witness reaches left of the preceding copy of `Y`, then

`i < q_i - gcd(P,q_i) < q_i <= R_prev`.

Thus all positions `i>=R_prev` are generated internally; dependence on older context is confined to a prefix of width at most the previous record period.

**Status:** PROVED from the master dichotomy, subject to endpoint audit.

## 5. Computational structures and checks

### 5.1 Promotion necklaces through length 25
Exhaustive enumeration of primitive binary words found one necklace up to rotation at lengths `1,4,13,21` and none at other lengths through 25.

**Status:** CHECKED(25), assuming preserved code/calibration.

### 5.2 Larger promotion necklaces
Genuine promotion necklaces were found at lengths `90`, `114`, and `621` (among others), refuting the conjecture that promotion-necklace lengths are bounded by 21.

**Status:** COMPUTATIONALLY CHECKED for the explicit words; exact word/code should be archived separately.

### 5.3 Morphic family
Candidate morphism

`mu(2)=2232`, `mu(3)=322232223`

produces lengths `1,4,21,114,621,3384` with recurrence `L_{n+2}=6L_{n+1}-3L_n`. Promotion property checked through length 3384.

**Status:** CHECKED through the stated iterate; general theorem CONJECTURAL.

### 5.4 Exact renormalized record ladders
Base ladder:

`4^2 -> 6^2 -> 7^2 -> 21^3`, followed by outputs `3,2,1`.

A second morphism `nu` lifts this to

`114^2 -> 186^2 -> 207^2 -> 621^3`, then `3,2,1`.

**Status:** COMPUTATIONALLY CHECKED; explicit code/output should be archived.

### 5.5 Binary-seed exhaustive check through length 18
All binary seeds of lengths 1 through 18 were run through their first 1. Among 9,722 fully generated strict record squares observed:

1. first symbol was always 2;
2. first-symbol bridge exponent was always 2, not 3;
3. no orbit had more than two consecutive fully generated strict record squares.

**Status:** CHECKED(18); open beyond.

## 6. Current target: frontier descent

Let consecutive strict record cubes be

`S_j = X_j Y_j^3`, `S_{j+1}=X_{j+1}Y_{j+1}^3`.

Define the cube left frontier `lambda_j=|X_j|`.

### Target A: record-cube recurrence
Every infinite binary orbit avoiding 1 and 4 has infinitely many strict record cubes. A sufficient strengthening is that infinitely many consecutive strict record squares cannot occur without an intervening strict record cube.

**Status:** CONJECTURAL.

### Target B: nonterminal cube-frontier descent
If the orbit survives beyond `S_{j+1}` without producing 1 or 4, then

`lambda_{j+1}<lambda_j`.

The expected mechanism is that every scale increase between record cubes must pass through a record square whose bridge witness imports old left context; for a nonterminal next cube, that imported witness should cross the left edge `lambda_j`, forcing the new cube to begin farther left.

**Status:** CONJECTURAL; this is the immediate research wall.

### Known warning
Unrestricted frontier monotonicity is false: a finite terminal transition can move the cube edge to the right (example described as period 7 cube at edge 0 leading to period 21 cube at edge 13, then termination). Any theorem must include a survival/nonterminal hypothesis or a sharper structural condition.

## 7. Audit obligations

- Re-verify exact statement and applicability of the Mignosi–Restivo–Salemi one-sided local-period theorem before treating K>=4 elimination as fully closed.
- Preserve and calibrate all orbit code against total lengths `a(3)=5`, `a(8)=66`, `a(22)=142`.
- Archive explicit words, event logs, shortest maximizing periods, and source code for every computational claim.
- Never infer maximality of a curling number from a displayed suffix power alone.
- Every use of primitivity must follow from shortest-root maximal-witness selection.
- Distinguish a strict record period from arbitrary larger-scale suffix powers.


## 8. Frontier audit and corrected descent target (2026-07-24, later pass)

### 8.1 First symbol of a fully generated strict record cube root
Let `S=X Y^3` be a strict record cube of shortest period `P=|Y|`, and suppose the final copy of `Y` is generated. Then the first symbol of `Y` is `2`.

**Proof.** Immediately before the first symbol of the final copy is generated, the prefix ends in `Y^2`. If the first symbol were `3`, that prefix would have a cube suffix of some shortest period `q<P`, because period `P` has not yet become a strict record. The same cube suffix, translated by one copy of `Y`, would be present at the completion of `Y^3`; hence the completed cube would have a shortest exponent-3 witness of period at most `q<P`, contradicting that `P` is the new shortest record period. Therefore the first symbol is `2`.

**Status:** PROVED, pending a final endpoint/maximality audit. In the binary hard core, the symbol appended immediately after `Y^3` is `3`, so it is a defect from the periodic fourth copy, which would begin with `2`.

### 8.2 First-import support-span lemma
Let a strict record cube of period `P` end at time `t=lambda+3P`. Consider any later generated symbol at time `n>t`, with value `a<=3` and shortest witness period `q<=P`. Its witness support begins at `n-aq`, and

`n-aq > lambda+3P-3P = lambda`.

Thus no post-cube witness of period at most `P` can reach left of the cube edge `lambda`. Consequently, the first future shortest witness whose support begins left of `lambda` must have period `q>P`; it is itself a new strict record event, and its record-power edge is strictly less than `lambda`.

**Status:** PROVED.

### 8.3 Unqualified pairwise cube-frontier descent is false
There are finite binary seeds with a record cube of period `7` at edge `69`, followed by a period-`21` record cube at edge `82`, after which the orbit survives to a period-`75` record square at edge `0` before reaching `1`.

This refutes the statement “whenever a later record cube survives for any positive number of steps, its edge is below the preceding cube edge.” However, the preceding period-`7` cube in this construction is preloaded in the seed and its final copy is not generated. It therefore does **not** refute the intended late-orbit statement for consecutive fully generated strict record cubes.

**Status:** REFUTED overstrengthening; corrected qualifier recorded.

### 8.4 Corrected immediate wall
The cleanest proved implication is now:

- once a shortest witness actually imports context from left of a fully generated strict record cube edge, the global record frontier drops immediately (8.2);
- what remains is to prove that a nonterminating binary orbit cannot remain forever autonomous to the right of that edge.

A stronger still-plausible target is:

> If two consecutive fully generated strict record cubes occur in a binary orbit, then the second cube edge is strictly smaller than the first.

No counterexample to this fully generated formulation is known. The known morphic hierarchy has cube-edge chains `6747 -> 6147 -> 0`, consistent with strict descent.

**Status:** CONJECTURAL.

### 8.5 Computational distinction that must remain explicit
“Final copy generated” is not the same as “the entire cube generated.” Right-moving finite cube transitions found by targeted left-completion searches have relied on the earlier cube being preloaded or not strict at its cube exponent. This distinction is load-bearing and must be tracked in every event log.
