# Literature-first search log

Search started: 2026-07-23.  This log records sources checked before new
lemma work.  Queries deliberately seek reusable results and prior reductions,
not a complete solution of the Curling Number Conjecture.

## Direct curling-number literature

Queries:

* `site:arxiv.org/abs/0912.2382 curling number conjecture Chaffin Sloane`
* `site:arxiv.org/abs/1212.6102 On Curling Numbers of Integer Sequences`
* `site:cs.uwaterloo.ca/journals/JIS curling numbers integer sequences Chaffin Linderman Sloane Wilks`
* `site:oeis.org A094004 curling number A090822 references`
* `"A Grammatical Approach to the Curling Number Conjecture"`
* `site:williams.edu Duane Bailey curling number grammar Bonafilia Liu Poudyal Templeton Timilsina`

Primary sources checked:

* B. Chaffin and N. J. A. Sloane, *The Curling Number Conjecture*,
  arXiv:0912.2382, <https://arxiv.org/abs/0912.2382>.
* B. Chaffin, J. P. Linderman, N. J. A. Sloane, and A. R. Wilks,
  *On Curling Numbers of Integer Sequences*, Journal of Integer Sequences
  16 (2013), Article 13.4.3,
  <https://cs.uwaterloo.ca/journals/JIS/VOL16/Sloane/CNC.pdf>.
* OEIS A094004 and A090822 and linked references,
  <https://oeis.org/A094004>, <https://oeis.org/A090822>.
* L. van de Pol, *The first occurrence of a number in Gijswijt's
  sequence*, arXiv:2209.04657, <https://arxiv.org/abs/2209.04657>.

Findings adopted:

1. Chaffin--Linderman--Sloane--Wilks Lemma 4: if `cn(S)=k`, the shortest
   root `Y` in a maximizing representation `S=XY^k` is unique and primitive;
   its curling number is `<k` for `k>1` and is `1` for `k=1`.  This supersedes
   any independently rederived shortest-root assertion.
2. Their Theorem 5 states the Fine--Wilf common-suffix form: if powers
   `X^i` and `Y^j` share a suffix of length at least
   `|X|+|Y|-gcd(|X|,|Y|)`, both roots are powers of a word of length the gcd.
3. Their Theorem 6: if primitive `S` of curling number `k` is non-robust and
   `S^(k+1)` has a proper `(k+1)`-power suffix, that suffix already lies in
   `S^2`.  Their Theorems 18--19 give a unique `S=X(TX)^k` normal form in
   the non-robust `k>1` case.
4. Their Theorems 9--10 are particularly relevant to the new terminal-prefix
   route.  If `cn(S)=1` but prefixing `S` by a proper suffix `T` of `S`
   raises its curling number, then `S` has a canonical form `S=XYX`, with
   `cn(X)=1` and the stated suffix relations; two distinct such decompositions
   would force `cn(S)>1`.  Theorem 13 refines a second extension and proves
   an explicit alternative between equal scale and a factor-greater-than-two
   scale gap.  We will use these theorems whenever a circular crossing can be
   converted to their suffix-prefix hypotheses rather than reprove them.
5. Section 2.5 mentions Shirshov and Lyndon decompositions as possible
   unavoidability routes but records no contradiction.  Searches within both
   curling papers found no rotation, minimal-nonterminating-seed, deleted-last-
   symbol, circular fixed-profile, or self-encoded cube-endpoint theorem.
6. The 2013 paper states that even the binary `{2,3}` case remained open at
   publication and asks whether Shirshov's theorem can be modified for it.
   This is status/context, not a load-bearing mathematical premise.
7. The 2018 Duane Bailey item located is a six-minute Gathering for Gardner
   talk described only as relating the conjecture to aperiodic grammars.  No
   archival paper, theorem statement, or proof was located in this search, so
   nothing from it is presently reusable.
8. Van de Pol's work proves exact first-occurrence results for the special
   level-`m` Gijswijt sequences.  Its hypotheses concern those recursively
   structured sequences, not arbitrary seeds or the critical circular word;
   no transfer theorem was found.

## Repetitions, circular words, and partial-word periodicity

Queries:

* `combinatorics on words circular squareful words every position begins square theorem`
* `squareful words minimal squares Saari`
* `characteristic sequence positions where cubes occur word encodes repetitions`
* `"cube positions" infinite word combinatorics`
* `"cube endpoints" word combinatorics`
* `"positions at which a cube ends" word`
* `one hole periodicity theorem word combinatorics Fine Wilf partial words one mismatch`
* `site:arxiv.org periodicity lemma word with one hole Fine Wilf`
* `critical factorization theorem local period precise statement`
* `runs theorem periodicity overlap squares cubes word endpoints`

Primary sources and precise scope are recorded in
`research/literature_terminal_prefix.md`.  The immediately reusable results
are Fine--Wilf and, only after a genuine common partial word with specified
periods has been constructed, the partial-word periodicity theorem.  The
squareful-word, runs, and critical-factorization results do not encode cube
endpoints and therefore do not imply the target terminal-prefix lemma.

Additional source checked:

* N. Rampersad, *Prefixes of the Fibonacci word that end with a cube*,
  C. R. Math. 360 (2022), arXiv:2111.09253,
  <https://arxiv.org/abs/2111.09253>.  It characterizes cube-ending positions
  in the fixed Fibonacci word using Walnut.  It does not study a word that is
  itself the characteristic sequence of its cube-ending positions.

Further exact searches for the fixed-indicator subproblem were:

* `site:arxiv.org word equals its cube occurrence indicator sequence combinatorics on words`;
* `site:arxiv.org power occurrence indicator word cubes borders periodicity`;
* `site:arxiv.org binary word self descriptive cube positions circular word`;
* `site:arxiv.org periodic word cube ending positions indicator`.

The only close primary source located was J. Bell, C. Schulz and
J. Shallit, *Consecutive Power Occurrences in Sturmian Words*,
arXiv:2402.09597.  It bounds gaps between cube-ending positions in
Sturmian words; it neither treats circular finite words nor identifies
the letters of a word with its own cube-ending indicator.  No searched
source supplies the `A V A` fitting-overlap lemma proved in
`research/ava_fixed_inheritance.md`.

## Novel-work boundary after the first audit

No searched source contains the current central object: a finite binary
circular word `P` with `P[j]=3` exactly when a proper circular cube ends at
cut `j`, together with a distinguished terminal circular square and a strict
finite-prefix curling drop.  Accordingly, the circular terminal-prefix lemma
remains a novel-proof target in this project.  Priority is stated only as
"not found in the recorded search", not as a certified first discovery.

## Overlap results checked for the canonical `A V A` branch

Before extending the same-scale and strict-scale cases in
`research/ava_fixed_inheritance.md`, these searches were run:

* `site:arxiv.org combinatorics on words three squares lemma overlapping cubes same period extension`
* `site:hal.science word equations overlapping cubes periodicity lemma three squares`
* `site:doi.org runs in strings two overlapping cubes Fine Wilf lemma`

The relevant primary result located was H. Bannai, T. Mieno and
Y. Nakashima, *Lyndon Words, the Three Squares Lemma, and Primitive
Squares*, arXiv:2006.13576.  Its generalized Three Squares Lemma constrains
three overlapping primitively rooted squares.  The present residual has one
distinguished wrapping square and a cube selected by a letter/cube endpoint
equivalence, with a pointed first prefix/suffix mismatch.  The published
theorem does not supply that conclusion, and local `A V A` words satisfy the
bare overlap equations.  Fine--Wilf remains reusable; the mismatch descent
requires an additional argument.

## Squareful-word classification check

Before attempting to classify the inherited binary cube-indicator word in
the canonical `A V A` branch, the following searches were run:

* `binary infinite squareful words every position begins with a square classification Saari Peltomaki`
* `optimal squareful words six minimal squares classification binary squareful words`
* `periodic squareful words minimal squares Fraenkel Simpson theorem`
* `site:arxiv.org squareful words every position begins a square binary`
* `Kalle Saari squareful words periodic classification minimal squares thesis theorem`
* `"periodic squareful" word combinatorics`

The primary/research sources located were K. Saari, *Everywhere
alpha-repetitive sequences and Sturmian words* (European J. Combin. 31
(2010), 177--192); J. Peltomaki and M. Whiteland, *A square root map on
Sturmian words* (EJC 24(1) (2017), P1.54); their follow-up
arXiv:1801.00920; and J. Currie and N. Rampersad, *Infinite words
containing squares at every position* (RAIRO 44 (2010), 113--124,
arXiv:0803.1189).  Saari's classification of **optimal aperiodic**
squareful words describes the six minimal square roots and implies that an
aperiodic squareful word with at most five minimal squares cannot exist.
Those results do not classify periodic squareful words by their cube-endpoint
indicator, and they do not force the canonical `A V A` seam to disappear.
They therefore remain background rather than a load-bearing shortcut.

The conditional seam-forcing lemma proved during the final-`3` audit was not
found in these sources.  Its proof is valid under the additional hypotheses
`cn(X)=cn(AX)=1` and `|A|<|X|`, but the audit later showed that those
hypotheses do not follow from the upstream canonical form.  It is therefore
not presently a closing lemma for the full final-`3` branch.

## Square-to-cube overlap and run search

Before extending the primitive square-to-cube child lemmas, these searches
were run:

* `combinatorics on words square followed later cube same endpoint primitive square cube overlap lemma`
* `word equation XHXHX cube square overlap primitive root theorem`
* `Crochemore Rytter three squares lemma exact statement primitive squares`
* `runs theorem square cube maturation adjacent endpoints word combinatorics`

The relevant sources found were again Bannai--Mieno--Nakashima,
arXiv:2006.13576; Crochemore and Rytter, *Squares, cubes, and time-space
efficient string searching* (Algorithmica 13 (1995)); and Bannai et al.,
*The Runs Theorem*, arXiv:1406.0263.  The classical Three Squares Lemma
separates three primitively rooted squares with a common start (and the
generalized version permits specified overlaps).  The Runs Theorem bounds
the number/sum of runs.  Neither theorem supplies the pointed conclusion
needed here: a self-labelled `2` midpoint and `3` endpoint with a
first-copy fitting cube, or preservation of that labelled maturation under
the smaller `X(HX)^2` decomposition.  Fine--Wilf and the period-difference
lemma remain the directly reusable ingredients.

