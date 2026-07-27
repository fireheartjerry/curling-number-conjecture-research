# Curling Number Conjecture — Three-Chat Mega-Ledger and Codex Handoff

**Project:** Jerry (Yuze) Li / ChatGPT collaborative attack  
**Consolidation date:** 2026-07-27  
**Coverage:** Part 1 + Part 2 + Part 3, plus all preserved proof ledgers, computational assets, corrections, and raw reports  
**Primary consumer:** a fresh high-reasoning agent or OpenAI Codex working from a repository  
**Current status:** **NO COMPLETE PROOF OR COUNTEREXAMPLE YET**

---

## 0. Read this before doing mathematics

This is the canonical consolidation of three long research chats. It is deliberately large. The project accumulated several layers of results, provisional proofs, computational observations, false strengthenings, and later corrections. A new agent must not flatten those distinctions.

### Conflict rule

When two passages conflict, use the following order of authority:

1. **The canonical current-status sections at the front of this file.**
2. **The latest Part 3 section.**
3. **The 2026-07-26 full handoff ledger.**
4. **Older proof/research ledgers and raw reports.**
5. **Computational evidence**, which never silently becomes a theorem.

The appendices preserve older documents verbatim for archaeology. They are not all simultaneously current. Human beings invented version control and then continued passing around contradictory proof notes anyway.

### Status vocabulary used here

- **PROVED-NL:** a complete natural-language argument is recorded, but it is not machine formalized.
- **PROVISIONAL:** a plausible argument exists and may be correct, but it still needs an independent endpoint/maximality audit.
- **CONDITIONAL:** the statement depends on an external theorem whose exact hypotheses or source must still be audited.
- **CHECKED(n):** exact computation verified all cases in the stated finite range.
- **EVIDENCE:** nonexhaustive or bounded computation only.
- **REFUTED:** a counterexample is known; do not reopen without a materially different statement.
- **OPEN:** no proof or counterexample is currently claimed.

Nothing in this file is labeled machine-verified. The original research prompt demanded code-produced curling-number values, calibrated implementations, explicit case splits, and no promotion of empirical patterns to theorem. Preserve that discipline.

---

## 1. Executive status at the end of Part 3

The strongest current structural picture is:

1. A hypothetical counterexample has bounded generated values, cannot have an ultimately periodic tail, and must have unbounded shortest maximizing witness periods.
2. After a local-period reduction, the binary hard core is governed by strict record powers of exponent only
   \[
   K\in\{2,3\}.
   \]
   This reduction remains **CONDITIONAL** on a primary-source audit of the one-sided local-period theorem used to eliminate \(K\ge4\).
3. Fully generated strict record cubes are autonomous promotion blocks:
   \[
   Y^2\longrightarrow Y^3
   \]
   without older left context.
4. Fully generated strict record squares have exact bridge form
   \[
   R=AB,
   \qquad
   Y=BAB=BR,
   \qquad
   q=|R|>\frac P2,
   \qquad
   P=|Y|=q+|B|.
   \]
5. The immediate local target is the **bridge-promotion lemma**: a bridge root \(R\) used to generate a genuine strict record square should itself be a promotion root.
6. Every position of \(R\) carrying symbol \(2\) is now proved to promote.
7. Therefore any first promotion failure must be at a symbol \(3\), where the standalone state has curling number exactly \(2\).
8. Such a failure produces two actual context-dependent cube witnesses whose endpoints are separated by exactly \(P\), with a conjugate of \(Y\) generated between them.
9. The corrected Two-External-Cubes / Generated Two-Cube Synchronization Lemma remains **OPEN**. Part 3 substantially narrowed its possible geometry but did not close it.
10. Even after bridge promotion and square-chain monotonicity, the final global wall is still **autonomous exact-power termination**:
    \[
    \boxed{
    \text{No exact binary square or cube seed has an infinite orbit avoiding }1\text{ and }4.
    }
    \]

### Immediate wall

Finish the generated two-cube synchronization argument, then derive promotion at every \(3\)-position and conclude the bridge-promotion lemma.

### Final wall

Eliminate an infinite sealed hierarchy of autonomous exact powers, especially record cubes and finite square ladders that never request context to their left.

---

## 2. Problem, deterministic orbit, and witness conventions

For a finite nonempty sequence \(S\),

\[
\operatorname{cn}(S)
=
\max\left\{
 k\ge1:
 S=XY^k
 \text{ for a possibly empty }X
 \text{ and a nonempty }Y
\right\}.
\]

If several roots attain the maximum exponent, the **canonical period** is the shortest root length. At a prefix of length \(n\), write

\[
k=\operatorname{cn}(S),
\qquad
p=\text{shortest period attaining }k.
\]

The canonical witness occupies

\[
[n-kp,n),
\]

and its start is

\[
s(S)=n-kp.
\]

The orbit is deterministic:

\[
S_{m+1}=S_m\,\operatorname{cn}(S_m).
\]

A **strict record period** is a canonical period larger than every earlier canonical period in the same orbit. A strict record witness is written

\[
S=XY^K,
\qquad
|Y|=P,
\]

where \(P\) is the new record. Its root \(Y\) is primitive because \(P\) is the shortest maximizing period.

### Generation qualifiers that must never be conflated

- **Preloaded power:** some or all repeated copies were already present in the seed.
- **Final copy generated:** the orbit appended the last copy of the displayed root.
- **Entire power generated:** every displayed copy was appended after the chosen boundary.
- **Actual bridge period:** the canonical period present at the true start of the final generated copy, not a period inferred from an arbitrary border decomposition.

A large fraction of the false examples in this project came from forgetting one of those adjectives. The adjectives won.

---

## 3. Canonical notation for the current promotion wall

For a fully generated strict record square of period \(P\), write

\[
R=AB,
\qquad
q=|R|,
\qquad
b=|B|=P-q,
\qquad
Y=BAB=BR,
\]

so

\[
|A|=2q-P=q-b>0,
\qquad
q>\frac P2.
\]

At a candidate first promotion failure at index \(j\), write

\[
T=R[0:j],
\qquad
U=R[j:q],
\qquad
R=TU.
\]

The correct four actual states are

\[
E:=LRT,
\qquad
G:=LR^2,
\qquad
F:=LR^2BT,
\qquad
H:=LR^2BR.
\]

The orbit segments are

\[
E\xrightarrow{\ U\ }G,
\qquad
F\xrightarrow{\ U\ }H.
\]

At a first \(3\)-position failure:

\[
\operatorname{cn}(E)=3,
\qquad
\operatorname{cn}(G)=2,
\qquad
\operatorname{cn}(F)=3,
\qquad
\operatorname{cn}(R^2T)=2.
\]

Let

\[
p=\text{shortest cube period at }E,
\qquad
r=\text{shortest cube period at }F.
\]

The endpoint displacement is

\[
|F|-|E|=q+b=P,
\]

and the generated block between them is

\[
UBT=R[j:q]BR[0:j],
\]

a conjugate of \(Y=BTU\).

**Important correction:** \(LR^2T\) is not automatically an actual orbit state. The later actual state is \(LR^2BT\). Any argument that silently removes the \(B\) is invalid.

---

# Part A. Chronological consolidation of Chat Part 1

## 4. Initial counterexample reductions

### 4.1 New-symbol reset — PROVED-NL

If the orbit appends a value \(k\) that has never appeared earlier in the sequence, then the next curling number is \(1\). Any suffix repetition ending at the newly introduced \(k\) would require another aligned copy of \(k\), which does not exist.

### 4.2 Finite recycled alphabet — PROVED-NL

A nonterminating orbit can append only values already appearing in its finite seed. Hence generated values are bounded.

### 4.3 No ultimately periodic counterexample tail — PROVED-NL

An ultimately periodic infinite tail would create arbitrarily high suffix powers at period-aligned endpoints. This contradicts bounded generated values.

### 4.4 Unbounded canonical periods — PROVED-NL

If both generated exponents and shortest maximizing periods were eventually bounded, the next output would depend only on a bounded suffix state. A repeated state would force eventual periodicity, contradicting the previous lemma.

### 4.5 High-symbol root constraint — PROVED-NL, endpoint audit advised

If a sufficiently late prefix ends in \(Y^k\) and the final copy of \(Y\) was generated, every symbol of \(Y\) is at least \(k-1\). Immediately before a symbol in the final copy is appended, the preceding \(k-1\) cyclic copies already provide a suffix power of exponent \(k-1\).

### 4.6 Infinitely many generated \(2\)'s — CONDITIONAL

A hypothetical counterexample cannot eventually generate only values at least \(3\). The intended argument invokes a one-sided local-period theorem at exponent threshold \(\varphi^2<3\) to force ultimate periodicity. The exact Mignosi–Restivo–Salemi statement and hypotheses still require primary-source verification.

---

## 5. Period-transition machinery

### 5.1 Adjacent period transition gap — PROVED-NL, index audit advised

Suppose a state has curling number \(k\) and shortest period \(p\). After appending \(k\), suppose the new state has curling number \(\ell\ge2\) and shortest period \(q\). Put

\[
d=\gcd(p,q).
\]

For \(p\ne q\), Fine–Wilf overlap yields

\[
(\ell-1)q\le p-d
\]

or

\[
q\ge(k-1)p+d+1.
\]

In the cube-to-cube case:

\[
q=p,
\qquad
q<\frac p2,
\qquad\text{or}\qquad
q>2p.
\]

### 5.2 Adjacent period increases move the canonical start left — PROVED-NL

With

\[
s=n-kp,
\qquad
s'=n+1-\ell q,
\]

the large-period branch gives

\[
s-s'=
\ell q-kp-1>0.
\]

This is useful for frontier descent, but only for adjacent transitions. It never justified an unconditional statement about arbitrary later record powers.

### 5.3 Master record-scale dichotomy — PROVED-NL, full endpoint audit advised

For a strict record power

\[
S=XY^K,
\qquad |Y|=P,
\]

consider the symbol \(\ell=Y[i]\) in the final generated copy. Let \(q_i<P\) be the shortest witness period generating that symbol and put

\[
d_i=\gcd(P,q_i).
\]

Fine–Wilf gives

\[
(\ell-1)q_i\le P-d_i-1
\]

or

\[
(K-2)P+i\le q_i-d_i-1.
\]

This dichotomy became the main local engine for separating record cubes from record squares.

---

## 6. Reduction to the binary \(K\in\{2,3\}\) hard core

### 6.1 Circular short-cube theorem — CONDITIONAL

The claimed external statement is:

> A primitive circular word of length \(P\) has a cut at which no cube of period below \(P/2\) ends.

The intended derivation applies a one-sided local-period theorem to the bi-infinite periodic extension. The exact source and applicability must be audited before publication.

### 6.2 Elimination of strict record exponents \(K\ge4\) — CONDITIONAL

The master dichotomy plus the high-symbol constraint would force a short cube at every circular cut of a primitive record root. The circular short-cube theorem forbids this. Therefore later strict record exponents reduce to

\[
K\in\{2,3\}.
\]

---

## 7. Record cubes

### 7.1 Autonomous record cube theorem — PROVED-NL, maximality deletion audit advised

For a generated strict record cube

\[
S=XY^3,
\qquad |Y|=P,
\]

one obtains

\[
\operatorname{cn}\bigl(Y^2Y[0:i]\bigr)=Y[i]
\qquad(0\le i<P).
\]

Thus

\[
Y^2\longrightarrow Y^3
\]

independently of the older context \(X\).

### 7.2 Promotion roots / necklaces

A primitive binary word \(Y\) satisfying

\[
\operatorname{cn}\bigl(\rho_i(Y)^2\bigr)=Y[i]
\]

at every circular cut is a promotion root or promotion necklace. Every fully generated strict record cube root is one.

Observed promotion lengths include

\[
1,4,13,21,90,114,621,3384,\ldots
\]

The morphism

\[
\mu(2)=2232,
\qquad
\mu(3)=322232223
\]

produces a checked family with lengths

\[
1,4,21,114,621,3384,
\]

satisfying

\[
L_{n+2}=6L_{n+1}-3L_n.
\]

General synchronization of this morphism remains open.

---

## 8. Record squares

### 8.1 Root curling number and robustness — PROVED-NL

For a fully generated strict record square \(XY^2\), \(|Y|=P\):

\[
\operatorname{cn}(Y)=1.
\]

Moreover, no proper suffix of \(Y^2\) has curling number at least \(2\). In particular, the later useful suffix

\[
RBR
\]

has curling number \(1\).

### 8.2 Exact bridge form — PROVED-NL

Let \(q<P\) be the shortest witness period generating the first symbol of the final copy of \(Y\). Then

\[
q>\frac P2.
\]

Write

\[
R=AB,
\qquad
|R|=q,
\qquad
|B|=P-q.
\]

Then

\[
Y=BAB=BR,
\]

and

\[
|A|=2q-P>0.
\]

At the start of the final generated copy, the state ends in

\[
R^2.
\]

The bridge defect is

\[
\alpha=2q-P=|A|.
\]

### 8.3 Context localization and square scale bound — PROVED-NL

At position \(i\) of a record-square root, an external generating witness of period \(q_i\) can occur only when

\[
i<q_i-\gcd(P,q_i).
\]

If \(R_{\mathrm{prev}}\) is the previous global record period, all positions

\[
i\ge R_{\mathrm{prev}}
\]

are generated internally.

The bridge period already existed before the new record, so

\[
q\le R_{\mathrm{prev}}.
\]

Since \(q>P/2\),

\[
P<2R_{\mathrm{prev}}.
\]

This was the state handed from Part 1 into the frontier work of Part 2.

---

# Part B. Chronological consolidation of Chat Part 2

## 9. Frontier descent and the corrected first-crossing theorem

For a completed record cube of period \(P\) ending at time \(N\), define its left edge

\[
\lambda=N-3P.
\]

Old-scale witnesses of period at most \(P\) cannot later cross this completed cube edge. Any later canonical witness beginning left of \(\lambda\) must have period larger than \(P\).

The original universal claim that every intervening square bridge crosses the preceding record cube edge was found false for finite terminating trajectories. The correct statement became a **first crossing** theorem:

> Let \(\tau>N\) be the first later endpoint whose canonical witness begins left of the old cube edge. Under the sufficiently late fully generated hypotheses, the first crossing cannot be a square. It is a cube of period larger than \(P\), and its cube edge lies strictly left of \(\lambda\).

This proves local frontier descent **once context import occurs**. It does not prove that context import must eventually occur. A sealed autonomous suffix may execute internal record ladders.

---

## 10. Global-minimum power-seed reduction — PROVED-NL

Assume an infinite binary orbit avoiding \(1\) and \(4\). For each prefix choose its canonical witness start and let \(L\) be the global minimum, first attained at time \(t\). The suffix beginning at \(L\) is an exact square or cube

\[
R^k,
\qquad
k\in\{2,3\}.
\]

All later canonical witnesses begin at or to the right of \(L\). Deleting the prefix before \(L\) preserves every later curling number: existing suffix witnesses remain, and deleting a prefix cannot create a new suffix repetition absent from the original state.

Therefore any binary counterexample implies an exact square/cube seed whose future orbit never needs context to the left of that initial power.

This converts the final global problem into autonomous exact-power termination.

---

## 11. Refuted strengthenings and traps

### 11.1 False equality-graph theorem — REFUTED

The claim that cube-equality components equal residue classes modulo the total gcd is false. A \(P=12\) assignment with one local period \(1\) and the others period \(4\) gives two components despite total gcd \(1\).

### 11.2 Universal bridge crossing — REFUTED

Not every intervening strict record square bridge crosses the preceding cube edge. Finite autonomous ladders contain noncrossing transitions.

### 11.3 Unconditional pairwise cube-edge descent — REFUTED

Later record cubes can move right when an earlier cube is preloaded or lacks the exact generated/nonterminal hypotheses.

### 11.4 Static bridge geometry — INSUFFICIENT

Words may satisfy border equations suggesting \(q_2>q_1\), while their actual deterministic orbits do not realize the corresponding squares as consecutive generated records. Actual canonical periods and generation times are load-bearing.

### 11.5 Bounded promotion-necklace lengths — REFUTED

Lengths \(90,114,621\) and later checked iterates rule out any claim that promotion necklaces stop at \(21\).

### 11.6 Restricted-map predecessor isolation — REFUTED

In the bounded finite-memory map, the observed length-21 cycle has valid binary predecessors; predecessor isolation does not close the autonomous tail.

---

## 12. Computed autonomous ladders and censuses

### 12.1 Base and lifted ladders

A checked base ladder is

\[
4^2\to6^2\to7^2\to21^3,
\]

followed by termination. A lifted ladder is

\[
114^2\to186^2\to207^2\to621^3,
\]

again followed by termination.

These are real renormalized structures, not counterexamples.

### 12.2 Consecutive square census

Using exact shortest-maximizing-period computation:

- all binary seeds through length \(26\) were checked;
- \(491{,}330\) qualifying consecutive generated strict-record-square pairs were found;
- no case had \(q_2>q_1\);
- every local pair type was
  \[
  (P_1,q_1)=(6,4)
  \longrightarrow
  (P_2,q_2)=(7,4).
  \]

Further audits recorded:

- \(566{,}566\) valid primitive exact square seeds with root length at most \(20\);
- \(1{,}474{,}298\) valid primitive exact cube seeds with root length at most \(20\);
- an exact-square-root census through root length \(24\);
- \(1{,}000{,}000\) random binary seeds of lengths \(27\) through \(200\), producing \(3{,}583\) qualifying pairs, all of the same \(6/4\to7/4\) type.

These are evidence, not proof.

### 12.3 Canonical small transition

The canonical observed transition has

\[
Y_1=232223,
\qquad P_1=6,
\qquad q_1=4,
\]

with

\[
A_1=22,
\qquad B_1=23,
\qquad R_1=2223.
\]

The next square has

\[
Y_2=2232223,
\qquad P_2=7,
\qquad q_2=4,
\]

with

\[
A_2=2,
\qquad B_2=223,
\qquad R_2=2223.
\]

Thus

\[
R_2=R_1,
\qquad
A_1=A_2^2,
\qquad
B_2=A_2B_1,
\qquad
Y_2=A_2Y_1.
\]

After the first square, the orbit appends exactly \(R_1=2223\) and returns to \(R_1^2\).

---

## 13. Bridge-period monotonicity and replay framework

For consecutive autonomous generated strict record squares, write

\[
S_{t_i}=X_iY_i^2,
\qquad
|Y_i|=P_i,
\qquad
P_1<P_2,
\]

and let \(q_i\) be the actual canonical bridge period at the start of the final generated copy. The target is

\[
q_2\le q_1.
\]

Define

\[
\alpha_i=2q_i-P_i=|A_i|>0.
\]

If \(q_2\le q_1\), then

\[
\alpha_2-
\alpha_1
=
2(q_2-q_1)-(P_2-P_1)<0.
\]

Thus bridge defects strictly descend, ruling out an infinite square-record-only chain.

The stronger computed target is a first-return lemma:

> If the next strict record after a generated record square is another generated square rather than a cube or termination, the orbit appends the old bridge root \(R\), returns to a suffix \(R^2\) after exactly \(q\) steps, and the returned state has curling number \(2\).

### Replay notation

During the generation of the final copy of \(Y=BR\), define

\[
E_j=L R^2 B R[0:j],
\qquad 0\le j\le q.
\]

Generation means

\[
\operatorname{cn}(E_j)=R[j]
\qquad(0\le j<q).
\]

At \(j=q\),

\[
E_q=LR^2BR,
\]

the completed record square.

The proposed replay states are

\[
F_j=LR^2BRR[0:j].
\]

If

\[
\operatorname{cn}(F_j)=R[j]
\]

for every \(j<q\), the square appends \(R\) and returns to \(R^2\).

A provisional first-mismatch analysis showed that, assuming \(R\) is already a promotion root, a replay mismatch below period \(P\) should be impossible except for termination or a new record. This argument remains **PROVISIONAL** and requires endpoint auditing after promotion is proved.

---

# Part C. Chat Part 3 — newest bridge-promotion work

## 14. Exact bridge-promotion lemma

Let

\[
R=AB,
\qquad
Y=BAB=BR,
\qquad
q=|R|,
\qquad
P=|Y|,
\qquad
q>\frac P2.
\]

Suppose:

1. an actual full state \(LR^2\) generates \(Y\);
2. every canonical witness period used before completion is below \(P\);
3. the completed word is a strict record square of shortest period \(P\);
4. the occurrence \(LR^2\) itself was reached by actually generating its second \(R\), and at that point
   \[
   \operatorname{cn}(LR^2)=2
   \]
   with shortest maximizing period \(q\).

The desired conclusion is

\[
\boxed{
\operatorname{cn}\bigl(R^2R[0:j]\bigr)=R[j]
\quad(0\le j<q).
}
\]

Equivalently, the genuine strict-record bridge root is a promotion root.

---

## 15. Every \(2\)-position promotes — PROVED-NL

Let

\[
T=R[0:j]
\]

and assume

\[
R[j]=2.
\]

The word \(R^2T\) ends in two copies of the conjugate

\[
R[j:q]R[0:j],
\]

so

\[
\operatorname{cn}(R^2T)\ge2.
\]

Suppose it has a cube suffix of period \(p\). Since

\[
|R^2T|=2q+j<3q,
\]

we have

\[
p<q.
\]

When the corresponding symbol in the generated second copy of \(R\) was produced, the actual state ended in \(RT\) and had curling number exactly \(2\). Hence the cube in \(R^2T\) cannot lie wholly inside \(RT\), so

\[
3p>q+j. \tag{15.1}
\]

If \(j\le p\), deleting the final \(j\) symbols leaves a \(p\)-periodic suffix of \(R^2\) of length

\[
3p-j\ge2p.
\]

Then \(LR^2\) has a square suffix of period \(p<q\), contradicting the minimality of \(q\). Therefore

\[
j>p. \tag{15.2}
\]

Combining (15.1) and (15.2),

\[
3p>q+j>q+p,
\]

so

\[
2p>q. \tag{15.3}
\]

Let

\[
d=\gcd(p,q).
\]

The \(p\)-cube lies in the \(q\)-periodic word \(R^2T\). By (15.3), its length reaches the Fine–Wilf threshold:

\[
3p\ge p+q-d.
\]

Thus the cube has period \(d\). Since \(p<q\), we have \(d<p\). Write

\[
p=md,
\qquad q=nd.
\]

Then \(m\ge2\) and \(n\ge3\). Furthermore,

\[
q+j>q+p\ge5d.
\]

The suffix \(RT\), being a suffix of the \(d\)-periodic cube, contains at least three consecutive copies of a length-\(d\) block. That contradicts the fact that the actual generated state ending in \(RT\) had curling number \(2\).

Therefore \(R^2T\) has no cube suffix. Hence

\[
\boxed{
\operatorname{cn}(R^2T)=2=R[j].
}
\]

---

## 16. Generated \(R^2\) alone does not imply promotion — REFUTED overstrengthening

The exact counterexample is

\[
D=223222,
\qquad
R=322232.
\]

Starting from \(DR\), exact computation generates the second copy of \(R\):

\[
3,2,2,2,3,2,
\]

