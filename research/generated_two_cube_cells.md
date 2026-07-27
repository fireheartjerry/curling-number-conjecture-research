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

In fact the overlap equations force \(d\) beyond two full copies of \(B\).
Period \(p=q-d\) on \(W\) makes \(R\) have border \(d\).

If \(d<r\), that border gives \(B\) period \(r-d\), while the equality
\(R[d:d+r]=B=R[0:r]\) gives \(B\) period \(d\). Fine--Wilf on the
length-\(r\) word \(B\) gives period \(\gcd(d,r-d)\). This proper divisor
of \(r\) makes \(B\) a proper power, contradicting the canonical pair
\((\kappa(F),\pi(F))=(3,r)\).

If \(d=r\), the middle occurrence in (C.22) begins immediately after the
initial \(B\). It therefore requires
\(Q[0]=R[r]=B[0]\), contradicting \(Q[0]=3\) and \(B[0]=2\).

It remains to exclude \(r<d\le2r\). Put
\[
a=d-r.
\]
Since \(d<q/2\), one has \(2a<q-2r=|Q|\). Define the disjoint prefix and
suffix
\[
A=Q[0:a],\qquad C=Q[|Q|-a:|Q|].
\]
The length-\(d\) border equation on \(R=BQB\) is exactly
\[
BA=CB.
\]
If \(a<r\), this equality gives \(B\) period \(a\) and
\(A=\operatorname{suf}_a(B)\). Hence \(BA\) is \(a\)-periodic and has
length \(r+a>2a\). As \(BA\) is also the length-\(d\) suffix of \(R\),
it gives an \(a\)-square ending at \(G\), contradicting \(\pi(G)=q\).
If \(a=r\), the same equation gives \(A=B\), contradicting
\(A[0]=Q[0]=3\) and \(B[0]=2\). Therefore

\[
\boxed{d>2r,\qquad q>4r,\qquad p>2r.}
\tag{C.24}
\]

The surviving coordinates have a useful exact normal form. Put
\[
\nu=d-2r>0.
\]
The equation \(BA=CB\) now gives
\[
A=\Theta B,\qquad C=B\Theta
\]
for a word \(\Theta\) of length \(\nu\). The middle occurrence in (C.22)
supplies the following copy of \(B\), so

\[
\boxed{
Q[0:\nu+2r]=\Theta B^2,\qquad
Q[|Q|-(r+\nu):|Q|]=B\Theta.
}
\tag{C.24a}
\]

In particular \(d>r\), so \(p=q-d<q-r=|U|\). The terminal root in (C.23)
can be written entirely in \(Q\)-coordinates:

\[
\boxed{X=Q[d:|Q|]\,B^2.}
\tag{C.24b}
\]

The two possible seams in (C.24a) can be exposed exactly. Put

\[
D=Q[d:|Q|],\qquad \sigma=|D|=p-2r.
\]

Then

\[
Q=\Theta B^2D,\qquad \sigma>\nu,
\]

where the strict inequality is equivalent to \(p>q/2\). Define

\[
e=\sigma-r-\nu=2p-P.
\]

If \(e\ge0\), the required suffix \(B\Theta\) lies wholly in \(D\), and
there is a word \(J\) of length \(e\) such that

\[
\boxed{D=JB\Theta.}
\tag{C.24c}
\]

If \(e<0\), put \(c=-e=P-2p\). The inequality \(\sigma>\nu\) gives
\(0<c<r\). The length-\((r+\nu)\) suffix of \(Q\) starts in the final
displayed \(B\), so comparison with \(B\Theta\) gives

\[
\boxed{
B[0:c]=B[r-c:r],\qquad D=B[c:r]\Theta.
}
\tag{C.24d}
\]

The localization proof below sharpens this seam to \(0<c<r/2\) in (C.28a).
Both alternatives have the same useful conjugate-overlap form. Temporarily
put

\[
C=\Theta B^2,\qquad H_0=\Theta B,\qquad
A=
\begin{cases}
JB,&e\ge0,\\
B[c:r],&e<0.
\end{cases}
\]

Here \(A\ne\epsilon\) because \(\sigma>\nu\), and \(H_0\) is a local tail
word, not the global completion state \(H\). In both seams \(D=A\Theta\),
so

\[
\boxed{X=AC,\qquad U=CAH_0.}
\tag{C.24e}
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

### 5. All-continuation localization on the boundary

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

**All-continuation localization lemma.** In either branch \(p>q\) or
\(p<q\), let \(0\le v<2q\), and suppose

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

First suppose \(p>q\). For \(k=2\), the canonical square has length
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
Thus the canonical cube cannot cross in the \(p>q\) branch.

Now suppose \(p<q\). One extra suffix calculation handles the only range
not covered directly by Fine--Wilf. If \(2p<P\), put
\[
c=P-2p.
\]
The inequality \(p>q/2\) gives \(0<c<r\). Since \(W\) is the
length-\(P\) suffix of \(X^3\),
\[
W=\operatorname{suf}_c(X)X^2.
\]
The length-\(r\) prefix and suffix of \(W\) are both \(B\), and \(X\) ends
in \(B\). Hence
\[
B[0:c]=B[r-c:r],
\]
so \(B\) has period \(r-c\). If \(r-c\le r/2\), the end of \(B\), and
therefore of \(G\), contains an \((r-c)\)-square with root below \(q\).
This contradicts \((\kappa(G),\pi(G))=(2,q)\). Thus
\[
\boxed{2p<P\ \Longrightarrow\ 0<c=P-2p<r/2.}
\tag{C.28a}
\]

Suppose a canonical \(k\)-power of root length \(h<P\) crosses the left
edge of \(A_v\). It contains \(X^3\), so
\[
kh>|A_v|\ge3p.
\]
For \(k=2\) this gives \(h>3p/2\), and for \(k=3\) it gives \(h>p\).
Thus \(h>p\) in either case.

If \(p<h<2p\), then the length-\(3p\) word \(X^3\) has periods \(p,h\).
Fine--Wilf gives period \(\gcd(p,h)<p\), contradicting the primitivity of
\(X\).

If \(h=2p\), write the crossing power as \(Y^k\), with \(|Y|=2p\).
The period-\(p\) equalities in its factor \(X^3\) have \(2p\) consecutive
starting positions. They therefore meet every residue modulo \(2p\) and
give \(Y\) period \(p\). Thus \(Y\) is a square, and \(Y^k\) has exponent
at least four, contradicting \(k\in\{2,3\}\).

Finally suppose \(h>2p\). This case can occur only when \(2p<P\). Put
\[
\delta=h-2p.
\]
By (C.28a),
\[
0<\delta<c<r/2.
\]
Period \(h=2p+\delta\) on \(X^3\) gives
\[
X[i]=X[i+\delta]\qquad(0\le i<p-\delta),
\]
so \(X\) has period \(\delta\). Since \(X\) ends in \(B\), the final
\(2\delta\) letters of \(B\) form a \(\delta\)-square ending at \(G\),
again contradicting \(\pi(G)=q\).

All possible crossing roots are excluded in both branches. The canonical
suffix power therefore lies wholly in \(A_v\), and the full and local
exponents agree.

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
negation of either target. Let

\[
z=\min\{\ell:U[\ell]=2\}.
\]

This index exists and satisfies \(1\le z<m\): \(U[0]=3\), while
\(U=QB\) contains \(B[0]=2\). Let \(\lambda\) be the length of the
terminal run of \(3\)'s in \(B\).
The later state \(F_z\) ends in that run followed by the prefix
\(U[0:z]=3^z\), so it ends in \(3^{\lambda+z}\). Paired generation gives
\(\kappa(F_z)=U[z]=2\), and hence

\[
\lambda+z\le2.
\tag{C.33}
\]

In particular \(z\le2\). Both period branches give \(p>2\):
for \(p>q\), use \(q>2r\), and for \(p<q\), use (C.24). Thus \(z<p\).

Compare \(U\) with the periodic extension \(X^\omega\). This formulation is
essential in the \(p<q\) branch, where (C.24) gives
\(p<q-r=|U|\). If there is no mismatch before \(z\), then
\(X[0:z]=U[0:z]\). Writing \(X=C_0D_0\) with
\(C_0=X[0:z]\), the local state at phase \(z\) would be

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
\tag{C.34}
\]

