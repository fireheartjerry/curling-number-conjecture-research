# Decision log

This file records research and repository decisions in chronological order.
Entries are append-only; superseded decisions are marked, not deleted.

## D-001 — GitHub is the canonical durable state

- Date: 2026-07-27
- Status: active
- Decision: use the private repository
  `fireheartjerry/curling-number-conjecture-research` as the source of truth.
- Reason: local and external ChatGPT work previously lived in disconnected
  locations with conflicting status labels.
- Evidence: repository audit and provenance documents; initial commit
  `e865fd9`.

## D-002 — Preserve imported evidence byte-for-byte

- Date: 2026-07-27
- Status: active
- Decision: do not normalize whitespace or line endings inside `external/` or
  `archive/`.
- Reason: imported hashes and provenance matter more than cosmetic diffs.
- Consequence: historical Markdown trailing spaces are accepted.

## D-003 — Exclude vendored runtimes and generated caches

- Date: 2026-07-27
- Status: active
- Decision: omit `.vendor`, executable/runtime binaries, Python caches, and
  test caches from version control.
- Reason: these are reproducible dependencies, not research artifacts.
- Replacement: declare Python dependencies in `requirements.txt`.

## D-004 — Stop the cloud continuation

- Date: 2026-07-27
- Status: active
- Decision: cancel the newly created ChatGPT Work cloud task and continue
  locally.
- Reason: explicit user direction.
- Verification: the cloud page exposed no `Stop answering` control after
  cancellation and returned to an idle prompt state.

## D-005 — Attack the repaired synchronization wall first

- Date: 2026-07-27
- Status: active
- Decision: prioritize an exact Generated Two-Cube Synchronization statement,
  a matching bounded falsifier, and separate treatment of Cells A, B, and C.
- Alternatives considered:
  1. audit every earlier lemma first;
  2. expand bounded censuses without repairing the theorem;
  3. attack downstream replay/monotonicity conditionally.
- Reason: the repository audit identifies synchronization as the nearest
  load-bearing open wall, while static geometry already has impostors.

## D-006 — Record failures as durable progress

- Date: 2026-07-27
- Status: active
- Decision: document refuted lemmas, failed proof branches, counterexamples,
  cutoff effects, and assumption changes alongside successful results.
- Reason: repeated rediscovery of invalid strengthenings is a major research
  cost in the inherited corpus.

## D-007 — Use theorem-first proof/falsification checkpoints

- Date: 2026-07-27
- Status: active
- Decision: a new lemma is not promoted from `CONJECTURED` or
  `PROVISIONAL-NL` until its exact quantifiers are mirrored in executable
  bounded checks where finite testing is meaningful and its endpoint algebra
  is independently audited.
- Reason: several inherited computations checked weaker generation predicates
  than the prose claimed.

## D-008 — Include \(G\) and exclude \(H\) from synchronization

- Date: 2026-07-27
- Status: active
- Decision: define the proper pre-completion synchronization set as
  \[
  \mathcal I=\{E_\ell:0\le\ell\le m\}
  \cup\{F_\ell:0\le\ell<m\}.
  \]
  Thus \(G=E_m\) is included and \(H=F_m\) is excluded.
- Reason: \(G\) is the completed first generated copy of \(U\) and still
  precedes record-square completion, so its canonical data are legitimately
  available to synchronization. By contrast, \(H\) is the terminal completed
  state with \(\pi(H)=P\); including it would make the desired conclusion
  \(\max_{W\in\mathcal I}\pi(W)\ge P\) tautological.
- Consequence: strict-record minimality is applied separately as a
  contradiction corollary, not embedded circularly in the combinatorial
  synchronization implication.

## D-009 — Fix the \(\kappa=1\) sentinel and bound extractor scope

- Date: 2026-07-27
- Status: active
- Decision: use the executable convention
  \[
  \pi(W)=|W|\quad\text{when }\kappa(W)=1,
  \]
  and use the shortest maximizing suffix period when \(\kappa(W)\ge2\).
  Separately, retain (G2CS) as a general record-free combinatorial core, while
  restricting the planned bounded extractor to fully generated strict-record
  applications whose terminal \(Y^2\) starts at or after the seed boundary.