and reaches \(DR^2\) with curling number \(2\) and shortest period \(6\).

But standalone \(R^2\) begins with continuation

\[
2,2,3,2,2,3,
\]

rather than \(R\).

The bundled script `verify_part3_examples.py` reproduces these values after calibration. Therefore the following statement is false:

> If some context generates a second copy of \(R\) and finishes at an exact \(R^2\), then \(R\) is a promotion root.

The subsequent generation of the strict record-square root \(Y=BR\) is essential.

---

## 17. Only possible first failures are \(3\)-positions — PROVED-NL

The previous lemma eliminates all positions carrying \(2\). Let \(j\) be a first promotion failure. Then

\[
R[j]=3.
\]

The standalone state \(R^2T\) already has a square suffix, so its curling number is at least \(2\). It cannot be \(3\), by assumption of failure. It also cannot be at least \(4\):

Suppose

\[
K=\operatorname{cn}(R^2T)\ge4
\]

with shortest maximizing period \(p\). Since

\[
Kp\le2q+j<3q,
\]

we have \(p<q\).

The \(K\)-power cannot lie wholly in \(RT\), because the actual generated state ending in \(RT\) has curling number exactly \(3\). Hence

\[
Kp>q+j. \tag{17.1}
\]

If

\[
j\le(K-2)p,
\]

deleting the final \(T\) leaves a \(p\)-periodic suffix of \(R^2\) of length at least \(2p\), contradicting the shortest square period \(q\) at \(LR^2\). Therefore

\[
j>(K-2)p. \tag{17.2}
\]

From (17.1) and (17.2),

\[
Kp>q+(K-2)p,
\]

so

\[
2p>q. \tag{17.3}
\]

Let \(d=\gcd(p,q)\). The \(K\)-power is a factor of the \(q\)-periodic word \(R^2T\), and its length exceeds the Fine–Wilf threshold, so it has period \(d\). It contains the entire suffix \(RT\). Because \(p<q<2p\), one has \(d\le p/2\), while (17.2) with \(K\ge4\) gives

\[
|RT|=q+j>q+2p>3p\ge6d.
\]

Thus the actual state ending in \(RT\) would contain many consecutive \(d\)-blocks and have curling number larger than \(3\), contradiction.

Therefore a first failure satisfies

\[
\boxed{
R[j]=3,
\qquad
\operatorname{cn}(R^2T)=2.
}
\]

---

## 18. Correct two-external-cube geometry

At the earlier occurrence of the symbol \(R[j]=3\), the actual state is

\[
E=LRT
\]

and has curling number \(3\). Since standalone \(R^2T\) has no cube, every early cube witness crosses the beginning of \(RT\).

At the later occurrence, while the \(R\)-part of \(Y=BR\) is generated, the actual state is

\[
F=LR^2BT
\]

and again has curling number \(3\). Since \(R^2T\) also ends in \(BT\), any cube wholly inside \(BT\) would already be present in the standalone state. Therefore every later cube witness crosses the beginning of \(BT\).

The endpoints are separated by

\[
P=q+b,
\]

and the intervening generated block is the conjugate

\[
UBT.
\]

Let \(p\) and \(r\) be the shortest cube periods at \(E\) and \(F\).

### Original target

Prove that the two cubes force either:

\[
R^2T\text{ has a cube suffix}
\]

or

\[
\max(p,r)\ge P.
\]

The first gives the missing promotion value \(3\); the second contradicts strict record minimality because both endpoints occur before completion of the record-\(P\) square.

### Refined generated target

Static word equations alone are insufficient. The exact remaining statement should use the two actual orbit segments

\[
E\xrightarrow{\ U\ }G,
\qquad
F\xrightarrow{\ U\ }H.
\]

A useful refined version is:

> If \(R^2T\) has no cube, then one of the two canonical cube periods, or an intermediate canonical period during one of the two generated copies of \(U\), is at least \(P\).

This is the **Generated Two-Cube Synchronization Lemma**.

---

## 19. Audited restrictions on any counterexample to synchronization

Assume for contradiction

\[
p<P,
\qquad
r<P,
\]

and \(R^2T\) has no cube.

### 19.1 Early cube Fine–Wilf defect — PROVED-NL

The early cube crosses the beginning of \(RT\), so

\[
3p>q+j. \tag{19.1}
\]

The word \(RT\) has period \(q\), and as a suffix of the early cube it also has period \(p\). Put

\[
d=\gcd(p,q).
\]

If

\[
q+j\ge p+q-d,
\]

Fine–Wilf would give period \(d\) on \(RT\), hence on its first \(q\) letters \(R\). Since \(p<P<2q\) and \(p\ne q\), this gives a proper period of \(R\), contradicting the canonical square period \(q\). Therefore

\[
\boxed{
j<p-d.} \tag{19.2}
\]

### 19.2 The early cube cannot have period \(q\) — PROVED-NL

If \(p=q\), then \(E=LRT\) ends in

\[
(UT)^3.
\]

Appending \(U\) gives

\[
(UT)^3U=U(TU)^3,
\]

so \(G=LR^2\) ends in

\[
(TU)^3=R^3,
\]

contradicting \(\operatorname{cn}(G)=2\). Hence

\[
\boxed{p\ne q.} \tag{19.3}
\]

Thus

\[
p<q
\qquad\text{or}\qquad
q<p<P.
\]

### 19.3 Complete later-cube dichotomy — PROVED-NL

Put

\[
s=b+j,
\qquad
e=\gcd(r,P).
\]

The later suffix \(YBT\) has period \(P\).

If the \(r\)-cube lies wholly inside \(YBT\), Fine–Wilf and the primitivity of \(Y\) force

\[
\boxed{2r\le P-e-1.} \tag{19.4}
\]

If the cube begins before \(YBT\), then all of \(YBT\) lies inside it. Fine–Wilf forces

\[
\boxed{b+j\le r-e-1.} \tag{19.5}
\]

Hence

\[
\boxed{
2r\le P-e-1
\quad\text{or}\quad
b+j\le r-e-1.
} \tag{19.6}
\]

### 19.4 Common-suffix escape condition — PROVED-NL

The common suffix \(BT\) has periods \(p\) and \(r\). Put

\[
g=\gcd(p,r).
\]

If

\[
b+j\ge p+r-g
\]

and

\[
b+j\ge3g,
\]

Fine–Wilf gives a \(g\)-cube in \(BT\), hence in \(R^2T\), contradiction. Therefore

\[
\boxed{
 b+j<p+r-g
 \quad\text{or}\quad
 b+j<3g.
} \tag{19.7}
\]

These inequalities are restrictive but not by themselves contradictory.

---

## 20. Static two-cube impostor — why deterministic generation is essential

Exact computation gives the static configuration

\[
R=233323,
\qquad
B=23,
\qquad
j=1,
\qquad
T=2,
\qquad
P=8,
\]

with

\[
L=23332322333232.
\]

The bundled verification script computes:

\[
\operatorname{cn}(LRT)=3
\quad\text{with shortest period }7,
\]

\[
\operatorname{cn}(LR^2)=2
\quad\text{with shortest period }6,
\]

\[
\operatorname{cn}(LR^2BT)=3
\quad\text{with shortest period }2,
\]

\[
\operatorname{cn}(LR^2BR)=2
\quad\text{with shortest period }8,
\]

and

\[
\operatorname{cn}(R^2T)=2.
\]

So both external cube periods lie below \(P\) while the standalone word has no cube.

However, starting from \(LR\), the actual generated block is

\[
232332,
\]

not the desired second copy

\[
R=233323.
\]

Thus the full generation hypothesis eliminates this impostor. Any successful proof must use the fact that the same block \(U\) is actually generated in both windows.

---

## 21. Border–conjugate short-period lemma — PROVISIONAL-NL, full proof preserved

This lemma was developed to close a subcase of the equal-period later-cube branch.

### Statement

Let \(W\) be a word of length \(n\). Suppose:

1. \(W\) has a border \(B\) of length
   \[
   0<b<\frac n2;
   \]
2. \(W=TU\), where
   \[
   j=|T|<n-b;
   \]
3. the conjugate
   \[
   C=UT
   \]
   has a period \(t\) with
   \[
   0<t<b.
   \]

Then \(W\) has a square suffix.

### Period-extension sublemma

Suppose a word \(V\) has period \(m\). Suppose a suffix \(S\) of \(V\) has period \(d\), with \(d\mid m\), and length at least \(m+d\). Then \(V\) has period \(d\).

Let the suffix begin at index \(a\). For any \(x<a\), choose the least \(k\ge0\) such that \(x+km\ge a\). Minimality gives \(x+km<a+m\). Since \(|S|\ge m+d\), both \(x+km\) and \(x+d+km\) lie inside \(S\). Therefore

\[
V[x]=V[x+km]=V[x+d+km]=V[x+d].
\]

The prefix version follows by reversal.

### Proof of the main lemma

Write

\[
a=n-b,
\]

and \(W=BMB\).

#### Case 1: \(j\ge b\)

The prefix \(T\) begins with \(B\), and \(U\) ends with \(B\), so \(C=UT\) contains \(B^2\) across the cut. The word \(B^2\) has periods \(b\) and \(t\). Fine–Wilf gives period

\[
d=\gcd(b,t)<b.
\]

Because \(d\mid b\), the suffix \(B\) contains a \(d\)-square.

#### Case 2: \(t\le j<b\)

Now \(T\) is the length-\(j\) prefix of \(B\). The conjugate ends in \(BT\), which has periods \(b\) and \(t\) and length \(b+j\ge b+t\). Fine–Wilf again gives period \(d=\gcd(b,t)\) on \(B\), producing a square suffix.

#### Case 3: \(j<t\) and \(|U|\ge2t\)

The word \(U\) is a prefix of the \(t\)-periodic conjugate. Its final \(2t\) symbols form a square, and \(U\) is a suffix of \(W\).

#### Case 4: \(j<t\) and \(|U|<2t\)

Put

\[
h=|U|=n-j,
\qquad
e=b-t,
\qquad\rho=n-2t,
\qquad v=\rho-e.
\]

Since \(b<n/2\),

\[
\rho>2e>0.
\]

Since \(h<2t\),

\[
\rho<j<t.
\]

Thus

\[
0<2e<\rho<j<t,
\qquad
v=\rho-e>e>0,
\]

and

\[
a=t+v.
\]

Let \(\omega\) be the bi-infinite \(t\)-periodic extension of \(C\), and define

\[
c_i=\omega(h-b+i).
\]

The block \(c_0\cdots c_{b-1}\) is the suffix occurrence of \(B\).

For \(0\le i<j\), prefix-suffix equality gives

\[
c_i=c_{i+e}.
\]

Therefore

\[
I=[0,j+e)
\]

has period \(e\).

For \(j\le i<b\), one obtains

\[
c_i=c_{i-v}.
\]

Therefore

\[
J=[j-v,b)
\]

has period \(v\).

The overlap

\[
I\cap J=[j-v,j+e)
\]

has length

\[
e+v=\rho.
\]

Let

\[
g_1=\gcd(e,v).
\]

Fine–Wilf gives period \(g_1\) on the overlap. Since the overlap is long enough relative to both \(e\) and \(v\), the period-extension sublemma propagates period \(g_1\) through \(I\) and \(J\). Their union is \([0,b)\), so \(B\) has period \(g_1\).

The word \(B\) also has period \(t\), being a factor of \(C\). Put

\[
g=\gcd(t,g_1).
\]

Because \(|B|=t+e\) and \(g_1\mid e\), the Fine–Wilf threshold is met, so \(B\) has period \(g\). Moreover

\[
g\mid t,
\qquad
g\mid e,
\qquad
g\mid b=t+e,
\]

with \(g<b\). Thus \(B\) ends in a \(g\)-square.

This completes the natural-language proof. It should still receive an independent formal index audit before being load-bearing.

---

## 22. External later-cube branch: rigid normal forms

Assume the later \(r\)-cube begins before \(YBT\), so

\[
b+j\le r-\gcd(r,P)-1<r.
\]

Deleting the appended suffix \(BT\) from the \(r\)-cube leaves an \(r\)-periodic suffix at \(G=LR^2\) of length greater than \(2r\). Hence \(G\) already has an \(r\)-square suffix. Since its curling number is \(2\) with shortest square period \(q\),

\[
\boxed{q\le r<P.}
\]

The branch splits exactly into \(r=q\) and \(q<r<P\).

### 22.1 Equal period: \(r=q\)

The later state \(F\) ends in a \(q\)-cube, while \(G\) ends in \(R^2\). Since \(|BT|<q\), the appended word must be the corresponding prefix of the next \(R\):

\[
\boxed{BT=R[0:b+j].} \tag{22.1}
\]

Therefore \(B\) is both a prefix and suffix of \(R\):

\[
\boxed{B\text{ is a border of }R.} \tag{22.2}
\]

The remaining letters give

\[
\boxed{R[0:j]=R[b:b+j].} \tag{22.3}
\]

The border of length \(b\) gives \(R\) period \(q-b\). Since \(\operatorname{cn}(R)=1\), this period exceeds \(q/2\), so

\[
\boxed{b<\frac q2.} \tag{22.4}
\]

Moving the later \(q\)-cube back by \(P=q+b\) leaves at the early endpoint a \(q\)-periodic suffix of length

\[
2q-b.
\]

This overlaps the canonical early \(p\)-cube. With \(d=\gcd(p,q)\), Fine–Wilf minimality forces

\[
\boxed{
\min(3p,2q-b)<p+q-d.
} \tag{22.5}
\]

Equivalently:

\[
3p\le2q-b
\quad\Longrightarrow\quad
2p<q-d, \tag{22.6}
\]

while

\[
3p>2q-b
\quad\Longrightarrow\quad
p>q-b+d. \tag{22.7}
\]

The Border–conjugate lemma closes this cell once the early cube is shown to impose any period

\[
0<t<b
\]

on \(UT\).

### 22.2 Unequal period: \(q<r<P\)

Put

\[
c=r-q.
\]

At \(G\), an \(r\)-square and the \(q\)-square \(R^2\) share an endpoint. Writing the length-\(r\) root as \(KR\), with \(|K|=c\), comparison of the last \(2q\) symbols gives

\[
R[c:q]K=R.
\]

Hence

\[
\boxed{R\text{ has period }c,} \tag{22.8}
\]

and

\[
\boxed{K=R[q-c:q].} \tag{22.9}
\]

Since \(\operatorname{cn}(R)=1\),

\[
\boxed{c>\frac q2.} \tag{22.10}
\]

Because \(r=q+c<P=q+b\),

\[
\boxed{c<b.} \tag{22.11}
\]

Thus

\[
\boxed{\frac q2<c<b,} \tag{22.12}
\]

so this branch forces \(b>q/2\), complementary to the equal-period branch.

Put

\[
\delta=b-c=P-r>0.
\]

The \(r\)-periodic continuation after \(G\) begins with \(KR\), and \(BT\) is its prefix. Therefore

\[
\boxed{B=K R[0:\delta],} \tag{22.13}
\]

\[
\boxed{T=R[\delta:\delta+j],} \tag{22.14}
\]

and hence

\[
\boxed{R[0:j]=R[\delta:\delta+j].} \tag{22.15}
\]

If \(e=\gcd(r,P)\), the external-cube inequality becomes

\[
\boxed{\delta+j\le q-e-1.} \tag{22.16}
\]

This is the exact surviving word-equation cell.

---

## 23. Current immediate open cells

The bridge-promotion lemma is not yet complete. The remaining work inside the immediate promotion wall is:

### Cell A: external later cube with \(r=q\)

Known:

\[
b<q/2,
\]

\(B\) is a border of \(R\),

\[
R[0:j]=R[b:b+j],
\]

and the early period \(p\) satisfies one of the narrow inequalities (22.6) or (22.7).

Needed:

- extract a period \(t<b\) on the conjugate \(UT\), allowing the Border–conjugate lemma to force a square suffix; or
- directly force a cube in \(R^2T\); or
- force an intermediate canonical period at least \(P\) using actual generation of \(U\).

### Cell B: external later cube with \(q<r<P\)

Known:

\[
q/2<c<b,
\qquad
R\text{ has period }c,
\]

\[
B=\operatorname{suf}_c(R)R[0:\delta],
\]

\[
R[0:j]=R[\delta:\delta+j],
\]

and

\[
\delta+j\le q-\gcd(r,P)-1.
\]

Needed:

- combine the long period \(c\), short prefix shift \(\delta\), and the fact that the same block \(U\) is actually generated twice;
- derive a forbidden smaller power in \(R\), a cube in \(R^2T\), or a period at least \(P\).

### Cell C: internal later cube

Known:

\[
2r\le P-
\gcd(r,P)-1.
\]

Needed:

- exploit that the later cube lies wholly in the \(P\)-periodic suffix \(YBT\), yet the endpoint symbol is generated from actual orbit context;
- combine with the early external cube and the generated conjugate \(UBT\);
- rule out all subrecord \(r\).

Once Cells A–C are closed, the corrected Two-External-Cubes Lemma follows, then every \(3\)-position promotes, and the bridge-promotion lemma is complete.

---

# Part D. Consolidated dependency graph

## 24. Local square-chain route

\[
\begin{array}{c}
\text{record-square bridge structure}\\
\Downarrow\\
\text{every 2-position promotes}\\
\Downarrow\\
\text{Generated Two-Cube Synchronization}\\
\Downarrow\\
\text{every 3-position promotes}\\
\Downarrow\\
\text{bridge-promotion lemma}\\
\Downarrow\\
\text{replay stability + first return to }R^2\\
\Downarrow\\
q_2\le q_1\text{ (preferably }R_2=R_1\text{)}\\
\Downarrow\\
\alpha_i=2q_i-P_i\text{ strictly descends}\\
\Downarrow\\
\text{no infinite square-record-only chain.}
\end{array}
\]

## 25. Global route

\[
\begin{array}{c}
\text{counterexample reductions}\\
\Downarrow\\
K\in\{2,3\}\text{ at strict record scales}\\
\Downarrow\\
\text{record cubes autonomous; square chains finite}\\
\Downarrow\\
\text{record-cube recurrence}\\
\Downarrow\\
\text{eventual context import or sealed autonomous power tail}\\
\Downarrow\\
\text{first import gives larger cube farther left}\\
\Downarrow\\
\text{frontier descent contradiction,}
\end{array}
\]

provided one proves autonomous exact-power termination and audits the external local-period theorem.

---

## 26. Master status table

| Item | Current status |
|---|---|
| New-symbol reset | PROVED-NL |
| Finite recycled alphabet | PROVED-NL |
| No ultimately periodic counterexample tail | PROVED-NL |
| Unbounded canonical periods | PROVED-NL |
| High-symbol root constraint | PROVED-NL; endpoint audit advised |
| Infinitely many generated \(2\)'s | CONDITIONAL on external local-period theorem |
| Adjacent transition gap | PROVED-NL; index audit advised |
| Master record-scale dichotomy | PROVED-NL; endpoint audit advised |
| Strict record exponents only \(2,3\) | CONDITIONAL |
| Record cubes autonomous | PROVED-NL; maximality/deletion audit advised |
| Record-square root has curling number \(1\) | PROVED-NL |
| Record-square robustness | PROVED-NL |
| Exact bridge form \(Y=BAB\) | PROVED-NL |
| Square scale bound \(P<2R_{\mathrm{prev}}\) | PROVED-NL |
| Old-scale witness cannot cross completed cube edge | PROVED-NL |
| Corrected first crossing gives larger cube farther left | PROVED-NL under stated hypotheses |
| Universal bridge crossing | REFUTED |
| Unconditional pairwise cube-edge descent | REFUTED |
| Generated \(R^2\) alone implies promotion | REFUTED by \(D=223222,R=322232\) |
| Every \(2\)-position promotes | PROVED-NL |
| First failure must be \(3\to2\) | PROVED-NL |
| Early cube: \(p\ne q\), \(j<p-\gcd(p,q)\) | PROVED-NL |
| Later cube internal/external dichotomy | PROVED-NL |
| Border–conjugate short-period lemma | PROVISIONAL-NL; independent audit required |
| External later-cube normal forms | PROVISIONAL-NL; derived in Part 3 |
| Generated Two-Cube Synchronization | OPEN, immediate wall |
| Full bridge-promotion lemma | OPEN |
| Conditional replay stability | PROVISIONAL |
| Old-bridge first return | OPEN |
| Consecutive square bridge monotonicity \(q_2\le q_1\) | OPEN |
| Infinite square-record-only chain impossible | would follow from route above |
| Autonomous exact-power termination | OPEN, final global wall |
| Full Curling Number Conjecture | OPEN |

---

## 27. Exact computational discipline and calibration

Every code path used for research must maximize over every suffix block length and retain the shortest period among maximizing witnesses. The preserved implementations use a Z-function on the reversed word.

Mandatory calibration targets, interpreted as total length immediately before the first \(1\), are:

- seed `322` gives \(5\);
- seed `23222323` gives \(66\);
- seed `2322322323222323223223` gives \(142\).

Any program disagreeing with these values is invalid for research conclusions.

### Preserved exact outputs

- `replay_local_promo2.out`:
  `valid=2286 strict=1536 promotion=1536 non=0 sgtq=0`
- `audit_bridge_promotion.out`:
  `squares=9722 promotion=9722 non=0 kinds=0`
- Re-run of `audit_all_square_replay.cpp` through binary seed length \(18\):
  `squares=9722 tested=9722 fullmatch=9722 mismatch=0 terminalmis=0 newrecordmis=0 kinds=0`
- `verify_part3_examples.py` calibrates and reproduces both the generated-\(R^2\) impostor and the static two-cube impostor.

These outputs strongly support promotion and replay, but they do not replace the missing synchronization proof.

---

# Part E. Instructions for the next Codex/reasoning agent

## 28. Immediate mission

Do not restart from the conjecture statement. Start from Section 23.

The next goal is:

> Close Cells A, B, and C of the Generated Two-Cube Synchronization Lemma, then derive the full bridge-promotion lemma.

Prioritize actual generation of \(U\). Static Fine–Wilf geometry has already been pushed close to its limit and admits impostors.

## 29. Required proof discipline

For every claimed curling number:

1. maximize over every suffix period;
2. retain the shortest maximizing period;
3. distinguish a displayed lower-bound power from actual maximality;
4. retain whether each copy was generated or preloaded.

For every Fine–Wilf use, state:

1. the exact interval;
2. its length;
3. both periods;
4. the threshold \(p+q-\gcd(p,q)\);
5. what proper period is obtained;
6. why that period contradicts primitivity, robustness, canonical minimality, or an actual curling number.

Never use “the remaining cases are similar.” The remaining cases are precisely where this project has repeatedly found counterexamples.

## 30. Suggested attack program