Since \(z\ge1\) and \(0\le h<z\), only three cases remain:

\[
\begin{array}{c|c|c}
(z,h)&\text{start of }U&\text{forced data}\\
\hline
(1,0)&32&X[0]=2,\ \lambda\le1,\\
(2,0)&332&X[0]=2,\ B\text{ ends in }2,\\
(2,1)&332&X[0:2]=32,\ B\text{ ends in }2.
\end{array}
\tag{C.35}
\]

In the \(p>q\) branch, put \(a=P-p=r-t\). Formula (C.19) identifies the
displayed \(X\)-coordinates with \(B[a]\) in the first two rows and with
\(B[a:a+2]\) in the last row. For the last row,
\(t>r/2\) implies integer \(t\ge2\), so both coordinates lie in the
initial block \(B[a:r]\). In the \(p<q\) branch the same three rows apply
to the periodic word \(X^\omega\), with \(X\) given by (C.24b).

#### Two-scale phase dichotomy in the \(p>q\) branch

The canonical \(G\)-scale gives a sharper restriction on every early
replacement root, although it does not close the branch. Retain \(p>q\) and
put \(a=r-t\). For \(0\le\ell\le m=|U|\), the identities \(W=RB\) and
\(R=BU\) give the exact suffix

\[
T_\ell=R\,R[0:r+\ell]
\tag{C.35a}
\]

of \(A_\ell=X^3U[0:\ell]\). Thus \(T_\ell\) has period \(q\) and length

\[
L_\ell=q+r+\ell.
\]

Let \(A_\ell\) have canonical pair \((k,s)\), where
\[
k\in\{2,3\},\qquad s<P,\qquad s\ne q,
\]
and put \(g=\gcd(s,q)\). The canonical \(s\)-power and \(T_\ell\) are both
suffixes, so their common suffix has length

\[
M=\min(ks,L_\ell)
\]

and periods \(s,q\). We claim that the Fine--Wilf threshold is missed:

\[
\boxed{M<s+q-g.}
\tag{C.35b}
\]

Phases with \(s=q\) are deliberately outside (C.35b); they already sit at
the \(G\)-scale rather than in the replacement-root comparison below.

Suppose instead that \(M\ge s+q-g\). Fine--Wilf gives period \(g\) on the
common suffix. If \(M=ks\), this common suffix is the whole canonical
\(s\)-power. When \(g<s\), its primitive length-\(s\) root acquires the
proper period \(g\), a contradiction.

There is one divisor endpoint which must not be skipped. If \(g=s\), then
\(s\mid q\), and the assumed threshold gives \(ks\ge q\). The final
length-\(q\) block of the \(s\)-power is therefore a proper power of a
conjugate of its length-\(s\) root. The same block is the final
length-\(q\) factor of \(T_\ell\). Since
\[
T_\ell=R\,R[0:r+\ell],
\]
that factor is a conjugate of \(R\) (or \(R\) itself when
\(r+\ell=q\)). A conjugate of a proper power is a proper power, so \(R\)
would be imprimitive. This contradicts
\((\kappa(R^2),\pi(R^2))=(2,q)\).

If \(M=L_\ell\), then all of \(T_\ell\) has period \(g\), so its prefix
\(R\) has period \(g\). Here \(g<q\): otherwise \(q\mid s\), while
\[
0<s<P=q+r<2q
\]
and \(s\ne q\), which is impossible. Because \(g\mid q\), the word \(R\)
would again be a proper power. This proves (C.35b).

The comparison in the minimum now gives an exact two-branch restriction:

\[
\boxed{
\begin{array}{ll}
ks\le L_\ell:&(k-1)s<q-g,\\[1mm]
L_\ell<ks:&s>r+\ell+g.
\end{array}}
\tag{C.35c}
\]

The first row is a contained low-root branch; the second is a
context-crossing high-root branch. This is a phase restriction, not a
monotone rank: adjacent root pushes can move from the first branch back
toward the \(q\)-scale.

The first mismatch gives one additional exact pop. Let \(u\) be the
mismatch index in (C.34), and put \(w=u+1\). The state \(A_u\) still ends
in a primitive maximizing \(p\)-cube, because
\(U[0:u]=X[0:u]\). The appended symbol is
\[
U[u]=3\ne X[u]=2,
\]
so the \(p\)-periodic suffix does not extend. Write the next canonical pair
as
\[
(\kappa(A_w),\pi(A_w))=(k_1,s).
\]
Under either target negation, \(s<P\). The adjacent-root separation lemma
proved in `research/adjacent_root_stack.md` rules out \(s=p\). A push
\(s>p\) would require
\[
s>2p+\gcd(p,s),
\]
whereas \(s<P=q+r<2p\). Hence the first replacement is necessarily a pop:

\[
\boxed{s<p,\qquad p\ge(k_1-1)s+\gcd(p,s).}
\tag{C.35d}
\]

In the rows \((z,u)=(1,0),(2,1)\), the new label is \(k_1=2\). In the
row \((2,0)\), it is \(k_1=3\), so
\[
p\ge2s+\gcd(p,s).
\]
Both the early and later states at phase \(w\) share the suffix
\(B^2U[0:w]\) of length \(2r+w\). Thus the replacement power is local to
that common suffix exactly when
\[
k_1s\le2r+w;
\]
otherwise it is a context-crossing replacement. Equations (C.35c)--(C.35d)
classify the latter case but do not eliminate it.

The endpoint jump itself is genuinely feasible. The exact structural model

\[
\begin{gathered}
q=9,\quad r=4,\quad t=3,\quad p=12,\quad P=13,\\
B=2332,\quad Q=3,\quad U=32332,\\
R=233232332,\quad X=332323322332,\quad Y=B^2U
\end{gathered}
\tag{C.35e}
\]

has
\[
(\kappa(X^3),\pi(X^3))=(3,12)
\]
and the simultaneous one-symbol transitions
\[
\begin{array}{rcl}
R^2[0:2q-1]:(2,1)&\xrightarrow{\ 2\ }&R^2:(2,9),\\
Y^2[0:2P-1]:(2,1)&\xrightarrow{\ 2\ }&Y^2:(2,13).
\end{array}
\tag{C.35f}
\]
It fails the required early replay earlier: at phase \(1\), the requested
symbol is \(U[1]=2\), while the local pair remains \((3,12)\). Therefore
endpoint and adjacent-root geometry alone cannot close the word wall; a
completion must use the whole replay before the final push.

#### Universal elimination of the double-`3` rows

The two rows with \(z=2\) are in fact impossible without distinguishing
\(p>q\) from \(p<q\). Suppose \(z=2\). Then

\[
U[0:3]=332.
\]

The first appended `3` after \(F\) produces the actual sampled state

\[
F_1=F\,3=LR^2B^2\,3.
\]

Paired generation at phase \(1\) gives \(\kappa(F_1)=U[1]=3\). Moreover
\(F_1\in\mathcal I\) because \(1<m\), and hence \(F_1\in\mathcal J\).
Under the negation of either target its exact canonical pair is therefore

\[
\boxed{
(\kappa(F_1),\pi(F_1))=(3,\rho),\qquad \rho<P=q+r.
}
\tag{C.35g}
\]

Delete the final `3` from the canonical \(\rho\)-cube at \(F_1\). What
remains is a \(\rho\)-periodic suffix of \(F\) of length

\[
3\rho-1.
\tag{C.35h}
\]

Put \(g=\gcd(r,\rho)\). We first eliminate every \(\rho\le2r+g\).

