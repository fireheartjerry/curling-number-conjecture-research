# Generated Two-Cube cell ledger

This ledger audits the three later-cube placements in the repaired Generated
Two-Cube Synchronization implication (G2CS). Its statuses are deliberately
local:

| Cell | Status | Meaning |
|---|---|---|
| A | `OPEN` | No claim is made here. |
| B | `PROVED-NL` | The Cell B branch contradicts the repaired hypotheses and the negation of the G2CS conclusion. This is a natural-language proof, not a formal proof. |
| C | `OPEN` | No claim is made here. |

In particular, closing Cell B does **not** prove (G2CS) and does not prove the
Curling Number Conjecture.

## Cell B — `PROVED-NL`

### 1. Inputs, intervals, and the Fine--Wilf threshold

Assume the repaired G2CS antecedent and negate its conclusion:

\[
\max_{W\in\mathcal I}\pi(W)<P.
\tag{B.1}
\]

Retain the statement's notation

\[
R=AB=TU,\quad q=|R|,\quad b=|B|,\quad
P=q+b,\quad 0<b<q,
\]

and put

\[
r=\pi(F),\qquad s=b+j=|BT|,\qquad e=\gcd(r,P).
\]

Since \(F=F_0\in\mathcal I\), (B.1) gives \(r<P\). Also,
\(\kappa(F)=3\), so the canonical \(r\)-cube at \(F\) is the exact suffix
interval

\[
C=[n-3r,n),\qquad n=|F|=x+2q+b+j.
\]

Cell B is the external case with

\[
n-3r<n-(P+s),\qquad q<r<P.
\tag{B.2}
\]

The word

\[
W=YBT
\]

is the exact suffix

\[
W=F[n-(P+s):n]
  =F[x+q-b:x+2q+b+j]
\]

of length \(P+s\). The strict external inequality in (B.2) places all of
\(W\) inside \(C\), so \(W\) has period \(r\). It also has period \(P\):
\(W=Y(BT)\), while \(Y=BTU\), and therefore the two half-open slices

\[
W[0:s]=BT=W[P:P+s]
\]

agree.

Fine--Wilf says that a word with periods \(r\) and \(P\) has period
\(e=\gcd(r,P)\) once its length is at least

\[
r+P-e.
\]

Thus, if

\[
P+s\ge r+P-e,
\]

then \(W\), and hence its prefix \(Y=W[0:P]\), has period \(e\).
Here \(e\mid P\) and \(e<P\), because \(e\le r<P\). Consequently, for
\(D=Y[0:e]\),

\[
Y=D^{P/e}.
\]

The terminal state \(H\) ends in

\[
Y^2=D^{2P/e},
\]

so \(\kappa(H)\ge 2P/e\ge4\), contradicting \(\kappa(H)=2\). The canonical
datum \((\kappa(H),\pi(H))=(2,P)\) is therefore impossible already in its
first coordinate; no inference from a lower-power display to \(\pi(H)\) is
needed.

Therefore the Fine--Wilf threshold cannot be attained:

\[
P+s<r+P-e,\qquad
s<r-e,\qquad
\boxed{s\le r-e-1<r}.
\tag{B.3}
\]

The last inequality includes the equality endpoint audit: Fine--Wilf applies
at equality, so the surviving side is strict before integrality changes it
to \(s\le r-e-1\).

### 2. Delete \(BT\): an \(r\)-square already ends at \(G\)

Let

\[
g=|G|=n-s.
\]

Deleting the final \(BT=F[g:n]\), whose length \(s\) is strictly less than
\(r\), leaves the part

\[
C\cap[0,g)=[n-3r,g)
\]

of the \(r\)-periodic cube. Its length obeys

\[
3r-s\ge 2r+e+1>2r.
\]

In particular, the interval

\[
[g-2r,g)
\]

lies inside \(C\). Put

\[
Z=F[g-r:g].
\]

Period \(r\) on \(C\) gives

\[
F[g-2r:g-r]=F[g-r:g]=Z,
\]

so \(G=F[0:g]\) has the suffix square \(Z^2\) on \([g-2r,g)\).
Because \(\kappa(G)=2\) and \(\pi(G)=q\), this maximizing square witness
implies \(q\le r\). Cell B is the strict branch \(q<r<P\).

Normalize

\[
c=r-q,\qquad \delta=b-c=P-r.
\tag{B.4}
\]

The inequalities \(q<r<P=q+b\) and \(b<q\) give

\[
0<c<b<q,\qquad \delta>0,\qquad r<2q.
\tag{B.5}
\]

### 3. The square at \(G\) forces period \(c\) on \(R\)

The last \(q\) letters of \(Z=F[g-r:g]\) are the final copy of \(R\) in
\(G=LR^2\). Its preceding \(c=r-q\) letters are the suffix

\[
K=R[q-c:q]
\]

of the preceding copy of \(R\). Hence

\[
Z=KR,\qquad |K|=c.
\tag{B.6}
\]