- Reason: minimizing the displayed \(X^1\) period would give
  \(\pi((2,3))=1\), contradicting the inherited executable convention and the
  planned regression value \((\kappa,\pi)=(1,2)\). The full-generation filter
  is also materially stronger than the general core and must not be hidden in
  an apparently exhaustive antecedent count.
- Consequence: the \(\kappa=1\) value is explicitly a sentinel, not a word
  periodicity claim. It does not affect any state with \(\kappa\ge2\), nor the
  intended binary \(\{2,3\}\) synchronization set. Future bounded results must
  be labeled as evidence for the fully generated strict-record specialization,
  not as a scan of every general-core antecedent.

## D-010 — Preserve generated trace semantics in synchronization evaluation

- Date: 2026-07-27
- Status: active
- Decision: generated-state traces include both their starting and terminal
  states. The synchronization evaluation family includes \(G\) and excludes
  \(H\).
- Reason: these endpoints directly encode the canonical theorem's evaluation
  boundary without making terminal-period conclusions tautological.
- Consequence: evaluation order and duplicate states are preserved for trace
  provenance. They are irrelevant to a maximum \(\pi\) calculation, but remain
  useful when auditing how a state was reached.

## D-011 — Name and freeze the synchronization evaluation family

- Date: 2026-07-27
- Status: active
- Decision: rename the ordered trace API to
  `synchronization_evaluation_states` and normalize every supplied inner state
  to an immutable tuple.
- Reason: the old name implied a mathematical set despite preserved order and
  duplicates, while immutable recorded words prevent later mutation of caller
  lists from rewriting trace provenance.
- Consequence: the exact generated-symbol mismatch text remains
  `expected {expected} but generated {actual}` until candidate extraction
  establishes a need for structured diagnostic errors.

## D-012 — Trace capped orbits and extract only fully generated record squares

- Date: 2026-07-27
- Status: active
- Decision: interpret `step_limit` as the maximum number of symbols appended.
  A capped trace evaluates and records both the seed state at time \(0\) and
  the state after exactly `step_limit` appends. It terminates as `hit_one`
  when that evaluation has exponent \(1\), including at the cap; otherwise it
  terminates explicitly as `step_limit`. Every exponent other than \(1\),
  including \(4\) and above, is appended and traced.
- Generation predicates: for an event with state \(W\), exponent \(k\),
  canonical period \(p\), and seed length \(n\), the final displayed copy is
  generated exactly when
  \[
  |W|-p\ge n,
  \]
  while the entire displayed maximal power is generated exactly when
  \[
  |W|-kp\ge n.
  \]
  Equality counts as generated in both cases.
- Strict-record convention: a terminal event is a strict canonical-period
  record only when its period exceeds every prior event's canonical period.
  Prior events of every exponent participate, not only squares.
- Candidate identities: a counted terminal square has period \(P\), with a
  prior square \(G\) at time \(t_H-P\) and canonical period \(q\), where
  \[
  b=P-q>0,\qquad a=2q-P>0.
  \]
  Writing \(R\) for the length-\(q\) suffix of \(G\),
  \(B\) for the length-\(b\) suffix of \(R\), \(A=R[0:q-b]\), and \(Y=BR\),
  extraction requires
  \[
  R=AB,\quad G=LR^2,\quad
  H=G\,Y=LR^2BR,\quad H\text{ ends in }Y^2.
  \]
  The event at time \(t_G-q\) must be present, and the stored trace must replay
  the generated \(R\) from that event to \(G\) and the generated \(Y\) from
  \(G\) to \(H\), one append at a time.
- Scope: the bounded extractor counts only strict-record candidates for which
  the entire terminal \(Y^2\) is generated from the seed boundary. Generating
  merely the final copy is insufficient. A bounded scan is computational
  evidence for this fully generated specialization only; it is neither a
  proof nor an exhaustive scan of the general record-free (G2CS) core.

## D-013 — Fail closed on candidate provenance defects

- Date: 2026-07-27
- Status: superseded by D-014
- Decision: candidate extraction rejects malformed provenance rather than
  inferring generation from static endpoint identities. Required event words
  must be nonempty; every required timestamp must occur exactly once; and
  every stored canonical witness, word length, seed prefix, and one-symbol
  orbit transition across the generated spans must agree.
- Adversarial boundary: a missing or duplicate interior event invalidates the
  candidate. So does an internally self-consistent replacement event whose
  word has the right length and seed prefix but breaks contiguous replay,
  even when the second-\(R\), \(G\), and \(H\) endpoints still satisfy all
  displayed concatenation identities.
