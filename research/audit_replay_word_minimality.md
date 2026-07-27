# Replay-word minimality does not transfer

This note audits the use of the terminal-prefix inequality

```
cn(P[:-1]) < P[-1]
```

for the critical replay word produced by the shortest-seed deletion
argument.  The inequality is valid only when that replay word is the
original minimum-length counterseed.  In the longer-root branch the
orbit rule gives equality instead.

## Setup

Let `S` be a nonterminating seed of globally minimum length `n`, and
compare its orbit with the terminating orbit of `S[1:]`.  At their first
different output, the standard whole-power argument gives

```
high state = P^k,
low state  = P[1:] P^(k-1),
```

where `P` is primitive and the displayed curling numbers are `k` and
`k-1`.

Put `p=|P|`.  There are three logically different cases.

## 1. The short-root case `p<n`

Here minimum seed length says that the standalone word `P` terminates.
The state `P^k` may nevertheless lie on the nonterminating orbit because
the orbit did not start from `P`; it entered the displayed power with
left context already present.  Therefore `P` is not a counterseed to
which minimum-counterseed terminal-prefix reasoning can be applied.

## 2. The equal-root case `p=n`

The length-`p` prefix of the high state is the original seed, so

```
P=S.
```

Now `P[:-1]` has length below `n` and terminates.  If

```
cn(P[:-1])=P[-1],
```

its first orbit step reaches the nonterminating state `P`, a
contradiction.  The circular fixed-profile upper bound

```
cn(P[:-1])<=P[-1]
```

therefore gives the strict terminal-prefix inequality.  This is the
only branch in which global minimum seed length supplies that
inequality.

## 3. The long-root case `p>n`

Every prefix of the nonterminating orbit word whose length is at least
`n` is an orbit state: the process appends exactly one symbol per step.
Since the high state begins in `P` and `p>n`, the words

```
P[:-1], P
```

are consecutive states, at times `p-n-1` and `p-n`.  The appended symbol
which changes the former into the latter is its curling number.  Hence

```
cn(P[:-1])=P[-1].                                  (1)
```

Thus the desired strict inequality does not merely lack a proof in the
long-root branch; it is false there.

The first-symbol deletion behaves differently.  At the time the high
orbit reaches `P`, the still-synchronized low orbit has reached `P[1:]`.
Consequently `P[1:]` is a state on the terminating deleted orbit, while
`P` is a state on the nonterminating orbit.  The critical replay
equations and the later state

```
rot_left(P)^3
```

on the terminating branch remain valid.  What fails is only the
unjustified transfer of *last-symbol* predecessor minimality to `P`.

## Executed calibration

`research/check_replay_word_minimality.py` reconstructs the calibration
already used in `research/shortest_seed_normal_form.md`.  Starting from

```
S=223222323
```

the executed orbit reaches

```
P=223222323222322232232
```

after twelve extensions.  Both independent curling-number
implementations return

```
cn(P[:-1])=2=P[-1].
```

The computation is only a calibration.  Equation (1) follows directly
from the orbit rule for every long replay root.

## Consequence

Every argument in the final-`2` or final-`3` terminal-prefix route which
uses

```
cn(P[:-1])<P[-1]
```

must be stated conditionally on either

```
|P|=|S|
```

or an independently proved terminal-prefix drop.  A generic critical
replay word supplied by the shortest-seed normal form does not satisfy
that hypothesis.
