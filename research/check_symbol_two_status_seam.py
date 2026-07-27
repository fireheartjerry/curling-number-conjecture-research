"""Executed audits for ``symbol_two_status_seam.md``.

Run the A094004 calibration first.  Every curling number printed or used
here is recomputed by both independent implementations.
"""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import (
    curling_number,
    curling_number_reference,
    tail_length,
)

from check_run_length_grammar import (
    primitive,
    proper_profile,
)


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def root_exponent(word: Word, root: int) -> int:
    exponent = 1
    while (exponent + 1) * root <= len(word) and (
        word[-(exponent + 1) * root : -exponent * root]
        == word[-root:]
    ):
        exponent += 1
    return exponent


def maximizing_roots(word: Word) -> tuple[int, ...]:
    value = exact_cn(word)
    return tuple(
        root
        for root in range(1, len(word) // value + 1)
        if root_exponent(word, root) == value
    )


def q21_audit() -> tuple[dict[str, object], ...]:
    p = tuple(map(int, "223222322232322232223"))
    n = len(p)
    assert primitive(p)
    assert proper_profile(p) == p
    rows: list[dict[str, object]] = []
    for phase, label in enumerate(p):
        if label != 2:
            continue
        c = p[phase:] + p[:phase]
        r_word = c[1:]
        q = r_word + (2,)
        d = (q * 3)[:-1]
        h_word = (2,) + d + (3,)
        e_word = (2,) + d + (2,)
        b_word = d + (2,)
        assert c * 3 == (2,) + d
        assert e_word == (2,) + b_word
        assert b_word == q * 3

        # The cut-zero conjugate-power argument gives q[0]=C[1]<=3.
        assert q[0] <= 3
        b_value = max(3, q[0])
        assert b_value == 3
        assert exact_cn(c * 3) == 3
        assert exact_cn(e_word) == exact_cn(b_word) == b_value
        u = exact_cn(h_word)
        assert 1 <= u <= 4
        roots = maximizing_roots(h_word) if u >= 2 else ()
        if u >= 2:
            assert roots
            assert all(
                (u - 1) * root + gcd(n, root) <= n
                and root < n
                for root in roots
            )
        rows.append(
            {
                "phase": phase,
                "next_label": q[0],
                "cn_H_E_B": (
                    u,
                    exact_cn(e_word),
                    exact_cn(b_word),
                ),
                "H_maximizing_roots": roots,
                "tail_H_E_B": (
                    tail_length(h_word, step_limit=10_000),
                    tail_length(e_word, step_limit=10_000),
                    tail_length(b_word, step_limit=10_000),
                ),
                "tau_D_and_equal_endpoint_ranks": (
                    tail_length(d, step_limit=10_000),
                    len(c * 3) + tail_length(d, step_limit=10_000),
                    len(e_word)
                    + tail_length(b_word, step_limit=10_000),
                ),
            }
        )
        tau_d, rank_a, rank_e = rows[-1][
            "tau_D_and_equal_endpoint_ranks"
        ]
        assert tau_d == 1 + tail_length(b_word, step_limit=10_000)
        assert rank_a == rank_e
    assert len(rows) == 15
    return tuple(rows)


def locked_example() -> dict[str, object]:
    # Q=R2, C=2R, with R containing no 2.
    r_word = (3, 3)
    q = r_word + (2,)
    c = (2,) + r_word
    b_word = q * 3
    e_word = (2,) + b_word
    common_values: list[int] = []
    for required in r_word:
        left = exact_cn(e_word)
        right = exact_cn(b_word)
        assert left == right == required
        common_values.append(required)
        e_word += (required,)
        b_word += (required,)
    assert e_word == c * 4
    assert b_word == r_word + c * 3
    assert exact_cn(e_word) == 4
    assert exact_cn(b_word) == 3
    return {
        "Q": q,
        "C": c,
        "common_output": tuple(common_values),
        "first_mismatch_values": (4, 3),
        "locked_root": len(c),
    }


def bounded_prefix_search(max_n: int = 8) -> dict[str, object]:
    """Classify every finite E/B mismatch reached before a 1."""
    roots = 0
    mismatches = 0
    locked = 0
    external = 0
    for n in range(3, max_n + 1):
        for prefix in product((2, 3), repeat=n - 1):
            q = prefix + (2,)
            if not primitive(q):
                continue
            roots += 1
            left = (2,) + q * 3
            right = q * 3
            common: list[int] = []
            for _ in range(1_000):
                left_value = exact_cn(left)
                right_value = exact_cn(right)
                if left_value != right_value:
                    mismatches += 1
                    k = left_value
                    assert len(left) % k == 0
                    root = len(left) // k
                    y = left[:root]
                    assert left == y * k
                    if root == n:
                        locked += 1
                        assert k == 4
                        assert tuple(common) == q[:-1]
                        assert all(value >= 3 for value in q[:-1])
                    else:
                        external += 1
                        assert k == 3
                        assert root > 2 * n + gcd(n, root)
                    break
                if left_value == 1:
                    break
                common.append(left_value)
                left += (left_value,)
                right += (right_value,)
            else:
                raise RuntimeError("paired trace limit reached")
    assert external == 0
    return {
        "alphabet": (2, 3),
        "maximum_root_length": max_n,
        "primitive_Q_ending_2": roots,
        "first_mismatches": mismatches,
        "locked": locked,
        "external": external,
    }


def main() -> None:
    print(
        {
            "Q21_symbol_two_rows": q21_audit(),
            "locked_word_example": locked_example(),
            "bounded_prefix_search": bounded_prefix_search(),
        }
    )


if __name__ == "__main__":
    main()