## Border and nested-square follow-up

Before continuing the bordered-root quotient and the final-`3` short-border
case, the following additional searches were run:

* `site:arxiv.org curling number integer sequences primitive word robust 2013..2026`
* `site:arxiv.org combinatorics words three squares lemma nested square cube primitive border overlap`
* `site:arxiv.org bordered primitive word conjugate fourth power overlap theorem`
* `site:doi.org "curling number" sequence combinatorics`

No post-2013 primary curling-number theorem located by these queries
strengthens the CLSW robust/non-robust normal forms used above.  The useful
precise statement recovered from Bannai--Mieno--Nakashima,
arXiv:2006.13576, Lemma 1, is: if `u^2`, `v^2`, and `w^2` are three prefixes
of one word, `w` is primitive, and `|u|>|v|>|w|`, then
`|u|>=|v|+|w|`.  Their Corollary 2 extends this to a specified nesting of
overlapping squares via L-root intervals.  This can certify scale gaps once
three square occurrences have the required common/nested geometry, but it
does not itself supply the labelled midpoint, the cube endpoint, or the
first-copy fitting inheritance in the present child nodes.

Daniel Gabric, *Mutual Borders and Overlaps*, arXiv:2010.14663, was also
checked.  Its results enumerate and estimate mutually bordered pairs; they
do not classify a primitive bordered word carrying the exact binary
square/cube endpoint profile used here.  Accordingly the Euclidean border
normal form in the live proof remains a direct word-equation derivation,
not an invocation of that paper.

## Deleted-prefix curling numbers and immediate pure powers

Before building on the minimum-deleted-hitting-time reduction, these
searches were run:

* `site:arxiv.org curling number conjecture deleting first term primitive power suffix`
* `site:cs.uwaterloo.ca Journal Integer Sequences curling number prefix suffix theorem`
* `"curling number" "primitive" sequence word`
* `"curling number" suffix deletion`

The relevant published local fact is Theorem 7 of Chaffin--Linderman--
Sloane--Wilks, *On Curling Numbers of Integer Sequences*, JIS 16 (2013),
Art. 13.4.3 / arXiv:1212.6102: prefixing a single symbol changes the
curling number from `k` to either `k` or `k+1`.  The proof of their
Theorem 8 also isolates the strict case as a whole power `S=V^k` and
uses primitivity/robustness to count it.  We therefore adopt that local
one-step result instead of presenting it as new.

What was not found in the queried literature is the dynamical selection
step: among pairs `A` bad and `A[1:]` terminating, minimize the latter
orbit's first-one hitting time.  Equality of the first outputs would
advance both states while preserving deletion and lower that hitting
time, so the selected pair must diverge immediately.  Combined with
CLSW Theorem 7 (and their whole-power case), this yields the immediate
primitive-power normal form.  Until a wider literature audit or expert
review, only this hitting-time selection should be described as "not
found in the searched literature," not categorically as new.

## Robust square roots and square-prefix literature

Before treating the `tau=0` specialization as a new word class, these
queries were run:

* `Gabric Shallit Borders Palindrome Prefixes Square Prefixes theorem square no proper prefix square`
* `infinite word infinitely many primitive square prefixes classification`
* `"infinitely many square prefixes" word`
* `Sturmian word square prefixes characterization`

The `tau=0` normal form `A=Y^2`, `cn(A[1:])=1` is exactly the robust
primitive curling-one class already counted by CLSW: every proper suffix
of `Y^2` lies in `A[1:]`, hence has curling number one.  OEIS A216958 is
the first column of A218875 and records the equivalent reversed formulation
as squares of length `2n` having no proper square prefix.

Daniel Gabric and Jeffrey Shallit, *Borders, Palindrome Prefixes, and
Square Prefixes*, Information Processing Letters 165 (2021), 106027,
arXiv:1906.03689, prove the corresponding 2013 enumeration conjecture by
a bijective relation with border data.  Their result supplies enumeration,
not a termination theorem for the orbit of such a square, so it does not
close the protected-power branch.

The wider search also confirmed that infinitely many nested square
prefixes are not a periodicity certificate: every Sturmian word has
infinitely many square prefixes (see the initial-critical-exponent
literature, e.g. Damanik--Lenz and later surveys), and the square-root-map
literature of Peltomaki--Whiteland studies aperiodic words factorized into
minimal squares.  Accordingly, the live reset-tower argument must use the
numeric self-label equations, not merely the existence or scale growth of
nested square prefixes.

For the subsequent whole-prefix reset tower, the classical Three Squares
Lemma is the strongest directly applicable published spacing result.  In
the prefix form used by current string-indexing literature: if primitive
square prefixes have root lengths `w<v<u`, then `u>v+w`.  Thus a word has
only logarithmically many primitive square prefixes up to any fixed length.
This gives Fibonacci-scale growth for reset roots, but not termination:
aperiodic Sturmian words supply infinite nested square-prefix phenomena.
No searched source classifies nested primitive power prefixes whose
following symbol is numerically equal to the exact maximal exponent, which
is the extra orbit constraint here.

## Orbit-compatible hidden-reset transitions

Before classifying the first transition between two successive whole-prefix
resets, these additional searches were run:

* `site:arxiv.org combinatorics on words nested primitive power prefixes prescribed following letters periods Fine Wilf`
* `site:arxiv.org combinatorics on words runs consecutive primitive power prefixes exponent labels`
* `site:hal.science word equations prefix square extension orbit deterministic sequence periods`
* `site:doi.org combinatorics words square prefixes following letter primitive root transition`

The searches recovered general sources on primitive roots, runs, gapped
repeats, and Fine--Wilf-type period extraction, including Crochemore et al.,
*Extracting powers and periods in a word from its runs structure*, TCS 521
(2014), 29--41.  None located a theorem about a word-generated dynamical
rule in which each appended letter must itself equal the maximal suffix
exponent of the prefix.  Consequently the overlap geometry continues to use
standard period lemmas, while compatibility with the curling orbit is a
separate project-specific condition.  This is only a record of the searched
sources, not a priority claim.

## Circular fixed profiles at hidden cube-reset seams

Before encoding the exact late hidden-reset equations, the following
curling-number-specific searches were run:

* `"curling number" periodic word fixed point circular`
* `"curling number" primitive word circular shifts`
* `"curling number" self describing word suffix powers`
* `site:cs.uwaterloo.ca "curling number" robust primitive word`

The searches recovered the two Chaffin--Sloane papers, the Gijswijt
fixed-point literature, and van de Pol's 2025 JIS paper.  They did not
locate a published classification of finite primitive circular words
whose symbol at every cut is their exact maximal proper-root exponent,
nor a transition theorem for two such words related by
`V=U^2 U[:h]`.  The resulting finite solver is therefore being used as
an exploratory classifier, with no novelty or completeness claim beyond
its stated bounded search.

## Power-free block codings for bounded reset defects

After internal cube resets were reduced to a finite set of seed-anchored
defect lengths, these searches checked whether a general theorem forbids
an infinite cube-free concatenation of the associated prefix blocks:

* `combinatorics on words infinite cube-free concatenation finite set nested prefix words`
* `morphism images of cube-free words prefix-related code power-free`
* `finite set of prefixes infinite concatenation cube-free theorem`
* `site:arxiv.org power-free morphism prefix code nested prefixes words`

The literature points the other way at the level of bare block codings.
Richomme--Wlazinski, *Some results on k-power-free morphisms*, TCS 273
(2002), gives finite test sets for binary cube-free morphisms, and later
work constructs many power-free binary morphisms.  Infinite binary
cube-free words therefore prevent treating “finitely many defect block
types” as a contradiction by itself.  The live argument must retain the
pointed labels, exact maximal exponents, and the reset-child equations;
ordinary cube avoidance of the defect code is insufficient.

## Increasing hidden defects and co-terminal primitive squares

Before trying to turn the `a<d<h` carrier event into a new overlap
theorem, the following targeted ordinary-combinatorics queries were run:

* `combinatorics on words two overlapping powers periodicity theorem primitive roots overlap critical factorization theorem`
* `runs theorem three squares lemma combinatorics on words Crochemore Rytter primitive squares overlap`
* `Lyndon Schutzenberger equation overlapping squares cube primitive word theorem`
* `periodicity lemma word has border u and square suffix primitive root Fine Wilf overlap`

The strongest directly relevant result located was the Three Squares
Lemma, restated as Lemma 1 of Bannai, Mieno and Nakashima,
*Lyndon Words, the Three Squares Lemma, and Primitive Squares*,
SPIRE 2020, arXiv:2006.13576:

> If `u^2`, `v^2`, and `w^2` are prefixes of one word, `w` is primitive,
> and `|u|>|v|>|w|`, then `|u|>=|v|+|w|`.

Their paper also gives a variant for three overlapping squares which do
not share a common start.  These theorems require three simultaneous
square occurrences.  At one increasing-defect maturation the available
data are only the co-terminal primitive square `D^2` and the square
inside one maximizing cube `R^3`; the old reset-scale square has already
been broken by the promoted marker.  Thus the theorem does not by itself
exclude the locally realized rescue cases `d<r<2d` or `r>=2d`.

Lothaire, *Algebraic Combinatorics on Words*, Chapter 8 (Cambridge
University Press, 2002), confirms that the standard tools at this
generality are Fine--Wilf, its three-period variants, and critical
factorization.  The Archive of Formal Proofs entry by Holub, Raška and
Starosta, *Combinatorics on Words Basics* (2021), contains machine-checked
versions of the Periodicity Lemma and Lyndon--Schützenberger word
equations.  Neither source supplies the missing dynamical closure from a
contexted cube root `R` back to a prefix reset/carrier.  The literature
therefore supports the exact scale inequalities already used, but does
not remove the need for a project-specific argument using the
fixed-profile child and orbit provenance.

## Golden-suffix periodicity and squareful words

