# Repaired Generated Two-Cube Synchronization statement

**Status:** open target; statement frozen for falsification and proof work.
Nothing below claims that synchronization, bridge promotion, or the Curling
Number Conjecture has been proved.

## Canonical functions

All words are finite words over the positive integers. For a nonempty word
\(W\), define its curling number by

\[
\kappa(W)=\max\{k\ge 1: W=SX^k
  \text{ for some word }S\text{ and nonempty word }X\}.
\]

Define the executable canonical-period convention piecewise:

\[
\pi(W)=
\begin{cases}
|W|, & \kappa(W)=1,\\[2mm]
\min\{|X|: W=SX^{\kappa(W)}
  \text{ for some word }S\text{ and nonempty word }X\},
  & \kappa(W)\ge2.
\end{cases}
\]

When \(\kappa(W)\ge2\), \(\pi(W)\) is the least period among suffixes
\(X^{\kappa(W)}\): it is the shortest maximizing period, never merely the
period of a displayed lower power. When \(\kappa(W)=1\), the value \(|W|\) is
an explicit executable sentinel. It is not a claim that \(|W|\) is the
literal shortest choice of \(X\) in a decomposition \(W=SX^1\), whose
unrestricted minimum would be \(1\).

For a word \(V\), the slice \(V[a:b]\) uses zero-based, half-open
coordinates. A curling-number orbit is a sequence of full states
\((S_t)_{t\ge0}\) satisfying

\[
S_{t+1}=S_t\,\kappa(S_t),
\]

where every \(S_t\) is nonempty and \(\kappa(S_t)\) is appended as the next
symbol.

## Structural data and actual states

Let \(L,A,B,T,U\) be words, write \(x=|L|\), and suppose

\[
R=AB=TU,\qquad q=|R|,\qquad b=|B|,\qquad P=q+b,
\]

with \(B\ne\epsilon\) and

\[
|A|=q-b>0.
\]

Equivalently,

\[
0<b<q,\qquad q>\frac P2.
\]

Choose \(j\) with

\[
T=R[0:j],\qquad U=R[j:q],\qquad
0\le j<q,
\]

and put

\[
m=|U|=q-j>0,\qquad Y=BR=BTU.
\]

The four endpoint states are

\[
E=LRT,\qquad G=LR^2,\qquad
F=LR^2BT,\qquad H=LR^2BR.
\]

The exact states during the two generated copies of \(U\) are

\[
E_\ell=LRTU[0:\ell]\quad(0\le\ell\le m),
\]

\[
F_\ell=LR^2BTU[0:\ell]\quad(0\le\ell\le m).
\]

Consequently,

\[
E_0=E,\qquad E_m=G,\qquad F_0=F,\qquad F_m=H.
\]

The proper pre-completion set is

\[
\mathcal I=
\{E_\ell:0\le\ell\le m\}
\mathbin{\cup}
\{F_\ell:0\le\ell<m\}.
\]

In particular, \(G\in\mathcal I\) and \(H\notin\mathcal I\). The union is a
set: duplicate descriptions, if any, are counted once and cannot change
\(\max_{W\in\mathcal I}\pi(W)\). Under the present nondegeneracy conditions,
the displayed full-state lengths are distinct in orbit order anyway.

## Actual paired generation

The primitive actual-generation hypothesis is not shorthand for a static word
equation. There must be a curling-number orbit \((S_t)\) and an index \(t_0\)
such that the following full-state equalities hold:

\[
E_\ell=S_{t_0+\ell}\quad(0\le\ell\le m),
\]

\[
F_\ell=S_{t_0+P+\ell}\quad(0\le\ell\le m).
\]

The following are derived audit consequences, not additional generation
hypotheses. Applying the orbit recurrence to consecutive full-state
equalities gives, at every proper prefix of the two copies of \(U\),

\[
\boxed{
\kappa(E_\ell)=U[\ell]=\kappa(F_\ell)
\qquad(0\le\ell<m).
}
\]

These are curling numbers of the full contexts \(LRTU[0:\ell]\) and
\(LR^2BTU[0:\ell]\). They are stronger than static equalities of displayed
words, and stronger than any assertion about a standalone continuation from
\(R^2T\). In this orbit the word generated between the endpoints \(E\) and
\(F\) is exactly \(UBT\), and every state in \(\mathcal I\) occurs strictly
before the completion state \(H=S_{t_0+P+m}\). Indeed,

\[
G=S_{t_0+m},\qquad H=S_{t_0+m+P},
\]

so the full bridge root \(Y=BTU\) is actually generated from \(G\) to \(H\).
Moreover,

