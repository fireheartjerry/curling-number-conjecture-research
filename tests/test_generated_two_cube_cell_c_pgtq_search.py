import hashlib
import json
import subprocess
import sys
from itertools import product
from pathlib import Path

import pytest

from research.generated_two_cube_cell_c_pgtq_search import (
    definition_first_witness,
    iter_pgtq_parameters,
    iter_structured_models,
    raw_root_parameter_pairs,
    render_scan,
    run_definition_first_oracle,
    scan_pgtq_boundary,
)


def _definition_first_witness(
    word: tuple[int, ...],
) -> tuple[int, int]:
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


def _raw_structural_keys(max_q: int) -> set[tuple[object, ...]]:
    retained: set[tuple[object, ...]] = set()
    for q in range(1, max_q + 1):
        for r in range(1, (q - 1) // 2 + 1):
            for t in range(1, r):
                if 2 * t <= r:
                    continue
                for R in product((2, 3), repeat=q):
                    B = R[:r]
                    U = R[r:]
                    if B[0] != 2 or U[0] != 3 or U[-r:] != B:
                        continue
                    if any(B[index] != B[index - t] for index in range(t, r)):
                        continue
                    retained.add((q, r, t, B, U))
    return retained


@pytest.fixture(scope="module")
def length_10_summary():
    return scan_pgtq_boundary(max_q=10)


def test_equality_generator_matches_raw_binary_roots_through_q_10():
    generated = {
        (
            model.parameters.q,
            model.parameters.r,
            model.parameters.t,
            model.B,
            model.U,
        )
        for parameters in iter_pgtq_parameters(max_q=10)
        for model in iter_structured_models(parameters)
    }
    raw = _raw_structural_keys(10)

    assert generated == raw
    assert len(generated) == 42


def test_definition_first_witness_is_independent_on_all_oracle_words():
    checked = 0
    for length in range(1, 11):
        for word in product((2, 3), repeat=length):
            assert _definition_first_witness(word) == (
                definition_first_witness(word)
            )
            checked += 1

    assert checked == 2046


def test_q_10_stage_counts_are_exact_and_nonvacuous(length_10_summary):
    assert length_10_summary.max_q == 10
    assert length_10_summary.parameter_triples == 6
    assert raw_root_parameter_pairs(max_q=10) == 3456
    assert length_10_summary.raw_root_parameter_pairs == 3456
    assert length_10_summary.structured_assignments == 42
    assert length_10_summary.canonical_r2 == 7
    assert length_10_summary.standalone_exponent_two == 7
    assert length_10_summary.canonical_x3 == 7
    assert length_10_summary.late_exponent_replays == 1
    assert length_10_summary.exact_late_window_replays == 1
    assert length_10_summary.late_period_cap_survivors == 0
    assert length_10_summary.terminal_h_canonical == 1
    assert length_10_summary.early_after_exact_late_replays == 0
    assert length_10_summary.full_continuation_replays == 0
    assert length_10_summary.I_window_survivors == 0
    assert length_10_summary.J_window_survivors == 0
    assert length_10_summary.first_mismatch_trichotomy_candidates == 3
    assert length_10_summary.trichotomy_z1_h0 == 0
    assert length_10_summary.trichotomy_z2_h0 == 1
    assert length_10_summary.trichotomy_z2_h1 == 2
    assert length_10_summary.trichotomy_early_failure_phase_0 == 0
    assert length_10_summary.trichotomy_early_failure_phase_1 == 1
    assert length_10_summary.trichotomy_early_failure_phase_2 == 0
    assert length_10_summary.trichotomy_early_failure_phase_other == 2
    assert length_10_summary.trichotomy_exact_early_windows == 0


def test_trichotomy_diagnostic_enforces_terminal_run_inequality():
    summary = scan_pgtq_boundary(max_q=12)

    assert summary.first_mismatch_trichotomy_candidates == 16
    assert summary.trichotomy_z1_h0 == 6
    assert summary.trichotomy_z2_h0 == 4
    assert summary.trichotomy_z2_h1 == 6


def test_definition_first_raw_oracle_reproduces_q_10_counts():
    oracle = run_definition_first_oracle(max_q=10)

    assert oracle.max_q == 10
    assert oracle.parameter_triples == 6
    assert oracle.raw_root_parameter_pairs == 3456
    assert oracle.structured_assignments == 42
    assert oracle.canonical_r2 == 7
    assert oracle.standalone_exponent_two == 7
    assert oracle.canonical_x3 == 7
    assert oracle.late_exponent_replays == 1
    assert oracle.exact_late_window_replays == 1
    assert oracle.late_period_cap_survivors == 0
    assert oracle.terminal_h_canonical == 1
    assert oracle.early_after_exact_late_replays == 0
    assert oracle.full_continuation_replays == 0
    assert oracle.I_window_survivors == 0
    assert oracle.J_window_survivors == 0


def test_q_9_certificate_pins_shadow_and_early_failure(length_10_summary):
    certificate = length_10_summary.late_replay_certificate

    assert certificate is not None
    assert (certificate.q, certificate.r, certificate.t) == (9, 3, 2)
    assert (certificate.P, certificate.p) == (12, 11)
    assert certificate.B == tuple(map(int, "232"))
    assert certificate.C == tuple(map(int, "322"))
    assert certificate.U == tuple(map(int, "322232"))
    assert certificate.R == tuple(map(int, "232322232"))
    assert certificate.X == tuple(map(int, "32322232232"))
    assert certificate.Y == tuple(map(int, "232232322232"))
    assert certificate.rotated_Y == tuple(map(int, "223223232223"))
    assert certificate.r2_witness == (2, 9)
    assert certificate.standalone_witness == (2, 3)
    assert certificate.x3_witness == (3, 11)
    assert certificate.late_witnesses == (
        (3, 3),
        (2, 2),
        (2, 2),
        (2, 1),
        (3, 1),
        (2, 12),
    )
    assert certificate.h_witness == (2, 12)
    assert certificate.early_witnesses == (
        (3, 11),
        (3, 11),
        (3, 11),
        (2, 1),
        (3, 1),
        (1, 38),
        (2, 9),
    )
    assert certificate.first_early_mismatch == (1, 2, (3, 11))
    assert certificate.shadow_predecessor == 2
    assert certificate.shadow_last_symbol == 2
    assert certificate.has_shifted_P_square
    assert certificate.U == certificate.B[1:] + certificate.B[:1] + certificate.B


def test_render_is_deterministic_and_labels_bounded_scope(length_10_summary):
    oracle = run_definition_first_oracle(max_q=10)

    first = render_scan(length_10_summary, oracle)
    second = render_scan(length_10_summary, oracle)

    assert first == second
    assert (
        hashlib.sha256(first.encode("utf-8")).hexdigest().upper()
        == "CB408F6CE4D74E617973E0F583DC085BB5ED531B58190FA2DE7B805958FDCCB9"
    )
    assert first.startswith("label=bounded_binary_cell_C_p_gt_q_boundary\n")
    assert "late_period_cap_survivors=0\n" in first
    assert "I_window_survivors=0\n" in first
    assert "J_window_survivors=0\n" in first
    assert "oracle_structured_assignments=42\n" in first
    certificate_line = next(
        line
        for line in first.splitlines()
        if line.startswith("late_replay_certificate=")
    )
    serialized = json.loads(certificate_line.split("=", 1)[1])
    assert serialized["R"] == list(map(int, "232322232"))
    assert serialized["late_witnesses"][-1] == [2, 12]
    assert first.endswith(
        "NOT_A_PROOF: bounded binary p>q boundary search; "
        "zero bounded survivors does not prove Cell C.\n"
    )


def test_preserved_q_25_output_has_exact_counts_and_stable_hash():
    output_path = (
        Path(__file__).parents[1]
        / "research"
        / "outputs"
        / "generated_two_cube_cell_c_pgtq_scan_2026-07-27.txt"
    )
    payload = output_path.read_bytes()
    text = payload.decode("utf-8")

    assert "max_q=25\n" in text
    assert "parameter_triples=220\n" in text
    assert "raw_root_parameter_pairs=1792552320\n" in text
    assert "structured_assignments=2388798\n" in text
    assert "canonical_r2=563708\n" in text
    assert "standalone_exponent_two=563708\n" in text
    assert "canonical_x3=563688\n" in text
    assert "late_exponent_replays=1\n" in text
    assert "exact_late_window_replays=1\n" in text
    assert "late_period_cap_survivors=0\n" in text
    assert "terminal_h_canonical=1\n" in text
    assert "early_after_exact_late_replays=0\n" in text
    assert "I_window_survivors=0\n" in text
    assert "J_window_survivors=0\n" in text
    assert "oracle_max_q=10\n" in text
    assert "oracle_structured_assignments=42\n" in text
    assert (
        hashlib.sha256(payload).hexdigest().upper()
        == "8837CF352EA83B6F2195B17FFD222E42F831C7EA332827EC9C2D7A29F026B06E"
    )


def test_script_entrypoint_runs_from_repository_root():
    root = Path(__file__).parents[1]
    script = (
        root / "research" / "generated_two_cube_cell_c_pgtq_search.py"
    )
    completed = subprocess.run(
        [
            sys.executable,
            str(script),
            "--max-q",
            "10",
            "--oracle-max-q",
            "10",
        ],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.startswith(
        "label=bounded_binary_cell_C_p_gt_q_boundary\n"
    )


@pytest.mark.parametrize("bound", [0, -1])
def test_invalid_bounds_fail_closed(bound):
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        tuple(iter_pgtq_parameters(max_q=bound))
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        raw_root_parameter_pairs(max_q=bound)
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        scan_pgtq_boundary(max_q=bound)
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        run_definition_first_oracle(max_q=bound)
