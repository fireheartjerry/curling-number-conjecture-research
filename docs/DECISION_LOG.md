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

## D-029 — Localize the full \(p>q\) continuation

- Date: 2026-07-27
- Status: `PROVED-NL` localization; Cell C remains `OPEN`
- Supersession boundary: D-028's separate early and later rescue inequalities
  remain valid, but they are no longer the strongest available statement.
  This entry supersedes only that dynamic-localization component; D-028's
  universal inequalities, boundary form, period branches, computations, and
  open-status warnings remain active.
- Decision: on the simultaneous boundary in the \(p>q\) branch, put
  \[
  \mathcal C=UB^2U,\qquad
  A_v=X^3\mathcal C[0:v],\qquad
  S_v=\mathcal D A_v.
  \]
  For any proper phase with binary output
  \(k=\kappa(S_v)\in\{2,3\}\) and canonical period
  \(h=\pi(S_v)<P\), the full and local canonical pairs agree.
- Proof: for \(k=2\), the canonical square has
  \(2h<2P<3p\le|A_v|\), so it is local. If a canonical \(h\)-cube for
  \(k=3\) crossed the left edge of \(A_v\), then
  \(p<h<P<2p\) and \(X^3\) would have periods \(p,h\).
  Fine--Wilf gives period \(\gcd(p,h)<p\) on \(X^3\); because the gcd
  divides \(p\), this makes \(X\) a proper power, contradicting its
  primitivity. Once a global maximizing witness is local, the canonical
  periods agree in both directions because every local suffix power also
  persists in the full state.
- Target scope: under the \(\mathcal I\)-negation, its period cap guarantees
  localization of every \(E_\ell\), including \(G=E_m\), and every proper
  \(F_\ell\), but not the omitted bridge interior. Under the
  \(\mathcal J\)-negation, it localizes every proper state from \(E\)
  through the state before \(H\); the entire \(UB^2U\) continuation is
  autonomous. The endpoint also localizes to
  \[
  (\kappa(A_{2q}),\pi(A_{2q}))=(2,P).
  \]
  These scopes are recorded separately and are not interchangeable.
- First-mismatch corollary: let
  \(a=P-p=r-t\), let \(z\) be the first index with \(U[z]=2\), and let
  \(h\) be the first mismatch between \(X[0:m]\) and \(U\). Autonomous
  early replay gives
  \[
  h<z,\qquad U[0:h+1]=3^{h+1},\qquad X[h]=2.
  \]
  If \(d\) is the terminal run length of \(3\)'s in \(B\), then \(F_z\)
  ends in \(3^{d+z}\) while \(\kappa(F_z)=2\), so \(d+z\le2\).
  Exactly three cases remain:
  \[
  \begin{array}{c|c}
  (z,h)&\text{forced data}\\
  \hline
  (1,0)&U\text{ starts }32,\ B[a]=2,\\
  (2,0)&U\text{ starts }332,\ B[a]=2,\ B\text{ ends }2,\\
  (2,1)&U\text{ starts }332,\ B[a:a+2]=32,\ B\text{ ends }2.
  \end{array}
  \]
- Sharpness models: D-028's \(q=9\) local \(F\)-replay model is now also
  eliminated globally by the first-mismatch corollary: it has \(z=1\) but
  \(X[0]=B[a]=3\). Conversely, the independently checked
  \[
  q=10,\ r=4,\ P=14,\ t=3,\ p=13,\quad
  B=2232,\ Q=32
  \]
  near-model replays both sampled \(U=322232\) windows with every displayed
  period below \(P\). Its local \(G\)- and \(H\)-scale periods are both
  \(6\), not \(q=10\) and \(P=14\). It is a warning that the endpoint
  scales remain essential, not a G2CS survivor.
- Exact open walls: for \(\mathcal I\), exclude the forced local early and
  later window pairs while respecting the uncapped bridge interior. For
  \(\mathcal J\), exclude the fully autonomous \(UB^2U\) episode with all
  proper periods below \(P\) and endpoint pair \((2,P)\). The \(p<q\)
  branch and non-boundary Cell C placements also remain open. No
  synchronization theorem, bridge-promotion theorem, or Curling Number
  Conjecture conclusion is promoted.
- Verification: the focused reduction plus Cell C search suites pass `12`
  tests and the full repository passes `108`. Both authoritative scans remain
  byte-identical to their preserved outputs, with unchanged SHA-256 hashes
  `F6597BD5D75455F3E2D354090308C57B310433A601AB0A9C3B7DC6C691166D37`
  and
  `C461FF476D8F274C1203864A06B2C16F0312B398F19A71F01310C4DF4EB2B24F`,
  respectively.

## D-030 — Exhaust the \(p>q\) simultaneous-boundary residual structurally

- Date: 2026-07-27
- Status: `COMPUTED`; Cell C remains `OPEN`
- Decision: search the exact binary \(p>q\) boundary normal form by structural
  coordinates rather than raw roots. For each
  \(q>2r>0,\ r/2<t<r\), generate the length-\(r\) word \(B\) from its first
  \(t\) coordinates with \(B[0]=2\), generate
  \(C=U[0:q-2r]\) with \(C[0]=3\), and set
  \[
  U=CB,\quad R=BU,\quad X=B[r-t:r]UB.
  \]
  The exact key is \((q,r,t,B,U)\); equal words at different \(t\) remain
  distinct because \(p=q+t\) changes.
- Command:
  `python research/generated_two_cube_cell_c_pgtq_search.py --max-q 25
  --oracle-max-q 10`.
- Counts: `220` integer triples and `1792552320` theoretical raw
  root--parameter pairs reduce to `2388798` structural assignments.
  Exact filtering retains `563708` canonical \(R^2\) words, all `563708`
  standalone exponent-two words, and `563688` canonical \(X^3\) words.
  Exactly one word replays the later exponents and also has the required
  initial later pair \((3,r)\). It has terminal pair \((2,P)\), but its
  final proper later period is already \(P\). Hence the late-period-cap,
  complete-\(\mathcal I\), and complete-\(\mathcal J\) survivor counts are
  all zero.
- Scope correction: `early_after_exact_late_replays=0` is explicitly a
  post-late-filter count, not a count over every canonical \(X^3\) word.
  The \(\mathcal I\) count requires both sampled local replays, their proper
  period caps, and the \(G,H\) endpoint scales. The \(\mathcal J\) count
  requires the exact full local continuation, its proper period cap, and
  terminal pair. Full-continuation checks may short-circuit after the exact
  later filter because full replay implies later replay.
- Certificate: the sole later replay is
  \[
  (q,r,t,P,p)=(9,3,2,12,11),\quad
  B=232,\quad U=322232,\quad
  R=232322232,\quad X=32322232232.
  \]
  Its later pairs are
  `(3,3),(2,2),(2,2),(2,1),(3,1),(2,12)`.
  Its early phase \(1\) requests `2` while the exact local pair remains
  `(3,11)`, so all-continuation localization rules out a full G2CS trace.
- Shadow decision: write \(Y=B^2U\). The final proper local state has a
  period-\(P\) square exactly when
  \(C[-1]=Y[-1]=B[-1]\). The certificate realizes this equality and has
  \(U=\operatorname{rot}_{\rm left}(B)B\). This identity is retained as the
  next proof lead, not promoted to a universal replay theorem.
- Trichotomy diagnostic: after the canonical filters, `197773` assignments
  satisfy all three alternatives in D-029, including the terminal-run
  inequality. Their row counts are `105851`, `45116`, and `46806`.
  Every one fails exact early replay: `71487` at phase `1`, `46843` at phase
  `2`, and `79443` later. There are zero phase-`0`, endpoint-only, or
  completed cases. These finite counts do not replace an unbounded proof.
- Independent oracle: a raw-root, definition-first implementation through
  \(q\le10\) enumerates `3456` raw pairs, retains `42` structural tuples, and
  reproduces the production stage counts `7,7,7,1,0,1,0`.
- Reproduction: the corrected authoritative run took `85.161` seconds. A
  second run took `80.994` seconds and was byte-identical.
  The deterministic artifact
  `research/outputs/generated_two_cube_cell_c_pgtq_scan_2026-07-27.txt`
  has SHA-256
  `8837CF352EA83B6F2195B17FFD222E42F831C7EA332827EC9C2D7A29F026B06E`.
- Scope: this is bounded binary evidence for the simultaneous-boundary
  \(p>q\) branch only. It proves neither the unbounded boundary word
  obstruction, the \(p<q\) branch, the non-boundary regions, Cell C, either
  G2CS target, nor the Curling Number Conjecture.
- Review: independent exact-spec and code-quality reviews both returned
  `APPROVED`. At commit
  `337098a3e436a887aed97ddb4d111d39ba0210f6`, the focused suite passed `11`
  tests, the full repository passed `119`, the worktree and remote branch
  matched, and the three preserved artifact hashes were unchanged.

## D-031 — Strengthen and localize the \(p<q\) boundary branch

- Date: 2026-07-27
- Status: `PROVED-NL` reductions; Cell C remains `OPEN`
- Supersession boundary: this replaces D-028's conditional
  \(d<r\Rightarrow d>r/2\) by the universal \(d>2r\) theorem and extends
  D-029's all-continuation localization from \(p>q\) to both period
  branches. It does not close either boundary word wall, any non-boundary
  placement, Cell C, or either G2CS target.