- Record accounting: strictness compares the terminal period with canonical
  periods of every prior event in supplied trace order. Prior cubes and other
  nonsquare exponents can therefore suppress a square candidate just as a
  prior square can.
- Reason: endpoint algebra establishes word geometry, not actual orbit
  provenance. Failing closed prevents incomplete, duplicated, empty, or
  corrupted traces from manufacturing evidence for the fully generated
  strict-record specialization.

## D-014 — Validate the whole chronological orbit before record extraction

- Date: 2026-07-27
- Status: active
- Decision: before record accounting or candidate extraction, validate the
  entire supplied event sequence as one complete chronological orbit prefix.
  Nonempty input must have times exactly \(0,1,\ldots,n-1\) in supplied order,
  one shared positive seed length and seed prefix, the corresponding
  time/length relation, nonempty words, correct canonical witnesses, and every
  adjacent one-symbol orbit transition. An exponent-\(1\) event may occur only
  as the final event. Empty input still yields no candidates.
- Record accounting: only after whole-trace validation succeeds, scan the
  actual events chronologically and update the prior canonical-period maximum
  from every exponent. Malformed, omitted, duplicated, reordered, or
  mixed-seed events invalidate the whole extraction and never alter record
  state. Candidate-local span checks remain as defense in depth.
- Correction: D-013's supplied-order record rule and candidate-local
  provenance checks were too weak. For seed `22322232`, the real orbit has a
  period-\(7\) square at time \(20\) and another candidate-shaped period-\(7\)
  square at time \(41\). Deleting only time \(20\) previously made time \(41\)
  appear to be a strict record, manufacturing a false positive from an
  incomplete trace.
- Reason: strict-record status is a property of the complete orbit history,
  not of whichever subsequence reaches the extractor. Chronology and complete
  provenance must therefore be established before any record comparison.

## D-015 — Isolate all-exponent record accounting by rebasing at a cube

- Date: 2026-07-27
- Status: active
- Decision: test nonsquare record accounting on the orbit rebased at time
  \(52\) of seed `22323222322`. The rebased seed state has canonical data
  \((\kappa,\pi)=(3,21)\) at time \(0\), while the candidate-shaped,
  fully-generated square occurs at rebased time \(16\) with canonical data
  \((2,7)\).
- Isolation: every square strictly before rebased time \(16\) has canonical
  period at most \(6\). Thus a square-only record scan would incorrectly treat
  period \(7\) as a strict record; the time-\(0\) cube's period \(21\) is the
  causal reason the extractor rejects it.
- Reason: in the unre-based orbit, earlier period-\(7\) squares also blocked
  the later square, so that regression did not independently prove that
  nonsquare exponents participate in strict-record accounting.

## D-016 — Audit Generated Two-Cube candidates before classification

- Date: 2026-07-27
- Status: active
- Decision: a `RecordSquareCandidate` is admissible evidence only after it is
  found again by `extract_record_square_candidates(events)`. An arbitrary or
  mutated dataclass is `invalid_provenance` with the missing bridge hypothesis
  and is not audited as a promotion root or first failure. Static word
  identities never substitute for actual orbit generation: for every cut
  \(j\), both formula families \(E_\ell\) and \(F_\ell\) are checked against
  the stored full-state words, times, curling numbers, and shortest maximizing
  periods.
- Interval convention: a first-failure report computes \(\mathcal I\) from
  every \(E_\ell\) through \(G=E_m\) and every \(F_\ell\) with \(\ell<m\), so
  \(G\) is included and \(H=F_m\) is excluded. At \(F\), coordinates are
  zero-based and half-open. When the G2CS cube premises hold, a later
  canonical \(r\)-cube with `cube_start >= ybt_start`, including equality, is
  internal Cell C. Only an external cube may be Cell A (`r=q`) or Cell B
  (`q<r<P`); every other or non-cube failure is unclassified.
- Reason: endpoint algebra and standalone continuation are not provenance for
  the two actual generated \(U\)-windows, and the Cell partition is meaningful
  only for a genuine canonical cube at \(F\).

## D-017 — Scan the bounded fully generated specialization through length 18

