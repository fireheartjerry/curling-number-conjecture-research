"""Independent regressions for the D-035 local bridge census."""

from __future__ import annotations

import ast
import hashlib
import subprocess
import sys
from dataclasses import asdict, replace
from pathlib import Path

import pytest

from research.generated_two_cube_cell_c_z1_atlas import (
    Z1Model,
    is_z1_static_candidate,
    is_z1_structural,
    iter_z1_branch_models,
)
from research.generated_two_cube_d035_bridge_census import (
    audit_bridge_certificate,
    known_bridge_certificates,
    render_census,
    scan_bridge_census,
    trace_bridge,
)
from tests.d035_bridge_oracle import (
    LITERAL_CERTIFICATES,
    PERIOD_P_KEYS,
    SEAM_CROSS_KEYS,
    THEOREM_KEYS,
    audit_literal_certificate,
    fourth_power_roots,
    raw_reference,
    visible_proper_fourth_roots,
    word,
)

EXPECTED_Q25_ARTIFACT_SHA256 = (
    "60a3d2f846ac34d081a5321ac24bb7114c8c6b1a5dbf7e846756331ca6454df7"
)
NONPROOF_LINE = (
    "NOT_A_PROOF: bounded standalone-local D-035 bridge census; "
    "no arbitrary left context was enumerated, and zero violations "
    "prove neither bridge theorem, boundary wall, nor Cell C.\n"
)


def _pgtq_q12_model() -> Z1Model:
    return Z1Model(
        branch="p>q",
        q=12,
        r=4,
        p=15,
        P=16,
        seam="none",
        B=word("2232"),
        Theta=(),
        D=(),
        Q=word("3233"),
        U=word("32332232"),
        R=word("223232332232"),
        X=word("232323322322232"),
    )


def _zero_counter(keys: tuple[str, ...]) -> dict[str, int]:
    return {key: 0 for key in keys}


def _run_cli(*arguments: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        (
            sys.executable,
            "-m",
            "research.generated_two_cube_d035_bridge_census",
            *arguments,
        ),
        cwd=Path(__file__).resolve().parents[1],
        check=True,
        capture_output=True,
    )


def _normalize_newlines(value: bytes) -> bytes:
    return value.replace(b"\r\n", b"\n")