- Separation theorem: put \(d=q-p>0\). Period \(p=q-d\) on \(W\) makes
  \(R\) have border \(d\), while the middle occurrence remains
  \(R[d:d+r]=B\).
  - If \(d<r\), \(B\) has periods \(d\) and \(r-d\); Fine--Wilf makes it a
    proper power.
  - If \(d=r\), the middle copy equates \(Q[0]=3\) with \(B[0]=2\).
  - If \(r<d\le2r\), put \(a=d-r\). The disjoint border equation
    \(BA=CB\), with \(A=Q[0:a]\) and \(C=\operatorname{suf}_a(Q)\),
    either creates an \(a\)-square ending at \(G\) when \(a<r\), or again
    equates \(Q[0]\) with \(B[0]\) when \(a=r\).
  Therefore
  \[
  d>2r,\qquad q>4r,\qquad p>2r.
  \]
- Exact normal form: with \(\nu=d-2r=|\Theta|>0\), the same border equation
  gives
  \[
  Q[0:\nu+2r]=\Theta B^2,\qquad
  Q[|Q|-(r+\nu):|Q|]=B\Theta,\qquad
  X=Q[d:|Q|]B^2.
  \]
  In particular \(p<q-r=|U|\), so comparisons beyond one copy of \(X\)
  must use \(X^\omega\).
- Shifted-suffix lemma: if \(2p<P\), put \(c=P-2p\). Since
  \(W=\operatorname{suf}_c(X)X^2\) begins and ends in \(B\), the word
  \(B\) has period \(r-c\). The canonical pair at \(G\) forces
  \(0<c<r/2\).
- Localization decision: a capped canonical \(k\)-power crossing the left
  edge of \(A_v=X^3(UB^2U)[0:v]\) has root \(h>p\).
  - For \(p<h<2p\), Fine--Wilf makes \(X\) imprimitive.
  - For \(h=2p\), the \(2p\) period-\(p\) equalities inside \(X^3\) cover
    every residue of the crossing root, making that root a square and the
    suffix exponent at least four.
  - For \(h>2p\), write \(\delta=h-2p\). The shifted-suffix lemma gives
    \(0<\delta<r/2\), while period \(h\) on \(X^3\) gives \(X\) period
    \(\delta\), hence a short square ending at \(G\).
  Thus the complete canonical-pair localization (C.28) holds for \(p<q\)
  as well as \(p>q\), with the same distinct \(\mathcal I\) and
  \(\mathcal J\) scopes.
- First-mismatch correction: paired early and later replay first gives
  \(\lambda+z\le2\), where \(\lambda\) is the terminal \(3\)-run length in
  \(B\) and \(z\) is the first \(2\) in \(U\). Hence \(z\le2<p\).
  Compare \(U\) with \(X^\omega\), not the invalid slice \(X[0:|U|]\).
  Localization then gives the same three rows
  \((z,h)=(1,0),(2,0),(2,1)\). The terminal-run conclusion is not an
  early-replay-only fact; it uses the paired later window.
- Sharpness: the exact static model
  \[
  (q,r,p,d,P,c)=(20,3,11,9,23,1),\quad
  B=232,\quad Q=33223223232332
  \]
  realizes \(2p<P\), the \(\Theta B^2/B\Theta\) form, the \(G,F,H\)
  endpoint scales, and mismatch row \((2,1)\). It fails the later replay at
  phase \(1\),
  where the requested symbol is `3` and the local pair is `(2,2)`.
  Therefore static endpoint geometry and the trichotomy alone are not a
  contradiction.
- Bounded verification: an independent definition-first test through
  \(q\le14\) retains `141` static \(p<q\) tuples and checks every stated
  normal-form identity. It checks `3753` potential crossing-root slots and
  finds zero candidates. Its `74` mismatch-qualified tuples split
  `41,21,12` across the three rows. These finite checks are evidence and
  index validation only, not proof of an unbounded word obstruction.
- Review: independent exact-spec and code-quality reviews both returned
  `APPROVED`. The focused reduction suite passes `7` tests, the full
  repository passes `123`, compilation and `git diff --check` are clean,
  and the definition-first test does not import either production search.

## D-032 — Exhaust the necessary \(p>q\) early-replay relaxation by QF_BV

- Date: 2026-07-27
- Status: `COMPUTED` bounded exclusion plus `PROVED-NL` phase reductions;
  Cell C remains `OPEN`
- Scope decision: encode exactly the conjunction
  \[
  (\kappa(X^3),\pi(X^3))=(3,p),\qquad
  X^3\xrightarrow{\ U\ }\text{ autonomously},\qquad
  (\kappa(R^2),\pi(R^2))=(2,q)
  \]
  in the \(p>q\) simultaneous-boundary normal form. This is a necessary
  early-replay relaxation, not the complete boundary residual: it
  deliberately omits standalone \(R^2B\), canonical \(F=B^3\), the later
  replay, the \(\mathcal J\)-only bridge replay, terminal canonical
  \(H=(2,P)\), and all target-specific proper-period caps. No
  first-mismatch trichotomy is encoded because that trichotomy uses the
  omitted later replay.
- Exact encoding: map `2 -> 0`, `3 -> 1`, store the leftmost symbol as the
  most significant bit, and express every suffix power by equality of
  fixed bit-vector slices. For each admissible \((q,r,t)\),
  \(B\) is generated from \(t\) period coordinates with \(B[0]=2\), while
  \(Q[0]=3\), \(U=QB\), \(R=BQB\), and \(X=B[r-t:r]UB\).
  - Canonical \(X^3=(3,p)\) is the displayed \(p\)-cube together with no
    shorter cube root and no fourth-power suffix.
  - At every proper output phase, a requested `2` means some square and no
    cube; a requested `3` means some cube and no fourth power.
  - Canonical \(R^2=(2,q)\) is the displayed \(q\)-square together with no
    square suffix of root below \(q\). This also excludes every cube in the
    length-\(2q\) word.
- Executed command:
  `python research/generated_two_cube_cell_c_pgtq_early_replay_smt.py
  --max-q 40 --oracle-max-q 14 --timeout-ms 3000`.
  It checks all `1050` admissible parameter triples through \(q\le40\) and
  returns `0 SAT`, `1050 UNSAT`, and `0 UNKNOWN`. The previously unsearched
  interval \(26\le q\le40\) contributes `830` of those triples. Every
  fixed-triple solver call completed within the timeout.
- Independent oracle: a definition-first engine separately enumerates all
  `1014` concrete structural assignments in the `26` parameter triples
  through \(q\le14\). Literal exponent/period loops find no direct model;
  all `26` existential triple outcomes agree with QF_BV, with zero
  mismatches or unknowns. The oracle shares neither bit-vector power
  predicates nor solver models.
- Positive-path audit: dropping only canonical \(R^2\) preserves exact
  early replay at
  \[
  (q,r,t)=(10,4,3),(17,4,3),(17,7,4),(19,9,8),(27,10,7).
  \]
  Their endpoint pairs are respectively
  \[
  (2,6),(2,3),(2,4),(2,4),(2,4),
  \]
  all strictly below \(q\). The first four are the historical early-only
  collapse models; the fifth has
  \(B=2322322232,Q=3222322\). These SAT checks make the encoding's positive
  path nonvacuous.
- Endpoint sharpness: the exact structural model
  \[
  (q,r,t)=(9,4,3),\quad B=2332,\quad Q=3
  \]
  has canonical \(X^3=(3,12)\), and appending one `2` simultaneously changes
  the pairs on \(R^2[:-1]\to R^2\) from \((2,1)\) to \((2,9)\), and on
  \(Y^2[:-1]\to Y^2\), \(Y=B^2U\), from \((2,1)\) to \((2,13)\).
  It fails early replay at phase one, where \(U[1]=2\) but the local pair
  remains \((3,12)\). Thus the final low-to-\(\{q,P\}\) push is feasible;
  endpoint geometry alone is not the missing contradiction.
- Phase reductions: for an early pair \((k,s)\), \(k\in\{2,3\}\),
  \(s<P\), \(s\ne q\), the suffix
  \(T_\ell=R\,R[0:r+\ell]\) has period \(q\). With
  \(g=\gcd(s,q)\),
  \[
  \min(ks,q+r+\ell)<s+q-g.
  \]
  In the contained branch this gives
  \((k-1)s<q-g\); in the crossing branch it gives
  \(s>r+\ell+g\). The divisor endpoint \(g=s\) is discharged by observing
  that the final length-\(q\) factor is both a proper \(s\)-power and a
  conjugate of \(R\), contradicting primitivity of \(R\).
  At the first \(X^\omega/U\) mismatch, the displayed \(p\)-cube cannot
  survive: the replacement root \(s\) is a strict adjacent pop satisfying
  \[
  s<p,\qquad p\ge(k_1-1)s+\gcd(p,s).
  \]
  These are `PROVED-NL` restrictions, not a proof of the remaining replay
  wall.
