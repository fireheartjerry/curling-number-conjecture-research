"""Exact unequal colored-exit parent cycle inside the Q21 profile.

Q21 is the primitive circular fixed profile

    223222322232322232223.

Every 3 is an isolated H_3 component.  At the cut after the following
2, the colored marker is ``32``.  Choosing the least primitive maximizing
root defines a parent map between these marker cuts.

The resulting recurrent cycle has constant component length, constant
separator color, and unequal rescue-root lengths.  Unlike the formal M=6
model, every cut of this word satisfies the complete proper curling
profile.
"""

from __future__ import annotations

from check_run_length_grammar import (
    primitive,
    proper_profile,
    word_power_root_lengths,
)


Q21 = tuple(map(int, "223222322232322232223"))


def main() -> None:
    n = len(Q21)
    assert primitive(Q21)
    assert proper_profile(Q21) == Q21
    marker_cuts = tuple(
        (phase + 2) % n
        for phase, value in enumerate(Q21)
        if value == 3 and Q21[(phase + 1) % n] == 2
    )
    records = {}
    for cut in marker_cuts:
        exponent = Q21[cut]
        roots = word_power_root_lengths(Q21, cut, exponent)
        assert roots
        least = roots[0]
        parent = (cut - least) % n
        assert parent in marker_cuts
        # The adjacent H_3 component is the singleton 3, preceded and
        # followed by the exit color 2.
        assert Q21[(cut - 3) % n] == 2
        assert Q21[(cut - 2) % n] == 3
        assert Q21[(cut - 1) % n] == 2
        records[cut] = {
            "label": exponent,
            "roots": roots,
            "least_root": least,
            "parent": parent,
            "H3_length": 1,
            "separator": 2,
        }

    start = 1
    cycle = []
    current = start
    while current not in cycle:
        cycle.append(current)
        current = records[current]["parent"]
    assert current == start
    cycle_roots = tuple(records[cut]["least_root"] for cut in cycle)
    assert cycle == [1, 18, 12, 8, 4]
    assert cycle_roots == (4, 6, 4, 4, 3)
    assert len(set(cycle_roots)) > 1
    print(
        {
            "word": "".join(map(str, Q21)),
            "proper_profile_exact": True,
            "marker_cuts": marker_cuts,
            "records": records,
            "least_root_parent_cycle": tuple(cycle),
            "cycle_roots": cycle_roots,
        }
    )


if __name__ == "__main__":
    main()