Before attempting to convert the fact that every counterorbit prefix ends
in a square into ultimate periodicity, the following searches were run:

* `Mignosi Restivo Salemi ultimately periodic each sufficiently long prefix repetition phi+1 suffix exact theorem pdf`
* `Mignosi Restivo Salemi left repetitive sequences theorem golden ratio suffix prefix`
* `squareful words every position begins with a square classification Sturmian Saari`
* `infinite words containing squares at every position`

Mignosi--Restivo--Salemi, *Periodicity and the Golden Ratio*, TCS 204
(1998), 153--167, proves that a right-infinite word is ultimately periodic
iff every sufficiently long prefix has a suffix of exponent at least
`phi^2=(3+sqrt(5))/2`.  A curling number of two supplies exponent two,
not `phi^2`; therefore this theorem does not turn the conjecture into an
immediate periodicity result.  It does justify the existing reduction to
infinitely many `phi^2`-deficient ("golden-bad") cuts in any hypothetical
counterorbit.  Saari's squareful-word results likewise allow aperiodic
words with bounded square witnesses (Sturmian examples); his stronger
ultimate-periodicity criterion applies at exponent `phi+1`, not at two.

## Gijswijt block/glue structure versus arbitrary critical roots

Before trying to identify an external reset tower with a level-2 Gijswijt
construction, the following searches were run:

* `van de Pol Gijswijt sequence curling number block glue theorem`
* `van de Pol Gijswijt curling sequences higher order blocks glue strings`
* `Gijswijt sequence arbitrary initial block glue sequence theorem`
* `curling number generalized Gijswijt sequence arbitrary seed attractor`

Van de Bult--Gijswijt--Linderman--Sloane--Wilks, *A Slow-Growing Sequence
Defined by an Unusual Recurrence*, JIS 10 (2007), proves unboundedness for
the canonical level-`m` sequences and their specific recursively defined
blocks and glue strings.  Van de Pol's 2022/2025 work sharpens first
occurrence and growth estimates for those same canonical sequences.  No
searched theorem transfers the block/glue recursion to an arbitrary
self-replaying critical word or arbitrary initial seed.  Van de Pol's
2025 paper explicitly says its techniques are unsuitable for the Curling
Number Conjecture.  Consequently canonical unboundedness may be used only
after an explicit transfer theorem; resemblance of an external reset
`V` beginning `U^3 3` to a canonical block is not such a theorem.

## Periodic squareful profiles and later direct searches

Searches performed on 2026-07-22 included the phrases `periodic squareful
words every position begins square classification`, `circular word every
position starts square shorter than period`, `consecutive positions ending
in cubes`, and direct searches for post-2013 work on the Curling Number
Conjecture.

Saari's squareful-word results, as summarized and used by Peltomaeki and
Whiteland in *A Square Root Map on Sturmian Words* (Electronic Journal of
Combinatorics 24 (2017), P1.54), classify **optimal squareful** words only
after imposing aperiodicity and the minimum possible number of distinct
minimal squares.  Their definition and classification do not cover a
purely periodic word whose displayed symbols prescribe its exact suffix
exponents.  The accompanying fact that at most five minimal squares forces
ultimate periodicity is also in the wrong direction for a profile which is
periodic from the outset.  Currie--Rampersad's 7/3-power threshold concerns
aperiodic binary words with squares starting at every position and likewise
does not classify the present periodic exact-profile object.

Bell--Schulz--Shallit, *Consecutive Power Occurrences in Sturmian Words*
(2024), bounds gaps between cube endpoints in Sturmian words.  A critical
reset profile has not been shown Sturmian, so that theorem cannot be
imported without a new transfer result.

Direct searches for later curling-number work found the two Chaffin--Sloane
papers, the van de Bult et al. / van de Pol Gijswijt papers, and a 2018
six-minute talk announcement by Duane Bailey titled *A Grammatical Approach
to the Curling Number Conjecture*.  The searchable announcement says only
that the talk relates the conjecture to aperiodic grammars; no theorem,
paper, or reusable proof statement was located.  No searched post-2013
source supplied the minimum-deleted-hitting-time selection, the exact reset
transition equation, or a classification of primitive self-labelled
circular profiles.  This is a bounded literature search result, not a claim
that those ideas have never appeared anywhere.

## Fixed-threshold greedy power rule

Before pursuing a possible reduction of a maximum-`M` profile to the binary
rule "append one iff the current word ends in an `M`-th power", searches
were made for greedy power-free binary words, periodic squareful words, and
power occurrences at consecutive positions.  No theorem located states
that this rule overflows from every seed.  Small executed experiments also
produce long surviving trajectories for thresholds four and five, so the
rule is not being treated as an easy surrogate for the Curling Number
Conjecture.

## Circular squareful words and co-terminal square/cube overlaps

Before trying to classify the primitive binary profile by its minimal
square witnesses, the following searches were added on 2026-07-22:
`circular squareful words`, `circularly squareful word`, `every position
begins with a square periodic word classification`, and `ABA word cube
suffix primitive square Fine-Wilf`.  The closest primary results were
Saari's squareful/optimal-squareful theory, Currie--Rampersad's
`7/3`-threshold construction, and Bannai--Mieno--Nakashima's generalized
Three Squares Lemma.  None classifies a finite primitive period whose
symbol at every cut is the exact maximum proper exponent and whose witnesses
also fit after deleting the first symbol.  The generalized Three Squares
Lemma supplies overlap length inequalities, but not the pointed
first-copy closure needed here.  Consequently the new equality-graph
completion and fitting cube-halving lemmas are being treated as
not-found-in-the-searched-literature derivations, not as priority claims.

## One-mismatch powers and one-hole periodicity

Before treating the post-promotion word `(U^3)[1:]3` as a cube with one
changed endpoint, searches were run on 2026-07-23 for `almost power one
mismatch Fine Wilf`, `approximate periods one mismatch`, `partial words one
hole Fine Wilf`, and `three squares partial word one hole`.

Berstel--Boasson, *Partial Words and a Theorem of Fine and Wilf*, TCS 218
(1999), and Kociumaka--Radoszewski--Rytter--Walen, *On Periodicity Lemma for
Partial Words* (arXiv:1801.01096; Information and Computation 2021), study
the exact threshold `L(h,p,q)` at which a partial word with `h` holes and
strong periods `p,q` must have period `gcd(p,q)`.  The latter gives an
algorithmic closed form for arbitrary fixed `h`; its statement specializes
to the ordinary Fine--Wilf threshold when `h=0`.  Blanchet-Sadri--Mercas,
*The Three-Squares Lemma for Partial Words with One Hole*, TCS 428 (2012),
proves in particular that a one-hole word weakly periodic with periods
`p,q` and length at least `p+q` is strongly `gcd(p,q)`-periodic, and develops
sharp coinitial three-square bounds.

These results are relevant language for the single artificial endpoint in
`(U^3)[1:]3`, but their hypotheses do not by themselves supply the missing
second period across the whole almost-cube interval.  The incoming parent
cube occupies only a subinterval and can be larger than the post-promotion
root, as the executed length-21 critical models demonstrate.  Therefore no
published one-hole theorem found in these searches proves the external
reset local-death lemma directly.  It may still sharpen individual overlap
subcases once the exact common interval has been established.

## Suffix-square prefixes and restart cycles

Before using the bare condition that every late orbit prefix ends in a
square, searches were run on 2026-07-23 for `every prefix ends in a
square infinite word`, `each prefix square suffix`, `squareful word suffix
squares`, `cyclic overlapping powers return words`, and `primitive roots
overlapping powers cyclic factors`.

The direct condition is known to be far too weak.  Mignosi--Restivo--Salemi,
*Periodicity and the Golden Ratio*, Theoretical Computer Science 204
(1998), 153--167, prove the sharp local-periodicity threshold: a
right-infinite word is ultimately periodic exactly when every sufficiently
long prefix has a suffix of exponent at least
`phi^2=(3+sqrt(5))/2`.  Their Fibonacci-word extremality shows why suffix
squares of exponent two do not reach that threshold.  Bell--Schulz--Shallit,
*Consecutive Power Occurrences in Sturmian Words*, Comptes Rendus
Mathematique 362 (2024), 1273--1278, also explicitly notes that every
Fibonacci prefix of length at least six has a square suffix.  Saari's
squareful-word results concern squares beginning at every position (with
finitely many minimal squares), rather than the exact curling-label rule at
successive prefix endpoints.

For cyclic restart overlaps, the applicable standard tools found were the
Fine--Wilf periodicity theorem, Lyndon--Schuetzenberger word equations, and
return-word/critical-factorization theory.  No searched source supplies a
theorem saying that a cycle of variable left-boundary deletions and
curling-generated right extensions is impossible.  In particular, a
repeated bounded window makes the *moving-boundary output* periodic, but it
does not make those symbols the autonomous outputs of the undeleted full
prefix.  That distinction prevents importing an ordinary periodic-orbit
argument.  Any endpoint-rank restart-cycle exclusion is therefore recorded
as a new derivation if proved, with no claim of priority beyond the searched
literature.

## Rotten words versus moving-boundary context loss

Before using prefix sensitivity of the terminating deletion time, the
following direct searches were run:

* `"doubly rotten" curling`
* `"rotten sequences" "curling number"`
* `"prefix decreases tail" "curling number"`
* `OEIS A216730 curling`

The relevant published notion is Section 4.3 and Conjecture 22 of
Chaffin--Linderman--Sloane--Wilks, *On Curling Numbers of Integer
Sequences*, JIS 16 (2013), Article 13.4.3 / arXiv:1212.6102.  For binary
`S`, they call `S` rotten if `tau(2S)<tau(S)` or `tau(3S)<tau(S)`, and
doubly rotten if both inequalities hold; they conjecture that no doubly
rotten word exists and report a search through length 34.

That result has the opposite orientation from the live context-loss event.
Here a one-symbol prefix changes a terminating word into a nonterminating
one, while the driven transition also appends on the right.  No later
primary theorem located by the displayed searches controls that event.
Accordingly rotten-word terminology is useful context, but neither the
published computation nor Conjecture 22 is used as a lemma.

