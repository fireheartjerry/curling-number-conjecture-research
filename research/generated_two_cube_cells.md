# Generated Two-Cube cell ledger

This ledger audits the three later-cube placements in the repaired Generated
Two-Cube Synchronization implications. The stronger
(G2CS-\(\mathcal I\)) evaluates only the two generated \(U\)-windows; the
weaker (G2CS-\(\mathcal J\)) evaluates every proper state before \(H\).
Statuses are deliberately local:

| Cell | (G2CS-\(\mathcal I\)) | (G2CS-\(\mathcal J\)) / strict-record route | Meaning |
|---|---|---|---|
| A | `OPEN` | `BRIDGE-PROVED-NL` | A period-\(P\) witness is forced at \(E\) or at the genuine bridge state \(S_{t_0+q}\). The latter is outside \(\mathcal I\). |
| B | `PROVED-NL` | `PROVED-NL` | The Cell B branch contradicts even the negation over \(\mathcal I\). |
| C | `OPEN` | `OPEN` | No claim is made here. |

These are natural-language proofs, not formal proofs. In particular, closing
Cell A for the bridge-inclusive target and Cell B for both targets does
**not** close Cell C, prove the stronger (G2CS-\(\mathcal I\)), complete
bridge promotion, or prove the Curling Number Conjecture.

## Cell A — `BRIDGE-PROVED-NL`; I-only status `OPEN`

### 1. Border--conjugate short-period lemma

We first make the load-bearing auxiliary lemma self-contained.

**Lemma.** Let \(W\) be a word of length \(N\). Suppose:

1. \(W\) has a border \(B\) of length \(b\), with
   \[
   0<b<N/2;
   \]
2. \(W=TU\), where \(j=|T|<N-b\);
3. the conjugate \(C=UT\) has a period \(t\), with
   \[
   0<t<b.
   \]

Then \(W\) has a square suffix.

We use the following period-extension fact. Let a word \(V\), of length
\(v_N\), have period \(m\), and let its suffix
\[
S=V[a:v_N]
\]
have period \(d\), where \(d\mid m\) and \(|S|\ge m+d\). Then \(V\) has
period \(d\).

Indeed, fix the full required range
\[
0\le z<v_N-d.
\]
If \(z\ge a\), both \(z\) and \(z+d\) lie in \(S\), so its period \(d\)
gives \(V[z]=V[z+d]\). If \(z<a\), choose the least integer \(k\ge0\)
with \(z+km\ge a\). Minimality gives
\[
z+km<a+m.
\]
The length bound on \(S\) puts both \(z+km\) and \(z+d+km\) in \(S\).
Repeated use of period \(m\), followed by period \(d\) on \(S\), gives
\[
V[z]=V[z+km]=V[z+d+km]=V[z+d].
\]
This covers every \(z<v_N-d\). Reversal gives the corresponding prefix
version.

Return to the lemma. Put
\[
a=N-b,
\]
so the disjoint border occurrences give \(W=BMB\). There are four exhaustive
cases.

#### Case 1: \(j\ge b\)

The prefix \(T\) begins with \(B\). Since \(j<N-b=a\), the suffix \(U\)
still contains and ends with the terminal \(B\). Thus \(C=UT\) contains
\(B^2\) across the \(U\mid T\) cut. This factor has periods \(t\) and
\(b\). Its length \(2b\) meets the Fine--Wilf threshold for those periods,
so it has period
\[
d_1=\gcd(t,b)<b.
\]
The final copy of \(B\) has period \(d_1\). Since \(d_1\mid b\) and
\(d_1<b\), we have \(2d_1\le b\), and the last \(2d_1\) letters of \(B\)
form a \(d_1\)-square suffix of \(W\).

#### Case 2: \(t\le j<b\)

Now \(T=B[0:j]\). Hence \(C\) ends in \(BT\), a word of length
\(b+j\) with periods \(t\) and \(b\). Since
\[
b+j\ge b+t,
\]
Fine--Wilf gives period \(d_2=\gcd(t,b)\) on \(BT\), and therefore on its
prefix \(B\). Again \(d_2\mid b\), \(d_2<b\), and the terminal \(B\)
contains a \(d_2\)-square suffix.

#### Case 3: \(j<t\) and \(|U|\ge2t\)

The word \(U\) is a prefix of the \(t\)-periodic word \(C\), so its final
\(2t\) letters form a square. Since \(U\) is the suffix of \(W=TU\), this
is already a square suffix of \(W\).

#### Case 4: \(j<t\) and \(|U|<2t\)

Write
\[
h=|U|=N-j,\qquad e=b-t,\qquad
\rho_0=N-2t,\qquad v=\rho_0-e.
\]
The inequalities \(b<N/2\), \(|U|<2t\), and \(j<t\) give
\[
0<2e<\rho_0<j<t,\qquad v>e>0,
\qquad a=t+v.
\tag{A.1}
\]

Let \(\omega\) be the bi-infinite \(t\)-periodic extension of \(C\), and
define
\[
c_i=\omega(h-b+i).
\]
The block \(c_0\cdots c_{b-1}=C[h-b:h]\) is exactly the terminal occurrence
of \(B\).