\[
P-m=b+j>0,
\]

which places \(E_m=G\) strictly before \(F_0=F\), and places every member of
\(\mathcal I\) strictly before \(F_m=H\).

## Bridge states and the full proper pre-completion set

Put

\[
s=|BT|=b+j.
\]

The endpoint equalities above and the one-symbol orbit recurrence also fix
every state in the otherwise omitted bridge from \(G\) to \(F\):

\[
K_h=S_{t_0+m+h}=LR^2(BT)[0:h]
\qquad(0\le h\le s).
\]

Thus

\[
K_0=G,\qquad K_s=F,
\]

and \(s>0\). The natural full proper pre-completion set is

\[
\mathcal J=\{S_t:t_0\le t<t_H\},
\qquad t_H=t_0+P+m.
\]

Its decomposition into the three chronological windows is

\[
\boxed{
\mathcal J=
\{E_\ell:0\le\ell\le m\}
\mathbin{\cup}
\{K_h:0\le h\le s\}
\mathbin{\cup}
\{F_\ell:0\le\ell<m\}.
}
\]

The overlapping descriptions at \(G=E_m=K_0\) and
\(F=K_s=F_0\) denote the same orbit occurrences. Equivalently, a disjoint
occurrence decomposition uses \(E_0,\ldots,E_m\), then
\(K_1,\ldots,K_s\), then \(F_1,\ldots,F_{m-1}\). It includes the entire
proper bridge, includes \(F\), and excludes \(H=F_m=S_{t_H}\). In
particular,

\[
\mathcal I\subseteq\mathcal J.
\]

The executable helper `bridge_inclusive_precompletion_states` mirrors this
ordered decomposition: it checks both endpoint overlaps, includes each of
\(G,F\) once, and removes only \(H\).

### Binary hard-core scope of the sentinel

In the intended binary hard-core application, \(U\in\{2,3\}^m\). The derived
paired-generation equalities give

\[
\kappa(E_\ell),\kappa(F_\ell)\in\{2,3\}\quad(0\le\ell<m),
\]

and the canonical data below require \(\kappa(G)=2\). Thus every state in
\(\mathcal I\) has curling number two or three, and the \(\kappa=1\) sentinel
cannot affect (G2CS) in that application. The general core permits arbitrary
positive-integer \(U\); even there, the sentinel changes no \(\pi(W)\) for any
state with \(\kappa(W)\ge2\). Any state with \(\kappa(W)=1\) in such a general
instance uses the \(|W|\) sentinel by definition.

## Repaired combinatorial synchronization implications

The original, stronger **Generated Two-Cube Synchronization Lemma** is the
following fully quantified, presently unproved implication.

For every choice of \(L,A,B,T,U,R,q,b,P,j,m,Y\), orbit
\((S_t)\), and index \(t_0\) satisfying all structural hypotheses and the
primitive full-state orbit equalities above, assume also the following
canonical data:

- the two external states have maximal curling number three,
   \[
   \kappa(E)=\kappa(F)=3;
   \]
   hence paired generation at \(\ell=0\) gives
   \[
   R[j]=U[0]=3;
   \]
- the first generated copy of \(U\) ends at
   \[
   \kappa(G)=2,\qquad \pi(G)=q;
   \]
- the standalone word \(R^2T=T(UT)^2\) has no cube suffix, equivalently in
   this setting
   \[
   \kappa(R^2T)=2;
   \]
- \(H\) is the completed \(Y^2\)-square state and has canonical data
   \[
   \kappa(H)=2,\qquad \pi(H)=P;
   \]

The actual pre-completion order of \(\mathcal I\) is already a consequence of
the primitive orbit equalities and \(P-m=b+j>0\); it is not an independent
antecedent.

Then

\[
\boxed{
\max_{W\in\mathcal I}\pi(W)\ge P.
}
\tag{G2CS-\mathcal I}
\]

The standalone no-cube clause is retained in the antecedent rather than
restated informally as "promotion failure." Although \(R^2T\) visibly ends in
the square
\((UT)^2\), that displayed period \(q\) need not be its canonical period.

### Bridge-inclusive target

Keep every structural, actual-generation, and canonical-data antecedent above
unchanged, but evaluate every proper orbit state rather than only the two
\(U\)-windows. The separate bridge-inclusive implication is

\[
\boxed{
\max_{W\in\mathcal J}\pi(W)\ge P.
}
\tag{G2CS-\mathcal J}
\]

