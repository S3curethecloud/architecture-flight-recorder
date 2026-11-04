from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
from datetime import datetime, timezone
import json
from pathlib import Path
import unittest

import afr.conformance.conformance_summary as cs
import afr.conformance.drift_evaluation as de
import afr.conformance.evidence_foundation as ef
import afr.conformance.finding_derivation as fd
from afr.kernel.canonicalization import CANONICALIZATION_VERSION
from afr.kernel.contracts import (
    ContractValidationError,
    EnvironmentBinding,
    EvaluationBinding,
    Identifier,
    OptionalValue,
    ProcessingFailureCode,
    ProvenanceBinding,
    ReleaseBinding,
    ResourceLimits,
    SemanticVersion,
    SubjectBinding,
    TenantBinding,
    TimeBinding,
)
from afr.kernel.fingerprints import FINGERPRINT_VERSION, compute_fingerprint


UTC = timezone.utc
VECTOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "vectors/conformance/conformance-summary-v1.json"
)


def aware(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def limits() -> ResourceLimits:
    return ResourceLimits(
        version=CANONICALIZATION_VERSION,
        maximum_input_bytes=65536,
        maximum_collection_items=2048,
        maximum_nesting_depth=32,
        maximum_canonical_bytes=65536,
        maximum_work_units=262144,
    )


def evaluation(
    *,
    tenant: str,
    subject: str,
    environment: str,
    release: str,
) -> EvaluationBinding:
    return EvaluationBinding(
        invocation_id=Identifier(f"invocation.{tenant}.{subject}"),
        tenant=TenantBinding(Identifier(tenant)),
        subject=SubjectBinding(
            Identifier(subject),
            Identifier("architecture"),
        ),
        environment=EnvironmentBinding(Identifier(environment)),
        release=ReleaseBinding(Identifier(release)),
        time=TimeBinding(
            evaluated_at=aware("2026-10-27T20:00:00Z"),
            valid_from=aware("2026-10-27T20:00:00Z"),
            valid_until=aware("2026-10-29T20:00:00Z"),
        ),
        contract_version=SemanticVersion("1.0.0"),
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )


def provenance(*, tenant: str, subject: str) -> ProvenanceBinding:
    return ProvenanceBinding(
        source_id=Identifier(f"source.{tenant}.{subject}"),
        collector_id=Identifier("collector.synthetic"),
        observed_at=aware("2026-10-27T19:59:00Z"),
        integrity_reference=OptionalValue.of(
            Identifier(f"sha256.synthetic.{tenant}.{subject}")
        ),
    )


def foundation(
    *,
    tenant: str = "tenant.synthetic",
    subject: str = "subject.synthetic.001",
    environment: str = "env.synthetic",
    release: str = "release.synthetic.001",
    truth: str = "truth.phase12.synthetic.001",
) -> ef.EvidenceFoundationBinding:
    return ef.build_evidence_foundation(
        foundation_contract_version=ef.FOUNDATION_CONTRACT_VERSION,
        source_evaluation_cycle_id=Identifier(
            f"cycle.{tenant}.{subject}"
        ),
        source_evaluation_result_id=Identifier(
            f"result.{tenant}.{subject}"
        ),
        source_evaluation_status=ef.ACCEPTED_SOURCE_EVALUATION_STATUS,
        tenant_id=Identifier(tenant),
        subject_id=Identifier(subject),
        architecture_truth_reference_id=Identifier(truth),
        evidence_binding_or_set_id=Identifier(
            f"evidence.set.{tenant}.{subject}"
        ),
        trusted_time_context_id=Identifier("time.synthetic.001"),
        evaluation_binding=evaluation(
            tenant=tenant,
            subject=subject,
            environment=environment,
            release=release,
        ),
        provenance=provenance(tenant=tenant, subject=subject),
        limitations=(Identifier("limitation.synthetic-only"),),
        unresolved_conditions=(
            Identifier("condition.external-issuance-not-authorized"),
        ),
        resource_limits=limits(),
        input_byte_length=2048,
    )


def drift_for_state(
    fnd: ef.EvidenceFoundationBinding,
    state: str,
) -> de.DriftEvaluationResult:
    evidence_available = state != "EVIDENCE_UNAVAILABLE"
    evidence_conclusive = state not in {
        "INCONCLUSIVE",
        "EVIDENCE_UNAVAILABLE",
    }
    evidence_value: str | None = "expected.synthetic.v1"
    evidence_observed_at: datetime | None = aware(
        "2026-10-28T19:59:00Z"
    )
    freshness_bound_seconds = 3600
    if state == "CONTRADICTED":
        evidence_value = "different.synthetic.v1"
    elif state == "STALE":
        evidence_observed_at = aware("2026-10-28T17:00:00Z")
    elif state == "EVIDENCE_UNAVAILABLE":
        evidence_value = None
        evidence_observed_at = None

    return de.evaluate_drift(
        drift_contract_version=de.DRIFT_EVALUATION_CONTRACT_VERSION,
        foundation=fnd,
        expected_value="expected.synthetic.v1",
        evidence_available=evidence_available,
        evidence_conclusive=evidence_conclusive,
        evidence_value=evidence_value,
        evidence_observed_at=evidence_observed_at,
        trusted_evaluation_time=aware("2026-10-28T20:00:00Z"),
        freshness_bound_seconds=freshness_bound_seconds,
        evidence_references=(
            Identifier("evidence.ref.synthetic.b"),
            Identifier("evidence.ref.synthetic.a"),
        ),
        resource_limits=limits(),
        input_byte_length=2048,
    )


def make_finding(
    *,
    state: str = "SUPPORTED",
    ordinal: int = 1,
    tenant: str = "tenant.synthetic",
    subject: str = "subject.synthetic.001",
    environment: str = "env.synthetic",
    release: str = "release.synthetic.001",
    truth: str = "truth.phase12.synthetic.001",
    claim: str | None = None,
    policy_version: str = "1.0.0",
) -> fd.ConformanceFinding:
    fnd = foundation(
        tenant=tenant,
        subject=subject,
        environment=environment,
        release=release,
        truth=truth,
    )
    drift = drift_for_state(fnd, state)
    return fd.derive_finding(
        finding_contract_version=fd.FINDING_CONTRACT_VERSION,
        s2_result_status=fd.ACCEPTED_S2_RESULT_STATUS,
        foundation=fnd,
        drift_result=drift,
        finding_id=Identifier(f"finding.synthetic.{ordinal:03d}"),
        tenant_id=fnd.tenant_id,
        subject_id=fnd.subject_id,
        environment_id=fnd.environment_id,
        release_id=fnd.release_id,
        claim_id=Identifier(claim or f"claim.synthetic.{ordinal:03d}"),
        finding_derivation_policy_id=Identifier("policy.finding.synthetic"),
        finding_derivation_policy_version=SemanticVersion(policy_version),
        evaluator_id=Identifier("evaluator.finding.synthetic"),
        evaluator_version=SemanticVersion("1.0.0"),
        finding_valid_from=aware("2026-10-28T20:00:00Z"),
        finding_valid_until=aware("2026-10-29T19:00:00Z"),
        limitations=(
            Identifier(f"limitation.finding.{ordinal:03d}"),
            Identifier("limitation.synthetic-only"),
        ),
        unresolved_conditions=(
            Identifier(f"condition.finding.{ordinal:03d}"),
            Identifier("condition.external-issuance-not-authorized"),
        ),
        supersedes_finding_id=OptionalValue.missing(),
        resource_limits=limits(),
        input_byte_length=4096,
    )


def summary_args(
    findings: tuple[fd.ConformanceFinding, ...],
) -> dict[str, object]:
    return {
        "score_contract_version": cs.SCORE_CONTRACT_VERSION,
        "finding_set_status": cs.ACCEPTED_FINDING_SET_STATUS,
        "findings": findings,
        "score_formula_id": cs.SCORE_FORMULA_ID,
        "score_formula_version": cs.SCORE_FORMULA_VERSION,
        "additional_limitations": (
            Identifier("limitation.summary.synthetic"),
        ),
        "resource_limits": limits(),
        "input_byte_length": 8192,
    }


def project(
    findings: tuple[fd.ConformanceFinding, ...] | None = None,
    **overrides: object,
) -> cs.ConformanceScoreSummary:
    actual_findings = findings or (make_finding(),)
    args = summary_args(actual_findings)
    args.update(overrides)
    return cs.project_conformance_summary(**args)


def vector_cases() -> list[dict[str, object]]:
    data = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
    return list(data["cases"])


class ConformanceSummaryTests(unittest.TestCase):
    def test_t01_accepted_finding_set_required(self) -> None:
        args = summary_args((make_finding(),))
        args["finding_set_status"] = Identifier("REJECTED")
        with self.assertRaises(ContractValidationError):
            cs.project_conformance_summary(**args)
        args = summary_args((make_finding(),))
        args["findings"] = ()
        with self.assertRaises(ContractValidationError):
            cs.project_conformance_summary(**args)

    def test_t02_exact_14_field_score_representation(self) -> None:
        summary = project()
        self.assertEqual(summary.score_contract_version, cs.SCORE_CONTRACT_VERSION)
        self.assertEqual(
            [item.name for item in fields(cs.ConformanceScoreSummary)],
            [
                "score_contract_version",
                "score_formula_id",
                "score_formula_version",
                "finding_set_id",
                "eligible_finding_count",
                "supported_count",
                "contradicted_count",
                "stale_count",
                "inconclusive_count",
                "evidence_unavailable_count",
                "excluded_count",
                "score_value_or_unavailable",
                "score_fingerprint",
                "limitations",
            ],
        )

    def test_t03_formula_id_and_version_bound(self) -> None:
        with self.assertRaises(ContractValidationError):
            project(score_formula_id=Identifier("afr.score.other"))
        with self.assertRaises(ContractValidationError):
            project(score_formula_version=SemanticVersion("1.0.1"))

    def test_t04_finding_set_identity_deterministic(self) -> None:
        first = make_finding(ordinal=1)
        second = make_finding(state="CONTRADICTED", ordinal=2)
        forward = project((first, second))
        reverse = project((second, first))
        self.assertEqual(forward.finding_set_id, reverse.finding_set_id)
        self.assertTrue(forward.finding_set_id.value.startswith("finding-set."))

    def test_t05_five_state_counts_exact(self) -> None:
        states = (
            "SUPPORTED",
            "CONTRADICTED",
            "STALE",
            "INCONCLUSIVE",
            "EVIDENCE_UNAVAILABLE",
        )
        findings = tuple(
            make_finding(state=state, ordinal=index + 1)
            for index, state in enumerate(states)
        )
        summary = project(findings)
        self.assertEqual(summary.eligible_finding_count, 5)
        self.assertEqual(summary.supported_count, 1)
        self.assertEqual(summary.contradicted_count, 1)
        self.assertEqual(summary.stale_count, 1)
        self.assertEqual(summary.inconclusive_count, 1)
        self.assertEqual(summary.evidence_unavailable_count, 1)

    def test_t06_denominator_and_exclusions_explicit(self) -> None:
        findings = (
            make_finding(ordinal=1),
            make_finding(state="CONTRADICTED", ordinal=2),
            make_finding(ordinal=3),
        )
        summary = project(findings)
        self.assertEqual(summary.eligible_finding_count, 3)
        self.assertEqual(summary.excluded_count, 0)
        self.assertEqual(
            summary.supported_count
            + summary.contradicted_count
            + summary.stale_count
            + summary.inconclusive_count
            + summary.evidence_unavailable_count,
            summary.eligible_finding_count,
        )
        for finding in findings:
            for limitation in finding.limitations:
                self.assertIn(limitation, summary.limitations)
        self.assertIn(
            Identifier("limitation.summary.synthetic"),
            summary.limitations,
        )

    def test_t07_unresolved_mandatory_state_makes_score_unavailable(self) -> None:
        for state in ("STALE", "INCONCLUSIVE", "EVIDENCE_UNAVAILABLE"):
            with self.subTest(state=state):
                summary = project((make_finding(state=state),))
                self.assertFalse(summary.score_value_or_unavailable.present)
                self.assertIsNone(summary.score_value_or_unavailable.value)

    def test_t08_stale_not_hidden_as_success(self) -> None:
        summary = project((make_finding(state="STALE"),))
        self.assertEqual(summary.stale_count, 1)
        self.assertEqual(summary.supported_count, 0)
        self.assertFalse(summary.score_value_or_unavailable.present)

    def test_t09_inconclusive_not_hidden_as_success(self) -> None:
        summary = project((make_finding(state="INCONCLUSIVE"),))
        self.assertEqual(summary.inconclusive_count, 1)
        self.assertEqual(summary.supported_count, 0)
        self.assertFalse(summary.score_value_or_unavailable.present)

    def test_t10_evidence_unavailable_not_hidden_as_success(self) -> None:
        summary = project((make_finding(state="EVIDENCE_UNAVAILABLE"),))
        self.assertEqual(summary.evidence_unavailable_count, 1)
        self.assertEqual(summary.supported_count, 0)
        self.assertFalse(summary.score_value_or_unavailable.present)

    def test_t11_contradicted_not_counted_as_supported(self) -> None:
        summary = project(
            (
                make_finding(ordinal=1),
                make_finding(state="CONTRADICTED", ordinal=2),
            )
        )
        self.assertEqual(summary.supported_count, 1)
        self.assertEqual(summary.contradicted_count, 1)
        self.assertTrue(summary.score_value_or_unavailable.present)
        self.assertEqual(summary.score_value_or_unavailable.value, 5000)

    def test_t12_cross_tenant_aggregation_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            project(
                (
                    make_finding(ordinal=1),
                    make_finding(ordinal=2, tenant="tenant.other"),
                )
            )
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.TENANT_BINDING_MISMATCH,
        )

    def test_t13_cross_subject_aggregation_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            project(
                (
                    make_finding(ordinal=1),
                    make_finding(ordinal=2, subject="subject.other"),
                )
            )
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.SUBJECT_BINDING_MISMATCH,
        )

    def test_t14_incompatible_environment_release_or_claimset_fails_closed(self) -> None:
        base = make_finding(ordinal=1)
        cases = (
            make_finding(ordinal=2, environment="env.other"),
            make_finding(ordinal=2, release="release.other"),
            make_finding(ordinal=2, policy_version="1.0.1"),
            make_finding(ordinal=2, claim="claim.synthetic.001"),
        )
        for other in cases:
            with self.subTest(other=other.finding_id.value):
                with self.assertRaises(ContractValidationError):
                    project((base, other))

    def test_t15_score_fingerprint_reproducible(self) -> None:
        summary = project(
            (
                make_finding(ordinal=1),
                make_finding(state="CONTRADICTED", ordinal=2),
            )
        )
        canonical_bytes = cs.canonical_score_summary_bytes(
            summary,
            limits(),
            input_byte_length=8192,
        )
        self.assertEqual(
            compute_fingerprint(
                canonical_bytes,
                limits(),
                canonicalization_version=CANONICALIZATION_VERSION,
                fingerprint_version=FINGERPRINT_VERSION,
            ),
            summary.score_fingerprint,
        )

    def test_t16_equivalent_input_order_reproduces_identical_summary(self) -> None:
        first = make_finding(ordinal=1)
        second = make_finding(state="CONTRADICTED", ordinal=2)
        self.assertEqual(project((first, second)), project((second, first)))

    def test_t17_score_cannot_become_architecture_truth_or_replace_findings(self) -> None:
        summary = project()
        self.assertNotIn(
            "architecture_truth_reference_id",
            [item.name for item in fields(cs.ConformanceScoreSummary)],
        )
        self.assertNotIn(
            "finding_state",
            [item.name for item in fields(cs.ConformanceScoreSummary)],
        )
        with self.assertRaises(FrozenInstanceError):
            summary.supported_count = 99
        self.assertFalse(hasattr(cs, "approve_architecture"))
        self.assertFalse(hasattr(cs, "mutate_finding"))

    def test_t18_no_external_side_effects_and_vector_replay(self) -> None:
        source_path = Path(cs.__file__).resolve()
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        imported_roots: set[str] = set()
        direct_calls: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(
                    alias.name.split(".", 1)[0] for alias in node.names
                )
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".", 1)[0])
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                direct_calls.add(node.func.id)
        self.assertLessEqual(
            imported_roots,
            {"__future__", "dataclasses", "afr"},
        )
        self.assertTrue(
            {"open", "exec", "eval", "print"}.isdisjoint(direct_calls)
        )

        cases = vector_cases()
        self.assertEqual(len(cases), 5)
        for case in cases:
            findings = tuple(
                make_finding(state=str(state), ordinal=index + 1)
                for index, state in enumerate(case["finding_states"])
            )
            summary = project(findings)
            with self.subTest(case=case["id"]):
                self.assertEqual(
                    summary.supported_count,
                    int(case["supported_count"]),
                )
                self.assertEqual(
                    summary.contradicted_count,
                    int(case["contradicted_count"]),
                )
                if bool(case["score_available"]):
                    self.assertTrue(summary.score_value_or_unavailable.present)
                    self.assertEqual(
                        summary.score_value_or_unavailable.value,
                        int(case["score_basis_points"]),
                    )
                else:
                    self.assertFalse(summary.score_value_or_unavailable.present)


if __name__ == "__main__":
    unittest.main()