For \(0\le i<j\), the border equality reads the matching prefix occurrence
through the \(T\)-part of \(C\):
\[
c_i=\omega(h+i).
\]
On the other hand, the definition of \(c_{i+e}\) and \(b=t+e\) give
\[
c_{i+e}=\omega(h-b+i+e)=\omega(h-t+i).
\]
These two \(\omega\)-positions differ by \(t\), so
\[
c_i=c_{i+e}.
\]
Thus the half-open interval
\[
I=[0,j+e)
\]
has period \(e\). For \(j\le i<b\), the border equality instead reads the
matching prefix occurrence through the \(U\)-part of \(C\):
\[
c_i=\omega(i-j).
\]
Using \(h-b=t+v-j\), which is equivalent to \(a=t+v\), the definition gives
\[
c_{i-v}
=\omega(h-b+i-v)
=\omega(t-j+i).
\]
Again the two positions differ by \(t\), so
\[
c_i=c_{i-v}.
\]
Thus
\[
J_0=[j-v,b)
\]
has period \(v\).

Their overlap is exactly
\[
O=I\cap J_0=[j-v,j+e),
\qquad |O|=e+v=\rho_0.
\]
Put \(g_1=\gcd(e,v)\). The exact Fine--Wilf threshold is met:
\[
|O|=e+v\ge e+v-g_1.
\]
Therefore \(O\) has period \(g_1\).
The overlap is a suffix of \(I\) of length
\[
e+v\ge e+g_1,
\]
so the period-extension fact propagates \(g_1\mid e\) through \(I\).
By the reversed form, since
\[
e+v\ge v+g_1,
\]
it also propagates \(g_1\mid v\) through \(J_0\).

This propagation on the two pieces still needs an explicit glue step.
The overlap has length \(e+v\ge g_1\), so it contains a representative of
every residue class modulo \(g_1\). The two \(g_1\)-periodic pieces agree on
that common full residue block. Therefore their periodic residue values
agree throughout the union
\[
I\cup J_0=[0,b),
\]
and \(B\) has period \(g_1\).

The same occurrence \(B=C[h-b:h]\) also has period \(t\). Put
\[
g=\gcd(t,g_1).
\]
Because \(g_1\mid e\), its length \(b=t+e\) meets the Fine--Wilf threshold:
\[
b=t+e\ge t+g_1\ge t+g_1-g.
\]
Hence \(B\) has period \(g\). Moreover
\[
g\mid t,\qquad g\mid g_1\mid e,\qquad
g\mid b=t+e,\qquad g<b.
\]
The positive proper divisor relation \(g\mid b\), \(g<b\) explicitly gives
\(2g\le b\). The final two length-\(g\) blocks of \(B\) are equal, so they
form the required square suffix of \(W\). This finishes all four cases.

### 2. Exact Cell A normal form

Assume all antecedents of the repaired synchronization statement and enter
the external later-cube branch with
\[
r=\pi(F)=q.
\]
Put
\[
s=b+j=|BT|,\qquad n=|F|,\qquad
\gamma=\gcd(q,P)=\gcd(q,b).
\]
The canonical \(q\)-cube at \(F\) occupies
\[
[n-3q,n),
\]
while
\[
YBT=F[n-(P+s):n]
\]
has length \(P+s\). Externality says that the first interval begins strictly
before the second, so all of \(YBT\) is \(q\)-periodic. It is also
\(P\)-periodic because its prefix and suffix of length \(s\) are both
\(BT\).

If the Fine--Wilf threshold were met, including at equality,
\[
P+s\ge q+P-\gamma,
\]
then \(YBT\), and hence its length-\(P\) prefix \(Y\), would have period
\(\gamma\). Since \(\gamma\mid P\) and \(\gamma<P\), the terminal state
\(H\), which ends in \(Y^2\), would end in at least four copies of a
length-\(\gamma\) word. This contradicts \(\kappa(H)=2\). Therefore
\[
\boxed{s\le q-\gamma-1<q.}
\tag{A.2}
\]
In particular,
\[
\boxed{j<q-b.}
\tag{A.3}
\]

Let \(g_N=|G|=n-s\). Both half-open intervals
\[
[g_N,g_N+s)
\quad\text{and}\quad
[g_N-q,g_N-q+s)
\]
lie in the \(q\)-cube, and period \(q\) identifies them. The first is the
generated block \(BT\); the second is the length-\(s\) prefix of the final
copy of \(R\) in \(G\). Hence
\[
\boxed{BT=R[0:s].}
\tag{A.4}
\]
Its first \(b\) letters and the structural suffix \(R[q-b:q]=B\) show that
\(B\) is a border of \(R\). Its next \(j\) letters give
\[
\boxed{R[0:j]=R[b:b+j].}
\tag{A.5}
\]

The border makes \(q-b\) a period of \(R\). If \(b\ge q/2\), then
\(q-b\le q/2\), so \(R\) ends in a \((q-b)\)-square. The same square ends
at \(G=LR^2\), contradicting \(\kappa(G)=2\) and its shortest maximizing
period \(\pi(G)=q\). Thus
\[
\boxed{b<q/2.}
\tag{A.6}
\]

### 3. The genuine bridge state at time \(t_0+q\)

The actual outputs from \(E\) to \(G\) are \(U\). On the bridge
\[
K_h=S_{t_0+m+h}=LR^2(BT)[0:h],
\qquad 0\le h\le s.
\]
Equation (A.4) gives
\[
(BT)[0:j]=R[0:j]=T.
\]
Therefore
\[
\boxed{
K:=K_j=S_{t_0+q}=LR^2T,
}
\tag{A.7}
\]
and the first \(q\) output labels after \(E\) are exactly
\[
UT.
\]

The next label after \(K\) is
\[
(BT)[j]=R[j]=U[0]=3,
\]
where the final equality is the paired-generation label at \(E=E_0\).
Consequently
\[
\kappa(K)=3.
\tag{A.8}
\]
If \(j=0\), then \(K=K_0=G\), and (A.8) contradicts
\(\kappa(G)=2\) immediately. Hence every surviving Cell A instance has
\(j>0\), and its exact chronology is
\[
t_G=t_0+m<t_K=t_0+q<t_F=t_0+P.
\tag{A.9}
\]
Thus \(K\) is a proper \(G\)-to-\(F\) bridge state in
\(\mathcal J\setminus\mathcal I\).

