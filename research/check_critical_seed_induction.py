"""Exact checks for the critical one-symbol-deletion normal form.

All curling numbers printed by this file are evaluated by both independent
implementations in ``curling.py``.  The proper circular profile is evaluated
directly from circular equality comparisons, independently of either orbit
implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from curling import curling_number, curling_number_reference


Word = tuple[int, ...]


def exact_cn(word: Word) -> int:
    value = curling_number(word)
    assert value == curling_number_reference(word)
    return value


def primitive(word: Word) -> bool:
    n = len(word)
    return not any(
        n % period == 0
        and all(word[i] == word[i % period] for i in range(period, n))
        for period in range(1, n)
    )


def proper_circular_profile(word: Word) -> Word:
    """Return the exact profile using roots shorter than ``len(word)``."""
    n = len(word)
    assert primitive(word)
    profile: list[int] = []
    for cut in range(n):
        best = 1
        for root in range(1, n):
            matched = 0
            # For a primitive n-cycle and root<n, the circular equality
            # indicator cannot be true for a complete n-symbol cycle.
            while (
                matched < n
                and word[(cut - 1 - matched) % n]
                == word[(cut - 1 - matched - root) % n]
            ):
                matched += 1
            assert matched < n
            best = max(best, 1 + matched // root)
        profile.append(best)
    return tuple(profile)


def proper_circular_maximizing_roots(word: Word, cut: int) -> tuple[int, ...]:
    """Primitive proper roots attaining the exact circular profile value."""
    n = len(word)
    value = proper_circular_profile(word)[cut]
    roots: list[int] = []
    for root in range(1, n):
        block = tuple(word[(cut - root + i) % n] for i in range(root))
        if not primitive(block):
            continue
        if all(
            word[(cut - copy * root + i) % n]
            == word[(cut - root + i) % n]
            for copy in range(2, value + 1)
            for i in range(root)
        ):
            roots.append(root)
    return tuple(roots)


def maximizing_roots(word: Word, value: int) -> tuple[int, ...]:
    if value == 1:
        return ()
    return tuple(
        root
        for root in range(1, len(word) // value + 1)
        if word[-value * root :] == word[-root:] * value
    )


def is_rotation(left: Word, right: Word) -> bool:
    return len(left) == len(right) and any(
        left == right[shift:] + right[:shift] for shift in range(len(right))
    )


def circular_factor(word: Word, factor: Word) -> bool:
    if not factor:
        return True
    n = len(word)
    return any(
        all(factor[i] == word[(phase + i) % n] for i in range(len(factor)))
        for phase in range(n)
    )


@dataclass(frozen=True)
class PostTrace:
    outputs: Word
    root_sets: tuple[tuple[int, ...], ...]


def trace_to_one(seed: Word, limit: int = 500) -> PostTrace:
    state = seed
    outputs: list[int] = []
    root_sets: list[tuple[int, ...]] = []
    for _ in range(limit):
        value = exact_cn(state)
        outputs.append(value)
        root_sets.append(maximizing_roots(state, value))
        if value == 1:
            return PostTrace(tuple(outputs), tuple(root_sets))
        state += (value,)
    raise RuntimeError("trace limit reached")


def first_deletion_divergence(root: Word, limit: int = 500):
    high = root
    low = root[1:]
    for step in range(limit):
        high_value = exact_cn(high)
        low_value = exact_cn(low)
        if high_value != low_value:
            return step, high_value, low_value, high, low
        high += (high_value,)
        low += (low_value,)
    raise RuntimeError("divergence limit reached")


def main() -> None:
    # Calibration values from the problem statement.
    calibrations = {
        (1,): 1,
        (2, 2): 2,
        (3, 2, 2): 2,
        (1, 2, 1, 2, 1, 2): 3,
        (1,) * 8: 8,
        (-3,) * 3: 3,
    }
    for word, expected in calibrations.items():
        assert exact_cn(word) == expected

    # Circular fixedness alone does not imply replay to a cube when profile
    # value one is allowed.
    profile_one_countermodel = (1, 2, 1)
    assert primitive(profile_one_countermodel)
    assert (
        proper_circular_profile(profile_one_countermodel)
        == profile_one_countermodel
    )
    profile_one_state = profile_one_countermodel
    profile_one_outputs: list[int] = []
    for _ in range(2 * len(profile_one_countermodel)):
        value = exact_cn(profile_one_state)
        profile_one_outputs.append(value)
        profile_one_state += (value,)
    assert tuple(profile_one_outputs) == (1, 2, 1, 2, 2, 2)
    assert profile_one_state != profile_one_countermodel * 3

    base = tuple(map(int, "223222322232322232223"))
    p = len(base)
    assert primitive(base)
    assert proper_circular_profile(base) == base

    # Rotation replay and the multi-symbol deletion visibility radius.
    # Every displayed finite curling number is recomputed by exact_cn.
    witness_spans = tuple(
        base[cut] * min(proper_circular_maximizing_roots(base, cut))
        for cut in range(p)
    )
    visibility = tuple(
        max(
            0,
            min(
                p - 1,
                min(
                    p + step - witness_spans[(shift + step) % p]
                    for step in range(p)
                ),
            ),
        )
        for shift in range(p)
    )

    for shift in range(p):
        root = base[shift:] + base[:shift]
        state = root
        for step in range(2 * p):
            value = exact_cn(state)
            assert value == root[step % p]
            state += (value,)
        assert state == root * 3

        if root[0] != 2:
            continue
        assert exact_cn(state) == 3
        for deletion in range(1, visibility[shift] + 1):
            high = root
            low = root[deletion:]
            for step in range(2 * p):
                high_value = exact_cn(high)
                low_value = exact_cn(low)
                assert high_value == low_value == root[step % p]
                high += (high_value,)
                low += (low_value,)
            assert high == root * 3
            assert low == root[deletion:] + root * 2
            assert exact_cn(high) == 3
            assert exact_cn(low) == 2
            for step in range(deletion):
                value = exact_cn(low)
                assert value == root[step]
                low += (value,)
            rotated = root[deletion:] + root[:deletion]
            assert low == rotated * 3

    # The visibility hypothesis is necessary: these two longer deletions
    # from phase zero leave the common replay strictly before the cube.
    phase_zero = base
    # Use the general two-word comparison here; first_deletion_divergence
    # itself is specialized to deleting one symbol.
    def compare_prefixes(left: Word, right: Word, limit: int = 100):
        for step in range(limit):
            left_value = exact_cn(left)
            right_value = exact_cn(right)
            if left_value != right_value:
                return step, left_value, right_value
            left += (left_value,)
            right += (right_value,)
        raise RuntimeError("comparison limit reached")

    deletion_signatures = {
        deletion: compare_prefixes(base, base[deletion:])
        for deletion in (12, 14)
    }
    assert deletion_signatures == {
        12: (2, 3, 2),
        14: (0, 2, 1),
    }

    two_phases = tuple(
        phase for phase, symbol in enumerate(base) if symbol == 2
    )
    allowed_counterexample_sets: list[tuple[int, ...]] = []
    for mask in range(1 << len(two_phases)):
        candidate = {
            two_phases[index]
            for index in range(len(two_phases))
            if mask & (1 << index)
        }
        if all(
            all(
                (phase + distance) % p not in candidate
                for distance in range(1, visibility[phase] + 1)
            )
            for phase in candidate
        ):
            allowed_counterexample_sets.append(tuple(sorted(candidate)))
    maximum_allowed = max(map(len, allowed_counterexample_sets))
    assert maximum_allowed == 2
    extremal_counterexample_sets = sorted(
        candidate
        for candidate in allowed_counterexample_sets
        if len(candidate) == maximum_allowed
    )
    assert set(extremal_counterexample_sets) == {
        (7, 15),
        (7, 17),
        (7, 18),
    }

    surviving: list[tuple[int, Word]] = []
    post_records: list[tuple[int, int, int]] = []
    for shift in range(p):
        root = base[shift:] + base[:shift]
        assert proper_circular_profile(root) == root
        if root[0] != 2:
            continue

        step, high_value, low_value, high, low = (
            first_deletion_divergence(root)
        )
        assert step == 2 * p
        assert high == root * 3
        assert low == high[1:]
        assert (high_value, low_value) == (3, 2)

        post = trace_to_one(root * 3 + (3,))
        nonone = post.outputs[:-1]
        maximum_root = max(
            (max(roots) for roots in post.root_sets if roots),
            default=0,
        )
        post_records.append((shift, len(nonone), maximum_root))
        if len(nonone) >= p:
            block = nonone[:p]
            assert is_rotation(block, root)
            surviving.append((shift, block))

    assert surviving == [
        (8, tuple(map(int, "222322232232223222323")))
    ]

    critical = base[8:] + base[:8]
    post = trace_to_one(critical * 3 + (3,))
    assert len(post.outputs) - 1 == 59
    assert max(max(roots) for roots in post.root_sets if roots) == 38

    # The first root after promotion is Z=23.  Rotating it to begin at the
    # copied marker gives 32, which is not a smaller critical seed.
    assert exact_cn((3, 2)) == 1

    # A whole fixed-profile rotation beginning with the internal marker 3
    # self-replays two copies, but fails while attempting a fourth copy.
    marker_rotation = base[2:] + base[:2]
    state = marker_rotation
    mismatch = None
    for step in range(4 * p):
        value = exact_cn(state)
        expected = marker_rotation[step % p]
        if value != expected:
            mismatch = (step, value, expected)
            break
        state += (value,)
    assert mismatch == (43, 3, 2)

    # Audit the first-loss normal form in Section 7 for every phase-zero
    # rotation.  All values and root sets are exact, not inferred from the
    # displayed digits.
    loss_records: list[tuple[int, int, int, int, int]] = []
    seam_records: list[tuple[int, int, int]] = []
    for shift in range(p):
        root = base[shift:] + base[:shift]
        if root[0] != 2:
            continue
        state = root * 3 + (3,)
        emitted: Word = (3,)
        assert circular_factor(root, emitted)
        for _ in range(p):
            value = exact_cn(state)
            if value == 1:
                break
            extended = emitted + (value,)
            if not circular_factor(root, extended):
                if value == 3:
                    trailing_twos = 0
                    for symbol in reversed(emitted):
                        if symbol != 2:
                            break
                        trailing_twos += 1
                    incoming_cubes = maximizing_roots(state, value)
                    assert incoming_cubes
                    incoming = min(incoming_cubes)
                    assert incoming > trailing_twos
                    seam_records.append(
                        (shift, trailing_twos, incoming)
                    )
                after = state + (value,)
                next_value = exact_cn(after)
                if next_value >= 2:
                    roots = maximizing_roots(after, next_value)
                    assert roots
                    q = min(roots)
                    e = len(emitted)
                    assert q <= e
                    assert emitted[e - q] == value
                    y = emitted[e - q + 1 :] + (value,)
                    assert len(y) == q
                    assert after[-next_value * q :] == y * next_value
                    assert exact_cn(y) <= next_value - 1
                    loss_records.append(
                        (shift, e, value, next_value, q)
                    )
                break
            emitted = extended
            state += (value,)

    assert loss_records == [
        (1, 9, 3, 2, 1),
        (5, 1, 3, 2, 1),
        (9, 5, 3, 2, 1),
        (14, 1, 3, 2, 1),
        (18, 5, 3, 2, 1),
    ]
    assert seam_records == [
        (1, 0, 10),
        (5, 0, 3),
        (9, 0, 7),
        (14, 0, 2),
        (18, 0, 6),
    ]

    # Section 8 calibration: force exactly two matched circular periods
    # behind every phase, with a fresh left delimiter preventing an extra
    # period-p copy.  Value-three phases satisfy the strict-root hypothesis;
    # value-two phases expose the necessary length-p maximizing square.
    lock_records: list[tuple[int, int, tuple[int, ...]]] = []
    for cut in range(p):
        matched = tuple(
            base[(cut - 2 * p + offset) % p]
            for offset in range(2 * p)
        )
        state = (99,) + matched
        value = exact_cn(state)
        assert value == base[cut]
        roots = maximizing_roots(state, value)
        if value == 3:
            assert roots and max(roots) < p
        else:
            assert p in roots
        lock_records.append((cut, value, roots))

    # Maximum-label backchain and endpoint-replay audit.  The available
    # exact fixed profile has M=3, so the M>=4 contradiction is not invoked;
    # all six chains nevertheless terminate at M-1 in one edge.
    maximum = max(base)
    chain_records: list[tuple[int, int, str, tuple[int, ...]]] = []
    for cut, symbol in enumerate(base):
        if symbol != maximum:
            continue
        roots = proper_circular_maximizing_roots(base, cut)
        assert roots
        q = min(roots)
        source = (cut - q) % p
        y = tuple(base[(cut - q + i) % p] for i in range(q))
        assert base[source] == maximum - 1
        assert set(y) <= {maximum - 1, maximum}
        replay = tuple(
            exact_cn(y * (maximum - 1) + y[:offset])
            for offset in range(q + 1)
        )
        assert replay == y + (maximum,)
        chain_records.append(
            (cut, q, "".join(map(str, y)), replay)
        )

    assert chain_records == [
        (2, 4, "2322", (2, 3, 2, 2, 3)),
        (6, 1, "2", (2, 3)),
        (10, 1, "2", (2, 3)),
        (12, 4, "2232", (2, 2, 3, 2, 3)),
        (16, 1, "2", (2, 3)),
        (20, 1, "2", (2, 3)),
    ]

    # Section 10: every first post-promotion root points to a circular
    # marker with its own incoming proper cube.  Audit all roots, not only
    # a preferred one, over every phase-zero rotation.
    ancestry_records: list[tuple[int, int, int, int]] = []
    for shift in range(p):
        root = base[shift:] + base[:shift]
        if root[0] != 2:
            continue
        promoted = root * 3 + (3,)
        value = exact_cn(promoted)
        if value == 1:
            continue
        for q in maximizing_roots(promoted, value):
            z = promoted[-q:]
            assert primitive(z)
            parent = p - q
            assert root[parent] == 3
            incoming = proper_circular_maximizing_roots(root, parent)
            assert incoming
            for r in incoming:
                assert 2 * r + gcd(p, r) < p
                assert q <= 3 * r
                v = tuple(
                    root[(parent - r + offset) % p]
                    for offset in range(r)
                )
                if q >= 2 * r + 1:
                    assert (root * 3)[-2 * r :] == v * 2
                if q == 3 * r:
                    cube = v * 3
                    assert z == cube[1:] + (3,)
                    assert exact_cn(cube) == 3
                    assert exact_cn(cube[1:]) == 2
                ancestry_records.append((shift, q, r, q - 3 * r))

    assert {(q, r) for _, q, r, _ in ancestry_records} == {
        (1, 4),
        (2, 4),
        (3, 4),
        (1, 1),
        (2, 1),
        (3, 1),
        (6, 4),
        (7, 4),
        (10, 4),
    }

    # A local countermodel to the overstrong claim that one genuine parent
    # cube forces an immediate 3,2,1 death.
    local_marker = tuple(map(int, "23232332223232"))
    local_profile = proper_circular_profile(local_marker)
    assert primitive(local_marker)
    assert (
        local_profile[0],
        local_profile[6],
        local_profile[7],
    ) == (2, 3, 2)
    assert exact_cn(local_marker * 3) == 3
    local_trace = trace_to_one(local_marker * 3 + (3,))
    assert local_trace.outputs == (
        3,
        2,
        2,
        2,
        3,
        2,
        2,
        2,
        3,
        2,
        2,
        2,
        3,
        3,
        2,
        1,
    )

    # Section 12: the legal unary leaf of cube ancestry dies immediately
    # when considered as a standalone cube-marker factor.
    unary_cube_marker = (2, 2, 2, 3)
    assert exact_cn(unary_cube_marker) == 1

    # Exact local countermodel for the top-entrance return-word quotient.
    # The original cut has value a=2, while the quotient sees only a-1
    # complete repeated return gaps.  Both distinct gaps have the same
    # successor weight, so collapsing to weights is noninjective.
    top_maximum = 4
    top_marker = (
        (top_maximum - 2,)
        + (top_maximum - 1,) * top_maximum
        + (top_maximum,)
    )
    copied_root = (2,) + top_marker
    unmatched_prefix = (2, 2)
    top_quotient_model = (
        unmatched_prefix + copied_root + copied_root
    )
    assert primitive(top_quotient_model)
    top_profile = proper_circular_profile(top_quotient_model)
    assert top_profile[0] == 2
    assert proper_circular_maximizing_roots(
        top_quotient_model, 0
    ) == (len(copied_root),)
    assert exact_cn(top_quotient_model) == 2
    assert top_quotient_model[-2 * len(copied_root) :] == (
        copied_root * 2
    )
    marker_starts = tuple(
        start
        for start in range(len(top_quotient_model))
        if all(
            top_quotient_model[
                (start + offset) % len(top_quotient_model)
            ]
            == symbol
            for offset, symbol in enumerate(top_marker)
        )
    )
    assert marker_starts == (3, 10)
    exact_gap_tokens = (0, 1)
    assert primitive(exact_gap_tokens)
    assert proper_circular_profile(exact_gap_tokens) == (1, 1)
    gap_successor_weights = (2, 2)
    assert exact_cn(gap_successor_weights) == 2

    # Two-level synchronization/seam audit.  The one-symbol deletion of
    # the fixed word realizes the exact common-suffix equations through
    # the high cube / low square divergence and the delayed cube one copy
    # later.  This is a local model, not a second fixed-profile level.
    shifted_context = base[1:]
    assert len(shifted_context) == p - 1
    nested_checkpoints: list[
        tuple[
            int,
            int,
            tuple[int, ...],
            int,
            tuple[int, ...],
            int,
        ]
    ] = []
    for step in range(3 * p + 1):
        replay = (base * 3)[:step]
        high = base + replay
        low = shifted_context + replay
        high_value = exact_cn(high)
        low_value = exact_cn(low)

        common = 0
        while (
            common < min(len(high), len(low))
            and high[-1 - common] == low[-1 - common]
        ):
            common += 1
        assert common == p - 1 + step

        if step < 2 * p:
            assert high_value == low_value == base[step % p]
        elif step == 2 * p:
            assert high_value == 3
            assert low_value == 2
        elif step == 3 * p:
            assert low_value == 3

        if step in (0, p, 2 * p, 3 * p):
            nested_checkpoints.append(
                (
                    step,
                    high_value,
                    maximizing_roots(high, high_value),
                    low_value,
                    maximizing_roots(low, low_value),
                    common,
                )
            )

    assert nested_checkpoints == [
        (0, 2, (4, 10), 2, (4, 10), 20),
        (21, 2, (4, 10, 21), 2, (4, 10), 41),
        (42, 3, (21,), 2, (4, 10, 21), 62),
        (63, 4, (21,), 3, (21,), 83),
    ]

    # Prefix-cube plus suffix-square constraints alone do not force a
    # contradiction.  A unique delimiter prevents every repeated suffix
    # power from crossing it, so this seed has the correct old prefix and
    # exactly the shifted-context continuation through delayed maturation.
    # The model is intentionally not proper-profile fixed and is not a
    # pair of prefixes on one autonomous tower.
    delimiter_model = (
        base * 3 + (3, 99) + shifted_context
    )
    assert delimiter_model[: 3 * p + 1] == base * 3 + (3,)
    assert delimiter_model.count(99) == 1
    delimiter_outputs: list[int] = []
    for step in range(3 * p + 1):
        replay = (base * 3)[:step]
        model_value = exact_cn(delimiter_model + replay)
        shifted_value = exact_cn(shifted_context + replay)
        assert model_value == shifted_value
        delimiter_outputs.append(model_value)
        if step < 2 * p:
            assert model_value == base[step % p]
        elif step == 2 * p:
            assert model_value == 2
        elif step == 3 * p:
            assert model_value == 3

    print(f"proper_fixed_word={''.join(map(str, base))}")
    print(
        "profile_one_replay_countermodel="
        f"outputs={tuple(profile_one_outputs)}"
    )
    print(f"rotation_witness_spans={witness_spans}")
    print(f"rotation_visibility_radii={visibility}")
    print(f"long_deletion_signatures={deletion_signatures}")
    print(
        "rotation_counterexample_packing="
        f"maximum={maximum_allowed} "
        f"extremals={extremal_counterexample_sets}"
    )
    print(f"minimum_start_rotations={len(post_records)}")
    print(
        "full_block_survivors="
        + repr(
            [
                (shift, "".join(map(str, block)))
                for shift, block in surviving
            ]
        )
    )
    print(
        "long_survivor="
        f"shift=8 post_nonone={len(post.outputs) - 1} "
        f"maximum_root={max(max(rs) for rs in post.root_sets if rs)}"
    )
    print(f"marker_block_32_cn={exact_cn((3, 2))}")
    print(f"marker_rotation_first_replay_mismatch={mismatch}")
    print(f"first_phase_loss_records={loss_records}")
    print(f"last_marker_seam_records={seam_records}")
    print(
        "two_period_lock_audit="
        f"phases={len(lock_records)} "
        f"strict_root_phases={sum(value == 3 for _, value, _ in lock_records)}"
    )
    print(f"maximum_label_chain_records={chain_records}")
    print(
        "first_marker_ancestry="
        f"records={len(ancestry_records)} "
        f"sharp={sum(delta == 0 for *_, delta in ancestry_records)}"
    )
    print(
        "local_marker_countermodel="
        f"length={len(local_marker)} post_nonone={len(local_trace.outputs)-1}"
    )
    print(f"unary_cube_marker_cn={exact_cn(unary_cube_marker)}")
    print(
        "top_marker_quotient_countermodel="
        f"original_cn={exact_cn(top_quotient_model)} "
        f"root={len(copied_root)} "
        f"token_profile={proper_circular_profile(exact_gap_tokens)} "
        f"weights={gap_successor_weights}"
    )
    print(f"nested_two_level_checkpoints={nested_checkpoints}")
    print(
        "nested_prefix_suffix_countermodel="
        f"length={len(delimiter_model)} "
        f"static_cuts={len(delimiter_outputs)} "
        f"cube_endpoint_value={delimiter_outputs[-1]}"
    )


if __name__ == "__main__":
    main()