If \(\rho<r\) and \(2\rho\le r\), the final \(2\rho\) letters in (C.35h)
form a \(\rho\)-square inside the last \(B\). The identical word \(B\) ends
\(G\), so this is a square at \(G\) with root below \(q\), contradicting
\((\kappa(G),\pi(G))=(2,q)\).

If \(\rho<r\) and \(2\rho>r\), the suffix in (C.35h) lies inside the
terminal \(B^3\), so it has periods \(\rho,r\). The Fine--Wilf threshold is
met because

\[
3\rho-1-(r+\rho-g)=2\rho+g-r-1\ge0.
\]

It therefore has period \(g<r\). The suffix contains a complete terminal
copy of \(B\); since \(g\mid r\), \(B\) is a proper power. Then the
terminal \(B^3\) at \(F\) has exponent at least six, contradicting
\(\kappa(F)=3\).

If \(\rho=r\), periodicity of the canonical cube makes its final `3` equal
to the symbol \(r\) positions earlier. That symbol is the first letter of
the final \(B\), namely \(B[0]=2\), a contradiction.

It remains within this range to take \(r<\rho\le2r+g\). Now (C.35h)
contains the whole terminal \(B^3\). That word has periods \(r,\rho\), and

\[
3r\ge r+\rho-g.
\]

Fine--Wilf gives period \(g\) on \(B^3\). If \(g<r\), the same
proper-power contradiction follows. If \(g=r\), then \(r\mid\rho\), and

\[
r<\rho\le3r
\]

leaves only \(\rho=2r\) or \(\rho=3r\). In either case the final `3` in
the canonical cube copies the first symbol of one of the displayed
\(B\)'s, again \(B[0]=2\).

Consequently

\[
\rho>2r+g.
\tag{C.35i}
\]

Remove the last \(2r\) symbols, namely the appended \(B^2\), from the
suffix in (C.35h). The remaining suffix of \(G\) is \(\rho\)-periodic and
has length

\[
L_\rho=3\rho-1-2r>2\rho.
\tag{C.35j}
\]

Thus \(G\) ends in a \(\rho\)-square, so its exact canonical pair forces
\(\rho\ge q\). Write

\[
\rho=q+u,\qquad 0\le u<r,
\tag{C.35k}
\]

where the upper bound uses \(\rho<P\). If \(u>0\), then

\[
L_\rho-2q=q+3u-2r-1>0
\]

because \(q>2r\). The whole terminal \(R^2\) of \(G\) is therefore
\((q+u)\)-periodic. Comparing its two displayed copies gives

\[
R[0:q-u]=R[u:q],
\]

so \(R\) has period \(u<r<q/2\). Its final \(2u\) letters form a
\(u\)-square ending at \(G\), again contradicting the canonical root
\(q\). Hence \(u=0\) and

\[
\rho=q.
\]

Finally label the displayed copies in the suffix of \(F_1\):

\[
S=R_1R_2B_3B_4\,3.
\]

Its length is \(2q+2r+1\le3q\), since \(q>2r\). Therefore \(S\) lies
inside the terminal canonical \(q\)-cube at \(F_1\) and inherits period
\(q\). But the two positions

\[
R_2[r]=Q[0]=3,\qquad B_4[0]=B[0]=2
\]

are exactly \(q\) apart inside \(S\), the final contradiction.

Thus \(z=2\) is impossible under the negation of either target. The
three-row trichotomy (C.35) collapses to

\[
\boxed{
(z,h)=(1,0),\qquad U[0:2]=32,\qquad X[0]=2,\qquad\lambda\le1.
}
\tag{C.35l}
\]

This conclusion is local to the simultaneous boundary. It does not move
the other Cell C placements onto that boundary and does not eliminate the
remaining row.

#### Exact transition restrictions in the surviving row

Retain \((z,h)=(1,0)\), and use the shorter paired-state notation

\[
E_\ell=X^3U[0:\ell],\qquad
F_\ell=X^3UB^2U[0:\ell]\qquad(0\le\ell\le m).
\]

Under the negation of either target, phase \(1\) is sampled in both
windows, so (C.28) gives exact local pairs

\[
\boxed{
(\kappa(E_1),\pi(E_1))=(2,\alpha),\qquad
(\kappa(F_1),\pi(F_1))=(2,\beta),\qquad
\alpha,\beta<P.
}
\tag{C.35m}
\]

Both old cubes break when the first `3` is appended:

\[
3\ne X[0]=B[0]=2.
\]

For the early transition, \(\alpha\ne p\). If \(\alpha>p\), the
adjacent-root separation lemma would give

\[
\alpha>2p+\gcd(p,\alpha).
\]

But (C.28) localizes the canonical square to \(X^3\,3\), while the last
inequality gives

\[
2\alpha>4p+2>|X^3\,3|=3p+1.
\]

Thus the early transition is always a strict pop:

\[
\boxed{
\alpha<p,\qquad
p\ge\alpha+\gcd(p,\alpha).
}
\tag{C.35n}
\]

For the later transition, \(\beta\ne r\), and adjacent-root separation
gives the exact alternative

\[
\boxed{
\begin{array}{ll}
\beta<r:&r\ge\beta+\gcd(r,\beta),\\[1mm]
\beta>r:&\beta>2r+\gcd(r,\beta).
\end{array}}
\tag{C.35o}
\]

The two phase-one states have the identical terminal word

\[
T_1=B^2\,3,\qquad |T_1|=2r+1.
\]

If either canonical square has root at most \(r\), that square lies in
\(T_1\) and therefore occurs in both states. Since both exponents are
exactly two, least-root minimality in each direction forces equality.
The equality cannot be \(r\), because the appended `3` broke the
\(r\)-root at \(F_0\). Consequently

\[
\boxed{
\min(\alpha,\beta)\le r
\Longrightarrow
\alpha=\beta=s<r.
}
\tag{C.35p}
\]

The exact low square and its two pop inequalities are

\[
\operatorname{suf}_{2s}(B^2\,3)
  =(B[r-s+1:r]\,3)^2,\qquad B[r-s]=3,
\]

\[
r\ge s+\gcd(r,s),\qquad
p\ge s+\gcd(p,s).
\]

Otherwise both \(\alpha,\beta\) exceed \(r\). In particular, when \(r=1\),
the common suffix is \(223\), which has no square, so the low alternative
is impossible.

The high \(\beta\)-branch first gives

\[
2r+\gcd(r,\beta)<\beta<P.
\]

The endpoint \(\beta=q\) is impossible. Its terminal \(q\)-square contains
the two positions

\[
R_2[r]=Q[0]=3,\qquad B_4[0]=B[0]=2,
\]

which are exactly \(q\) apart. Nor can \(\beta=q+w\) for
\(0<w<r\). Copying \(T_1\) left by \(q+w\) gives

\[
R[q-w:q]R[0:|T_1|-w]=B^2\,3.
\]

The first \(w\) positions say \(B[-w:]=B[:w]\), and the next \(r\)
positions say

\[
B=B[w:r]B[0:w].
\]

Thus \(B\) is invariant under a nontrivial rotation and is a proper power.
Then the terminal \(B^3\) at \(F_0\) has exponent at least six,
contradicting \(\kappa(F_0)=3\). Since \(\beta<P=q+r\), this proves
\(\beta<q\) in the high alternative.

That alternative also has an exact return restriction before either period
branch is used. Put

\[
g_r=\gcd(r,\beta),\qquad v=P-\beta.
\]

The push inequality in (C.35o) gives

\[
1\le v\le m-g_r-1.
\]

Inside the terminal word \(R^2B^2\,3\), the canonical square is

\[
\boxed{
\operatorname{suf}_{2\beta}(R^2B^2\,3)
  =(R[r+v+1:q]B^2\,3)^2,\qquad R[r+v]=3.
}
\tag{C.35q}
\]