- Date: 2026-07-27
- Status: `COMPUTED`
- Command:
  ```
  python research/generated_two_cube_falsifier.py --max-seed-length 18 --step-limit 500 > research/outputs/generated_two_cube_scan_2026-07-27.txt
  ```
- Calibration: terminal lengths `5,66,142` reproduced exactly.
- Caps and results: all `524286` binary seeds of lengths `1..18` were
  enumerated. All `524286` trajectories hit curling number one within the
  explicit `500`-append cap, so `capped=0`. The repaired whole-power boundary
  \(n-2p\ge n_{\mathrm{seed}}\) yielded `5016` fully generated strict-record
  candidates. All `5016` had promotion bridge roots; first failures, G2CS
  antecedents, verified antecedents, counterexamples, and Cell
  A/B/C/unclassified counts were all zero.
- Reproduction: an independent rerun took `20.326` seconds on the reporting
  machine and was byte-identical to the preserved output; both SHA-256 digests
  were `C461FF476D8F274C1203864A06B2C16F0312B398F19A71F01310C4DF4EB2B24F`.
- Scope: these are bounded `fully_generated_specialization` results only.
  Zero bounded failures or counterexamples is **NOT_A_PROOF** of bridge
  promotion, the Generated Two-Cube implication, or the Curling Number
  Conjecture.

## D-018 — Gate synchronization cells on the complete local antecedent

- Date: 2026-07-27
- Status: active
- Decision: compute the later canonical cube coordinate and classify Cell
  A/B/C only for a genuine local G2CS antecedent: the failed position expects
  \(3\), the standalone state has curling number \(2\), both actual paired
  states \(E\) and \(F\) have curling number \(3\), and the audited \(G,H\)
  endpoint data have their required exponents and periods. Every other first
  failure records `cube_start=None` and Cell `unclassified`.
- Clarification: standalone curling number \(2\) is the target no-cube clause;
  the visible square suffix remains. Standalone curling number \(4\) is a
  higher-power mismatch, not a no-cube state, and is outside the Cell A/B/C
  partition even when the paired \(E,F\) states are genuine cubes.
- Reason: Cell geometry describes the canonical cube at \(F\) within the
  repaired \(3\to2\) synchronization specialization. Classifying anomalous
  failures before all local antecedent clauses hold would misstate diagnostic
  evidence and inflate Cell counts.

## D-019 — Preserve a positive executable path through the G2CS audit

- Date: 2026-07-27
- Status: active
- Decision: retain a regression that takes the reviewed seed `23222323`
  candidate at cut \(j=3\) and injects the target standalone mismatch
  \(3\to2\). The audit must mark the complete local antecedent, evaluate its
  strict-record period maximum as a counterexample, classify the actual
  \(F\)-cube as Cell C, and aggregate antecedent/counterexample/Cell counts
  without counting a promotion or verified implication.
- Scope: the injected standalone witness is a test seam for the otherwise
  unobserved report branch. It is not the canonical witness of that reviewed
  word and therefore is not a computed G2CS counterexample.
- Reason: negative and zero-count tests alone could pass if the antecedent
  predicate were accidentally made permanently false.

## D-020 — Fail closed outside helper mathematical domains

- Date: 2026-07-27
- Status: active
- Decision: `check_standalone_promotion` rejects an empty root. The pure Cell
  classifier requires nonnegative half-open start coordinates,
  \(0<q<P\), and \(0<r<P\). It does not constrain the relative start
  positions, and legitimate external cases with \(r<q\) remain
  `unclassified`.
- Reason: empty roots have no promotion positions, while negative coordinates,
  degenerate bridge periods, and \(r\ge P\) are outside the repaired Cell
  geometry. Silently assigning such inputs to Cell C would manufacture a
  mathematical classification.

## D-021 — Reuse validated extraction inside the bounded scanner

- Date: 2026-07-27
- Status: active
- Decision: keep public `audit_record_square_candidate(events, candidate)`
  fail-closed by re-extracting and checking candidate membership. Inside the
  scanner only, pass the candidates returned by its single validated
  extraction to a private batch audit core.
- Verification: the length-eight regression audits `510` binary-seed orbits,
  finds the same `2` candidates, and records exactly `510` extractor calls
  rather than `512`.
- Reason: provenance revalidation is mandatory at the public boundary, but
  repeating the complete extraction for objects just returned by that same
  scanner call adds cost without adding evidence.

## D-022 — Close Cell B directly before Cell A

