# Exact return closure for a complete valuation block

Fix `M>=4`, put `A=M-1`, and encode `A` by `0` and `M` by
`1`.  Write

```
W_N = product_(1<=j<=N) 0^M 1^(1+v_M(j)),
A_h = W_(M^h).
```

Thus `A_0=0^M1` and `A_h=A_(h-1)^M1`.  Let `e<=M-2`,
let

```
F=A_h e,
```

and put a boundary immediately after every occurrence of `F`.  This
note isolates the exact obstruction to closing the return-word quotient
between identical copies of `A_h`.

The marker `F` is unbordered.  Every nonempty suffix ends in the lower
symbol `e`, whereas every proper prefix ends in one of the high symbols
`A,M`.

## 1. Proper suffixes of `A_h` cannot restart a top component

**Complete-block suffix lemma.**  No nonempty proper suffix of `A_h`
is a complete maximal `{A,M}`-component containing `M` when placed
immediately after a symbol below `A`.

Proof.  A top component beginning immediately after a lower symbol
starts with the block `0^M1`.  Every zero run in `A_h` has length
exactly `M`.  Hence a suffix which is itself such a component cannot
start inside a zero run or a one run: it starts at the beginning of
one of the displayed blocks.

Suppose the suffix starts at block `s+1` and contains `N=M^h-s`
blocks.  Since it ends at the end of `A_h`, its final one run has
length

```
1+v_M(M^h)=h+1.                                  (1)
```

The deterministic top-component rule says that a fresh component with
`N` completed blocks has final one-run length

```
1+v_M(N).                                        (2)
```

Equality of the integer words forces (1) and (2) to agree.  Therefore
`v_M(N)=h`.  The bounds `1<=N<=M^h` imply `N=M^h`, hence `s=0`.
The suffix is the whole word `A_h`, contrary to properness.

The argument also excludes a suffix contained in the final one run:
such a suffix begins with `M`, while a fresh top component begins with
`A`.

## 2. The exact unmatched-copy trichotomy

The next lemma is independent of the valuation form.  Let `F` be any
unbordered marker, and decompose a circular word into exact return words
from one `F`-boundary to the next.

Suppose an `a`-th power with primitive root `Y` of length `q` ends at
an `F`-boundary `b`, where

```
a>=2,                  q>=|F|.
```

Copying the terminal marker through the equal roots certifies the
boundaries

```
b, b-q, ..., b-(a-1)q.                            (3)
```

Put

```
z=b-(a-1)q,             x=z-q.
```

The aligned block `[z,z+q)` is a concatenation of whole returns,

```
B=G_1 G_2 ... G_m,                                (4)
```

and the unmatched first root satisfies

```
[x,z)=B.                                          (5)
```

Exactly one of the following occurs.

1. `x` is an `F`-boundary.  Then the missing token copy is aligned.
2. No occurrence of `F` straddles `x`.  If `H` is the return containing
   `x`, then

   ```
   H=J G_1                         with J nonempty. (6)
   ```

   In particular `|G_1|<|H|`.
3. An occurrence of `F` ends at `x+d`, where

   ```
   0<d<|F|,
   prefix_d(G_1)=suffix_d(F).                      (7)
   ```

Proof.  Let `ell=|G_1|`.  The terminal occurrence of `F` in `G_1`
is wholly contained in `[z,z+q)`, so (5) copies it to an occurrence
ending at `x+ell`.  If an earlier occurrence ends at `x+d`, then
`d<|F|`: for `d>=|F|`, that occurrence is wholly contained in
`[x,z)`, and (5) would copy an `F`-boundary to `z+d`, contradicting
that `G_1` is the first return after `z`.  Such an earlier occurrence
therefore straddles `x`, and equality (5) gives (7).

If there is no earlier occurrence, the first boundary after `x` is
`x+ell`.  When `x` is not itself a boundary, it lies strictly inside
the return `H` ending there.  Equality (5) identifies the suffix of
`H` beginning at `x` with `G_1`, which gives (6).  These alternatives
are disjoint and exhaustive.

## 3. Specialization to `F=A_h e`

Apply the trichotomy to the complete valuation marker `F=A_h e`.
In alternative 3 write

```
D=suffix_(d-1)(A_h).
```

Equation (7) says that the return `G_1` begins in

```
D e.                                             (8)
```

The symbol immediately before `G_1` is the lower exit symbol at the
end of the preceding marker.  If `d>=2`, the nonempty word `D`
therefore becomes a complete `{A,M}`-component followed by the lower
symbol `e`.  It contains `M`, because every nonempty suffix of `A_h`
contains a symbol from its final nonempty `M`-run.  It is a proper
suffix because `d<|F|`.  This contradicts the complete-block suffix
lemma.  Consequently alternative 3 has the single form

```
d=1,                  G_1 begins with e.          (9)
```

Thus identical complete valuation components eliminate every
high-symbol straddle.  The exact closure problem has only two defects:
the strict return extension (6), and the one-letter lower-symbol
straddle (9).  Equation (9) is not an ordinary lower-maximum fixed
profile: roots at subsequent lower cuts can still cross the preceding
copy of `A_h`.

## 4. Conditional maturation forced by a maximal lower exponent

Retain the one-letter straddle (9), and now write `a=P[b]` for the
actual exponent of the displayed root `Y`.  Since the unmatched copy
`[x,z)` equals the aligned block beginning in `G_1`, equation (9) says
that the first symbol of `Y` is `e`.

At the preceding root boundary `b-q`, the periodic state already ends
in

```
Y^(a-1).
```

The next displayed symbol there is the first symbol of the final copy
of `Y`, namely

```
P[b-q]=e.
```

Exactness at that cut therefore gives

```
e>=a-1.                                           (10)
```

This does not eliminate a generic square straddle.  It has a sharp
consequence in the maximal lower-exponent subcase

```
a=M-1.
```

Since every exit satisfies `e<=M-2`, equation (10) forces

```
e=M-2,              P[b-q]=M-2.                  (11)
```

The suffix `Y^(M-2)` attains the exact value in (11).  The `q`
successive displayed symbols from `b-q` to `b` are one literal copy of
`Y`, after which the suffix has matured to `Y^(M-1)` and the value at
`b` is `M-1`.  Thus a one-letter straddle at exponent `M-1` is not an
arbitrary lower exit: it is a visible

```
Y^(M-2)  ->  Y^(M-1)
```

suffix-maturation episode beginning with the maximal lower exit
`M-2`.

## 5. Executed counterexample to eliminating the last straddle locally

The one-letter case (9) is compatible with exact curling numbers at
both relevant cuts.  For every tested `4<=M<=10`, take the raw symbols

```
C=(M-1)^M M,
e=2,
F=C e,
Y=e F,
S=C Y^2 = F^2 e F.                               (10)
```

Executed code gives

```
cn(F^2)=2,       sole maximizing root length |F|,
cn(S)=2,         sole maximizing root length |Y|. (11)
```

The earliest copy of `Y` in `S` starts at the final `e` of the first
straddling marker `F`; the aligned copy starts immediately after the
second marker and also begins with `e`.  Hence (10) realizes `d=1`
with no larger competing exponent.

`research/check_top_return_straddle.py` recomputes (10)--(11) with
both curling-number implementations for every `M=4,...,10`.  This is a
local counterexample, not a circular fixed profile.  It proves that the
last step from (9) to a lower-maximum induction requires a genuinely
global compatibility argument; marker unborderedness and the local
power equation do not supply it.