Delete the terminal \(B\,3\). The word

\[
K=R^2B=B(UB)^2
\]

inherits a \(\beta\)-periodic suffix of length

\[
L=2\beta-r-1.
\]

It also ends in the displayed \(q\)-square \((UB)^2\), whose root is
primitive because \(\kappa(K)=2\). Put \(d_\beta=\gcd(\beta,q)\).
There is one divisor endpoint to separate. If \(d_\beta=\beta\), then
\(\beta\mid q\), and \(\beta<q\) gives \(q\ge2\beta\). Therefore

\[
L=2\beta-r-1<2\beta\le q
  =\beta+q-d_\beta,
\]

so the Fine--Wilf threshold misses automatically.

Now suppose \(d_\beta<\beta\). If the common suffix of length
\(M=\min(L,2q)\) met the threshold, Fine--Wilf would give it period
\(d_\beta\). When \(M=L\), the threshold implies \(L>\beta\), and the
whole first primitive \(\beta\)-root left after deleting \(B\,3\) would
have the proper period \(d_\beta\). When \(M=2q<L\), the whole displayed
\(q\)-square would have period \(d_\beta\), so its primitive length-\(q\)
root \(UB\) would have that proper period. Both cases are impossible.
Hence

\[
\boxed{\min(L,2q)<\beta+q-d_\beta.}
\tag{C.35r}
\]

Equivalently,

\[
2v\ge r-1\Longrightarrow v\ge d_\beta,\qquad
2v<r-1\Longrightarrow v<r-d_\beta.
\]

Together with the push inequality and the two endpoint eliminations, the
high alternative is therefore restricted to

\[
\boxed{2r+\gcd(r,\beta)<\beta<q.}
\tag{C.35s}
\]

For \(p<q\), (C.24e) turns the two high-root returns into explicit seam
coordinates. Recall

\[
X=AC,\qquad U=CAH_0,\qquad |C|=d,\qquad |CA|=p.
\]

For \(\beta\), the return of \(T_1\) is

\[
\boxed{
\begin{array}{ll}
\beta\le m:&
U[m-\beta:m-\beta+|T_1|]=T_1,\\[1mm]
m<\beta<q:&
B[r-\delta:r]U[0:|T_1|-\delta]=T_1,\quad
\delta=\beta-m.
\end{array}}
\tag{C.35t}
\]

In the first row, the return interval has exactly six possible weak orders
relative to the cuts \(d,p\): wholly in \(C\), across \(C/A\), wholly in
\(A\), across \(A/H_0\), across both cuts, or wholly in \(H_0\).
The overlap seam \(A=B[c:r]\) is shorter than \(r\), so an interval of
length \(2r+1\) cannot lie wholly in \(A\).

The word \(T_1\) has no period \(\Delta\le r\). If \(\Delta<r\), compare
its positions \(r-\Delta\) and \(2r-\Delta\): period \(\Delta\) would make
\(B[r-\Delta]\) equal first to \(B[0]=2\) and then to the final `3`.
For \(\Delta=r\), the first symbol \(B[0]\) is compared directly with that
final `3`. The remaining endpoint \(\Delta=2r\) is also impossible, since
it compares \(T_1[0]=B[0]=2\) directly with \(T_1[2r]=3\). Thus every
proper period has the form \(\Delta=r+a\), \(1\le a<r\).

For the early root, if \(r<\alpha<|T_1|\), writing
\(\alpha=r+a\) makes the period comparisons on \(T_1\) give
\(B[i]=B[i+a]\) for \(0\le i<r-a\), together with
\(B[r-a]=3\). Thus \(B\) has period \(a\). If \(2a\le r\), its final
\(2a\) symbols form an \(a\)-square at \(G\), forcing
\(\pi(G)\le a<r<q\), a contradiction. Therefore

\[
r/2<a<r,\qquad B[r-a]=3,\qquad B\text{ has period }a.
\]

If \(\alpha\ge|T_1|\), put \(\sigma=p-2r\). Its return is

\[
\boxed{
\begin{array}{ll}
\alpha\le\sigma:&
X[\sigma-\alpha:\sigma-\alpha+|T_1|]=T_1,\\[1mm]
\alpha>\sigma:&
X[p-\delta_\alpha:p]X[0:|T_1|-\delta_\alpha]=T_1,\quad
\delta_\alpha=\alpha-\sigma.
\end{array}}
\tag{C.35u}
\]

These return equations expose the high-root word wall; they do not
eliminate it.

There is also a branch-independent restriction at every paired phase.
For \(0\le\ell\le m\), let the common requested exponent be
\(k_\ell\), with \(k_\ell=U[\ell]\) for \(\ell<m\) and \(k_m=2\), and
write the two canonical roots as \(a_\ell,b_\ell\). The states share

\[
T_\ell=B^2U[0:\ell],\qquad |T_\ell|=2r+\ell.
\]

If \(a_\ell\ne b_\ell\) and the smaller full maximizing power fit inside
\(T_\ell\), it would occur in both states. Since their exact exponents are
the same, canonical minimality would force the other root no larger, a
contradiction. Therefore

\[
\boxed{
a_\ell\ne b_\ell
\Longrightarrow
k_\ell\min(a_\ell,b_\ell)>2r+\ell.
}
\tag{C.35v}
\]

This permits context-crossing root divergence before a later failure; it
does not prove that paired roots or failure phases stay synchronized.

If the paired roots do remain equal through phase \(m-1\), write their
common predecessor root as \(s<P\) and put \(k=B[-1]\). Adjacent-root
separation at the two endpoints gives the exhaustive endpoint-only table

\[
\boxed{
\begin{array}{c|l}
k=3&
s<q,\quad q>2s+\gcd(s,q),\quad
P>2s+\gcd(s,P),\\[1mm]
k=2,\ s<q&
q>s+\gcd(s,q),\quad P>s+\gcd(s,P),\\[1mm]
k=2,\ s=q&
\text{the early root extends, while the later root pushes and }
r>\gcd(q,r),\\[1mm]
k=2,\ q<s<P&
s\ge q+\gcd(s,q),\quad P>s+\gcd(s,P).
\end{array}}
\tag{C.35w}
\]

The genuine bridge midpoint has one additional target-scope refinement.
Although

\[
M=LR^2B
\]

is omitted from \(\mathcal I\), its suffix

\[
K=R^2B=B(UB)^2
\]

has standalone label two. It displays the \(q\)-square \((UB)^2\), and
it also ends in the \(r\)-square \(B^2\). Actual bridge generation gives
\(\kappa(M)=B[0]=2\). If \((2,c)\) is the global pair at \(M\),
persistence and canonical minimality therefore sharpen the earlier
midpoint bound to

\[
\boxed{c\le\pi(K)\le r<q<P.}
\tag{C.35x}
\]

Thus (C.28) localizes \(M\) even under the \(\mathcal I\)-negation.
This does not cap every interior bridge state as the
\(\mathcal J\)-negation does.

#### Every proper actual-orbit bridge cut requesting `2` self-caps

On the simultaneous boundary, \(T=B\), so the actual output from \(G\)
to \(F\) is \(BT=B^2\). For \(0\le i<r\), put

\[
A_i=B[0:i],\qquad
G_i=G\,A_i=LR^2A_i,\qquad
M_i=M\,A_i=LR^2B A_i.
\]

In the general bridge notation, \(G_i=K_i\) and
\(M_i=K_{r+i}\). Hence the two indexed families form the exact disjoint
list of all proper bridge-generation cuts \(K_h\), \(0\le h<2r\):
the first half has \(h=i\), and the second has \(h=r+i\).
These are the cuts before the two occurrences of the bridge symbol
\(B[i]\). The actual-orbit recurrence, rather than the static occurrence
of that symbol in \(B\), gives

\[
\boxed{\kappa(G_i)=B[i]=\kappa(M_i).}
\]