- Reproduction: the authoritative Z3 `5.0.0` run took approximately
  `213` wall-clock seconds. The LF-normalized deterministic artifact
  `research/outputs/generated_two_cube_cell_c_pgtq_early_replay_smt_2026-07-27.txt`
  has SHA-256
  `D3C8FB986F20665777EB3DDD362F3DA1E09E88328716241809AADC1B56A0CF09`.
- Scope: bounded UNSAT for a necessary relaxation is stronger bounded
  exclusion evidence than filtering the full residual, but it is still not
  an unbounded proof. The \(p>q\) word wall, \(p<q\) word wall,
  non-boundary Cell C placements, both G2CS targets, and the Curling Number
  Conjecture remain open.
- Review: independent exact-spec and code-quality reviews both returned
  `APPROVED`. The focused suite passes `12` tests, the full repository
  passes `135`, compilation and `git diff --check` are clean, the
  definition-first oracle is independent of the QF_BV predicates and
  models, and the pinned artifact hash matches the stored output.

## D-033 — Eliminate the simultaneous-boundary double-`3` rows

- Date: 2026-07-27
- Status: `PROVED-NL` under the exact simultaneous-boundary and
  target-negation hypotheses; Cell C remains `OPEN`
- Scope decision: retain
  \[
  q>2r>0,\quad P=q+r,\quad R=BQB,\quad U=QB,\quad
  B[0]=2,\quad Q[0]=3,
  \]
  together with the full-state canonical data
  \[
  (\kappa(G),\pi(G))=(2,q),\qquad
  (\kappa(F),\pi(F))=(3,r).
  \]
  No \(p>q\) or \(p<q\) early-root formula is used in the elimination.
- Target legality: if the first `2` in \(U\) is at \(z=2\), then
  \(U[0:3]=332\). The actual state
  \[
  F_1=F\,3=LR^2B^2\,3
  \]
  is a proper sampled later state for \(\mathcal I\), and hence also for
  \(\mathcal J\). Under either target negation it must have exact pair
  \((3,\rho)\) with \(\rho<P\). No uncapped bridge state is invoked.
- Small-root elimination: deleting the final `3` from the canonical
  \(\rho\)-cube leaves a \(\rho\)-periodic suffix of \(F\) of length
  \(3\rho-1\). For \(\rho<r\), its terminal square either copies into the
  final \(B\) of \(G\), or Fine--Wilf makes \(B\) a proper power.
  The case \(\rho=r\) makes the final `3` copy \(B[0]=2\).
  For \(r<\rho\le2r+\gcd(r,\rho)\), Fine--Wilf on \(B^3\) gives the same
  proper-power contradiction; the divisor endpoint leaves only
  \(\rho=2r,3r\), where the final symbol again copies \(B[0]\).
- Large-root elimination: after removing the final \(B^2\), the inherited
  suffix of \(G\) has length
  \[
  3\rho-1-2r>2\rho.
  \]
  Thus \(\rho\ge q\). Writing \(\rho=q+u<P\), any \(u>0\) makes all of
  \(R^2\) \((q+u)\)-periodic, hence makes \(R\) \(u\)-periodic and creates
  a forbidden \(u\)-square at \(G\). Therefore \(\rho=q\).
- Audited endpoint contradiction: inside
  \[
  S=R_1R_2B_3B_4\,3,
  \]
  whose length is at most \(3q\), terminal \(q\)-cube periodicity equates
  the positions
  \[
  R_2[r]=Q[0]=3,\qquad B_4[0]=B[0]=2.
  \]
  These positions, not the appended final `3` and \(B_4[0]\), are exactly
  \(q\) apart.
- Consequence: both \((z,h)=(2,0)\) and \((2,1)\) are impossible under
  either target negation. The simultaneous-boundary first-mismatch
  residual is now only
  \[
  (z,h)=(1,0),\quad U[0:2]=32,\quad X[0]=2,\quad\lambda\le1.
  \]
- Exact \(p<q\) seam decision: with
  \(d=q-p=2r+\nu\), \(D=Q[d:]\), and \(e=2p-P\), the suffix equation has
  precisely
  \[
  D=JB\Theta\quad(e\ge0),
  \]
  or, for \(c=-e=P-2p\),
  \[
  B[0:c]=B[-c:],\qquad D=B[c:]\Theta
  \quad(e<0,\ 0<c<r/2).
  \]
  Taking \(C=\Theta B^2\), \(H_0=\Theta B\), and
  \(A=JB\) or \(B[c:]\) gives the unified form
  \(X=AC,\ U=CAH_0\). The subscript prevents confusion with the global
  completion state \(H\).
- Independent regression: the new definition-first engine imports neither
  production Cell C search. Through \(q\le20\), it checks `73470`
  \(p>q\) structures and retains `1394,1447` candidates in the two
  \(z=2\) rows. Their \(F_1\)-exponent distributions are
  `{1: 399, 2: 995}` and `{1: 43, 2: 1404}`. The \(p<q\) engine checks
  `34405` structures and retains `1343,673`, with distributions
  `{1: 1090, 2: 253}` and `{1: 547, 2: 126}`. Both exact seams occur.
  Across all `4857` retained candidates, zero has
  \(\kappa(F_1)=3\). This is a nonvacuous bounded audit, not the proof.
- Surviving-row warning: the exact overlap-seam model
  \[
  q=23,\ r=4,\ p=13,\ P=27,\quad
  B=2232,\ \Theta=32,\ D=23232
  \]
  has \(X=2323222322232\),
  \(U=3222322232232322232\), and exact static \(G,F,H\) pairs
  \((2,23),(3,4),(2,27)\). Both sampled local traces replay phases
  `0` through `12`; at phase `13`, the requested `3` meets pair
  \((2,3)\) in both. It shows that the remaining \((1,0)\) row is a later,
  nonlocal replay obstruction, not that it survives either target.
- Scope: the \(p>q\) and \(p<q\) \((1,0)\) word walls, every non-boundary
  Cell C placement, Cell C itself, both G2CS targets, and the Curling Number
  Conjecture remain open.
- Verification: the new focused suite passes `4` tests in `2.40` seconds;
  the full repository passes `139` tests in `26.68` seconds.
  `python -m compileall -q research tests` and `git diff --check` are clean.
  The definition-first regression imports neither of the production Cell C
  search modules, and the checkpoint deliberately adds no generated output
  artifact.
- Review: independent exact-spec and code-quality reviews both returned
  `APPROVED`. They separately verified the \(\rho\)-case thresholds, the
  \(q\)-separated endpoint coordinates, both target scopes, both \(p<q\)
  seams, all pinned counts, the \(q=23\) warning model, and the absence of
  status inflation.

## D-034 — Preserve the surviving-row transition atlas

- Date: 2026-07-27
- Status: exact transition lemmas `PROVED-NL`; two-branch finite atlas
  `COMPUTED`; Cell C remains `OPEN`
- Row decision: after D-033, retain only
  \[
  (z,h)=(1,0),\qquad U[0:2]=32,\qquad X[0]=2,\qquad\lambda\le1
  \]
  on the simultaneous boundary. Write the sampled phase-one pairs as
  \[
  E_1:(2,\alpha),\qquad F_1:(2,\beta),\qquad\alpha,\beta<P.
  \]
  No claim is made about non-boundary Cell C instances.
- Early-root decision: all-continuation localization places the
  \(\alpha\)-square inside \(X^3\,3\). The appended `3` breaks the old
  \(p\)-root. A push would require
  \(\alpha>2p+\gcd(p,\alpha)\), making its square longer than
  \(3p+1\). Therefore
  \[
  \alpha<p,\qquad p\ge\alpha+\gcd(p,\alpha).
  \]
- Later-root decision: the same mismatch breaks the \(r\)-root, and
  adjacent-root separation gives exactly
  \[
  \beta<r,\quad r\ge\beta+\gcd(r,\beta),
  \]
  or
  \[
  \beta>2r+\gcd(r,\beta).
  \]
- Common-suffix decision: both states end in \(T_1=B^2\,3\). If either
  canonical square has root at most \(r\), it occurs in both states and
  least-root minimality forces
  \[
  \alpha=\beta=s<r.
  \]
  The exact low square is
  \(\operatorname{suf}_{2s}(T_1)=(B[r-s+1:r]\,3)^2\), with
  \(B[r-s]=3\). Otherwise both roots exceed \(r\). Since \(223\) has no
  square, \(r=1\) is necessarily high/context-crossing.
- High-\(\beta\) decision: initially
  \(2r+\gcd(r,\beta)<\beta<P\). The endpoint \(\beta=q\) equates the
  fixed symbols `3` and `2`. For \(\beta=q+w\), \(0<w<r\), copying
  \(T_1\) left gives \(B=B[w:]B[:w]\), making \(B\) a proper power and
  contradicting \(\kappa(F_0)=3\). Thus the high range is exactly
  restricted to
  \[
  2r+\gcd(r,\beta)<\beta<q.
  \]
  With \(v=P-\beta\), \(g_r=\gcd(r,\beta)\), the copied square has the
  exact form
  \[
  \operatorname{suf}_{2\beta}(R^2B^2\,3)
    =(R[r+v+1:q]B^2\,3)^2,\qquad R[r+v]=3,
  \]
  and \(1\le v\le m-g_r-1\). On
  \(K=R^2B=B(UB)^2\), put \(d_\beta=\gcd(\beta,q)\). If
  \(d_\beta=\beta\), then \(\beta\mid q\), \(\beta<q\), and
  \(2\beta-r-1<2\beta\le q=\beta+q-d_\beta\), so the threshold misses
  automatically. If \(d_\beta<\beta\), threshold attainment on the whole
  shorter common suffix would, on the length-\((2\beta-r-1)\) side,
  include the complete first primitive \(\beta\)-root and make it
  imprimitive; on the length-\(2q\) side, the common suffix is the whole
  displayed \(q\)-square and makes its primitive root \(UB\) imprimitive.
  Hence Fine--Wilf must miss:
  \[
  \min(2\beta-r-1,2q)<\beta+q-d_\beta.
  \]
  It is not eliminated.