1. Encode the Part 3 variables \((q,b,j,p,r,c,\delta)\) and all proved inequalities in a symbolic search script.
2. Enumerate small satisfying integer cells before word enumeration. Identify which inequality becomes tight in actual generated record-square examples.
3. For each surviving cell, enumerate primitive binary \(R\), compatible \(B,T\), and left contexts \(L\), but require both actual generation windows.
4. Extract invariants of the generated period sequence while appending \(U\). In particular, compare canonical witness starts in the two parallel windows.
5. Attempt an induction on the position inside \(U\): either canonical periods agree, or the first mismatch creates a period at least \(P\).
6. In Cell A, target a short period \(t<b\) on \(UT\), then invoke the Border–conjugate lemma after independently auditing it.
7. In Cell B, combine the \(c\)-periodicity of \(R\) with the \(\delta\)-shift equality and the generation of \(U\). Search for a forced Fine–Wilf interval spanning at least \(c+\delta-\gcd(c,\delta)\).
8. In Cell C, classify whether the internal \(r\)-cube is contained in \(Y\), crosses the \(Y|B\) cut, or crosses the \(B|T\) cut. Do not merge these cases without proving equivalence.
9. Once promotion is proved, audit replay stability, prove first return, and derive \(q_2\le q_1\).
10. Only then return to autonomous exact-power termination.

## 31. Routes not to reopen unchanged

- total-gcd equality-graph connectivity;
- universal bridge crossing;
- unconditional pairwise cube-edge descent;
- static border geometry without deterministic generation;
- generated \(R^2\) alone implying promotion;
- bounded promotion-necklace lengths;
- predecessor isolation in the restricted finite-memory map.

## 32. Expected output from the next agent

The next agent should produce all of:

1. an updated proof ledger with explicit statuses;
2. executable calibrated verification for any numeric example;
3. a full proof or a concrete counterexample for Generated Two-Cube Synchronization;
4. if successful, a complete proof of bridge promotion;
5. an adversarial audit listing every generation and endpoint hypothesis used;
6. no claim that the full Curling Number Conjecture follows until autonomous exact-power termination is also solved.

---

# Part F. Source and artifact inventory

The downloadable ZIP contains this mega-ledger plus:

- the 2026-07-26 full 1,381-line handoff;
- earlier proof/research ledgers;
- frontier-descent memo;
- consecutive-square monotonicity checkpoint;
- exact C++ and Python audit code;
- exact output files;
- raw autonomous-square report;
- the original research prompt PDF;
- a fresh verifier for the Part 3 counterexamples;
- a Codex continuation prompt and machine-readable project status.

The remainder of this file appends the major textual and code sources verbatim so the ledger remains useful even when separated from the ZIP.

---

# Verbatim appendices

These appendices are preserved source material. Earlier statements may be superseded by the canonical sections above.

---

# Appendix A. 2026-07-26 full handoff ledger (historical baseline)

**Source file:** `Curling_Number_Conjecture_Full_Handoff_Ledger_2026-07-26.md`

~~~~markdown
# Curling Number Conjecture — Full Research Handoff Ledger

**Project:** Jerry (Yuze) Li / ChatGPT collaborative attack  
**Handoff date:** 2026-07-26  
**Intended recipient:** A fresh high-reasoning mathematical agent continuing the proof/disproof attempt  
**Status:** **NO COMPLETE PROOF OR COUNTEREXAMPLE YET**

---

## 0. Read this first

This document consolidates the strongest current reductions, proof ideas, computations, failed strengthenings, and exact remaining walls from a long research conversation.

The project has made substantial structural progress, but several statements still require formal endpoint/maximality audits, and one major ingredient depends on the exact applicability of an external local-period theorem. Do **not** silently promote a computational observation or a plausible overlap argument to a theorem.

The current immediate local target is the **bridge-promotion lemma** for a generated strict record square. Proving it should close the possibility of an infinite chain of autonomous strict record squares by forcing bridge-period monotonicity.

However, that would still not by itself prove the full Curling Number Conjecture. The final global obstruction is an infinite **sealed autonomous power orbit**, especially an autonomous hierarchy of record cubes that never requests context to its left.

The correct global finish line is:

> **Autonomous power termination.**  
> No exact binary square or cube seed has an infinite orbit whose curling numbers remain in \(\{2,3\}\).

A counterexample to this statement would disprove the conjecture. A proof, together with the reductions below and the audited external theorem, would finish the binary hard core and potentially the full conjecture.

---

# Part I. Problem and conventions

## 1. Curling number

For a finite nonempty sequence \(S\), its curling number is

\[
\operatorname{cn}(S)
=
\max\left\{
k\ge 1:
S=XY^k
\text{ for some nonempty }Y
\right\}.
\]

The prefix \(X\) may be empty. If several roots \(Y\) attain the maximal exponent, choose one with the shortest length.

The deterministic orbit is

\[
S_{n+1}=S_n\,\operatorname{cn}(S_n).
\]

The Curling Number Conjecture states:

> Every finite nonempty integer sequence eventually reaches a prefix of curling number \(1\).

## 2. Canonical witness data

At a prefix \(S\) of length \(n\), write

\[
k=\operatorname{cn}(S),
\qquad
p=\text{shortest period attaining }k.
\]

The canonical power suffix occupies

\[
[n-kp,n).
\]

Define its canonical witness start by

\[
s(S)=n-kp.
\]

A **strict record period** is a shortest maximizing period \(p\) larger than every earlier shortest maximizing period in the orbit.

A strict record witness is written

\[
S=XY^K,
\qquad
|Y|=P,
\]

with \(P\) the new record period. Since the witness period is chosen shortest, \(Y\) is primitive.

## 3. Generated-copy qualifiers

The phrases below are not interchangeable:

- **preloaded power:** part or all of the repeated suffix already lies in the initial seed;
- **final copy generated:** the final copy of the root was appended by the curling-number orbit;
- **entire power generated:** all copies in the displayed power were generated after the chosen boundary.

Many apparent counterexamples to frontier descent or bridge monotonicity use preloaded powers. Every theorem must state precisely which generation hypothesis it needs.

---

# Part II. General counterexample reductions

## 4. Finite recycled alphabet

### Lemma A1 — new-symbol reset

If the orbit appends a value \(k\) that has never appeared earlier, then the next curling number is \(1\).

Reason: any suffix repetition ending at the new \(k\) would require a matching occurrence of \(k\) at an earlier aligned position.

### Consequence A2 — bounded outputs in a counterexample

A nonterminating orbit can append only symbols already appearing in its finite seed. Therefore its appended values are bounded.

## 5. No ultimately periodic tail

### Lemma A3

A counterexample tail cannot be ultimately periodic.

An ultimately periodic tail would create arbitrarily large suffix powers at period-aligned endpoints, forcing unbounded curling numbers, contradicting bounded appended values.

## 6. Unbounded shortest witness periods

### Lemma A4

In a counterexample, shortest maximizing witness periods are unbounded.

If exponents were bounded by \(M\) and shortest periods eventually bounded by \(P\), the next output would depend only on a finite suffix state of length at most \(MP\). Deterministic state repetition would force eventual periodicity, contradicting A3.

## 7. High-symbol root constraint

### Lemma A5

If a sufficiently late generated prefix ends in \(Y^k\), with the final copy of \(Y\) generated by the orbit, then every symbol of \(Y\) is at least \(k-1\).

The intended proof examines the orbit immediately before each symbol in the final copy is generated. At that point a conjugate of \(Y\) already occurs \(k-1\) times as a suffix, so the appended curling number cannot be below \(k-1\).

## 8. Infinitely many generated \(2\)'s

A counterexample cannot eventually have every output at least \(3\). Otherwise every sufficiently long prefix ends in a cube, and an appropriate one-sided local-period theorem at exponent threshold \(\varphi^2<3\) forces ultimate periodicity.

**Status:** externally dependent. The exact Mignosi–Restivo–Salemi theorem statement and its hypotheses must be audited from the primary source before this step is treated as fully closed.

---

# Part III. Period-transition machinery

## 9. Adjacent period transition gap

Suppose a prefix has curling number \(k\) and shortest period \(p\). After appending \(k\), suppose the new prefix has curling number \(\ell\ge2\) and shortest period \(q\). Let

\[
d=\gcd(p,q).
\]

For \(p\ne q\), Fine–Wilf overlap yields the dichotomy

\[
(\ell-1)q\le p-d
\]

or

\[
q\ge (k-1)p+d+1.
\]

In the cube-to-cube case \(k=\ell=3\),

\[
q=p,
\qquad
q<\frac p2,
\qquad\text{or}\qquad
q>2p.
\]

This is the adjacent shortest-cube-period gap.

**Status:** proved in the research ledger, but a final formal endpoint audit is still recommended.

## 10. Adjacent period increases move the canonical start left

Using

\[
s=n-kp,
\qquad
s'=n+1-\ell q,
\]

the large-period branch gives

\[
s-s'
=
\ell q-kp-1
>
0.
\]

Hence every adjacent increase in shortest maximizing period strictly moves the canonical witness start to the left.

This fact is useful for frontier descent, but it does not imply that every non-adjacent record transition moves left.

## 11. Master record-scale dichotomy

Let

\[
S=XY^K,
\qquad
|Y|=P
\]

be a strict record witness. Consider the symbol \(\ell=Y[i]\) in the final generated copy. Let \(q_i<P\) be the shortest witness period that generated this symbol, and let

\[
d_i=\gcd(P,q_i).
\]

Fine–Wilf gives

\[
(\ell-1)q_i\le P-d_i-1
\]

or

\[
(K-2)P+i\le q_i-d_i-1.
\]

This is the main local inequality used to separate the cube and square branches.

---

# Part IV. Eliminating record exponents \(K\ge4\)

## 12. Circular short-cube statement

Claim used:

> A primitive circular word of length \(P\) has a cut at which no cube of period below \(P/2\) ends.

The intended proof applies a one-sided local-period theorem to the bi-infinite periodic extension.

**Status:** externally dependent. The exact theorem statement and its applicability must be rechecked before publication.

## 13. Consequence

For a strict record power with exponent \(K\ge4\), the master record-scale dichotomy and high-symbol constraint force a short cube at every circular cut of the primitive root. This contradicts the circular short-cube statement.

Thus every strict record exponent in the binary hard core is

\[
K\in\{2,3\}.
\]

---

# Part V. Record cubes

## 14. Autonomous record cube theorem

Let

\[
S=XY^3,
\qquad
|Y|=P
\]

be a strict record cube whose final copy is generated.

For every \(0\le i<P\),

\[
\operatorname{cn}\bigl(Y^2Y[0:i]\bigr)=Y[i].
\]

Therefore

\[
Y^2\longrightarrow Y^3
\]

independently of the older left context \(X\).

This is a major proved structural result.

## 15. Promotion roots / necklaces

A primitive binary word \(Y\) satisfying

\[
\operatorname{cn}\bigl(\rho_i(Y)^2\bigr)=Y[i]
\]

at every circular cut \(i\), where \(\rho_i(Y)\) is the corresponding rotation, is called a promotion root or promotion necklace.

Every fully generated strict record cube root is a promotion root.

Computationally observed promotion lengths include

\[
1,4,13,21,90,114,621,3384,\ldots
\]

The morphism

\[
\mu(2)=2232,
\qquad
\mu(3)=322232223
\]

produces a checked family with lengths

\[
1,4,21,114,621,3384,
\]

satisfying

\[
L_{n+2}=6L_{n+1}-3L_n.
\]

General synchronization of this morphism remains unproved.

## 16. Cube frontier and first import

For a record cube ending at time \(N\), period \(P\), define its edge

\[
\lambda=N-3P.
\]

If a later witness has exponent \(k\in\{2,3\}\) and period \(q\le P\), its start is strictly to the right of \(\lambda\). Therefore no old-scale witness can later cross the completed cube edge.

Any later canonical witness beginning left of \(\lambda\) must have period \(>P\).

## 17. Corrected first-crossing theorem

Let \(\tau>N\) be the first later endpoint whose canonical witness begins left of the old cube edge \(\lambda\).

The latest corrected route shows that the earliest crossing after a sufficiently late fully generated record cube cannot be a square. It is a cube of period larger than \(P\), and its edge is strictly left of \(\lambda\).

This proves **local frontier descent once context import occurs**.

It does **not** prove that context import must eventually occur. A sealed autonomous suffix may execute internal record ladders without ever reaching left of the current frontier.


---

# Part VI. Record squares

## 18. Root curling number and robustness

Let

\[
S=XY^2,
\qquad
|Y|=P
\]

be a fully generated strict record square.

### Lemma E1

\[
\operatorname{cn}(Y)=1.
\]

If \(Y\) itself ended in a square or cube of shorter period, the completed \(Y^2\) would have a maximizing square witness below \(P\), contradicting record minimality.

### Lemma E2 — robust suffix property

No proper suffix of \(Y^2\) has curling number at least \(2\).

In particular, every proper suffix relevant to the bridge geometry has curling number \(1\).

This includes the useful suffix \(RBR\) described later.

## 19. Exact bridge form

Let \(q<P\) be the shortest witness period generating the first symbol of the final copy of \(Y\).

Then

\[
q>\frac P2.
\]

Write

\[
R=AB,
\qquad
|R|=q,
\qquad
|B|=P-q.
\]

Then the root has the exact form

\[
Y=BAB=BR.
\]

Also

\[
|A|=2q-P>0.
\]

The quantity

\[
\alpha=2q-P=|A|
\]

is called the bridge defect.

At the beginning of the final generated copy, the state ends in

\[
R^2.
\]

## 20. Context localization

At position \(i\) in a record-square root, an external generating witness of period \(q_i\) can occur only when

\[
i<q_i-\gcd(P,q_i).
\]

If \(R_{\mathrm{prev}}\) is the previous global record period, every position

\[
i\ge R_{\mathrm{prev}}
\]

is generated internally.

## 21. Square scale bound

The bridge period existed before the new record square, so

\[
q\le R_{\mathrm{prev}}.
\]

Since \(q>P/2\),

\[
P<2R_{\mathrm{prev}}.
\]

---

# Part VII. Disproved strengthenings and warnings

## 22. False equality-graph theorem

The conjecture that cube-equality components equal residue classes modulo the total gcd is false.

A \(P=12\) assignment with one local period \(1\) and the others period \(4\) gives two components despite total gcd \(1\).

Discard this route.

## 23. False universal bridge-crossing claim

The statement

> every intervening strict record square bridge crosses the preceding record cube edge

is false for finite terminal trajectories.

The canonical autonomous ladder contains transitions whose relevant bridges remain to the right of the old cube frontier.

## 24. False pairwise cube-edge descent

The statement

> every later surviving record cube has a smaller edge than the preceding record cube

is false without precise generation/nonterminal hypotheses.

Right-moving examples occur when the earlier cube is preloaded or not fully generated at its cube exponent.

## 25. Static bridge geometry is insufficient

Words can satisfy two putative border decompositions with \(q_2>q_1\) while their actual curling-number orbit does not realize them as consecutive generated strict record squares.

Every valid proof of bridge monotonicity must use the deterministic generation condition and actual shortest maximizing periods.

---

# Part VIII. Computed record ladders

## 26. Base and lifted ladders

A checked base ladder is

\[
4^2\to6^2\to7^2\to21^3,
\]

followed by termination through outputs such as \(3,2,1\), depending on the exact starting alignment.

A lifted ladder is

\[
114^2\to186^2\to207^2\to621^3,
\]

again followed by termination.

These are genuine renormalized structures, not counterexamples.

## 27. Square-pair census

Using exact shortest-maximizing-period computation calibrated on total pre-\(1\) lengths

\[
5,\ 66,\ 142
\]

for the standard binary benchmark seeds:

- every binary seed through length \(26\) was checked;
- \(491{,}330\) qualifying consecutive generated strict-record-square pairs were found;
- no case had \(q_2>q_1\);
- every local pair type was

\[
(P_1,q_1)=(6,4)
\longrightarrow
(P_2,q_2)=(7,4).
\]

Further audits:

- \(566{,}566\) valid primitive exact square seeds with root length at most \(20\);
- \(1{,}474{,}298\) valid primitive exact cube seeds with root length at most \(20\);
- an exact-square-root census through root length \(24\);
- \(1{,}000{,}000\) random binary seeds of lengths \(27\) through \(200\).

No violation was found.

This is evidence, not proof.

## 28. Canonical square-pair algebra

The canonical small transition has

\[
Y_1=232223,
\qquad
P_1=6,
\qquad
q_1=4,
\]

with

\[
A_1=22,
\qquad
B_1=23,
\qquad
R_1=A_1B_1=2223.
\]

The next square has

\[
Y_2=2232223,
\qquad
P_2=7,
\qquad
q_2=4,
\]

with

\[
A_2=2,
\qquad
B_2=223,
\qquad
R_2=A_2B_2=2223.
\]

Thus

\[
R_2=R_1,
\]

and more strongly,

\[
A_1=A_2^2,
\qquad
B_2=A_2B_1,
\qquad
Y_2=A_2Y_1.
\]

After the first square completes, the orbit appends exactly

\[
R_1=2223
\]

and returns to a suffix \(R_1^2\).

---

# Part IX. Bridge-period monotonicity target

## 29. Consecutive square setup

Let two consecutive autonomous, fully generated strict record squares be completed at times

\[
t_1<t_2.
\]

Write

\[
S_{t_i}=X_iY_i^2,
\qquad
|Y_i|=P_i,
\qquad
P_1<P_2.
\]

Let

\[
a_i=t_i-P_i
\]

be the start time of the final generated copy.

Let \(q_i<P_i\) be the actual shortest maximizing period at \(a_i\). Write

\[
Y_i=B_iA_iB_i,
\qquad
R_i=A_iB_i,
\qquad
q_i=|R_i|.
\]

The target is

\[
q_2\le q_1.
\]

The scale bound already gives

\[
q_2\le P_1.
\]

Thus only

\[
q_1<q_2\le P_1
\]

must be excluded.

## 30. Why monotonicity closes infinite square chains

Define

\[
\alpha_i=2q_i-P_i=|A_i|>0.
\]

If \(q_2\le q_1\), then

\[
\alpha_2-\alpha_1
=
2(q_2-q_1)-(P_2-P_1)
<
0.
\]

Thus the positive integer bridge defect strictly decreases along consecutive autonomous square records.

Therefore an infinite square-record-only chain is impossible.

This would establish record-cube recurrence inside a hypothetical infinite binary \(2/3\) orbit.

---

# Part X. First-return and replay framework

## 31. Old-bridge persistence target

At the start \(a_2\) of the final copy of the second square, it would suffice to prove

\[
S_{a_2}\text{ ends in }R_1^2
\]

and

\[
\operatorname{cn}(S_{a_2})=2.
\]

Then period \(q_1\) is a maximizing square witness at \(a_2\). Since \(q_2\) is the shortest maximizing period there,

\[
q_2\le q_1.
\]

## 32. Stronger first-return lemma

The computationally suggested stronger statement is:

> If the next strict record after a generated record square \(Y^2\) is another generated square, rather than a cube or termination, then the orbit appends the old bridge root \(R\), returns to a suffix \(R^2\) after exactly \(q=|R|\) steps, and the returned state has curling number \(2\).

This gives

\[
R_2=R_1,
\qquad
q_2=q_1,
\qquad
\alpha_2<\alpha_1.
\]

## 33. Replay notation

For one record square, write

\[
R=AB,
\qquad
Y=BAB=BR,
\]

with

\[
q=|R|,
\qquad
P=|Y|.
\]

Let \(L\) denote the left context before the bridge state \(R^2\).

During generation of the final copy of \(Y\), define

\[
E_j=L\,R^2B\,R[0:j],
\qquad
0\le j\le q.
\]

Generation of the record square means

\[
\operatorname{cn}(E_j)=R[j],
\qquad
0\le j<q.
\]

At \(j=q\),

\[
E_q=L\,R^2BR.
\]

Using

\[
R^2Y=R^2BR=AY^2,
\]

this is the completed record square.

Define proposed replay states

\[
F_j=L\,R^2BR\,R[0:j].
\]

If

\[
\operatorname{cn}(F_j)=R[j]
\]

for all \(j<q\), then the completed square appends \(R\) and returns to a suffix \(R^2\).


---

# Part XI. First replay mismatch analysis

## 34. Exact first-mismatch geometry

Suppose \(j\) is the first replay index where

\[
\operatorname{cn}(F_j)\ne R[j].
\]

Write

\[
T=R[0:j],
\qquad
R=TU.
\]

Because every earlier replay symbol matched, the orbit travelled from \(E_j\) to \(F_j\) by generating the conjugate block

\[
UT.
\]

Define the common suffix

\[
W_j=B\,R[0:j].
\]

Then

\[
E_j=L\,R^2W_j,
\]

while

\[
F_j=L\,R^2BA\,W_j.
\]

The two words share the suffix \(W_j\), of length

\[
|W_j|=|B|+j<P.
\]

In a binary \(2/3\) orbit, a nonterminal mismatch is a \(2\leftrightarrow3\) discrepancy. Any distinguishing cube must cross the boundary immediately before \(W_j\); otherwise it would occur in both words.

If its period is \(p\),

\[
3p>|W_j|=|B|+j.
\]

Thus every first replay failure is reduced to a single crossing cube.

## 35. Forced \(q\)-square in the later replay phase

Let

\[
\alpha=|A|=2q-P.
\]

For every

\[
j\ge\alpha,
\]

the state \(F_j\) ends in

\[
\bigl(R[j:q]R[0:j]\bigr)^2,
\]

a square of period \(q\).

Hence

\[
\operatorname{cn}(F_j)\ge2
\qquad
(j\ge\alpha).
\]

After the defect block \(A\) is crossed, output \(1\) is impossible. Only cube discrepancies remain.

## 36. Useful robust suffix

Since

\[
Y^2=B\,RBR,
\]

the word

\[
RBR
\]

is a proper suffix of \(Y^2\).

By record-square robustness,

\[
\operatorname{cn}(RBR)=1.
\]

This observation emerged during the final promotion-lemma attack and may be load-bearing.

---

# Part XII. Conditional replay-stability result

## 37. Promotion-root hypothesis

Suppose the bridge root \(R\) is itself a promotion root in the relevant linear sense:

\[
\operatorname{cn}\bigl(R^2R[0:j]\bigr)=R[j],
\qquad
0\le j<q.
\]

Under this assumption, the first replay mismatch can be excluded except when termination or a witness period at least \(P\) occurs.

## 38. Provisional replay-stability argument

**Important status note:** The following argument was developed in the latest pass and appears structurally sound, but it has not yet received an independent full endpoint audit. A new agent should verify every containment and Fine–Wilf threshold before citing it as final.

At a first mismatch, compare a context-free promotion state with the replay state. A distinguishing cube crosses their common suffix.

Two central cases were isolated:

### Case 1: expected \(3\) falls to \(2\)

The promotion state has a cube suffix of period \(p\) absent from the replay state. The common suffix has periods \(p\) and \(q\). Because the record-square root has curling number \(1\), one derives

\[
P<2p.
\]

Fine–Wilf on the cube inside the \(q\)-periodic promotion state gives a proper divisor period

\[
d=\gcd(p,q)<p.
\]

Since \(d\mid p\), one gets \(d\le p/2\), producing too many repeats and contradicting that the promotion state's curling number is exactly \(3\).

### Case 2: expected \(2\) is upgraded to \(3\) with period \(p<P\)

Removing the appended prefix from the distinguishing cube leaves a long \(p\)-periodic suffix of \(Y^2\).