### 4. The bridge cube must have period \(q\)

We prove the sharper Cell A proposition
\[
\boxed{
\max\{\pi(E),\pi(S_{t_0+q})\}\ge P.
}
\tag{A.10}
\]
Suppose for contradiction that
\[
p=\pi(E)<P,\qquad \rho=\pi(K)<P.
\tag{A.11}
\]

The canonical \(\rho\)-cube at \(K\) cannot lie wholly in its suffix
\[
R^2T,
\qquad |R^2T|=2q+j,
\]
because the standalone hypothesis says \(\kappa(R^2T)=2\). Hence
\[
\boxed{3\rho>2q+j.}
\tag{A.12}
\]

Equation (A.4) also says that deleting the final \(b\) letters of \(F\)
leaves \(K\). Deleting those letters from the canonical \(q\)-cube at \(F\)
therefore leaves a \(q\)-periodic suffix of \(K\) of length
\[
3q-b.
\]
Its overlap with the canonical \(\rho\)-cube at \(K\) has length
\[
M=\min(3\rho,3q-b)
\]
and periods \(\rho,q\). Put
\[
d=\gcd(\rho,q).
\]
Both terms in the minimum meet the Fine--Wilf threshold. For the first,
(A.12) implies \(2\rho>q-d\), and hence
\[
3\rho>\rho+q-d.
\]
For the second, \(\rho<P=q+b\) and (A.6) give
\[
3q-b-(\rho+q-d)
=2q-b-\rho+d
>q-2b+d>0.
\]
Thus
\[
M\ge\rho+q-d,
\]
and the overlap has period \(d\).

If \(\rho\ne q\), then \(d<\rho\): otherwise
\(\rho\mid q\), so \(q\ge2\rho\), contradicting
\(3\rho>2q+j\). Also \(d<q\): otherwise \(q\mid\rho\), but
\[
0<\rho<P=q+b<3q/2
\]
leaves \(q\) as the only positive multiple of \(q\), contrary to
\(\rho\ne q\). Hence
\[
\rho\ge2d,\qquad q\ge2d.
\]
It follows that
\[
3\rho\ge6d,\qquad
3q-b>\frac52q\ge5d,
\]
so \(M\ge4d\). The common suffix then ends in four copies of a
length-\(d\) block, contradicting \(\kappa(K)=3\). We conclude
\[
\boxed{\rho=q.}
\tag{A.13}
\]

### 5. The early cube creates a forbidden short conjugate period

Put
\[
C=UT,\qquad |C|=q.
\]
The identities
\[
R^2T=T(UT)^2=TC^2,\qquad K=EC
\]
and (A.13) show that \(K\) ends in \(C^3\) and \(E\) ends in \(C^2\).

If \(3p\le2q\), the canonical \(p\)-cube at \(E\) lies wholly in that
terminal \(C^2\). The same \(C^2\) is the suffix of the standalone word
\(R^2T=TC^2\), contradicting \(\kappa(R^2T)=2\). Therefore
\[
3p>2q.
\tag{A.14}
\]
If \(p=q\), then \(E\) ends in \(C^3\), and the generated next block
\(C\) makes \(K\) end in \(C^4\), contradicting \(\kappa(K)=3\).
Thus \(p\ne q\).

The word \(C^2\) lies inside the canonical \(p\)-cube and has periods
\(p,q\). Let \(e_0=\gcd(p,q)\). If
\[
2q\ge p+q-e_0,
\]
Fine--Wilf would give period \(e_0\) on \(C^2\). Here \(e_0<q\), because
\(p\ne q\) and \(p<P<3q/2\). Since \(e_0\mid q\), the suffix \(C^2\)
would then contain at least four consecutive length-\(e_0\) blocks,
contradicting \(\kappa(E)=3\). Hence the threshold fails:
\[
\boxed{p>q+e_0.}
\tag{A.15}
\]

Set
\[
t=p-q.
\]
Equations (A.11) and (A.15) give
\[
\boxed{0<t<b.}
\tag{A.16}
\]
Moreover, period \(p=q+t\) on \(C^2\) says, for every
\(0\le z<q-t\),
\[
C[z]=C^2[z]=C^2[z+p]=C^2[q+(z+t)]=C[z+t].
\]
Thus \(t\) is a period of \(C=UT\).

Apply the Border--conjugate lemma with
\[
W=R=TU,\qquad N=q.
\]
Equations (A.3), (A.4)--(A.6), and (A.16) supply every hypothesis:
\(B\) is a border with \(0<b<q/2\), \(j<q-b\), and \(UT\) has a
period \(0<t<b\). The lemma forces a square suffix of \(R\). That square
also ends at \(G=LR^2\), so \(\kappa(G)=2\) makes it a maximizing witness
of period strictly below \(q\). This contradicts \(\pi(G)=q\).

The contradiction proves (A.10). Since \(E\in\mathcal I\) but the alternative
witness \(K=S_{t_0+q}\) lies only in the bridge part of \(\mathcal J\), this
closes Cell A for (G2CS-\(\mathcal J\)) and for the strict-record
application, while deliberately leaving the stronger
(G2CS-\(\mathcal I\)) Cell A branch open.

### Bounded executable index certificate