- \(p<q\) return decision: retain both exact seams in the common form
  \(X=AC,\ U=CAH_0\). The high \(\beta\)-return is either wholly in \(U\)
  at `m-beta`, or crosses from the preceding \(B\) into \(U\).
  Its internal interval has six weak orders relative to the cuts
  \(|C|=d\), \(|CA|=p\); the overlap seam cannot place all of \(T_1\)
  inside \(A\). The high \(\alpha\)-return is recorded relative to
  \(\sigma=p-2r\). These are word equations, not a closure proof.
- Proper-period correction: \(T_1\) has no period
  \(\Delta\le r\). For \(\Delta<r\), its repeated \(B[r-\Delta]\)
  coordinate would equal both \(B[0]=2\) and the final `3`; the case
  \(\Delta=r\) compares those fixed symbols directly. The endpoint
  \(\Delta=2r\) also compares \(T_1[0]=2\) directly with
  \(T_1[2r]=3\). Every proper period is therefore \(r+a\) with
  \(1\le a<r\); its comparisons make \(B\) period \(a\) and give
  \(B[r-a]=3\). If \(2a\le r\), the final \(2a\) symbols of \(B\) form an
  \(a\)-square at \(G\), forcing \(\pi(G)\le a<r<q\). Hence
  \(r/2<a<r\).
- Paired-root decision: if phase \(\ell\) has common requested exponent
  \(k_\ell\) and different canonical roots \(a_\ell,b_\ell\), their shared
  suffix has length \(2r+\ell\). A contained smaller maximizing power
  would occur in both states and contradict least-root minimality. Hence
  \[
  k_\ell\min(a_\ell,b_\ell)>2r+\ell.
  \]
  This explicitly permits later root divergence.
- Endpoint decision: if the roots remain equal through phase \(m-1\), the
  final transition has the exhaustive adjacent-root classification in
  (C.35w), split by final label `2` versus `3` and by
  \(s<q,s=q,q<s<P\). Exact endpoints do not by themselves imply that their
  predecessor labels were generated correctly.
- Target-scope decision: the bridge midpoint \(M=LR^2B\) is omitted from
  \(\mathcal I\), but its suffix \(K=B(UB)^2\) directly gives its global
  root \(c\le\pi(K)\le q<P\), so (C.28) localizes it anyway.
  \(\mathcal J\) caps every proper bridge state. At a bridge cut
  \(B=AD\),
  \[
  B^2B[0:i]=A(DA)^2.
  \]
  This localizes an omitted \(\mathcal I\)-bridge phase when the requested
  symbol \(B[i]\) is `2`. No converse or fixed canonical profile is claimed
  at cuts requesting `3`; the stronger two-half bridge atlas is reserved
  for D-035.
- Executable decision: add
  `research/generated_two_cube_cell_c_z1_atlas.py`, independent of both
  production Cell C searches. Its literal witness engine, exact structural
  generators, transition classifier, deterministic renderer, and six
  recomputed certificates are covered by a test-side raw-root reference.
- \(p>q\) census through \(q\le25\): `2388798` structures, `595896`
  structural rows, and `105851` exact static candidates. Phase one has
  `79471` both-label-two, `9` early-only, `0` late-only, and `26371`
  neither. All `79471` paired cases are equal/local and capped. Failures
  synchronize in `105838` cases and differ in `13`; root divergence occurs
  at the first failure in `43471` and after it in `62380`.
  Both endpoints are exact in all `105851`, while the early, late, and
  paired predecessor-label counts are `29416`, `64641`, `28724`.
- \(p<q\) census through \(q\le25\): `1115405` structures, `418622`
  structural rows, and `100053` exact static candidates. Phase one has
  `61200` both-label-two, `32800` early-only, `507` late-only, and `5546`
  neither. The paired cases split into `6555` equal/local and `54645`
  unequal/high cases; the latter are exactly the bounded \(r=1\) family.
  The generic/overlap seams contribute `100050/3` static candidates.
  Failures synchronize in `46364` and differ in `53689`; divergence occurs
  before/at/after the first failure in `54780/45268/5`.
  Early endpoints are all exact, late endpoints are exact in `99934`, and
  predecessor-label counts are `91133`, `13138`, `13128`.
- Certificate decision: pin six exact words:
  \(q=8\) unequal high roots plus late-endpoint failure;
  endpoint-correct \(q=9,r=1\);
  \(q=11\) desynchronized failures;
  \(q=16,r=2\) valid phase-two root divergence;
  the \(q=23\) overlap long replay; and the \(q=29,r=4\) high static model
  with \(E_1:(2,9)\), \(F_1:(2,20)\).
  These refute overstrong monotonicity/equality claims and are not
  survivors or conjecture counterexamples.
- Artifact decision: the \(q\le25\) artifact is LF-stable and byte-identical
  across two independent runs (`43.451`, `43.523` seconds), with SHA-256
  `975E542B6AEF428B39C087095BCB0A77AD68E390D597CC21F1FB43DA72BCEFE9`.
- Verification: the focused transition-atlas suite passes `5` tests, the
  full repository suite passes `144` tests, `compileall` is clean, and
  `git diff --check` reports no whitespace errors. A fresh in-memory
  \(q\le25\) render matches the stored `12508`-byte LF-only artifact
  byte-for-byte.
- Review: independent exact-proof and publication-quality reviews both
  returned `APPROVED`. They separately checked the ordering of the
  \(\beta=q\) and \(\beta=q+w\) exclusions before (C.35r), both
  \(d_\beta=\beta\) and \(d_\beta<\beta\) Fine--Wilf branches, the
  \(\Delta=2r\) endpoint, the noncircular proof of \(a>r/2\), line-ending
  stability, all pinned counts and hashes, the nine-file change scope, and
  the absence of status inflation.
- Checkpoint decision: publish this nine-file D-034 snapshot on
  `research/generated-two-cube-wall`; do not start or resume any cloud
  task. Continue the proof search locally with D-035.
- Scope: the high phase-one alternative, the \(r=1\) family, both
  target-specific boundary word walls, every non-boundary Cell C
  placement, Cell C, both G2CS targets, and the Curling Number Conjecture
  remain open. Bounded failure counts are not proof.

## D-035 — Begin the two-half bridge atlas

- Date: 2026-07-27
- Status: bridge-`2` self-capping lemma `PROVED-NL`; overall D-035
  `IN PROGRESS`; Cell C remains `OPEN`
- Boundary decision: work on the simultaneous boundary
  \(b=j=r,\ R=BQB,\ T=B,\ U=QB,\ P=q+r\), where the actual output from
  \(G\) to \(F\) is \(BT=B^2\).
- Bridge-coordinate decision: for \(0\le i<r\), put
  \(A_i=B[0:i]\) and
  \[
  G_i=LR^2A_i,\qquad M_i=LR^2B A_i.
  \]
  These are the cuts before the two occurrences of \(B[i]\), so actual
  generation gives
  \(\kappa(G_i)=B[i]=\kappa(M_i)\).
- Circular-square decision: writing
  \(R=A_iC_i\) and \(B=A_iD_i\) gives the two exact identities
  \[
  R^2A_i=A_i(C_iA_i)^2,\qquad
  B^2A_i=A_i(D_iA_i)^2.
  \]
  Their displayed roots have lengths \(q\) and \(r\).
- Self-cap decision: if \(B[i]=2\), both actual curling numbers are exactly
  two. The displayed squares therefore attain the maximal suffix exponent,
  and least-root minimality proves
  \[
  \pi(G_i)\le q<P,\qquad \pi(M_i)\le r<P.
  \]
  The cap is direct and target-independent. It licenses the subsequent
  application of (C.28); (C.28) is not used to prove the cap.
- Endpoint decision: \(i=0\) is included with \(A_0\) empty. Thus
  \(G_0=G\), \(M_0=M\), and the midpoint bound strengthens from
  \(\pi(M)\le q\) to \(\pi(M)\le r\). Extending the first family gives
  \(G_r=M_0\), one state rather than two. The cut \(i=r-1\) is included;
  after the second \(B\) is complete, the state is \(F\) and the next
  requested symbol is \(U[0]=3\), outside this indexed bridge family.
- Target-scope decision: no negation of G2CS-\(\mathcal I\) or
  G2CS-\(\mathcal J\) is needed. Every such `2`-cut self-caps even when it
  is omitted from \(\mathcal I\). This is not itself a witness inside
  \(\mathcal I\), and it proves nothing about bridge cuts requesting `3`.
