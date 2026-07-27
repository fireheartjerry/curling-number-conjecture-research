"""Concrete unequal square-rescue marker cycle and its first profile failure.

The ternary token word below is a primitive circular word with proper
curling profile two at every cut.  For M=6, replace token color e by the
equal-length return

    2,4,5^6,6,e,       e in {2,3,4}.

Each return contains the shortest formal top component ``5^6 6`` and
ends in its colored exit.  Token squares therefore lift to aligned raw
squares between complete exit markers.  The induced raw rescue roots have
mixed lengths because the token square roots do.

The construction is only a model of the currently derived exit-marker
constraints.  The script computes the full proper circular profile and
reports the earliest cut where the raw labels fail.
"""

from __future__ import annotations

from check_run_length_grammar import primitive, proper_profile


TOKEN_WORD = "0010200100101001020010200100101"
EXITS = (2, 3, 4)
M = 6
TOP = (M - 1,) * M + (M,)


def token_profile(word: str) -> tuple[int, ...]:
    return proper_profile(tuple(map(int, word)))


def power_roots(
    word: tuple[int, ...],
    cut: int,
    exponent: int,
) -> tuple[int, ...]:
    n = len(word)
    return tuple(
        root
        for root in range(1, n)
        if all(
            word[(cut - block * root + offset) % n]
            == word[(cut - root + offset) % n]
            for block in range(2, exponent + 1)
            for offset in range(root)
        )
    )


def functional_cycles(parent: tuple[int, ...]):
    seen: set[int] = set()
    cycles = []
    for start in range(len(parent)):
        path = []
        positions = {}
        current = start
        while current not in positions and current not in seen:
            positions[current] = len(path)
            path.append(current)
            current = parent[current]
        if current in positions:
            cycles.append(tuple(path[positions[current] :]))
        seen.update(path)
    return tuple(cycles)


def threshold_signature(raw_return: tuple[int, ...]):
    exit_value = raw_return[-1]
    levels = []
    for threshold in range(exit_value + 1, M):
        start = len(raw_return) - 1
        while start > 0 and raw_return[start - 1] >= threshold:
            start -= 1
        component = raw_return[start:-1]
        separator = raw_return[start - 1] if start else None
        levels.append(
            {
                "threshold": threshold,
                "component_length": len(component),
                "separator": separator,
                "component": component,
            }
        )
    return tuple(levels)


def first_entry_violation(raw_return: tuple[int, ...]):
    exit_value = raw_return[-1]
    for threshold in range(exit_value + 2, M + 1):
        lower = threshold - 1
        start = len(raw_return) - 1
        while start > 0 and raw_return[start - 1] >= lower:
            start -= 1
        component = raw_return[start:-1]
        first_high = next(
            (
                index
                for index, value in enumerate(component)
                if value >= threshold
            ),
            None,
        )
        if first_high is None:
            continue
        expected = (lower,) * threshold
        actual = component[max(0, first_high - threshold) : first_high]
        if first_high < threshold or actual != expected:
            return {
                "threshold": threshold,
                "component": component,
                "first_high_offset": first_high,
                "required_prefix": expected,
                "actual_predecessor": actual,
            }
    return None


def main() -> None:
    token = tuple(map(int, TOKEN_WORD))
    token_values = token_profile(TOKEN_WORD)
    assert primitive(token)
    assert token_values == (2,) * len(token)

    returns = {
        color: (2, M - 2) + TOP + (EXITS[color],)
        for color in range(len(EXITS))
    }
    assert len({len(value) for value in returns.values()}) == 1
    width = len(returns[0])
    raw = tuple(
        value
        for color in token
        for value in returns[color]
    )
    raw_profile = proper_profile(raw)
    assert primitive(raw)

    marker_cuts = tuple(
        ((index + 1) * width) % len(raw)
        for index in range(len(token))
    )
    marker_records = []
    for index, cut in enumerate(marker_cuts):
        token_cut = (index + 1) % len(token)
        token_roots = power_roots(token, token_cut, 2)
        raw_roots = power_roots(raw, cut, 2)
        lifted = tuple(width * root for root in token_roots)
        assert all(root in raw_roots for root in lifted)
        assert all(root >= len(TOP) + 1 for root in lifted)
        assert all(
            primitive(
                tuple(
                    raw[(cut - root + offset) % len(raw)]
                    for offset in range(root)
                )
            )
            for root in lifted
        )
        marker_records.append(
            {
                "cut": cut,
                "label": raw[cut],
                "profile": raw_profile[cut],
                "token_roots": token_roots,
                "lifted_raw_roots": lifted,
                "all_raw_square_roots": raw_roots,
            }
        )

    failures = tuple(
        (cut, raw[cut], raw_profile[cut])
        for cut in range(len(raw))
        if raw[cut] != raw_profile[cut]
    )
    marker_failures = tuple(
        record
        for record in marker_records
        if record["label"] != record["profile"]
    )
    distinct_lifted = tuple(
        sorted(
            {
                root
                for record in marker_records
                for root in record["lifted_raw_roots"]
            }
        )
    )
    token_square_roots = tuple(
        power_roots(token, cut, 2)
        for cut in range(len(token))
    )
    least_parent = tuple(
        (cut - roots[0]) % len(token)
        for cut, roots in enumerate(token_square_roots)
    )
    least_cycles = functional_cycles(least_parent)
    least_cycle_roots = tuple(
        tuple(width * token_square_roots[cut][0] for cut in cycle)
        for cycle in least_cycles
    )
    assert any(len(set(roots)) > 1 for roots in least_cycle_roots)
    signatures = {
        EXITS[color]: threshold_signature(returns[color])
        for color in range(len(EXITS))
    }
    entry_violations = {
        EXITS[color]: first_entry_violation(returns[color])
        for color in range(len(EXITS))
    }
    print(
        {
            "token_length": len(token),
            "token_profile": token_values,
            "return_width": width,
            "raw_length": len(raw),
            "mixed_lifted_square_roots": distinct_lifted,
            "least_root_parent_cycles": least_cycles,
            "least_root_cycle_raw_roots": least_cycle_roots,
            "threshold_signatures": signatures,
            "first_entry_violations": entry_violations,
            "marker_failure_count": len(marker_failures),
            "first_marker_failure": (
                marker_failures[0] if marker_failures else None
            ),
            "failure_count": len(failures),
            "first_full_profile_failure": failures[0],
        }
    )


if __name__ == "__main__":
    main()