## Conjugacy equation at a restart cycle

Before solving the net restart equation, the following searches were run:

* `"uz = zv" conjugate words theorem combinatorics on words`
* `"xz=zy" conjugate words theorem Lothaire`
* `site:arxiv.org "uz=zv" words conjugate`
* `site:hal.science conjugacy equation words "xz=zy"`

The exact reusable result is the classical conjugacy-equation theorem.
Theorem 4 of J. Karhumäki's *Combinatorics on Words* notes states that
`u z=z v` holds exactly when there are words `p,q` and an integer `n>=0`
with

```
u=pq,             v=qp,             z=p(qp)^n.
```

The same result appears as Proposition 1.3.4 in M. Lothaire,
*Combinatorics on Words*.  It is stronger than merely saying that `u,v`
are conjugate, so the exact solution form is adopted for the restart
equation `A W=W Q` rather than rederived.  No searched source combines
this equation with the exact curling reset `W=Y^k`; the subsequent
locked-versus-bordered Fine--Wilf classification is therefore recorded
as a project derivation, with no priority claim beyond the searched
literature.

## Reverse-status prefix resets

Searches on 2026-07-23 for `curling number prefixing nonterminating
sequence`, `rotten sequence bad suffix`, `doubly rotten curling number`,
and `prefix extension termination curling number` returned CLSW Section
4.3 and its OEIS-linked rotten-word data, but no theorem about a terminal
word whose one-symbol deletion is nonterminating.  CLSW's rotten and doubly
rotten notions compare finite tail lengths only.  The minimum-terminal-time
reverse whole-power reset in `reverse_status_reset.md` is therefore being
used as a not-found-in-the-searched-literature lemma, not as a priority
claim.

For the equation `A W=W Q` arising from a restart cycle, searches for
`word equation XZ=ZY conjugate words`, `Lyndon Schuetzenberger conjugacy
equation`, and `combinatorics on words conjugate periods` located the
standard conjugacy solution already formalized in Holub--Raska--Starosta,
*Combinatorics on Words Basics*, Archive of Formal Proofs (2021).  The
restart analysis therefore cites that standard equation rather than
claiming it.  Its combination with the primitive whole-power reset and the
endpoint-rank cycle, recorded in `restart_cycle_conjugacy.md`, was not found
in the searched curling-number literature.

## Pointed bordered power completions

Before exploiting the extra orbit provenance `Q[0]=cn(W)` in the
bordered conjugacy case, searches on 2026-07-23 used:

* `primitive power followed by one letter square suffix theorem`;
* `word equation x^k a ends in square primitive word`;
* `conjugacy equation power border UVU primitive word`;
* `bordered primitive word power suffix completion Fine Wilf`.

The results recovered standard material on borders, conjugacy equations,
Fine--Wilf periodicity, and square-prefix/square-completion operations.
No located primary source combines a solution of `AW=WQ` with a whole
primitive power `W=Y^k`, the exact deleted curling value
`cn(W[1:])=k-1`, and the numerical pointing constraint `Q[0]=k`.
Accordingly the conjugacy-equation solution itself remains cited as
classical, while the positive/pointed refinement and the explicit
factorization

```
Y=UC=DU,          Q=C Y^(k-1),          Y[h]=k
```

are recorded as project derivations, without a claim of priority beyond
the stated searches.

## First divergence from a periodic splice

Before classifying the first curling-number mismatch between an
untruncated periodic splice and its bounded restarted suffix window,
searches on 2026-07-23 used:

* `periodic word suffix power primitive root longer than period Fine Wilf`;
* `circular word local exponent profile every position power periodicity`;
* `local exponent function periodic word powers at every position`;
* `periodic infinite word maximal suffix exponent primitive root`.

The searches recovered standard primitive-root and Fine--Wilf sources,
including Czeizler--Kari--Seki's presentation of the conjugacy and
Fine--Wilf theorems and general literature on local periods and critical
exponents.  No located primary source gives the project-specific
dynamical statement comparing a curling orbit with a periodically
spliced sequence of outputs from separately restarted suffixes.
Accordingly the fact that a maximizing root longer than the least tape
period is impossible is treated as a direct Fine--Wilf application; the
outer/proper first-crossing dichotomy and the bordered underprofile
reduction are recorded as project derivations, with no broader priority
claim.

## Halving children and boundary-crossing square masks

Before trying to force the low-phase square of a primitive cube root to remain
inside its parent cube, searches on 2026-07-23 used:

* `runs periodicity lemma overlapping square cube local periods boundary`;
* `square cube overlap primitive word Fine Wilf theorem runs`;
* `critical factorization local period square crossing boundary`;
* `overlapping squares combinatorics words primitive cube square run theorem`;
* `New Periodicity Lemma squares string`;
* `Three Squares Lemma Crochemore Rytter theorem statement`.

The imported baseline is Fine and Wilf, *Uniqueness Theorems for Periodic
Functions*, Proceedings of the American Mathematical Society 16 (1965),
109--114: if a word of length at least `p+q-gcd(p,q)` has periods `p` and
`q`, it also has period `gcd(p,q)`.

Crochemore and Rytter, *Squares, Cubes, and Time-Space Efficient String
Searching*, Algorithmica 13 (1995), 405--425,
doi:`10.1007/BF01190846`, prove the coinitial Three Squares Lemma.  In the
form restated as Lemma 1 by Bai--Deza--Franek, *On a Lemma of Crochemore and
Rytter*, Journal of Discrete Algorithms 34 (2015), 18--22: if distinct
primitive squares `u^2` and `v^2` are proper prefixes of a primitive square
`w^2`, then `|u|+|v|<=|w|`.  Bannai--Mieno--Nakashima, *Lyndon Words, the
Three Squares Lemma, and Primitive Squares*, SPIRE 2020 / arXiv:2006.13576,
extend the method to three overlapping squares which need not share a common
prefix.

Fan--Puglisi--Smyth--Turpin, *A New Periodicity Lemma*, SIAM Journal on
Discrete Mathematics 20 (2006), 656--668, doi:`10.1137/050630180`, restrict
the periods of a third square near two squares beginning at one position.
Bai--Franek--Smyth, *The New Periodicity Lemma Revisited*, Discrete Applied
Mathematics 212 (2016), 30--36,
doi:`10.1016/j.dam.2016.05.003`, removes the older regularity hypothesis
through a canonical factorization of the two coinitial squares.  The Critical
Factorization Theorem, in the form recorded by Harju, *Critical Factorisation
in Square-Free Words*, RAIRO Theoretical Informatics and Applications 56
(2022), Article 3 / arXiv:2107.09421, says that every word of length at least
two has a cut whose minimal local period is its global period.

None of these statements supplies containment of a square ending at an
arbitrary low phase of a different cube.  This is not only a mismatch of
hypotheses: `halving_square_mask_bridge.md` and
`check_halving_square_mask_bridge.py` give an exact fixed-profile
countermodel.  In the length-21 profile, a globally maximal period-four cube
has low-hole rescue runs of periods three and seven; each intersects the cube
run in exactly `p+q-gcd(p,q)-1` symbols.  Thus the strict Fine--Wilf bound is
sharp even with exact circular labels, singleton `3`-runs, and full
first-copy fitting.  The literature controls longer overlaps, but no theorem
can prove the false universal containment bridge under these hypotheses.

## Bordered circular underprofiles and reset exponents

Before using the nonfitting bordered reset power to bound its exponent,
searches on 2026-07-24 used:

* `curling number circular profile primitive word suffix power border`;
* `curling number robust primitive suffix power`;
* `"proper circular" "curling number"`;
* `"curling number" "circular" word power primitive`.

The searches returned Chaffin--Linderman--Sloane--Wilks, *On Curling
Numbers of Integer Sequences*, especially its robustness definition,
Fine--Wilf theorem, and canonical forms for non-robust curling-one words.
Their Theorem 9 states that if `cn(S)=1` but `cn(TS)>1` for a proper
suffix `T` of `S`, then

```
S=X V X,       cn(X)=1,       X is longer than V,
```

with `T` ending in `V`; Theorem 10 gives uniqueness of this canonical
form.  Its constructive proof uses only word equations, suffix
comparability, and the curling-number definition, not the binary alphabet.
It therefore applies directly to the residual square case
`Q=C U C`, `UQ=(UC)^2`, yielding `cn(C)=1`, `U` a proper suffix of `C`,
and `2|U|<|UC|`.  This stronger published normal form is adopted in
`moving_boundary_context_loss.md`, Corollary 25.

Those CLSW results do not state the preceding bound on the exponent of a
power crossing the distinguished cut of a primitive circular fixed
profile.  General results on primitive circular words and borders likewise
did not combine that crossing power with the self-labelled proper curling
profile.

The minimum-symbol-two input is not new: it remains the already cited
application of Saari's everywhere-repetitive periodicity theorem in
`critical_seed_induction.md`, Section 3.  The deduction that the bordered
reset exponent is at most three combines that published input with the
project-specific equations `Q=C Y^(k-1)` and `pc_Q=Q`; it is recorded as
a project derivation without a priority claim beyond the searches above.

For the residual cubic seam, additional searches used:

* `cube suffix of two conjugate squares Fine Wilf theorem`;
* `primitive conjugate words overlapping square cube period inequality`;
* `overlapping cubes conjugate words Fine Wilf`;
* `overlapping squares cubes primitive conjugates`.

They recovered the standard Fine--Wilf theorem, conjugacy and commutation
results in Lothaire and in Holub--Raška--Starosta's AFP formalization, and
the Three Squares / overlapping-squares literature already logged above.
No located statement treats the project-specific fractional-cube seam
`Q=(CU)^2C`, whose exact profile forces a cube at the cut after `(CU)^2`.
Lemma 26 of `moving_boundary_context_loss.md` therefore uses only the cited
Fine--Wilf and commutation theorems to derive its explicit
small-cube/large-cube scale split; no priority is asserted beyond these
searches.

## Cyclic covers by heterogeneous cubic runs

Before trying to generalize the finite whole-cycle equality-graph exclusion,
searches on 2026-07-24 used:

