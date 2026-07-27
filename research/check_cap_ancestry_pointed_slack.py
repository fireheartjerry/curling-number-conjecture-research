"""Audit pointed fitting-slack transport in the Q21 ancestry DAG.

The script performs no curling-number evaluation.  It reconstructs every
first-copy-fitting square-ancestry edge of the exact Q21 circular profile
and checks the lifted slack identity

    child_slack - parent_slack = 2*parent_root - 3*child_root - distance.
"""

from __future__ import annotations

from check_max_square_terminal_forest import fitting_square_ancestry
from check_run_length_grammar import primitive, proper_profile


Q21 = tuple(map(int, "223222322232322232223"))


def square_slack(size: int, cut: int, root: int) -> int:
    return size + cut - 1 - 2 * root


def main() -> None:
    word = Q21
    size = len(word)
    assert size == 21
    assert primitive(word)
    assert proper_profile(word) == word

    vertices, edges = fitting_square_ancestry(word)
    records: list[dict[str, object]] = []
    for parent in sorted(vertices):
        parent_cut, parent_root = parent
        parent_slack = square_slack(size, parent_cut, parent_root)
        assert parent_slack >= 0
        for child_cut, child_root, distance, high_cut in edges[parent]:
            lifted_high = parent_cut - distance
            lifted_child_cut = lifted_high - child_root
            lifted_child_slack = square_slack(
                size,
                lifted_child_cut,
                child_root,
            )
            canonical_child_slack = square_slack(
                size,
                child_cut,
                child_root,
            )
            assert child_cut == lifted_child_cut % size
            assert high_cut == lifted_high % size
            assert (
                lifted_child_slack - parent_slack
                == 2 * parent_root - 3 * child_root - distance
            )
            assert (
                canonical_child_slack - lifted_child_slack
            ) % size == 0
            records.append(
                {
                    "parent": parent,
                    "child": (child_cut, child_root),
                    "distance": distance,
                    "parent_slack": parent_slack,
                    "lifted_child_cut": lifted_child_cut,
                    "lifted_child_slack": lifted_child_slack,
                    "canonical_child_slack": canonical_child_slack,
                }
            )

    # The globally longest fitting square is boundary-tight at phase zero.
    # Its actual lifted child already terminates at an unrelated root-one
    # leaf before the powered factor reaches the fitting-window boundary.
    parent = (0, 10)
    assert square_slack(size, *parent) == 0
    assert edges[parent] == ((19, 1, 1, 20),)
    lifted_high = -1
    lifted_child_cut = -2
    assert square_slack(size, lifted_child_cut, 1) == 16
    assert edges[19, 1] == ()

    leaves = tuple(
        sorted(
            (
                vertex,
                square_slack(size, *vertex),
            )
            for vertex in vertices
            if not edges[vertex]
        )
    )
    assert leaves == (
        ((5, 1), 23),
        ((9, 1), 27),
        ((15, 1), 33),
        ((19, 1), 37),
    )

    print(
        {
            "word": "".join(map(str, word)),
            "vertices": len(vertices),
            "edges": sum(map(len, edges.values())),
            "tight_parent_path": {
                "parent": parent,
                "parent_slack": 0,
                "lifted_high": lifted_high,
                "lifted_child": (lifted_child_cut, 1),
                "lifted_child_slack": 16,
                "canonical_child": (19, 1),
                "canonical_child_slack": 37,
            },
            "root_one_leaves": leaves,
            "edge_slack_records": tuple(records),
        }
    )


if __name__ == "__main__":
    main()