def test_raw_oracle_module_has_only_stdlib_imports():
    oracle_path = Path(__file__).with_name("d035_bridge_oracle.py")
    tree = ast.parse(oracle_path.read_text(encoding="utf-8"))
    imported_roots = {
        alias.name.split(".", 1)[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_roots.update(
        node.module.split(".", 1)[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module != "__future__"
    )
    assert imported_roots <= {
        "collections",
        "dataclasses",
        "itertools",
        "math",
    }


def test_trace_bridge_checks_literal_suffixes_and_both_fourth_root_sets():
    model = _pgtq_q12_model()

    trace = trace_bridge(model)

    assert trace.first_failure_phase is None
    assert tuple(cut.witness for cut in trace.cuts) == (
        (2, 12),
        (2, 1),
        (3, 1),
        (2, 12),
        (2, 4),
        (2, 1),
        (3, 1),
        (2, 4),
    )
    assert tuple(cut.requested for cut in trace.cuts) == word("22322232")
    assert tuple(cut.half for cut in trace.cuts) == (
        "first",
        "first",
        "first",
        "first",
        "second",
        "second",
        "second",
        "second",
    )

    state = model.X * 3 + model.U
    for cut in trace.cuts:
        expected_visible_suffix = (
            model.R * 2 + model.B[: cut.index]
            if cut.half == "first"
            else model.B * 2 + model.B[: cut.index]
        )
        assert (
            state[-cut.visible_context_length :]
            == expected_visible_suffix
        )
        assert cut.full_fourth_power_roots == fourth_power_roots(state)
        assert (
            cut.visible_proper_fourth_roots
            == visible_proper_fourth_roots(
                expected_visible_suffix,
                ambient_period=(
                    model.q if cut.half == "first" else model.r
                ),
            )
        )
        state += (cut.requested,)

    assert all(not cut.full_fourth_power_roots for cut in trace.cuts)
    assert all(not cut.visible_proper_fourth_roots for cut in trace.cuts)
    assert trace.endpoint == (3, 4)


def test_trace_bridge_detects_full_and_visible_fourth_power_roots():
    model = Z1Model(
        branch="p>q",
        q=8,
        r=3,
        p=10,
        P=11,
        seam="none",
        B=(2, 2, 2),
        Theta=(),
        D=(),
        Q=(3, 2),
        U=(3, 2, 2, 2, 2),
        R=(2, 2, 2, 3, 2, 2, 2, 2),
        X=(2, 2, 3, 2, 2, 2, 2, 2, 2, 2),
    )

    trace = trace_bridge(model)

    assert trace.first_failure_phase == 0
    assert len(trace.cuts) == 1
    cut = trace.cuts[0]
    assert cut.witness == (4, 1)
    assert cut.requested == 2
    assert (
        cut.full_fourth_power_roots,
        cut.visible_proper_fourth_roots,
    ) == ((1,), (1,))


def test_q12_census_matches_independent_oracle_and_audit_universes():
    census = scan_bridge_census(max_q=12)
    reference = raw_reference(12)

    assert (
        census.pgtq.structured_assignments,
        census.pgtq.z1_structural_assignments,
        census.pgtq.static_candidates,
        census.pgtq.local_bridge_replays,
        census.pgtq.all_proper_periods_below_P_local_replays,
        census.pgtq.local_endpoint_exact_replays,
        census.pgtq.proper_cut_count,
    ) == (222, 60, 6, 1, 1, 1, 8)
    assert dict(census.pgtq.first_failure_phase_counts) == {
        "2": 1,
        "3": 1,
        "5": 1,
        "7": 2,
    }
    assert dict(census.pgtq.local_r_counts) == {"4": 1}
    assert dict(census.pgtq.local_B_counts) == {"2232": 1}
    assert dict(census.pgtq.local_seam_counts) == {"none": 1}
    assert dict(census.pgtq.cut_relation_counts) == {
        "first:2:<q": 1,
        "first:2:=q": 2,
        "first:3:<q": 1,
        "second:2:<r": 1,
        "second:2:=r": 2,
        "second:3:<r": 1,
    }
    expected_pgtq_period_P = _zero_counter(PERIOD_P_KEYS)
    expected_pgtq_period_P.update(
        {
            "first:2:<P": 3,
            "first:3:<P": 1,
            "second:2:<P": 3,
            "second:3:<P": 1,
        }
    )
    assert (
        dict(census.pgtq.period_P_relation_counts)
        == expected_pgtq_period_P
    )
    expected_pgtq_seams = _zero_counter(SEAM_CROSS_KEYS)
    expected_pgtq_seams["lt_r:seam_false"] = 1
    assert (
        dict(census.pgtq.second_half_three_seam_cross_counts)
        == expected_pgtq_seams
    )
    expected_pgtq_opportunities = _zero_counter(THEOREM_KEYS)
    expected_pgtq_opportunities.update(
        {
            "endpoint_pair": 1,
            "first_2_cap": 3,
            "second_2_cap": 3,
            "first_3_bound": 1,
            "first_3_visibility": 1,
            "second_3_bound": 1,
            "second_3_visibility": 1,
            "full_fourth_power": 8,
            "visible_fourth_power": 8,
        }
    )
    assert (
        dict(census.pgtq.theorem_opportunity_counts)
        == expected_pgtq_opportunities
    )

    assert (
        census.pltq.structured_assignments,
        census.pltq.z1_structural_assignments,
        census.pltq.static_candidates,
        census.pltq.local_bridge_replays,
        census.pltq.all_proper_periods_below_P_local_replays,
        census.pltq.local_endpoint_exact_replays,
        census.pltq.proper_cut_count,
    ) == (107, 46, 9, 9, 9, 9, 18)
    assert dict(census.pltq.first_failure_phase_counts) == {}
    assert dict(census.pltq.local_r_counts) == {"1": 9}
    assert dict(census.pltq.local_B_counts) == {"2": 9}
    assert dict(census.pltq.local_seam_counts) == {"D=JBTheta": 9}
    assert dict(census.pltq.cut_relation_counts) == {
        "first:2:=q": 9,
        "second:2:=r": 9,
    }
    expected_pltq_period_P = _zero_counter(PERIOD_P_KEYS)
    expected_pltq_period_P.update(
        {
            "first:2:<P": 9,
            "second:2:<P": 9,
        }
    )
    assert (
        dict(census.pltq.period_P_relation_counts)
        == expected_pltq_period_P
    )
    assert dict(
        census.pltq.second_half_three_seam_cross_counts
    ) == _zero_counter(SEAM_CROSS_KEYS)
    expected_pltq_opportunities = _zero_counter(THEOREM_KEYS)
    expected_pltq_opportunities.update(
        {
            "endpoint_pair": 9,
            "first_2_cap": 9,
            "second_2_cap": 9,
            "full_fourth_power": 18,
            "visible_fourth_power": 18,
        }
    )
    assert (
        dict(census.pltq.theorem_opportunity_counts)
        == expected_pltq_opportunities
    )

    for summary in (census.pgtq, census.pltq):
        assert summary.full_fourth_power_root_occurrences == 0
        assert summary.full_fourth_power_cut_count == 0
        assert summary.visible_proper_fourth_root_occurrences == 0
        assert summary.visible_proper_fourth_cut_count == 0
        assert dict(summary.theorem_violation_counts) == _zero_counter(
            THEOREM_KEYS
        )

    for branch, summary in (
        ("p>q", census.pgtq),
        ("p<q", census.pltq),
    ):
        raw = reference[branch]
        for field, expected in raw.items():
            observed = getattr(summary, field)
            if isinstance(expected, dict):
                observed = dict(observed)
            assert observed == expected, (branch, field)


def test_six_literal_certificates_are_independently_and_production_audited():
    assert all(
        audit_literal_certificate(certificate)
        for certificate in LITERAL_CERTIFICATES
    )

    certificates = known_bridge_certificates()

    assert tuple(
        asdict(certificate) for certificate in certificates
    ) == tuple(
        asdict(certificate) for certificate in LITERAL_CERTIFICATES
    )
    assert all(
        audit_bridge_certificate(certificate)
        for certificate in certificates
    )
    assert certificates[0].second_half_three_rows == (
        (2, (3, 1), False),
    )
    assert all(
        certificate.second_half_three_rows == ((3, (3, 1), True),)
        for certificate in certificates[2:]
    )
    assert certificates[4].Q != certificates[5].Q
    assert certificates[4].X != certificates[5].X

    first = certificates[0]
    assert not audit_bridge_certificate(
        replace(first, all_proper_periods_below_P=False)
    )
    assert not audit_bridge_certificate(
        replace(first, second_half_three_rows=())
    )
    assert not audit_bridge_certificate(
        replace(first, full_fourth_power_cut_count=1)
    )
    assert not audit_bridge_certificate(
        replace(first, visible_proper_fourth_root_occurrences=1)
    )


def test_certificate_audits_fail_closed_on_types_and_shapes():
    production = known_bridge_certificates()[0]
    literal = LITERAL_CERTIFICATES[0]
    zeroed_fields = {
        "q": 0,
        "r": 0,
        "p": 0,
        "P": 0,
        "B": (),
        "Q": (),
        "U": (),
        "R": (),
        "X": (),
        "expected_cut_pairs": (),
        "second_half_three_rows": (),
        "endpoint": (0, 0),
    }
    production_invalid = (
        None,
        replace(production, **zeroed_fields),
        replace(production, full_fourth_power_cut_count=False),
        replace(production, all_proper_periods_below_P=1),
        replace(production, B=list(production.B)),
        replace(production, expected_cut_pairs=((2,),)),
        replace(
            production,
            second_half_three_rows=((2, (3, 1), 1),),
        ),
        replace(production, endpoint=[3, 4]),
    )
    literal_invalid = (
        None,
        replace(literal, **zeroed_fields),
        replace(literal, full_fourth_power_cut_count=False),
        replace(literal, all_proper_periods_below_P=1),
        replace(literal, B=list(literal.B)),
        replace(literal, expected_cut_pairs=((2,),)),
        replace(
            literal,
            second_half_three_rows=((2, (3, 1), 1),),
        ),
        replace(literal, endpoint=[3, 4]),
    )

    assert all(
        audit_bridge_certificate(certificate) is False
        for certificate in production_invalid
    )
    assert all(
        audit_literal_certificate(certificate) is False
        for certificate in literal_invalid
    )


def test_public_atlas_predicates_fail_closed_on_malformed_models():
    malformed = replace(_pgtq_q12_model(), r=0, B=())
    nonbinary = replace(_pgtq_q12_model(), B=(2, 2, 4, 2))

    assert is_z1_structural(None) is False
    assert is_z1_static_candidate(None) is False
    assert is_z1_structural(malformed) is False
    assert is_z1_static_candidate(malformed) is False
    assert is_z1_structural(nonbinary) is False
    assert is_z1_static_candidate(nonbinary) is False


def test_render_is_deterministic_standalone_scoped_and_fail_closed():
    census = scan_bridge_census(max_q=12)
    certificates = known_bridge_certificates()

    first = render_census(census, certificates)
    second = render_census(census, certificates)

    assert first == second
    assert first.startswith(
        "label=bounded_binary_D035_two_half_local_bridge_census\n"
        "max_q=12\n"
        "alphabet=2,3\n"
        "status=COMPUTED\n"
    )
    for exact_line in (
        "row=z1_h0",
        "mismatch_index=0",
        "orbit_scope=standalone_G_loc_seed",
        "target_assumption=none",
        "full_context_not_enumerated=true",
        "I_bridge_membership=K0_and_K2r_only",
        "J_bridge_membership=all_K0_through_K2r",
        "two_cut_cap=target_independent",
        "interior_three_cut_I_cap=not_automatic",
        "proper_bridge_J_cap=under_J_negation",
        "Cell_C=OPEN",
        (
            "counter_universe.structured_assignments="
            "all_exact_normal_form_assignments"
        ),
        (
            "counter_universe.z1_structural_assignments="
            "structured_assignments_with_z1_mismatch0_lambda_at_most1"
        ),
        (
            "counter_universe.static_candidates="
            "z1_structural_assignments_passing_exact_static_filters"
        ),
        (
            "counter_universe.first_failure_phase_counts="
            "failed_local_prefixes_of_static_candidates"
        ),
        (
            "counter_universe.local_bridge_replays="
            "static_candidates_matching_all_2r_requested_labels"
        ),
        (
            "counter_universe.local_replay_model_counters="
            "complete_local_bridge_replays"
        ),
        (
            "counter_universe.proper_cut_counters="
            "proper_cuts_of_complete_local_bridge_replays"
        ),
        (
            "counter_universe.theorem_opportunity_counts="
            "eligible_conclusions_after_complete_local_replay"
        ),
        (
            "counter_universe.theorem_violation_counts="
            "matching_theorem_opportunities_only"
        ),
        (
            "counter_definition.first_failure_phase_counts="
            "one_first_mismatch_phase_per_failed_static_candidate"
        ),
        (
            "counter_definition.proper_cut_count="
            "sum_2r_over_complete_local_bridge_replays"
        ),
        (
            "counter_definition.full_fourth_power_root_occurrences="
            "sum_full_state_fourth_suffix_roots_over_proper_cuts"
        ),
        (
            "counter_definition.full_fourth_power_cut_count="
            "proper_cuts_with_a_full_state_fourth_suffix_root"
        ),
        (
            "counter_definition.visible_proper_fourth_root_occurrences="
            "sum_visible_proper_fourth_suffix_roots_over_proper_cuts"
        ),
        (
            "counter_definition.visible_proper_fourth_cut_count="
            "proper_cuts_with_a_visible_proper_fourth_suffix_root"
        ),
        (
            "counter_definition.period_P_relation_counts="
            "proper_cuts_by_half_label_and_canonical_period_vs_P"
        ),
        (
            "counter_definition.second_half_three_seam_cross_counts="
            "second_half_3_cuts_by_period_vs_r_and_independent_seam"
        ),
        (
            "counter_definition.theorem_opportunity_counts="
            "theorem_specific_eligible_instances"
        ),
        (
            "counter_definition.theorem_violation_counts="
            "failed_conclusions_within_matching_opportunities"
        ),
    ):
        assert f"{exact_line}\n" in first
    assert "actual_bridge" not in first
    assert "actuality=" not in first
    assert "pgtq.local_bridge_replays=1\n" in first
    assert "pltq.local_bridge_replays=9\n" in first
    assert "pgtq.period_P_relation_counts=" in first
    assert "pgtq.second_half_three_seam_cross_counts=" in first
    assert "pgtq.theorem_opportunity_counts=" in first
    assert "certificate_count=6\n" in first
    assert first.endswith(
        "NOT_A_PROOF: bounded standalone-local D-035 bridge census; "
        "no arbitrary left context was enumerated, and zero violations "
        "prove neither bridge theorem, boundary wall, nor Cell C.\n"
    )

    for invalid_max_q in (0, -1, 1.5, True):
        with pytest.raises(ValueError, match="positive integer"):
            scan_bridge_census(max_q=invalid_max_q)
    with pytest.raises(ValueError, match="positive integer"):
        tuple(iter_z1_branch_models(branch="p>q", max_q=0))
    with pytest.raises(ValueError, match="branch"):
        tuple(iter_z1_branch_models(branch="invalid", max_q=1))
    with pytest.raises(ValueError, match="valid D-035 model"):
        trace_bridge(replace(_pgtq_q12_model(), r=0, B=()))

    invalid = replace(certificates[0], endpoint=(4, 1))
    with pytest.raises(ValueError, match="invalid bridge certificate"):
        render_census(census, (invalid,) + certificates[1:])
    with pytest.raises(ValueError, match="invalid bridge certificate"):
        render_census(census, (None,) + certificates[1:])
    with pytest.raises(ValueError, match="exactly six"):
        render_census(census, certificates[:-1])


def test_render_rejects_incoherent_census_metadata():
    census = scan_bridge_census(max_q=12)
    certificates = known_bridge_certificates()
    invalid_censuses = (
        None,
        replace(census, max_q=25),
        replace(census, max_q=True),
        replace(
            census,
            pgtq=replace(census.pgtq, max_q=11),
        ),
        replace(
            census,
            pltq=replace(census.pltq, branch="not-p<q"),
        ),
        replace(census, pgtq=None),
    )

    for invalid_census in invalid_censuses:
        with pytest.raises(ValueError, match="invalid bridge census"):
            render_census(invalid_census, certificates)


def test_cli_keeps_deterministic_artifact_content_off_timing_stream(
    tmp_path: Path,
):
    first = _run_cli("--max-q", "1")
    second = _run_cli("--max-q", "1")
    normalized_first = _normalize_newlines(first.stdout)
    normalized_second = _normalize_newlines(second.stdout)

    assert normalized_first == normalized_second
    assert normalized_first.endswith(NONPROOF_LINE.encode("utf-8"))
    assert b"scan_seconds=" not in first.stdout
    assert b"scan_seconds=" in first.stderr

    output = tmp_path / "q1.txt"
    file_run = _run_cli(
        "--max-q",
        "1",
        "--output",
        str(output),
    )
    assert file_run.stdout == b""
    assert b"scan_seconds=" in file_run.stderr
    assert output.read_bytes().endswith(NONPROOF_LINE.encode("utf-8"))


def test_authoritative_q25_bridge_artifact_is_byte_reproducible(
    tmp_path: Path,
):
    artifact = (
        Path(__file__).resolve().parents[1]
        / "research"
        / "outputs"
        / "generated_two_cube_d035_bridge_census_2026-07-27.txt"
    )
    reproduced = tmp_path / "reproduced-q25.txt"
    completed = _run_cli(
        "--max-q",
        "25",
        "--output",
        str(reproduced),
    )
    expected_bytes = reproduced.read_bytes()
    artifact_bytes = artifact.read_bytes()

    assert completed.stdout == b""
    assert b"scan_seconds=" in completed.stderr
    assert artifact_bytes == expected_bytes
    assert (
        hashlib.sha256(artifact_bytes).hexdigest()
        == EXPECTED_Q25_ARTIFACT_SHA256
    )
    text = artifact_bytes.decode("utf-8")
    assert "max_q=25\n" in text
    assert "status=COMPUTED\n" in text
    assert "pgtq.structured_assignments=2388798\n" in text
    assert "pgtq.z1_structural_assignments=595896\n" in text
    assert "pgtq.static_candidates=105851\n" in text
    assert "pgtq.local_bridge_replays=15881\n" in text
    assert (
        "pgtq.all_proper_periods_below_P_local_replays=15881\n"
        in text
    )
    assert "pgtq.local_endpoint_exact_replays=15881\n" in text
    assert "pgtq.proper_cut_count=127048\n" in text
    assert 'pgtq.local_r_counts={"4":15881}\n' in text
    assert 'pgtq.local_B_counts={"2232":15881}\n' in text
    assert 'pgtq.local_seam_counts={"none":15881}\n' in text
    assert (
        'pgtq.first_failure_phase_counts='
        '{"1":15041,"2":27107,"3":19005,"4":1454,"5":4190,'
        '"6":117,"7":23051,"8":4,"9":1}\n'
        in text
    )
    assert (
        'pgtq.cut_relation_counts='
        '{"first:2:<q":16042,"first:2:=q":31601,'
        '"first:3:<q":15881,"second:2:<r":15881,'
        '"second:2:=r":31762,"second:3:<r":15881}\n'
        in text
    )
    assert (
        'pgtq.period_P_relation_counts='
        '{"first:2:<P":47643,"first:2:=P":0,"first:2:>P":0,'
        '"first:3:<P":15881,"first:3:=P":0,"first:3:>P":0,'
        '"second:2:<P":47643,"second:2:=P":0,"second:2:>P":0,'
        '"second:3:<P":15881,"second:3:=P":0,'
        '"second:3:>P":0}\n'
        in text
    )
    assert (
        'pgtq.second_half_three_seam_cross_counts='
        '{"eq_r:seam_false":0,"eq_r:seam_true":0,'
        '"gt_r:seam_false":0,"gt_r:seam_true":0,'
        '"lt_r:seam_false":15881,"lt_r:seam_true":0}\n'
        in text
    )
    assert (
        'pgtq.theorem_opportunity_counts='
        '{"endpoint_pair":15881,"first_2_cap":47643,'
        '"first_3_bound":15881,"first_3_visibility":15881,'
        '"full_fourth_power":127048,"full_root_seam":0,'
        '"full_root_suffix":0,"full_root_terminal":0,'
        '"second_2_cap":47643,"second_3_bound":15881,'
        '"second_3_visibility":15881,'
        '"visible_fourth_power":127048}\n'
        in text
    )
    assert (
        'pgtq.theorem_violation_counts='
        '{"endpoint_pair":0,"first_2_cap":0,"first_3_bound":0,'
        '"first_3_visibility":0,"full_fourth_power":0,'
        '"full_root_seam":0,"full_root_suffix":0,'
        '"full_root_terminal":0,"second_2_cap":0,'
        '"second_3_bound":0,"second_3_visibility":0,'
        '"visible_fourth_power":0}\n'
        in text
    )

    assert "pltq.structured_assignments=1115405\n" in text
    assert "pltq.z1_structural_assignments=418622\n" in text
    assert "pltq.static_candidates=100053\n" in text
    assert "pltq.local_bridge_replays=93497\n" in text
    assert (
        "pltq.all_proper_periods_below_P_local_replays=93497\n"
        in text
    )
    assert "pltq.local_endpoint_exact_replays=93497\n" in text
    assert "pltq.proper_cut_count=187018\n" in text
    assert 'pltq.local_r_counts={"1":93493,"4":4}\n' in text
    assert 'pltq.local_B_counts={"2":93493,"2223":4}\n' in text
    assert 'pltq.local_seam_counts={"D=JBTheta":93497}\n' in text
    assert (
        'pltq.first_failure_phase_counts='
        '{"1":6343,"2":210,"5":2,"7":1}\n'
        in text
    )
    assert (
        'pltq.cut_relation_counts='
        '{"first:2:<q":4,"first:2:=q":93501,"first:3:<q":4,'
        '"second:2:<r":4,"second:2:=r":93501,'
        '"second:3:<r":4}\n'
        in text
    )
    assert (
        'pltq.period_P_relation_counts='
        '{"first:2:<P":93505,"first:2:=P":0,"first:2:>P":0,'
        '"first:3:<P":4,"first:3:=P":0,"first:3:>P":0,'
        '"second:2:<P":93505,"second:2:=P":0,"second:2:>P":0,'
        '"second:3:<P":4,"second:3:=P":0,"second:3:>P":0}\n'
        in text
    )
    assert (
        'pltq.second_half_three_seam_cross_counts='
        '{"eq_r:seam_false":0,"eq_r:seam_true":0,'
        '"gt_r:seam_false":0,"gt_r:seam_true":0,'
        '"lt_r:seam_false":0,"lt_r:seam_true":4}\n'
        in text
    )
    assert (
        'pltq.theorem_opportunity_counts='
        '{"endpoint_pair":93497,"first_2_cap":93505,'
        '"first_3_bound":4,"first_3_visibility":4,'
        '"full_fourth_power":187018,"full_root_seam":0,'
        '"full_root_suffix":0,"full_root_terminal":0,'
        '"second_2_cap":93505,"second_3_bound":4,'
        '"second_3_visibility":4,'
        '"visible_fourth_power":187018}\n'
        in text
    )
    assert (
        'pltq.theorem_violation_counts='
        '{"endpoint_pair":0,"first_2_cap":0,"first_3_bound":0,'
        '"first_3_visibility":0,"full_fourth_power":0,'
        '"full_root_seam":0,"full_root_suffix":0,'
        '"full_root_terminal":0,"second_2_cap":0,'
        '"second_3_bound":0,"second_3_visibility":0,'
        '"visible_fourth_power":0}\n'
        in text
    )

    assert text.count("full_fourth_power_root_occurrences=0\n") == 2
    assert text.count("full_fourth_power_cut_count=0\n") == 2
    assert (
        text.count("visible_proper_fourth_root_occurrences=0\n")
        == 2
    )
    assert text.count("visible_proper_fourth_cut_count=0\n") == 2
    assert text.count("certificate=") == 6
    assert text.endswith(
        "NOT_A_PROOF: bounded standalone-local D-035 bridge census; "
        "no arbitrary left context was enumerated, and zero violations "
        "prove neither bridge theorem, boundary wall, nor Cell C.\n"
    )
