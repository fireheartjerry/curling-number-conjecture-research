# Curling Number Conjecture Research Ledger

## Status

-   **No complete proof or counterexample yet.**
-   This is a handoff document containing our strongest reductions and
    current frontier.

## Core reductions

-   Shifted analysis to **strict record witness periods** `S = X Y^K`.
-   Derived adjacent shortest cube periods are either equal or differ by
    **more than a factor of two** (Fine--Wilf overlap).
-   Eliminated the `K >= 4` record branch via the circular short-cube
    route (subject to the cited local-period theorem being used
    correctly and fully audited).

## Binary hard core

Remaining record exponents: - `K = 2` - `K = 3`

Everything else has effectively been pushed aside.

## Record cube theorem

For `K = 3`: - The entire record cube is generated internally. -
`Y^2 -> Y^3` is autonomous. - No older left context is needed.

## Record square bridge theorem

For `K = 2`: - Every record square root has structure

    Y = B A B

with

    |AB| = q > P/2.

Squares are the only mechanism importing old left-context.

## Context localization

Only an initial prefix of a record square can depend on older history.
The remainder of the square is autonomous.

## Renormalization hierarchy

Observed:

    4² -> 6² -> 7² -> 21³

which lifts to

    114² -> 186² -> 207² -> 621³

This is a genuine recursive structure but **not** yet a counterexample
because every larger stage still requires additional left boundary
information.

## Remaining conjectures

### Conjecture A

Every infinite surviving binary orbit contains infinitely many strict
record cubes.

### Conjecture B

For consecutive surviving record cubes

    X1 Y1³
    X2 Y2³

prove

    |X2| < |X1|.

This would immediately force infinite descent.

## Current finish line

Prove:

> Every record square bridge necessarily imports a witness that crosses
> the previous record cube's left boundary.

If true:

1.  every surviving record cube moves the frontier left,
2.  infinitely many record cubes imply an infinite strictly decreasing
    frontier,
3.  contradiction,
4.  Curling Number Conjecture follows (for the binary core).

## Important corrections

-   A proposed gcd-connectivity theorem for the equality graph was found
    false (counterexample at P=12) and discarded.
-   Every reduction must be adversarially audited before use.
