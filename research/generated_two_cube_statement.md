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

Define the canonical period

\[
\pi(W)=\min\{|X|: W=SX^{\kappa(W)}
  \text{ for some word }S\text{ and nonempty word }X\}.
\]

Thus \(\pi(W)\) is the least period among suffixes
\(X^{\kappa(W)}\): it is the shortest maximizing period, never merely the
period of a displayed lower power.

For a word \(V\), the slice \(V[a:b]\) uses zero-based, half-open
coordinates. A curling-number orbit is a sequence of full states
\((S_t)_{t\ge0}\) satisfying

\[
S_{t+1}=S_t\,\kappa(S_t),
\]

where every \(S_t\) is nonempty and \(\kappa(S_t)\) is appended as the next
symbol.

## Structural data and actual states

Let \(L,A,B,T,U\) be words such that

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

The generation hypothesis is not shorthand for a static word equation.
There must be a curling-number orbit \((S_t)\) and an index \(n\) such that

\[
E_\ell=S_{n+\ell}\quad(0\le\ell\le m),
\]

\[
F_\ell=S_{n+P+\ell}\quad(0\le\ell\le m).
\]

At every proper prefix of the two copies of \(U\), the next generated symbol
is the corresponding symbol of \(U\):

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
before the completion state \(H=S_{n+P+m}\). Also

\[
G=S_{n+m},\qquad H=S_{n+m+P},
\]

so the full bridge root \(Y=BTU\) is actually generated from \(G\) to \(H\).

## Repaired combinatorial synchronization implication

The **Generated Two-Cube Synchronization Lemma** is the following fully
quantified, presently unproved implication.

For every choice of \(L,A,B,T,U,R,q,b,P,j,m,Y\), orbit
\((S_t)\), and index \(n\) satisfying all structural and actual-generation
hypotheses above, assume also:

1. the two external states have maximal curling number three,
   \[
   \kappa(E)=\kappa(F)=3;
   \]
   hence paired generation at \(\ell=0\) gives
   \[
   R[j]=U[0]=3;
   \]
2. the first generated copy of \(U\) ends at
   \[
   \kappa(G)=2,\qquad \pi(G)=q;
   \]
3. the standalone word \(R^2T=T(UT)^2\) has no cube suffix, equivalently in
   this setting
   \[
   \kappa(R^2T)=2;
   \]
4. \(H\) is the completed \(Y^2\)-square state and has canonical data
   \[
   \kappa(H)=2,\qquad \pi(H)=P;
   \]
5. every state in \(\mathcal I\) is an actual state strictly preceding that
   completion.

Then

\[
\boxed{
\max_{W\in\mathcal I}\pi(W)\ge P.
}
\tag{G2CS}
\]

Hypothesis 3 is retained in the antecedent rather than restated informally as
"promotion failure." Although \(R^2T\) visibly ends in the square
\((UT)^2\), that displayed period \(q\) need not be its canonical period.

### Strict-record contradiction corollary

The combinatorial implication (G2CS) deliberately does **not** assume record
minimality. This keeps its antecedent consistent with its conclusion.

For the strict-record application, add the independent orbit hypothesis that
\(H\) is a completed strict-record square of canonical period \(P\). Precisely,
if \(N=n+P+m\), require

\[
\pi(S_t)<P\qquad(0\le t<N),
\]

while \(\pi(H)=P\). Since every \(W\in\mathcal I\) precedes \(H\), strict-record
availability gives

\[
\max_{W\in\mathcal I}\pi(W)<P.
\]

Once (G2CS) is proved, the two inequalities contradict each other. Therefore
the stated first-\(3\)-position promotion-failure configuration cannot occur
at such a strict record. This is a corollary of the open combinatorial lemma,
not a hypothesis smuggled into its proof.

## Half-open coordinate audit

Let \(x=|L|\), and define

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
- [ ] **Shortest maximizing period:** compute \(\pi(W)\) only after finding
  \(\kappa(W)\), and minimize over all suffix witnesses at that maximal
  exponent.
- [ ] **Half-open endpoints:** recheck every interval as \([a,b)\), especially
  the two cube starts and the \(YBT\), \(U\), and \(UBT\) boundaries.
- [ ] **Proper pre-completion set:** include \(G=E_m\), include only
  \(F_\ell\) with \(\ell<m\), and exclude \(H=F_m\).
- [ ] **Duplicate states:** treat \(\mathcal I\) as a set; multiplicity must
  not affect its maximum.
- [ ] **Strict-record availability:** use \(\pi(S_t)<P\) for earlier states
  only in the corollary, after independently establishing that \(H\) is a
  strict record.
- [ ] **Canonical cube periods:** verify that \(p=\pi(E)\) and \(r=\pi(F)\)
  are the shortest periods of maximizing cube suffixes, not selected cube
  periods.
- [ ] **Terminal non-tautology:** confirm that the maximum ranges over
  \(\mathcal I\) and therefore cannot be satisfied merely by the known
  terminal value \(\pi(H)=P\).