- Documentation decision: add root `AGENTS.md` so future chat explanations
  start from concrete finite sequences and define technical terms before
  using them. Formal proof files may remain advanced. Also replace the
  duplicate Phase-1 changing-origin checkbox with a handoff note; its one
  actual completion gate remains in Phase 3. Neither documentation change
  advances a mathematical status.
- Verification: direct enumeration checked each circular-square identity
  on `18434` binary word/cut pairs through root length `10`. This is a
  finite index guard, not the proof. The full repository suite passes
  `144` tests in `21.03` seconds; `compileall` and `git diff --check` are
  clean.
- Review: independent exact-proof and scope/status reviews returned
  `APPROVED`. They checked the exact use of \(\kappa=2\), both rotations,
  all endpoint conventions, the strengthened midpoint, the continuation
  coordinates needed for (C.28), target independence, and every stated
  non-claim.
- Scope: the capped bridge-`3` classifications, the no-fourth consequence,
  the bounded bridge census, both boundary word walls, non-boundary Cell C,
  Cell C, both G2CS targets, and the Curling Number Conjecture remain open.

## D-035 item 1 — adversarial completion audit

- Date: 2026-07-27
- Status: the first D-035 checklist item remains `PROVED-NL`; its
  quantifier and load-bearing hypothesis are now stated explicitly.
- Exhaustion decision: on the simultaneous boundary the generated bridge is
  \(BT=B^2\), so its proper generation cuts are exactly
  \(K_h\) for \(0\le h<2r\). They split disjointly as
  \[
  G_i=K_i,\qquad M_i=K_{r+i}\qquad(0\le i<r).
  \]
  Thus the two families in (C.35y)--(C.35z) cover every cut named by the
  checklist item.
- Exact-label decision: “requesting `2`” means
  \(\kappa(K_h)=2\) in the actual full orbit. A static occurrence of the
  symbol `2` inside a proposed word is not enough. Actual generation gives
  \(\kappa(G_i)=B[i]=\kappa(M_i)\), which supplies the needed equality.
- Definition-first decision: if a full state \(W\) has
  \(\kappa(W)=2\) and ends in \(X^2\), then \(X\) belongs to the set over
  which the defining minimum for \(\pi(W)\) is taken. Therefore
  \(\pi(W)\le |X|\). Applied to the two full-state suffixes in (C.35y),
  this gives \(\pi(G_i)\le q\) and \(\pi(M_i)\le r\). No primitivity,
  persistence, localization, target negation, or restriction on the left
  context is used.
- Endpoint decision: \(K_0=G\), \(K_r=M\), and both final cuts of the two
  halves are included. The completed bridge state \(K_{2r}=F\) is not a
  proper bridge-generation cut and satisfies
  \(\kappa(F)=U[0]=Q[0]=3\), so it is not an omitted `2`-cut.
- Review decision: three independent adversarial reviews separately audited
  the bridge quantifier, the raw definitions, and attempted counterexamples.
  All returned `APPROVED`; no missing cut or mathematical hypothesis was
  found. The wording was tightened to say “proper actual-orbit bridge cut”
  and “canonical-root length” so the proved scope cannot be mistaken for a
  merely static word claim.

## D-035 item 2 — capped first-half `3` cuts

- Date: 2026-07-27
- Status: first-half capped-`3` lemma `PROVED-NL`; overall D-035 remains
  `IN PROGRESS`; Cell C remains `OPEN`
- Exact scope: for \(0\le i<r\), let
  \(G_i=LR^2A_i\), where \(A_i=B[0:i]\). Assume the actual bridge cut
  requests `3` and is capped:
  \[
  \kappa(G_i)=B[i]=3,\qquad h=\pi(G_i)<P=q+r.
  \]
  The conclusion is conditional on this cap; no target negation is part of
  the lemma.
- High-root decision: if \(h=q+u>q\), the cap gives \(0<u<r\). The visible
  suffix \(R^2A_i\) lies wholly in the canonical \(h\)-cube. Comparing its
  first two \(R\)-copies at distance \(q+u\) makes \(u\) a period of \(R\).
  Since \(u<r<q/2\), this gives a maximizing \(u\)-square at \(G\), contrary
  to \(\pi(G)=q\).
- Equality decision: if \(h=q\), the canonical root is the phase-\(i\)
  rotation \(C_iA_i\). Writing it as \(D_iV_i\), where
  \(D_i=B[i:r]\), and appending the actual remaining first-half output gives
  \[
  (D_iV_i)^3D_i=D_i(V_iD_i)^3
  \]
  at \(M\). This contradicts the actual midpoint equality
  \(\kappa(M)=B[0]=2\). Thus \(h<q\).
- Circularity decision: if the \(h\)-cube crossed the left edge of
  \(R^2A_i\), that entire visible suffix would have periods \(h,q\).
  Fine--Wilf gives period \(\gcd(h,q)<q\) on a complete copy of \(R\).
  Since that gcd divides \(q\), \(R\) would be a proper power and \(R^2\)
  would give exponent at least four at \(G\), contradicting
  \(\kappa(G)=2\). Hence the canonical cube lies wholly in
  \(R^2R[0:i]\subset R^{\mathbb Z}\) and is a proper circular cube of \(R\).
- Endpoint decision: \(i=0\) cannot request `3` because \(B[0]=2\);
  \(i=r-1\) is included, with nonempty one-symbol \(D_i\); \(r=1\) is
  vacuous.
- Target decision: the G2CS-\(\mathcal J\) negation caps every proper
  bridge state, so the lemma covers all its first-half `3` cuts. The
  G2CS-\(\mathcal I\) negation does not cap omitted interior bridge cuts;
  the lemma makes no unconditional \(\mathcal I\)-scope claim. The proof
  does not use (C.28), persistence, either early-period branch, or
  primitivity of \(B\).
- Sharpness decision: the midpoint recurrence is load-bearing. The exact
  local word
  \[
  r=2,\ B=23,\ Q=32,\ R=233223,\ i=1,\ L=33223
  \]
  has \((\kappa(G),\pi(G))=(2,6)\) and
  \(G_i=(332232)^3\), so its capped first-half pair is \((3,6)\) with
  \(h=q<P=8\). But its midpoint has pair \((3,6)\), violating the required
  \(\kappa(M)=2\). It refutes the weakened static/current-cut-only claim,
  not the actual-orbit lemma.
- Verification: the definition-first canonical oracle and both independent
  curling-number implementations recompute the sharpness pairs
  \(G:(2,6)\), \(G_i:(3,6)\), and \(M:(3,6)\), together with both displayed
  cube factorizations. The full repository suite passes `144` tests;
  `compileall` and `git diff --check` are clean.
- Review: independent exact-proof, adversarial-countermodel, and
  publication/scope reviews all returned `APPROVED`. They checked both
  root-size exclusions, the Fine--Wilf threshold, the circular
  interpretation, the midpoint dependency, all endpoints, the
  \(\mathcal I/\mathcal J\) distinction, unique equation tags, and every
  stated non-claim.
- Scope: the second-half capped-`3` classification, terminal seam,
  no-fourth consequence, bounded bridge census, both boundary word walls,
  non-boundary Cell C, Cell C, both G2CS targets, and the Curling Number
  Conjecture remain open.

## D-035 item 3 — capped second-half `3` cuts

- Date: 2026-07-27
- Status: second-half capped-`3` classification `PROVED-NL`; overall D-035
  remains `IN PROGRESS`; Cell C remains `OPEN`.
- Exact scope: for \(0\le i<r\), let \(A_i=B[0:i]\) and
  \(M_i=LR^2B A_i\). Assume the actual bridge cut requests `3` and is
  capped:
  \[
  \kappa(M_i)=B[i]=3,\qquad h=\pi(M_i)<P=q+r.
  \]
  The conclusion is \(h\le r\); if \(h<r\), the canonical cube is a
  proper circular cube of \(B\). Equality \(h=r\) remains an exceptional
  full-root seam placement.
- Terminology decision: item 3 records only the placement of an \(r\)-root
  cube across the boundary \(BQ\mid B^2A_i\). The exact equation
  \(\operatorname{suf}_{r-i}(BQ)=B[i:r]\), its persistence consequences,
  and the eventual conclusion \(i=r-1\) remain item 4. This avoids both
  duplicating the next obligation and suggesting the false converse
  “seam implies \(h=r\).”
- Long-delete decision: put \(E_i=BA_i\). When \(h>r\) and
  \(h\ge r+i=|E_i|\), writing the canonical root as \(V_iE_i\) and
  deleting \(E_i\) leaves \(V_i(E_iV_i)^2\) at \(G\). Thus \(G\) has an
  \(h\)-root maximizing square, so \(h\ge\pi(G)=q\).
- Marker decision: if the transferred root has \(h=q\), then
  \(E_iV_i=R\). Since a `3` cut has \(i>0\), position \(r\) of that
  prefix exists; it is simultaneously \(B[0]=2\) in \(E_i=BA_i\) and
  \(Q[0]=3\) in \(R=BQB\), a contradiction.