`tests/test_border_conjugate.py` independently checks the lemma's literal
hypotheses. For every binary \(R\) through length \(15\), and every
\((b,j,t)\) satisfying
\[
0<b<|R|/2,\qquad j<|R|-b,\qquad 0<t<b,
\]
it tests the border, conjugate-period, and square-suffix predicates directly.
It retains exactly \(1776\) tuples and finds zero failures. Repeating the
same audit over the ternary alphabet through length \(11\) retains exactly
\(690\) tuples and finds zero failures. The caps and both nonzero counts are
assertions.

The same test file pins the ordered \(\mathcal J\) decomposition, including
the \(j=0\) nonempty-bridge boundary, normalization of mutable states,
deduplication of \(G,F\), exclusion of \(H\), and fail-closed endpoint
overlap checks. These computations are index and implementation audits; they
do not replace the proof above.

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

## Cell C — `OPEN`; equality-first residual audit

Cell C is the internal placement of the later canonical \(r\)-cube. The
following reduction and bounded search sharpen the branch but do not prove
either synchronization target.

Fix either target and negate its conclusion. Since
\(F=F_0\in\mathcal I\subseteq\mathcal J\), the corresponding negation gives

\[
\boxed{r=\pi(F)<P.}
\]

If \(r\ge P\), then \(F\) itself already witnesses both conclusions, so that
case is outside the survivor residual considered below.

### 1. Exact internal coordinates

Work relative to the suffix

\[
V=YBT=BRBT
\]

of \(F\). Put \(s=b+j\) and \(N=|V|=P+s\). The three copies of the
canonical \(r\)-root occupy

\[
[\alpha,\beta),\quad[\beta,\gamma),\quad[\gamma,N),
\]

where

\[
\alpha=N-3r,\qquad\beta=N-2r,\qquad\gamma=N-r.
\tag{C.1}
\]

Cell C is exactly \(\alpha\ge0\). The copied-block cuts are

\[
Y\mid B=P,\qquad B\mid T=D=P+b=N-j.
\tag{C.2}
\]

Thus there is no ambiguous "contained/crossing" prose partition: every case
is determined by the order of the five half-open coordinates in (C.1)--(C.2).

The word \(V\) has period \(P\), because its length-\(s\) prefix and suffix
are both \(BT\). Let

\[
Z=V[\alpha:N]
\]

be the displayed \(r\)-cube, of length \(3r\), and put
\(e=\gcd(r,P)\). Suppose

\[
3r\ge r+P-e,
\]

so \(P\le2r+e\le3r\). The word \(Z\) has period \(r\) by construction,
and the coordinate comparisons inherited from the \(P\)-periodic word \(V\)
make \(P\) a period of \(Z\). Fine--Wilf therefore gives period \(e\) on
all of \(Z\).

If \(e<r\), then \(e\mid r\) and \(r/e\ge2\). Since \(e\mid3r\), the whole
word \(Z\) is at least six consecutive copies of an \(e\)-block. It is a
suffix of \(F\), contradicting the exact maximal value \(\kappa(F)=3\).

If \(e=r\), then \(r\mid P\). The assumed threshold gives \(P\le3r\), so,
because \(r<P\), one has \(P/r\in\{2,3\}\). The final length-\(P\) factor
of \(V\) lies inside \(Z\), hence is a proper \(r\)-power. But \(V\) is the
length-\((P+s)\) prefix of \(Y^2\), so this final length-\(P\) factor is a
conjugate of \(Y\). A conjugate of a proper power is a power of the conjugate
root. Thus \(Y\) is a proper power, and the suffix \(Y^2\) of \(H\) has
exponent at least four, contradicting \(\kappa(H)=2\).

Both cases are impossible. Therefore \(2r<P-e\), which over the integers is
the strict internal bound

\[
\boxed{2r\le P-\gcd(r,P)-1}.
\tag{C.3}
\]

The standalone no-cube clause forces \(s<3r\): otherwise the internal cube
lies wholly in the common terminal block \(BT\). Equation (C.3) and
\(P<2q\) give \(r<q\). If \(s\le r\), deleting the \(s\)-letter \(BT\)
append from the \(r\)-cube at \(F\) leaves an \(r\)-square at \(G\), forcing
\(\pi(G)\le r<q\). Consequently every surviving integer residual satisfies

\[
\boxed{r<s<3r}.
\tag{C.4}
\]

Writing \(e=\gcd(r,P)\), (C.3)--(C.4) also give

\[
\alpha=(P-2r)+(s-r)\ge e+2.
\]

The exhaustive cut orders are therefore

\[
\begin{array}{ll}
r<s<2r:&\alpha<\beta<P<\gamma<N,\\
s=2r:&\alpha<\beta=P<\gamma<N,\\
2r<s<3r:&\alpha<P<\beta<\gamma<N,
\end{array}
\tag{C.5}
\]

and

\[
\begin{array}{ll}
j<r:&\gamma<D\le N,\\
j=r:&D=\gamma,\\
r<j<2r:&\beta<D<\gamma,\\
j=2r:&D=\beta,\\
2r<j<3r:&\alpha<D<\beta.
\end{array}
\tag{C.6}
\]

These include every equality boundary. The coordinate table by itself allows
\(j=0\), with \(D=N\), but the complete canonical data eliminate that
endpoint below.

### 2. Two universal strict inequalities

The copied block

\[
B=V[P:P+b]
\]

lies wholly inside the internal \(r\)-cube: (C.4) gives
\(\alpha=P+s-3r<P\), while the cube ends at \(N\ge D=P+b\). If \(b\ge2r\),
the final \(2r\) letters of this occurrence of \(B\) would be an
\(r\)-square. Since \(B\) is the suffix of \(R\), the same square would end
at \(G\). But (C.3) gives \(r<q\), so
\((\kappa(G),\pi(G))=(2,q)\) forbids such a square. Hence