* `runs overlap graph acyclic periodic runs words`;
* `maximal repetitions overlap graph cycle combinatorics on words`;
* `"runs" "directed cycle" combinatorics on words periodicity`;
* `cubic runs overlap graph Lyndon roots theorem`.

The primary results located were Bannai--I--Inenaga--Nakashima--Takeda--
Tsuruta, *The “Runs” Theorem* (arXiv:1406.0263), and Crochemore--Iliopoulos--
Kubica--Radoszewski--Rytter--Walen, *On the maximal number of highly periodic
runs in a string* (arXiv:0907.2157).  They bound the number and total exponent
of runs by assigning Lyndon-root positions; they do not state that a directed
cycle of different square/cube periods and prescribed endpoint labels is
impossible.  The density refinements likewise charge positions to cubic runs
rather than identify the equality components of a heterogeneous cyclic cover.
No located theorem subsumes the proposed cyclic-cover lemma in
`circular_low_hole_transition.md`, Section 13.  This negative search result is
only a scope boundary, not a novelty or priority claim.

## Rotation cubes and one-letter prefix windows

Before analyzing a bad/terminal status change between consecutive cubes of
circular rotations, searches on 2026-07-24 used:

* `curling number rotten sequence rotations conjugates cube`;
* `"curling number" rotation word cube conjugate`;
* `delete first letter power append first letter conjugate power lemma`;
* `combinatorics on words word a w^3 h power prefix last letter Fine Wilf`;
* `primitive word cube factor of another power Fine Wilf theorem overlap`.

CLSW, *On Curling Numbers of Integer Sequences*, JIS 16 (2013), Article
13.4.3, Theorem 7 supplies the exact one-letter bound: prefixing one symbol
leaves the curling number unchanged or raises it by one.  Its Section 4.3
and OEIS A216730 treat finite rotten words, not the status of rotation cubes
under a hypothetical infinite orbit.  Fine--Wilf supplies the required
period collapse inside an internal primitive cube.  The Archive of Formal
Proofs entry Holub--Raška--Starosta, *Combinatorics on Words Basics* (2021,
updated 2023), confirms that the standard periodicity, primitive-root, and
rotation facts used here have machine-checked formulations.

No searched source states the derived classification: for primitive
`Q=Rx`, if prefixing `x` to `Q^3 H` changes its curling number, the
maximizing root either locks to length `|Q|`, forcing
`H=R(xR)^(k-4)`, or has length greater than
`2|Q|+gcd(|Q|,r)`.  The short-window `4`-versus-`3` exception is its first
locked case.  The derivation is recorded in
`rotation_cube_status_cycle.md`.  This is a
not-found-in-the-searched-literature result, not an unconditional novelty
or priority claim.

## Sink-SCC attachment to one maximal fitting cube

On 2026-07-24 a focused search checked whether standard run theory supplies
a nesting theorem strong enough to place an entire ancestry SCC inside one
globally maximal cubic run.  Queries included:

* `nested runs maximal repetitions crossing cubes containment tree
  combinatorics words`;
* `overlapping cubic runs primitive periods containment theorem`;
* `runs nesting forest primitive words Fine Wilf`; and
* `chain of maximal repetitions overlapping cubes words`.

The closest primary sources found were Kubica--Radoszewski--Rytter--Walen,
*On the Maximal Number of Cubic Subwords in a String* (arXiv:0911.1370),
Kolpakov, *On Primary and Secondary Repetitions in Words*
(arXiv:1103.5230), Kolpakov--Kucherov--Ochem, *On Maximal Repetitions of
Arbitrary Exponent* (arXiv:0906.4750), and Crochemore--Ilie,
*Understanding Maximal Repetitions in Strings* (arXiv:0802.2829).  These
papers bound, classify, or encode runs in one finite word; none states that
a directed suffix-ancestry SCC is laminar inside one selected cubic run.

The missing statement is false under the full project hypotheses: Q21 has
a unique sink SCC whose two globally maximal fitting root-four cubes
overlap in one symbol and neither contains the other in a common lift.
The exact certificate is in `sink_scc_attachment.md`,
`check_sink_scc_attachment_q21.py`, and the independent
`check_external_source_sink_attachment.py`.  Thus non-laminarity is not
merely a literature gap here; the desired single-container conclusion has
a fixed-profile counterexample.

For the endpoint-rank follow-up, searches used:

* `combinatorics on words nested primitive powers root length doubles
  infinite chain theorem`;
* `prefix chain powers primitive roots exponentially increasing
  periodicity theorem`;
* `Fine Wilf nested powers increasing periods infinite word ultimately
  periodic`;
* `runs theorem nested cubic runs root periods doubling chain`.

The located runs theorems, including
Bannai--I--Inenaga--Nakashima--Takeda--Tsuruta,
*The “Runs” Theorem* (arXiv:1406.0263), bound the number or total exponent
of runs in one finite ambient word.  They do not turn root doubling across
successively longer orbit states into a well-founded descent.  No located
source couples such growth to a curling-orbit endpoint rank.  The
project-specific rank conservation and its limitation are recorded in
`rotation_cube_status_cycle.md`, Section 6.

## Heterogeneous periodic-interval equality graphs, second pass

On 2026-07-24 the root agent searched before extending the whole-cycle
equality-graph classification, using:

* `periodic intervals cyclic cover heterogeneous periods Fine Wilf theorem local periodicity graph`;
* `combinatorics on words system of overlapping periodicities intervals cyclic word theorem`;
* `local periods interval overlap graph periodic words theorem Ehrenfeucht Silberger`;
* `runs periodic intervals overlap endpoint equality theorem combinatorics on words`.

The closest primary results found were Stuart A. Rankin, *Fine-Wilf graphs
and the generalized Fine-Wilf theorem* (arXiv:0906.1780), which concerns
several periods of one common word/factor, and Bannai et al., *The “Runs”
Theorem* (arXiv:1406.0263), which bounds and characterizes maximal
repetitions in a word.  Lothaire's *Algebraic Combinatorics on Words*,
Chapter 8, likewise separates simultaneous periods of one factor from
critical/local periodicity.  None of the located statements treats a
cyclic chain of different length-three periodic intervals with the
project's forced endpoint labels and root-scale transition split.  The
unrestricted equality-graph lemma therefore remains project-specific; this
is a search report, not a novelty or priority claim.

A focused follow-up used the queries `combinatorics on words chain of
overlapping runs cubic runs close endpoints theorem`, `two runs same right
endpoint distance bounded periods overlap lemma strings`, `sequence of
overlapping cubes increasing periods combinatorics words theorem`, and
`cubic runs chain overlap periods word theorem`.  The search recovered cubic
run-count bounds and ordinary pairwise overlap lemmas, but no theorem for a
closed chain of successively shifted cubes with distinct endpoints.  These
results remain potentially useful for counting, but none implies the needed
forced-label collision.

A third pass checked whether the cyclic chain could be oriented using
Lyndon roots of runs.  Queries included `Bannai runs theorem Lyndon root
overlapping runs right boundary lexicographic order lemma`, `Lyndon roots
nested overlapping runs periods right endpoints combinatorics words`, and
`cubic runs Lyndon root characterization right endpoint`.  Bannai et al.
(arXiv:1406.0263) assign L-roots using the nonextendable run boundary, and
Bannai--Mieno--Nakashima (arXiv:2006.13576) generalize the Three Squares
Lemma to overlapping primitive squares.  Neither states the required
closed-chain result.  The project proof ultimately uses a simpler global
lexicographic minimum over length-`n` rotations; no Lyndon-root theorem is
invoked in P-20260724-003459-MSTF.

## First-mismatch replay and rotated fourth-power obstruction

Before promoting the symbol-`3` status theorem in
`rotation_cube_status_cycle.md`, the follow-up searches on 2026-07-24 used:

* `word square prefix cube overlap hidden square primitive word equation C^3 prefix Y^2`;
* `cube prefix of square primitive words Fine Wilf classification`;
* `word equation x^3 prefix y^2 primitive overlap theorem`;
* `curling number robust primitive square first letter deletion cn 1 theorem`;
* `site:arxiv.org combinatorics on words cube prefix square one-letter deletion rotation fourth power Fine Wilf`;
* `site:cs.uwaterloo.ca/journals/JIS curling number rotten sequence prefix deletion theorem 7`;
* `site:arxiv.org "word equation" cube square overlap primitive prefix`;
* `"curling number" "fourth power" sequence`;
* `"curling number" rotation cube`.

CLSW, *On Curling Numbers of Integer Sequences*, JIS 16 (2013), Article
13.4.3, Theorem 7 remains the applicable published one-letter result:
prefixing a symbol changes the curling number by zero or one, and in the
strict case the longer word is a whole power.  Section 4.3 of that paper and
OEIS A216730 discuss finite tail-length drops under prefixing ("rotten"
words).  They do not assign bad/terminal status to consecutive rotation
cubes or analyze a hypothetical first mismatch of their infinite orbits.

The combinatorics-on-words results returned by the other searches concern
standard Fine--Wilf overlap, primitive roots, general word-equation
algorithms, or repetition avoidance.  No located statement gives either of
the two project-specific conclusions:

1. a terminal-to-bad first mismatch at a symbol `3` forces a
   `4`-versus-`3` whole power whose bad branch rotates into a fourth power
   and terminates; or
2. a bad-to-terminal `2`-versus-`1` mismatch forces the exact overlap
   `C[:h]=C[s:]3` and an adjacent pair `C[h-1]=C[h]=3`.

The reused ingredients are CLSW Theorem 7 and Fine--Wilf.  The first-mismatch
visibility, orbit-status use, and rotated-fourth-power obstruction are
derived in `rotation_cube_status_cycle.md`, Sections 9--10.  This is a
not-found-in-the-searched-literature report, not a priority claim.

## Binary circular square coverage and exact square/cube profiles

Before reopening the run-code and terminal-macro classification on
2026-07-24, the root agent searched for an existing classification using:

