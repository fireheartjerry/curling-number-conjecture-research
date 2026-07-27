import hashlib
import importlib
import subprocess
import sys
from pathlib import Path

import pytest


MODULE_NAME = (
    "research.generated_two_cube_cell_c_pgtq_early_replay_smt"
)
ROOT = Path(__file__).parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "generated_two_cube_cell_c_pgtq_early_replay_smt.py"
)
OUTPUT_PATH = (
    ROOT
    / "research"
    / "outputs"
    / "generated_two_cube_cell_c_pgtq_early_replay_smt_2026-07-27.txt"
)


@pytest.fixture(scope="module")
def checkpoint():
    return importlib.import_module(MODULE_NAME)


@pytest.fixture(scope="module")
def oracle_summary(checkpoint):
    return checkpoint.run_direct_oracle(max_q=14, timeout_ms=3000)


def test_checkpoint_module_exists():
    assert MODULE_PATH.is_file()


def test_parameter_domain_counts_are_exact(checkpoint):
    through_14 = tuple(checkpoint.iter_parameter_triples(max_q=14))
    through_40 = tuple(checkpoint.iter_parameter_triples(max_q=40))

    assert len(through_14) == 26
    assert len(through_40) == 1050
    assert sum(
        2
        ** (
            parameters.t
            - 1
            + parameters.q
            - 2 * parameters.r
            - 1
        )
        for parameters in through_14
    ) == 1014
    assert (
        sum(parameters.q == 26 for parameters in through_40) == 30
    )
    assert (
        sum(parameters.q == 40 for parameters in through_40) == 81
    )


def test_definition_first_oracle_agrees_with_solver_through_q_14(
    oracle_summary,
):
    assert oracle_summary.max_q == 14
    assert oracle_summary.parameter_triples == 26
    assert oracle_summary.structured_assignments == 1014
    assert oracle_summary.direct_sat == 0
    assert oracle_summary.solver_sat == 0
    assert oracle_summary.solver_unsat == 26
    assert oracle_summary.solver_unknown == 0
    assert oracle_summary.mismatches == ()


def test_known_early_replay_models_collapse_without_canonical_r2(
    checkpoint,
):
    certificates = checkpoint.known_collapse_certificates()

    assert tuple(
        (item.q, item.r, item.t) for item in certificates
    ) == (
        (10, 4, 3),
        (17, 4, 3),
        (17, 7, 4),
        (19, 9, 8),
        (27, 10, 7),
    )
    assert tuple(item.r2_witness for item in certificates) == (
        (2, 6),
        (2, 3),
        (2, 4),
        (2, 4),
        (2, 4),
    )
    assert tuple(item.x3_witness for item in certificates) == (
        (3, 13),
        (3, 20),
        (3, 21),
        (3, 27),
        (3, 34),
    )
    assert all(
        checkpoint.audit_collapse_certificate(item)
        for item in certificates
    )

    for item in certificates:
        parameters = checkpoint.PgtqParameters(
            q=item.q,
            r=item.r,
            t=item.t,
        )
        relaxed = checkpoint.solve_parameter(
            parameters,
            require_canonical_r2=False,
            timeout_ms=3000,
        )
        exact = checkpoint.solve_parameter(
            parameters,
            require_canonical_r2=True,
            timeout_ms=3000,
        )
        assert relaxed.status == "sat"
        assert exact.status == "unsat"


def test_q_9_endpoint_jump_is_exact_and_fails_early_phase_1(
    checkpoint,
):
    certificate = checkpoint.endpoint_jump_certificate()

    assert (certificate.q, certificate.r, certificate.t) == (9, 4, 3)
    assert certificate.B == tuple(map(int, "2332"))
    assert certificate.Q == tuple(map(int, "3"))
    assert certificate.U == tuple(map(int, "32332"))
    assert certificate.R == tuple(map(int, "233232332"))
    assert certificate.X == tuple(map(int, "332323322332"))
    assert certificate.Y == tuple(map(int, "2332233232332"))
    assert certificate.x3_witness == (3, 12)
    assert certificate.g_pre_witness == (2, 1)
    assert certificate.g_witness == (2, 9)
    assert certificate.h_pre_witness == (2, 1)
    assert certificate.h_witness == (2, 13)
    assert certificate.appended_symbol == 2
    assert certificate.first_early_mismatch == (1, 2, (3, 12))
    assert checkpoint.audit_endpoint_jump_certificate(certificate)