Because \(A_i\) is a prefix of both \(B\) and \(R\), write

\[
R=A_iC_i,\qquad B=A_iD_i.
\]

The two bridge halves then have the literal circular-square
factorizations

\[
\boxed{
\begin{aligned}
R^2A_i
  &=A_iC_iA_iC_iA_i
   =A_i(C_iA_i)^2,\\
B^2A_i
  &=A_iD_iA_iD_iA_i
   =A_i(D_iA_i)^2.
\end{aligned}}
\tag{C.35y}
\]

The displayed roots \(C_iA_i\) and \(D_iA_i\) have lengths \(q\) and
\(r\), respectively. If the actual cut requests \(B[i]=2\), then the
two full-state curling numbers in the preceding box are exactly two.
Consequently each displayed square attains the maximal suffix exponent,
and the definition of the least maximizing root length gives

\[
\boxed{
B[i]=2
\Longrightarrow
\pi(G_i)\le q<P,\qquad
\pi(M_i)\le r<P.
}
\tag{C.35z}
\]

This includes \(i=0\), where \(A_0\) is empty,
\(G_0=G\), and \(M_0=M\). The identity at \(M_0\) is the \(B^2\)
square used in (C.35x). If the first family is extended to \(i=r\),
then \(G_r=M_0\), so the midpoint is one state rather than two.
The final proper cut \(i=r-1\) is also included. After the second copy of
\(B\) is complete, \(K_{2r}=F\). It is not a proper bridge-generation
cut, and paired generation gives
\(\kappa(F)=U[0]=Q[0]=3\), so it is not an omitted `2`-cut.

No negation of either G2CS target was used. More precisely,
\(G_i=S_{m+i}\) and \(M_i=S_{m+r+i}\), where \(m=q-r\).
For \(i<r\), both continuation coordinates are below \(2q\).
The direct inequalities in (C.35z) therefore verify the period hypothesis
of (C.28), which may now localize every such `2`-cut even when the state
is omitted from \(\mathcal I\). This order is essential: the application
of (C.28) at these cuts is licensed by the direct cap here; (C.28) is not
being used to prove that cap.

The result supplies only upper bounds. The displayed rotations need not
be canonical roots, and no equality with \(q\) or \(r\) is claimed
except for the separately known \(\pi(G)=q\). At a cut requesting `3`,
the visible square proves only a lower bound on the exponent; it supplies
none of the `3`-cut conclusions reserved for the rest of D-035.

#### Capped first-half `3` cuts give proper circular cubes of \(R\)

Fix \(0\le i<r\), retain

\[
A_i=B[0:i],\qquad R=A_iC_i,\qquad B=A_iD_i,
\]

and suppose the actual first-half cut requests `3` and is capped:

\[
\kappa(G_i)=B[i]=3,\qquad h=\pi(G_i)<P=q+r.
\]

Let \(Y_i^3\) be its canonical suffix cube, with \(|Y_i|=h\), and put

\[
Z_i=R^2A_i.
\]

Thus \(Z_i\) is the visible length-\((2q+i)\) suffix of \(G_i\), and it
has period \(q\).

First suppose \(h>q\), and write \(h=q+u\). The cap gives
\(0<u<r\). Since \(i<r<q/2\),

\[
3h>3q>2q+i=|Z_i|.
\]

Hence all of \(Z_i\) lies in the terminal \(h\)-periodic cube. For
\(0\le x<q-u\), period \(q+u\) on its first two displayed copies of
\(R\) gives

\[
R[x]=Z_i[x]=Z_i[x+q+u]=R[x+u].
\]

Thus \(R\) has period \(u<r<q/2\). Its final \(2u\) letters form a
\(u\)-square ending at \(G\). Because \(\kappa(G)=2\), this is a
maximizing square witness and forces
\(\pi(G)\le u<q\), contrary to \(\pi(G)=q\). Therefore \(h\le q\).

Equality also fails, but here the actual bridge chronology is
load-bearing. If \(h=q\), the final length-\(q\) block of \(G_i\) is

\[
Y_i=C_iA_i.
\]

The identity \(R=BQB=A_iD_iQB\) lets us write
\(Y_i=D_iV_i\), where \(V_i=QBA_i\). The word \(D_i\) is nonempty
because \(i<r\), and it is exactly the remaining output that carries
\(G_i\) to the midpoint \(M=G_iD_i\). But then

\[
Y_i^3D_i=(D_iV_i)^3D_i=D_i(V_iD_i)^3,
\]

so \(M\) ends in a cube and \(\kappa(M)\ge3\). Actual generation of the
second copy of \(B\) instead gives
\(\kappa(M)=B[0]=2\), a contradiction. Consequently

\[
\boxed{h<q.}
\tag{C.35aa}
\]

It remains to show that the cube is genuinely circular rather than
rescued by the unknown left context. Suppose \(Y_i^3\) crossed the left
edge of \(Z_i\). Since both words end at the same cut, this would mean
\(3h>2q+i\), so all of \(Z_i\) would inherit period \(h\). Put
\(g=\gcd(h,q)\). The word \(Z_i\) would then have periods \(h,q\), and

\[
|Z_i|=2q+i\ge2q\ge q+h-g.
\]

Fine--Wilf would give period \(g\) on \(Z_i\), hence on its prefix \(R\).
But \(g\mid q\) and \(g<q\), so \(R\) would be a proper \(g\)-power.
The suffix \(R^2\) of \(G\) would then have exponent
\(2q/g\ge4\), contradicting \(\kappa(G)=2\). Therefore

\[
\boxed{
3h\le2q+i,\qquad
\operatorname{suf}_{3h}(R^2A_i)=Y_i^3,\qquad h<q.
}
\tag{C.35ab}
\]

The word \(R^2A_i=R^2R[0:i]\) is the factor of the periodic word
\(R^{\mathbb Z}\) ending at circular phase \(i\). Thus the canonical
cube in (C.35ab) is a proper circular cube of \(R\): it lies wholly in
that periodic word and its root is strictly shorter than \(R\).

The endpoint \(i=0\) is vacuous because \(B[0]=2\); \(i=r-1\) is
included, with \(D_i\) a single symbol. For \(r=1\) there are no
first-half `3` cuts. No target negation or application of (C.28) was
used. Under the \(\mathcal J\)-negation every proper bridge state is
capped, so the conclusion applies at all first-half `3` cuts. Under the
\(\mathcal I\)-negation an interior first-half `3` cut is omitted and
the cap remains an explicit conditional hypothesis.

The midpoint label cannot be replaced by a merely local word condition.
For example,

\[
r=2,\quad B=23,\quad Q=32,\quad R=233223,\quad
i=1,\quad L=33223
\]

gives

\[
(\kappa(G),\pi(G))=(2,6),\qquad
G_1=(332232)^3,\qquad
(\kappa(G_1),\pi(G_1))=(3,6).
\]

Thus \(h=q=6<P=8\) satisfies the weakened local premises. Completing
the first \(B\), however, gives
\(\kappa(M)=3\), not the required \(B[0]=2\). This is a countermodel
only to the weakened static statement, and confirms why the actual
midpoint recurrence is essential above.

#### Capped second-half `3` cuts have no root longer than \(B\)

Fix \(0\le i<r\), put

\[
A_i=B[0:i],\qquad D_i=B[i:r],\qquad
M_i=LR^2B A_i,
\]

and suppose the actual second-half cut requests `3` and is capped:

\[
\kappa(M_i)=B[i]=3,\qquad h=\pi(M_i)<P=q+r.
\]

Let \(Y_i^3\) be its canonical suffix cube, with \(|Y_i|=h\), and
write

\[
Z_i=B^2A_i=A_i(D_iA_i)^2,\qquad |Z_i|=2r+i.
\]

Thus \(Z_i\) is the visible suffix of \(M_i\) supplied by the final copy
of \(B\) in \(R\), the first appended \(B\), and the prefix \(A_i\) of
the second appended \(B\). It has period \(r\).

