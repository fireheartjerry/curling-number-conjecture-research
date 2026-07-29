# \(p>q,\ r=4\): the forced replay and the mandatory exit

Status: `PROVED-NL` (the pair table is exact finite letter arithmetic,
double-checked with two independent curling implementations during
drafting; no repository script is attached). Scope: Cell C
simultaneous boundary, branch \(p>q\), surviving row \((z,h)=(1,0)\),
\(r=4\), \(B=\texttt{2232}\); both targets, every \(q\). This note
removes the "low case" hypothesis, determinizes the entire tame
replay, and proves that every counterorbit must produce a
context-crossing canonical power by phase \(60\).

## E.1 — the phase-one high branch is vacuous at \(r=4\)

\(T_1=B^2\,3\) ends in the square \((23)^2\), and root \(1\) admits no
square there. Paired generation gives
\(\kappa(E_1)=\kappa(F_1)=U[1]=2\) exactly, so the canonical root of
each window is the **least** root achieving exponent two, which is
\(2\). Hence

\[
\boxed{(\kappa,\pi)(E_1)=(\kappa,\pi)(F_1)=(2,2)\ \text{always.}}
\tag{E.1}
\]

The high alternative of PB.7c never occurs at \(r=4\), and the "low
case" hypothesis of `pgtq_r4_phase_two.md` and
`pgtq_r4_horn2_geography.md` is discharged: those results now hold
unconditionally at \(r=4\).

## E.2 — local pairs and the tame regime

For a state with shared tail \(T*\ell=B^2U[0:\ell]\), call a suffix
power **local** when its full window fits inside \(T*\ell\), and let
\(\kappa*{\rm loc}(T*\ell)\) be the greatest local exponent — this is
exactly the curling number of the word \(T\_\ell\). Basic facts:

1. \(\kappa(\text{state})\ge\kappa\_{\rm loc}\), because local powers
   are genuine suffix powers.
2. If \(\kappa(\text{state})=\kappa\_{\rm loc}\), the canonical pair of
   the state **equals** the local canonical pair: the least local
   achiever bounds the canonical root, and any root smaller than the
   least local achiever would itself be local.
3. A **downward deviation** \(U[\ell]<\kappa*{\rm loc}(T*\ell)\) is
   impossible: generation would give
   \(\kappa(\text{state})=U[\ell]<\kappa\_{\rm loc}\), contradicting 1.
4. An **upward deviation** \(U[\ell]>\kappa*{\rm loc}(T*\ell)\) forces
   a window-crossing canonical power: exponent \(U[\ell]\), window
   \(U[\ell]\cdot\pi>8+\ell\). Both windows deviate together, since
   they share \(T\_\ell\) and the requested symbol.

Call the replay **tame at phase \(\ell\)** when
\(U[j]=\kappa\_{\rm loc}(T_j)\) for all \(1\le j\le\ell\). While tame,
the tail evolves autonomously: the replay is precisely the curling
orbit of the seed word

\[
T_1=B^2\,3=\texttt{223222323}.
\]

## E.3 — the forced word and the phase-60 wall

Running that orbit (exact arithmetic, both engines agreeing) gives the
forced symbols

\[
U[0:60]=\texttt{322232223223222322232322232223223222322232322232223223232223}
\]

with local pair table

\[
\begin{array}{l}
1{:}(2,2);\ 2{:}(2,2);\ 3{:}(2,1);\ 4{:}(3,1);\ 5{:}(2,6);\
6{:}(2,6);\ 7{:}(2,1);\ 8{:}(3,1);\\
9{:}(2,4);\ 10{:}(2,4);\ 11{:}(3,4);\ 12{:}(2,3);\ 13{:}(2,3);\
14{:}(2,1);\ 15{:}(3,1);\ 16{:}(2,7);\\
17{:}(2,4);\ 18{:}(2,1);\ 19{:}(3,1);\ 20{:}(2,4);\ 21{:}(3,4);\
22{:}(2,2);\ 23{:}(2,2);\ 24{:}(2,1);\\
25{:}(3,1);\ 26{:}(2,6);\ 27{:}(2,6);\ 28{:}(2,1);\ 29{:}(3,1);\
30{:}(2,4);\ 31{:}(2,4);\ 32{:}(3,4);\\
33{:}(2,3);\ 34{:}(2,3);\ 35{:}(2,1);\ 36{:}(3,1);\ 37{:}(2,7);\
38{:}(2,4);\ 39{:}(2,1);\ 40{:}(3,1);\\
41{:}(2,4);\ 42{:}(3,4);\ 43{:}(2,2);\ 44{:}(2,2);\ 45{:}(2,1);\
46{:}(3,1);\ 47{:}(2,6);\ 48{:}(2,6);\\
49{:}(2,1);\ 50{:}(3,1);\ 51{:}(2,4);\ 52{:}(2,4);\ 53{:}(3,4);\
54{:}(2,3);\ 55{:}(3,21);\ 56{:}(2,2);\\
57{:}(2,2);\ 58{:}(2,1);\ 59{:}(3,1);\qquad
60{:}\ \kappa\_{\rm loc}=1 .
\end{array}
\tag{E.3}
\]