- Date: 2026-07-27
- Status: `PROVED-NL`
- Decision: audit Cell B before Cell A because a direct contradiction was
  found from the repaired G2CS statement and
  \(\max_{W\in\mathcal I}\pi(W)<P\). For the external canonical \(r\)-cube
  at \(F\), Fine--Wilf forces \(s=b+j\le r-\gcd(r,P)-1<r\). Deleting \(BT\)
  exposes an \(r\)-square at \(G\); exact suffix comparison gives period
  \(c=r-q\) on \(R\), no-square data at \(G\) gives \(c>q/2\), and the
  continued cube gives period \(\delta=b-c=P-r\) on \(B\). Since
  \(0<\delta<c\), \(B\) ends in a \(\delta\)-square, contradicting
  \(\pi(G)=q\).
- Deviation: the planned union-find and paired-generation enumeration are
  unnecessary for this cell. The proof derives every normalized relation
  from half-open intervals and does not cite inherited provisional normal
  forms. It does not need the early cube at \(E\), the standalone
  promotion-failure clause, or strict-record minimality once Cell B is
  entered.
- Executable audit: `tests/test_generated_two_cube_cells.py` exhausts binary
  roots through \(q=12\). Its exact `84` retained word-parameter cases all
  satisfy the derived period-\(\delta\) and terminal-square slices. This is a
  bounded index certificate, not the proof.
- Scope: `PROVED-NL` is a natural-language closure of Cell B only. Cells A
  and C remain open, so this does not prove G2CS or the Curling Number
  Conjecture.

## D-023 — Separate the natural full precompletion target from G2CS-I

- Date: 2026-07-27
- Status: active
- Decision: preserve the stronger two-window family \(\mathcal I\) and its
  implication (G2CS-\(\mathcal I\)) unchanged in mathematical content and
  open in status. Separately define the actual bridge states
  \[
  K_h=S_{t_0+m+h}=LR^2(BT)[0:h]\qquad(0\le h\le b+j)
  \]
  and the natural full proper precompletion family
  \[
  \mathcal J=\{S_t:t_0\le t<t_H\}.
  \]
  The new implication (G2CS-\(\mathcal J\)) has exactly the same structural,
  generation, and canonical-data antecedents and conclusion
  \(\max_{W\in\mathcal J}\pi(W)\ge P\).
- Endpoint semantics: \(\mathcal J\) is the union of the early, bridge, and
  later windows. It identifies \(G=E_m=K_0\) and \(F=K_{b+j}=F_0\), includes
  every state through \(F_{m-1}\), and excludes \(H=F_m\). The helper
  `bridge_inclusive_precompletion_states` normalizes supplied states, checks
  both endpoint overlaps, includes \(G,F\) once, and fails closed on
  degenerate traces.
- Quantifier boundary: \(\mathcal I\subseteq\mathcal J\), so the
  \(\mathcal J\) implication is weaker. A witness in the omitted bridge is
  not retroactively declared to lie in \(\mathcal I\). This is not quantifier
  laundering: both targets remain named, their antecedents are identical, and
  their statuses are tracked independently.
- Strict-record reason: every state in \(\mathcal J\) still occurs strictly
  before \(H\). Therefore (G2CS-\(\mathcal J\)) is already sufficient for
  the intended strict-record contradiction even though it does not prove
  (G2CS-\(\mathcal I\)).

## D-024 — Close Cell A only through the genuine bridge state

- Date: 2026-07-27
- Status: `BRIDGE-PROVED-NL`
- Decision: in external Cell A, the later canonical \(q\)-cube and
  Fine--Wilf equality endpoint force
  \[
  b+j\le q-\gcd(q,b)-1<q.
  \]
  Exact \(q\)-periodic coordinates then give
  \(BT=R[0:b+j]\), make \(B\) a border of \(R\), give
  \(R[0:j]=R[b:b+j]\), and force \(b<q/2\).
- Actual-generation step: the first \(q\) labels generated from \(E\) are
  \(UT\), so
  \[
  K=S_{t_0+q}=LR^2T.
  \]
  Its next label is \(R[j]=3\). The boundary \(j=0\) contradicts
  \(\kappa(G)=2\) immediately; otherwise \(t_G<t_0+q<t_F\), so \(K\) is a
  genuine proper bridge state.