* `binary circular word every position ends square cube exact exponent combinatorics words`;
* `squareful circular binary words classification runs code cubes`;
* `every position squareful periodic binary word classification Saari`;
* `binary word exact square cube profile self describing curling number`.

The closest primary papers located were Currie--Rampersad, *Infinite words
containing squares at every position* (arXiv:0803.1189), which determines
the binary repetition threshold for infinite words having arbitrarily large
squares beginning at every position, and Currie--Johnson,
*Characterization of the lengths of binary circular words containing no
squares other than 00, 11, and 0101* (arXiv:2005.09742), which classifies
lengths for a circular square-avoidance problem.  Peltomaki--Whiteland,
*A Square Root Map on Sturmian Words* (EJC 24(1), P1.54, 2017), summarizes
Saari's classification of aperiodic optimal squareful infinite words in
terms of six minimal squares and studies a different square-root map.

These sources concern squares beginning at positions, finite sets of
minimal square factors, or avoidance of all but specified squares.  They do
not classify primitive binary circular words whose *ending* exponent at
every cut is exactly two or three, nor the additional self-profile equation
used here.  No located source supplies the project's run-code equations,
terminal-edge macro classification, or the Q21 exception.  Those statements
therefore remain project-specific, with the conservative label
"not found in the searched literature" rather than a novelty or priority
claim.

Primary links checked:

* https://arxiv.org/abs/0803.1189
* https://arxiv.org/abs/2005.09742
* https://doi.org/10.37236/6074

A follow-up on the same date checked whether Saari's everywhere-repetitive
theory already classifies the periodic case, using `Kalle Saari Everywhere
alpha-repetitive sequences periodic squareful words classification minimal
squares theorem`, `"Everywhere alpha-repetitive sequences" Saari pdf
squareful periodic`, and `periodic squareful words classification every
position begins with a square binary`.  Saari's *Everywhere
alpha-Repetitive Sequences and Sturmian Words* (TCS 410 (2009), DOI
10.1016/j.tcs.2008.12.009; extended abstract DOI
10.1007/978-3-540-74510-5_37) defines squareful words and determines the
minimum number of minimal squares needed for an aperiodic example.  The
optimal-squareful classification quoted in Peltomaki--Whiteland explicitly
assumes aperiodicity.  It therefore does not classify primitive periods of
purely periodic squareful words and does not imply the project's exact
ending-profile equation.

## Root-one ancestry sources versus terminal run-code gadgets

On 2026-07-24 a focused search was made before translating the
root-one/`2` external ancestry edge into the terminal-gadget language.
Queries included:

* `squareful words primitive square roots return words theorem`;
* `combinatorics on words cube overlap primitive roots Fine Wilf runs theorem`;
* `binary squareful words classification square root map`;
* `run length encoding repetitions cubes words`;
* `"squareful words" combinatorics`;
* `"optimal squareful" words`;
* `"square root map" Sturmian words`; and
* `"every position" square word combinatorics`.

The closest primary sources were Currie--Rampersad, *Infinite words
containing squares at every position* (arXiv:0803.1189),
Peltomaki--Whiteland, *A Square Root Map on Sturmian Words*
(arXiv:1509.06349), Peltomaki--Whiteland, *More on the Dynamics of the
Symbolic Square Root Map* (arXiv:1801.00920), and
Peltomaki--Saarela, *Standard Words and Solutions of the Word Equation
`X_1^2 ... X_n^2=(X_1...X_n)^2`* (arXiv:2004.14657).  These papers
classify or study squares beginning at positions, minimal-square
factorizations, and a square-root map on special infinite languages.
They do not retain a distinguished deleted-copy origin, do not impose
the project's exact ending-exponent profile, and do not state that a
local unary-square source makes an adjacent cube's primitive run code
terminal.

The searches on runs and run-length encoding returned standard
Fine--Wilf/run-overlap results and RLE pattern-indexing papers, including
Akagi--Okabe--Mieno--Nakashima--Inenaga, *Minimal Absent Words on
Run-Length Encoded Strings* (arXiv:2202.13591).  None supplies the
project-specific transport from one anchored `3 2 2 2` boundary to
fitting terminal gadgets at all run-code defects, nor does any located
statement control the first-copy weak-square masks lost under the
unpointed halving descent.  The bridge and its countermodel are therefore
derived directly in `terminal_source_gadget_bridge.md`; “not found” here
is not a novelty or priority claim.

## Arbitrary-alphabet rotation-cube status transitions

Before generalizing the binary rotation-status theorem on 2026-07-24, the
following searches were made:

* `site:arxiv.org/abs/1212.6102 curling numbers integer sequences Theorem 7 prefixing one term`;
* `site:cs.uwaterloo.ca/journals/JIS/VOL16/Sloane/sloane3.pdf curling number Theorem 7 rotten sequence`;
* `combinatorics on words primitive conjugate powers one letter deletion word fourth power theorem`;
* `Fine Wilf theorem period primitive word cube factor another power`;
* `"proper circular" "curling number" profile`;
* `"curling number" cyclic word rotation primitive profile`;
* `site:cs.uwaterloo.ca/journals/JIS "rotten" "curling number" prefix`;
* `Kalle Saari Everywhere alpha-repetitive sequences and Sturmian words Theorem 5.3 phi+1`;
* `"Suppose a sequence z is everywhere (phi+1)-repetitive"`;
* `"Fundamental Periodicity Theorem" "Mignosi" phi+1`;
* `word equation C prefix h C suffix s letter square deletion curling number`;
* `primitive word square one-letter deletion curling number one orbit replay`; and
* `"curling number" square deletion rotation orbit`.

The primary curling-number source is Chaffin--Linderman--Sloane--Wilks,
*On Curling Numbers of Integer Sequences*, JIS 16 (2013), Article 13.4.3.
Its Theorem 7 says that prefixing one term raises the curling number by at
most one; its proof is alphabet-independent.  Section 4.3 treats finite
tail-length drops under prefixing, not bad/terminal statuses of rotations.

The periodicity source is Kalle Saari, *On the Frequency and Periodicity of
Infinite Words*, TUCS Dissertations 83 (2008), Theorem 5.3:

> Everywhere `(phi+1)`-repetitive sequences are ultimately periodic.

The journal version is Saari, *Everywhere alpha-repetitive sequences and
Sturmian words*, European Journal of Combinatorics 31 (2010), 177--192,
DOI `10.1016/j.ejc.2009.01.004`.  Fine--Wilf remains the overlap input.

The other results returned concern ordinary primitive conjugates,
repetition avoidance, square networks, or general word equations.  No
located source gives the project-specific conclusions that an external
one-letter first mismatch replays a new circular fixed profile, that its
minimum is at least the deleted leading label, or that this excludes every
terminal-to-bad rotation-cube transition at an arbitrary label at least
three.  Nor was the residual square-reset equation

```
C[:h]=C[s:]a,
C[h-1]=a,
C[h]=max(3,C[1])
```

found in the searched literature.  The derivation is recorded in
`general_rotation_status.md`.  This is a scoped not-found report, not an
unconditional priority claim.

## Independent audit: external root-one sources and selected cubes

On 2026-07-24, before independently auditing whether a root-one/`2`
external source forces its selected high cube to be nonunary or terminal,
the searches included:

* `combinatorics on words cube periodic word run length encoding primitive root defects`;
* `binary words every position ends square cube return words primitive roots`;
* `squareful words optimal squareful words square root map binary`;
* `runs Lyndon cubic overlap primitive words`;
* `"run-length encoding" repetitions squares cubes word combinatorics`;
* `"every position" "square" binary word combinatorics`;
* `circular binary words cubes primitive period overlap Fine Wilf`; and
* `"minimal square" binary word classification squareful`.

The closest primary sources located were Bannai--I--Inenaga--Nakashima--
Takeda--Tsuruta, *The "Runs" Theorem* (arXiv:1406.0263);
Peltomaki--Whiteland, *A Square Root Map on Sturmian Words*
(arXiv:1509.06349) and *More on the Dynamics of the Symbolic Square Root
Map* (arXiv:1801.00920); Currie--Rampersad--Shallit, *Binary Words
Containing Infinitely Many Overlaps* (arXiv:math/0511425); and
Akagi--Okabe--Mieno--Nakashima--Inenaga, *Minimal Absent Words on
Run-Length Encoded Strings* (arXiv:2202.13591).  These give general
results about runs, primitive periodicity, overlap avoidance, special
squareful languages, or RLE indexing.  None states a result connecting
an anchored local `3,2,2,2` boundary to (i) exclusion of a unary cube
immediately before the anchor, or (ii) recursive terminality of the
primitive run code of a nonunary cube.  In particular, the square-root-map
papers concern special infinite languages and factorizations into squares,
not the project's proper circular ending-exponent profile or common
first-copy fitting origin.  The conclusions below therefore require direct
coordinate proofs or executed countermodels.  This is a scoped search
report, not a claim of novelty.

## Symbol-two rotation seam: adjacent completion and conjugate cubes

On 2026-07-24, before analyzing the remaining status boundary at a
phase labelled `2`, the focused searches included:

* `combinatorics words one letter deletion cube primitive conjugate powers completion theorem`;
* `word equation adjacent completion square cube conjugate primitive word Fine Wilf`;
* `one-letter extension curling number powers suffix word combinatorics`;
* `prefixing one letter exponent suffix primitive word theorem`; and
* the corresponding searches restricted to arXiv.

The only directly applicable curling-number source located was
Chaffin--Linderman--Sloane--Wilks, *On Curling Numbers of Integer
Sequences* (arXiv:1212.6102), especially Theorem 7 on prefixing one
symbol.  General conjugate-power and overlap searches led back to the
Fine--Wilf periodicity theorem and runs/Lyndon-word literature, including
Bannai et al., *The "Runs" Theorem* (arXiv:1406.0263); none treats the
specific three-word fork

```
2D3,  2D2,  D2,       D=(R2)^3[:-1],
```

or combines it with a proper circular self-profile `pc_P=P`.  Search
also rediscovered the two primary curling-number papers but no published
locked/external classification for this seam.  The case split below
therefore uses CLSW's prefix bound, Fine--Wilf, and direct word
identities.  This is a scoped not-found report.