- High-root decision: if \(h=q+u>q\), the cap gives \(0<u<r\).
  The inherited \(h\)-square contains \(R^2\), whose periods \(q\) and
  \(q+u\) make \(u\) a period of \(R\). This supplies a maximizing
  \(u\)-square at \(G\), contradicting \(\pi(G)=q\).
- Short-crossing decision: the remaining range \(r<h<r+i\) puts all of
  \(B^2A_i\) inside the canonical cube. Fine--Wilf gives period
  \(\gcd(h,r)<r\) on \(B\). As that period divides \(r\), \(B\) is a
  proper power, so the suffix \(B^3\) at \(F\) has exponent at least six,
  contradicting \(\kappa(F)=3\).
- Circularity decision: for \(h<r\), a cube crossing the left edge of
  \(B^2A_i\) would give the same forbidden gcd period on \(B\).
  Therefore the cube lies wholly in
  \(B^2B[0:i]\subset B^{\mathbb Z}\), with root strictly shorter than
  \(B\).
- Endpoint decision: \(i=0\) cannot request `3` because \(B[0]=2\);
  \(i=r-1\) is included; \(r=1\) is vacuous. The completed endpoint
  \(F=M_r\) is not an indexed proper bridge cut.
- Dependency decision: the cap is used only after deletion, to put
  \(h-q<r\). The proof also uses the actual bridge chronology,
  \((\kappa(G),\pi(G))=(2,q)\), the marker mismatch
  \(B[0]=2\ne3=Q[0]\), and \(\kappa(F)=3\). It does not use (C.28),
  either \(p\)-branch, or either target negation.
- Target decision: the G2CS-\(\mathcal J\) negation supplies the cap at
  every proper second-half bridge cut. The G2CS-\(\mathcal I\) negation
  omits these interior cuts, so the lemma remains conditional there.
- Finite-audit decision: an independent definition-first enumeration
  through \(r,|Q|\le6\) and \(|L|\le8\) inspected `31,641` full actual
  bridges with capped second-half `3` cuts. It found no \(h>r\) case,
  no \(h<r\) cube crossing \(B^2B[0:i]\), and no noncircular low-root
  case. This is corroborating finite evidence only; the symbolic proof
  above carries the result.
- Verification: the full repository suite passes `144` tests;
  `compileall`, unique-tag inspection, and `git diff --check` are clean.
- Review: independent exact-proof, adversarial definition-first, and
  publication/scope reviews returned `APPROVED`. The scope review caught
  and corrected one prose error: the full-root cube begins \(r-i\)
  symbols before \(Z_i\) and crosses the displayed seam; it does not
  begin at the seam.
- Scope: the exact full-root seam equation and phase restriction,
  no-fourth consequence, bounded bridge census, both boundary word walls,
  non-boundary Cell C, Cell C, both G2CS targets, and the Curling Number
  Conjecture remain open.

## D-035 item 4 — full-root seam and terminal phase

- Date: 2026-07-27
- Status: full-root seam equation and terminal-phase implication
  `PROVED-NL`; overall D-035 remains `IN PROGRESS`; Cell C remains `OPEN`.
- Exact scope: retain an actual binary second-half bridge cut
  \(M_i=LR^2B A_i\), \(0\le i<r\), with
  \[
  \kappa(M_i)=B[i]=3,\qquad \pi(M_i)=r.
  \]
  Item 4 does not assume the cap \(h<P\); it starts after the equality
  case \(h=r\) is already known.
- Seam decision: with \(D_i=B[i:r]\) and \(d=r-i\), the canonical root is
  \(D_iA_i\). The two exact descriptions
  \[
  \operatorname{suf}_{3r}(M_i)
    =\operatorname{suf}_{d}(BQ)B^2A_i,\qquad
  (D_iA_i)^3=D_iB^2A_i
  \]
  give \(\operatorname{suf}_{r-i}(BQ)=B[i:r]\) by right cancellation.
  This proves only \(h=r\Rightarrow\) seam.
- Rotation decision: for \(C_t=D_i[0:t]\) and
  \(V_t=D_i[t:d]A_i\),
  \[
  (C_tV_t)^3C_t=C_t(V_tC_t)^3.
  \]
  Since \(M_{i+t}=M_iC_t\), an \(r\)-root cube persists at every remaining
  proper bridge cut.
- Chronology decision: the persistent cube gives
  \(\kappa(M_{i+t})\ge3\), while actual binary generation gives
  \(\kappa(M_{i+t})=B[i+t]\in\{2,3\}\). Therefore
  \(B[i:r]=3^{r-i}\).
- Terminal-run decision: \(\lambda\) is the number of trailing `3`
  symbols in \(B\), allowing \(\lambda=0\). The preceding all-`3`
  conclusion gives
  \[
  1\le r-i\le\lambda.
  \]
  Hence \(\lambda\le1\) forces \(r-i=\lambda=1\) and \(i=r-1\).
  The seam then reduces to \(Q[-1]=B[-1]=3\).
- Dependency decision: the binary alphabet and the full future actual
  recurrence through the remaining bridge are load-bearing. No cap,
  target negation, (C.28), \(p\)-branch, \(G/F\) canonical pair, or
  primitivity argument is used by item 4 itself. The bound
  \(\lambda\le1\) already follows from (C.33), since \(z\ge1\) and
  \(\lambda+z\le2\); (C.35l) packages it in the surviving row.
- Static sharpness decision: for
  \[
  r=3,\quad B=232,\quad Q=332,\quad R=232332232,\quad
  L=\epsilon,\quad i=1,
  \]
  the exact pairs are \(G:(2,9)\), \(M_i:(3,3)\), and \(F:(3,3)\);
  the seam is \(\operatorname{suf}_2(BQ)=32=B[1:3]\), and
  \(\lambda=0\), yet \(i\ne r-1\). It is not an actual bridge:
  after the current `3`, persistence forces another `3` instead of the
  proposed \(B[2]=2\). This pins why a static/current-cut argument is
  insufficient.
- Converse decision: the seam equation does not make the \(r\)-root
  canonical. The frozen
  \(q=13,r=4,B=2232,Q=32332,L=\epsilon,i=2\) model has the prescribed
  \(B^2\) recurrence through cut six, with pairs
  \[
  (2,13),(2,1),(3,1),(2,4),(2,4),(2,1),(3,1).
  \]
  It satisfies the seam, but its canonical pair at \(M_i\) is \((3,1)\).
  Cut seven has pair \((3,4)\) instead of the proposed final `2`, so future
  generation fails. The implication remains one-way.
- Finite-audit decision: independently enumerate all binary \(B,Q\) with
  \(B[0]=2,\ Q[0]=3,\ R=BQB,\ L=\epsilon\),
  \(1\le r,|Q|\le7\), and every \(i\) with \(B[i]=3\), cross-checking each
  pair with two exact suffix-power oracles. Exactly `5,314` static cuts
  have pair \((3,r)\), with zero seam failures; `1,113` further static
  seam cuts have pair \((3,h)\) with \(h<r\). After additionally requiring
  \(G:(2,q)\) and the prescribed recurrence at all \(2r\) proper bridge
  cuts, `29` seam cuts remain, all also with endpoint pair \(F:(3,r)\).
  Every one has \(B[i:r]\) all `3`, and none with \(\lambda\le1\) has
  \(i\ne r-1\). These counts are finite corroboration only, not the later
  \(q\le25\) D-035 census.
- Endpoint decision: \(i=0\) cannot request `3` because \(B[0]=2\);
  \(r=1\) is vacuous; the induction uses only \(0\le t<r-i\), so the
  completed state \(F=M_r\) is not treated as another proper indexed cut.
- Target decision: the implication from \(h=r\) is target-independent.
  The \(\mathcal J\)-negation is only how item 3 supplies the cap at every
  proper bridge cut. The \(\mathcal I\)-negation does not cap arbitrary
  omitted second-half `3` cuts, so items 3--4 do not give an exhaustive
  \(\mathcal I\)-classification.
- Verification: both independent curling-number implementations recompute
  the \(q=9\) chronology warning and the \(q=13\) failed-converse model.
  An independent reproduction gives the exact finite counts
  `5,314 / 1,113 / 29`. The full repository suite passes `144` tests;
  `compileall`, unique-tag inspection, and `git diff --check` are clean.
- Review: independent exact-proof, adversarial countermodel/evidence, and
  publication/scope reviews returned `APPROVED`. They checked the seam
  cancellation, every rotation index, the binary and future-recurrence
  dependencies, the C.33/C.35l distinction, endpoints, both warnings,
  finite count units, target scope, and every stated non-claim.
- Scope: the no-fourth consequence, bounded bridge census, both boundary
  word walls, non-boundary Cell C, Cell C, both G2CS targets, and the
  Curling Number Conjecture remain open.

## D-035 item 5 — exact target-scope ledger

- Date: 2026-07-27
- Status: target distinction `PROVED-NL`; overall D-035 remains
  `IN PROGRESS`; Cell C remains `OPEN`.