The square \(Z^2=(KR)(KR)\) occupies \([g-2r,g)\). Its final \(2q\) letters
start at relative offset

\[
(g-2q)-(g-2r)=2(r-q)=2c.
\]

Since \(0<c<q\), an exact half-open slice calculation gives

\[
Z^2[2c:2r]=R[c:q]\,K\,R.
\]

But \(G\)'s final \(2q\) letters are \(R^2\). Comparing these equal-length
suffixes and then their first \(q\) letters yields

\[
R[c:q]\,K\,R=R\,R,
\qquad
\boxed{R[c:q]\,K=R}.
\tag{B.7}
\]

In particular,

\[
R[0:q-c]=R[c:q],
\]

so \(R\) has period \(c\). Notice that (B.7) was derived directly from the
two suffix intervals; it is not an inherited normal form used as an axiom.

### 4. The period satisfies \(c>q/2\)

First, \(R\) has no square suffix. If \(R\) ended in \(V^2\), with
\(|V|=t>0\), then \(t\le q/2<q\) and the same square would end at \(G\).
Because \(\kappa(G)=2\), it would be a maximizing square witness and would
force

\[
\pi(G)\le t<q,
\]

contrary to \(\pi(G)=q\).

If the period \(c\) from (B.7) satisfied \(c\le q/2\), then the two
half-open suffix blocks

\[
R[q-2c:q-c]
\quad\text{and}\quad
R[q-c:q]
\]

would agree by period \(c\). That would be a \(c\)-square suffix of \(R\),
which was just excluded. Therefore

\[
\boxed{c>q/2}.
\tag{B.8}
\]

### 5. The generated continuation forces period \(\delta\) on \(B\)

The interval \(F[g:n]=BT\) is the next \(s<r\) letters in the same
\(r\)-periodic cube that supplied the block \(Z=F[g-r:g]\). Therefore

\[
BT=Z[0:s]=(KR)[0:s].
\tag{B.9}
\]

Since \(b=c+\delta\), the first \(b\) letters in (B.9) give

\[
\boxed{B=K\,R[0:\delta]}.
\tag{B.10}
\]

On the other hand, \(B=R[q-b:q]\) and \(c<b\), so

\[
K=R[q-c:q]=B[b-c:b]=B[\delta:b].
\tag{B.11}
\]

Equation (B.10) says \(B[0:c]=K\); combining it with (B.11) gives

\[
B[0:c]=B[\delta:b].
\]

Because \(c=b-\delta\), this is exactly the half-open period condition

\[
\boxed{B[0:b-\delta]=B[\delta:b]}.
\tag{B.12}
\]

Thus \(B\) has period \(\delta\).

For completeness, (B.3), after substituting \(s=c+\delta+j\) and
\(r=q+c\), first gives

\[
\delta+j\le q-e-1.
\]

Thus the relevant slice stays strictly inside \(R\), and the unused remainder
of (B.9) gives

\[
R[0:j]=T=R[\delta:\delta+j].
\]

These familiar normalized relations are consequences of the audited
intervals; neither is needed for the final contradiction.

### 6. Contradiction inside \(G\)

From \(b<q\) and (B.8),

\[
0<\delta=b-c<q-c<c.
\tag{B.13}
\]

Consequently,

\[
|B|=b=c+\delta>2\delta.
\]

The period-\(\delta\) identity (B.12) applies in particular to the two final
blocks

\[
B[b-2\delta:b-\delta]
=B[b-\delta:b].
\]

So \(B\) ends in a \(\delta\)-square. Since \(G=LR^2\) ends in
\(B=R[q-b:q]\), the same \(\delta\)-square ends at \(G\). Using
\(\kappa(G)=2\) once more,

\[
\pi(G)\le\delta<q,
\]

contradicting \(\pi(G)=q\).

This closes Cell B under the repaired G2CS antecedent and (B.1). The proof
does not use the early cube at \(E\), the standalone failure
\(\kappa(R^2T)=2\), strict-record minimality, or an inherited provisional
normal form. Those clauses remain relevant to the complete theorem, but they
are unnecessary once the later canonical cube enters external Cell B.

### Bounded executable index certificate

`tests/test_generated_two_cube_cells.py` independently exhausts every binary
word \(R\) for

\[
3\le q\le12,\qquad q/2<c<b<q,
\]

and every integer parameter pair in that range. It retains exactly the cases
where \(R\) has period \(c\) and

\[
B=R[q-b:q]=R[q-c:q]\,R[0:\delta].
\]

There are 84 retained word-parameter cases. In every one, the test checks the
exact slices in (B.12), verifies period \(\delta\) on \(B\), and verifies the
terminal \(\delta\)-square. The cap and survivor count are assertions, so the
certificate cannot pass vacuously.

This bounded computation is only an index sanity check. It does not supply
the Fine--Wilf argument, does not enumerate the full G2CS orbit hypotheses,
and is not the proof of Cell B.