- Proof result: under the temporary assumptions
  \(\pi(E),\pi(K)<P\), a canonical-period overlap at \(K\) first forces
  \(\pi(K)=q\). Writing \(C=UT\), the states then end in \(C^3\) at \(K\)
  and \(C^2\) at \(E\). Fine--Wilf on \(C^2\) would make
  \(t=\pi(E)-q\) a period of \(C\) with \(0<t<b\). The audited
  Border--conjugate lemma would give a square suffix of \(R\), contradicting
  \((\kappa(G),\pi(G))=(2,q)\). Therefore
  \[
  \max\{\pi(E),\pi(S_{t_0+q})\}\ge P.
  \]
- Border--conjugate audit: the preserved four-case proof now quantifies the
  full period-extension range, writes both Case 4 index equalities
  explicitly, meets the overlap Fine--Wilf threshold at its exact endpoint,
  glues the two periodic pieces through an overlap of at least one full gcd
  block, and derives \(2g\le b\) before asserting the terminal square.
  `tests/test_border_conjugate.py` independently checks every binary root
  through length `15` and every ternary root through length `11`, with every
  integer \((b,j,t)\) satisfying the lemma hypotheses. It retains exactly
  `1776` binary plus `690` ternary tuples (`2466` total) and finds zero
  failures.
- Plan deviation: actual chronology supplied the decisive intermediate state,
  so the planned broad static/paired survivor search was replaced by the
  exhaustive load-bearing auxiliary-lemma audit. The resulting witness may be
  \(K\notin\mathcal I\), so Cell A is `OPEN` for
  (G2CS-\(\mathcal I\)) and `BRIDGE-PROVED-NL` only for
  (G2CS-\(\mathcal J\)) and the strict-record route. Cell C remains open.
  This does not prove either full synchronization statement, complete bridge
  promotion, or the Curling Number Conjecture.

## D-025 — Search Cell C by integer geometry and equality classes

- Date: 2026-07-27
- Status: active
- Decision: replace the inherited ambiguous Cell C prose split by exact
  coordinates in \(V=YBT=BRBT\). With \(s=b+j\), \(N=P+s\), define
  \[
  \alpha=N-3r,\quad\beta=N-2r,\quad\gamma=N-r,\quad D=N-j.
  \]
  The internal cube copies begin at \(\alpha,\beta,\gamma\); the copied cuts
  are \(Y\mid B=P\) and \(B\mid T=D\). Retain the necessary integer residual
  \[
  \alpha\ge0,\qquad r<s<3r,\qquad
  2r\le P-\gcd(r,P)-1.
  \]
  Equality cases \(s=2r\), \(j=r\), \(j=2r\), and the allowed endpoint
  \(j=0\Rightarrow D=N\) remain explicit.
- Equality-first engine: map every coordinate of \(V\) back to \(R\) by
  \[
  \phi(z)=
  \begin{cases}
  q-b+z,&0\le z<b,\\
  z-b,&b\le z<P,\\
  q-b+z-P,&P\le z<P+b,\\
  z-P-b,&P+b\le z<N.
  \end{cases}
  \]
  Union \(\phi(z)\) with \(\phi(z+r)\) for
  \(\alpha\le z<N-r\), force the class of \(R[j]\) to symbol \(3\), and
  enumerate only the free binary classes. A definition-first brute-force
  oracle through \(q=8\) independently reproduces exactly `197` parameter
  tuples and `1036` root assignments.
- Local-start scope: enumerate every binary \(L\) with
  \(|E=LRT|\le M\). This is a record-free bounded local-start cap, not a cap
  on an original orbit seed and not the fully generated strict-record
  specialization from D-017. Recompute the standalone canonical witness and
  every actual label of \(UBTU\) with a separate exact oracle; then recheck
  the canonical \(E,G,F,H\) data and evaluate \(\mathcal I\) and
  \(\mathcal J\) separately. Deduplicate only by the complete structural key
  \((L,R,b,j,r)\).
- Reason: integer pruning and equality classes remove impossible roots before
  context enumeration without replacing actual-generation or canonical
  checks by static word equations. The computation is a residual
  falsification tool, not a proof step.

## D-026 — Compute the bounded record-free Cell C residual through 18

- Date: 2026-07-27
- Status: `COMPUTED`
- Command:
  ```
  python research/generated_two_cube_cell_c_search.py --max-start-length 18 > research/outputs/generated_two_cube_cell_c_scan_2026-07-27.txt
  ```