## Ruler/valuation words and unbordered conjugates

On 2026-07-24, two exploratory branches were screened before further
investment.  The exact searches included:

* `p-adic valuation word borders periods combinatorics on words ruler sequence repetitions`;
* `generalized ruler sequence v_k(n) powers borders periodic factors`;
* `Toeplitz valuation word repetition factor powers combinatorics words`;
* `primitive word unbordered conjugates theorem`;
* `Harju Nowotka primitive word unbordered conjugates`; and
* `Border correlation of binary words Harju Nowotka 2004`.

The ruler-word results located describe the valuation word, its recursive or
automatic structure, and its power-avoidance properties.  They do not state
the exact ending-profile, border, or orbit-replay theorem needed by the
project, so no result from that branch is currently load-bearing.

For conjugates, the closest primary sources were Harju--Nowotka,
*Border Correlation of Binary Words*, Journal of Combinatorial Theory A 108
(2004), 331--341, DOI `10.1016/j.jcta.2004.07.009`; Harju--Nowotka,
*Bordered Conjugates of Words over Large Alphabets*, Electronic Journal of
Combinatorics 15 (2008), N41, DOI `10.37236/916`; and Harju--Nowotka,
*Periodicity and Unbordered Words: A Proof of the Extended Duval
Conjecture*, arXiv:`cs/0305039`.  These establish strong facts about which
conjugates are bordered/unbordered and about the longest unbordered factors
of a word.  They do not couple those borders to the project's exact
proper-circular curling profile or to bad/terminal orbit status.  The results
are therefore retained as possible future inputs, not cited as proving any
current transition lemma.  This is a scoped not-found record, not a novelty
or priority claim.

## Two-sided completion at the symbol-two rotation seam

Before attacking the only remaining rotation-status boundary on 2026-07-24,
the searches included:

* `combinatorics on words two words a w b and w c powers different end letters Fine Wilf theorem`;
* `conjugate cubes one letter extension word equation awb wc powers`;
* `primitive word cube rotation one letter deletion two completions power theorem`; and
* `curling number prefix suffix two-letter completion cube rotation theorem`.

The search recovered the CLSW curling-number paper and generic work on
primitive words, periodic overlaps, and critical exponents, but no primary
source stating the project-specific diagonal comparison between
`(2R)^3 3` and `(R2)^3`, or between the two completions `(2R)^3 2` and
`(2R)^3 3`.  CLSW Theorems 7--10 remain relevant one-sided inputs;
Fine--Wilf remains the overlap input.  The two-sided symbol-two
classification therefore requires a direct argument.  This is a scoped
search record, not a priority claim.

## Conjugacy equation in the short external symbol-two branch

On 2026-07-24, before classifying the overlap equation left by the short
external seam, the searches included:

* `Lyndon Schutzenberger word equation XY = YZ solution X=uv Y=(uv)^k u Z=vu source`;
* `combinatorics on words equation xy=yz theorem conjugacy Lothaire`;
* `"xy = yz" "(uv)^i u" words theorem`; and
* `Berstel Perrin Theory of Codes conjugacy equation xy=yz proposition`.

This equation is standard and will not be reproved as a project novelty.
Brlek--Li, *On the number of squares in a finite word*, Combinatorial
Theory 5(1) (2025), article 3, DOI `10.5070/C65165014`, Lemma 6 (attributed
there to Lyndon--Schuetzenberger) records the conjugacy normal form.  The
zero-index endpoint needed when the middle word is shorter is also stated
explicitly in Jean Berstel's online 2009 manuscript,
*Transductions and Context-Free Languages*, Exercise 2.6.  In the project's
variables the full form is

```
A=UV,       B=(UV)^k U,       T=VU,       k>=0.
```

The literature theorem supplies only this word-equation normal form; all
restrictions coming from the exact proper-circular profile and orbit status
remain project work.

## One-position defects between periodic words

Before extending the contained-completion analysis on 2026-07-24, the
searches included:

* `combinatorics on words Hamming distance one powers different periods theorem words coincide except one position`;
* `"coincide except in one position" word periods theorem`; and
* `two words differ in one position both powers primitive roots Fine Wilf`.

The directly relevant source is Margot Bruneaux, *A note about words which
coincide except in one position*, Theoretical Computer Science 791 (2019),
109--111, DOI `10.1016/j.tcs.2019.04.005`, arXiv:`1709.02430`.
Proposition 1 says that two equal-length words which differ in at most one
position and have periods `p,q` must be equal if
`max(p,q)<=floor(length/2)`.  The paper also gives the counterexample
`ababab` / `abaaab` to the weaker claim from Lothaire Problem 8.1.4 that
`p+q<=length` suffices.  Therefore the project must not invoke that weaker
one-defect periodicity statement.  At the current completion fork the long
ambient period is not at most half of the common shadow, so Proposition 1
does not close the case; the exact Fine--Wilf separation already recorded
remains the applicable bound.

## Adjacent-transposition periodic shadows

Before analyzing the residual `D32` versus `D23` defect on 2026-07-24,
the searches included:

* `combinatorics on words two words Pab Pba powers primitive roots Fine Wilf adjacent transposition`;
* `adjacent transposition periodic words Fine Wilf theorem Hamming distance two`; and
* `words differing by adjacent swap both periodic primitive root theorem`.

The results recovered the standard Fine--Wilf theorem, the periodicity
chapters of Lothaire, and work on one-position or quasiperiodic defects,
but no primary source stating the co-terminal adjacent-transposition
root-separation inequality needed here.  The direct proof in
`adjacent_transposition_power_separation.md`, Lemma 1, is a single
Fine--Wilf application after deleting the two transposed symbols.  This
is a scoped not-found record, not a claim of novelty or priority.

## Nested reset towers, squareful words, and the golden-ratio threshold

Before trying to turn the cross-rank nested cube tower into a periodicity
contradiction on 2026-07-24, the searches included:

* `infinite squareful words optimal squareful words Saari Peltomaki`;
* `infinite words every position begins with square squareful S-adic`;
* `nested prefixes cubes primitive roots infinite word theorem`;
* `periodic squareful words avoid fourth powers classification`;
* `Mignosi Restivo Salemi Periodicity and the golden ratio theorem
  prefixes suffix repetition phi+1`; and
* `Fibonacci word cubes occurrence positions cube roots theorem`.

The load-bearing external result located is Mignosi--Restivo--Salemi,
*Periodicity and the golden ratio*, Theoretical Computer Science 204
(1998), 153--167, DOI `10.1016/S0304-3975(98)00037-1`: a right-infinite
word is ultimately periodic if and only if every sufficiently long prefix
has a suffix of exponent at least `phi+1=phi^2`.  The threshold is strict
for the present purpose: an integer square gives exponent two, not
`phi^2`.

For the sharp aperiodic side, Shallit, *Prefixes of the Fibonacci word*,
Theoretical Computer Science (2026), article 115876, DOI
`10.1016/j.tcs.2026.115876` (preprint arXiv:`2302.04640`), restates the
Mignosi--Restivo--Salemi threshold and gives an explicit form of their
result that Fibonacci prefixes eventually have suffix exponent at least
`phi^2-epsilon` for each positive `epsilon`.  Rampersad, *Prefixes of the
Fibonacci word that end with a cube*, Comptes Rendus Mathématique 361
(2023), 323--330, DOI `10.5802/crmath.408`, gives an exact automatic
description of cube-ending positions; it does not identify the
cube-indicator word with the letters of a curling fixed profile.

The squareful-word sources located were Saari, *Everywhere
alpha-Repetitive Sequences and Sturmian Words*, European Journal of
Combinatorics 31 (2010), 177--192, and Peltomäki--Whiteland,
*A square root map on Sturmian words*, Electronic Journal of
Combinatorics 24(1) (2017), P1.54.  They show, among other things, that
Sturmian words are optimal squareful and describe their six minimal
squares.  Their hypotheses concern occurrence of squares, not the
project's exact equality between each letter and the greatest proper
power at that cut.

No searched source states that nested primitive cube prefixes with a fixed
delimiter, even together with square coverage and fourth-power avoidance,
force the `phi^2` suffix threshold.  The Fibonacci construction already
recorded in `recurrent_tower.md` is an explicit countermodel to such a
delimiter-only claim.  The new audit in `cross_rank_tower_audit.md` therefore
uses the literature as a guardrail and retains exact symbol/profile equality
and autonomous orbit ancestry as load-bearing hypotheses.  This is a scoped
not-found report, not a novelty or priority claim.

## Squareful infinite words and local-periodicity thresholds

Before investing further in the nested cross-rank tower on 2026-07-24, the
searches included:

* `infinite squareful words every position begins with square classification Saari optimal squareful`;
* `Peltomaki Whiteland optimal squareful words arXiv 1801.00920 minimal squares`;
* `infinite word each position begins square ultimately periodic`;
* `Currie Rampersad infinite binary words arbitrarily large squares every position 7/3`; and
* `Mignosi Restivo Salemi Periodicity and the golden ratio local period threshold`.

The primary results rule out a squarefulness-only closure.  Currie--Rampersad,
*Infinite words containing squares at every position*, RAIRO Theoretical
Informatics and Applications 44 (2010), 113--124, DOI
`10.1051/ita/2010007`, construct a binary `7/3`-power-free infinite word with
arbitrarily large squares beginning at every position.  Peltomaki--Whiteland,
*A square root map on Sturmian words*, Electronic Journal of Combinatorics
24(1) (2017), P1.54, arXiv:`1509.06349`, explicitly construct infinitely many
non-Sturmian fixed points of the symbolic square-root map.  Their sequel,
*More on the dynamics of the symbolic square root map*, Theoretical Computer
Science 806 (2020), 10--27, DOI `10.1016/j.tcs.2018.08.019`,
arXiv:`1801.00920`, studies periodic points and limit sets among optimal
squareful words.  These show that aperiodic squareful and square-root
self-similar words exist.

