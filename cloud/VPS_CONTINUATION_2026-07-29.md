# VPS continuation brief — 2026-07-29 pause point

State of Cell C, boundary p>q wall (checklist Phase 2C, box 1),
after the 2026-07-28/29 campaign (commits b7815f2..2fcfa89).

## Closed

- r <= 3: impossible (PB.1/PB.3). r = 4: branch fully closed (C.1 in
  `research/pgtq_r4_phase51_wall.md`), via: forced-replay theorem,
  exit-root kills (Theorem R / Lemma M / Lemma F), band theorem +
  period-ten closure, empty shallow zoo (52,880 cases), phase-51 wall.
  Pending: adversarial audit of the chain.
- 5 <= r <= 20: every catalogue word killed by the cut filters
  (`research/pgtq_r5_cut_filters.md`) EXCEPT the two r=13 words below.

## Open — the three remaining items of the p>q wall

1. **B1 = 2232223322232** (r=13, t=9, a=4, lambda=0).
   Seed orbit of B1^2 3: forced symbols 3,2,2,2,3; kappa_loc = 1 at
   phase 5. E-side and F-side local pairs agree through phase 4
   (F-side has no forced deviation). Exits: cubes at phases 1,2,3;
   squares or cubes at phase 5 (both windows kappa_loc = 1 there).
   Plan: re-instantiate the r=4 exit machinery at r=13 (Theorem R is
   r-generic: kills roots in [l*+13, (q-13)/2]; Lemma F is generic;
   short roots via tail periods + pinned sieve; band via the
   separator rev(B1[4:13]) + rev(B1^2), 35 known letters, sigma_0 =
   l*+q+1, same two-hop lemma). The phase-5 square exits need the
   square machinery of item 2.
2. **B2 = 2232223222332** (r=13, t=12, a=1, lambda=0).
   Seed B2^2 3 has NO local square (kappa_loc = 1 at phase 1), and
   the F-side B2^3 3 also has kappa = 1. The z-row forces U[1] = 2,
   so BOTH windows need context-crossing SQUARES at phase 1. Known
   restrictions: alpha < p with the adjacent pop (C.35n);
   alpha > 2r (new second-large-period lemma in
   `research/pgtq_r5_cut_filters.md`: alpha in (r,2r] would force a
   second large period delta = alpha - r with B[r-delta] = 3, and B2
   has none); beta in the (C.35o/s) high branch with the (C.35q)
   return. NEEDED: an exponent-two analogue of the exit pipeline.
   Square relations give only ONE copy (t_i = t_{i+s}, i <= s), so:
   partial-period known-known tests; pin-then-sieve (pinned Q-tail =
   reversed tail at depths [alpha-n+1, alpha]); one-hop separator
   equations for large alpha; cross-window double-pin consistency
   (E pins vs F pins on the shared Q-tail); then post-exit
   continuation. Small q: run `research/engines/r13_zoo.py` (ready,
   not yet run) for q <= 160 for both words.
3. **Uniform r >= 21.** Route laid out in
   `research/pgtq_r5_cut_filters.md`: S16/S11 bound all letter runs
   by three; S12 grounds every 3 in a 222-feed or an exotic circular
   cube; the interior-slide argument bounds every exotic cube's
   periodic support below four times its root; recursively the
   exotic roots satisfy miniature S11/S12 conditions. Target: a
   finite-tile classification of admissible B, closed against the
   border structure (S2: B = A N A with the double-A seam) and
   primitivity. The empirical fact that only the two r=13 words
   survive through r = 20 suggests the classification is tight.

## Practical notes

- The J-caps (D-035) are legitimate for this box: the checklist item
  is the p>q wall for G2CS-J.
- Beware the local formatter corruption issue if editing markdown
  with tool-assisted editors (see the 2026-07-28 hygiene entry in
  docs/DECISION_LOG.md): underscore/asterisk swaps. Plain-file
  writes are safe.
- All letter-arithmetic claims in the notes were machine-verified
  with the engines in `research/engines/`; re-run them after any
  refactor.
- House rules: proof-first, thin slices, exact finite checks are
  proofs of finite statements only, update CURRENT_STATUS.md and
  docs/DECISION_LOG.md at every checkpoint.
