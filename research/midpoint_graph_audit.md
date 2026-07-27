# Minimal-square midpoint graph under admissibility and fixedness

Let `Q` be a primitive circular word of length `q`.  At a cut `c`, let
`mu(c)` be the least proper root length of a square ending at `c`, and
put

`M(c)=c-mu(c) mod q`.

The letter immediately preceding a cut is preserved by `M`, because the
two copies in the square have the same final letter.

This note audits two proposed properties:

1. every directed cycle of `M` has winding number one;
2. for each preceding-letter color, `M` has at most one directed cycle.

The second property is false even after imposing the actual admissibility
hypothesis `pc_Q(c) in {2,3}` at every cut.  The first property survives
the computations recorded below, but no proof is supplied.

The direct certificate is checked by
`research/check_midpoint_counterexample.py`.  The exhaustive range audit
is `research/search_admissible_midpoint.cpp`.

## 1. Admissible counterexample

Take

`W=3323223323232233232322`, `q=22`.

The exact proper circular exponent profile is

`pc_W=2223332222222322222223`.

Thus every cut ends in a proper square, no cut ends in a proper fourth
power, and `pc_W(c)` belongs to `{2,3}` at every phase.

The word is primitive.  Since `22` has proper divisors `1,2,11`, only
those three candidate power periods need testing.  Periods 1 and 2 fail
at index 2, where `W[2]=2` and `W[0]=3`; period 11 fails at index 12,
where `W[12]=2` and `W[1]=3`.

The complete sets of proper circular square-root lengths are:

| cut | all roots | `mu` |
|---:|:---|---:|
| 0 | `1,8` | 1 |
| 1 | `8` | 8 |
| 2 | `1,8` | 1 |
| 3 | `8` | 8 |
| 4 | `8` | 8 |
| 5 | `2,8` | 2 |
| 6 | `1` | 1 |
| 7 | `6` | 6 |
| 8 | `1,6` | 1 |
| 9 | `6` | 6 |
| 10 | `6` | 6 |
| 11 | `2,6` | 2 |
| 12 | `2` | 2 |
| 13 | `2` | 2 |
| 14 | `1` | 1 |
| 15 | `14` | 14 |
| 16 | `1,14` | 1 |
| 17 | `8,14` | 8 |
| 18 | `8,14` | 8 |
| 19 | `2,8,14` | 2 |
| 20 | `2,8` | 2 |
| 21 | `2,8` | 2 |

The resulting parent vector is

`(21,15,1,17,18,3,5,1,7,3,4,9,10,11,13,1,15,9,10,17,18,19)`.

It has three cycles:

* `(17,9,3)`, with roots `(8,6,8)` and preceding colors `(2,2,2)`;
* `(1,15)`, with roots `(8,14)` and preceding colors `(3,3)`;
* `(4,18,10)`, with roots `(8,8,6)` and preceding colors `(3,3,3)`.

The last two are distinct cycles with the same preserved color 3.  This
directly disproves same-color uniqueness under primitivity,
squarefulness, and proper-fourth-power-freeness.  Each cycle's root
lengths sum to 22, so all three cycles have winding number one.

The root table is a finite certificate rather than an inference from the
search that found the word: every candidate root length from 1 through
21 is tested at every cut.  Nonemptiness proves circular squarefulness,
and the first entry in each row proves the displayed minimal root.

## 2. Smallest binary admissible certificate

`research/search_admissible_midpoint.cpp` enumerates all `2^n` binary
words at each length.  It rejects imprimitive words, computes the proper
exponent at every cut using every proper root, retains exactly profiles
in `{2,3}`, computes every shortest square root, and then enumerates all
directed cycles of `M`.

For lengths 1 through 21, no retained word has two cycles of the same
preceding color.  At length 22 there are 264 retained words and 44 have
same-color multiple cycles; the first emitted word is `W`.  Therefore
`W` is a smallest binary counterexample under this exhaustive
enumeration.  This minimality statement is finite computational
verification, not a general structural theorem.

## 3. What fixedness adds

The counterexample is not profile-fixed:

`pc_W != W`.

For a profile-fixed word `pc_Q=Q`, a midpoint cycle of preceding color
`a` has an additional decoration absent from the local
prefix-comparability lemma:

`pc_Q(c-1)=Q[c-1]=a`

at every cycle node `c`.

Thus a color-3 cycle has a proper cube ending at every immediately
preceding phase, while a color-2 cycle has exponent exactly two there.
Proper-fourth-power-freeness alone does not link these numeric exponents
to the word's letter colors.

The two color-3 cycles of `W` fail this local compatibility explicitly.
For cycle `(1,15)`, the predecessor phases are `(0,14)` and their profile
values are `(2,2)`.  For cycle `(4,18,10)`, the predecessor phases are
`(3,17,9)` and their profile values are `(3,2,2)`.  Hence neither
same-color pair can occur unchanged in a fixed profile.

As a more focused finite test, the exhaustive program counted cycles
that satisfy this predecessor-label compatibility even when the whole
word is not fixed.  Through binary length 25, no admissible word has two
compatible cycles of one color.  This is evidence only.  A proof would
have to use the overlap between:

* the minimal square ending at `c`, whose midpoint defines `M(c)`; and
* the square or cube ending at the adjacent cut `c-1`, prescribed by
  `pc_Q(c-1)=Q[c-1]`.

Saari's prefix-comparability lemma compares minimal squares at a square's
endpoint and midpoint.  It does not use the exponent at the adjacent cut
`c-1`, so it cannot by itself exploit profile fixedness.

For the executed fixed word

`Q=223222322232322232223`,

the midpoint cycles are

`(0,17,11,7)` with roots `(4,6,4,7)` and preceding color 3,

`(1,18,12,8,4)` with roots `(4,6,4,4,3)` and preceding color 2.

Both sums are 21, and there is one cycle of each color.  Exhaustive binary
enumeration through length 25 finds no fixed words below length 21, the
21 rotations of this word at length 21, and none at lengths 22 through
25.

## 4. Winding status

No winding greater than one was found:

* for all primitive circular squareful ternary words through length 16;
* for all primitive admissible binary words through length 26;
* for the fixed length-21 word above.

These computations do not prove winding one.  A winding-`h` cycle has
positive root lengths whose sum is `h q`; the local
prefix-comparability inequalities `2 mu(M(c))>mu(c)` do not by themselves
turn that arithmetic identity into `h=1`.  No well-founded or
noncrossing argument closing this gap has been established here.

## 5. Route disposition

Same-color uniqueness is closed at the admissible level: the explicit
word `W` satisfies every admissibility hypothesis and falsifies it.
Fourth-power-freeness is not the missing mechanism.

The only surviving version is profile-fixed uniqueness, or the weaker
predecessor-label-compatible uniqueness isolated in Section 3.  Reopening
that route requires a new adjacent cube/square overlap argument.  Winding
one is also a separate surviving conjectural lemma; finite searches and
the local root-length inequality are not a proof.
