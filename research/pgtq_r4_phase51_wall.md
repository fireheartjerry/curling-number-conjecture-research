# \(p>q,\ r=4\): the phase-51 wall and the closure of the branch

Status: `PROVED-NL` (the wall theorem is a three-step synthetic
argument); the closure statement collects the previously recorded
kills. Scope: Cell C simultaneous boundary, \(p>q\), row
\((z,h)=(1,0)\), \(r=4\), \(B=\texttt{2232}\); both targets, every
\(q\).

## The letter identity

The forced word contains the bridge word at position nine:

\[
U_f[9{:}13]=(2,2,3,2)=B .
\]

Since the shared tail is \(T_\ell=B^2U_f[0{:}\ell]\), this says
\(T_\ell[17{:}21]=B\) — the bridge word sits inside the tail exactly
one quasi-period \(21\) after its own \(B^2\) head.

## Theorem W51 — the phase-51 wall

Suppose a counterorbit is tame through phase \(50\). The later
window's known consecutive suffix at phase \(51\) is

\[
B\cdot B^2\cdot U_f[0{:}51]=B^3U_f[0{:}51],
\]

of length exactly \(63\): the final \(B\) of \(R^2\) followed by the
appended \(B^2\) and the fifty-one tame symbols. The tail
\(T_{51}\) has period \(21\), and by the letter identity the
prepended \(B\) continues that period, so the whole \(63\)-letter
suffix is \(Y^3\) for its last \(21\) letters \(Y\): a genuine suffix
cube with every letter known. Hence

\[
\kappa(F_{51})\ge3>2=\kappa_{\rm loc}(T_{51}),
\]

and paired generation forces \(U[51]=\kappa(F_{51})\ge3\): the tame
value \(2\) is impossible. Therefore

\[
\boxed{\text{every }r=4\text{ counterorbit exits at some phase }
\ell^*\le51.}
\tag{W.1}
\]

This sharpens the exit ceiling of the forced-replay theorem from
\(\min(m-1,60)\) to \(\min(m-1,51)\), eliminates the exit phases
\(52,54,56,57,58,60\) outright, and in particular kills the
**period-21 exit family**: the configurations
\((\ell^*,s)=(52,21)\) and \((54,21)\) presuppose tameness through
phase \(51\), which never occurs. The family is impossible for every
\(q\). (At phase \(51\) itself the later window needs no crossing —
its cube is visible — while the early window still requires a
crossing cube, so phase \(51\) is an ordinary exit phase of the
existing inventory.)

## Theorem C — closure of the \(r=4\) branch

Every \(r=4\) exit configuration is impossible:

- exit phases are confined to \(\ell^*\le\min(m-1,51)\) (W.1);
- short roots \(s\le\ell^*+7\) force a tail period; every such pair
  at phases \(\le51\) is killed by the corrected Lemma M disposition
  (`pgtq_r4_exit_root_kill.md`, all rows valid there) in the deep
  regime \(q\ge3s-\ell^*\), and the deep condition is implied by the
  generic regime;
- non-period roots below \(\ell^*+4\) are impossible (the tail-period
  forcing is unconditional);
- \(\ell^*+4\le s\le(q-4)/2\) dies by Theorem R (unconditional);
- the band \((q-4)/2<s<(p+\ell^*-\gcd(s,p))/2\) is empty for
  \(q\ge2\ell^*+31\) (band theorem and band closure);
- \(2s\ge p+\ell^*-\gcd(s,p)\) and \(s=p\) die by Lemma F
  (unconditional);
- every configuration with \(q\le2\ell^*+30\) — including every
  small-\(q\) validity boundary above — is dead by the shallow-zoo
  verification (Z.1).

Together with the forced-replay theorem (every counterorbit must
exit) this closes the branch:

\[
\boxed{\text{No }r=4\text{ counterorbit exists: the }p>q\text{ wall
holds at }r=4\text{ for both targets and every }q.}
\tag{C.1}
\]

The chain behind (C.1) is natural-language proof plus exact finite
verification (the forced-replay table, the Lemma M disposition, the
band alignment dispositions, and the shallow zoo), in the sense fixed
in `FULL_PROOF_CHECKLIST.md`: the finite components are complete
checks of finite statements, not bounded evidence for unbounded ones.

## Non-claims

- The \(r\ge5\) catalogue of the \(p>q\) branch remains open; so do
  the \(p<q\) wall, non-boundary Cell C, both G2CS targets, and the
  conjecture.
- (C.1) should receive an adversarial audit of its full dependency
  chain before the \(p>q\) checklist box is advanced.