Because \(\mathcal I\subseteq\mathcal J\), this is a weaker implication than
(G2CS-\(\mathcal I\)): a period-\(P\) witness in the omitted \(G\)-to-\(F\)
bridge proves only the \(\mathcal J\) version. Introducing \(\mathcal J\)
does not alter the quantifiers or hypotheses of the stronger target, and
(G2CS-\(\mathcal I\)) remains open.

### Strict-record contradiction corollary

Neither combinatorial implication deliberately assumes record minimality.
This keeps each antecedent consistent with its conclusion.

For the strict-record application, add the independent orbit hypothesis that
\(H\) is a completed strict-record square of canonical period \(P\). Precisely,
if

\[
t_H=t_0+P+m,
\]

require

\[
\pi(S_t)<P\qquad(0\le t<t_H),
\]

while \(\pi(H)=P\). Since every \(W\in\mathcal J\), and hence every
\(W\in\mathcal I\), precedes \(H\), strict-record availability gives

\[
\max_{W\in\mathcal J}\pi(W)<P,
\qquad
\max_{W\in\mathcal I}\pi(W)<P.
\]

Either matching synchronization implication contradicts its corresponding
strict-record inequality. Therefore a proof of the weaker
(G2CS-\(\mathcal J\)) is already sufficient to exclude the stated
first-\(3\)-position promotion-failure configuration at a strict record.
This is a corollary of a record-free combinatorial statement, not a
minimality hypothesis smuggled into that statement. It does not prove the
stronger (G2CS-\(\mathcal I\)).

### Fully generated strict-record application specialization

The future bounded extractor tests only the following specialization of the
strict-record application. Let the orbit seed be \(S_0\), let

\[
n_{\mathrm{seed}}=|S_0|,
\qquad
N=|H|=x+3q+b,
\]

and retain the strict-record and all core hypotheses above. Since every orbit
step appends one symbol, \(N=n_{\mathrm{seed}}+t_H\). The terminal
square suffix \(Y^2\), of length \(2P\), occupies

\[
[N-2P,N)
=[x+q-b,x+3q+b).
\]

The seed occupies \([0,n_{\mathrm{seed}})\), so this entire occurrence of
\(Y^2\) is generated exactly when

\[
\boxed{
N-2P=x+q-b\ge n_{\mathrm{seed}}.
}
\tag{FG}
\]

This is the full-generation condition. It is stronger than merely generating
the final copy of \(Y\), which already follows from the primitive orbit
equalities \(G\to H\). In particular, (FG) is a seed-boundary condition, not
the unqualified inequality \(N\ge2P\).

Candidates counted by the bounded extractor must satisfy (FG).
Therefore its antecedent count is a subset of the antecedents allowed by the
general record-free cores; the extractor does not exhaust arbitrary actual
occurrences covered by either core.

## Half-open coordinate audit

Recall \(x=|L|\), and define

\[
e_\ell=x+q+j+\ell,\qquad
f_\ell=x+2q+b+j+\ell.
\]

All coordinates in the table are zero-based and half-open. An empty generated
interval at \(\ell=0\) is written \([a,a)\).

| State | Full-state interval; length/end | Generated append interval in its \(U\)-window | In \(\mathcal I\)? | Known canonical data |
|---|---|---|---|---|
| \(E_\ell\), \(0\le\ell<m\) | \([0,e_\ell)\); \(e_\ell=x+q+j+\ell\) | \([x+q+j,e_\ell)\), containing \(U[0:\ell]\) | included | \(\kappa(E_\ell)=U[\ell]\); at \(\ell=0\), \(\kappa(E)=3\), \(\pi(E)=p\) |
| \(G=E_m\) | \([0,x+2q)\); \(x+2q\) | \([x+q+j,x+2q)\), containing all of \(U\) | included | \(\kappa(G)=2\), \(\pi(G)=q\) |
| \(F_\ell\), \(0\le\ell<m\) | \([0,f_\ell)\); \(f_\ell=x+2q+b+j+\ell\) | \([x+2q+b+j,f_\ell)\), containing \(U[0:\ell]\) | included | \(\kappa(F_\ell)=U[\ell]\); at \(\ell=0\), \(\kappa(F)=3\), \(\pi(F)=r\) |
| \(H=F_m\) | \([0,x+3q+b)\); \(x+3q+b\) | \([x+2q+b+j,x+3q+b)\), containing all of \(U\) | **excluded** | \(\kappa(H)=2\), \(\pi(H)=P\); suffix \(Y^2\) |
| standalone \(R^2T\) | \([0,2q+j)\); \(2q+j\) | none: this is not an actual full-state window | excluded | \(\kappa(R^2T)=2\), no cube suffix; \(\pi(R^2T)\le q\), but need not equal \(q\) |

