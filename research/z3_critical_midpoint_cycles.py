"""Falsify midpoint-cycle claims under the full critical fitting equations.

This encodes a primitive binary word P with P[0]=2, pc_P=P, and a
first-copy-fitting maximizing witness at every cut.  Candidate midpoint
cycles are then imposed through exact *minimal* square-root equations.
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, PbEq, Solver, sat  # type: ignore


def build_base(n: int):
    is_three = [Bool(f"b_{i}") for i in range(n)]
    solver = Solver()
    solver.add(Not(is_three[0]))

    # Exclude every proper divisor period.
    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        is_three[i] != is_three[i % period]
                        for i in range(period, n)
                    )
                )
            )

    powers = {}
    for cut in range(n):
        for root in range(1, n):
            for exponent in (2, 3, 4):
                powers[cut, root, exponent] = And(
                    *(
                        is_three[(cut - block * root + j) % n]
                        == is_three[(cut - root + j) % n]
                        for block in range(2, exponent + 1)
                        for j in range(root)
                    )
                )

    minima = {}
    for cut in range(n):
        squares = [powers[cut, root, 2] for root in range(1, n)]
        solver.add(Or(*squares))
        cubes = [powers[cut, root, 3] for root in range(1, n)]
        solver.add(is_three[cut] == Or(*cubes))
        solver.add(
            Not(Or(*(powers[cut, root, 4] for root in range(1, n))))
        )

        fitting_squares = [
            powers[cut, root, 2]
            for root in range(1, n)
            if 2 * root <= n + cut - 1
        ]
        fitting_cubes = [
            powers[cut, root, 3]
            for root in range(1, n)
            if 3 * root <= n + cut - 1
        ]
        solver.add(Or(*fitting_squares) if fitting_squares else False)
        solver.add(
            (Or(*fitting_cubes) == is_three[cut])
            if fitting_cubes
            else Not(is_three[cut])
        )

        shorter = []
        for root in range(1, n):
            minima[cut, root] = And(
                powers[cut, root, 2],
                *(Not(square) for square in shorter),
            )
            shorter.append(powers[cut, root, 2])
    return solver, is_three, minima


def add_exact_cycle(solver, minima, cycle: tuple[int, ...], n: int):
    roots = tuple(
        (cycle[i] - cycle[(i + 1) % len(cycle)]) % n
        for i in range(len(cycle))
    )
    solver.add(*(minima[cut, root] for cut, root in zip(cycle, roots)))
    return roots


def random_cycle(
    rng: random.Random, n: int, size: int, winding: int
) -> tuple[int, ...] | None:
    cycle = tuple(rng.sample(range(n), size))
    roots = tuple(
        (cycle[i] - cycle[(i + 1) % size]) % n for i in range(size)
    )
    if sum(roots) != winding * n:
        return None
    if any(2 * roots[(i + 1) % size] <= roots[i] for i in range(size)):
        return None
    return cycle


def model_word(model, is_three):
    return "".join("3" if model.eval(x) else "2" for x in is_three)


def search_winding(args):
    solver, letters, minima = build_base(args.length)
    rng = random.Random(args.seed)
    seen = set()
    checked = 0
    for _ in range(args.trials):
        size = rng.randint(3, min(args.max_cycle, args.length))
        cycle = random_cycle(rng, args.length, size, 2)
        if cycle is None or cycle in seen:
            continue
        seen.add(cycle)
        solver.push()
        roots = add_exact_cycle(solver, minima, cycle, args.length)
        result = solver.check()
        checked += 1
        if result == sat:
            print(
                f"word={model_word(solver.model(), letters)} "
                f"cycle={cycle} roots={roots} winding=2"
            )
            return
        solver.pop()
    print(f"no_winding2_model checked={checked}")


def search_same_color(args):
    solver, letters, minima = build_base(args.length)
    rng = random.Random(args.seed)
    checked = 0
    for _ in range(args.trials):
        size1 = rng.randint(2, min(args.max_cycle, args.length // 2))
        size2 = rng.randint(2, min(args.max_cycle, args.length - size1))
        c1 = random_cycle(rng, args.length, size1, 1)
        c2 = random_cycle(rng, args.length, size2, 1)
        if c1 is None or c2 is None or set(c1) & set(c2):
            continue
        solver.push()
        r1 = add_exact_cycle(solver, minima, c1, args.length)
        r2 = add_exact_cycle(solver, minima, c2, args.length)
        # The midpoint map preserves the preceding letter on each cycle.
        # Require the two cycles to have the same preserved color.
        solver.add(letters[(c1[0] - 1) % args.length] ==
                   letters[(c2[0] - 1) % args.length])
        result = solver.check()
        checked += 1
        if result == sat:
            print(
                f"word={model_word(solver.model(), letters)} "
                f"cycle1={c1} roots1={r1} cycle2={c2} roots2={r2}"
            )
            return
        solver.pop()
    print(f"no_same_color_model checked={checked}")


def search_same_color_direct(args):
    solver, letters, minima = build_base(args.length)
    n = args.length
    groups = [
        [Bool(f"cycle_group_{group}_{cut}") for cut in range(n)]
        for group in range(2)
    ]
    color = Bool("common_preceding_color")
    for group in groups:
        solver.add(Or(*group))
        for cut in range(n):
            # Closure under the exact midpoint successor.
            solver.add(
                Or(
                    Not(group[cut]),
                    Or(
                        *(
                            And(
                                minima[cut, root],
                                group[(cut - root) % n],
                            )
                            for root in range(1, n)
                        )
                    ),
                )
            )
            incoming = []
            for source in range(n):
                root = (source - cut) % n
                if root:
                    incoming.append(
                        (And(group[source], minima[source, root]), 1)
                    )
            # Together with closure, indegree one makes the selected
            # subgraph a nonempty union of directed cycles (no trees).
            solver.add(group[cut] == PbEq(incoming, 1))
            solver.add(
                Or(
                    Not(group[cut]),
                    letters[(cut - 1) % n] == color,
                )
            )
    solver.add(
        *(Or(Not(groups[0][cut]), Not(groups[1][cut])) for cut in range(n))
    )
    if solver.check() != sat:
        print("no_same_color_model_direct")
        return
    model = solver.model()
    selected = [
        tuple(c for c in range(n) if model.eval(group[c]))
        for group in groups
    ]
    print(
        f"word={model_word(model, letters)} "
        f"selected1={selected[0]} selected2={selected[1]}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument(
        "mode",
        choices=("winding", "same-color", "same-color-direct", "base"),
    )
    parser.add_argument("--trials", type=int, default=10000)
    parser.add_argument("--max-cycle", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260723)
    args = parser.parse_args()
    if args.mode == "base":
        solver, letters, _ = build_base(args.length)
        if solver.check() == sat:
            print(f"word={model_word(solver.model(), letters)}")
        else:
            print("base_unsat")
    elif args.mode == "winding":
        search_winding(args)
    elif args.mode == "same-color-direct":
        search_same_color_direct(args)
    else:
        search_same_color(args)


if __name__ == "__main__":
    main()
