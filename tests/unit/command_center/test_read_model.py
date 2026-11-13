from __future__ import annotations

import ast
import json
import unittest
from dataclasses import FrozenInstanceError, replace
from datetime import datetime, timezone
from pathlib import Path

import afr.command_center.read_model as rm
from afr.conformance.conformance_summary import (
    ACCEPTED_FINDING_SET_STATUS,
    SCORE_CONTRACT_VERSION,
    SCORE_FORMULA_ID,
    SCORE_FORMULA_VERSION,
    ConformanceScoreSummary,
    project_conformance_summary,
)
from afr.conformance.finding_derivation import (
    FINDING_CONTRACT_VERSION,
    ConformanceFinding,
    FindingState,
    canonical_finding_bytes,
)
from afr.kernel.canonicalization import CANONICALIZATION_VERSION
from afr.kernel.contracts import (
    ContractValidationError,
    Identifier,
    OptionalValue,
    ResourceLimits,
    SemanticVersion,
)
from afr.kernel.fingerprints import (
    FINGERPRINT_VERSION,
    Fingerprint,
    compute_fingerprint,
)


VECTOR = (
    Path(__file__).resolve().parents[2]
    / "vectors"
    / "command_center"
    / "command-center-foundation-v1.json"
)


def limits() -> ResourceLimits:
    return ResourceLimits(
        version=CANONICALIZATION_VERSION,
        maximum_input_bytes=1_000_000,
        maximum_collection_items=10_000,
        maximum_nesting_depth=64,
        maximum_canonical_bytes=1_000_000,
        maximum_work_units=1_000_000,
    )


_FINDINGS_BY_SET_ID: dict[str, tuple[ConformanceFinding, ...]] = {}


def make_finding(
    index: int,
    state: FindingState,
    *,
    tenant: str = "tenant.synthetic",
    subject: str = "subject.synthetic",
    environment: str = "environment.synthetic",
    release: str = "release.synthetic",
    architecture_truth: str = "architecture.synthetic",
) -> ConformanceFinding:
    provisional = ConformanceFinding(
        finding_contract_version=
            FINDING_CONTRACT_VERSION,
        finding_id=
            Identifier(f"finding.synthetic.{index:04d}"),
        finding_state=state,
        tenant_id=Identifier(tenant),
        subject_id=Identifier(subject),
        environment_id=Identifier(environment),
        release_id=Identifier(release),
        architecture_truth_reference_id=
            Identifier(architecture_truth),
        claim_id=
            Identifier(f"claim.synthetic.{index:04d}"),
        source_evaluation_cycle_id=
            Identifier("cycle.synthetic"),
        source_evaluation_result_id=
            Identifier("result.synthetic"),
        evidence_binding_or_set_id=
            Identifier("evidence.synthetic"),
        finding_derivation_policy_id=
            Identifier("policy.synthetic"),
        finding_derivation_policy_version=
            SemanticVersion("1.0.0"),
        evaluator_id=
            Identifier("evaluator.synthetic"),
        evaluator_version=
            SemanticVersion("1.0.0"),
        canonicalization_version=
            CANONICALIZATION_VERSION,
        fingerprint_version=
            FINGERPRINT_VERSION,
        trusted_time_context_id=
            Identifier("trusted-time.synthetic"),
        finding_valid_from=datetime(
            2026,
            11,
            10,
            19,
            0,
            tzinfo=timezone.utc,
        ),
        finding_valid_until=datetime(
            2026,
            11,
            10,
            21,
            0,
            tzinfo=timezone.utc,
        ),
        limitations=(
            Identifier("limitation.synthetic"),
        ),
        unresolved_conditions=(),
        finding_fingerprint=Fingerprint(
            algorithm="sha256",
            fingerprint_version=
                FINGERPRINT_VERSION,
            canonicalization_version=
                CANONICALIZATION_VERSION,
            digest_hex="0" * 64,
        ),
        supersedes_finding_id=
            OptionalValue.missing(),
    )

    fingerprint = compute_fingerprint(
        canonical_finding_bytes(
            provisional,
            limits(),
            input_byte_length=8192,
        ),
        limits(),
        canonicalization_version=
            CANONICALIZATION_VERSION,
        fingerprint_version=
            FINGERPRINT_VERSION,
    )

    return replace(
        provisional,
        finding_fingerprint=fingerprint,
    )