If the mismatch index \(j\le p\), this suffix has length at least \(2p\), giving a square suffix of \(Y^2\) with period \(p<P\), contradicting strict record minimality.

If \(j>p\), the common suffix is Fine–Wilf-long for periods \(p\) and \(q\), yielding a proper gcd period on \(Y\), contradicting \(\operatorname{cn}(Y)=1\).

### Consequence

Under the promotion-root hypothesis,

\[
\text{first replay mismatch}
\Longrightarrow
\operatorname{cn}\notin\{2,3\}
\quad\text{or}\quad
\text{shortest witness period}\ge P.
\]

Therefore no first mismatch can occur between consecutive strict record squares.

Again, this needs an endpoint audit before being tagged fully proved.

---

# Part XIII. Immediate current wall: the bridge-promotion lemma

## 39. Exact statement

Let

\[
R=AB,
\qquad
Y=BAB=BR,
\]

where

\[
q=|R|,
\qquad
P=|Y|,
\qquad
q>\frac P2.
\]

Suppose:

1. a full state \(LR^2\) generates \(Y\);
2. every shortest witness period used during that generation is below \(P\);
3. the completed word is a strict record square of shortest period \(P\).

Prove:

\[
\boxed{
\operatorname{cn}\bigl(R^2R[0:j]\bigr)=R[j]
\quad
\text{for all }0\le j<q.
}
\]

Equivalently:

> A bridge root used to generate a genuine strict record square is a promotion root.

This is the **immediate local proof wall**.

## 40. Why this is difficult

The full word \(LR^2\) and the standalone word \(R^2\) can generate different next symbols because the full word may have a maximizing witness crossing into \(L\).

At their first divergence:

- the standalone continuation is determined by internal suffix powers;
- the full continuation must use a larger curling number;
- every distinguishing maximizing witness in the full word crosses the boundary before \(R^2\).

The computation suggests the first divergence is always a same-period \(q\)-cube. For example:

- at the small scale, the divergence uses period \(q=4\);
- in the lifted hierarchy, the analogous divergence uses period \(q=114\).

The remaining proof task is to exclude a first divergence using period

\[
p\ne q
\]

unless it creates:

- termination;
- a shortest witness period at least \(P\);
- or a contradiction to strict record minimality/robustness.

Once \(p=q\), the same-period cube geometry should force the standalone continuation to be exactly \(R\).

## 41. Suggested attack coordinates

Let the first divergence between the full orbit from \(LR^2\) and the standalone orbit from \(R^2\) occur after a common generated block \(T\).

Let

\[
|T|=j.
\]

The standalone state is

\[
R^2T.
\]

The full state is

\[
LR^2T.
\]

If the full state has a distinguishing cube of period \(p\), it must cross the boundary before \(R^2T\). Therefore

\[
3p>2q+j.
\]

The first serious split should be:

1. \(p<q\);
2. \(p=q\);
3. \(q<p<P\);
4. \(p\ge P\).

Cases 1 and 3 should be attacked with Fine–Wilf plus the robust suffix condition

\[
\operatorname{cn}(RBR)=1
\]

and the fact that the actual generation of \(Y=BR\) uses only periods below \(P\).

The target conclusion is:

\[
p=q
\quad\text{or}\quad
p\ge P.
\]

Then use the same-period \(q\)-cube to identify the standalone symbol and inductively recover the entire word \(R\).

## 42. Computational evidence for promotion

Targeted checks found:

- all \(1{,}536\) locally strict generated completions in a bounded context/root search had promotion bridge roots;
- all \(9{,}722\) fully generated strict record squares from binary seeds through length \(18\) had promotion bridge roots;
- zero strict failures;
- every nonpromotion failure found was non-strict and required a generation witness period at least \(P\).

This evidence matches the exact obstruction predicted by the lemma.

---

# Part XIV. Post-return dependence

## 43. Eliminated intermediate band

After successful replay, the state again ends in \(R^2\).

Compare the full orbit with the standalone orbit from \(R^2\). If their first divergence is caused by a crossing cube of period \(p\), a provisional argument eliminates

\[
q<p<P.
\]

Writing

\[
p=q+h,
\]

one splits according to the common continuation length \(j\):

- if \(j\le h\), removing the appended continuation leaves a \(p\)-periodic suffix of the previous \(Y^2\) of length at least \(2p\), contradicting the shortest square period \(P\);
- if \(j>h\), the common suffix is Fine–Wilf-long for periods \(p,q\), producing a proper period of \(R\), contradicting primitivity.

Thus the first post-return dependence has

\[
p\le q
\quad\text{or}\quad
p\ge P.
\]

This argument also needs an endpoint audit.

## 44. Remaining post-return classification

Even after proving promotion and replay, one must still show that a first dependence with

\[
p\le q
\]

cannot later produce a new square bridge with period larger than \(q\) without first causing:

- a cube record;
- termination;
- or a witness period at least \(P\).

This is smaller than the promotion lemma and may collapse under the same-period excursion analysis.

---

# Part XV. Global-minimum power-seed reduction

## 45. Boundary-autonomy reduction

Assume an infinite binary orbit avoiding \(1\) and \(4\) exists.

For each prefix, choose its canonical witness start \(s_n\). Let \(L\) be the global minimum of these starts, attained at time \(t\).

The suffix beginning at \(L\) is an exact square or cube

\[
R^k,
\qquad
k\in\{2,3\}.
\]

All later canonical witnesses begin at or to the right of \(L\).

Deleting the prefix before \(L\) preserves every later curling number:

- every actual maximizing witness remains;
- deleting a prefix cannot create a new suffix repetition that was not already present.

Therefore:

> Any binary counterexample implies a counterexample seed that is an exact square or cube and whose future orbit never requires context to the left of that initial power.

This is the strongest clean global reduction currently available.

---

# Part XVI. Final global wall

## 46. Autonomous power termination

The full binary-hard-core finish line is:

\[
\boxed{
\text{No exact binary square or cube seed has an infinite orbit avoiding }1\text{ and }4.
}
\]

Equivalent formulation:

> Every infinite-looking autonomous power trajectory must eventually request context across its current left boundary, terminate at \(1\), or create a curling number at least \(4\).

If it requests older context, the first-crossing machinery produces a larger cube with a strictly smaller frontier.

Repeated crossing would force an impossible infinite descent of nonnegative frontier positions.

## 47. Why square monotonicity is not the whole proof

Proving the bridge-promotion lemma should lead to

\[
q_2\le q_1
\]

for consecutive autonomous square records.

Then the bridge defect

\[
\alpha=2q-P
\]

strictly decreases, ruling out an infinite square-record-only regime.

This should imply infinitely many record cubes in a hypothetical infinite orbit.

But record cubes are autonomous, and known finite autonomous ladders can jump between cube scales before terminating.

The final unresolved possibility is:

> an infinite sealed hierarchy of autonomous cubes and finite square ladders, never using context left of its initial exact-power boundary.

That possibility must be eliminated or explicitly constructed.

---

# Part XVII. Recommended next-agent workflow

## 48. Immediate priority

Prove or disprove the bridge-promotion lemma.

Do not return to the already refuted universal bridge-crossing or unconditional cube-edge descent statements.

## 49. Required rigor discipline

For every claimed curling number:

- maximize over every suffix block length;
- retain the shortest period among maximizing witnesses;
- distinguish displayed lower-bound powers from actual maximality;
- preserve whether the relevant copy was generated or preloaded.

For every Fine–Wilf application, state:

- the exact interval;
- its length;
- both periods;
- the threshold \(p+q-\gcd(p,q)\);
- why the resulting gcd period contradicts primitivity, robustness, or shortest maximizing period.

## 50. Suggested promotion-lemma proof skeleton

At first divergence between \(LR^2\) and \(R^2\):

1. Prove the full curling number is strictly larger than the standalone one.
2. Therefore every full maximizing witness crosses the left boundary of \(R^2\).
3. Let \(p\) be the shortest such distinguishing period.
4. Show \(p<q\) contradicts the robust suffix \(RBR\) or creates a shorter square suffix of \(Y^2\).
5. Show \(q<p<P\) contradicts Fine–Wilf on a long shared suffix or creates a forbidden \(p\)-square in \(Y^2\).
6. Conclude \(p=q\) or \(p\ge P\).
7. The \(p\ge P\) branch contradicts the hypothesis that all generation periods before the new record square are below \(P\).
8. Therefore \(p=q\).
9. Use exact same-period cube geometry to determine the next standalone symbol.
10. Induct over all \(q\) positions to prove standalone generation of \(R\).

The main missing detail is Step 9: formulate the same-period geometry so it forces the correct symbol without assuming the conclusion.

## 51. After promotion

1. Audit the conditional replay-stability proof.
2. Prove first return to \(R^2\).
3. Prove \(q_2\le q_1\), preferably \(q_2=q_1\).
4. Deduce strict descent of \(\alpha=2q-P\).
5. Close the infinite square-chain branch.
6. Return to autonomous exact-power termination, focusing on sealed cube hierarchies and the morphic promotion family.

---

# Part XVIII. Reproducible computational assets

The following files were generated during the project:

- `curling_research_tools.py`
- `curling_q_monotonicity_audit.cpp`
- `Curling_q_monotonicity_checkpoint_2026-07-25.md`
- `replay_local_promo2.cpp`
- `replay_local_promo2.out`
- `audit_bridge_promotion.cpp`
- `audit_bridge_promotion.out`
- `audit_all_square_replay.cpp`
- `_tmp_autonomous_square_report.txt`
- `Curling_Number_Frontier_Descent_Memo.md`
- `curling_number_proof_ledger.md`

The exact curling-number routine uses the Z-function of the reversed word and checks every possible suffix period.

Calibration targets used:

- seed `322` reaches the first \(1\) at total length \(5\);
- seed `23222323` at total length \(66\);
- seed `2322322323222323223223` at total length \(142\).

Any implementation disagreeing with these is invalid for research conclusions.

---

# Part XIX. Status table

| Item | Status |
|---|---|
| Finite recycled alphabet | Proved |
| No ultimately periodic counterexample tail | Proved |
| Unbounded shortest witness periods | Proved |
| High-symbol root constraint | Proved |
| Infinitely many generated \(2\)'s | External theorem dependency |
| Adjacent period transition gap | Proved, endpoint audit advised |
| Strict record exponents only \(2,3\) | Conditional on audited local-period theorem |
| Record cubes autonomous | Proved, audit maximality deletion step |
| Record-square root has curling number \(1\) | Proved |
| Record-square robustness | Proved |
| Exact bridge form \(Y=BAB\) | Proved |
| Square scale bound \(P<2R_{\mathrm{prev}}\) | Proved |
| Old-scale witnesses cannot cross completed cube frontier | Proved |
| First actual context import moves frontier left | Proved in corrected cube-crossing form |
| Universal bridge-crossing | Refuted |
| Unconditional pairwise cube-edge descent | Refuted |
| \(q_2\le q_1\) for consecutive generated square records | Open |
| Old-bridge first return | Open |
| Conditional replay-stability under promotion | Provisional proof, audit required |
| Bridge-promotion lemma | **Immediate open wall** |
| Infinite autonomous square chain impossible | Follows from promotion/monotonicity route; not yet proved |
| Autonomous exact-power termination | **Final global wall** |
| Full Curling Number Conjecture | Open |

---

# Part XX. One-paragraph handoff summary

A hypothetical counterexample has bounded outputs, no periodic tail, and unbounded shortest witness periods. After an externally dependent local-period reduction, strict record exponents are only squares and cubes. Record cubes are autonomous; record squares have robust roots of the exact form \(Y=BAB\), with bridge root \(R=AB\), bridge period \(q>P/2\), and positive defect \(2q-P\). Actual first use of context across a completed cube frontier produces a larger cube strictly farther left, but finite autonomous ladders show that not every transition imports context. To rule out an infinite square-record-only regime, it is enough to prove consecutive bridge periods do not increase. Computation overwhelmingly shows the stronger inheritance \(R_2=R_1\). The local route reduces this to the **bridge-promotion lemma**: if \(LR^2\) generates the strict record-square root \(Y=BAB\) using only periods below \(P\), then standalone \(R^2\) generates \(R\). Conditional on this, a first replay mismatch appears impossible below period \(P\), yielding first return, \(q_2\le q_1\), and strict descent of the bridge defect. Even after closing squares, the final global wall is to prove **autonomous power termination**: no exact binary square/cube seed can avoid \(1\) and \(4\) forever. An explicit infinite autonomous exact-power orbit would disprove the conjecture; proving none exists would complete the frontier-descent strategy.
~~~~

---

# Appendix B. Detailed proof ledger

**Source file:** `curling_number_proof_ledger.md`

~~~~markdown
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
~~~~

---

# Appendix C. Research ledger and autonomous-cube findings

**Source file:** `curling_number_research_ledger.md`

~~~~markdown
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
~~~~

---

# Appendix D. Frontier-descent memo

**Source file:** `Curling_Number_Frontier_Descent_Memo.md`

~~~~markdown
# Curling Number Conjecture: Frontier-Descent Memo

Date: 2026-07-24
Status: research ledger; proved statements are separated from computational or conjectural statements.

## Standing binary hard-core setup

A hypothetical binary counterexample eventually has outputs only in {2,3}. For a prefix W of length n, write

- k = cn(W),
- p = the shortest period attaining k,
- s(W) = n-kp for the start of its canonical suffix power.

Witness periods are unbounded. Strict record periods can have exponent only 2 or 3, using the circular short-cube theorem and the one-sided local-period theorem of Mignosi-Restivo-Salemi.

## Previously proved record-scale normal form

### Record cubes are autonomous

For a fully generated strict record cube X Y^3, |Y|=P, every symbol of the final copy of Y is generated by a witness contained in the preceding Y^2. Hence Y^2 generates Y^3 independently of X.

### Record-square bridge theorem

For a fully generated strict record square X Y^2, |Y|=P, if the first symbol of the final copy is generated by shortest period q<P, then q>P/2. Writing R=AB with |R|=q, |B|=P-q, gives

Y = B A B.

If the first symbol is ell in {2,3}, the bridge power R^ell begins at H, the record-square edge is E, and

E-H = ell*q-P > 0.

For ell=2, R^2 Y = A Y^2. For ell=3, R^3 Y = (A B A) Y^2.

## New proved statement 1: adjacent period increases move the canonical start left

Suppose W has curling number k and shortest maximizing period p. After appending k, suppose the new prefix has curling number ell>=2 and shortest maximizing period q>p. Let d=gcd(p,q). The exact period-transition gap gives

q >= (k-1)p+d+1.

The old and new canonical starts are

s = n-kp,

s' = n+1-ell*q.

Therefore

s-s' = ell*q-kp-1 > 0.

So every adjacent increase in shortest witness period strictly decreases the canonical witness start.

## New proved statement 2: first crossing of a boundary carried by a record power

Let a record power of period P and exponent at least 2 end at c and begin at L. Let tau>c be the first later endpoint whose canonical witness begins before L. Let R be the largest shortest-witness period occurring before tau.

Then:

1. If the crossing witness at tau is a square of period Q, then Q>R. It is a strict record square.
2. If it is a cube of period Q, then Q>=R. Thus it is either a strict record cube or a cube at the current maximum scale.

Proof sketch: the latest R-record witness before tau begins at or to the right of L, so its endpoint is at least L+2R. A square with Q<=R cannot cross L at a later endpoint. A cube with Q<R would contain that earlier R-power. Fine-Wilf then supplies a proper gcd period on the entire earlier power, contradicting the canonical period/exponent there.

## New proved statement 3: geometry of a first square crossing after a record cube

Let the old record cube be X Y^3, |Y|=P, ending at c and beginning at L. Suppose the first witness to cross L is a strict record square of period Q, ending at tau. Let a=tau-Q be the beginning of its final copy.

Then:

- a<c<tau. If a>=c, the bridge witness generating the first symbol of the final copy would already begin left of L at time a, contradicting first crossing.
- Its bridge start H and square edge F satisfy H<F<L.
- The new Q-periodic square contains the old primitive P-cube. Fine-Wilf therefore forces

  Q > 2P + gcd(P,Q).

This shows that a first square crossing is a violent scale jump and imports context strictly to the left of the old cube edge.

## New proved statement 4: global-minimum power-seed reduction

Let an infinite binary orbit avoiding 1 and 4 exist. For every prefix choose its canonical witness start s_n. Let L be the global minimum of the s_n, attained at time t. The suffix beginning at L is exactly a square or cube R^k, k in {2,3}.

All later canonical witnesses begin at or to the right of L. Deleting the prefix before L therefore preserves every later curling number: every actual witness remains, and deleting a prefix cannot create a new suffix repetition. Hence R^k itself is a counterexample seed.

Therefore:

Any binary counterexample implies a binary counterexample whose starting word is an exact square or exact cube and whose future orbit never requires context to the left of that power.

This is the exact boundary-autonomy reduction.

## Corrected frontier target

The literal claim that every intervening record-square bridge crosses the preceding cube edge is false for finite terminating trajectories.

The correct statement needed for global descent is:

> Autonomous power termination. No exact binary square or cube seed can generate an infinite orbit avoiding both 1 and 4.

Equivalently, for a nonterminal record-scale transition in an arbitrary orbit, some later canonical witness must cross the old dependency boundary. The first-crossing theorem then turns that event into a strict record square bridge or a record-level cube strictly farther left.

## Computational evidence only

- All binary seeds through length 18 were checked with exact shortest-period curling computation.
- 9,722 fully generated strict record-square cases were inspected.
- No violation of the nonterminal frontier-descent pattern was found.
- The literal bridge-crossing statement has terminating counterexamples, including the finite 4-to-21 promotion hierarchy.
- Observed renormalization: 4^2 -> 6^2 -> 7^2 -> 21^3 and its mu^2 lifts, with mu(2)=2232 and mu(3)=322232223. These stages terminate and do not themselves form a counterexample.

## Exact remaining wall

The current proof has reduced the binary hard core to the autonomous-power problem. A complete solution now needs either:

1. a theorem that every exact binary square/cube seed reaches 1 or 4, likely by a recognizable square-bridge/cube renormalization descent; or
2. an explicit exact power seed whose orbit avoids 1 and 4 forever, which would disprove the conjecture.

No proof of autonomous-power termination is currently claimed.
~~~~

---

# Appendix E. Consecutive-square bridge-period checkpoint

**Source file:** `Curling_q_monotonicity_checkpoint_2026-07-25.md`

~~~~markdown
# Curling Number Conjecture: Consecutive-Square Bridge-Period Checkpoint

**Date:** 2026-07-25  
**Status:** No counterexample found. The desired inequality is not yet proved, but it has been reduced to one local first-return lemma.

## 1. Exact target

Let two consecutive strict record squares in a binary orbit be completed at times

\[
t_1<t_2,
\qquad
S_{t_i}=X_iY_i^2,
\qquad
|Y_i|=P_i,
\qquad
P_1<P_2.
\]

Assume the final copy of each root is generated by the orbit. Put

\[
a_i=t_i-P_i,
\]

so `a_i` is the time at which the final copy of `Y_i` begins. Let `q_i<P_i` be the shortest maximizing witness period at time `a_i`.

For a square bridge, the proved bridge theorem gives

\[
Y_i=B_iA_iB_i,
\qquad
R_i=A_iB_i,
\qquad
q_i=|R_i|,
\]

with

\[
|A_i|=2q_i-P_i>0,
\qquad
|B_i|=P_i-q_i.
\]

The target is

\[
\boxed{q_2\le q_1.}
\]

Since `P_1` is the previous global record when the second square forms, the scale bound already gives

\[
q_2\le P_1.
\]

Thus the only bad range is

\[
q_1<q_2\le P_1.
\]

## 2. Why this inequality would close autonomous square chains

Define the bridge defect

\[
\alpha_i:=2q_i-P_i=|A_i|>0.
\]

If `q_2 <= q_1`, then

\[
\alpha_2-\alpha_1
=2(q_2-q_1)-(P_2-P_1)<0.
\]

Hence every consecutive autonomous square-record transition strictly decreases a positive integer. An infinite record-square chain is therefore impossible.

## 3. Critical false-positive trap

A candidate `q_i` cannot be chosen from an arbitrary border decomposition of a square root. It must be the **actual shortest maximizing period at the generated final-copy start** `a_i`.

For example, a preloaded exact square can possess a border suggesting a larger `q`, but that border was never used by the orbit to generate its final copy. Counting it produces fake examples with `q_2>q_1`. These are not counterexamples to the theorem.

This distinction is load-bearing:

- preloaded square border: insufficient;
- actual generated bridge at `a_i`: required.

## 4. Reproduced exact computation

The audit program computes every suffix block length using the Z-function of the reversed word and keeps the shortest period attaining the maximum exponent.

Calibration passed on the standard binary cases:

- `322` reaches the first `1` at total pre-1 length `5`;
- `23222323` at length `66`;
- `2322322323222323223223` at length `142`.

### Exhaustive binary-seed census

Across every binary seed of lengths `1` through `26`:

- qualifying consecutive generated strict-record-square pairs: **491,330**;
- violations `q_2>q_1`: **0**;
- distinct local transition types: **1**;

namely

\[
(P_1,q_1)=(6,4)
\longrightarrow
(P_2,q_2)=(7,4).
\]

### Exact power seeds

For every primitive exact square seed with root length at most `20`:

- valid exact square seeds audited: **566,566**;
- generated consecutive square-record pairs: one local type only;
- violations: **0**.

For every primitive exact cube seed with root length at most `20`:

- valid exact cube seeds audited: **1,474,298**;
- generated consecutive square-record pairs: **0**.

An additional exact-square-root census through root length `24` found no new transition type.

### Random stress tests

One completed random audit of **1,000,000** binary seeds of lengths `27` through `200` found **3,583** qualifying pairs, all again `6/4 -> 7/4`. A later larger run inspected millions more seeds before its execution budget ended and found no second transition type.

These are computational checks, not a proof.

## 5. Canonical transition

A representative orbit is generated from the seed

`22322232`.

The consecutive square records are

\[
Y_1=232223,
\qquad
P_1=6,
\qquad
q_1=4,
\]

with

\[
A_1=22,
\qquad
B_1=23,
\qquad
R_1=A_1B_1=2223,
\]

followed by

\[
Y_2=2232223,
\qquad
P_2=7,
\qquad
q_2=4,
\]

with

\[
A_2=2,
\qquad
B_2=223,
\qquad
R_2=A_2B_2=2223.
\]

Thus

\[
R_2=R_1,
\qquad
A_1=A_2^2,
\qquad
B_2=A_2B_1,
\qquad
Y_2=A_2Y_1.
\]

After the first square is completed, the next four appended symbols are exactly

\[
R_1=2223.
\]

At that point the suffix `R_1^2` has returned, and this is precisely the start of the final copy of the second square.

## 6. Static geometry alone is insufficient

There exist words satisfying the border equations for two putative square bridges with `q_2>q_1`. Their actual curling-number trajectories do not realize those two words as consecutive generated record squares.

Therefore no proof based only on

\[
Y_i=B_iA_iB_i
\]

and Fine--Wilf overlap can be sufficient. The orbit-generation condition must be used.

## 7. Exact reduction to one local lemma

