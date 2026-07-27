"""Execute the long replay-root predecessor-equality calibration."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curling import curling_number, curling_number_reference


def main() -> None:
    seed = tuple(map(int, "223222323"))
    replay = tuple(map(int, "223222323222322232232"))

    state = seed
    steps = 0
    while len(state) < len(replay):
        fast = curling_number(state)
        reference = curling_number_reference(state)
        assert fast == reference
        state += (fast,)
        steps += 1

    assert state == replay
    fast_prefix = curling_number(replay[:-1])
    reference_prefix = curling_number_reference(replay[:-1])
    assert fast_prefix == reference_prefix == replay[-1]

    print(
        {
            "seed_length": len(seed),
            "replay_length": len(replay),
            "extensions_to_replay": steps,
            "prefix_cn_fast": fast_prefix,
            "prefix_cn_reference": reference_prefix,
            "replay_last_symbol": replay[-1],
        }
    )


if __name__ == "__main__":
    main()
