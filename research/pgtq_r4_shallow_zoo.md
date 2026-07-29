# \(p>q,\ r=4\): the shallow zoo is empty

Status: `PROVED` by complete finite verification (the zoo is a finite
set, so an exhaustive check of it is a proof of the finite statement,
in the same sense as the per-\(r\) bridge catalogues); plus one
`CORRECTION` to `pgtq_r4_exit_root_kill.md` recorded below. Scope:
Cell C simultaneous boundary, \(p>q\), row \((z,h)=(1,0)\), \(r=4\),
\(B=\texttt{2232}\).

## The zoo

Every generic kill of the previous notes carries a validity bound; the
**shallow zoo** is their union: all exit configurations
\((\ell^*,q,s)\) with

\[
\ell^*\le\min(m-1,60),\qquad q\le2\ell^*+30\ (\le150),
\]

together with every admissible exit root at that \((\ell^*,q)\):
tail-period short roots, the whole band range, and the phase-\(60\)
crossing squares. Feasibility already requires the tame prefix to be
compatible with \(U=QB\) (the \(B\)-overlap conditions of the
forced-replay theorem), which alone eliminates most \((\ell^*,q)\).

## The verification

For each of the \(52{,}880\) candidate triples:

1. **Consistency.** The full three-copy state model of
   \(E=X^3U_f[0:\ell^*]\) — with both interior separators attached,
   all three occurrences of \(Q\) identified as one word, the tame
   prefix pins \(Q[0:\ell^*]\) (forced letters), and the exit-symbol
   pin — is closed under the cube relations by union-find. A known
   letter collision kills the triple outright; \(1{,}372\) triples
   survive with a partially determined \(Q\).
2. **Replay.** Each survivor is run through the complete replay with
   branch-on-demand over the remaining free letters of \(Q\): the
   early window phases \(0\) to \(m-1\) (each generated symbol must
   equal the curling number of the state), the endpoint
   \((\kappa,\pi)=(2,q)\), the four bridge cuts (generated symbols
   \(B[i]\); at \(r=4\) the bridge-cut pairs are the unconditional
   exact pins of PB.6, so this stage is target-independent), the
   later window phases, and the terminal endpoint \((2,P)\). The
   branching is exact: a letter is split only when the curling
   computation genuinely depends on it.

**Result: every one of the \(1{,}372\) survivors dies during the
replay; there are no capacity aborts and no completions.**

\[
\boxed{\text{The shallow zoo is empty.}}
\tag{Z.1}
\]

## Correction to the exit-root disposition

The re-audit performed while assembling the zoo found that two rows of
the Lemma M disposition in `pgtq_r4_exit_root_kill.md` —
\((\ell^*,s)=(52,21)\) and \((54,21)\) — had been killed with a
\(B\)-tail sieve read at pin depth \(4\), while their valid pin depth
\(3s-n\) is only \(3\) and \(1\). The note has been corrected (count
\(53\to51\), correction paragraph added), and a mechanical re-audit
of the full table with the corrected validity bound confirms these are
the only affected rows. Consequently the **period-21 exit family**

\[
(\ell^*,s)\in\{(52,21),(54,21)\},\qquad q>2\ell^*+30,
\]

is open again at generic \(q\): the exit cube rides the quasi-period
\(21\) of the forced word at the last two \(21\)-periodic exit
phases, its window crosses by only \(3\) (resp. \(1\)) letters, and
none of the generic kills reaches it. Inside the zoo it is dead by
(Z.1).

## Where the \(r=4\) branch stands

Combining the forced-replay theorem, the exit-root kills, the band
theorem with its closure, and (Z.1):

- every exit configuration with \(q\le2\ell^*+30\) is dead (Z.1);
- every exit configuration with \(q\ge2\ell^*+31\) is dead **except**
  the period-21 family;
- hence the \(r=4\) branch of the \(p>q\) wall reduces to exactly
  two items: the **period-21 exit family** at generic \(q\), and the
  \(r\ge5\) catalogue.

## Non-claims

- The period-21 family at \(q>2\ell^*+30\) is not eliminated; it is
  the next synthetic target (simulation is inapplicable there — the
  free middle of \(Q\) grows with \(q\)).
- The bridge-cut stage of the verification uses the exact \(r=4\)
  bridge pins of PB.6; the windows and endpoints are conditions of
  both targets.
- Per the math-only policy no verification script is committed; the
  method is specified above precisely enough to reproduce, and the
  run was performed twice with independent survivor extraction.
- Nothing here closes the \(p>q\) wall, Cell C, either G2CS target,
  or the conjecture.
