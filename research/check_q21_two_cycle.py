"""Direct audit of the forced U/B equal-scale predecessor two-cycle."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from curling import curling_number


U = tuple(map(int, "223232223222322322232"))
B = tuple(map(int, "223222323222322232232"))
P = len(U)
U_PHASE = 4
B_PHASE = 8
U_TO_B = 3 * P - U_PHASE
B_TO_U = 3 * P - B_PHASE
CYCLE = U_TO_B + B_TO_U


def place(target, start, word):
    for offset, value in enumerate(word):
        coordinate = start + offset
        previous = target.get(coordinate)
        if previous is not None:
            assert previous == value
        target[coordinate] = value


def cycle_word():
    # Put a predecessor U^3 at 0, the intervening B^3 at 55, and the
    # next U^3 at 114.  The overlaps are respectively eight and four.
    line = {}
    place(line, 0, U * 3)
    place(line, B_TO_U, B * 3)
    place(line, CYCLE, U * 3)
    assert set(range(0, CYCLE + 3 * P)) <= set(line)
    return tuple(line[i] for i in range(CYCLE))


def main():
    assert P == 21
    assert U_TO_B == 59
    assert B_TO_U == 55
    assert CYCLE == 114

    # Equal-root cubes ending at the selected phases have the required
    # overlap suffixes.
    assert (B * 3)[-U_PHASE:] == U[:U_PHASE]
    assert (U * 3)[-B_PHASE:] == B[:B_PHASE]

    # Consecutive predecessor cubes cover without a gap.
    current_u = (0, 63)
    predecessor_b = (-59, 4)
    predecessor_u = (-114, -51)
    assert min(current_u[1], predecessor_b[1]) - max(
        current_u[0], predecessor_b[0]
    ) == 4
    assert min(predecessor_b[1], predecessor_u[1]) - max(
        predecessor_b[0], predecessor_u[0]
    ) == 8

    w = cycle_word()
    expected = U * 3 + (B * 3)[8:59]
    assert len(w) == len(expected) == CYCLE
    assert w == expected

    # Four completed ancestry cycles force an actual fourth power at the
    # current 3-cut.  This is evaluated by the reference curling-number
    # implementation, not inferred by inspection.
    four = w * 4
    value = curling_number(four)
    assert value >= 4
    # The same periodic tail at the U^3 endpoint is the 63-shifted bridge.
    # That endpoint is the selected 3-cut in the next B node.
    endpoint_block = w[3 * P :] + w[: 3 * P]
    endpoint_value = curling_number(endpoint_block * 4)
    assert endpoint_value >= 4

    # The finite circular proper profile of one bridge has precisely the
    # two familiar missing-square cuts.  This is diagnostic only; the
    # fourth-power contradiction above is the load-bearing conclusion.
    circular = w * 3
    profile = tuple(
        curling_number(circular[: len(w) + phase])
        for phase in range(len(w))
    )
    holes = tuple(
        phase
        for phase, (wanted, actual) in enumerate(zip(w, profile))
        if wanted != actual
    )
    assert holes == (9, 10)
    assert tuple(profile[phase] for phase in holes) == (1, 1)
    assert tuple(w[phase] for phase in holes) == (2, 2)

    print(f"|U|=|B|={P}")
    print(f"displacements={U_TO_B},{B_TO_U}; cycle={CYCLE}")
    print("W=" + "".join(map(str, w)))
    print(f"cn(W^4)={value}")
    print(f"cn(rot63(W)^4)={endpoint_value}")
    print(f"proper-profile holes={holes}")


if __name__ == "__main__":
    main()
