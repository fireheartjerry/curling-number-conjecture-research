"""Executed checks for the local one-residue obstructions.

No curling number is evaluated here.  The script checks the exact
run-code power equations used in Section 8 of
``gadget_cycle_structure.md``:

* a marker value b_j=3 gives a proper fourth power;
* ``22`` plus the forced span-one defect gadget shifts to a cube at
  offset r=1; and
* cyclic ``11`` gives a period-ten cube at the following r=0 cut.
"""

from __future__ import annotations

from itertools import product
import sys

from check_run_length_grammar import (
    defect_gadget,
    h_root_length,
    power_code_condition,
)
from explore_one_residue_codes import expand


def check(max_m: int = 12) -> None:
    checked_11 = checked_22 = checked_3 = 0
    for m in range(1, max_m + 1):
        for b in product((1, 2, 3), repeat=m):
            a = expand(b)
            for j, value in enumerate(b):
                if value == 3:
                    i = 3 * j + 2
                    assert power_code_condition(a, i, a[i], 1, 4)
                    assert h_root_length(a, i, a[i], 1) == 4
                    checked_3 += 1

                if value == 2 and b[(j - 1) % m] == 2:
                    i = 3 * j
                    gadget = defect_gadget(a, i, 1)
                    assert gadget is not None
                    assert gadget.alpha == 1 and gadget.beta == 2
                    assert power_code_condition(a, i, 1, 1, 3)
                    assert h_root_length(a, i, 1, 1) == 4
                    checked_22 += 1

                # For m=1, h=3 is the full code circumference and is
                # deliberately excluded by the proper-root condition.
                if (
                    m > 1
                    and b[(j - 2) % m] == 1
                    and b[(j - 1) % m] == 1
                ):
                    i = 3 * j
                    assert power_code_condition(a, i, 0, 3, 3)
                    assert h_root_length(a, i, 0, 3) == 10
                    checked_11 += 1

    # The exceptional one-marker cases used in the proof.
    a1 = expand((1,))
    assert all(defect_gadget(a1, 0, s) is None for s in (1, 2))
    a2 = expand((2,))
    assert defect_gadget(a2, 0, 1) is not None
    assert power_code_condition(a2, 0, 1, 1, 3)
    a3 = expand((3,))
    assert power_code_condition(a3, 2, a3[2], 1, 4)

    print(
        f"checked through |b|={max_m}: "
        f"11_obstructions={checked_11}, "
        f"22_shifts={checked_22}, "
        f"b=3_fourths={checked_3}"
    )


if __name__ == "__main__":
    bound = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    check(bound)