\[
\boxed{b<2r.}
\tag{C.7}
\]

Now suppose \(j=0\). Then \(s=b\), so (C.4) gives \(r<b<2r\).
Moreover \(F=LR^2B\) ends in \(B^2\), while it also ends in its canonical
\(r\)-cube. Their common suffix has length

\[
M_0=\min(3r,2b)
\]

and periods \(r,b\). Put \(d_0=\gcd(r,b)\). The Fine--Wilf threshold is met.
Indeed, if \(b\le3r/2\), then

\[
M_0-(r+b-d_0)=b-r+d_0>0,
\]

whereas if \(b>3r/2\), then

\[
M_0-(r+b-d_0)=2r-b+d_0>0.
\]

Thus the common suffix has period \(d_0\). The equality \(d_0=r\) would
make \(b\) a multiple of \(r\) strictly between \(r\) and \(2r\), which is
impossible. Therefore \(d_0<r\). Both \(r\) and \(b\) are then positive
multiples of \(d_0\), so

\[
M_0\ge4d_0.
\]

The common suffix ends in four copies of a length-\(d_0\) block,
contradicting \(\kappa(F)=3\). Consequently

\[
\boxed{j>0.}
\tag{C.8}
\]

This removes the apparent \(j=0\) endpoint in (C.6); no bounded search is
used in either argument.

### 3. The simultaneous boundary \(s=2r,\ j=r\)

The bounded scan lands only on this boundary, so it is worth reducing it
exactly, without claiming that every unbounded Cell C instance lies there.
The two equalities give

\[
b=j=r.
\tag{C.9}
\]

The final \(3r\) letters of \(V=BRBT\) are then \(BBT\). Since they form
the canonical \(r\)-cube, \(T=B\). Thus, for a middle word \(Q\),

\[
\boxed{R=BQB,\qquad T=B,\qquad U=QB.}
\tag{C.10}
\]

The word \(B\) is simultaneously a prefix and suffix of \(R\). If
\(r\ge q/2\), this border would give period \(q-r\le q/2\) on \(R\), and
the final \(2(q-r)\) letters of \(R\) would be a square ending at \(G\) with
period below \(q\). Therefore

\[
\boxed{r<q/2.}
\tag{C.11}
\]

In particular \(Q\ne\epsilon\). Actual generation at \(G\) supplies the
first bridge symbol

\[
B[0]=\kappa(G)=2,
\]

whereas paired generation at \(E\) gives

\[
Q[0]=R[j]=\kappa(E)=3.
\tag{C.12}
\]

Finally, the canonical later cube is literally

\[
\boxed{B^3.}
\tag{C.13}
\]

In particular \(B\) is primitive: otherwise \(B^3\) would display an
exponent greater than three at \(F\).

### 4. The early cube on the simultaneous boundary

Continue to negate either synchronization conclusion, so

\[
p=\pi(E)<P=q+r.
\]

Put

\[
W=RB=BUB,\qquad |W|=P.
\tag{C.14}
\]

The state \(E=LW\) ends in its canonical cube \(X^3\), where \(|X|=p\).
The root \(X\) is primitive: if \(X=K^v\) with \(v\ge2\), then \(E\)
would end in \(K^{3v}\), contradicting \(\kappa(E)=3\).
If \(3p\le P\), that cube would lie wholly in \(W\), which is also a suffix
of the standalone word \(R^2B=R^2T\). This contradicts
\(\kappa(R^2T)=2\). Hence

\[
\boxed{3p>P.}
\tag{C.15}
\]

The whole word \(W\) is consequently contained in the \(p\)-periodic cube,
so it has period \(p\). It also has period \(q\), because its length-\(r\)
prefix and suffix are both \(B\).

The equality \(p=q\) is impossible. In that case the terminal \(q\)-block
of \(E\) would be \(C=UB\), and \(E\) would end in \(C^3\). Appending the
actually generated word \(U\) from \(E\) to \(G\) gives

\[
C^3U=(UB)^3U=U(BU)^3=UR^3,
\]

contradicting \(\kappa(G)=2\). Thus \(p\ne q\).

Let \(e_0=\gcd(p,q)\). If the length \(P=q+r\) met the Fine--Wilf
threshold for the periods \(p,q\), then \(W\), and hence its length-\(q\)
prefix \(R\), would have period \(e_0\). Here \(e_0\mid q\) and
\(e_0<q\): (C.11) gives \(p<P<3q/2\), so the only multiple of \(q\) in
the allowed range is the already excluded value \(p=q\). The word \(R\)
would therefore be a proper \(e_0\)-power, and the suffix \(R^2\) of \(G\)
would have exponent at least four. This is impossible, so the threshold
fails:

\[
\boxed{r<p-\gcd(p,q).}
\tag{C.16}
\]

A second Fine--Wilf failure is useful. Put \(g_0=\gcd(p,r)\). If

\[
2r\ge p+r-g_0,
\]

then \(p\le r+g_0\le2r\), so the suffix \(B^2\) inherits period \(p\)
from \(W\); it also has period \(r\). Fine--Wilf therefore gives period
\(g_0\) on \(B^2\). When \(g_0<r\), the divisor relation
\(g_0\mid r\) makes \(B\) a proper power, contradicting the canonical
cube \(B^3\). The endpoint \(g_0=r\) also fails: (C.16) gives \(p>r\),
while the displayed threshold gives \(p\le2r\), so \(r\mid p\) forces
\(p=2r\). The terminal \(p\)-block is then \(X=B^2\), and \(X^3=B^6\)
contradicts both the primitivity of the canonical root \(X\) and
\(\kappa(E)=3\). Therefore