def make_findings(
    *,
    eligible: int = 4,
    supported: int = 4,
    contradicted: int = 0,
    stale: int = 0,
    inconclusive: int = 0,
    evidence_unavailable: int = 0,
    tenant: str = "tenant.synthetic",
    subject: str = "subject.synthetic",
    environment: str = "environment.synthetic",
    release: str = "release.synthetic",
    architecture_truth: str = "architecture.synthetic",
) -> tuple[ConformanceFinding, ...]:
    states = (
        [FindingState.SUPPORTED] * supported
        + [FindingState.CONTRADICTED] * contradicted
        + [FindingState.STALE] * stale
        + [FindingState.INCONCLUSIVE] * inconclusive
        + [FindingState.EVIDENCE_UNAVAILABLE]
          * evidence_unavailable
    )

    if len(states) != eligible:
        raise ValueError(
            "synthetic finding counts must equal eligible"
        )

    return tuple(
        make_finding(
            index,
            state,
            tenant=tenant,
            subject=subject,
            environment=environment,
            release=release,
            architecture_truth=architecture_truth,
        )
        for index, state in enumerate(states, start=1)
    )


def make_summary(
    *,
    eligible: int = 4,
    supported: int = 4,
    contradicted: int = 0,
    stale: int = 0,
    inconclusive: int = 0,
    evidence_unavailable: int = 0,
    tenant: str = "tenant.synthetic",
    subject: str = "subject.synthetic",
    environment: str = "environment.synthetic",
    release: str = "release.synthetic",
    architecture_truth: str = "architecture.synthetic",
) -> ConformanceScoreSummary:
    findings = make_findings(
        eligible=eligible,
        supported=supported,
        contradicted=contradicted,
        stale=stale,
        inconclusive=inconclusive,
        evidence_unavailable=evidence_unavailable,
        tenant=tenant,
        subject=subject,
        environment=environment,
        release=release,
        architecture_truth=architecture_truth,
    )

    summary = project_conformance_summary(
        score_contract_version=
            SCORE_CONTRACT_VERSION,
        finding_set_status=
            ACCEPTED_FINDING_SET_STATUS,
        findings=findings,
        score_formula_id=
            SCORE_FORMULA_ID,
        score_formula_version=
            SCORE_FORMULA_VERSION,
        additional_limitations=(),
        resource_limits=limits(),
        input_byte_length=8192,
    )

    _FINDINGS_BY_SET_ID[
        summary.finding_set_id.value
    ] = findings

    return summary


def binding_for(
    summary: ConformanceScoreSummary,
) -> rm.SourceScopeBinding:
    findings = _FINDINGS_BY_SET_ID[
        summary.finding_set_id.value
    ]

    return rm.build_source_scope_binding(
        summary=summary,
        source_findings=findings,
        resource_limits=limits(),
        input_byte_length=8192,
    )


def project_with_binding(
    summary: ConformanceScoreSummary,
    binding: rm.SourceScopeBinding,
    *,
    freshness: Identifier = rm.FRESHNESS_CURRENT,
    availability: Identifier = rm.AVAILABILITY_AVAILABLE,
    trusted_time: datetime | None = None,
):
    return rm.project_executive_status(
        summary=summary,
        source_scope_binding=binding,
        as_of_trusted_time=(
            trusted_time
            if trusted_time is not None
            else datetime(
                2026,
                11,
                10,
                20,
                0,
                tzinfo=timezone.utc,
            )
        ),
        freshness_state=freshness,
        availability_state=availability,
        warnings=(
            Identifier("warning.synthetic"),
        ),
        resource_limits=limits(),
        input_byte_length=8192,
    )


def project(
    summary: ConformanceScoreSummary | None = None,
    *,
    freshness: Identifier = rm.FRESHNESS_CURRENT,
    availability: Identifier = rm.AVAILABILITY_AVAILABLE,
):
    resolved = summary or make_summary()

    return project_with_binding(
        resolved,
        binding_for(resolved),
        freshness=freshness,
        availability=availability,
    )