We first exclude \(h>r\). There are two exhaustive placements.
Suppose first that

\[
h\ge r+i.
\]

Put \(E_i=BA_i\), so \(|E_i|=r+i\) and \(M_i=G E_i\). Since \(E_i\)
fits in the final canonical root, write \(Y_i=V_iE_i\). Deleting the
actual output \(E_i\) from the cube gives the suffix

\[
(V_iE_i)^2V_i=V_i(E_iV_i)^2
\]

at \(G\). Hence \(G\) ends in an \(h\)-root square. The exact pair
\((\kappa(G),\pi(G))=(2,q)\) makes this square maximizing, and therefore
\(h\ge q\). By the cap, write

\[
h=q+u,\qquad 0\le u<r.
\]

If \(u>0\), the \(h\)-square at \(G\) contains its suffix \(R^2\), which
therefore has period \(q+u\). Comparing the two displayed copies of
\(R\) gives

\[
R[x]=R[x+u]\qquad(0\le x<q-u).
\]

Thus \(R\) has period \(u<r<q/2\). Its final \(2u\) symbols form an
\(u\)-square ending at \(G\), so \(\pi(G)\le u<q\), a contradiction.

It remains in this placement to exclude \(u=0\), or \(h=q\). The
transferred square at \(G\) has root \(E_iV_i\), so its final
length-\(q\) block gives

\[
E_iV_i=R.
\]

The index \(i\) is positive because \(B[0]=2\), whereas this cut requests
`3`. Consequently position \(r\) exists in \(E_i=BA_i\), but

\[
E_i[r]=A_i[0]=B[0]=2,\qquad R[r]=Q[0]=3,
\]

contradicting the displayed prefix equality.

Now suppose instead that

\[
r<h<r+i.
\]

Since \(i<r\),

\[
3h>3r>2r+i=|Z_i|,
\]

so all of \(Z_i\) lies in the canonical \(h\)-periodic cube. Put
\(g=\gcd(h,r)\). The word \(Z_i\) has periods \(h,r\), and

\[
|Z_i|=2r+i>r+h\ge r+h-g.
\]

Fine--Wilf gives period \(g\) on \(Z_i\), hence on its prefix \(B\).
Here \(r<h<2r\), so \(g<r\); moreover \(g\mid r\). Thus \(B\) is a
proper \(g\)-power. But \(F=LR^2B^2\) ends in \(B^3\), which would then
have exponent \(3r/g\ge6\), contrary to \(\kappa(F)=3\). Both placements
are impossible, and therefore

\[
\boxed{h\le r.}
\tag{C.35ac}
\]

Suppose now that \(h<r\). If \(Y_i^3\) crossed the left edge of \(Z_i\),
then all of \(Z_i\) would again have periods \(h,r\). With
\(g=\gcd(h,r)\),

\[
|Z_i|=2r+i\ge2r\ge r+h-g,
\]

so Fine--Wilf would make \(B\) a proper \(g\)-power and contradict
\(\kappa(F)=3\) exactly as above. Therefore

\[
\boxed{
3h\le2r+i,\qquad
\operatorname{suf}_{3h}(B^2A_i)=Y_i^3,\qquad h<r.
}
\tag{C.35ad}
\]

The word \(B^2A_i=B^2B[0:i]\) is the factor of the periodic word
\(B^{\mathbb Z}\) ending at circular phase \(i\). Hence (C.35ad) is a
proper circular cube of \(B\).

The only remaining alternative is \(h=r\). In that case the final
length-\(r\) block is \(D_iA_i\), while the cube has length \(3r\) and
the visible word \(Z_i\) has length \(2r+i\). The full-root cube therefore
begins exactly \(r-i\) symbols before the left edge of \(Z_i\) and crosses
the displayed boundary

\[
\cdots BQ\mid B^2A_i.
\]

This is the exceptional full-root seam placement retained for the next
D-035 item. The exact suffix equation forced there, and the subsequent
restriction on \(i\), are not claimed here. In particular, no converse
from a seam equality to \(h=r\) is being used.

The endpoint \(i=0\) is vacuous because \(B[0]=2\); \(i=r-1\) is
included. For \(r=1\) there are no second-half `3` cuts. The cap is
load-bearing only in the deletion argument, where it gives \(h<q+r\).
No target negation or use of (C.28) is needed. Under the
\(\mathcal J\)-negation every proper bridge state is capped, whereas
under the \(\mathcal I\)-negation this second-half result remains
conditional at the omitted interior cuts.

#### The full-root seam forces the terminal bridge phase

Retain the actual binary second-half bridge and suppose that the exceptional
case above occurs:

\[
\kappa(M_i)=B[i]=3,\qquad \pi(M_i)=r,\qquad 0\le i<r.
\]

Put

\[
A_i=B[0:i],\qquad D_i=B[i:r],\qquad d=|D_i|=r-i.
\]

The canonical cube root is the final length-\(r\) block

\[
Y_i=D_iA_i.
\]

Because \(R=BQB\),

\[
M_i=LR^2BA_i=LR\,BQ\,B^2A_i.
\]

Moreover \(|BQ|=q-r>r\ge d\), while
\(d+|B^2A_i|=3r\). Hence the structural and canonical descriptions of
the final \(3r\) symbols are

\[
\operatorname{suf}_{3r}(M_i)
  =\operatorname{suf}_{d}(BQ)\,B^2A_i,
\qquad
Y_i^3=(D_iA_i)^3=D_iB^2A_i.
\]

Right cancellation of the common word \(B^2A_i\) gives the one-way seam
equation

\[
\boxed{
\operatorname{suf}_{r-i}(BQ)=D_i=B[i:r].
}
\tag{C.35ae}
\]

This establishes only \(h=r\Rightarrow\) seam. The equation alone does
not say that the displayed \(r\)-root is canonical.

The restriction on the phase uses the future actual bridge, not merely
the seam. For \(0\le t<d\), put

\[
C_t=D_i[0:t],\qquad V_t=D_i[t:d]A_i.
\]

Thus \(Y_i=C_tV_t\), and the actual remaining output gives
\(M_{i+t}=M_iC_t\). Rotating the existing cube yields

\[
Y_i^3C_t=(C_tV_t)^3C_t=C_t(V_tC_t)^3.
\tag{C.35af}
\]

Therefore every remaining proper cut \(M_{i+t}\) ends in a cube and has
curling number at least three. Actual bridge generation and the binary
alphabet give

\[
3\le\kappa(M_{i+t})=B[i+t]\le3
\qquad(0\le t<d).
\]

Consequently

\[
\boxed{
B[i:r]=3^{r-i},\qquad r-i\le\lambda.
}
\tag{C.35ag}
\]

Since \(i<r\), one has \(r-i\ge1\). In the surviving row (C.35l),
\(\lambda\le1\), so

\[
\boxed{
1\le r-i\le\lambda\le1
\quad\Longrightarrow\quad
i=r-1\ \text{ and }\ \lambda=1.
}
\tag{C.35ah}
\]

At this terminal proper cut, (C.35ae) reduces to
\(Q[-1]=B[-1]=3\). The completed state after appending that last `3` is
\(F=M_r\); it is not another indexed proper cut.

The future actual-orbit hypothesis is load-bearing. For a static
current-cut warning, take

\[
r=3,\qquad B=232,\qquad Q=332,\qquad
R=232332232,\qquad L=\epsilon,\qquad i=1.
\]

Definition-first calculation gives

\[
G=R^2:(2,9),\qquad M_i:(3,3),\qquad
F=R^2B^2:(3,3),
\]

and

\[
\operatorname{suf}_2(BQ)=32=B[1:3],\qquad
\lambda=0,\qquad i=1\ne r-1.
\]