def test_small_render_is_deterministic_and_scope_safe(
    checkpoint,
    oracle_summary,
):
    summary = checkpoint.scan_early_replay_wall(
        max_q=14,
        timeout_ms=3000,
    )
    certificates = checkpoint.known_collapse_certificates()
    jump = checkpoint.endpoint_jump_certificate()

    first = checkpoint.render_checkpoint(
        summary,
        oracle_summary,
        certificates,
        jump,
    )
    second = checkpoint.render_checkpoint(
        summary,
        oracle_summary,
        certificates,
        jump,
    )

    assert first == second
    assert first.startswith(
        "label=bounded_binary_cell_C_p_gt_q_early_replay_qfbv\n"
    )
    assert "solver_logic=QF_BV\n" in first
    assert "uses_first_mismatch_trichotomy=false\n" in first
    assert (
        "omits=standalone_R2B,canonical_F_B3,later_replay,"
        "J_only_bridge_replay,canonical_H_pair_2_P,"
        "all_proper_period_caps\n"
    ) in first
    assert "parameter_triples=26\n" in first
    assert "sat=0\nunsat=26\nunknown=0\n" in first
    assert "oracle_structured_assignments=1014\n" in first
    assert "oracle_mismatch_count=0\n" in first
    assert "historical_collapse_certificate_count=4\n" in first
    assert "collapse_certificate_count=5\n" in first
    assert "endpoint_jump_q=9\n" in first
    assert first.endswith(
        "NOT_A_PROOF: bounded QF_BV UNSAT is computed evidence only; "
        "the unbounded p>q wall and Cell C remain open.\n"
    )


def test_preserved_q_40_output_has_exact_counts_and_stable_hash():
    payload = OUTPUT_PATH.read_bytes()
    text = payload.decode("utf-8")

    assert "max_q=40\n" in text
    assert "timeout_ms=3000\n" in text
    assert "parameter_triples=1050\n" in text
    assert "sat=0\nunsat=1050\nunknown=0\n" in text
    assert "q_26_parameter_triples=30\n" in text
    assert "q_40_parameter_triples=81\n" in text
    assert "oracle_max_q=14\n" in text
    assert "oracle_parameter_triples=26\n" in text
    assert "oracle_structured_assignments=1014\n" in text
    assert "oracle_mismatch_count=0\n" in text
    assert "collapse_certificate_count=5\n" in text
    assert "endpoint_jump_q=9\n" in text
    assert "status=COMPUTED\n" in text
    assert (
        "omits=standalone_R2B,canonical_F_B3,later_replay,"
        "J_only_bridge_replay,canonical_H_pair_2_P,"
        "all_proper_period_caps\n"
    ) in text
    assert (
        hashlib.sha256(payload).hexdigest().upper()
        == "D3C8FB986F20665777EB3DDD362F3DA1E09E88328716241809AADC1B56A0CF09"
    )


def test_script_entrypoint_runs_from_repository_root():
    completed = subprocess.run(
        [
            sys.executable,
            str(MODULE_PATH),
            "--max-q",
            "10",
            "--oracle-max-q",
            "10",
            "--timeout-ms",
            "3000",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.startswith(
        "label=bounded_binary_cell_C_p_gt_q_early_replay_qfbv\n"
    )
    assert "parameter_triples=6\n" in completed.stdout
    assert "sat=0\nunsat=6\nunknown=0\n" in completed.stdout


@pytest.mark.parametrize("bound", [0, -1])
def test_invalid_q_bounds_fail_closed(checkpoint, bound):
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        tuple(checkpoint.iter_parameter_triples(max_q=bound))
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        checkpoint.scan_early_replay_wall(
            max_q=bound,
            timeout_ms=3000,
        )
    with pytest.raises(ValueError, match=r"^max_q must be positive$"):
        checkpoint.run_direct_oracle(
            max_q=bound,
            timeout_ms=3000,
        )


@pytest.mark.parametrize("timeout_ms", [0, -1])
def test_invalid_timeout_fails_closed(checkpoint, timeout_ms):
    parameters = checkpoint.PgtqParameters(q=9, r=3, t=2)
    with pytest.raises(ValueError, match=r"^timeout_ms must be positive$"):
        checkpoint.solve_parameter(
            parameters,
            require_canonical_r2=True,
            timeout_ms=timeout_ms,
        )
