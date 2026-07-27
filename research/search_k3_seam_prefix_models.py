"""Find finite orbit-prefix models of the residual bordered k=3 seam.

The search retains substantially more than the static word equation:

* ``W=Y^3`` has exact curling number 3 and its deletion has value 2;
* ``Y`` is primitive with a proper border ``U``;
* ``Q=C Y^2`` begins with 3 and is primitive;
* the actual orbit from ``W`` outputs ``Q[:2|Y|+1]``;
* at the forced seam state ``Y^3 (CU)^2`` a maximizing cube root is
  strictly shorter than ``Y``.

Returned words are finite and their tail lengths are computed.  They are
countermodels only to automatic child-profile/status inheritance, never to
the Curling Number Conjecture.
"""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference, tail_length
from research.check_run_length_grammar import primitive, proper_profile


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def maximizing_roots(word: Word) -> tuple[int, tuple[int, ...]]:
    value = exact_cn(word)
    roots = tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :] == word[-root:] * value
    )
    assert roots
    return value, roots


def find_model(branch: str, max_root: int = 16):
    if branch not in {"contained", "crossing"}:
        raise ValueError(branch)
    for r in range(2, max_root + 1):
        for y in product((2, 3), repeat=r):
            if not primitive(y):
                continue
            for h in range(1, r):
                if y[:h] != y[-h:]:
                    continue
                if not h < r - gcd(r, h):
                    continue
                u = y[:h]
                c = y[h:]
                if c[0] != 3:
                    continue
                q = c + y + y
                if not primitive(q):
                    continue

                w = y * 3
                if exact_cn(w) != 3 or exact_cn(w[1:]) != 2:
                    continue

                state = w
                valid = True
                for time in range(2 * r + 1):
                    if exact_cn(state) != q[time]:
                        valid = False
                        break
                    if time < 2 * r:
                        state += (q[time],)
                if not valid:
                    continue

                value, roots = maximizing_roots(state)
                assert value == 3
                selected_roots = tuple(
                    root
                    for root in roots
                    if (root < r) == (branch == "contained")
                    and root != r
                )
                if not selected_roots:
                    continue

                children = []
                for root in selected_roots:
                    child = state[-root:]
                    children.append(
                        {
                            "root": root,
                            "word": "".join(map(str, child)),
                            "profile": proper_profile(child),
                            "is_fixed_profile": (
                                primitive(child)
                                and proper_profile(child) == child
                            ),
                            "cube_tail_length": tail_length(child * 3),
                        }
                    )

                return {
                    "r": r,
                    "h": h,
                    "branch": branch,
                    "Y": "".join(map(str, y)),
                    "U": "".join(map(str, u)),
                    "C": "".join(map(str, c)),
                    "Q": "".join(map(str, q)),
                    "Q_cn": exact_cn(q),
                    "Q_profile": proper_profile(q),
                    "Q_profile_mismatches": tuple(
                        index
                        for index, (actual, wanted) in enumerate(
                            zip(proper_profile(q), q)
                        )
                        if actual != wanted
                    ),
                    "W": "".join(map(str, w)),
                    "W_tail_length": tail_length(w),
                    "deleted_tail_length": tail_length(w[1:]),
                    "seam_state": "".join(map(str, state)),
                    "seam_tail_length": tail_length(state),
                    "seam_roots": roots,
                    "children": tuple(children),
                }
    return None


def main() -> None:
    for branch in ("contained", "crossing"):
        model = find_model(branch)
        if model is None:
            print({"branch": branch, "model": None})
        else:
            print(model)


if __name__ == "__main__":
    main()