- Cap and exact counts: the bound is
  \(1\le|E=LRT|\le18\) over the binary alphabet. The run found
  `parameter_tuples=2361`, `equality_assignments=714444`,
  `standalone_no_cube_assignments=239350`,
  `bounded_contexts=2866488`, `actual_generation_traces=120`, and
  `g2cs_antecedents=120`. All antecedents were witnesses for both targets:
  `I_witnesses=120`, `I_survivors=0`, `J_witnesses=120`,
  `J_survivors=0`, and `J_only_witnesses=0`.
- Boundary and family audit: all 120 antecedents belong to the one family
  \[
  (R,b,j,r)=((2,3,2),1,1,1)
  \]
  and all satisfy both exact boundaries \(s=2r\) and \(j=r\).
  Accordingly,
  `boundary_s_eq_2r_j_eq_r_antecedents=120`.
- Positive certificate: the first retained context is
  \(L=23222322\), \(E=232223222322\), with requested future
  \(UBTU=322232\). Its exact \((\kappa,\pi)\) timeline is
  `(3,4),(2,3),(2,3),(2,1),(3,1),(2,7),(2,4)`.
  The original \(\mathcal I\) times are `0,1,2,4,5`; the full
  \(\mathcal J\) family additionally contains bridge time `3`. Both period
  maxima are `7`, while \(P=4\).
- Reproduction: the reporting run took `12.213` seconds. A second run took
  `12.882` seconds and was byte-identical. The deterministic output SHA-256 is
  `F6597BD5D75455F3E2D354090308C57B310433A601AB0A9C3B7DC6C691166D37`.
- Verification: the focused Cell C suite passes `9` tests, including the
  independent binary canonical oracle through length 10, union-find versus
  brute force through \(q=8\), the exact positive timeline, the
  \(\mathcal I/\mathcal J\) split, and the exact length-12 integration
  counters and the preserved length-18 boundary artifact. The full repository
  suite passes `105` tests.
- Scope: this is bounded binary `COMPUTED` evidence. Zero bounded survivors
  is **NOT_A_PROOF** of either G2CS target, bridge promotion, or the Curling
  Number Conjecture. Cell C remains `OPEN`.

## D-027 — State the Cell C survivor and oracle boundaries explicitly

- Date: 2026-07-27
- Status: active
- Decision: the Cell C reduction is made only after negating the selected
  synchronization conclusion. Since
  \(F\in\mathcal I\subseteq\mathcal J\), either negation supplies
  \(r=\pi(F)<P\); when \(r\ge P\), \(F\) already witnesses both conclusions
  and no residual analysis is needed.
- Verification boundary: the bounded traversal uses one exact canonical
  witness implementation. A definition-first implementation independently
  cross-checks that canonical function on every binary word through length
  `10`; it is not described as an independent implementation of the entire
  orbit traversal.
- Reason: both qualifications were implicit in the executable filter and
  tests but must be explicit before the Fine--Wilf reduction and the evidence
  summary can be read without importing hidden premises or overstating
  independent verification.

## D-028 — Sharpen Cell C without promoting the remaining word wall

- Date: 2026-07-27
- Status: `PROVED-NL` reductions; Cell C remains `OPEN`
- Universal reduction: the copied \(B\)-block lies inside the internal
  \(r\)-cube. If \(b\ge2r\), it contains an \(r\)-square suffix ending at
  \(G\), contradicting \((\kappa(G),\pi(G))=(2,q)\) and \(r<q\).
  Therefore \(b<2r\). If \(j=0\), the canonical \(r\)-cube and the suffix
  \(B^2\) of \(F\) overlap in
  \[
  M_0=\min(3r,2b)\ge r+b-\gcd(r,b).
  \]
  Fine--Wilf gives the proper gcd period on an overlap of at least four gcd
  blocks, contradicting \(\kappa(F)=3\). Therefore \(j>0\).
- Simultaneous-boundary reduction: this does not assert that every Cell C
  instance lies on the boundary. Under the additional equalities
  \(s=2r,j=r\), one has
  \[
  b=j=r,\qquad R=BQB,\qquad T=B,\qquad U=QB,\qquad q>2r,
  \]
  with \(B[0]=2\), \(Q[0]=3\), and the later canonical cube exactly
  \(B^3\).