This does not contradict (C.35ah): after the current `3` is appended,
the rotated cube still forces curling number three, whereas the proposed
next bridge symbol \(B[2]\) is `2`. The labels at the six static cuts
obtained from the proposed prefixes are `222233`, not the proposed output
\(B^2=\texttt{232232}\), so the word is not an actual bridge.

No cap, target negation, localization theorem, endpoint canonical data,
or \(p\)-branch is used once \(h=r\) and the numerical hypothesis
\(\lambda\le1\) are supplied. The binary alphabet and the actual
recurrence through every remaining proper bridge cut are essential. In
fact (C.33) already gives \(\lambda\le1\), because \(z\ge1\) and
\(\lambda+z\le2\); (C.35l) packages that bound in the surviving Cell C
row. As before, \(i=0\) is impossible because \(B[0]=2\), and \(r=1\)
is vacuous.

### 6. Exact remaining word obstructions

The stronger localization still does not close either period branch. It
gives different exact word residuals for the two targets.

For the stronger \(\mathcal I\)-only target, both branches share the forced
tuple

\[
q>2r>0,\quad P=q+r,\quad |B|=r,\quad
R=BQB,\quad U=QB,\quad B[0]=2,\quad Q[0]=3,
\]

and one of the two exact branch forms

\[
\begin{array}{ll}
p>q:&p=q+t,\quad r/2<t<r,\quad X=B[r-t:r]UB,\\[2mm]
p<q:&d=q-p>2r,\quad \nu=d-2r=|\Theta|>0,\quad
      X=Q[d:|Q|]B^2,\\
&Q[0:\nu+2r]=\Theta B^2,\quad
Q[|Q|-(r+\nu):|Q|]=B\Theta.
\end{array}
\]

In the \(p<q\) row, (C.24c)--(C.24e) additionally split the suffix seam as
\(D=JB\Theta\) or \(D=B[c:r]\Theta\) and put both in the common form
\(X=AC,\ U=CAH_0\). Each branch is combined with (C.35l) and the inherited
standalone conditions

\[
(\kappa(R^2),\pi(R^2))=(2,q),\qquad
\kappa(R^2B)=2,\qquad
(\kappa(BRB^2),\pi(BRB^2))=(3,r).
\]

The desired two-window replay must then realize

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

It remains to prove that no forced boundary word in either branch satisfies
(C.36), or to extract the required period-\(P\) witness. The interior
bridge is deliberately absent from the period inequalities in (C.36);
adding it would silently replace the stronger target by \(\mathcal J\).

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

The new \(p<q\) inequalities also have a nonvacuous sharpness model in the
exceptional range \(2p<P\):

\[
\begin{gathered}
q=20,\quad r=3,\quad p=11,\quad d=9,\quad P=23,\quad c=1,\\
B=232,\quad Q=33223223232332,\quad U=33223223232332232,\\
R=23233223223232332232,\quad X=32332232232.
\end{gathered}
\]

It has the exact static pairs

\[
\begin{array}{c|c}
\text{word}&(\kappa,\pi)\\
\hline
R^2&(2,20)\\
R^2B&(2,3)\\
BRB^2&(3,3)\\
X^3&(3,11)\\
X^3U&(2,20)\\
X^3UB^2&(3,3)\\
X^3UB^2U&(2,23).
\end{array}
\]

Moreover \(W=\operatorname{suf}_1(X)X^2\), \(B[0]=B[-1]\), and \(B\)
has period
\(r-c=2\), exactly as (C.28a) predicts. Its first-mismatch data are
\((z,h)=(2,1)\), with \(X[0:2]=32\) and \(B\) ending in \(2\).
Nevertheless it is not a survivor: at phase \(1\) of the later replay the
requested symbol is \(U[1]=3\), while the exact local pair is \((2,2)\).
Thus the static endpoint algebra, the shifted suffix, and the mismatch
trichotomy do not by themselves close the \(p<q\) word wall.

#### Equality-first \(p>q\) boundary checkpoint

`research/generated_two_cube_cell_c_pgtq_search.py` exhausts the exact
binary normal form above through \(q\le25\). Put
\[
C=U[0:q-2r],
\]
so \(U=CB\), with \(C[0]=3\). For every integer triple
\[
q>2r>0,\qquad r/2<t<r,
\]
the executable generates \(B\) from its first \(t\) coordinates, forces
\(B[0]=2\) and period \(t\), generates \(C\) from its first symbol, and then
forms
\[
U=CB,\qquad R=BU,\qquad X=B[r-t:r]UB.
\]
The exact deduplication key is \((q,r,t,B,U)\). A repeated word \(B\) at two
different values of \(t\) is deliberately retained because the early period
\(p=q+t\) is different.

The `220` integer triples would contain `1792552320` raw binary
root--parameter pairs. Structural generation reduces this to `2388798`
assignments. Exact filtering gives

```text
canonical R^2=(2,q)                 563708
kappa(R^2B)=2                       563708
canonical X^3=(3,p)                 563688
late exponent replay                    1
exact late replay with F=(3,r)          1
all proper late periods below P         0
terminal H=(2,P)                         1
early replay after the late filter       0
full autonomous continuation replay      0
I-window survivors                        0
J-window survivors                        0
```

The \(\mathcal I\)-survivor count requires both exact sampled replays, their
proper period caps, and the \(G,H\) endpoint scales. The
\(\mathcal J\)-survivor count independently requires exact replay of the
whole \(UB^2U\) continuation, all of its proper periods below \(P\), and the
terminal pair \((2,P)\). Full-continuation candidates may safely be checked
only after the exact late-window filter because full replay implies late
replay. There is no obsolete left-context-rescue category: the
all-continuation localization lemma converts either target's capped states
to the local words being checked.

The one exact late replay is the \(q=9\) sharpness word above. It has
\[
U=\operatorname{rot}_{\rm left}(B)B=322\,232.
\]
Its exact late pairs are
\[
(3,3),(2,2),(2,2),(2,1),(3,1),(2,12),
\]
and its terminal pair is \((2,12)\). Thus its final proper late state already
has \(\pi=P\). Its early pairs through \(G\) are
\[
(3,11),(3,11),(3,11),(2,1),(3,1),(1,38),(2,9),
\]
so phase \(1\) requests \(2\) while the displayed local suffix still has
value \(3\). It is not a full G2CS trace.

There is also an exact coordinate explanation for the final period-\(P\)
square. Put \(Y=B^2U\). The local terminal word ends in \(Y^2\), and the
symbol immediately before that shadow is \(C[-1]\). Consequently the final
proper state's last \(2P\) symbols are
\[
C[-1]\,Y^2[0:2P-1].
\]
Its two length-\(P\) blocks agree exactly when
\[
\boxed{C[-1]=Y[-1]=B[-1].}
\tag{C.38}
\]
For the \(q=9\) word both symbols are \(2\), and the square root is the
right rotation \(223223232223\) of \(Y\). Equality (C.38) is a coordinate
identity, not yet a proof that every unbounded survivor must close its
shadow or that \(P\) must be the shortest maximizing period.

As a separate diagnostic, the executable applies the complete
first-mismatch trichotomy (C.35), including the terminal-\(3\)-run inequality
\(\lambda+z\le2\), after the canonical filters. It retains `197773`
candidates:
`105851`, `45116`, and `46806` in the respective
\((z,h)=(1,0),(2,0),(2,1)\) rows. Every one fails exact early replay:
`71487` at phase `1`, `46843` at phase `2`, and `79443` at a later phase,
with no phase-`0`, endpoint-only, or completed cases. This is a bounded
static contradiction at the tested cap, not an unbounded argument.

An independent definition-first oracle enumerates all `3456` raw binary
root--parameter pairs through \(q\le10\). It finds the same `42` structural
tuples and the exact stage counts `7,7,7,1,0,1,0` for canonical \(R^2\),
standalone exponent two, canonical \(X^3\), exact late replay, late
period-cap survivors, terminal \(H\), and early replay after the late
filter. The deterministic \(q\le25\) artifact is
`research/outputs/generated_two_cube_cell_c_pgtq_scan_2026-07-27.txt`.
Its SHA-256 is
`8837CF352EA83B6F2195B17FFD222E42F831C7EA332827EC9C2D7A29F026B06E`.