\[
\boxed{p>r+\gcd(p,r).}
\tag{C.17}
\]

There are now two exact branches.

#### The branch \(p>q\)

Put \(t=p-q\). Since \(p<P=q+r\), one has \(0<t<r\). Comparing the
length-\((r-t)\) prefix and suffix imposed by period \(p=q+t\) on
\(W=BUB\) gives

\[
B[0:r-t]=B[t:r],
\]

so \(B\) has period \(t\). If \(t\le r/2\), the final \(2t\) letters of
\(B\) form a square ending at \(G\) with period below \(q\). Hence

\[
\boxed{r/2<t<r.}
\tag{C.18}
\]

The terminal \(p\)-block of \(W\) is forced:

\[
\boxed{X=B[r-t:r]\,U\,B.}
\tag{C.19}
\]

#### The branch \(p<q\)

Put \(d=q-p>0\). The prefix \(R\) of the \(p\)-periodic word \(W\) has
period \(p\). If \(p\le q/2\), it ends in a \(p\)-square, again
contradicting \(\pi(G)=q\). Thus

\[
\boxed{p>q/2.}
\tag{C.20}
\]

Writing \(Z=R[0:p]\), the exact \(p\)-periodic form is

\[
\boxed{R=Z\,Z[0:d].}
\tag{C.21}
\]

Both \(d<q/2\) and \(r<q/2\), so \(d+r<q\). Period \(p=q-d\) on \(W\)
then compares the two length-\(r\) factors at offsets \(d\) and \(q\):

\[
\boxed{R[d:d+r]=B=R[0:r]=R[q-r:q].}
\tag{C.22}
\]

The terminal \(p\)-block is

\[
\boxed{X=R[d+r:q]\,B.}
\tag{C.23}
\]

There is no universal deduction \(d<r\). In the subcase where \(d<r\),
(C.22) gives period \(d\) on \(B\); if \(d\le r/2\), that again creates a
shorter square suffix at \(G\). The exact conditional restriction is

\[
\boxed{d<r\ \Longrightarrow\ d>r/2.}
\tag{C.24}
\]

Finally define the positive frontier length

\[
\eta=3p-P>0.
\]

Since \(E=LW\) ends in \(X^3\), the early left context is not free:

\[
\boxed{\operatorname{suf}_{\eta}(L)\,W=X^3.}
\tag{C.25}
\]

This frontier equation applies to both \(p\)-branches.

### 5. All-continuation localization in the branch \(p>q\)

The previous early- and later-window length estimates can be replaced by one
stronger lemma. Put

\[
\mathcal C=UB^2U,\qquad |\mathcal C|=2q,
\tag{C.26}
\]

write \(E=\mathcal D X^3\), and define

\[
A_v=X^3\mathcal C[0:v],\qquad
S_v=\mathcal D A_v
\qquad(0\le v\le2q).
\tag{C.27}
\]

These are the actual consecutive states from \(S_0=E\) through
\(S_{2q}=H\).

**All-continuation localization lemma.** Let \(0\le v<2q\), and suppose

\[
\kappa(S_v)=k\in\{2,3\},\qquad h=\pi(S_v)<P.
\]

Then

\[
\boxed{
(\kappa(A_v),\pi(A_v))
=
(\kappa(S_v),\pi(S_v)).
}
\tag{C.28}
\]

For \(k=2\), the canonical square has length
\[
2h<2P<3p\le |A_v|,
\]
where \(3p>2P\) follows from \(p>q>2r\). It therefore lies wholly in
\(A_v\). The suffix relation gives
\(\kappa(A_v)\le\kappa(S_v)=2\), so the exponents agree.

For \(k=3\), suppose instead that the canonical \(h\)-cube crosses the left
edge of \(A_v\). It then contains all of \(A_v\), in particular \(X^3\),
and

\[
3h>|A_v|\ge3p,
\]

so \(h>p\). On the other hand, \(r<q/2\) and \(p>q\) give

\[
p<h<P=q+r<2p.
\tag{C.29}
\]

The factor \(X^3\) has periods \(p\) and \(h\). Put
\(g=\gcd(p,h)\). Since \(h<2p\),

\[
3p\ge p+h-g,
\]

so Fine--Wilf gives period \(g\) on \(X^3\). Moreover \(g<p\):
otherwise \(p\mid h\), but there is no multiple of \(p\) strictly between
\(p\) and \(2p\). Because \(g\mid p\), the length-\(p\) word \(X\) is then
a proper \(g\)-power, contradicting the already proved primitivity of \(X\).
Thus the canonical cube cannot cross; it too lies wholly in \(A_v\), and the
full and local exponents agree.

In either case, the global canonical \(h\)-witness is a local maximizing
witness, so \(\pi(A_v)\le h\). Conversely, every local maximizing suffix
power is also a suffix power of \(S_v\), so \(h\le\pi(A_v)\). This proves
the complete canonical-pair equality (C.28), not only equality of curling
numbers.

The target scopes must remain separate. Under the negation of
(G2CS-\(\mathcal I\)), the period cap guarantees the lemma's hypotheses on

\[
E_\ell=S_\ell\quad(0\le\ell\le m),
\qquad
F_\ell=S_{P+\ell}\quad(0\le\ell<m).
\tag{C.30}
\]

This includes \(G=E_m\) and every proper \(F\)-window state. It does **not**
cap, and therefore does not guarantee localization of, the omitted interior
bridge states

\[
S_v\qquad(m<v<P).
\]

