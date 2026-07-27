# Curling Number Conjecture — Approach Registry

This registry groups work by mathematical mechanism. A route is `blocked` when its
remaining lemma is theorem-strength or equivalent to the original conjecture.

| Family | Mechanism under test | Status | Concrete deliverable required |
|---|---|---|---|
| Word periods | Borders, primitive roots, Fine–Wilf overlaps | active: cube rises double | Control abrupt root drops after `q>2p` increases |
| Well-founded descent | Minimal counterexample, ordinal/rank potential | blocked: pure-power / context orientation | Descend through source-high contexted defects or fixed-origin maturations without orbit-transfer circularity |
| Infinite dynamics | Infinite counter-orbit, return words, compactness | blocked: unbounded roots | Incompatibility of bounded exponents with unbounded maximizing root lengths |
| Compression/entropy | Repeated-suffix encodings and information loss | blocked: generic squareful words | Exact self-labeling is indispensable; certificate volume alone can be quadratic |
| Arithmetic values | Constraints linking appended exponents to earlier symbols | active | Global incompatibility theorem for an infinite counter-orbit |
| Structural induction | Delete/prefix/normalize starts while preserving termination | blocked: growing pure roots | A forced pure-power root can exceed the minimal seed and reconstruct the same state |
| Eventual high exponents | Golden-ratio periodicity criterion | proved reduction | A counterorbit must output `2` infinitely often |
| Golden bad cuts | Fractional suffix exponent below `phi^2` | active: bounded kernels | Control latent crossing periods masked by identical small kernels |
| Two-event blocks | Decompose at successive square-only (`cn=2`) events | blocked: internal-square branch | New root is gap-sized/large, or lies wholly inside the 2-free gap |
| Escape towers | Exact climbs from `r` to `r+2` | blocked: scale-preserving returns | Escape blocks are realizable and can return with the same root length |
| Recurrent maximum | Forced top entrance `(M-2)(M-1)^M M` | blocked locally; global hierarchy active | Eliminate an infinite copy-parent ray of exact entrance blocks |
| Binary core | Hypothetical recurrent tail over `{2,3}` | active: low resets syndetic | Reconcile a reset root `<=2` with unbounded transported/born roots using exact labels |
| Suffix shadows | Compare global orbit to promoted orbit of a powered suffix | blocked: merging/diagonal drift | Reopen only with uniform return control or a fixed-occurrence continuation theorem |
| Root compatibility | Accumulate exact word equations across transitions | active: birth/transport split | Prove genuine root births form a well-founded tower |
| Copy-parent rays | Koenig ray plus canonical suffix duplication | active: exact push/pop geometry | Amortize left-expansion/right-drop cycles using origins |
| Rewriting/automata | Reverse orbit, grammars, dependency DAGs | active | Well-founded earliest-origin argument using exponent labels |
| Extremal/minimal bad word | Shortest bad start and forced suffix structure | queued | Finite contradiction without assuming bounded bad tail |
| Computation/oracle | Exhaustive falsification of proposed local lemmas | active | Executed counterexamples or bounded checks only |
| Formal audit | Lean 4 definitions and proof dependency check | queued | No axioms for load-bearing claims |
| Square replay | Compare one-copy and two-copy evolution | active: exact quotient split | Eliminate contexted `R^2 -> R^3` maturation; broad contexted-defect closure is false inside q21 |
| Reset anchoring | Normalize autonomous-`1` masking bridges | active: fixed-anchor descent proved | Produce unbounded `cn=1` factors at one fixed anchor; bounded sinks are equivalent to the canonical ray gap |
| Circular classification | Primitive proper-circular self-label profiles | active: q21 isolated computationally | Prove all profiles have bounded length / classify them; max-label and minimal-square routes remain open |
| Run stack | Maximal periodic runs along the canonical `2`-ray | active | Amortize >2 expansions against sharp drops while retaining exact labels |

## Computational convention and calibration

`tail_length(S)` is the least `t` such that `cn(S_t) = 1`; the corresponding
total length through the appended `1` is `len(S) + tail_length(S) + 1`, while the
A094004 convention supplied by the user is `len(S) + tail_length(S)`. The current
calibration test follows the supplied benchmark convention and exhaustively obtains
`5`, `66`, and `142` for binary starts of lengths `3`, `8`, and `22`.