At time `a_2`, if the current prefix has suffix `R_1^2` and has curling number `2`, then period `q_1=|R_1|` is a maximizing square witness. Since `q_2` is the shortest maximizing witness period at `a_2`, immediately

\[
q_2\le q_1.
\]

Therefore it is enough to prove the following.

### Old-bridge persistence lemma

Let `Y_1^2` and `Y_2^2` be consecutive autonomous, generated strict record squares. At the start `a_2` of the final copy of `Y_2`,

\[
S_{a_2}\text{ ends in }R_1^2
\]

and

\[
\operatorname{cn}(S_{a_2})=2.
\]

This lemma implies the desired monotonicity in one line.

## 8. Stronger form suggested by every computed pair

Every computed pair satisfies the sharper statement

\[
a_2=t_1+q_1,
\]

and the generated block between these times is exactly

\[
S[t_1,a_2)=R_1.
\]

Since `S_{t_1}` already ends in `R_1`, the state at `a_2` ends in `R_1^2`. Its curling number is `2`, and the second bridge root is exactly inherited:

\[
R_2=R_1.
\]

This motivates the strongest clean local target.

### Square-to-square first-return lemma

If the next strict record after a generated record square `Y_1^2` is another generated square rather than a cube or termination, then the orbit appends the old bridge root `R_1`, returns to `R_1^2` after exactly `q_1` steps, and the returned state has curling number `2`.

The implications are

\[
\text{first-return lemma}
\Longrightarrow R_2=R_1
\Longrightarrow q_2=q_1
\Longrightarrow \alpha_2<\alpha_1.
\]

## 9. Remaining proof obligation

The unresolved content is now only the no-delay/return dichotomy:

> Starting from the completed first record square, prove that failure to return to `R_1^2` as the next square bridge forces either a strict record cube or an output outside `{2,3}` before a later strict record square can form.

This is strictly smaller than the original monotonicity claim. It is a local statement about the finite interval between one square endpoint and the next record event.

## 10. Reproducible audit code

The accompanying C++ file is `curling_q_monotonicity_audit.cpp`.

Build:

```bash
g++ -O3 -std=c++20 curling_q_monotonicity_audit.cpp -o curling_q_monotonicity_audit
```

Examples:

```bash
./curling_q_monotonicity_audit all-seeds 12 300 1
./curling_q_monotonicity_audit power 20 2 600 1
./curling_q_monotonicity_audit power 20 3 600 1
```

The program stops immediately and prints the seed if it finds `q_2>q_1`.
~~~~

---

# Appendix F. Older first-crossing proof ledger

**Source file:** `Curling_Number_Proof_Ledger.md`

~~~~markdown
# Curling Number Conjecture Proof Ledger


## 2026-07-24: First-crossing and frontier correction

### DISPROVED: literal universal bridge-crossing claim

The statement “every intervening strict record square has an imported witness crossing the left edge of the preceding record cube” is false for finite terminating trajectories.

Exact calibrated examples include:

- the canonical \(4^3\to 21^3\) transition, where an intervening period-\(7\) record square has bridge start \(13\) while the preceding period-\(4\) cube has edge \(0\);
- a period-\(7\) cube whose next period-\(21\) cube begins at edge \(13>0\), after which the orbit terminates.

Therefore any valid descent theorem must include a nonterminal/infinite-orbit hypothesis or a terminal alternative.

### PROVED: first-crossing record theorem

Use half-open intervals. At a prefix of length \(n\), with curling number \(k\) and shortest maximizing period \(p\), call
\[
s=n-kp
\]
the canonical witness start.

Let a current strict record cube end at \(c\), have period \(P\), and have left edge
\[
L=c-3P.
\]
Let \(\tau>c\) be the first later endpoint whose canonical witness start is \(<L\). Let \(R\) be the largest shortest-witness period attained before \(\tau\).

Then:

1. If the witness at \(\tau\) is a square of period \(Q\), then \(Q>R\). Hence it is a strict record square.
2. If the witness at \(\tau\) is a cube of period \(Q\), then \(Q\ge R\). Thus it is either a strict record cube, or a cube at the current record scale, and in either case its cube edge is \(<L\).

Proof of (1): the endpoint \(r\) at which period \(R\) was last made a record has canonical start at least \(L\), so \(r\ge L+2R\). Since \(\tau>r\), a square of period \(Q\le R\) at \(\tau\) would start at
\[
\tau-2Q>L,
\]
contrary to the definition of \(\tau\).

Proof of (2): if \(Q<R\), the \(Q\)-cube at \(\tau\) crosses \(L\) and contains the earlier record-\(R\) power interval. That earlier factor then has periods \(R\) and \(Q\). Fine--Wilf gives period \(\gcd(R,Q)<R\) on enough of the suffix to produce a shorter maximizing witness, contradicting the canonical minimality of \(R\).

### PROVED: straddling bridge theorem at first square crossing

If the first crossing at \(\tau\) is a fully generated strict record square of period \(Q\), let its final copy begin at
\[
a=\tau-Q.
\]
Let its first symbol \(\ell\in\{2,3\}\) be generated by shortest witness period \(q<Q\), and let
\[
H=a-\ell q
\]
be that bridge witness start. Let the square edge be
\[
F=\tau-2Q=a-Q.
\]

Then:

\[
H<F<L.
\]

Indeed, the bridge theorem gives \(\ell q>Q\), so \(H<F\), and the square itself is the first witness crossing \(L\), so \(F<L\).

Moreover,
\[
a<c<\tau.
\]
If \(a\ge c\), the bridge crossing \(H<L\) would already occur at time \(a\in[c,\tau)\), contradicting the minimality of \(\tau\). Thus the new square straddles the old cube endpoint.

The \(Q\)-periodic square interval contains the old primitive \(P\)-cube. Fine--Wilf therefore yields the strict scale separation
\[
Q>2P+\gcd(P,Q).
\]
Otherwise the length-\(3P\) old cube would have both periods \(P,Q\) on a Fine--Wilf-long overlap, forcing a proper gcd-period and contradicting primitivity/minimality of \(P\).

### CHECKED(18): bridge-to-next-cube frontier

Across all binary seeds of lengths at most \(18\), comprising \(9{,}722\) fully generated strict record-square cases, every case with a later strict record cube satisfied:
\[
\text{next cube edge}<H,
\]
where \(H\) is the bridge start of the last intervening fully generated strict record square.

Random larger stress tests found no violation.

This is computational evidence only.

### Corrected frontier target

The valid local target is:

> If a transition after a strict record cube never reaches left of that cube's edge, then the transition is terminal (reaches \(1\) or \(4\)); equivalently, every nonterminal transition to a later strict record cube must move the dependency frontier strictly left.

A useful stronger form suggested by all checked data is:

> For a fully generated strict record square with bridge start \(H\), the next strict record cube, if the orbit remains nonterminal, has left edge \(<H\).

The literal unconditional claim is false; the terminal alternative is essential.

### Remaining exact wall

The missing step is an autonomous-contained-transition theorem:

> Starting at a record cube edge \(L\), if all later canonical witnesses remain in \([L,\infty)\), then the binary orbit cannot remain forever in \(\{2,3\}\).

This is the precise statement needed to turn first-crossing descent into a well-founded left-frontier argument.
~~~~

---

# Appendix G. Older compact research ledger

**Source file:** `Curling_Number_Research_Ledger(1)(1).md`

~~~~markdown
# Curling Number Conjecture Research Ledger

## Status

-   **No complete proof or counterexample yet.**
-   This is a handoff document containing our strongest reductions and
    current frontier.

## Core reductions

-   Shifted analysis to **strict record witness periods** `S = X Y^K`.
-   Derived adjacent shortest cube periods are either equal or differ by
    **more than a factor of two** (Fine--Wilf overlap).
-   Eliminated the `K >= 4` record branch via the circular short-cube
    route (subject to the cited local-period theorem being used
    correctly and fully audited).

## Binary hard core

Remaining record exponents: - `K = 2` - `K = 3`

Everything else has effectively been pushed aside.

## Record cube theorem

For `K = 3`: - The entire record cube is generated internally. -
`Y^2 -> Y^3` is autonomous. - No older left context is needed.

## Record square bridge theorem

For `K = 2`: - Every record square root has structure

    Y = B A B

with

    |AB| = q > P/2.

Squares are the only mechanism importing old left-context.

## Context localization

Only an initial prefix of a record square can depend on older history.
The remainder of the square is autonomous.

## Renormalization hierarchy

Observed:

    4² -> 6² -> 7² -> 21³

which lifts to

    114² -> 186² -> 207² -> 621³

This is a genuine recursive structure but **not** yet a counterexample
because every larger stage still requires additional left boundary
information.

## Remaining conjectures

### Conjecture A

Every infinite surviving binary orbit contains infinitely many strict
record cubes.

### Conjecture B

For consecutive surviving record cubes

    X1 Y1³
    X2 Y2³

prove

    |X2| < |X1|.

This would immediately force infinite descent.

## Current finish line

Prove:

> Every record square bridge necessarily imports a witness that crosses
> the previous record cube's left boundary.

If true:

1.  every surviving record cube moves the frontier left,
2.  infinitely many record cubes imply an infinite strictly decreasing
    frontier,
3.  contradiction,
4.  Curling Number Conjecture follows (for the binary core).

## Important corrections

-   A proposed gcd-connectivity theorem for the equality graph was found
    false (counterexample at P=12) and discarded.
-   Every reduction must be adversarially audited before use.
~~~~

---

# Appendix H. Exact Python research tools

**Source file:** `curling_research_tools.py`