- Membership decision: on the simultaneous boundary \(s=2r\),
  \[
  K_0=G,\qquad K_r=M,\qquad K_{2r}=F,
  \]
  and the family definitions give
  \[
  \mathcal I\cap\{K_h:0\le h\le2r\}=\{G,F\},\qquad
  \{K_h:0\le h\le2r\}\subseteq\mathcal J.
  \]
  Thus every strict interior bridge state is omitted from \(\mathcal I\)
  and included in \(\mathcal J\). The completed endpoint \(F=K_{2r}\)
  is not an indexed proper bridge-generation cut.
- \(\mathcal J\)-decision: negating G2CS-\(\mathcal J\) gives
  \(\pi(W)<P\) for every \(W\in\mathcal J\), hence directly caps every
  proper \(K_h\), \(0\le h<2r\).
- \(\mathcal I\)-decision: negating G2CS-\(\mathcal I\) directly caps
  \(G,F\), but supplies no inequality for \(0<h<2r\). Since \(B[0]=2\),
  every proper bridge cut requesting `3` has \(i>0\) and is one of these
  omitted interior states. Its cap is not automatic.
- Self-cap decision: independently of either target, (C.35z) gives
  \[
  B[i]=2\Longrightarrow
  \pi(K_i)\le q<P,\qquad \pi(K_{r+i})\le r<P.
  \]
  Therefore every proper actual `2`-cut is capped even in the stronger
  \(\mathcal I\) analysis.
- Localization-order decision: (C.28) assumes the period is below \(P\).
  It may localize a `2`-cut only after (C.35z) supplies that cap. It cannot
  be invoked circularly to cap an arbitrary omitted `3`-cut.
- Non-claim: saying that the \(\mathcal I\)-negation supplies no automatic
  cap at omitted `3`-cuts does not assert that a particular cut has
  \(\pi\ge P\). The two `3`-cut theorems remain valid conditional on an
  independently supplied cap.
- Verification: the closed bridge membership was re-derived from the
  authoritative definitions of \(\mathcal I,\mathcal J,K_h\), with both
  endpoint overlaps and the proper-cut range checked separately. The full
  repository suite passes `144` tests; `compileall`, unique-tag inspection,
  and `git diff --check` are clean.
- Review: independent exact-scope and adversarial/publication reviews
  returned `APPROVED`. They checked \(G,M,F\), every proper-cut quantifier,
  the label-`3` endpoint exception, the C.35y--C.35z self-cap dependency,
  the C.28 ordering, repository-standard evidence labels, and all
  non-claims.
- Scope: the no-fourth consequence, bounded bridge census, both boundary
  word walls, non-boundary Cell C, Cell C, both G2CS targets, and the
  Curling Number Conjecture remain open.

## D-035 item 6 — actual binary cuts exclude fourth-power suffixes

- Date: 2026-07-27
- Status: no-fourth bridge consequence `PROVED-NL`; overall D-035 remains
  `IN PROGRESS`; Cell C remains `OPEN`.
- Terminology decision: the roadmap phrase “visible proper fourth power”
  was previously undefined and overloaded. In this checkpoint, *visible at
  the cut* means wholly contained in the displayed finite suffix ending at
  that cut. A proper circular root has length below the ambient word scale:
  \(a<q\) in \(R^2A_i\) and \(a<r\) in \(B^2A_i\). The exact containment
  conditions are \(4a\le2q+i\) and \(4a\le2r+i\), respectively.
- Strong theorem decision: for every indexed proper bridge cut,
  \(0\le h<2r\), actual generation gives
  \[
  \kappa(K_h)=(B^2)[h]=B[h\bmod r]\in\{2,3\}.
  \]
  A suffix \(Y^4\), \(Y\ne\epsilon\), would instead force
  \(\kappa(K_h)\ge4\). Therefore no fourth-power suffix of any root length
  ends at any proper actual binary bridge cut. The visible proper circular
  statement is an immediate special case.
- Dependency decision: the proof is definition-level. It uses only the
  actual-orbit recurrence and the binary output alphabet. It uses no period
  cap, canonical root, target negation, (C.28), Fine--Wilf argument, or
  primitivity hypothesis.
- Endpoint decision: \(F=K_{2r}\) is not an indexed proper bridge cut and
  is excluded from the quantified theorem. It separately has
  \(\kappa(F)=3\), so it also has no fourth-power suffix.
- Nonclaims: the theorem does not exclude an internal fourth-power factor
  which ends before the current cut, a circular occurrence not contained
  in the displayed suffix, or a static proposed bridge which does not obey
  the orbit recurrence. It gives no bound on \(\pi(K_h)\) and does not make
  the whole bridge word fourth-power-free as a factor language.
- Review: independent derivation and adversarial-semantic audits agreed on
  the stronger suffix theorem and produced explicit warnings against the
  internal-factor and static-bridge readings. A fresh exact-proof/spec
  review returned `APPROVED`; it checked the modulo indexing, both visible
  suffixes, containment inequalities, endpoint, dependencies, nonclaims,
  and unique equation tags. The publication review caught and required the
  item-6 block to be moved after item 5 so the append-only chronology and
  latest scope remained correct; its fresh re-review then returned
  `APPROVED`.
- Verification: the full repository suite passes `144` tests;
  `compileall`, ordered item-heading inspection, unique-tag inspection, and
  `git diff --check` are clean.
- Scope: the definition-first \(q\le25\) two-branch bridge census, final
  D-035 integrated reviews, both boundary word walls, non-boundary Cell C,
  Cell C, both G2CS targets, and the Curling Number Conjecture remain open.

## D-035 item 7 — bounded standalone-local bridge census

- Date: 2026-07-27
- Status: the census is `COMPUTED`, and the mathematical and
  code/publication reviews are `APPROVED`. Overall D-035 remains
  `IN PROGRESS` pending commit and push; Cell C remains `OPEN`.
- Scope decision: the scan begins at the finite standalone seed
  \(G_{\rm loc}=X^3U\) and directly requests \(B^2\). A complete local
  replay matches all \(2r\) requested labels. No arbitrary left context
  \(L\) or full-context orbit is enumerated. The executable records
  `orbit_scope=standalone_G_loc_seed`, `target_assumption=none`, and
  `full_context_not_enumerated=true`. It preserves the exact
  \(\mathcal I/\mathcal J\) bridge ledger without assuming either target
  negation.
- Enumeration decision: through \(q\le25\), the \(p>q\) branch has
  `2,388,798` structures, `595,896` \(z=1\) assignments, `105,851` exact
  static candidates, `15,881` complete local replays, and `127,048`
  proper cuts; every replay has \(r=4,\ B=\texttt{2232}\). The \(p<q\)
  branch has `1,115,405 / 418,622 / 100,053 / 93,497 / 187,018` in the
  same stages. Its replays split into `93,493` with
  \(r=1,\ B=\texttt{2}\) and four with
  \(r=4,\ B=\texttt{2223}\). Every complete replay has all proper periods
  below \(P\) and the exact endpoint pair \((3,r)\). These counts are
  finite `COMPUTED` evidence.
- Fourth-power decision: every proper cut separately enumerates all
  fourth-power suffix roots of the full standalone-local state and the
  visible proper-circular subset. Both root-occurrence and affected-cut
  counts are zero in both branches.
- Theorem-audit unit decision: an opportunity is counted once per eligible
  completed replay or proper cut, not once per root. The \(p>q\)
  opportunity counts are `15,881` endpoints, `47,643` for each `2` cap,
  `15,881` for each first/second low-root `3` bound and visibility
  conclusion, and `127,048` for each full and visible fourth-power check.
  The corresponding \(p<q\) counts are
  `93,497 / 93,505 / 4 / 187,018`. Every violation count is zero.
  Full-root seam, suffix, and terminal opportunities are zero in both
  branches, so their zero violations provide no bounded corroboration.
- One-way seam decision: the second-half `3` cross-tab contains `15,881`
  \(p>q\) rows in \((\pi<r,\text{seam false})\) and four \(p<q\) rows in
  \((\pi<r,\text{seam true})\), with every \(\pi=r\) cell zero. The audit
  checks only \(\pi=r\Rightarrow\) seam; the four true-seam low-root rows
  permanently protect the nonconverse.
- Certificate decision: six literal certificates pin the \(p>q\)
  \(q=12,r=4,B=\texttt{2232}\) replay, the \(p<q\)
  \(q=8,r=1,B=\texttt{2}\) replay, and all four nontrivial
  \(p<q,r=4,B=\texttt{2223}\) replays at \(q=23,24,25,25\). Each pins the
  full words, every cut pair, period-cap result, second-half `3` seam rows,
  endpoint, and both full and visible fourth-power counts.
- Independent-oracle decision: the test-side oracle imports no production
  D-034 generator, static predicate, witness, bridge tracer, or
  certificate selector. It reconstructs both normal forms, raw-enumerates
  \(q\le12\) with literal exponent/period loops, and independently audits
  all six certificates, including the four \(q\ge23\) rows.
- Artifact/CLI decision: the LF-stable artifact
  `research/outputs/generated_two_cube_d035_bridge_census_2026-07-27.txt`
  is reproduced end to end through
  `python -m research.generated_two_cube_d035_bridge_census --max-q 25`.
  Default stdout contains only deterministic artifact text; file-output
  mode leaves stdout empty; runtime timing is confined to stderr. The
  pinned SHA-256 is
  `60A3D2F846AC34D081A5321AC24BB7114C8C6B1A5DBF7E846756331CA6454DF7`.