At phases \(5\), \(6\), and \(55\) the exponent-limiting mismatch of
the tabulated root lies outside the tail, so the tabulated exponent is
exact only in the no-crossing regime — which is what tame means; at
every other phase it is exact unconditionally. All local roots are at
most \(21<P\), so tameness never violates the sampled period caps.

**The wall.** At phase \(60\) the tame tail has **no square at all**:
\(\kappa*{\rm loc}(T*{60})=1\). The counterorbit must generate
\(U[60]\in\{2,3\}\), which then requires a crossing power. In other
words, the inner curling orbit of the seed \(\texttt{223222323}\)
reaches curling number \(1\) after \(59\) steps — exactly the
behaviour the Curling Number Conjecture predicts — and the counterorbit
can survive only by a context-crossing power.

## E.4 — endpoint necessity

Suppose the replay is tame through phase \(m-1\). Then \(U\) equals
the forced word wherever defined, and since \(U=QB\) ends in \(B\),
the forced word must contain \(\texttt{2232}\) at position \(|Q|=q-8\).
Within the valid range this happens exactly for

\[
q\in\{10,14,17,21,25,31,35,38,42,46,52,56,59\},
\]

and for each of these the tame local pair at the endpoint phase
\(m=q-4\) is

\[
(2,6),(2,4),(2,3),(2,4),(3,4),(2,6),(2,4),(2,3),(2,4),(3,4),(2,6),
(2,4),(3,21)
\]

respectively — never the required \((\kappa,\pi)(E*m)=(2,q)\): the
\(\kappa*{\rm loc}=3\) cases contradict \(\kappa=2\) outright, and in
the \(\kappa\_{\rm loc}=2\) cases the canonical root equals the local
root \(\le6<q\). For every other \(q\le64\), the \(B\)-suffix of \(U\)
clashes with the forced word before phase \(m\); a clash where the
forced value is \(3\) and the \(B\)-letter is \(2\) is a downward
deviation (impossible), and a clash the other way is an upward
deviation. For \(q\ge65\), phase \(60\) precedes \(m\). In every case
tameness through phase \(m-1\) is impossible.

The documented \(q=10\) near-model is exactly the tame trajectory
(\(Q=\texttt{32}\) is the forced prefix), and its recorded failure is
exactly this endpoint kill at \((2,6)\ne(2,10)\). The \(q=23\) warning
model deviates upward from the forced word first at phase \(13\) —
precisely the phase where the atlas recorded its replay failure.

## Theorem E.5 — the mandatory exit

Every \(r=4\) counterorbit (either target, every \(q\)) has a first
**exit phase** \(\ell^\*\) with

\[
\boxed{\ell^\*\le\min(m-1,\,60),}
\tag{E.5}
\]

at which both windows end in window-crossing canonical powers with
common exponent \(U[\ell^*]\): crossing **cubes** when
\(\kappa*{\rm loc}(T*{\ell^_})=2\) (all exit phases except \(60\)),
and a crossing square or cube at phase \(60\). Exits are impossible at
\(\kappa\_{\rm loc}=3\) phases. The prior phase-two dichotomy and the
horn-2 band geography describe the case \(\ell^_=2\); every other exit
phase carries a concrete known tail from (E.3), so the same
correlation machinery applies to each.

**Proof.** By E.2(3) no downward deviation exists, so the replay is
tame until its first upward deviation, which by E.2(4) is a crossing
exit at both windows simultaneously. By E.4 tameness cannot reach
phase \(m\), and by E.3 it cannot pass phase \(59\). At
\(\kappa\_{\rm loc}=3\) phases the requested symbol cannot exceed the
local value because \(U[\ell]\le3\). \(\square\)

## Consequences

- The \(r=4\) wall is no longer an unbounded phase-by-phase problem:
  it is reduced to finitely many concrete exit events — one per
  \(\kappa\_{\rm loc}\le2\) phase in (E.3) — each a double
  crossing-power configuration over an explicitly known tail.
- For the thirteen tame-consistent \(q\) values, the unique tame
  choice of \(Q\) (the forced prefix) is eliminated outright.
- The connection to the conjecture is structural: the tame core of the
  wall dies because the inner curling orbit of \(\texttt{223222323}\)
  reaches \(1\); counterorbits survive only through context-crossing
  powers, which is where all remaining difficulty now lives.

## Non-claims

- The exit events themselves are not eliminated; phase \(2\) is
  restricted by the earlier notes, the others await the same
  treatment.
- Nothing here treats \(r\ge5\), the \(p<q\) branch, non-boundary
  Cell C, either G2CS target, or the conjecture.