~~~~python
"""Exact tools used in the Curling Number Conjecture research ledger.

Convention: an orbit stops at the first prefix whose curling number is not in
{2, 3}; for calibration examples this is the first 1. All suffix block lengths
are checked via the Z-function of the reversed word.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Sequence


def z_function(s: Sequence[int]) -> list[int]:
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def curling_number_and_shortest_period(seq: Sequence[int]) -> tuple[int, int]:
    """Return (curling number, shortest period attaining it)."""
    if not seq:
        raise ValueError("The curling number is defined only for nonempty sequences")
    n = len(seq)
    rev = list(reversed(seq))
    z = z_function(rev)
    best_k = 1
    best_p = n
    for p in range(1, n):
        k = 1 + z[p] // p
        if k > best_k or (k == best_k and p < best_p):
            best_k, best_p = k, p
    return best_k, best_p


@dataclass(frozen=True)
class Event:
    length: int
    exponent: int
    period: int
    edge: int
    strict_period_record: bool


def trace_binary_orbit(seed: Sequence[int], max_steps: int = 100_000) -> list[Event]:
    """Trace until the first curling number outside {2,3}, or max_steps."""
    if not seed:
        raise ValueError("seed must be nonempty")
    s = list(seed)
    max_period = 0
    events: list[Event] = []
    for _ in range(max_steps + 1):
        k, p = curling_number_and_shortest_period(s)
        record = p > max_period
        if record:
            max_period = p
        events.append(Event(len(s), k, p, len(s) - k * p, record))
        if k not in (2, 3):
            break
        s.append(k)
    return events


def total_length_before_first_one(seed: Sequence[int], max_steps: int = 100_000) -> int:
    events = trace_binary_orbit(seed, max_steps=max_steps)
    if events[-1].exponent != 1:
        raise RuntimeError("No 1 reached within max_steps")
    return events[-1].length


def digits(text: str) -> list[int]:
    return [int(ch) for ch in text.strip()]


def calibrate() -> None:
    cases = {
        "322": 5,
        "23222323": 66,
        "2322322323222323223223": 142,
    }
    for seed_text, expected in cases.items():
        actual = total_length_before_first_one(digits(seed_text))
        if actual != expected:
            raise AssertionError((seed_text, expected, actual))
    print("Calibration passed: total lengths 5, 66, 142")


if __name__ == "__main__":
    calibrate()
~~~~

---

# Appendix I. Consecutive-square monotonicity audit

**Source file:** `curling_q_monotonicity_audit.cpp`

~~~~cpp
#include <bits/stdc++.h>
using namespace std;

struct Event {
    int length;
    int exponent;
    int period;
    bool fully_generated_square;
    int bridge_period;
};

pair<int,int> curling_number_and_shortest_period(const vector<unsigned char>& s) {
    const int n = (int)s.size();
    if (n == 0) throw runtime_error("curling number requires a nonempty word");

    // Z-function of the reversed word. For a suffix period p,
    // 1 + Z[p]/p is the suffix exponent at period p.
    vector<int> z(n, 0);
    int left = 0, right = 0;
    auto rev_at = [&](int i) -> unsigned char { return s[n - 1 - i]; };
    for (int i = 1; i < n; ++i) {
        if (i < right) z[i] = min(right - i, z[i - left]);
        while (i + z[i] < n && rev_at(z[i]) == rev_at(i + z[i])) ++z[i];
        if (i + z[i] > right) {
            left = i;
            right = i + z[i];
        }
    }

    int best_k = 1;
    int best_p = n;
    for (int p = 1; p < n; ++p) {
        const int k = 1 + z[p] / p;
        if (k > best_k || (k == best_k && p < best_p)) {
            best_k = k;
            best_p = p;
        }
    }
    return {best_k, best_p};
}

vector<unsigned char> digits(const string& x) {
    vector<unsigned char> s;
    s.reserve(x.size());
    for (char c : x) {
        if (c != '2' && c != '3') throw runtime_error("binary word must use only 2 and 3");
        s.push_back((unsigned char)(c - '0'));
    }
    return s;
}

int total_length_before_first_one(vector<unsigned char> s, int max_steps = 100000) {
    for (int step = 0; step <= max_steps; ++step) {
        auto [k, p] = curling_number_and_shortest_period(s);
        if (k == 1) return (int)s.size();
        if (k != 2 && k != 3) throw runtime_error("calibration orbit hit a value other than 1,2,3");
        s.push_back((unsigned char)k);
    }
    throw runtime_error("calibration max_steps exceeded");
}

void calibrate() {
    const vector<pair<string,int>> cases = {
        {"322", 5},
        {"23222323", 66},
        {"2322322323222323223223", 142},
    };
    for (const auto& [seed, expected] : cases) {
        int actual = total_length_before_first_one(digits(seed));
        if (actual != expected) {
            throw runtime_error("calibration failed for " + seed + ": expected " +
                                to_string(expected) + ", got " + to_string(actual));
        }
    }
    cerr << "Calibration passed: total pre-1 lengths 5, 66, 142.\n";
}

string mask_word(uint64_t mask, int n) {
    string s;
    s.reserve(n);
    for (int i = 0; i < n; ++i) s.push_back(((mask >> i) & 1ULL) ? '3' : '2');
    return s;
}

bool primitive_mask(uint64_t mask, int n) {
    for (int d = 1; d < n; ++d) if (n % d == 0) {
        bool periodic = true;
        for (int i = d; i < n; ++i) {
            if (((mask >> i) & 1ULL) != ((mask >> (i % d)) & 1ULL)) {
                periodic = false;
                break;
            }
        }
        if (periodic) return false;
    }
    return true;
}

using PairKey = tuple<int,int,int,int>; // (P1,q1,P2,q2)

void audit_all_binary_seeds(int max_n, int max_steps, int min_n) {
    map<PairKey,long long> counts;
    map<PairKey,string> example;
    long long seeds = 0, pairs = 0;

    for (int seed_length = min_n; seed_length <= max_n; ++seed_length) {
        if (seed_length >= 63) throw runtime_error("mask enumeration supports lengths below 63");
        const uint64_t total = 1ULL << seed_length;
        for (uint64_t mask = 0; mask < total; ++mask) {
            ++seeds;
            vector<unsigned char> s;
            s.reserve(seed_length + max_steps + 2);
            for (int i = 0; i < seed_length; ++i)
                s.push_back(((mask >> i) & 1ULL) ? 3 : 2);

            int global_record = 0;
            vector<int> periods;
            periods.reserve(max_steps + 2);
            Event previous_record{-1,-1,-1,false,-1};

            for (int step = 0; step <= max_steps; ++step) {
                auto [k,p] = curling_number_and_shortest_period(s);
                const int n = (int)s.size();
                periods.push_back(p); // index = n-seed_length

                if (p > global_record) {
                    global_record = p;
                    const bool fully = (k == 2 && n - p >= seed_length);
                    const int bridge = fully ? periods[(n - p) - seed_length] : -1;
                    Event current{n,k,p,fully,bridge};

                    if (previous_record.length >= 0 && previous_record.exponent == 2 &&
                        current.exponent == 2 && previous_record.fully_generated_square &&
                        current.fully_generated_square) {
                        ++pairs;
                        PairKey key{previous_record.period, previous_record.bridge_period,
                                    current.period, current.bridge_period};
                        ++counts[key];
                        example.emplace(key, mask_word(mask, seed_length));
                        if (current.bridge_period > previous_record.bridge_period) {
                            cout << "COUNTEREXAMPLE seed_length=" << seed_length
                                 << " seed=" << mask_word(mask, seed_length)
                                 << " first=" << previous_record.period << "/"
                                 << previous_record.bridge_period
                                 << " second=" << current.period << "/"
                                 << current.bridge_period << "\n";
                            return;
                        }
                    }
                    previous_record = current;
                }

                if (k != 2 && k != 3) break;
                s.push_back((unsigned char)k);
            }
        }
        cerr << "all-seeds n=" << seed_length << " cumulative_seeds=" << seeds
             << " cumulative_pairs=" << pairs << " kinds=" << counts.size() << "\n";
    }

    cout << "NO_COUNTEREXAMPLE all-seeds min_n=" << min_n << " max_n=" << max_n
         << " seeds=" << seeds << " pairs=" << pairs << " kinds=" << counts.size() << "\n";
    for (const auto& [key,count] : counts) {
        auto [P1,q1,P2,q2] = key;
        cout << P1 << "/" << q1 << " -> " << P2 << "/" << q2
             << " count=" << count << " example=" << example[key] << "\n";
    }
}

void audit_exact_power_seeds(int max_root, int max_steps, int exponent, int min_root) {
    map<PairKey,long long> counts;
    map<PairKey,string> example;
    long long masks = 0, valid = 0, pairs = 0;

    for (int root_length = min_root; root_length <= max_root; ++root_length) {
        if (root_length >= 63) throw runtime_error("mask enumeration supports lengths below 63");
        const uint64_t total = 1ULL << root_length;
        for (uint64_t mask = 0; mask < total; ++mask) {
            ++masks;
            if (!primitive_mask(mask, root_length)) continue;

            vector<unsigned char> s;
            s.reserve(exponent * root_length + max_steps + 2);
            for (int rep = 0; rep < exponent; ++rep)
                for (int i = 0; i < root_length; ++i)
                    s.push_back(((mask >> i) & 1ULL) ? 3 : 2);

            auto [initial_k, initial_p] = curling_number_and_shortest_period(s);
            if (initial_k != exponent || initial_p != root_length) continue;
            ++valid;

            const int seed_length = (int)s.size();
            int global_record = 0;
            vector<int> periods;
            Event previous_record{-1,-1,-1,false,-1};

            for (int step = 0; step <= max_steps; ++step) {
                auto [k,p] = curling_number_and_shortest_period(s);
                const int n = (int)s.size();
                periods.push_back(p);
                if (p > global_record) {
                    global_record = p;
                    const bool fully = (k == 2 && n - p >= seed_length);
                    const int bridge = fully ? periods[(n - p) - seed_length] : -1;
                    Event current{n,k,p,fully,bridge};
                    if (previous_record.length >= 0 && previous_record.exponent == 2 &&
                        current.exponent == 2 && previous_record.fully_generated_square &&
                        current.fully_generated_square) {
                        ++pairs;
                        PairKey key{previous_record.period, previous_record.bridge_period,
                                    current.period, current.bridge_period};
                        ++counts[key];
                        example.emplace(key, mask_word(mask, root_length));
                        if (current.bridge_period > previous_record.bridge_period) {
                            cout << "COUNTEREXAMPLE exact-power exponent=" << exponent
                                 << " root_length=" << root_length
                                 << " root=" << mask_word(mask, root_length)
                                 << " first=" << previous_record.period << "/"
                                 << previous_record.bridge_period
                                 << " second=" << current.period << "/"
                                 << current.bridge_period << "\n";
                            return;
                        }
                    }
                    previous_record = current;
                }
                if (k != 2 && k != 3) break;
                s.push_back((unsigned char)k);
            }
        }
        cerr << "power exponent=" << exponent << " root_length=" << root_length
             << " masks=" << masks << " valid=" << valid << " pairs=" << pairs << "\n";
    }

    cout << "NO_COUNTEREXAMPLE exact-power exponent=" << exponent
         << " min_root=" << min_root << " max_root=" << max_root
         << " masks=" << masks << " valid=" << valid << " pairs=" << pairs << "\n";
    for (const auto& [key,count] : counts) {
        auto [P1,q1,P2,q2] = key;
        cout << P1 << "/" << q1 << " -> " << P2 << "/" << q2
             << " count=" << count << " example_root=" << example[key] << "\n";
    }
}

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        calibrate();
        if (argc < 2) {
            cerr << "Usage:\n"
                 << "  " << argv[0] << " all-seeds MAX_N [MAX_STEPS=600] [MIN_N=1]\n"
                 << "  " << argv[0] << " power MAX_ROOT EXPONENT [MAX_STEPS=600] [MIN_ROOT=1]\n";
            return 2;
        }
        const string mode = argv[1];
        if (mode == "all-seeds") {
            if (argc < 3) throw runtime_error("all-seeds requires MAX_N");
            audit_all_binary_seeds(stoi(argv[2]), argc >= 4 ? stoi(argv[3]) : 600,
                                   argc >= 5 ? stoi(argv[4]) : 1);
        } else if (mode == "power") {
            if (argc < 4) throw runtime_error("power requires MAX_ROOT and EXPONENT");
            audit_exact_power_seeds(stoi(argv[2]), argc >= 5 ? stoi(argv[4]) : 600,
                                    stoi(argv[3]), argc >= 6 ? stoi(argv[5]) : 1);
        } else {
            throw runtime_error("unknown mode: " + mode);
        }
    } catch (const exception& e) {
        cerr << "ERROR: " << e.what() << "\n";
        return 1;
    }
    return 0;
}
~~~~

---

# Appendix J. Local promotion audit

**Source file:** `replay_local_promo2.cpp`

~~~~cpp
#include <bits/stdc++.h>
using namespace std; using W=vector<unsigned char>;
pair<int,int> cn(const W&s){int n=s.size();vector<int>z(n);int l=0,r=0;auto at=[&](int i){return s[n-1-i];};for(int i=1;i<n;i++){if(i<r)z[i]=min(r-i,z[i-l]);while(i+z[i]<n&&at(z[i])==at(i+z[i]))z[i]++;if(i+z[i]>r)l=i,r=i+z[i];}int bk=1,bp=n;for(int p=1;p<n;p++){int k=1+z[p]/p;if(k>bk||(k==bk&&p<bp))bk=k,bp=p;}return{bk,bp};}
bool primitive(const W&r){int n=r.size();for(int d=1;d<n;d++)if(n%d==0){bool ok=1;for(int i=d;i<n;i++)if(r[i]!=r[i%d]){ok=0;break;}if(ok)return false;}return true;}
bool promo(const W&R,int&jj,pair<int,int>&bad){W s=R;s.insert(s.end(),R.begin(),R.end());for(int j=0;j<(int)R.size();j++){auto z=cn(s);if(z.first!=R[j]){jj=j;bad=z;return false;}s.push_back(z.first);}return true;}
string sw(const W&w){string s;for(auto x:w)s+=char('0'+x);return s;}
int main(int argc,char**argv){int Q=argc>1?stoi(argv[1]):9,LM=argc>2?stoi(argv[2]):12;long long valid=0,strict=0,spromo=0,snon=0,sgtq=0;int printed=0;for(int q=2;q<=Q;q++){for(uint64_t rm=0;rm<(1ULL<<q);rm++){W R(q);for(int i=0;i<q;i++)R[i]=2+((rm>>i)&1);if(!primitive(R))continue;for(int b=1;b<q;b++){int a=q-b,P=q+b;W B(R.begin()+a,R.end()),Y=B;Y.insert(Y.end(),R.begin(),R.end());for(int ll=0;ll<=LM;ll++){for(uint64_t lm=0;lm<(1ULL<<ll);lm++){W L(ll);for(int i=0;i<ll;i++)L[i]=2+((lm>>i)&1);W s=L;s.insert(s.end(),R.begin(),R.end());s.insert(s.end(),R.begin(),R.end());bool ok=1;int mx=0;vector<pair<int,int>>gp;for(int i=0;i<P;i++){auto z=cn(s);gp.push_back(z);mx=max(mx,z.second);if(z.first!=Y[i]){ok=0;break;}s.push_back(z.first);}if(!ok)continue;auto c=cn(s);if(c!=make_pair(2,P)||gp[0].second!=q)continue;valid++;if(mx<P){strict++; if(mx>q) sgtq++; int jj;pair<int,int>bad;if(promo(R,jj,bad))spromo++;else{snon++;if(printed++<30)cerr<<"NON q="<<q<<" b="<<b<<" R="<<sw(R)<<" L="<<sw(L)<<" j="<<jj<<" expect="<<(int)R[jj]<<" got="<<bad.first<<"/"<<bad.second<<"\n";}}}}}}cerr<<"q="<<q<<" valid="<<valid<<" strict="<<strict<<" promo="<<spromo<<" non="<<snon<<"\n";}cout<<"valid="<<valid<<" strict="<<strict<<" promotion="<<spromo<<" non="<<snon<<" sgtq="<<sgtq<<"\n";}
~~~~

---

# Appendix K. Bridge-promotion audit

**Source file:** `audit_bridge_promotion.cpp`

~~~~cpp
#include <bits/stdc++.h>
using namespace std; using W=vector<unsigned char>;
pair<int,int> cn(const W&s){int n=s.size(); vector<int>z(n); int l=0,r=0; auto at=[&](int i){return s[n-1-i];}; for(int i=1;i<n;i++){if(i<r)z[i]=min(r-i,z[i-l]); while(i+z[i]<n&&at(z[i])==at(i+z[i]))z[i]++; if(i+z[i]>r){l=i;r=i+z[i];}} int bk=1,bp=n; for(int p=1;p<n;p++){int k=1+z[p]/p; if(k>bk||(k==bk&&p<bp)){bk=k;bp=p;}} return {bk,bp};}
string sw(const W&s){string x;for(auto c:s)x+=char('0'+c);return x;}
bool promotion(const W&R,int*jm=nullptr,pair<int,int>*got=nullptr){W s=R; s.insert(s.end(),R.begin(),R.end()); for(int j=0;j<(int)R.size();j++){auto z=cn(s); if(z.first!=R[j]){if(jm)*jm=j;if(got)*got=z;return false;} s.push_back(z.first);} return true;}
int main(int argc,char**argv){int N=argc>1?stoi(argv[1]):18,steps=argc>2?stoi(argv[2]):500; long long squares=0,promo=0,non=0; map<pair<int,int>,long long> kinds; int printed=0; for(int n0=1;n0<=N;n0++){uint64_t total=1ULL<<n0;for(uint64_t m=0;m<total;m++){W s;for(int i=0;i<n0;i++)s.push_back(2+((m>>i)&1));int rec=0;vector<pair<int,int>>ev;for(int st=0;st<=steps;st++){auto [k,p]=cn(s);ev.push_back({k,p});if(p>rec){rec=p;if(k==2&&(int)s.size()-p>=n0){int idx=(int)s.size()-p-n0;if(idx>=0&&idx<(int)ev.size()){int q=ev[idx].second;if(q<p){int b=p-q,a=2*q-p;if(b>0&&a>0){W Y(s.end()-p,s.end());W R(Y.begin()+b,Y.end());squares++;int jm;pair<int,int>g;if(promotion(R,&jm,&g)){promo++;}else{non++;kinds[{p,q}]++;if(printed<20){cerr<<"NON seed=";for(int i=0;i<n0;i++)cerr<<char('0'+2+((m>>i)&1));cerr<<" P="<<p<<" q="<<q<<" R="<<sw(R)<<" j="<<jm<<" exp="<<(int)R[jm]<<" got="<<g.first<<"/"<<g.second<<"\n";printed++;}}}}}}}if(k!=2&&k!=3)break;s.push_back(k);}}cerr<<"n="<<n0<<" sq="<<squares<<" promo="<<promo<<" non="<<non<<"\n";}cout<<"squares="<<squares<<" promotion="<<promo<<" non="<<non<<" kinds="<<kinds.size()<<"\n";for(auto [x,c]:kinds)cout<<x.first<<"/"<<x.second<<" "<<c<<"\n";}
~~~~

---

# Appendix L. Full square-replay audit

**Source file:** `audit_all_square_replay.cpp`

~~~~cpp
#include <bits/stdc++.h>
using namespace std;
using W = vector<unsigned char>;

pair<int,int> cn(const W& s) {
    int n = (int)s.size();
    vector<int> z(n);
    int l=0,r=0;
    auto at=[&](int i){ return s[n-1-i]; };
    for(int i=1;i<n;i++){
        if(i<r) z[i]=min(r-i,z[i-l]);
        while(i+z[i]<n && at(z[i])==at(i+z[i])) z[i]++;
        if(i+z[i]>r){l=i;r=i+z[i];}
    }
    int bk=1,bp=n;
    for(int p=1;p<n;p++){
        int k=1+z[p]/p;
        if(k>bk || (k==bk && p<bp)){bk=k;bp=p;}
    }
    return {bk,bp};
}

string sw(const W& s){ string x; for(auto c:s)x+=char('0'+c); return x; }

int main(int argc,char**argv){
    int N=argc>1?stoi(argv[1]):18;
    int steps=argc>2?stoi(argv[2]):500;
    long long squares=0,tested=0,fullmatch=0,mismatch=0,terminalmis=0,newrecordmis=0;
    map<tuple<int,int,int,int,int>,long long> pats;
    int printed=0;

    for(int n0=1;n0<=N;n0++){
        uint64_t total=1ULL<<n0;
        for(uint64_t m=0;m<total;m++){
            W s;
            s.reserve(n0+steps+2);
            for(int i=0;i<n0;i++) s.push_back(2+((m>>i)&1));
            int rec=0;
            vector<pair<int,int>> ev;
            ev.reserve(steps+2);

            for(int st=0;st<=steps;st++){
                auto [k,p]=cn(s);
                ev.push_back({k,p});
                bool isrec = p>rec;
                if(isrec){
                    rec=p;
                    if(k==2 && (int)s.size()-p>=n0){
                        squares++;
                        int t=(int)s.size();
                        int startFinal=t-p;
                        int idx=startFinal-n0;
                        if(idx>=0 && idx<(int)ev.size()){
                            int q=ev[idx].second;
                            if(q<p){
                                tested++;
                                W Y(s.end()-p,s.end());
                                int b=p-q;
                                int aLen=2*q-p;
                                if(b>0 && aLen>0 && b+(int)q==(int)Y.size()+0){
                                    W R(Y.begin()+b,Y.end());
                                    if((int)R.size()!=q) continue;
                                    W u=s;
                                    int jmis=-1;
                                    pair<int,int> got{-1,-1};
                                    for(int j=0;j<q;j++){
                                        auto z=cn(u);
                                        if(z.first!=R[j]){ jmis=j; got=z; break; }
                                        if(z.first!=2 && z.first!=3){ jmis=j; got=z; break; }
                                        u.push_back((unsigned char)z.first);
                                    }
                                    if(jmis<0){
                                        fullmatch++;
                                    }else{
                                        mismatch++;
                                        if(got.first!=2 && got.first!=3) terminalmis++;
                                        if(got.second>p) newrecordmis++;
                                        pats[{p,q,jmis,got.first,got.second}]++;
                                        if(printed<40){
                                            cerr<<"MIS seed=";
                                            for(int i=0;i<n0;i++) cerr<<char('0'+2+((m>>i)&1));
                                            cerr<<" t="<<t<<" P="<<p<<" q="<<q
                                                <<" Y="<<sw(Y)<<" R="<<sw(R)
                                                <<" j="<<jmis<<" expect="<<(int)R[jmis]
                                                <<" got="<<got.first<<"/"<<got.second<<"\n";
                                            printed++;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                if(k!=2 && k!=3) break;
                s.push_back((unsigned char)k);
            }
        }
        cerr<<"done n="<<n0<<" squares="<<squares<<" tested="<<tested
            <<" match="<<fullmatch<<" mis="<<mismatch<<"\n";
    }

    cout<<"squares="<<squares<<" tested="<<tested<<" fullmatch="<<fullmatch
        <<" mismatch="<<mismatch<<" terminalmis="<<terminalmis
        <<" newrecordmis="<<newrecordmis<<" kinds="<<pats.size()<<"\n";
    for(auto &[t,c]:pats){
        auto [P,q,j,k,p]=t;
        cout<<P<<"/"<<q<<" j"<<j<<" got"<<k<<"/"<<p<<" count="<<c<<"\n";
    }
    return 0;
}
~~~~

---

# Appendix M. Part 3 counterexample verifier

**Source file:** `verify_part3_examples.py`

~~~~python
from __future__ import annotations

from typing import Iterable, Sequence


def z_function(s: Sequence[int]) -> list[int]:
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def cn(seq: Sequence[int]) -> tuple[int, int]:
    if not seq:
        raise ValueError("empty word")
    n = len(seq)
    z = z_function(list(reversed(seq)))
    best_k, best_p = 1, n
    for p in range(1, n):
        k = 1 + z[p] // p
        if k > best_k or (k == best_k and p < best_p):
            best_k, best_p = k, p
    return best_k, best_p


def digits(s: str) -> list[int]:
    return [int(c) for c in s.strip()]


def continuation(seed: str, steps: int) -> list[tuple[int, int]]:
    s = digits(seed)
    out: list[tuple[int, int]] = []
    for _ in range(steps):
        k, p = cn(s)
        out.append((k, p))
        s.append(k)
    return out


def total_before_one(seed: str, cap: int = 100_000) -> int:
    s = digits(seed)
    for _ in range(cap):
        k, _ = cn(s)
        if k == 1:
            return len(s)
        s.append(k)
    raise RuntimeError("cap exceeded")


def show(label: str, word: str) -> None:
    print(f"{label}: word={word} cn/period={cn(digits(word))}")


def main() -> None:
    calibration = {
        "322": 5,
        "23222323": 66,
        "2322322323222323223223": 142,
    }
    for seed, expected in calibration.items():
        actual = total_before_one(seed)
        assert actual == expected, (seed, expected, actual)
    print("CALIBRATION PASSED: 5, 66, 142")

    D = "223222"
    R = "322232"
    full = continuation(D + R, len(R))
    stand = continuation(R + R, len(R))
    print("\nGENERATED-R^2 IMPOSTOR")
    print("D=", D, "R=", R)
    print("from DR generated symbols/periods:", full)
    print("generated symbols:", "".join(str(k) for k, _ in full))
    show("completed DR^2", D + R + "".join(str(k) for k, _ in full))
    print("from standalone R^2 symbols/periods:", stand)
    print("standalone symbols:", "".join(str(k) for k, _ in stand))

    R = "233323"
    B = "23"
    j = 1
    T = R[:j]
    L = "23332322333232"
    E = L + R + T
    G = L + R + R
    F = L + R + R + B + T
    H = L + R + R + B + R
    standalone = R + R + T
    print("\nSTATIC TWO-CUBE IMPOSTOR")
    print(f"L={L} R={R} B={B} j={j} T={T} P={len(R)+len(B)}")
    for label, word in [("E=LRT", E), ("G=LR^2", G), ("F=LR^2BT", F),
                        ("H=LR^2BR", H), ("R^2T", standalone)]:
        show(label, word)
    generated = continuation(L + R, len(R))
    print("actual symbols/periods from LR:", generated)
    print("actual generated block:", "".join(str(k) for k, _ in generated))
    print("desired second R:", R)
    assert "".join(str(k) for k, _ in generated) != R


if __name__ == "__main__":
    main()
~~~~

---

# Appendix N. Preserved exact outputs

**Source file:** `replay_local_promo2.out`

~~~~text
valid=2286 strict=1536 promotion=1536 non=0 sgtq=0
~~~~

---

# Appendix O. Preserved bridge-promotion output

**Source file:** `audit_bridge_promotion.out`

~~~~text
squares=9722 promotion=9722 non=0 kinds=0
~~~~

---

# Appendix P. Fresh full replay output

**Source file:** `audit_all_square_replay.out`

~~~~text
squares=9722 tested=9722 fullmatch=9722 mismatch=0 terminalmis=0 newrecordmis=0 kinds=0
~~~~

---

# Appendix Q. Fresh full replay progress log

**Source file:** `audit_all_square_replay.err`

~~~~text
done n=1 squares=0 tested=0 match=0 mis=0
done n=2 squares=0 tested=0 match=0 mis=0
done n=3 squares=0 tested=0 match=0 mis=0
done n=4 squares=0 tested=0 match=0 mis=0
done n=5 squares=0 tested=0 match=0 mis=0
done n=6 squares=0 tested=0 match=0 mis=0
done n=7 squares=0 tested=0 match=0 mis=0
done n=8 squares=4 tested=4 match=4 mis=0
done n=9 squares=13 tested=13 match=13 mis=0
done n=10 squares=32 tested=32 match=32 mis=0
done n=11 squares=70 tested=70 match=70 mis=0
done n=12 squares=147 tested=147 match=147 mis=0
done n=13 squares=300 tested=300 match=300 mis=0
done n=14 squares=605 tested=605 match=605 mis=0
done n=15 squares=1214 tested=1214 match=1214 mis=0
done n=16 squares=2430 tested=2430 match=2430 mis=0
done n=17 squares=4861 tested=4861 match=4861 mis=0
done n=18 squares=9722 tested=9722 match=9722 mis=0
~~~~

---

# Appendix R. Fresh Part 3 verifier output

**Source file:** `verify_part3_examples.out`

~~~~text
CALIBRATION PASSED: 5, 66, 142

GENERATED-R^2 IMPOSTOR
D= 223222 R= 322232
from DR generated symbols/periods: [(3, 4), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6)]
generated symbols: 322232
completed DR^2: word=223222322232322232 cn/period=(2, 6)
from standalone R^2 symbols/periods: [(2, 6), (2, 1), (3, 1), (2, 4), (2, 4), (3, 4)]
standalone symbols: 223223

STATIC TWO-CUBE IMPOSTOR
L=23332322333232 R=233323 B=23 j=1 T=2 P=8
E=LRT: word=233323223332322333232 cn/period=(3, 7)
G=LR^2: word=23332322333232233323233323 cn/period=(2, 6)
F=LR^2BT: word=23332322333232233323233323232 cn/period=(3, 2)
H=LR^2BR: word=2333232233323223332323332323233323 cn/period=(2, 8)
R^2T: word=2333232333232 cn/period=(2, 2)
actual symbols/periods from LR: [(2, 7), (3, 7), (2, 2), (3, 2), (3, 2), (2, 1)]
actual generated block: 232332
desired second R: 233323
~~~~

---

# Appendix S. Raw autonomous-square report

**Source file:** `_tmp_autonomous_square_report.txt`

~~~~text
STATS
(4, 21, 0, 1, (3, 2, 1)) count=2
(6, 21, 0, 1, (3, 3, 2, 1)) count=1
(6, 21, 1, 1, (3, 2, 1)) count=1
(6, 21, 1, 1, (3, 3, 2, 1)) count=1
(6, 21, 2, 1, (3, 3, 2, 1)) count=1
(6, 21, 3, 1, (3, 3, 2, 1)) count=1
(6, 21, 4, 1, (3, 3, 2, 1)) count=1
(7, 21, 0, 1, (3, 1)) count=1
(7, 21, 0, 1, (3, 3, 2, 1)) count=1
(7, 21, 1, 1, (3, 2, 1)) count=1
(7, 21, 1, 1, (3, 3, 2, 1)) count=1
(7, 21, 2, 1, (3, 3, 2, 1)) count=1
(7, 21, 3, 1, (3, 3, 2, 1)) count=1
(7, 21, 4, 1, (3, 3, 2, 1)) count=1
(8, 21, 7, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(8, 21, 7, 1, (3, 3, 2, 1)) count=1
(8, 21, 8, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(8, 21, 8, 1, (3, 3, 2, 1)) count=1
(8, 21, 9, 1, (3, 2, 1)) count=1
(8, 21, 9, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(8, 21, 10, 1, (3, 2, 1)) count=1
(8, 21, 10, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(8, 21, 11, 1, (3, 2, 1)) count=1
(8, 21, 12, 1, (3, 2, 1)) count=1
(8, 21, 13, 1, (3, 2, 1)) count=1
(9, 21, 7, 1, (3, 2, 2, 2, 3, 1)) count=1
(9, 21, 7, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 8, 1, (3, 2, 2, 2, 3, 1)) count=2
(9, 21, 8, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 9, 1, (3, 2, 2, 2, 3, 1)) count=2
(9, 21, 9, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 10, 1, (3, 2, 2, 2, 3, 1)) count=1
(9, 21, 10, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 10, 1, (3, 3, 2, 1)) count=1
(9, 21, 11, 1, (3, 2, 1)) count=2
(9, 21, 11, 1, (3, 2, 2, 2, 3, 1)) count=1
(9, 21, 11, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 12, 1, (3, 2, 1)) count=2
(9, 21, 12, 1, (3, 2, 2, 2, 3, 1)) count=1
(9, 21, 12, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 13, 1, (3, 2, 1)) count=2
(9, 21, 13, 1, (3, 2, 2, 2, 3, 1)) count=1
(9, 21, 13, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(9, 21, 14, 1, (3, 2, 1)) count=2
(9, 21, 15, 1, (3, 2, 1)) count=2
(9, 21, 16, 1, (3, 2, 1)) count=1
(10, 21, 0, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 1, 1, (3, 2, 1)) count=1
(10, 21, 1, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 2, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 3, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 4, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 5, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 6, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 7, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 8, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(10, 21, 8, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(10, 21, 8, 1, (3, 3, 2, 1)) count=1
(10, 21, 9, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(10, 21, 9, 1, (3, 3, 2, 1)) count=1
(10, 21, 10, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(10, 21, 10, 1, (3, 3, 2, 1)) count=1
(10, 21, 11, 1, (3, 2, 2, 2, 3, 1)) count=2
(10, 21, 11, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(10, 21, 11, 1, (3, 3, 2, 1)) count=1
(10, 21, 12, 1, (3, 2, 1)) count=2
(10, 21, 12, 1, (3, 2, 2, 2, 3, 1)) count=1
(10, 21, 12, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(10, 21, 12, 1, (3, 3, 2, 1)) count=2
(10, 21, 13, 1, (3, 2, 1)) count=4
(10, 21, 13, 1, (3, 2, 2, 2, 3, 1)) count=1
(10, 21, 13, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(10, 21, 14, 1, (3, 2, 1)) count=4
(10, 21, 14, 1, (3, 2, 2, 2, 3, 1)) count=1
(10, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(10, 21, 15, 1, (3, 2, 1)) count=4
(10, 21, 15, 1, (3, 2, 2, 2, 3, 1)) count=1
(10, 21, 16, 1, (3, 2, 1)) count=4
(10, 21, 17, 1, (3, 2, 1)) count=4
(10, 21, 18, 1, (3, 2, 1)) count=2
(11, 21, 0, 1, (3, 2, 1)) count=1
(11, 21, 1, 1, (3, 2, 1)) count=1
(11, 21, 2, 1, (3, 2, 1)) count=1
(11, 21, 3, 1, (3, 2, 1)) count=1
(11, 21, 4, 1, (3, 2, 1)) count=1
(11, 21, 5, 1, (3, 2, 1)) count=1
(11, 21, 6, 1, (3, 2, 1)) count=1
(11, 21, 7, 1, (3, 2, 1)) count=1
(11, 21, 8, 1, (3, 2, 1)) count=1
(11, 21, 9, 1, (3, 2, 1)) count=3
(11, 21, 10, 1, (3, 2, 1)) count=3
(11, 21, 11, 1, (3, 2, 1)) count=2
(11, 21, 12, 1, (3, 2, 1)) count=5
(11, 21, 12, 1, (3, 2, 2, 2, 3, 1)) count=2
(11, 21, 12, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(11, 21, 12, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(11, 21, 12, 1, (3, 3, 2, 1)) count=2
(11, 21, 13, 1, (3, 2, 1)) count=4
(11, 21, 13, 1, (3, 2, 2, 2, 3, 1)) count=4
(11, 21, 13, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(11, 21, 13, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=3
(11, 21, 13, 1, (3, 3, 2, 1)) count=2
(11, 21, 14, 1, (3, 2, 1)) count=6
(11, 21, 14, 1, (3, 2, 2, 2, 3, 1)) count=2
(11, 21, 14, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(11, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(11, 21, 14, 1, (3, 3, 2, 1)) count=4
(11, 21, 15, 1, (3, 2, 1)) count=10
(11, 21, 15, 1, (3, 2, 2, 2, 3, 1)) count=2
(11, 21, 15, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(11, 21, 15, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(11, 21, 16, 1, (3, 2, 1)) count=10
(11, 21, 16, 1, (3, 2, 2, 2, 3, 1)) count=2
(11, 21, 16, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(11, 21, 16, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(11, 21, 17, 1, (3, 2, 1)) count=9
(11, 21, 17, 1, (3, 2, 2, 2, 3, 1)) count=2
(11, 21, 17, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(11, 21, 18, 1, (3, 2, 1)) count=9
(11, 21, 19, 1, (3, 2, 1)) count=9
(11, 21, 20, 1, (3, 2, 1)) count=4
(12, 21, 10, 1, (3, 2, 1)) count=2
(12, 21, 11, 1, (3, 2, 1)) count=4
(12, 21, 11, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(12, 21, 11, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(12, 21, 12, 1, (3, 2, 1)) count=4
(12, 21, 12, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(12, 21, 12, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(12, 21, 13, 1, (3, 2, 1)) count=7
(12, 21, 13, 1, (3, 2, 2, 2, 3, 1)) count=2
(12, 21, 13, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(12, 21, 13, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(12, 21, 13, 1, (3, 3, 2, 1)) count=1
(12, 21, 14, 1, (3, 2, 1)) count=9
(12, 21, 14, 1, (3, 2, 2, 2, 3, 1)) count=4
(12, 21, 14, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(12, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(12, 21, 14, 1, (3, 3, 2, 1)) count=3
(12, 21, 15, 1, (3, 2, 1)) count=8
(12, 21, 15, 1, (3, 2, 2, 2, 3, 1)) count=8
(12, 21, 15, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(12, 21, 15, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=6
(12, 21, 15, 1, (3, 3, 2, 1)) count=3
(12, 21, 16, 1, (3, 2, 1)) count=12
(12, 21, 16, 1, (3, 2, 2, 2, 3, 1)) count=4
(12, 21, 16, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(12, 21, 16, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(12, 21, 16, 1, (3, 3, 2, 1)) count=7
(12, 21, 17, 1, (3, 2, 1)) count=20
(12, 21, 17, 1, (3, 2, 2, 2, 3, 1)) count=5
(12, 21, 17, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(12, 21, 17, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(12, 21, 18, 1, (3, 2, 1)) count=18
(12, 21, 18, 1, (3, 2, 2, 2, 3, 1)) count=5
(12, 21, 18, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(12, 21, 18, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(12, 21, 19, 1, (3, 2, 1)) count=16
(12, 21, 19, 1, (3, 2, 2, 2, 3, 1)) count=5
(12, 21, 19, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(12, 21, 20, 1, (3, 2, 1)) count=16
(12, 21, 20, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(12, 21, 21, 1, (3, 2, 1)) count=17
(12, 21, 22, 1, (3, 2, 1)) count=8
(13, 21, 9, 1, (3, 2, 2, 2, 3, 1)) count=1
(13, 21, 9, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(13, 21, 10, 1, (3, 2, 2, 2, 3, 1)) count=1
(13, 21, 10, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(13, 21, 11, 1, (3, 2, 2, 2, 3, 1)) count=2
(13, 21, 11, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(13, 21, 12, 1, (3, 1)) count=1
(13, 21, 12, 1, (3, 2, 1)) count=2
(13, 21, 12, 1, (3, 2, 2, 2, 3, 1)) count=2
(13, 21, 12, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(13, 21, 13, 1, (3, 1)) count=1
(13, 21, 13, 1, (3, 2, 1)) count=4
(13, 21, 13, 1, (3, 2, 2, 2, 3, 1)) count=2
(13, 21, 13, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(13, 21, 14, 1, (3, 1)) count=1
(13, 21, 14, 1, (3, 2, 1)) count=6
(13, 21, 14, 1, (3, 2, 2, 2, 3, 1)) count=2
(13, 21, 14, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(13, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(13, 21, 14, 1, (3, 3, 2, 1)) count=2
(13, 21, 15, 1, (3, 1)) count=1
(13, 21, 15, 1, (3, 2, 1)) count=14
(13, 21, 15, 1, (3, 2, 2, 2, 3, 1)) count=4
(13, 21, 15, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(13, 21, 15, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(13, 21, 15, 1, (3, 3, 2, 1)) count=4
(13, 21, 16, 1, (3, 1)) count=1
(13, 21, 16, 1, (3, 2, 1)) count=17
(13, 21, 16, 1, (3, 2, 2, 2, 3, 1)) count=8
(13, 21, 16, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(13, 21, 16, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=8
(13, 21, 16, 1, (3, 3, 2, 1)) count=8
(13, 21, 17, 1, (3, 1)) count=1
(13, 21, 17, 1, (3, 2, 1)) count=15
(13, 21, 17, 1, (3, 2, 2, 2, 3, 1)) count=16
(13, 21, 17, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(13, 21, 17, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=12
(13, 21, 17, 1, (3, 3, 2, 1)) count=8
(13, 21, 18, 1, (3, 2, 1)) count=23
(13, 21, 18, 1, (3, 2, 2, 2, 3, 1)) count=8
(13, 21, 18, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(13, 21, 18, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=8
(13, 21, 18, 1, (3, 3, 2, 1)) count=15
(13, 21, 19, 1, (3, 2, 1)) count=39
(13, 21, 19, 1, (3, 2, 2, 2, 3, 1)) count=8
(13, 21, 19, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(13, 21, 19, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=8
(13, 21, 20, 1, (3, 2, 1)) count=36
(13, 21, 20, 1, (3, 2, 2, 2, 3, 1)) count=8
(13, 21, 20, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(13, 21, 20, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=9
(13, 21, 21, 1, (3, 2, 1)) count=32
(13, 21, 21, 1, (3, 2, 2, 2, 3, 1)) count=8
(13, 21, 21, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(13, 21, 22, 1, (3, 2, 1)) count=33
(13, 21, 23, 1, (3, 2, 1)) count=33
(13, 21, 24, 1, (3, 2, 1)) count=16
(13, 21, 29, 1, (3, 2, 1)) count=1
(13, 21, 30, 1, (3, 2, 1)) count=1
(14, 21, 5, 1, (3, 2, 1)) count=1
(14, 21, 6, 1, (3, 2, 1)) count=1
(14, 21, 7, 1, (3, 2, 1)) count=1
(14, 21, 8, 1, (3, 2, 1)) count=1
(14, 21, 9, 1, (3, 2, 1)) count=1
(14, 21, 10, 1, (3, 2, 1)) count=1
(14, 21, 11, 1, (3, 2, 1)) count=1
(14, 21, 12, 1, (3, 2, 1)) count=1
(14, 21, 13, 1, (3, 2, 1)) count=2
(14, 21, 13, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(14, 21, 14, 1, (3, 2, 1)) count=4
(14, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(14, 21, 15, 1, (3, 1)) count=1
(14, 21, 15, 1, (3, 2, 1)) count=8
(14, 21, 15, 1, (3, 2, 2, 2, 3, 1)) count=2
(14, 21, 15, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(14, 21, 15, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(14, 21, 15, 1, (3, 3, 2, 1)) count=1
(14, 21, 16, 1, (3, 1)) count=1
(14, 21, 16, 1, (3, 2, 1)) count=18
(14, 21, 16, 1, (3, 2, 2, 2, 3, 1)) count=4
(14, 21, 16, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(14, 21, 16, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(14, 21, 16, 1, (3, 3, 2, 1)) count=3
(14, 21, 17, 1, (3, 1)) count=1
(14, 21, 17, 1, (3, 2, 1)) count=28
(14, 21, 17, 1, (3, 2, 2, 2, 3, 1)) count=8
(14, 21, 17, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(14, 21, 17, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=8
(14, 21, 17, 1, (3, 3, 2, 1)) count=7
(14, 21, 18, 1, (3, 1)) count=1
(14, 21, 18, 1, (3, 2, 1)) count=34
(14, 21, 18, 1, (3, 2, 2, 2, 3, 1)) count=16
(14, 21, 18, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=8
(14, 21, 18, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=16
(14, 21, 18, 1, (3, 3, 2, 1)) count=15
(14, 21, 19, 1, (3, 1)) count=1
(14, 21, 19, 1, (3, 2, 1)) count=30
(14, 21, 19, 1, (3, 2, 2, 2, 3, 1)) count=32
(14, 21, 19, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=8
(14, 21, 19, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=24
(14, 21, 19, 1, (3, 3, 2, 1)) count=15
(14, 21, 20, 1, (3, 2, 1)) count=46
(14, 21, 20, 1, (3, 2, 2, 2, 3, 1)) count=16
(14, 21, 20, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=8
(14, 21, 20, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=16
(14, 21, 20, 1, (3, 3, 2, 1)) count=30
(14, 21, 21, 1, (3, 2, 1)) count=78
(14, 21, 21, 1, (3, 2, 2, 2, 3, 1)) count=16
(14, 21, 21, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=9
(14, 21, 21, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=16
(14, 21, 22, 1, (3, 2, 1)) count=72
(14, 21, 22, 1, (3, 2, 2, 2, 3, 1)) count=17
(14, 21, 22, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=9
(14, 21, 22, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=16
(14, 21, 23, 1, (3, 2, 1)) count=65
(14, 21, 23, 1, (3, 2, 2, 2, 3, 1)) count=17
(14, 21, 23, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=9
(14, 21, 24, 1, (3, 2, 1)) count=66
(14, 21, 24, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(14, 21, 25, 1, (3, 2, 1)) count=68
(14, 21, 25, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(14, 21, 26, 1, (3, 2, 1)) count=33
(15, 21, 8, 1, (3, 2, 1)) count=1
(15, 21, 9, 1, (3, 2, 1)) count=1
(15, 21, 10, 1, (3, 2, 1)) count=1
(15, 21, 11, 1, (3, 2, 1)) count=1
(15, 21, 12, 1, (3, 2, 1)) count=1
(15, 21, 13, 1, (3, 2, 1)) count=2
(15, 21, 14, 1, (3, 2, 1)) count=4
(15, 21, 14, 1, (3, 2, 2, 2, 3, 1)) count=1
(15, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(15, 21, 15, 1, (3, 2, 1)) count=4
(15, 21, 15, 1, (3, 2, 2, 2, 3, 1)) count=1
(15, 21, 15, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(15, 21, 16, 1, (3, 1)) count=1
(15, 21, 16, 1, (3, 2, 1)) count=8
(15, 21, 16, 1, (3, 2, 2, 2, 3, 1)) count=2
(15, 21, 16, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(15, 21, 16, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(15, 21, 16, 1, (3, 3, 2, 1)) count=2
(15, 21, 17, 1, (3, 1)) count=2
(15, 21, 17, 1, (3, 2, 1)) count=18
(15, 21, 17, 1, (3, 2, 2, 2, 3, 1)) count=4
(15, 21, 17, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(15, 21, 17, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(15, 21, 17, 1, (3, 3, 2, 1)) count=4
(15, 21, 18, 1, (3, 1)) count=2
(15, 21, 18, 1, (3, 2, 1)) count=33
(15, 21, 18, 1, (3, 2, 2, 2, 3, 1)) count=8
(15, 21, 18, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=8
(15, 21, 18, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=8
(15, 21, 18, 1, (3, 3, 2, 1)) count=8
(15, 21, 19, 1, (3, 1)) count=2
(15, 21, 19, 1, (3, 2, 1)) count=56
(15, 21, 19, 1, (3, 2, 2, 2, 3, 1)) count=16
(15, 21, 19, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=8
(15, 21, 19, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=16
(15, 21, 19, 1, (3, 3, 2, 1)) count=16
(15, 21, 20, 1, (3, 1)) count=2
(15, 21, 20, 1, (3, 2, 1)) count=68
(15, 21, 20, 1, (3, 2, 2, 2, 3, 1)) count=32
(15, 21, 20, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(15, 21, 20, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=32
(15, 21, 20, 1, (3, 3, 2, 1)) count=30
(15, 21, 21, 1, (3, 1)) count=2
(15, 21, 21, 1, (3, 2, 1)) count=60
(15, 21, 21, 1, (3, 2, 2, 2, 3, 1)) count=64
(15, 21, 21, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(15, 21, 21, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=48
(15, 21, 21, 1, (3, 3, 2, 1)) count=30
(15, 21, 22, 1, (3, 2, 1)) count=92
(15, 21, 22, 1, (3, 2, 2, 2, 3, 1)) count=32
(15, 21, 22, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(15, 21, 22, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=33
(15, 21, 22, 1, (3, 3, 2, 1)) count=60
(15, 21, 23, 1, (3, 2, 1)) count=156
(15, 21, 23, 1, (3, 2, 2, 2, 3, 1)) count=33
(15, 21, 23, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(15, 21, 23, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=34
(15, 21, 24, 1, (3, 2, 1)) count=144
(15, 21, 24, 1, (3, 2, 2, 2, 3, 1)) count=34
(15, 21, 24, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(15, 21, 24, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=35
(15, 21, 25, 1, (3, 2, 1)) count=129
(15, 21, 25, 1, (3, 2, 2, 2, 3, 1)) count=35
(15, 21, 25, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=17
(15, 21, 26, 1, (3, 2, 1)) count=133
(15, 21, 26, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(15, 21, 27, 1, (3, 2, 1)) count=132
(15, 21, 28, 1, (3, 2, 1)) count=64
(16, 21, 14, 1, (3, 2, 1)) count=1
(16, 21, 14, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(16, 21, 14, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(16, 21, 15, 1, (3, 2, 1)) count=2
(16, 21, 15, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(16, 21, 15, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(16, 21, 15, 1, (3, 3, 2, 1)) count=1
(16, 21, 16, 1, (3, 2, 1)) count=6
(16, 21, 16, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(16, 21, 16, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=1
(16, 21, 16, 1, (3, 3, 2, 1)) count=1
(16, 21, 17, 1, (3, 1)) count=1
(16, 21, 17, 1, (3, 2, 1)) count=8
(16, 21, 17, 1, (3, 2, 2, 2, 3, 1)) count=2
(16, 21, 17, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(16, 21, 17, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=2
(16, 21, 17, 1, (3, 3, 2, 1)) count=2
(16, 21, 18, 1, (3, 1)) count=2
(16, 21, 18, 1, (3, 2, 1)) count=18
(16, 21, 18, 1, (3, 2, 2, 2, 3, 1)) count=4
(16, 21, 18, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=4
(16, 21, 18, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=4
(16, 21, 18, 1, (3, 3, 2, 1)) count=4
(16, 21, 19, 1, (3, 1)) count=4
(16, 21, 19, 1, (3, 2, 1)) count=36
(16, 21, 19, 1, (3, 2, 2, 2, 3, 1)) count=8
(16, 21, 19, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=8
(16, 21, 19, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=8
(16, 21, 19, 1, (3, 3, 2, 1)) count=7
(16, 21, 20, 1, (3, 1)) count=4
(16, 21, 20, 1, (3, 2, 1)) count=70
(16, 21, 20, 1, (3, 2, 2, 2, 3, 1)) count=16
(16, 21, 20, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(16, 21, 20, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=16
(16, 21, 20, 1, (3, 3, 2, 1)) count=15
(16, 21, 21, 1, (3, 1)) count=4
(16, 21, 21, 1, (3, 2, 1)) count=112
(16, 21, 21, 1, (3, 2, 2, 2, 3, 1)) count=32
(16, 21, 21, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=16
(16, 21, 21, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=32
(16, 21, 21, 1, (3, 3, 2, 1)) count=30
(16, 21, 22, 1, (3, 1)) count=4
(16, 21, 22, 1, (3, 2, 1)) count=136
(16, 21, 22, 1, (3, 2, 2, 2, 3, 1)) count=64
(16, 21, 22, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=32
(16, 21, 22, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=64
(16, 21, 22, 1, (3, 3, 2, 1)) count=60
(16, 21, 23, 1, (3, 1)) count=4
(16, 21, 23, 1, (3, 2, 1)) count=120
(16, 21, 23, 1, (3, 2, 2, 2, 3, 1)) count=128
(16, 21, 23, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=32
(16, 21, 23, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=95
(16, 21, 23, 1, (3, 3, 2, 1)) count=59
(16, 21, 24, 1, (3, 2, 1)) count=184
(16, 21, 24, 1, (3, 2, 2, 2, 3, 1)) count=64
(16, 21, 24, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=33
(16, 21, 24, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=64
(16, 21, 24, 1, (3, 3, 2, 1)) count=119
(16, 21, 25, 1, (3, 2, 1)) count=311
(16, 21, 25, 1, (3, 2, 2, 2, 3, 1)) count=64
(16, 21, 25, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=33
(16, 21, 25, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=65
(16, 21, 26, 1, (3, 2, 1)) count=289
(16, 21, 26, 1, (3, 2, 2, 2, 3, 1)) count=66
(16, 21, 26, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=34
(16, 21, 26, 1, (3, 2, 2, 2, 3, 3, 2, 1)) count=67
(16, 21, 27, 1, (3, 2, 1)) count=261
(16, 21, 27, 1, (3, 2, 2, 2, 3, 1)) count=69
(16, 21, 27, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=36
(16, 21, 28, 1, (3, 2, 1)) count=268
(16, 21, 28, 1, (3, 2, 2, 2, 3, 1)) count=1
(16, 21, 28, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=2
(16, 21, 29, 1, (3, 2, 1)) count=272
(16, 21, 29, 1, (3, 2, 2, 2, 3, 1)) count=1
(16, 21, 29, 1, (3, 2, 2, 2, 3, 2, 2, 2)) count=1
(16, 21, 30, 1, (3, 2, 1)) count=132

EXAMPLES
R=2232 q=4 cube=(p21,edge0,n63) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=65 records=[(2, 4, 0, None), (2, 6, 5, 3), (2, 7, 14, 13), (3, 21, 0, None)]
R=2322 q=4 cube=(p21,edge0,n63) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=65 records=[(2, 1, 6, None), (2, 4, 2, None), (2, 7, 3, 2), (3, 21, 0, None)]
R=222323 q=6 cube=(p21,edge4,n67) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=70 records=[(2, 2, 8, None), (2, 6, 4, None), (2, 7, 13, 12), (3, 21, 4, None)]
R=223232 q=6 cube=(p21,edge3,n66) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=69 records=[(2, 2, 8, None), (2, 6, 3, None), (2, 7, 12, 11), (3, 21, 3, None)]
R=232223 q=6 cube=(p21,edge0,n63) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=66 records=[(2, 6, 0, None), (2, 7, 9, 8), (3, 21, 0, None)]
R=232322 q=6 cube=(p21,edge2,n65) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=68 records=[(2, 1, 10, None), (2, 6, 2, None), (2, 7, 11, 10), (3, 21, 2, None)]
R=322232 q=6 cube=(p21,edge1,n64) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=66 records=[(2, 6, 0, None), (2, 7, 8, 7), (3, 21, 1, None)]
R=323222 q=6 cube=(p21,edge1,n64) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=67 records=[(3, 1, 9, None), (2, 6, 1, None), (2, 7, 10, 9), (3, 21, 1, None)]
R=2223223 q=7 cube=(p21,edge4,n67) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=70 records=[(2, 3, 8, None), (2, 7, 4, None), (3, 21, 4, None)]
R=2232223 q=7 cube=(p21,edge0,n63) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=66 records=[(2, 7, 0, None), (3, 21, 0, None)]
R=2232232 q=7 cube=(p21,edge3,n66) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=69 records=[(2, 3, 8, None), (2, 7, 3, None), (3, 21, 3, None)]
R=2322232 q=7 cube=(p21,edge0,n63) cont=[(3, 21), (1, 1)] stop=1 L=64 records=[(2, 4, 6, None), (2, 6, 11, 9), (2, 7, 20, 19), (3, 21, 0, None)]
R=2322322 q=7 cube=(p21,edge2,n65) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=68 records=[(2, 1, 12, None), (2, 7, 2, None), (3, 21, 2, None)]
R=3222322 q=7 cube=(p21,edge1,n64) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=66 records=[(2, 1, 12, None), (2, 4, 8, None), (2, 6, 10, 8), (2, 7, 19, 18), (3, 21, 1, None)]
R=3223222 q=7 cube=(p21,edge1,n64) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=67 records=[(3, 1, 11, None), (2, 7, 1, None), (3, 21, 1, None)]
R=22233223 q=8 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 8, 0, None), (3, 21, 13, None)]
R=22332232 q=8 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 8, 0, None), (3, 21, 12, None)]
R=23222323 q=8 cube=(p21,edge8,n71) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=74 records=[(2, 2, 12, None), (2, 6, 8, None), (2, 7, 17, 16), (3, 21, 8, None)]
R=23232223 q=8 cube=(p21,edge8,n71) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 8, 0, None), (3, 21, 8, None)]
R=23232322 q=8 cube=(p21,edge10,n73) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 1, 14, None), (2, 8, 2, None), (3, 21, 10, None)]
R=23322322 q=8 cube=(p21,edge11,n74) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 1, 14, None), (2, 8, 2, None), (3, 21, 11, None)]
R=32223232 q=8 cube=(p21,edge7,n70) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=73 records=[(2, 2, 12, None), (2, 6, 7, None), (2, 7, 16, 15), (3, 21, 7, None)]
R=32232223 q=8 cube=(p21,edge9,n72) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=74 records=[(2, 8, 0, None), (3, 21, 9, None)]
R=32322232 q=8 cube=(p21,edge7,n70) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 8, 0, None), (3, 21, 7, None)]
R=32323222 q=8 cube=(p21,edge9,n72) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=79 records=[(3, 1, 13, None), (2, 8, 1, None), (3, 21, 9, None)]
R=33223222 q=8 cube=(p21,edge10,n73) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=75 records=[(3, 1, 13, None), (2, 8, 1, None), (3, 21, 10, None)]
R=222322323 q=9 cube=(p21,edge13,n76) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=136 records=[(2, 2, 14, None), (2, 9, 4, None), (3, 21, 13, None)]
R=222323223 q=9 cube=(p21,edge13,n76) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=81 records=[(2, 9, 0, None), (3, 21, 13, None)]
R=222323323 q=9 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 3, 12, None), (2, 9, 4, None), (3, 21, 16, None)]
R=222333223 q=9 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 9, 0, None), (3, 21, 15, None)]
R=223222323 q=9 cube=(p21,edge9,n72) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (1, 1)] stop=1 L=77 records=[(2, 2, 14, None), (2, 6, 10, None), (2, 7, 19, 18), (3, 21, 9, None)]
R=223223232 q=9 cube=(p21,edge12,n75) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=135 records=[(2, 2, 14, None), (2, 9, 3, None), (3, 21, 12, None)]
R=223232223 q=9 cube=(p21,edge9,n72) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=132 records=[(2, 9, 0, None), (3, 21, 9, None)]
R=223232232 q=9 cube=(p21,edge12,n75) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=80 records=[(2, 3, 12, None), (2, 9, 3, None), (3, 21, 12, None)]
R=223233232 q=9 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 2, 14, None), (2, 9, 3, None), (3, 21, 15, None)]
R=223332232 q=9 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 9, 0, None), (3, 21, 14, None)]
R=232223232 q=9 cube=(p21,edge8,n71) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (1, 1)] stop=1 L=76 records=[(2, 2, 14, None), (2, 6, 9, None), (2, 7, 18, 17), (3, 21, 8, None)]
R=232232223 q=9 cube=(p21,edge9,n72) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=77 records=[(2, 9, 0, None), (3, 21, 9, None)]
R=232232322 q=9 cube=(p21,edge11,n74) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=134 records=[(2, 1, 16, None), (2, 9, 2, None), (3, 21, 11, None)]
R=232322232 q=9 cube=(p21,edge8,n71) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=131 records=[(2, 9, 0, None), (3, 21, 8, None)]
R=232322322 q=9 cube=(p21,edge11,n74) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=79 records=[(2, 1, 16, None), (2, 9, 2, None), (3, 21, 11, None)]
R=232332322 q=9 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 1, 16, None), (2, 9, 2, None), (3, 21, 14, None)]
R=233232223 q=9 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 9, 0, None), (3, 21, 12, None)]
R=233322322 q=9 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 1, 16, None), (2, 9, 2, None), (3, 21, 13, None)]
R=322232322 q=9 cube=(p21,edge7,n70) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (1, 1)] stop=1 L=75 records=[(2, 1, 16, None), (2, 6, 8, None), (2, 7, 17, 16), (3, 21, 7, None)]
R=322322232 q=9 cube=(p21,edge8,n71) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=76 records=[(2, 4, 10, None), (2, 6, 15, 13), (2, 7, 24, 23), (3, 21, 8, None)]
R=322323222 q=9 cube=(p21,edge10,n73) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=133 records=[(3, 1, 15, None), (2, 9, 1, None), (3, 21, 10, None)]
R=323222322 q=9 cube=(p21,edge7,n70) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=130 records=[(2, 1, 16, None), (2, 4, 12, None), (2, 7, 13, 12), (3, 21, 7, None)]
R=323222323 q=9 cube=(p21,edge10,n73) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 2, 14, None), (2, 6, 10, None), (2, 7, 19, 18), (3, 21, 10, None)]
R=323223222 q=9 cube=(p21,edge10,n73) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=78 records=[(3, 1, 15, None), (2, 9, 1, None), (3, 21, 10, None)]
R=323323222 q=9 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(3, 1, 15, None), (2, 9, 1, None), (3, 21, 13, None)]
R=332232223 q=9 cube=(p21,edge11,n74) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 9, 0, None), (3, 21, 11, None)]
R=332322232 q=9 cube=(p21,edge11,n74) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 9, 0, None), (3, 21, 11, None)]
R=333223222 q=9 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(3, 1, 15, None), (2, 9, 1, None), (3, 21, 12, None)]
R=2223222323 q=10 cube=(p21,edge8,n71) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=82 records=[(2, 2, 16, None), (2, 6, 12, None), (2, 7, 21, 20), (3, 21, 8, None)]
R=2223223323 q=10 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 10, 0, None), (3, 21, 18, None)]
R=2223232223 q=10 cube=(p21,edge4,n67) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=78 records=[(2, 6, 8, None), (2, 7, 17, 16), (3, 21, 4, None)]
R=2223233223 q=10 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 10, 0, None), (3, 21, 17, None)]
R=2223233323 q=10 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 10, 0, None), (3, 21, 18, None)]
R=2223323223 q=10 cube=(p21,edge15,n78) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=83 records=[(2, 10, 0, None), (3, 21, 15, None)]
R=2223333223 q=10 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 10, 0, None), (3, 21, 17, None)]
R=2232223223 q=10 cube=(p21,edge10,n73) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 3, 14, None), (2, 7, 10, None), (3, 21, 10, None)]
R=2232223232 q=10 cube=(p21,edge7,n70) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=81 records=[(2, 2, 16, None), (2, 6, 11, None), (2, 7, 20, 19), (3, 21, 7, None)]
R=2232232223 q=10 cube=(p21,edge10,n73) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (3, 6), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 10, 0, None), (3, 21, 10, None)]
R=2232233232 q=10 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 2, 16, None), (2, 10, 3, None), (3, 21, 17, None)]
R=2232322232 q=10 cube=(p21,edge3,n66) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=77 records=[(2, 6, 8, None), (2, 7, 16, 15), (3, 21, 3, None)]
R=2232332232 q=10 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 10, 0, None), (3, 21, 16, None)]
R=2232333232 q=10 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 2, 16, None), (2, 10, 3, None), (3, 21, 17, None)]
R=2233232223 q=10 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 10, 0, None), (3, 21, 14, None)]
R=2233232232 q=10 cube=(p21,edge14,n77) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=82 records=[(2, 3, 14, None), (2, 10, 3, None), (3, 21, 14, None)]
R=2233332232 q=10 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 10, 0, None), (3, 21, 16, None)]
R=2322232223 q=10 cube=(p21,edge0,n63) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=74 records=[(2, 4, 12, None), (2, 7, 13, 12), (3, 21, 0, None)]
R=2322232232 q=10 cube=(p21,edge9,n72) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=75 records=[(2, 3, 14, None), (2, 7, 9, None), (3, 21, 9, None)]
R=2322232322 q=10 cube=(p21,edge6,n69) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=80 records=[(2, 1, 18, None), (2, 6, 10, None), (2, 7, 19, 18), (3, 21, 6, None)]
R=2322322232 q=10 cube=(p21,edge9,n72) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (3, 6), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 4, 12, None), (2, 6, 17, 15), (2, 7, 26, 25), (3, 21, 9, None)]
R=2322332322 q=10 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 1, 18, None), (2, 10, 2, None), (3, 21, 16, None)]
R=2323222322 q=10 cube=(p21,edge2,n65) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=76 records=[(2, 1, 18, None), (2, 4, 14, None), (2, 7, 15, 14), (3, 21, 2, None)]
R=2323222323 q=10 cube=(p21,edge12,n75) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 2, 16, None), (2, 6, 12, None), (2, 7, 21, 20), (3, 21, 12, None)]
R=2323232223 q=10 cube=(p21,edge12,n75) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 10, 0, None), (3, 21, 12, None)]
R=2323232322 q=10 cube=(p21,edge14,n77) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 1, 18, None), (2, 10, 2, None), (3, 21, 14, None)]
R=2323322322 q=10 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 1, 18, None), (2, 10, 2, None), (3, 21, 15, None)]
R=2323332322 q=10 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 1, 18, None), (2, 10, 2, None), (3, 21, 16, None)]
R=2332232223 q=10 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 10, 0, None), (3, 21, 13, None)]
R=2332322232 q=10 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 10, 0, None), (3, 21, 13, None)]
R=2332322322 q=10 cube=(p21,edge13,n76) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=81 records=[(2, 1, 18, None), (2, 10, 2, None), (3, 21, 13, None)]
R=2333232223 q=10 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 10, 0, None), (3, 21, 14, None)]
R=2333322322 q=10 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 1, 18, None), (2, 10, 2, None), (3, 21, 15, None)]
R=3222322232 q=10 cube=(p21,edge1,n64) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=66 records=[(2, 4, 12, None), (2, 7, 12, None), (3, 21, 1, None)]
R=3222322322 q=10 cube=(p21,edge8,n71) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=74 records=[(2, 1, 18, None), (2, 7, 8, None), (3, 21, 8, None)]
R=3222323222 q=10 cube=(p21,edge5,n68) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=79 records=[(3, 1, 17, None), (2, 6, 9, None), (2, 7, 18, 17), (3, 21, 5, None)]
R=3223222322 q=10 cube=(p21,edge8,n71) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (3, 6), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 1, 18, None), (2, 4, 14, None), (2, 6, 16, 14), (2, 7, 25, 24), (3, 21, 8, None)]
R=3223222323 q=10 cube=(p21,edge11,n74) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (1, 1)] stop=1 L=79 records=[(2, 2, 16, None), (2, 6, 12, None), (2, 7, 21, 20), (3, 21, 11, None)]
R=3223223222 q=10 cube=(p21,edge11,n74) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (3, 6), (2, 1), (1, 1)] stop=1 L=81 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 11, None)]
R=3223323222 q=10 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 15, None)]
R=3232223222 q=10 cube=(p21,edge1,n64) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=75 records=[(3, 1, 17, None), (2, 4, 13, None), (2, 7, 14, 13), (3, 21, 1, None)]
R=3232223232 q=10 cube=(p21,edge11,n74) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 2, 16, None), (2, 6, 11, None), (2, 7, 20, 19), (3, 21, 11, None)]
R=3232232223 q=10 cube=(p21,edge11,n74) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=79 records=[(2, 10, 0, None), (3, 21, 11, None)]
R=3232322232 q=10 cube=(p21,edge11,n74) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 10, 0, None), (3, 21, 11, None)]
R=3232323222 q=10 cube=(p21,edge13,n76) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=83 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 13, None)]
R=3233223222 q=10 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 14, None)]
R=3233323222 q=10 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 15, None)]
R=3322322232 q=10 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 4, 12, None), (2, 6, 17, 15), (2, 7, 26, 25), (3, 21, 12, None)]
R=3323222322 q=10 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 1, 18, None), (2, 4, 14, None), (2, 7, 15, 14), (3, 21, 12, None)]
R=3323222323 q=10 cube=(p21,edge12,n75) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 2, 16, None), (2, 6, 12, None), (2, 7, 21, 20), (3, 21, 12, None)]
R=3323223222 q=10 cube=(p21,edge12,n75) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=80 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 12, None)]
R=3332232223 q=10 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 10, 0, None), (3, 21, 13, None)]
R=3332322232 q=10 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 10, 0, None), (3, 21, 13, None)]
R=3333223222 q=10 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(3, 1, 17, None), (2, 10, 1, None), (3, 21, 14, None)]
R=22223222323 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 2, 18, None), (2, 6, 14, None), (2, 7, 23, 22), (3, 21, 12, None)]
R=22223232223 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 11, 0, None), (3, 21, 12, None)]
R=22232222323 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 2, 18, None), (2, 11, 4, None), (3, 21, 16, None)]
R=22232223223 q=11 cube=(p21,edge9,n72) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=74 records=[(2, 3, 16, None), (2, 7, 12, None), (3, 21, 9, None)]
R=22232223232 q=11 cube=(p21,edge11,n74) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 2, 18, None), (2, 6, 13, None), (2, 7, 22, 21), (3, 21, 11, None)]
R=22232223323 q=11 cube=(p21,edge20,n83) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=85 records=[(2, 11, 0, None), (3, 21, 20, None)]
R=22232232223 q=11 cube=(p21,edge5,n68) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=70 records=[(2, 7, 8, None), (3, 21, 5, None)]
R=22232233223 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 4, 14, None), (2, 11, 1, None), (3, 21, 19, None)]
R=22232233323 q=11 cube=(p21,edge20,n83) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=85 records=[(2, 11, 0, None), (3, 21, 20, None)]
R=22232322232 q=11 cube=(p21,edge11,n74) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=76 records=[(2, 11, 0, None), (3, 21, 11, None)]
R=22232322323 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=140 records=[(2, 2, 18, None), (2, 11, 4, None), (3, 21, 17, None)]
R=22232323223 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=85 records=[(2, 11, 0, None), (3, 21, 17, None)]
R=22232323323 q=11 cube=(p21,edge20,n83) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=85 records=[(2, 3, 16, None), (2, 11, 4, None), (3, 21, 20, None)]
R=22232333223 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 11, 0, None), (3, 21, 19, None)]
R=22232333323 q=11 cube=(p21,edge20,n83) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=85 records=[(2, 11, 0, None), (3, 21, 20, None)]
R=22233222323 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 2, 18, None), (2, 11, 4, None), (3, 21, 16, None)]
R=22233232223 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 11, 0, None), (3, 21, 16, None)]
R=22233233223 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 11, 0, None), (3, 21, 19, None)]
R=22233323223 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=85 records=[(2, 11, 0, None), (3, 21, 17, None)]
R=22233333223 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 11, 0, None), (3, 21, 19, None)]
R=22322223232 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 15, None)]
R=22322232223 q=11 cube=(p21,edge1,n64) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=66 records=[(2, 4, 14, None), (2, 6, 16, 14), (2, 7, 25, 24), (3, 21, 1, None)]
R=22322232232 q=11 cube=(p21,edge8,n71) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=73 records=[(2, 3, 16, None), (2, 7, 11, None), (3, 21, 8, None)]
R=22322232322 q=11 cube=(p21,edge10,n73) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=75 records=[(2, 1, 20, None), (2, 6, 12, None), (2, 7, 21, 20), (3, 21, 10, None)]
R=22322233223 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 11, 0, None), (3, 21, 19, None)]
R=22322233232 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 19, None)]
R=22322322232 q=11 cube=(p21,edge4,n67) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=69 records=[(2, 4, 14, None), (2, 6, 19, 17), (2, 7, 28, 27), (3, 21, 4, None)]
R=22322332232 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 11, 0, None), (3, 21, 18, None)]
R=22322333232 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 19, None)]
R=22323222322 q=11 cube=(p21,edge10,n73) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=75 records=[(2, 1, 20, None), (2, 4, 16, None), (2, 7, 17, 16), (3, 21, 10, None)]
R=22323222323 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 2, 18, None), (2, 6, 14, None), (2, 7, 23, 22), (3, 21, 14, None)]
R=22323223232 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=139 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 16, None)]
R=22323232223 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 11, 0, None), (3, 21, 14, None)]
R=22323232232 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=84 records=[(2, 3, 16, None), (2, 11, 3, None), (3, 21, 16, None)]
R=22323233232 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 19, None)]
R=22323332232 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 11, 0, None), (3, 21, 18, None)]
R=22323333232 q=11 cube=(p21,edge19,n82) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 19, None)]
R=22332223232 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 2, 18, None), (2, 11, 3, None), (3, 21, 15, None)]
R=22332232223 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 11, 0, None), (3, 21, 15, None)]
R=22332322232 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 11, 0, None), (3, 21, 15, None)]
R=22332332232 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 11, 0, None), (3, 21, 18, None)]
R=22333232223 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 11, 0, None), (3, 21, 16, None)]
R=22333232232 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=84 records=[(2, 3, 16, None), (2, 11, 3, None), (3, 21, 16, None)]
R=22333332232 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 11, 0, None), (3, 21, 18, None)]
R=23222232322 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 14, None)]
R=23222322232 q=11 cube=(p21,edge0,n63) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=65 records=[(3, 4, 10, None), (2, 6, 15, None), (2, 7, 24, 23), (3, 21, 0, None)]
R=23222322322 q=11 cube=(p21,edge7,n70) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=72 records=[(2, 1, 20, None), (2, 7, 10, None), (3, 21, 7, None)]
R=23222323222 q=11 cube=(p21,edge9,n72) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=74 records=[(3, 1, 19, None), (2, 6, 11, None), (2, 7, 20, 19), (3, 21, 9, None)]
R=23222332232 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 11, 0, None), (3, 21, 18, None)]
R=23222332322 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 18, None)]
R=23223222322 q=11 cube=(p21,edge3,n66) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=68 records=[(2, 1, 20, None), (2, 4, 16, None), (2, 6, 18, 16), (2, 7, 27, 26), (3, 21, 3, None)]
R=23223222323 q=11 cube=(p21,edge13,n76) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (1, 1)] stop=1 L=81 records=[(2, 2, 18, None), (2, 6, 14, None), (2, 7, 23, 22), (3, 21, 13, None)]
R=23223232223 q=11 cube=(p21,edge13,n76) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=136 records=[(2, 11, 0, None), (3, 21, 13, None)]
R=23223232322 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=86 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 16, None)]
R=23223322322 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 17, None)]
R=23223332322 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 18, None)]
R=23232223222 q=11 cube=(p21,edge9,n72) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=74 records=[(3, 1, 19, None), (2, 4, 15, None), (2, 7, 16, 15), (3, 21, 9, None)]
R=23232223232 q=11 cube=(p21,edge13,n76) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 2, 18, None), (2, 6, 13, None), (2, 7, 22, 21), (3, 21, 13, None)]
R=23232232223 q=11 cube=(p21,edge13,n76) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=81 records=[(2, 11, 0, None), (3, 21, 13, None)]
R=23232232322 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=138 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 15, None)]
R=23232322232 q=11 cube=(p21,edge13,n76) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 11, 0, None), (3, 21, 13, None)]
R=23232322322 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=83 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 15, None)]
R=23232332322 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 18, None)]
R=23233232223 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 11, 0, None), (3, 21, 16, None)]
R=23233232322 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=86 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 16, None)]
R=23233322322 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 17, None)]
R=23233332322 q=11 cube=(p21,edge18,n81) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=83 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 18, None)]
R=23322232322 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 14, None)]
R=23322322232 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 4, 14, None), (2, 6, 19, 17), (2, 7, 28, 27), (3, 21, 14, None)]
R=23323222322 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=79 records=[(2, 1, 20, None), (2, 4, 16, None), (2, 7, 17, 16), (3, 21, 14, None)]
R=23323222323 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (3, 3), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 2, 18, None), (2, 6, 14, None), (2, 7, 23, 22), (3, 21, 14, None)]
R=23323232223 q=11 cube=(p21,edge14,n77) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=84 records=[(2, 11, 0, None), (3, 21, 14, None)]
R=23323322322 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 17, None)]
R=23332232223 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 11, 0, None), (3, 21, 15, None)]
R=23332322232 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=80 records=[(2, 11, 0, None), (3, 21, 15, None)]
R=23332322322 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (1, 1)] stop=1 L=83 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 15, None)]
R=23333232223 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(2, 11, 0, None), (3, 21, 16, None)]
R=23333322322 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 1, 20, None), (2, 11, 2, None), (3, 21, 17, None)]
R=32222323222 q=11 cube=(p21,edge13,n76) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=78 records=[(3, 1, 19, None), (2, 11, 1, None), (3, 21, 13, None)]
R=32223222322 q=11 cube=(p21,edge10,n73) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=75 records=[(3, 4, 10, None), (2, 7, 13, None), (3, 21, 10, None)]
R=32223222323 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 2, 18, None), (2, 6, 14, None), (2, 7, 23, 22), (3, 21, 12, None)]
R=32223223222 q=11 cube=(p21,edge6,n69) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=71 records=[(3, 1, 19, None), (2, 7, 9, None), (3, 21, 6, None)]
R=32223232223 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=77 records=[(2, 11, 0, None), (3, 21, 12, None)]
R=32223322322 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 1, 20, None), (2, 8, 8, None), (3, 21, 17, None)]
R=32223323222 q=11 cube=(p21,edge17,n80) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=82 records=[(3, 1, 19, None), (2, 11, 1, None), (3, 21, 17, None)]
R=32232223222 q=11 cube=(p21,edge2,n65) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=67 records=[(3, 1, 19, None), (2, 4, 15, None), (2, 6, 17, 15), (2, 7, 26, 25), (3, 21, 2, None)]
R=32232223223 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (3, 2), (2, 1), (1, 1)] stop=1 L=78 records=[(2, 3, 16, None), (2, 7, 12, None), (3, 21, 12, None)]
R=32232223232 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (1, 1)] stop=1 L=80 records=[(2, 2, 18, None), (2, 6, 13, None), (2, 7, 22, 21), (3, 21, 12, None)]
R=32232232223 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (3, 6), (2, 1), (1, 1)] stop=1 L=82 records=[(2, 11, 0, None), (3, 21, 12, None)]
R=32232322232 q=11 cube=(p21,edge12,n75) cont=[(3, 21), (2, 2), (2, 2), (2, 1), (3, 1), (2, 6), (2, 6), (2, 1)] stop=1 L=135 records=[(2, 11, 0, None), (3, 21, 12, None)]
R=32232323222 q=11 cube=(p21,edge15,n78) cont=[(3, 21), (2, 3), (2, 3), (2, 1), (3, 1), (3, 7), (2, 1), (1, 1)] stop=1 L=85 records=[(3, 1, 19, None), (2, 11, 1, None), (3, 21, 15, None)]
R=32233223222 q=11 cube=(p21,edge16,n79) cont=[(3, 21), (2, 1), (1, 1)] stop=1 L=81 records=[(3, 1, 19, None), (2, 11, 1, None), (3, 21, 16, None)]
~~~~

---

# Appendix T. Original multiagent research prompt PDF

The unmodified binary file `curling_number_prompt (1).pdf` is included in the ZIP under `sources/`. It is not embedded in this Markdown file. The prompt enforces calibrated exact curling-number computation, explicit case analysis, and strict status labeling.

---

# Appendix U. File manifest and SHA-256 checksums

| Path | Bytes | SHA-256 |
|---|---:|---|
| `sources/Curling_Number_Conjecture_Full_Handoff_Ledger_2026-07-26.md` | 33,177 | `77dd9d1f73ddd7445abaac6f41ddfd863ee6a53bd86ce14f4e73de6194386ee8` |
| `sources/Curling_Number_Frontier_Descent_Memo.md` | 5,965 | `91f32d35f4257b63b3e53ca13022462f3b8317f02d5e317ef25f9cecf9b17091` |
| `sources/Curling_Number_Proof_Ledger.md` | 4,647 | `37ba885c795b76505fb15cc33bedd59629d151645cc7c2554add88d29417f441` |
| `sources/Curling_Number_Research_Ledger(1)(1).md` | 2,349 | `634866c7503ae1a2c610925160b07a26790597ed15008b8bfc30e76a6e58c1c7` |
| `sources/Curling_q_monotonicity_checkpoint_2026-07-25.md` | 6,980 | `c7eb2010f09202001ec8eb517a4c62e2042c0ee276d1dd45e8f71c9e21c30a89` |
| `sources/_tmp_autonomous_square_report.txt` | 49,178 | `2741260f50093052b5671f1fb41f983ebb1863a6fe95d8312d8998a3c8e45a94` |
| `sources/audit_all_square_replay.cpp` | 4,571 | `f7fcb7b75529491b6214dbfc6b5aa96e8c6e513c80d3ac0f9bc5224ef9667f02` |
| `sources/audit_all_square_replay.err` | 828 | `02755c1e62261f40e658d8cd9ce4288cc5e903f3203747e21163ce38445b9fbe` |
| `sources/audit_all_square_replay.out` | 88 | `b4a18ffc268fc96d8e4c3af93bfd8705647c69938f6635be25ba0768a7504fbf` |
| `sources/audit_bridge_promotion.cpp` | 1,930 | `88c3d72ac6973e6a8961e64c1ed8a342aec12466c299cef2764b27603986a132` |
| `sources/audit_bridge_promotion.out` | 42 | `baa211d2bd591926eefd17c6de080d708ba02ed46a5fa44e1aa7f89cea99e209` |
| `sources/curling_number_prompt (1).pdf` | 91,933 | `b9edf21083fe618315220b93988a36aaa12742d2f552fe26078ad7fd708352f1` |
| `sources/curling_number_proof_ledger.md` | 13,844 | `ba59c2496dbf92eefd6887c9af75ef4746301f88b976cebc996bad19eab419c8` |
| `sources/curling_number_research_ledger.md` | 7,648 | `b0bad5c7e07c4c6445b08e1ba4ffe95631bb79f2fa2581b606eb3ce15147c209` |
| `sources/curling_q_monotonicity_audit.cpp` | 11,246 | `14ff308e5bd82a3a0bfed4983b7d2d5c369e94eaefeed5d5dbbfea8f87147428` |
| `sources/curling_research_tools.py` | 2,802 | `2c3612dac67935b5cbdf1970565643ecca8ff0b6c0077c95084e028c0a66c751` |
| `sources/replay_local_promo2.cpp` | 2,127 | `291cf25c91eeb2c5758589ff65dd9c4c210770382d277d3b791ee3e2f89874bf` |
| `sources/replay_local_promo2.out` | 51 | `1c8c7641b44deb9758e404741bb1422c4406e41a8635db68b7401cf01a58d3d5` |
| `sources/verify_part3_examples.out` | 840 | `296a797b0b4e0dabd6a72cfcf7a4a38f5ed5012deb5f2e2ca1c9798885c94513` |
| `sources/verify_part3_examples.py` | 3,005 | `2831257e4737728e92f8d8e810351b594999bbca60e6ccbeb749e52d8d46551d` |
