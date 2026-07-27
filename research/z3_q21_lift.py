"""Search two-return-word lifts of the binary length-21 weighted profile.

Token 2 is replaced by one raw return word R2 and token 3 by R3.  Each
return begins with its token weight and ends with the synchronized entrance
E=233334.  The resulting raw circular word is required to be a primitive
proper-curling fixed profile over {2,3,4}.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / ".vendor"))
from z3 import And, Bool, Not, Or, Solver, sat  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("length_r2", type=int)
    parser.add_argument("length_r3", type=int)
    parser.add_argument("--timeout-ms", type=int, default=0)
    args = parser.parse_args()
    a, b = args.length_r2, args.length_r3
    if a < 6 or b < 7:
        raise SystemExit("R2 needs length >=6 and R3 length >=7")

    token_word = tuple(map(int, "223222322232322232223"))
    entrance = (2, 3, 3, 3, 3, 4)

    # ge3/ge4 pairs encode raw return-word symbols 2,3,4.
    r2 = [(Bool(f"a3_{i}"), Bool(f"a4_{i}")) for i in range(a)]
    r3 = [(Bool(f"b3_{i}"), Bool(f"b4_{i}")) for i in range(b)]
    solver = Solver()
    if args.timeout_ms:
        solver.set(timeout=args.timeout_ms)
    for h, t in r2 + r3:
        solver.add(Or(Not(t), h))

    def fix(pair, value: int):
        h, t = pair
        if value == 2:
            solver.add(Not(h), Not(t))
        elif value == 3:
            solver.add(h, Not(t))
        else:
            solver.add(h, t)

    fix(r2[0], 2)
    fix(r3[0], 3)
    for block in (r2, r3):
        for pair, value in zip(block[-6:], entrance):
            fix(pair, value)

    q = []
    designated_entrance_starts = set()
    cursor = 0
    for token in token_word:
        block = r2 if token == 2 else r3
        q.extend(block)
        designated_entrance_starts.add(cursor + len(block) - 6)
        cursor += len(block)
    n = len(q)

    def equal_pair(x, y):
        return And(x[0] == y[0], x[1] == y[1])

    def equal(i: int, j: int):
        return equal_pair(q[i % n], q[j % n])

    def power(cut: int, root: int, exponent: int):
        return And(
            *(
                equal(cut - block * root + j, cut - root + j)
                for block in range(2, exponent + 1)
                for j in range(root)
            )
        )

    for cut in range(n):
        squares = [power(cut, root, 2) for root in range(1, n)]
        cubes = [power(cut, root, 3) for root in range(1, n)]
        fourths = [power(cut, root, 4) for root in range(1, n)]
        fifths = [power(cut, root, 5) for root in range(1, n)]
        solver.add(Or(*squares))
        solver.add(q[cut][0] == Or(*cubes))
        solver.add(q[cut][1] == Or(*fourths))
        solver.add(Not(Or(*fifths)))

    # Synchronization: the only E occurrences are the declared block suffixes.
    def is_entrance(start: int):
        clauses = []
        for offset, value in enumerate(entrance):
            h, t = q[(start + offset) % n]
            clauses.append(Not(h) if value == 2 else h)
            clauses.append(t if value == 4 else Not(t))
        return And(*clauses)

    for start in range(n):
        if start not in designated_entrance_starts:
            solver.add(Not(is_entrance(start)))

    # Primitive raw word.
    for period in range(1, n):
        if n % period == 0:
            solver.add(
                Or(
                    *(
                        Not(equal(i, i % period))
                        for i in range(period, n)
                    )
                )
            )

    result = solver.check()
    print(f"a={a} b={b} raw_length={n} result={result}")
    if result == sat:
        model = solver.model()

        def render(block):
            return "".join(
                "4"
                if model.eval(t)
                else "3"
                if model.eval(h)
                else "2"
                for h, t in block
            )

        print("R2=" + render(r2))
        print("R3=" + render(r3))


if __name__ == "__main__":
    main()
