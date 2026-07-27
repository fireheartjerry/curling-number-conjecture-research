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

These include every equality boundary. In particular, \(j=0\) is allowed in
the first line and gives the endpoint equality \(D=N\).

### 2. Equality-first exhaustive engine

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
\tag{C.7}
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

### 3. Bounded result through \(|E|\le18\)

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