Under the negation of (G2CS-\(\mathcal J\)), every proper state from \(E\)
through the state immediately before \(H\) has period below \(P\). Since the
actually generated continuation \(\mathcal C\) is binary, (C.28) applies at
every such state:

\[
\boxed{
(\kappa(A_v),\pi(A_v))
=
(\mathcal C[v],\pi(S_v)),
\qquad
\pi(A_v)<P
\quad(0\le v<2q).
}
\tag{C.31}
\]

Thus the entire \(UB^2U\) episode is autonomous under the
\(\mathcal J\)-negation. Finally, the known period-\(P\) square at \(H\) is
also contained in \(A_{2q}\), since
\[
|A_{2q}|=3p+2q>2P.
\]
Every local suffix power persists in \(H\). Hence

\[
\boxed{(\kappa(A_{2q}),\pi(A_{2q}))=(2,P).}
\tag{C.32}
\]

#### First-mismatch corollary

The autonomous early window gives a further exact restriction under the
negation of either target. Put

\[
a=P-p=r-t,
\]

and let

\[
z=\min\{\ell:U[\ell]=2\}.
\]

This index exists and satisfies \(1\le z<m\): \(U[0]=3\), while
\(U=QB\) contains \(B[0]=2\). Compare \(X[0:m]\) with \(U\). If there is
no mismatch before \(z\), then \(X[0:z]=U[0:z]\). Writing
\(X=C_0D_0\) with \(C_0=X[0:z]\), the local state at phase \(z\) would be

\[
A_z=X^3X[0:z]
    =(C_0D_0)^3C_0
    =C_0(D_0C_0)^3.
\]

It would have curling number at least three. But (C.28) applies to the
early state \(E_z=S_z\), while actual generation requires
\(\kappa(E_z)=U[z]=2\), a contradiction. Thus
there is a first mismatch \(h\), and it satisfies

\[
h<z,\qquad U[0:h+1]=3^{h+1},\qquad X[h]=2.
\tag{C.33}
\]

Let \(d\) be the length of the terminal run of \(3\)'s in \(B\). The
later state \(F_z\) ends in that run followed by the prefix
\(U[0:z]=3^z\), so it ends in \(3^{d+z}\). Paired generation gives
\(\kappa(F_z)=U[z]=2\), and hence

\[
d+z\le2.
\tag{C.34}
\]

Since \(z\ge1\) and \(0\le h<z\), only three cases remain:

\[
\begin{array}{c|c|c}
(z,h)&\text{start of }U&\text{forced data}\\
\hline
(1,0)&32&B[a]=2,\ d\le1,\\
(2,0)&332&B[a]=2,\ B\text{ ends in }2,\\
(2,1)&332&B[a:a+2]=32,\ B\text{ ends in }2.
\end{array}
\tag{C.35}
\]

For the last row, \(h=1\) gives \(X[0]=U[0]=3\) and \(X[1]=2\);
the initial block \(B[a:r]\) of \(X\) has length
\(t>r/2\), hence integer \(t\ge2\), so these are exactly the two
displayed coordinates of \(B\).

### 6. Exact remaining word obstructions

The stronger localization still does not close the \(p>q\) boundary branch.
It gives different exact word residuals for the two targets.

For the stronger \(\mathcal I\)-only target, the forced tuple

\[
q>2r>0,\quad P=q+r,\quad |B|=r,\quad
R=BQB,\quad U=QB,\quad B[0]=2,\quad Q[0]=3,
\]

\[
p=q+t,\quad r/2<t<r,\quad X=B[r-t:r]UB,
\]

with the inherited standalone conditions

\[
(\kappa(R^2),\pi(R^2))=(2,q),\qquad
\kappa(R^2B)=2,\qquad
(\kappa(BRB^2),\pi(BRB^2))=(3,r),
\]

must realize

\[
\begin{gathered}
(\kappa(A_0),\pi(A_0))=(3,p),\qquad
(\kappa(A_m),\pi(A_m))=(2,q),\\
(\kappa(A_P),\pi(A_P))=(3,r),\qquad
(\kappa(A_{2q}),\pi(A_{2q}))=(2,P),\\
\kappa(A_\ell)=\kappa(A_{P+\ell})=U[\ell],\\
\pi(A_\ell)<P,\qquad\pi(A_{P+\ell})<P
\qquad(0\le\ell<m).
\end{gathered}
\tag{C.36}
\]

It remains to prove that no forced boundary word satisfies (C.36), or to
extract the required period-\(P\) witness. The interior bridge is deliberately
absent from the period inequalities in (C.36); adding it would silently
replace the stronger target by \(\mathcal J\).

For the bridge-inclusive target, the exact open word wall is stronger:
prove that no forced boundary word can satisfy the autonomous episode
(C.31) together with the endpoint (C.32). This is now a finite-word
dynamical obstruction with no left-context variable, but it remains
unproved.

The earlier \(F\)-window-only replay claim required its period cap. The
sharp local model

\[
\begin{gathered}
q=9,\quad r=3,\quad P=12,\quad t=2,\quad p=11,\\
B=232,\quad U=322232,\quad R=232322232,\\
X=32322232232
\end{gathered}
\]

has local \(F\)-window pairs

\[
(3,3),(2,2),(2,2),(2,1),(3,1),(2,12),
\]

whose exponents replay \(U\), and its local terminal pair is \((2,12)\).
It is excluded twice from the exact residual: the final proper
\(F\)-window period is already \(P\), and
\(\kappa(A_1)=\kappa(X^3U[0:1])=3\ne U[1]=2\). By (C.28), no omitted left
context can repair that early mismatch. The model remains a sharpness
certificate for the older \(F\)-only claim, not a G2CS counterexample.
Equivalently, its first \(2\) has \(z=1\), but
\(a=r-t=1\) and \(B[a]=X[0]=3\), contradicting the first row of (C.35).