The \(q=9\) continuation is the same finite-window phase-loss/context-rescue
shape isolated in `critical_seed_induction.md`: the suffix \(B^3\) begins
the requested replay, and the outer period-\(P\) shadow rescues the first
autonomous loss. This is a proof-strategy connection, not a reduction:
\(B=232\) has proper circular profile \((1,2,1)\), so it does not satisfy
the fixed-profile hypotheses of that note.

The target-specific word walls remain unproved in both period branches, as
do the non-boundary regions of (C.5)--(C.6). There is also no transfer of
the final Cell A argument: here
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

`tests/test_generated_two_cube_cell_c_pltq_reduction.py` separately
enumerates the exact static \(p<q\) boundary tuples through \(q\le14\)
without importing either production search. It retains `141` tuples. Every
one satisfies \(d>2r\), the \(\Theta B^2/B\Theta\) normal form, (C.24b),
and the
frontier equation. Across both possible exponents and all proper
continuation phases, it checks `3753` numerical slots in which a root below
\(P\) would have to cross the local boundary; none supplies the required
second period on \(X^3\).

The same test uses \(X^\omega\), rather than an out-of-range slice of \(X\),
for the first-mismatch comparison. There are `74` static tuples satisfying
the two necessary mismatch inequalities, split `41,21,12` across the three
rows of (C.35), and all obey the stated coordinate conclusions. The
\(q=20\) model above pins the nonempty \(2p<P\) case. These are bounded,
nonvacuous index checks only; the localization lemma and the inequalities
remain natural-language proofs, and the word walls remain open.

`tests/test_generated_two_cube_cell_c_double_three.py` adds a separate
definition-first regression for the new elimination. It imports neither
production Cell C search and recomputes every canonical witness by literal
suffix-block enumeration. Through \(q\le20\), the \(p>q\) generator checks
`73470` structural assignments and retains `2841` exact \(z=2\) candidates:
`1394` in row \((2,0)\) and `1447` in row \((2,1)\). Their \(F_1\)
exponents split respectively as

\[
\{1:399,\ 2:995\},\qquad
\{1:43,\ 2:1404\}.
\]

The independent \(p<q\) generator checks `34405` assignments and retains
`2016` exact \(z=2\) candidates: `1343` and `673` in the two rows. Their
\(F_1\) exponent splits are

\[
\{1:1090,\ 2:253\},\qquad
\{1:547,\ 2:126\}.
\]

The seam counts are `1343,672` for \(D=JB\Theta\) and `0,1` for
\(D=B[c:r]\Theta\). Thus all `4857` retained candidates are nonvacuous,
but zero has \(\kappa(F_1)=3\). These bounded counts independently audit
the theorem's coordinates; they are not its proof.

The surviving row also has an endpoint-correct sharpness model:

\[
\begin{gathered}
q=23,\quad r=4,\quad p=13,\quad P=27,\quad \nu=2,\quad c=1,\\
B=2232,\quad \Theta=32,\quad D=23232,\\
Q=322232223223232,\quad
U=3222322232232322232,\\
R=22323222322232232322232,\quad
X=2323222322232.
\end{gathered}
\]

It lies on the overlap seam \(D=B[c:r]\Theta\), has
\((z,h)=(1,0)\), and has exact static endpoint pairs

\[
R^2:(2,23),\quad R^2B:(2,4),\quad
BRB^2:(3,4),\quad X^3:(3,13),
\]

\[
X^3U:(2,23),\quad X^3UB^2:(3,4),\quad
X^3UB^2U:(2,27).
\]

Both sampled local traces replay the first `13` requested symbols. At phase
`13`, however, the request is \(U[13]=3\) while both exact local pairs are
\((2,3)\). The remaining row is therefore a genuinely later, nonlocal
replay obstruction: endpoint scales and a long common prefix do not close
it. This word is not a survivor or counterexample.

`research/generated_two_cube_cell_c_z1_atlas.py` now audits the surviving
row directly in both exact normal forms. It imports neither production
Cell C search and recomputes every canonical pair from the suffix-power
definition. Through \(q\le25\), the \(p>q\) branch enumerates `2388798`
structures, of which `595896` have the structural \(z=1\) coordinates and
`105851` pass every exact static canonical filter. At phase one their label
table is

\[
\begin{array}{c|r}
\text{outcome}&\text{count}\\ \hline
E_1,F_1\text{ both label }2&79471\\
E_1\text{ only labels }2&9\\
F_1\text{ only labels }2&0\\
\text{neither labels }2&26371.
\end{array}
\]

All `79471` paired label-two cases obey the low alternative
\(\alpha=\beta<r<P\); none is unclassified. The first replay failures in
the two windows are synchronized in `105838` static candidates and differ
in `13`. The first post-phase-zero root divergence occurs at the first
failure in `43471` cases and after it in `62380`; none occurs before it.
All `105851` literal early and late endpoints have the exact pairs
\((2,q)\), \((2,P)\), but only `29416`, `64641`, and `28724` candidates
have the early, late, and both predecessor labels required for generation.

The \(p<q\) branch enumerates `1115405` structures, with `418622`
structural \(z=1\) rows and `100053` exact static candidates. Its phase-one
label table is

\[
\begin{array}{c|r}
E_1,F_1\text{ both label }2&61200\\
E_1\text{ only labels }2&32800\\
F_1\text{ only labels }2&507\\
\text{neither labels }2&5546.
\end{array}
\]

Among the `61200` paired cases, `6555` are equal/local and `54645` are
different/context-crossing; again none violates (C.35p). Exactly `93493`
static candidates have \(r=1\), including all `54645` paired high cases.
The generic seam contributes `100050` static candidates, while the overlap
seam contributes exactly `3`. First failures synchronize in `46364`
static candidates and differ in `53689`. Root divergence occurs before,
at, and after the first failure in `54780`, `45268`, and `5` cases.
Every early endpoint has pair \((2,q)\); `99934` late endpoints have
\((2,P)\). The predecessor label counts are `91133`, `13138`, and `13128`.

Every static candidate in both branches fails at least one literal replay
phase within the bound. This is `COMPUTED` evidence only. In particular,
the atlas also pins why stronger informal statements are false:

- the \(q=8,r=1,p=5\) word has
  \(E_1:(2,3)\), \(F_1:(2,4)\), and a noncanonical late endpoint
  \((2,5)\);
- the endpoint-correct \(q=9,r=1,p=6\) word has the same high phase-one
  split and replays phases `0` through `3` before both fail at phase `4`;
- the \(q=11,r=1,p=8\) word fails early at phase `3` and late at phase `5`;
- the \(q=16,r=2,p=10\) word has the common phase-one pair \((2,1)\), then
  different valid phase-two pairs \((2,6)\), \((2,8)\), before both fail
  at phase `3`;
- the \(q=23\) overlap model above first fails at phase `13`;
- the exact high static model
  \[
  q=29,\ r=4,\ p=20,\ P=33,\quad
  B=2332,\quad\Theta=3,\quad D=233233223323
  \]
  has \(E_1:(2,9)\), \(F_1:(2,20)\), exact endpoint pairs
  \((2,29),(2,33)\), and fails both windows at phase `2`.

The deterministic artifact
`research/outputs/generated_two_cube_cell_c_z1_atlas_2026-07-27.txt`
was generated twice with LF-stable, byte-for-byte identical output in
`43.451` and `43.523` seconds. Its SHA-256 digest is
`975E542B6AEF428B39C087095BCB0A77AD68E390D597CC21F1FB43DA72BCEFE9`.
The artifact and all six certificates are bounded audits, not a proof that
the remaining row is impossible.

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