Put

\[
p=\pi(E),\qquad r=\pi(F).
\]

Because \(\kappa(E)=\kappa(F)=3\), \(p\) and \(r\) are the shortest
maximizing cube periods. Their canonical suffix-cube intervals are exactly

\[
[|E|-3p,|E|)
=[x+q+j-3p,x+q+j),
\]

\[
[|F|-3r,|F|)
=[x+2q+b+j-3r,x+2q+b+j).
\]

They are not arbitrary periods of convenient displayed cubes.

At \(F\), the suffix \(YBT\) has the exact placement

\[
YBT:
[x+q-b,x+2q+b+j),
\]

with the partition

\[
\underbrace{B}_{[x+q-b,x+q)}
\underbrace{R}_{[x+q,x+2q)}
\underbrace{B}_{[x+2q,x+2q+b)}
\underbrace{T}_{[x+2q+b,x+2q+b+j)}.
\]

Appending the second generated copy of \(U\) occupies

\[
[|F|,|H|)
=[x+2q+b+j,x+3q+b),
\]

so the completed suffix

\[
YBTU=Y^2
\]

occupies \([x+q-b,x+3q+b)\), of length \(2P\).

The endpoint displacement is

\[
|F|-|E|=(x+2q+b+j)-(x+q+j)=q+b=P.
\]

The intervening generated block is

\[
UBT=R[j:q]\,B\,R[0:j],
\]

occupying

\[
[|E|,|F|)
=[x+q+j,x+2q+b+j),
\]

with \(U\), \(B\), and \(T\) respectively on

\[
[x+q+j,x+2q),\quad
[x+2q,x+2q+b),\quad
[x+2q+b,x+2q+b+j).
\]

It has length \(P\) and is a conjugate of \(Y=BTU\).

Finally,

\[
R^2T=T(UT)^2,
\]

so its displayed square suffix \((UT)^2\) occupies
\([j,2q+j)\). This proves only a square lower bound; the no-cube hypothesis
is what fixes \(\kappa(R^2T)=2\).

## Adversarial audit checklist

- [ ] **Generated versus preloaded:** verify both \(U\)-copies through the
  full-state equalities and verify that \(UBT\) is appended on the actual
  orbit; never infer this from a displayed \(R^2\).
- [ ] **Full context:** compute \(\kappa(E_\ell)\) and
  \(\kappa(F_\ell)\) in their full \(L\)-contexts; do not substitute
  standalone \(R^2T\).
- [ ] **Maximal versus lower-bound power:** each asserted curling number is
  an equality, not merely \(\kappa(W)\ge2\) or \(\kappa(W)\ge3\).
- [ ] **Canonical-period branch:** compute \(\kappa(W)\) first; use the
  \(|W|\) sentinel when \(\kappa(W)=1\), and minimize over all suffix witnesses
  at the maximal exponent only when \(\kappa(W)\ge2\).
- [ ] **Half-open endpoints:** recheck every interval as \([a,b)\), especially
  the two cube starts and the \(YBT\), \(U\), and \(UBT\) boundaries.
- [ ] **Proper pre-completion set:** include \(G=E_m\), include only
  \(F_\ell\) with \(\ell<m\), and exclude \(H=F_m\).
- [ ] **Target family:** distinguish the stronger two-window family
  \(\mathcal I\) from the natural full family \(\mathcal J\); a bridge witness
  proves only (G2CS-\(\mathcal J\)).
- [ ] **Bridge endpoints:** in \(\mathcal J\), identify
  \(G=E_m=K_0\) and \(F=K_s=F_0\) once, retain every proper bridge state, and
  still exclude \(H\).
- [ ] **Duplicate states:** treat \(\mathcal I\) as a set; multiplicity must
  not affect its maximum.
- [ ] **Strict-record availability:** use \(\pi(S_t)<P\) for earlier states
  only in the corollary, after independently establishing that \(H\) is a
  strict record.
- [ ] **Fully generated specialization:** count an extractor candidate only
  when the terminal \(Y^2\) start satisfies
  \(N-2P=x+q-b\ge n_{\mathrm{seed}}\); label such counts as specialization
  counts, not general-core counts.
- [ ] **Canonical cube periods:** verify that \(p=\pi(E)\) and \(r=\pi(F)\)
  are the shortest periods of maximizing cube suffixes, not selected cube
  periods.
- [ ] **Terminal non-tautology:** confirm that the maximum ranges over
  \(\mathcal I\) and therefore cannot be satisfied merely by the known
  terminal value \(\pi(H)=P\).
