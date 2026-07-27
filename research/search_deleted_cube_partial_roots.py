"""Enumerate binary roots surviving inherited-cube constraints.

This is exploratory evidence only. Every proper circular root length is checked.
"""

from __future__ import annotations

from itertools import product

from check_deleted_cube_profile_inheritance import (
    deleted_cube,
    exact_profile_at,
    primitive,
)


def profile(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(exact_profile_at(word, cut)[0] for cut in range(len(word)))


def candidates(length: int):
    if length < 7:
        return
    fixed = {0: 2, 1: 3}
    suffix = (2, 2, 2, 3, 2)
    for offset, value in enumerate(suffix, start=length - len(suffix)):
        if offset in fixed and fixed[offset] != value:
            return
        fixed[offset] = value
    free = tuple(index for index in range(length) if index not in fixed)
    for values in product((2, 3), repeat=len(free)):
        word_list = [0] * length
        for index, value in fixed.items():
            word_list[index] = value
        for index, value in zip(free, values):
            word_list[index] = value
        word = tuple(word_list)
        if not primitive(word):
            continue
        pc = profile(word)
        if any(got > target for got, target in zip(pc, word)):
            continue
        if any(target == 3 and got != 3 for got, target in zip(pc, word)):
            continue
        holes = tuple(i for i, (got, target) in enumerate(zip(pc, word))
                      if target == 2 and got == 1)
        if not holes:
            continue
        macro = deleted_cube(word)
        macro_pc = profile(macro)
        failures = tuple(i for i, (got, target) in enumerate(zip(macro_pc, macro))
                         if got != target)
        yield word, pc, holes, failures


def main() -> None:
    for length in range(7, 19):
        rows = list(candidates(length))
        print(f"length={length} count={len(rows)}", flush=True)
        for word, pc, holes, failures in rows[:5]:
            print(
                "  B=" + "".join(map(str, word))
                + " pc=" + "".join(map(str, pc))
                + f" holes={holes} Qfail={failures[:12]}"
            )


if __name__ == "__main__":
    main()