- Early-cube reduction: under the selected synchronization negation
  \(p=\pi(E)<P\), put \(W=RB\). Then \(W\) has periods \(p,q\),
  \(3p>P\), \(p\ne q\),
  \[
  r<p-\gcd(p,q),\qquad p>r+\gcd(p,r).
  \]
  The endpoint \(\gcd(p,r)=r\) is not discarded: the contrary
  Fine--Wilf threshold forces \(p=2r\), so the canonical root is
  \(X=B^2\) and \(E\) ends in \(B^6\).
- Exact branches: if \(p=q+t>q\), then
  \[
  r/2<t<r,\quad B\text{ has period }t,\quad
  X=B[r-t:r]UB.
  \]
  If \(p=q-d<q\), then
  \[
  p>q/2,\quad R=Z\,Z[0:d],\quad
  R[d:d+r]=B=R[0:r]=R[q-r:q],
  \]
  \[
  X=R[d+r:q]B,\qquad d<r\Longrightarrow d>r/2.
  \]
  There is no claim that \(d<r\) always holds. In both branches, with
  \(\eta=3p-P>0\), the early context obeys the exact frontier equation
  \(\operatorname{suf}_\eta(L)W=X^3\).
- Dynamic reduction in the \(p>q\) branch: writing
  \(E=\mathcal D X^3\) and
  \(Z_\ell=X^3UB^2U[0:\ell]\), a label-\(3\) witness at
  \(F_\ell=\mathcal D Z_\ell\) can require left context only if
  \[
  3p+\ell<2P-3.
  \]
  But \(q>2r\) and \(p>q\) give \(3p>2P\). Every proper \(F\)-window
  canonical pair is therefore context-free:
  \[
  (\kappa(Z_\ell),\pi(Z_\ell))
  =(\kappa(F_\ell),\pi(F_\ell)),\qquad0\le\ell<m.
  \]
  For the early local suffix
  \(A_\ell=X^3U[0:\ell]\), every label-\(2\) phase is likewise local, while
  a label-\(3\) left-context rescue requires
  \[
  \ell<3(P-p)-3=3(r-t)-3.
  \]
  This does not localize every early phase in general; it does localize all
  of them when \(P-p=1\).
- Exact open wall: it remains to prove or refute that no forced \(p>q\)
  boundary word can replay all of \(U\) in the \(Z_\ell\) while every proper
  local canonical period stays below \(P\). The cap is essential. The local
  model
  \[
  (q,r,P,t,p)=(9,3,12,2,11),\quad
  B=232,\ U=322232,\ X=32322232232
  \]
  replays all six \(F\)-window labels, but its final proper phase already has
  period \(P\). It also fails the early replay at \(\ell=1\), so it is not a
  G2CS counterexample; here \(P-p=1\), so no omitted left context can rescue
  that failure.
- Executable index audit:
  `tests/test_generated_two_cube_cell_c_reduction.py` independently checks
  the coordinate implications through \(q\le10\). It retains `4958`
  equality assignments, `538` exact \(G\)-canonical cases, and `489` cases
  after the standalone and local-\(F\) canonical filters. All `489` satisfy
  \(b<2r,j>0\); `257` are on \(s=2r,j=r\), `130` also have \(B[0]=2\),
  and their `13` possible early periods split as `7` with \(p>q\) and `6`
  with \(p<q\). These are bounded nonvacuous index checks, not proofs.
- Scope and warning: the non-boundary placements, the \(p<q\) frontier, and
  the local replay wall remain open. Cell A's \(C^2\) conjugate-period step
  does not transfer: Cell C's early state ends only in \(T(UT)\), not in
  two full copies of \(UT\). No G2CS target, bridge-promotion theorem, or
  Curling Number Conjecture conclusion is promoted by this checkpoint.
- Verification: the focused reduction plus Cell C search suites pass `11`
  tests and the full repository passes `107`. Fresh reruns of both preserved
  scans are byte-identical. Their SHA-256 hashes remain
  `F6597BD5D75455F3E2D354090308C57B310433A601AB0A9C3B7DC6C691166D37`
  for the Cell C local-start scan and
  `C461FF476D8F274C1203864A06B2C16F0312B398F19A71F01310C4DF4EB2B24F`
  for the fully generated strict-record scan.
