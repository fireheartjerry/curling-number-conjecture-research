"""SMT falsifier for proper-curl profiles whose labels are token weights."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Int, Or, Solver, sat  # type: ignore[import-not-found]


def power(q, cut: int, root: int, exponent: int):
    n = len(q)
    return And(*(q[(cut - block * root + j) % n]
                 == q[(cut - root + j) % n]
                 for block in range(2, exponent + 1)
                 for j in range(root)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int)
    parser.add_argument("alphabet", type=int, nargs="?", default=3)
    parser.add_argument("--all-two", action="store_true")
    parser.add_argument(
        "--mixed",
        action="store_true",
        help="require that both profile weights 2 and 3 occur",
    )
    args = parser.parse_args()
    n, sigma = args.length, args.alphabet
    q = [Int(f"q_{i}") for i in range(n)]
    weight = [Int(f"w_{a}") for a in range(sigma)]
    s = Solver()
    s.add(*(And(0 <= x, x < sigma) for x in q))
    s.add(*(And(2 <= x, x <= 3) for x in weight))
    if args.all_two:
        s.add(*(x == 2 for x in weight))
    if args.mixed:
        s.add(Or(*(x == 2 for x in weight)))
        s.add(Or(*(x == 3 for x in weight)))
    s.add(q[0] == 0)
    s.add(*(Or(*(x == a for x in q)) for a in range(sigma)))
    for p in range(1, n):
        if n % p == 0:
            s.add(Or(*(q[i] != q[i % p] for i in range(p, n))))
    for cut in range(n):
        square = Or(*(power(q, cut, root, 2) for root in range(1, n)))
        cube = Or(*(power(q, cut, root, 3) for root in range(1, n)))
        fourth = Or(*(power(q, cut, root, 4) for root in range(1, n)))
        s.add(square)
        label_three = Or(*(
            And(q[cut] == a, weight[a] == 3) for a in range(sigma)
        ))
        s.add(label_three == cube)
        s.add(~fourth)
    result = s.check()
    if result != sat:
        print(f"length={n} alphabet={sigma} result={result}")
        return
    m = s.model()
    word = tuple(m.eval(x).as_long() for x in q)
    weights = tuple(m.eval(x).as_long() for x in weight)
    print("word=" + "".join(map(str, word)))
    print("weights=" + "".join(map(str, weights)))
    print(f"length={n} alphabet={sigma} result=sat")


if __name__ == "__main__":
    main()