class ReadModelTests(unittest.TestCase):
    def test_t01_exact_foundation_envelope(self) -> None:
        model = project()

        self.assertEqual(
            model.read_model_contract_version,
            rm.READ_MODEL_CONTRACT_VERSION,
        )
        self.assertEqual(
            model.surface_id,
            rm.EXECUTIVE_STATUS_SURFACE_ID,
        )
        self.assertEqual(
            model.authority_state,
            rm.EXECUTIVE_STATUS_AUTHORITY_STATE,
        )

    def test_t02_source_identity_and_fingerprint_are_traceable(self) -> None:
        summary = make_summary()
        model = project(summary)

        self.assertEqual(
            model.source_fingerprint,
            summary.score_fingerprint,
        )
        self.assertIn(
            summary.finding_set_id,
            model.source_identity_set,
        )
        self.assertIn(
            Identifier(
                "score-fingerprint:"
                + summary.score_fingerprint.digest_hex
            ),
            model.source_identity_set,
        )

    def test_t03_summary_counts_and_score_are_preserved(self) -> None:
        summary = make_summary(
            eligible=4,
            supported=3,
            contradicted=1,
        )
        model = project(summary)

        self.assertEqual(model.data.eligible_finding_count, 4)
        self.assertEqual(model.data.supported_count, 3)
        self.assertEqual(model.data.contradicted_count, 1)
        self.assertTrue(
            model.data.score_value_or_unavailable.present
        )
        self.assertEqual(
            model.data.score_value_or_unavailable.value,
            7500,
        )

    def test_t04_unresolved_score_remains_unavailable(self) -> None:
        summary = make_summary(
            eligible=2,
            supported=1,
            stale=1,
        )
        model = project(
            summary,
            freshness=rm.FRESHNESS_STALE,
            availability=rm.AVAILABILITY_STALE,
        )

        self.assertFalse(
            model.data.score_value_or_unavailable.present
        )
        self.assertIsNone(
            model.data.score_value_or_unavailable.value
        )

    def test_t05_limitations_and_warnings_are_explicit(self) -> None:
        model = project()

        self.assertEqual(
            model.limitations,
            (Identifier("limitation.synthetic"),),
        )
        self.assertEqual(
            model.warnings,
            (Identifier("warning.synthetic"),),
        )

    def test_t06_canonical_projection_is_reproducible(self) -> None:
        first = project()
        second = project()

        self.assertEqual(
            rm.canonical_read_model_bytes(
                first,
                limits(),
                input_byte_length=8192,
            ),
            rm.canonical_read_model_bytes(
                second,
                limits(),
                input_byte_length=8192,
            ),
        )

    def test_t07_naive_trusted_time_fails_closed(self) -> None:
        summary = make_summary()
        binding = binding_for(summary)

        with self.assertRaises(ContractValidationError):
            project_with_binding(
                summary,
                binding,
                trusted_time=datetime(
                    2026,
                    11,
                    10,
                    20,
                    0,
                ),
            )

    def test_t08_unknown_freshness_identifier_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError):
            project(
                freshness=Identifier("FUTURE"),
            )

    def test_t09_noncurrent_state_cannot_render_available(self) -> None:
        for state in (
            rm.FRESHNESS_STALE,
            rm.FRESHNESS_UNKNOWN,
            rm.FRESHNESS_UNAVAILABLE,
        ):
            with self.subTest(state=state.value):
                with self.assertRaises(ContractValidationError):
                    project(
                        freshness=state,
                        availability=rm.AVAILABILITY_AVAILABLE,
                    )

    def test_t10_tampered_summary_fingerprint_fails_closed(self) -> None:
        summary = replace(
            make_summary(),
            score_fingerprint=Fingerprint(
                algorithm="sha256",
                fingerprint_version=FINGERPRINT_VERSION,
                canonicalization_version=CANONICALIZATION_VERSION,
                digest_hex="f" * 64,
            ),
        )

        with self.assertRaises(ContractValidationError):
            project(summary)

    def test_t11_count_mismatch_fails_closed(self) -> None:
        summary = replace(
            make_summary(),
            eligible_finding_count=99,
        )

        with self.assertRaises(ContractValidationError):
            project(summary)

    def test_t12_read_model_is_immutable(self) -> None:
        model = project()

        with self.assertRaises(FrozenInstanceError):
            model.surface_id = Identifier("live_findings")

    def test_t13_no_external_side_effect_primitives(self) -> None:
        source = Path(rm.__file__).read_text(encoding="utf-8")
        tree = ast.parse(source)

        imported_roots: set[str] = set()
        direct_calls: set[str] = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(
                    alias.name.split(".", 1)[0]
                    for alias in node.names
                )
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(
                    node.module.split(".", 1)[0]
                )
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
            ):
                direct_calls.add(node.func.id)

        self.assertLessEqual(
            imported_roots,
            {
                "__future__",
                "dataclasses",
                "datetime",
                "typing",
                "afr",
            },
        )
        self.assertTrue(
            {
                "open",
                "exec",
                "eval",
                "print",
                "system",
            }.isdisjoint(direct_calls)
        )

    def test_t14_vector_replay(self) -> None:
        data = json.loads(
            VECTOR.read_text(encoding="utf-8")
        )

        self.assertEqual(
            data["foundation_surface_id"],
            "executive_status",
        )

        for case in data["executive_cases"]:
            summary = make_summary(
                eligible=int(case["eligible"]),
                supported=int(case["supported"]),
                contradicted=int(case["contradicted"]),
                stale=int(case["stale"]),
                inconclusive=int(case["inconclusive"]),
                evidence_unavailable=int(
                    case["evidence_unavailable"]
                ),
            )

            unresolved = (
                summary.stale_count
                + summary.inconclusive_count
                + summary.evidence_unavailable_count
            ) > 0

            model = project(
                summary,
                freshness=(
                    rm.FRESHNESS_STALE
                    if unresolved
                    else rm.FRESHNESS_CURRENT
                ),
                availability=(
                    rm.AVAILABILITY_STALE
                    if unresolved
                    else rm.AVAILABILITY_AVAILABLE
                ),
            )

            with self.subTest(case=case["id"]):
                self.assertEqual(
                    model.data.score_value_or_unavailable.present,
                    bool(case["score_present"]),
                )
                self.assertEqual(
                    model.data.score_value_or_unavailable.value,
                    case["score_basis_points"],
                )

    def test_t15_tenant_relabel_fails_closed(self) -> None:
        summary = make_summary()
        binding = binding_for(summary)

        forged = replace(
            binding,
            tenant_id=Identifier("tenant.other"),
        )

        with self.assertRaises(ContractValidationError):
            project_with_binding(
                summary,
                forged,
            )

    def test_t16_subject_relabel_fails_closed(self) -> None:
        summary = make_summary()
        binding = binding_for(summary)

        forged = replace(
            binding,
            subject_id_or_scope=
                Identifier("subject.other"),
        )

        with self.assertRaises(ContractValidationError):
            project_with_binding(
                summary,
                forged,
            )

    def test_t17_system_scope_relabel_fails_closed(self) -> None:
        summary = make_summary()
        binding = binding_for(summary)

        forged = replace(
            binding,
            workspace_or_system_scope=
                Identifier("system.other"),
        )

        with self.assertRaises(ContractValidationError):
            project_with_binding(
                summary,
                forged,
            )

    def test_t18_different_scope_findings_fail_closed(self) -> None:
        summary = make_summary()
        binding = binding_for(summary)

        other = make_summary(
            tenant="tenant.other",
        )

        other_findings = _FINDINGS_BY_SET_ID[
            other.finding_set_id.value
        ]

        forged = replace(
            binding,
            source_findings=other_findings,
        )

        with self.assertRaises(ContractValidationError):
            project_with_binding(
                summary,
                forged,
            )

    def test_t19_binding_fingerprint_tamper_fails_closed(self) -> None:
        summary = make_summary()
        binding = binding_for(summary)

        forged = replace(
            binding,
            binding_fingerprint=Fingerprint(
                algorithm="sha256",
                fingerprint_version=
                    FINGERPRINT_VERSION,
                canonicalization_version=
                    CANONICALIZATION_VERSION,
                digest_hex="f" * 64,
            ),
        )

        with self.assertRaises(ContractValidationError):
            project_with_binding(
                summary,
                forged,
            )


if __name__ == "__main__":
    unittest.main()
