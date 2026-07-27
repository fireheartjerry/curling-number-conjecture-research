# Exact gap coding at successive `2` cuts

This note records an exact translation and a local obstruction.  It is not
a proof of the Curling Number Conjecture.

## The code

In an eventual `{2,3}` output tail, let the successive positions carrying
`2` be `t_j`.  Put

```
d_j = t_j-t_(j-1) in {1,2,3},
h(d) = 2 3^(d-1).
```

Thus the output from `t_(j-1)` through `t_j-1` is `h(d_j)`.

Consider a raw suffix power `Y^k`, `k>=2`, ending at a `2` cut, and assume
that this whole suffix lies in the coded tail.  If `Y` contains a `2`,
there are unique data

```
a in {0,1,2},     G in {1,2,3}*,     d in {1,2,3}
```

such that

```
Y = 3^a h(Gd).
```

Validity of the internal junctions of `Y^k` forces `d+a<=3`.  Direct
concatenation gives the exact identity

```
Y^k = 3^a h((G(d+a))^(k-1) Gd).                 (1)
```

When `a=0`, this is an aligned gap power `(Gd)^k`.  When `a>0`, the
initial `3^a` is the final part of a preceding gap `b`, where `b>=a+1`.
Consequently the exact gap suffix is

```
b (G(d+a))^(k-1) Gd,       b>=a+1.              (2)
```

Conversely, (2) gives the raw power in (1) by starting at the last `a`
copies of `3` in `h(b)`.  A primitive root containing no `2` is the
one-letter root `3`; at a `2` cut this is exactly the terminal-gap
exception `d_j=3`.

It follows that raw curling number two at a coded cut is equivalent to the
existence of an aligned square, a pointed square of form (2), or the
terminal `33`, together with exclusion of every corresponding certificate
with exponent at least three.  Powers crossing the fixed prefix are not
covered until their left endpoint enters the coded tail.

## Transport versus genuine birth

Use case 1 of Lemma 9 in `reductions.md`:

```
V=FD,
S_t=QFDF,
S_s=Q(FD)^2,
D=h(d).
```

Write `F=3^a h(G)`.  In the pointed case `a>0`, let `b` be the gap
containing the first displayed `3^a`.  Then

```
Q ends in D   iff   b=d+a.                       (3)
```

Indeed, before the final `a` threes of `h(b)` there are exactly
`b-1-a` threes after its leading `2`; the last `d` raw symbols there equal
`h(d)` exactly when `b-1-a=d-1`.

Therefore a pointed genuine birth has `b!=d+a`.  The inequalities
`a>0`, `b>=a+1`, and `d+a<=3` leave exactly

```
(a,d,b)=(1,1,3)  or  (1,2,2).
```

In particular `a=2` always transports.  The two remaining cases really
occur and are not eliminated by the intervening exact labels.

## Executed obstruction to a scale descent

`check_gap_word_translation.py` recomputes the following using both
curling-number implementations.  Start from

```
B = 23233223233223233.
```

Its orbit labels are

```
2,3,2,2,2,3,1.
```

At the successive `2` cuts `0 -> 2`, the gap is `D=23`.  The old
maximizing-root lengths are `{1,6}`.  The later state has the unique
maximizing root

```
V=323,   |V|=3.
```

Here `F=3`, the old suffix is `FDF=3233`, and the remaining prefix ends in
`2`, not in `D=23`.  This is the genuine pointed case `(a,d,b)=(1,2,2)`;
the intervening state has curling number exactly three.

At the immediately following successive cuts `2 -> 3`, the old unique
root has length three and the new unique root is

```
V=32,    |V|=2.
```

Again the birth is genuine: the remaining prefix ends in `3`, not
`D=2`.  This is `(a,d,b)=(1,1,3)`.  Thus, in one deterministic orbit,
the least maximizing-root scale first expands from `1` to `3` and then
drops from `3` to `2`.  The prior-square equation, exact intervening
labels, and pointed defect order do not supply a monotone scale parent.

The length-eight seed `23222323` gives a second obstruction.  Its executed
58-step tail contains identical pointed-root equations shifted by 21 raw
positions: roots of lengths `3,7,2,6,10` at cuts

```
13,17,22,26,30
```

recur at

```
34,38,43,47,51.
```

All are exact curling-number-two states.  Hence even the complete pointed
root word and its defect edge can reset exactly while a longer aligned
root crosses the retained context.

