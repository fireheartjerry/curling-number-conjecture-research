# Codex continuation prompt — Curling Number Conjecture

You are continuing a three-chat collaborative attack on the Curling Number Conjecture. The repository contains a 200 KB canonical mega-ledger plus every preserved audit, output, earlier ledger, and the original research prompt.

## Mandatory reading order

1. `CURLING_NUMBER_CONJECTURE_MEGA_LEDGER_2026-07-27.md`, Sections 0–3.
2. Part C, especially Sections 14–23.
3. Part E, especially Sections 28–32.
4. Only then use the verbatim appendices and `sources/` files for archaeology.

When older notes conflict with the front of the mega-ledger, the front is authoritative.

## Current mathematical target

Prove or disprove the **Generated Two-Cube Synchronization Lemma**, then conclude the full bridge-promotion lemma.

Use the canonical notation:

\[
R=AB=TU,
\qquad
q=|R|,
\qquad
b=|B|,
\qquad
P=q+b,
\]

\[
T=R[0:j],
\qquad
U=R[j:q],
\qquad
Y=BR=BTU.
\]

The actual orbit windows are

\[
E=LRT\xrightarrow{\ U\ }G=LR^2,
\]

\[
F=LR^2BT\xrightarrow{\ U\ }H=LR^2BR.
\]

At a first promotion failure:

\[
\operatorname{cn}(E)=3,
\quad
\operatorname{cn}(G)=2\text{ with shortest period }q,
\quad
\operatorname{cn}(F)=3,
\quad
\operatorname{cn}(R^2T)=2.
\]

Let `p` and `r` be the shortest cube periods at `E` and `F`. Prove that the hypotheses force a cube in `R^2T`, or force a canonical period at least `P` at one of the two endpoints or during one of the two generated copies of `U`.

## Already proved or provisionally derived

Do not redo these from scratch unless auditing them finds a specific error:

- every `2`-position promotes;
- a first failure is necessarily `3 -> 2`;
- `p != q`;
- `j < p - gcd(p,q)`;
- later cube dichotomy:
  \[
  2r\le P-\gcd(r,P)-1
  \quad\text{or}\quad
  b+j\le r-\gcd(r,P)-1;
  \]
- in the external later-cube branch, `q <= r < P`;
- if `r=q`, then `b<q/2`, `B` is a border of `R`, and
  \[
  R[0:j]=R[b:b+j];
  \]
- if `q<r<P`, with `c=r-q` and `delta=P-r=b-c`, then
  \[
  q/2<c<b,
  \]
  `R` has period `c`,
  \[
  B=suf_c(R)R[0:\delta],
  \qquad
  R[0:j]=R[\delta:\delta+j].
  \]
- the Border–conjugate short-period lemma has a natural-language proof but requires an independent index audit before load-bearing use.

## The three remaining cells

### Cell A: external later cube, `r=q`

Extract a period `0<t<b` on `UT`, directly force a cube in `R^2T`, or force an intermediate canonical period at least `P` by using actual generation of `U`.

### Cell B: external later cube, `q<r<P`

Combine the long `c`-period of `R`, the `delta`-shift equality on its prefix, and the fact that the same block `U` is generated in both windows.

### Cell C: internal later cube

Classify whether the `r`-cube is contained in `Y`, crosses `Y|B`, or crosses `B|T`. Exhaust the cases explicitly.

## Computational protocol

Before using any computed curling number, calibrate against:

- `322 -> 5`;
- `23222323 -> 66`;
- `2322322323222323223223 -> 142`.

Use the exact shortest-maximizing-period routine in `sources/curling_research_tools.py` or the C++ equivalents. Never infer `cn` from only the trailing symbol run.

Run first:

```bash
python sources/verify_part3_examples.py

g++ -O3 -std=c++20 sources/audit_all_square_replay.cpp -o /tmp/audit_replay
/tmp/audit_replay 18 500
```

## Prohibited stale routes

Do not reopen unchanged:

- total-gcd equality-graph connectivity;
- universal bridge crossing;
- unconditional pairwise cube-edge descent;
- static border geometry without actual generation;
- “generated `R^2` alone implies promotion”;
- bounded promotion-necklace lengths;
- restricted-map predecessor isolation.

## Required deliverables

Produce:

1. `UPDATED_PROOF_LEDGER.md` with explicit statuses;
2. executable code for every numeric claim;
3. a complete proof or counterexample for Generated Two-Cube Synchronization;
4. if successful, a complete bridge-promotion proof;
5. an adversarial endpoint/generation/maximality audit;
6. a revised remaining-work checklist toward autonomous exact-power termination.

Do not claim the full Curling Number Conjecture merely from bridge promotion. The final autonomous exact-power wall remains separate.
