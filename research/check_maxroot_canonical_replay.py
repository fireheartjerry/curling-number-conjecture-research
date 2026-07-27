"""Executed audit of the canonical valuation-root replay.

For M=4 and M=5, build

    A[-1]=(M-1),  A[h]=A[h-1]^M M

through every hierarchy level available before the top-component
no-return interval.  Both curling-number implementations check every
intermediate phase of

    A[h]^(M-1) A[h][:t].
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from curling import curling_number, curling_number_reference


def checked_cn(word: tuple[int, ...]) -> int:
    fast = curling_number(word)
    slow = curling_number_reference(word)
    assert fast == slow
    return fast


def audit(maximum: int):
    word = (maximum - 1,)
    records = []
    # A top component can expose levels -1 through M-3 before the
    # no-return interval.
    for level in range(-1, maximum - 2):
        values = tuple(
            checked_cn(
                word * (maximum - 1) + word[:phase]
            )
            for phase in range(len(word))
        )
        assert values == word
        endpoint = word * maximum + (maximum,)
        endpoint_value = checked_cn(endpoint)
        assert endpoint_value == level + 2
        marker_value = None
        if level <= maximum - 4:
            exit_symbol = level + 2
            assert exit_symbol not in endpoint
            marker_value = checked_cn(endpoint + (exit_symbol,))
            assert marker_value == 1
        records.append(
            {
                "level": level,
                "length": len(word),
                "replay_matches": True,
                "endpoint_length": len(endpoint),
                "endpoint_cn": endpoint_value,
                "standalone_marker_cn": marker_value,
            }
        )
        word = endpoint
    return records


def main() -> None:
    for maximum in (4, 5):
        print({"M": maximum, "records": audit(maximum)})


if __name__ == "__main__":
    main()
