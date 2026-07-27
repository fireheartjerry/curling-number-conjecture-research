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