Mignosi--Restivo--Salemi, *Periodicity and the golden ratio*, Theoretical
Computer Science 204 (1998), 153--167, DOI
`10.1016/S0304-3975(98)00037-1`, gives an ultimate-periodicity criterion using
left local repetitions at every sufficiently long prefix with exponent at
least `phi^2`; it does not follow from exponent two alone, and the threshold is
tight.  Consequently the project's nested cubic-boundary tower can be closed
by this literature only if its exact exponent-three/self-label/fitting
hypotheses are converted into the theorem's uniform local-period hypothesis.
The weaker statement that every relevant position begins or ends in some
square is insufficient.  The exact orbit labels, full proper-circular profile,
and nested delimiter equations remain load-bearing.

## Doubly rotten sequences and prefix-tail monotonicity

Before seeking a general comparison between the terminal tails of `D3` and
`D2`, the searches included:

* `curling number doubly rotten sequences Conjecture 22 later results`;
* `doubly rotten curling number sequence`; and
* `curling number prefix tail length monotonicity rotten`.

The directly relevant published statement remains Conjecture 22 of
Chaffin--Linderman--Sloane--Wilks, *On Curling Numbers of Integer Sequences*,
Journal of Integer Sequences 16 (2013), Article 13.4.3,
arXiv:`1212.6102`: doubly rotten sequences are conjectured not to exist.  The
paper verifies their absence only through the finite range it reports and
explains that the conjecture would imply prefix-tail monotonicity.  The search
did not locate a later primary-source proof.  Therefore no unproved rotten or
doubly-rotten assertion may support the current rank comparison.  This is a
scoped search record, not a claim that no later result exists.

## Linear sensitivity of terminal tails under a wrong completion

Before testing whether the terminal-`F` tower could be closed by a bound of
the form `tau(D3)-tau(D)<=|D|`, the searches included:

* `curling number tail length one symbol append bound tau(S2) tau(S3)`;
* `curling number sequence sensitivity one symbol change tail length`;
* `curling number wrong append terminal tail delay`; and
* the tail-length and rotten-sequence sections of
  Chaffin--Linderman--Sloane--Wilks (2013).

The directly relevant published material defines `tau`, tabulates finite
tail distributions, and studies the effect of *prefixing* one symbol.  It
does not provide a linear Lipschitz bound for replacing the final `2` by
`3`, or for the difference between the terminal tails of `D`, `D2`, and
`D3`.  The proposed static linear bound was therefore tested directly and
falsified; see `C-20260724-024726-ROOT`.  Any remaining upper bound must use
the exact fixed-profile ancestry and, crucially, badness of the prefixed
word `2D3`.  This is a scoped not-found report, not a priority claim.

## Bounded top components, return words, and periodicity

Before attempting to turn one-sided exit-marker ancestry into eventual
periodicity, the searches included:

* `Vuillon Sturmian words return words characterization primary paper 2001`;
* `Durand finite return words uniformly recurrent periodicity theorem return words primary source`;
* `return words finite number does not imply periodic Sturmian exactly two return words theorem`;
* the local-period sources already recorded above; and
* the first-return/circular-code sources recorded in
  `static_return_synchronization.md`.

Laurent Vuillon, *A Characterization of Sturmian Words by Return Words*,
European Journal of Combinatorics 22 (2001), 263--275, proves that a
recurrent infinite word is Sturmian exactly when every nonempty factor has
two return words.  Sturmian words are aperiodic.  Jacques Justin and Laurent
Vuillon, *Return Words in Sturmian and Episturmian Words*, RAIRO Theoretical
Informatics and Applications 34 (2000), 343--356, gives the related
Sturmian/episturmian return-word framework.  Thus even uniform recurrence
and a fixed finite number of return types for every marker do not imply
periodicity.

Berthé--De Felice--Dolce--Leroy--Perrin--Reutenauer--Rindone's prefix-code
property for first right returns, and Durand--Petite's circular-code result
under uniform recurrence, give unique decoding only after a marker boundary
is already aligned.  They do not retroactively align a powered suffix that
starts inside a return.  Mignosi--Restivo--Salemi's local-period criterion
requires exponent at least `phi^2` at every sufficiently long prefix;
bounded occurrences of top components do not upgrade the ever-present
suffix squares to that threshold.

Consequently no located return-word or local-period theorem turns a finite
alphabet of bounded top-component/exit markers into periodicity.  A
project-specific conclusion would still need bounded raw return lengths,
aligned root copies, or a stronger full-profile constraint.  This is an
applicability boundary, not a claim that the project-specific ancestry
cannot supply such extra data.

The follow-up search

```
"Square completion operation of maximal suffix in Fibonacci word"
```

located K. Ernest Bognini, Idrissa Kaboré and B. Thomas Ouedraogo,
*Square Completion Operation of Maximal Suffix in Fibonacci Word*,
Advances and Applications in Discrete Mathematics 39(1) (2023), 99--115,
DOI `10.17654/0974165823039`.  Its abstract states that both maximal-suffix
duplication and strict square completion can be iterated to generate the
Fibonacci word.  This supplies an external warning that one-sided
suffix-duplication ancestry can remain aperiodic.  It does not impose the
curling self-profile or prove that the duplicated suffix is a maximizing
curling root at every intermediate cut.  The project-specific encoded
Fibonacci identities in `one_sided_threshold_ancestry.md` are proved
directly and use the paper only as literature context.

## Van de Pol follow-up audit for arbitrary-seed transfer

The post-2013 direct search was refreshed with `"Curling Number Conjecture"
citations Gijswijt sequence van de Pol`, `site:arxiv.org curling numbers
integer sequences Gijswijt van de Pol`, `site:oeis.org A094004 curling number
references`, and searches for Levi van de Pol's publications.  The primary
follow-ups found were Levi van de Pol, *The first occurrence of a number in
Gijswijt's sequence*, arXiv:`2209.04657`, and *The Growth Rate of Gijswijt's
Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6.  They give
strong canonical block/glue and growth results for Gijswijt's sequence.
Section 9.1 of the arXiv paper states that its methods are insufficient for
the general Curling Number Conjecture.  No theorem transferring that
canonical structure to every arbitrary-seed orbit was located.  These works
are therefore launch-pad results only until such a transfer lemma is proved.
This is a scoped search record, not an exhaustive priority claim.

## Syndetic cube endpoints do not upgrade suffix-squarefulness

Before trying to combine bounded `H_3` components with the fact that every
bad-orbit prefix ends in a square, the searches included:

* `combinatorics on words every prefix has square suffix cubes bounded gaps ultimately periodic`;
* `infinite word square suffix every prefix syndetic cubes periodicity theorem`;
* `local periods every position square bounded gaps cube endpoints ultimate periodicity`; and
* `right infinite word every prefix ends in square cube infinitely often bounded gaps`.

Jason Bell, Chris Schulz, and Jeffrey Shallit, *Consecutive Power
Occurrences in Sturmian Words*, Comptes Rendus Mathématique 362 (2024),
1273--1279, DOI `10.5802/crmath.644`, records two directly decisive facts.
Every Fibonacci-word prefix of length at least six has a square suffix, and
consecutive positions where cubes end in the Fibonacci word have gaps in
`{1,2,3,4,8,9}`.  The Fibonacci word is aperiodic.  Their Theorem 1 more
generally bounds cube-ending gaps by ten in every Sturmian word.

Therefore the generic implication

```
square suffix at every sufficiently long prefix
+ syndetic cube-ending positions
=> ultimate periodicity
```

is false.  Any argument from the one-sided `H_3`-component bound must use
the exact self-label equation `T[n]=cn(T[:n])`, not only the geometry or
density of square and cube endpoints.

## Shortest roots and midpoint-reset iteration

Before deriving a new autonomous-one root statement for the external-child
suffix, the direct curling-number literature and the squareful-word sources
above were checked again.  The applicable published results are:

* Chaffin--Linderman--Sloane--Wilks, Lemma 4: among maximizing
  representations `S=XY^k`, the shortest root is unique and primitive, and
  its curling number is below `k` when `k>1`.  At an exact value-two cut this
  gives curling number one for the shortest square root.
* Saari's minimal-square midpoint lemma, in the form recorded in
  `saari_midpoint_audit.md`: consecutive shortest square roots along the
  midpoint map are prefix-comparable and the next length is greater than
  half the preceding length.
* Peltomäki--Whiteland's square-root dynamics, cited above, supplies periodic
  and aperiodic square-root-map behavior and therefore rules out treating a
  midpoint orbit as automatically well founded.

The new step in `cross_rank_tower_audit.md` is not a reproof of these
results.  It combines CLSW's autonomous-one root with actual external-child
provenance: the midpoint is an orbit state forced by its left context to
emit the second root copy.  Taking the shortest suffix of that midpoint
whose curling number is at least two produces a whole robust square
`Y^2`, with `cn(Y^2[1:])=cn(Y)=1`, and locates its left edge relative to
the old delimiter.  Iteration gives an exact delimiter landing/crossing
normal form.  No located source supplies the missing conclusion that the
crossing alternative is impossible.

## Partial-conjugate cube replay and first mismatch

Before formalizing the bounded-overhang mismatch lemma, the searches were:

* `site:arxiv.org combinatorics on words (uv)^n u conjugate power overlap prefix extension`;
* `site:hal.science combinatorics words conjugate powers prefix extension cube overlap`;
* `"(uv)^n u" words conjugate`; and
* `curling number conjugate cube rotation suffix`.

The search recovered Chaffin--Sloane, arXiv:`0912.2382`, and
Chaffin--Linderman--Sloane--Wilks, arXiv:`1212.6102`, but no theorem there
or in the other returned sources states the orbit-specific conclusion that
the bounded future overhang of a long maximizing cube must first fail as
`2 -> 3`.  The algebraic identity

```
(AB)^m A=A(BA)^m
```

is standard word conjugacy and needs no specialized imported theorem.  An
internal archive search found the related square-shadow and fixed-origin
maturation mechanisms already proved in `golden_bad_cuts.md` and
`root_episodes.md`; the new note `bounded_overhang_maturation.md` therefore
records a synthesis with the one-sided return-boundary theorem rather than
claiming priority.  This was a scoped literature search, not an exhaustive
novelty determination.
