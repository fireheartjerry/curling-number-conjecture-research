# Curling Number Conjecture Research Ledger

Updated: 2026-07-24

This ledger separates proved natural-language results, computational checks, and open claims. It is not a completed proof of the Curling Number Conjecture.

## Definitions

For a finite sequence S, cn(S) is the largest k such that S = X Y^k for a nonempty word Y. At a prefix of length n, choose p_n as the shortest period attaining cn(S_n)=k_n. Its witness interval is [n-k_n p_n, n). A strict record period is p_n > max_{m<n} p_m. A cube frontier is the left edge lambda = n-3p_n of a cube witness.

## Audited structural results

### 1. Counterexample tail reductions
- Any newly appended value absent from the current sequence forces curling number 1 at the next step.
- Hence a counterexample recycles a finite alphabet from its seed and has bounded outputs.
- Its generated tail cannot be ultimately periodic, since a periodic tail creates arbitrarily high suffix powers.
- Its shortest maximizing witness periods are unbounded.

### 2. High-symbol roots
If a late prefix ends in Y^k and the final copy of Y was generated, then every symbol of Y is at least k-1. Thus a maximal recurrent value M has record roots over {M-1,M}.

### 3. Adjacent shortest cube-period gap
If shortest cube periods at adjacent endpoints are p and q, then p=q, q>2p, or p>2q. This follows from Fine-Wilf, including separate treatment of the equality cases q=2p and p=2q.

### 4. Circular short-cube reduction
A strict record witness of exponent K>=4 forces a cube of period <P/2 at every cut of its primitive root. The intended closure uses the Mignosi-Restivo-Salemi local-period theorem. Exact source hypotheses still require a final primary-source audit before this is promoted to machine-verified status.

### 5. Record-boundary dichotomy
For a strict record witness S=X Y^K, |Y|=P, and symbol ell at offset i in the final generated copy, let q_i<P be its generating witness period and d_i=gcd(P,q_i). Then Fine-Wilf gives

(ell-1) q_i <= P-d_i-1

or

(K-2)P+i <= q_i-d_i-1.

For K=3 the second branch is impossible, so the record cube root is generated autonomously from Y^2. For K=2, the first symbol of the final copy has a bridge witness reaching left of the square edge.

### 6. Autonomous record cube theorem
For every strict record cube S=X Y^3 whose final copy was generated,

cn(Y^2 Y[0:i]) = Y[i]

for every 0<=i<|Y|. Thus Y^2 evolves to Y^3 independently of X.

### 7. Record-square bridge theorem
Let a sufficiently late strict record square have period Q and edge e=t-2Q. Let a in {2,3} be the first symbol of its final root copy, generated at time t-Q by a witness of period r<Q. Then ar>Q. Consequently that bridge witness starts at

t-Q-ar < t-2Q=e,

strictly left of the square itself. Also r>Q/2, and the square root has the overlap form B A B with |AB|=r and |B|=Q-r. In particular Q<2R_prev, where R_prev is the previous global record period.

### 8. Cube-barrier theorem (new)
Suppose at time N a cube witness of period P starts at lambda=N-3P. At any later time t>N, if the maximizing exponent is k in {2,3} and its shortest period q satisfies q<=P, then

start(t)=t-kq >= N+1-3P=lambda+1.

Therefore no witness at the old cube scale or below can ever cross the completed cube frontier. Any future witness beginning left of lambda has period >P.

### 9. Late crossing-square exclusion and first-crossing cube theorem (corrected)
Let N be a sufficiently late strict global record cube of period P and edge lambda=N-3P, with N>=2|S_0|. Let t>N be the earliest later time whose shortest maximizing witness starts left of lambda.

The first crossing witness cannot be a square.

Proof:
- The cube-barrier theorem gives its period Q>P.
- If Q is not a new global record, a prior record R>=Q was established after N. Since that prior record did not cross lambda, direct edge comparison shows t-2Q lies to the right of its edge and hence at or right of lambda, contradiction.
- Thus a crossing square would be a strict record square of period Q. Let f=t-Q be the start of its final root copy.
- If f>N, the record-square bridge at time f begins strictly left of the square edge, hence left of lambda, contradicting the minimality of t.
- Therefore f<=N. Since t>=N>=2|S_0|, the final root copy is generated and the bridge theorem applies. Its bridge period r was already available by time N, so r<=P, while r>Q/2. Hence Q<2P.
- The crossing square interval contains the entire preceding P-cube, so that length-3P factor has periods P and Q. Because Q<2P, Fine-Wilf gives period gcd(P,Q)<P, contradicting the primitivity of the P-root.

Therefore the earliest witness importing context across a sufficiently late strict record cube is a cube. Its period exceeds P and its left edge is strictly smaller than lambda. If an earlier post-N cube had at least that period, a direct edge comparison would prevent the crossing, so the imported cube is a new cube-period record.

This is the rigorous local frontier-descent statement. It does not by itself prove that a crossing must occur: an autonomous, noncrossing cube hierarchy remains the global obstruction.

## Exact computational findings

All reported curling numbers were computed by maximizing over every suffix block length, using the reversed-word Z-function identity. Calibration convention: total length immediately before the first 1; values 5, 66, 142 are reproduced for binary start lengths 3, 8, 22.

### Promotion hierarchy
- mu(2)=2232, mu(3)=322232223.
- Iterated lengths from 2: 1,4,21,114,621,3384, satisfying L_{n+2}=6L_{n+1}-3L_n.
- Promotion behavior checked through length 3384 for the tested canonical iterates.

### Renormalized stages
A base autonomous ladder contains record periods 4^2 -> 6^2 -> 7^2 -> 21^3 and terminates. Its nu=mu^2 lift contains 114^2 -> 186^2 -> 207^2 -> 621^3 and terminates.

### Restricted finite-memory map F_R
F_R stores the last 3R symbols and appends the exact curling exponent using only periods <=R when it is 2 or 3.
- Exhaustive cycles: R=1 has the trivial cycle; R=2,...,6 have none; R=7 and R=8 have one length-21 cycle up to rotation.
- The proposed predecessor-isolation lemma is false: every state of the R=7 length-21 cycle has both binary predecessors valid.
- Specific cube-completion defects mostly terminate in truncated dynamics, but some re-enter the cycle; full dynamics would then eventually detect the larger periodic power.

### Autonomous cube transitions
- Some rotations of period-4, 7, 9, 10, and 13 cube roots autonomously reach a period-21 cube and then terminate.
- Two rotations of a period-114 morphic root autonomously reach a period-621 cube and then terminate.
- All tested rotations of the canonical period-21 and period-621 roots terminate without a larger cube record.
- This supports a parity-like active/inactive morphic hierarchy but does not prove classification.

## Current exact frontier

The local imported-witness wall is now crossed:

1. old-scale witnesses cannot cross a completed cube edge;
2. the earliest crossing witness cannot be a square;
3. it is a larger cube with a strictly smaller left edge.

The remaining global obstruction is the possibility of a sealed autonomous cube tail: a counterexample beginning at Y^3 whose future witnesses never need context to its left. Eliminating such an infinite autonomous chain, or constructing one, is now the exact proof/counterexample fork.

A second outstanding statement is cube recurrence: an infinite binary 2/3 orbit must have infinitely many increasing cube scales. Record periods are unbounded, but a proof excluding an infinite record-square-only regime is still needed.