The first-mismatch trichotomy is not itself a contradiction. The
definition-first near-model

\[
\begin{gathered}
q=10,\quad r=4,\quad P=14,\quad t=3,\quad p=13,\\
B=2232,\quad Q=32,\quad U=322232,\\
R=2232322232,\quad X=2323222322232
\end{gathered}
\]

has \(z=1\), \(a=1\), and \(B[a]=X[0]=2\), as allowed by the first row.
Its local early-window pairs are

\[
(3,13),(2,2),(2,2),(2,1),(3,1),(2,6),
\]

and its local later-window pairs are

\[
(3,4),(2,2),(2,2),(2,1),(3,1),(2,6).
\]

Both sampled windows replay \(U\), and all twelve displayed periods are
below \(P\). However its local \(G\)- and \(H\)-scale pairs are
\((2,6)\), not \((2,q)\) and \((2,P)\). It is therefore a sharpness warning
that the endpoint scales in (C.36) remain load-bearing, not a survivor or
counterexample.

The two word walls above remain unproved, as do the \(p<q\) frontier equation
(C.25) and the non-boundary regions of (C.5)--(C.6). There is also no
transfer of the final Cell A argument: here
\[
E=LRT=LT(UT)
\]
ends only in \(T(UT)\), whereas Cell A obtained two full copies of the
conjugate \(UT\). Its \(C^2\) period step therefore cannot be imported into
Cell C.

### 7. Focused executable index certificate

`tests/test_generated_two_cube_cell_c_reduction.py` is independent of the
production equality-first search. Through \(q\le10\), a definition-first
enumeration retains `4958` cube-equality assignments, `538` after imposing
\((\kappa(R^2),\pi(R^2))=(2,q)\), and `489` after imposing both the
standalone no-cube condition and the exact local later-cube pair. All `489`
satisfy (C.7)--(C.8). Exactly `257` lie on \(s=2r,j=r\), and `130` of
those also have the generation-compatible first bridge label \(B[0]=2\).

Among those `130`, the certificate retains `13` possible \(p\)-periods
meeting (C.15) and \(p\ne q\): `7` in the \(p>q\) branch and `6` in the
\(p<q\) branch. It checks (C.16)--(C.25) directly in every retained tuple.
The same test pins the period-\(P\) sharpness model above and verifies that it
fails the early replay. It also pins the \(q=10\) near-model's two exact
six-state local timelines and its incorrect period-\(6\) endpoint scales.
These nonzero bounded counts are index and algebra checks only; they are
**not a proof** of the universal deductions or of either open word wall.

### 8. Equality-first exhaustive engine

For fixed \((q,b,j,r)\), every coordinate \(z\) of \(V=BRBT\) comes from
the following coordinate of \(R\):

\[
\phi(z)=
\begin{cases}
q-b+z,&0\le z<b,\\
z-b,&b\le z<P,\\
q-b+z-P,&P\le z<P+b,\\
z-P-b,&P+b\le z<N.
\end{cases}
\tag{C.37}
\]

The executable search first unions

\[
\phi(z)\sim\phi(z+r)\qquad(\alpha\le z<N-r),
\]

then forces the class containing \(j\) to carry symbol \(3\), as required by
\(R[j]=\kappa(E)=\kappa(F)=3\). It enumerates only the remaining binary
equality classes. An independent brute-force oracle through \(q=8\) finds
exactly the same `197` integer tuples and `1036` root assignments.

Each retained root is then checked for the exact standalone canonical
condition \(\kappa(R^2T)=2\). For every binary \(L\) with
\(|E=LRT|\) under the explicit cap, a separate canonical oracle verifies
every requested label in the full future word \(UBTU\), rechecks the
canonical data at \(E,G,F,H\), and evaluates the original \(\mathcal I\) and
bridge-inclusive \(\mathcal J\) time sets independently. Structural keys
\((L,R,b,j,r)\) prevent duplicate trace evidence.

### 9. Bounded result through \(|E|\le18\)

The deterministic run retained

```text
parameter_tuples=2361
equality_assignments=714444
standalone_no_cube_assignments=239350
bounded_contexts=2866488
actual_generation_traces=120
g2cs_antecedents=120
I_witnesses=120
I_survivors=0
J_witnesses=120
J_survivors=0
J_only_witnesses=0
root_parameter_families=1
boundary_s_eq_2r_j_eq_r_antecedents=120
```

All 120 antecedents have

\[
(R,b,j,r)=((2,3,2),1,1,1).
\]

Thus every retained antecedent lies simultaneously on the exact cut
boundaries \(s=2r\) and \(j=r\); none is lost into either adjacent strict
inequality case in (C.5)--(C.6).

The least positive certificate has

\[
L=23222322,\quad E=232223222322,\quad UBTU=322232,
\]

with exact relative-state witnesses

\[
(3,4),(2,3),(2,3),(2,1),(3,1),(2,7),(2,4).
\]

Here the entries are \((\kappa,\pi)\) at times \(0,\ldots,6\);
\(\mathcal I\) uses times \(0,1,2,4,5\), while \(\mathcal J\) additionally
uses bridge time \(3\). Both maxima are \(7\ge P=4\).

This is a bounded binary local-start computation. Zero \(\mathcal I\)- or
\(\mathcal J\)-survivors is **not a proof**, and Cell C remains `OPEN` for
both targets.