- TDD and review history: initial red/green work established the local
  replay, counter, certificate, render, and artifact contracts. The
  code/publication review then required four repairs: coherent renderer
  metadata validation; exact-type, shape-safe, fail-closed certificate and
  public-atlas audits; a positive fourth-power detector probe; and a
  deterministic stdout/stderr CLI contract with subprocess reproduction.
  Each repair received its own red/green regression, including the
  requested detector mutation test. Mathematical review remained
  `APPROVED`, and the repaired code/publication review returned
  `APPROVED`.
- Integrated-review correction: the final publication audit caught a
  notation collision in `CURRENT_STATUS.md` between the structural prefix
  \(L\) and a hypothetical context before \(X^3U\). The status now names
  the actual full bridge states \(K_h=LR^2(B^2)[0:h]\); focused re-review
  returned `APPROVED`.
- Fresh verification: `11` focused D-035 tests and `5` inherited D-034
  atlas tests pass. `compileall`, Ruff, stale-name/scope inspection,
  whitespace inspection, and `git diff --check` are clean.
- Nonclaims: this bounded standalone-local `COMPUTED` census proves no
  unbounded bridge theorem, supplies no arbitrary-\(L\) orbit, and closes
  neither period branch, non-boundary Cell C, Cell C, either G2CS target,
  nor the Curling Number Conjecture. Publication by commit and push remains
  the final unchecked D-035 checkpoint item.

## Workflow decision — proof-first research policy

- Date: 2026-07-27
- Decision: prioritize synthetic, unbounded mathematics. Defer
  nonessential infrastructure, renderers, dashboards, and large
  computational frameworks, and do not raise brute-force bounds merely
  for reassurance. Nontrivial auxiliary coding requires a clear
  mathematical necessity or explicit user approval.
- Explicit exception: short brute-force scripts and direct lemma-specific
  helpers used to test, falsify, discover, or verify a precise
  mathematical claim are not forbidden auxiliary coding.
- Freeze rule: once a bounded audit has served its mathematical role,
  freeze it and return to proof.

## D-035 closure and publication

- Date: 2026-07-27
- Status: D-035 / Phase 2B is `CLOSED`; Cell C remains `OPEN`.
- Publication: the independently reviewed eleven-file checkpoint was
  committed and pushed directly to private `main` as
  `65eaea25d3617e5cd81efa959782b82e3f5532ef`. Local `HEAD` and
  `origin/main` matched after the push.
- Final review: the integrated mathematical audit returned `APPROVED`.
  The integrated publication audit caught one notation collision in
  `CURRENT_STATUS.md`; after the actual full bridge state was written as
  \(K_h=LR^2(B^2)[0:h]\), focused re-review returned `APPROVED`.
- Final verification: the full repository suite passes `155` tests.
  `compileall`, Ruff on every touched Python file, the pinned artifact
  SHA-256, whitespace inspection, and `git diff --check` are clean.
- Scope: closing D-035 records the bridge lemmas and the bounded
  standalone-local audit. It does not close either unbounded boundary wall,
  non-boundary Cell C, Cell C, either G2CS target, or the Curling Number
  Conjecture.
- Handoff decision: freeze the D-035 census and move to the synthetic
  \(p>q\) boundary proof, followed by the synthetic \(p<q\) proof. The only
  coding exception is a short brute-force script or direct lemma helper
  tied to a precise mathematical claim.

## Synthetic p>q small-r bridge classification

- Date: 2026-07-28
- Result: `research/pgtq_boundary_small_r.md` proves, from the six
  inherited necessary conditions (S1)-(S6) of the surviving row
  \((z,h)=(1,0)\), valid for every \(q\) and both targets: \(r\ge3\)
  (PB.1); the terminal-run transfer \(B[r-1]=B[a-1]\) with
  \(\lambda=1\Rightarrow a\ge2\Rightarrow r\ge5\) (PB.2); \(r=3\)
  impossible (PB.3); \(r=4\Rightarrow(t,B)=(3,\texttt{2232})\) uniquely
  (PB.4); the complete four-word \(r=5\) catalogue (PB.5); the exact
  \(r=4\) interior bridge-cut atlas with \(q\)-independent canonical
  pairs (PB.6); the mid-range early-root exclusion \(\alpha\ne r+t\)
  plus the large-period Fine--Wilf gap, collapsing the \(r=4\)
  phase-one trichotomy (PB.7); and explicit `3`-placement coordinates
  for both high-root returns (PB.8).
- Method note: PB.6 exponents are exact only with the actual-generation
  labels \(\kappa(K_h)=B[h\bmod r]\); a first test draft asserted raw
  curling numbers on artificial words and was corrected to assert the
  context-free suffix-square content instead.
- Evidence: `research/enumerate_pgtq_small_r_catalogue.py` and the
  artifact `research/outputs/pgtq_small_r_catalogue_2026-07-28.txt`
  (per-r complete catalogues through \(r\le12\), counts
  0,0,0,1,4,9,23,47,105,211,447,899); independent re-derivation in
  `tests/test_pgtq_small_r_catalogue.py`. Full suite: `164` passed.
- Scope: PB.4 converts the bounded census observation (every complete
  \(p>q\) replay has \(r=4,B=\texttt{2232}\)) into a synthetic
  necessity at \(r=4\). Nothing here closes the unbounded \(p>q\)
  replay wall, the \(p<q\) wall, Cell C, either G2CS target, or the
  conjecture.
- Next: attack the \(r=4\) two-window replay itself, where the low
  phase-one case forces tail \((23)^2\) in both windows and the shared
  suffix begins to determine \(Q\) letter by letter.

## p>q r=4 phase-two slice

- Date: 2026-07-28
- Result: `research/pgtq_r4_phase_two.md` (`PROVED-NL`, one replay
  step only, per the thin-slice policy). Terminal-square sieve from
  \((\kappa(R^2),\pi(R^2))=(2,q)\): the letters before the final
  \(B\) of \(R\) cannot be \(23\) (a \((232)^2\) square) and \(Q\)
  cannot end in \(B\) (a \(B^2\) square); hence \(|Q|\ge2\) and
  \(q\ge10\). Low-case phase-two dichotomy: \(U[2]=2\) with exact
  pairs \((2,2)\) in both windows, or \(U[2]=3\) with canonical cube
  roots \(\ell\ge10\) (early; \(\ell=9\) dies on the sieve,
  \(\ell\le8\) on letter arithmetic) and \(\ell'\ge14\) (later;
  \(\ell'\le12\) on letter arithmetic against the final \(B\) of
  \(R^2\), \(\ell'=13\) on the sieve). \(\ell=10\) forces
  \(Q[-20:]=(B^232)^2\) (so \(q\ge28\)); \(\ell'=14\) forces
  \(Q[-28:]=(B^332)^2\) (so \(q\ge36\)); the minimal pair
  \((10,14)\) is inconsistent at \(Q[-16]\).
- Verification: the copy-back tables were mechanically cross-checked
  with a throwaway scratchpad script during drafting; per the user's
  instruction and the proof-first policy, no census script or test
  was added to the repository for this slice.
- Next slice: Fine--Wilf compatibility of the two forced periodic
  suffixes of \(Q\) in horn 2, aiming to eliminate every pair
  \((\ell,\ell')\) and force \(U[2]=2\) outright.
- Scope: nothing here closes the \(p>q\) wall, Cell C, either G2CS
  target, or the conjecture.

## p>q r=4 horn-2 root geography

- Date: 2026-07-28
- Result: `research/pgtq_r4_horn2_geography.md` (`PROVED-NL`). In horn
  2 of the phase-two dichotomy, each cube pins reversed tail blocks
  \(\tau\) (10 letters) and \(\tau''\) (14 letters) into \(Q\) at
  depths \(\ell-9,2\ell-9\) and \(\ell''-13,2\ell''-13\); the complete
  correlation tables of \(\tau,\tau''\) plus a Fine--Wilf/primitivity
  kill prove the band theorem (G.4): in the deep-\(Q\) regime the only
  admissible pairs satisfy \(\ell''=2\ell+4\), \(\ell''\ge2\ell+13\),
  \(\ell=2\ell''-4\), or \(\ell\ge2\ell''+9\); equal roots and all
  comparable pairs are impossible, and the regime forces \(q\ge66\)
  (G.5). For every \(q\le65\), horn 2 therefore collides with the
  left edge of \(Q\).
- Sharpness: a mechanical union-find propagation of both full
  copy-back systems over \(\ell\le160,\ \ell''\le160\) returned
  exactly `8204` consistent Fine--Wilf-missing pairs, all inside and
  covering the four bands; the correlation+Fine--Wilf toolset is
  exhausted. Drafting aid only; no repository script or test added,
  per the proof-first policy and the user's math-only instruction.
- Next slice: shallow-\(Q\) edge analysis — the copy-back window
  meets the known letters of \(232\), the leading \(B\), and the
  second \(R\); goal: kill horn 2 for \(q\le65\) outright, making
  \(U[2]=2\) a theorem there, then attack the four deep bands.
- Scope: nothing here closes the \(p>q\) wall, Cell C, either G2CS
  target, or the conjecture.
