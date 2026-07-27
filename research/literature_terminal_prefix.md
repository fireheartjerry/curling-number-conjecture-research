# Literature check for the circular terminal-prefix branch

Search date: 2026-07-23.

This note records a background-literature search.  It deliberately did not
search for a solution of the Curling Number Conjecture.

## Queries

The following query families were used:

* `combinatorics on words circular squareful words every position begins
  square theorem`;
* `squareful words minimal squares Saari`;
* `characteristic sequence positions where cubes occur word encodes
  repetitions`;
* `one hole periodicity theorem word combinatorics Fine Wilf partial words
  one mismatch`;
* `critical factorization theorem local period precise statement`;
* `runs theorem periodicity overlap squares cubes word endpoints`.

No source found in these searches studies a word whose letters are the
characteristic function of its own proper circular cube endpoints.  In
particular, no located result directly implies the circular terminal-prefix
lemma.

## Located results and exact scope

### Fine--Wilf

The standard statement located in the survey/search material is:

> If a word of length at least `p+q-gcd(p,q)` has periods `p` and `q`,
> then it has period `gcd(p,q)`.

Source: Fine and Wilf, *Uniqueness theorems for periodic functions*,
Proc. Amer. Math. Soc. 16 (1965), as restated in M. Lothaire,
*Algebraic Combinatorics on Words*, Chapter 8,
<https://doi.org/10.1017/CBO9781107326019.009>.

This theorem is applicable to overlap comparisons between two concrete
power witnesses.  It does not create the second period or propagate a
cube endpoint through a one-symbol defect, so it does not by itself prove
the target lemma.

### Berstel--Boasson one-hole extension

Berstel and Boasson define a partial word as a partial map from positions
to an alphabet and prove a Fine--Wilf variant for partial words with one
hole; they also state that the analogous elementary compatibility
properties fail once two holes are allowed.

Source: Jean Berstel and Luc Boasson, *Partial words and a theorem of Fine
and Wilf*, Theoretical Computer Science 218 (1999), 135--141,
<https://www-igm.univ-mlv.fr/~berstel/Articles/1999PartialWords.pdf>.

The terminal-prefix branch has a specified mismatching symbol, rather than
an unspecified hole, and a family of endpoint-existence predicates with
different root lengths.  The one-hole theorem can be used only after two
actual periods have been put on one common partial word.  It supplies no
direct endpoint-characteristic result.

### Critical factorization theorem

The located precise formulation says that every word of length at least
two has a factorization at which the minimal local period equals the
global period.  A local repetition at `w=uv` is a nonempty word suffix
comparable with `u` and prefix comparable with `v`; the local period is
the shortest such repetition.

Sources:

* Berstel and Perrin, *Combinatorics on Words -- A Tutorial*, Section 3.2,
  <https://www-igm.univ-mlv.fr/~berstel/Articles/2003TutorialCoWdec03.pdf>;
* Tero Harju, *Critical factorisation in square-free words*,
  <https://arxiv.org/abs/2107.09421>.

This theorem guarantees a critical cut for a chosen finite word.  It does
not identify that cut with either distinguished endpoint and has no
hypothesis connecting letters `2,3` to cube endpoints.

### Squareful words

Currie and Rampersad prove:

* there exists an infinite `7/3`-power-free binary word containing a
  square beginning at every position (Theorem 3.3);
* for every real `alpha>2`, there exists an infinite
  `alpha`-power-free binary word containing a square beginning at every
  position (Theorem 3.4).

They distinguish this from Saari's term *squareful*, which additionally
requires only finitely many distinct minimal squares.

Source: James D. Currie and Narad Rampersad, *Infinite words containing
squares at every position*, RAIRO 44 (2010), 113--124,
<https://www.numdam.org/article/ITA_2010__44_1_113_0.pdf>.

Saari's result located through the same literature is that every
aperiodic squareful sequence has at least six minimal squares, and six is
attained.  Those results concern infinite words, squares beginning at
positions, and bounded sets of minimal squares.  The current object is a
finite circular word, powers end at cuts, and the load-bearing extra
condition is the self-encoded cube-endpoint profile.  Hence the squareful
classification does not transfer.

### Runs

The runs theorem states that the number of runs (maximal periodicities) in
a word of length `n` is below `n`.

Source: Bannai et al., *The "Runs" Theorem*,
<https://arxiv.org/abs/1406.0263>.

This is a counting bound.  It neither forces a particular terminal power
to fit before the distinguished origin nor relates the existence of a
run ending at a cut to the letter at that cut.

## Conclusion of the literature check

The only immediately reusable published mechanism is Fine--Wilf (and,
where an actual one-hole periodic word is constructed, its partial-word
extension).  The circular terminal-prefix lemma still requires a new
endpoint-propagation argument.  In particular, the existing squareful
literature cannot be cited as if “a square at every position” forced
cubes or periodic termination; the cited constructions show that such
square coverage is compatible with avoiding powers above exponents
arbitrarily close to two.
