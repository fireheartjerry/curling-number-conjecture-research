"""Independent regressions for the surviving Cell C ``z=1`` row."""

from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path

import pytest

from research.generated_two_cube_cell_c_z1_atlas import (
    audit_transition_certificate,
    definition_first_witness,
    known_transition_certificates,
    render_atlas,
    scan_z1_transition_atlas,
)


Word = tuple[int, ...]


def _literal_reference_witness(word: Word) -> tuple[int, int]:
    feasible: dict[int, list[int]] = {}
    for exponent in range(2, len(word) + 1):
        for period in range(1, len(word) // exponent + 1):
            suffix = word[-exponent * period :]
            if suffix == suffix[:period] * exponent:
                feasible.setdefault(exponent, []).append(period)
    if not feasible:
        return 1, len(word)
    exponent = max(feasible)
    return exponent, min(feasible[exponent])


def _terminal_three_run(word: Word) -> int:
    run = 0
    for symbol in reversed(word):
        if symbol != 3:
            break
        run += 1
    return run


def _raw_candidate_is_static(
    *,
    branch: str,
    q: int,
    r: int,
    p: int,
    B: Word,
    Q: Word,
    U: Word,
    R: Word,
    X: Word,
) -> tuple[bool, bool]:
    z = U.index(2)
    h = next(
        (
            index
            for index, symbol in enumerate(U)
            if symbol != X[index % p]
        ),
        None,
    )
    is_z1 = (z, h) == (1, 0) and _terminal_three_run(B) <= 1
    if not is_z1:
        return False, False

    witness = _literal_reference_witness
    static = (
        witness(R * 2) == (2, q)
        and witness(R * 2 + B)[0] == 2
        and witness(B + R + B * 2) == (3, r)
        and witness(X * 3) == (3, p)
        and witness(X * 3 + U + B * 2) == (3, r)
    )
    return True, static


def _raw_reference_counts(max_q: int) -> dict[str, tuple[int, int, int]]:
    counts = {
        "p>q": [0, 0, 0],
        "p<q": [0, 0, 0],
    }

    for q in range(1, max_q + 1):
        for r in range(1, (q - 1) // 2 + 1):
            for t in range(r // 2 + 1, r):
                if 2 * t <= r:
                    continue
                p = q + t
                for R in product((2, 3), repeat=q):
                    B = R[:r]
                    Q = R[r : q - r]
                    if (
                        not Q
                        or B[0] != 2
                        or Q[0] != 3
                        or R[-r:] != B
                        or any(B[index] != B[index - t]
                               for index in range(t, r))
                    ):
                        continue
                    U = Q + B
                    X = B[r - t :] + U + B
                    counts["p>q"][0] += 1
                    is_z1, static = _raw_candidate_is_static(
                        branch="p>q",
                        q=q,
                        r=r,
                        p=p,
                        B=B,
                        Q=Q,
                        U=U,
                        R=R,
                        X=X,
                    )
                    counts["p>q"][1] += is_z1
                    counts["p>q"][2] += static

    for r in range(1, (max_q - 1) // 4 + 1):
        for nu in range(1, max_q + 1):
            for sigma in range(nu + 1, max_q + 1):
                q = 4 * r + nu + sigma
                if q > max_q:
                    break
                p = 2 * r + sigma
                P = q + r
                if not (
                    r < p - gcd(p, q)
                    and p > r + gcd(p, r)
                ):
                    continue
                d = q - p
                e = 2 * p - P
                if e < 0 and not 0 < -2 * e < r:
                    continue
                for R in product((2, 3), repeat=q):
                    B = R[:r]
                    Q = R[r : q - r]
                    Theta = Q[:nu]
                    D = Q[d:]
                    if (
                        B[0] != 2
                        or Theta[0] != 3
                        or R[-r:] != B
                        or Q != Theta + B * 2 + D
                        or Q[-(r + nu) :] != B + Theta
                    ):
                        continue
                    U = Q + B
                    X = D + B * 2
                    counts["p<q"][0] += 1
                    is_z1, static = _raw_candidate_is_static(
                        branch="p<q",
                        q=q,
                        r=r,
                        p=p,
                        B=B,
                        Q=Q,
                        U=U,
                        R=R,
                        X=X,
                    )
                    counts["p<q"][1] += is_z1
                    counts["p<q"][2] += static

    return {
        branch: tuple(values)
        for branch, values in counts.items()
    }


def _counter(items):
    return dict(items)


def test_definition_first_witness_matches_literal_oracle():
    checked = 0
    for length in range(1, 10):
        for word in product((2, 3), repeat=length):
            assert definition_first_witness(word) == (
                _literal_reference_witness(word)
            )
            checked += 1
    assert checked == 1022


def test_small_atlas_matches_raw_root_reference():
    atlas = scan_z1_transition_atlas(max_q=11)
    reference = _raw_reference_counts(11)

    assert (
        atlas.pgtq.structured_assignments,
        atlas.pgtq.z1_structural_assignments,
        atlas.pgtq.static_candidates,
    ) == reference["p>q"] == (102, 30, 3)
    assert (
        atlas.pltq.structured_assignments,
        atlas.pltq.z1_structural_assignments,
        atlas.pltq.static_candidates,
    ) == reference["p<q"] == (49, 22, 5)

    assert _counter(atlas.pgtq.phase_one_label_counts) == {
        "both_2": 2,
        "early_2_only": 0,
        "late_2_only": 0,
        "neither_2": 1,
    }
    assert _counter(atlas.pgtq.early_failure_counts) == {
        "1": 1,
        "4": 1,
        "5": 1,
    }
    assert _counter(atlas.pgtq.late_failure_counts) == {
        "1": 1,
        "4": 1,
        "5": 1,
    }
    assert _counter(atlas.pgtq.first_divergence_counts) == {
        "1": 1,
        "5": 1,
        "6": 1,
    }
    assert atlas.pgtq.phase_one_equal_local == 2
    assert atlas.pgtq.early_endpoint_exact == 3
    assert atlas.pgtq.late_endpoint_exact == 3
    assert (
        atlas.pgtq.early_predecessor_label_matches,
        atlas.pgtq.late_predecessor_label_matches,
        atlas.pgtq.both_predecessor_labels_match,
    ) == (1, 2, 1)

    assert _counter(atlas.pltq.phase_one_label_counts) == {
        "both_2": 5,
        "early_2_only": 0,
        "late_2_only": 0,
        "neither_2": 0,
    }
    assert _counter(atlas.pltq.early_failure_counts) == {
        "3": 1,
        "4": 4,
    }
    assert _counter(atlas.pltq.late_failure_counts) == {
        "4": 4,
        "5": 1,
    }
    assert _counter(atlas.pltq.first_divergence_counts) == {"1": 5}
    assert atlas.pltq.phase_one_different_crossing == 5
    assert atlas.pltq.r1_static_candidates == 5
    assert atlas.pltq.r1_phase_one_both_label_two == 5
    assert atlas.pltq.early_endpoint_exact == 5
    assert atlas.pltq.late_endpoint_exact == 4


def test_known_transition_certificates_are_recomputed_exactly():
    certificates = known_transition_certificates()
    assert tuple(certificate.name for certificate in certificates) == (
        "q8_r1_high_endpoint_failure",
        "q9_r1_high_endpoint_correct",
        "q11_r1_desynchronized_failure",
        "q16_r2_root_divergence",
        "q23_overlap_long_replay",
        "q29_r4_high_static",
    )
    assert all(
        audit_transition_certificate(certificate)
        for certificate in certificates
    )

    by_name = {
        certificate.name: certificate
        for certificate in certificates
    }
    assert (
        by_name["q8_r1_high_endpoint_failure"].early_phase_one,
        by_name["q8_r1_high_endpoint_failure"].late_phase_one,
        by_name["q8_r1_high_endpoint_failure"].late_endpoint,
    ) == ((2, 3), (2, 4), (2, 5))
    assert (
        by_name["q9_r1_high_endpoint_correct"].early_failure_phase,
        by_name["q9_r1_high_endpoint_correct"].late_failure_phase,
        by_name["q9_r1_high_endpoint_correct"].late_endpoint,
    ) == (4, 4, (2, 10))
    assert (
        by_name["q11_r1_desynchronized_failure"].early_failure_phase,
        by_name["q11_r1_desynchronized_failure"].late_failure_phase,
    ) == (3, 5)
    assert (
        by_name["q16_r2_root_divergence"].first_divergence_phase,
        by_name["q16_r2_root_divergence"].early_pairs[2],
        by_name["q16_r2_root_divergence"].late_pairs[2],
    ) == (2, (2, 6), (2, 8))
    assert (
        by_name["q23_overlap_long_replay"].seam,
        by_name["q23_overlap_long_replay"].early_failure_phase,
        by_name["q23_overlap_long_replay"].first_divergence_phase,
    ) == ("D=B[c:]Theta", 13, 18)
    assert (
        by_name["q29_r4_high_static"].early_phase_one,
        by_name["q29_r4_high_static"].late_phase_one,
        by_name["q29_r4_high_static"].early_failure_phase,
    ) == ((2, 9), (2, 20), 2)


def test_render_is_deterministic_and_rejects_invalid_bounds():
    atlas = scan_z1_transition_atlas(max_q=11)
    first = render_atlas(atlas, known_transition_certificates())
    second = render_atlas(atlas, known_transition_certificates())

    assert first == second
    assert first.startswith("label=bounded_binary_cell_C_z1_transition_atlas")
    assert "status=COMPUTED" in first
    assert "Cell_C=OPEN" in first
    assert "NOT_A_PROOF:" in first

    with pytest.raises(ValueError, match="max_q must be positive"):
        scan_z1_transition_atlas(max_q=0)


def test_authoritative_q25_artifact_has_pinned_digest():
    artifact = (
        Path(__file__).parents[1]
        / "research"
        / "outputs"
        / "generated_two_cube_cell_c_z1_atlas_2026-07-27.txt"
    )
    payload = artifact.read_bytes()

    assert b"\r" not in payload
    assert sha256(payload).hexdigest().upper() == (
        "975E542B6AEF428B39C087095BCB0A77AD68E390D597CC21F1FB43DA72BCEFE9"
    )
    text = payload.decode("utf-8")
    assert "pgtq.static_candidates=105851" in text
    assert "pltq.static_candidates=100053" in text
    assert "pgtq.phase_one_unclassified=0" in text
    assert "pltq.phase_one_unclassified=0" in text
