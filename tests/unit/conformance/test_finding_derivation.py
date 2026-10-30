from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
from datetime import datetime, timezone
import json
from pathlib import Path
import unittest

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
    / "vectors/conformance/finding-derivation-v1.json"
)


def aware(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def limits() -> ResourceLimits:
    return ResourceLimits(
        version=CANONICALIZATION_VERSION,
        maximum_input_bytes=32768,
        maximum_collection_items=1024,
        maximum_nesting_depth=32,
        maximum_canonical_bytes=32768,
        maximum_work_units=131072,
    )


def evaluation() -> EvaluationBinding:
    return EvaluationBinding(
        invocation_id=Identifier("invocation.synthetic.s3.001"),
        tenant=TenantBinding(Identifier("tenant.synthetic")),
        subject=SubjectBinding(
            Identifier("subject.synthetic.001"),
            Identifier("architecture"),
        ),
        environment=EnvironmentBinding(
            Identifier("env.synthetic")
        ),
        release=ReleaseBinding(
            Identifier("release.synthetic.001")
        ),
        time=TimeBinding(
            evaluated_at=aware("2026-10-27T20:00:00Z"),
            valid_from=aware("2026-10-27T20:00:00Z"),
            valid_until=aware("2026-10-29T20:00:00Z"),
        ),
        contract_version=SemanticVersion("1.0.0"),
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )


def provenance() -> ProvenanceBinding:
    return ProvenanceBinding(
        source_id=Identifier("source.synthetic"),
        collector_id=Identifier("collector.synthetic"),
        observed_at=aware("2026-10-27T19:59:00Z"),
        integrity_reference=OptionalValue.of(
            Identifier("sha256.synthetic.integrity.001")
        ),
    )


def foundation() -> ef.EvidenceFoundationBinding:
    return ef.build_evidence_foundation(
        foundation_contract_version=
            ef.FOUNDATION_CONTRACT_VERSION,
        source_evaluation_cycle_id=
            Identifier("cycle.synthetic.001"),
        source_evaluation_result_id=
            Identifier("result.synthetic.001"),
        source_evaluation_status=
            ef.ACCEPTED_SOURCE_EVALUATION_STATUS,
        tenant_id=Identifier("tenant.synthetic"),
        subject_id=Identifier("subject.synthetic.001"),
        architecture_truth_reference_id=
            Identifier("truth.phase12.synthetic.001"),
        evidence_binding_or_set_id=
            Identifier("evidence.synthetic.set.001"),
        trusted_time_context_id=
            Identifier("time.synthetic.001"),
        evaluation_binding=evaluation(),
        provenance=provenance(),
        limitations=(
            Identifier("limitation.synthetic-only"),
        ),
        unresolved_conditions=(
            Identifier(
                "condition.external-issuance-not-authorized"
            ),
        ),
        resource_limits=limits(),
        input_byte_length=1024,
    )


def vector_cases() -> list[dict[str, object]]:
    data = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
    return list(data["cases"])


def vector_case(state: str) -> dict[str, object]:
    for item in vector_cases():
        if item["expected_state"] == state:
            return item
    raise AssertionError(f"missing vector state: {state}")


def drift_for_state(
    fnd: ef.EvidenceFoundationBinding,
    state: str,
) -> de.DriftEvaluationResult:
    case = vector_case(state)
    observed_text = case["evidence_observed_at"]
    observed = (
        None
        if observed_text is None
        else aware(str(observed_text))
    )
    return de.evaluate_drift(
        drift_contract_version=
            de.DRIFT_EVALUATION_CONTRACT_VERSION,
        foundation=fnd,
        expected_value="expected.synthetic.v1",
        evidence_available=bool(case["evidence_available"]),
        evidence_conclusive=bool(case["evidence_conclusive"]),
        evidence_value=case["evidence_value"],
        evidence_observed_at=observed,
        trusted_evaluation_time=
            aware("2026-10-28T20:00:00Z"),
        freshness_bound_seconds=int(
            case["freshness_bound_seconds"]
        ),
        evidence_references=(
            Identifier("evidence.ref.synthetic.b"),
            Identifier("evidence.ref.synthetic.a"),
        ),
        resource_limits=limits(),
        input_byte_length=2048,
    )


def finding_args(
    fnd: ef.EvidenceFoundationBinding,
    drift: de.DriftEvaluationResult,
) -> dict[str, object]:
    return {
        "finding_contract_version": fd.FINDING_CONTRACT_VERSION,
        "s2_result_status": fd.ACCEPTED_S2_RESULT_STATUS,
        "foundation": fnd,
        "drift_result": drift,
        "finding_id": Identifier("finding.synthetic.001"),
        "tenant_id": fnd.tenant_id,
        "subject_id": fnd.subject_id,
        "environment_id": fnd.environment_id,
        "release_id": fnd.release_id,
        "claim_id": Identifier("claim.synthetic.001"),
        "finding_derivation_policy_id":
            Identifier("policy.finding.synthetic"),
        "finding_derivation_policy_version":
            SemanticVersion("1.0.0"),
        "evaluator_id": Identifier("evaluator.finding.synthetic"),
        "evaluator_version": SemanticVersion("1.0.0"),
        "finding_valid_from": aware("2026-10-28T20:00:00Z"),
        "finding_valid_until": aware("2026-10-29T19:00:00Z"),
        "limitations": (
            Identifier("limitation.finding.synthetic"),
            Identifier("limitation.synthetic-only"),
        ),
        "unresolved_conditions": (
            Identifier("condition.finding.synthetic"),
            Identifier(
                "condition.external-issuance-not-authorized"
            ),
        ),
        "supersedes_finding_id": OptionalValue.missing(),
        "resource_limits": limits(),
        "input_byte_length": 4096,
    }


def run_finding(
    state: str = "SUPPORTED",
    **overrides: object,
) -> fd.ConformanceFinding:
    fnd = foundation()
    drift = drift_for_state(fnd, state)
    args = finding_args(fnd, drift)
    args.update(overrides)
    return fd.derive_finding(**args)


class FindingDerivationTests(unittest.TestCase):
    def test_t01_accepted_s2_result_required(self) -> None:
        fnd = foundation()
        drift = drift_for_state(fnd, "SUPPORTED")
        args = finding_args(fnd, drift)
        args["s2_result_status"] = Identifier("REJECTED")
        with self.assertRaises(ContractValidationError) as ctx:
            fd.derive_finding(**args)
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_IDENTIFIER,
        )

    def test_t02_supported_state_preserved(self) -> None:
        self.assertEqual(
            run_finding("SUPPORTED").finding_state,
            fd.FindingState.SUPPORTED,
        )

    def test_t03_contradicted_state_preserved(self) -> None:
        self.assertEqual(
            run_finding("CONTRADICTED").finding_state,
            fd.FindingState.CONTRADICTED,
        )

    def test_t04_stale_state_preserved(self) -> None:
        self.assertEqual(
            run_finding("STALE").finding_state,
            fd.FindingState.STALE,
        )

    def test_t05_inconclusive_state_preserved(self) -> None:
        self.assertEqual(
            run_finding("INCONCLUSIVE").finding_state,
            fd.FindingState.INCONCLUSIVE,
        )

    def test_t06_evidence_unavailable_state_preserved(self) -> None:
        self.assertEqual(
            run_finding("EVIDENCE_UNAVAILABLE").finding_state,
            fd.FindingState.EVIDENCE_UNAVAILABLE,
        )

    def test_t07_exact_five_state_vocabulary(self) -> None:
        self.assertEqual(
            {item.value for item in fd.FindingState},
            {
                "SUPPORTED",
                "CONTRADICTED",
                "STALE",
                "INCONCLUSIVE",
                "EVIDENCE_UNAVAILABLE",
            },
        )

    def test_t08_tenant_and_subject_scope_bound(self) -> None:
        finding = run_finding()
        self.assertEqual(finding.tenant_id, Identifier("tenant.synthetic"))
        self.assertEqual(
            finding.subject_id,
            Identifier("subject.synthetic.001"),
        )

    def test_t09_environment_and_release_scope_bound(self) -> None:
        finding = run_finding()
        self.assertEqual(
            finding.environment_id,
            Identifier("env.synthetic"),
        )
        self.assertEqual(
            finding.release_id,
            Identifier("release.synthetic.001"),
        )

    def test_t10_truth_claim_evaluation_and_evidence_bound(self) -> None:
        finding = run_finding()
        self.assertEqual(
            finding.architecture_truth_reference_id,
            Identifier("truth.phase12.synthetic.001"),
        )
        self.assertEqual(
            finding.claim_id,
            Identifier("claim.synthetic.001"),
        )
        self.assertEqual(
            finding.source_evaluation_cycle_id,
            Identifier("cycle.synthetic.001"),
        )
        self.assertEqual(
            finding.source_evaluation_result_id,
            Identifier("result.synthetic.001"),
        )
        self.assertEqual(
            finding.evidence_binding_or_set_id,
            Identifier("evidence.synthetic.set.001"),
        )

    def test_t11_policy_and_evaluator_version_identities_bound(self) -> None:
        finding = run_finding()
        self.assertEqual(
            finding.finding_derivation_policy_id,
            Identifier("policy.finding.synthetic"),
        )
        self.assertEqual(
            finding.finding_derivation_policy_version,
            SemanticVersion("1.0.0"),
        )
        self.assertEqual(
            finding.evaluator_id,
            Identifier("evaluator.finding.synthetic"),
        )
        self.assertEqual(
            finding.evaluator_version,
            SemanticVersion("1.0.0"),
        )

    def test_t12_trusted_time_and_validity_interval_bound(self) -> None:
        finding = run_finding()
        self.assertEqual(
            finding.trusted_time_context_id,
            Identifier("time.synthetic.001"),
        )
        self.assertEqual(
            finding.finding_valid_from,
            aware("2026-10-28T20:00:00Z"),
        )
        self.assertEqual(
            finding.finding_valid_until,
            aware("2026-10-29T19:00:00Z"),
        )

    def test_t13_limitations_and_unresolved_conditions_preserved(self) -> None:
        finding = run_finding()
        self.assertIn(
            Identifier("limitation.synthetic-only"),
            finding.limitations,
        )
        self.assertIn(
            Identifier("condition.external-issuance-not-authorized"),
            finding.unresolved_conditions,
        )
        self.assertEqual(
            finding.limitations,
            tuple(sorted(finding.limitations, key=lambda item: item.value)),
        )
        self.assertEqual(
            finding.unresolved_conditions,
            tuple(
                sorted(
                    finding.unresolved_conditions,
                    key=lambda item: item.value,
                )
            ),
        )

    def test_t14_canonical_bytes_and_fingerprint_deterministic(self) -> None:
        first = run_finding()
        second = run_finding()
        first_bytes = fd.canonical_finding_bytes(
            first,
            limits(),
            input_byte_length=4096,
        )
        second_bytes = fd.canonical_finding_bytes(
            second,
            limits(),
            input_byte_length=4096,
        )
        self.assertEqual(first, second)
        self.assertEqual(first_bytes, second_bytes)
        self.assertEqual(
            compute_fingerprint(
                first_bytes,
                limits(),
                canonicalization_version=CANONICALIZATION_VERSION,
                fingerprint_version=FINGERPRINT_VERSION,
            ),
            first.finding_fingerprint,
        )
        self.assertEqual(
            [item.name for item in fields(fd.ConformanceFinding)],
            [
                "finding_contract_version",
                "finding_id",
                "finding_state",
                "tenant_id",
                "subject_id",
                "environment_id",
                "release_id",
                "architecture_truth_reference_id",
                "claim_id",
                "source_evaluation_cycle_id",
                "source_evaluation_result_id",
                "evidence_binding_or_set_id",
                "finding_derivation_policy_id",
                "finding_derivation_policy_version",
                "evaluator_id",
                "evaluator_version",
                "canonicalization_version",
                "fingerprint_version",
                "trusted_time_context_id",
                "finding_valid_from",
                "finding_valid_until",
                "limitations",
                "unresolved_conditions",
                "finding_fingerprint",
                "supersedes_finding_id",
            ],
        )

    def test_t15_accepted_finding_is_immutable(self) -> None:
        finding = run_finding()
        with self.assertRaises(FrozenInstanceError):
            finding.finding_id = Identifier("finding.mutated")

    def test_t16_supersession_creates_distinct_later_finding(self) -> None:
        prior = run_finding()
        later = run_finding(
            finding_id=Identifier("finding.synthetic.002"),
            finding_derivation_policy_version=SemanticVersion("1.0.1"),
            supersedes_finding_id=OptionalValue.of(prior.finding_id),
        )
        self.assertEqual(
            later.supersedes_finding_id.value,
            prior.finding_id,
        )
        self.assertNotEqual(later.finding_id, prior.finding_id)
        self.assertNotEqual(
            later.finding_fingerprint,
            prior.finding_fingerprint,
        )

    def test_t17_cross_scope_mismatch_fails_closed(self) -> None:
        cases = (
            (
                "tenant_id",
                Identifier("tenant.other"),
                ProcessingFailureCode.TENANT_BINDING_MISMATCH,
            ),
            (
                "subject_id",
                Identifier("subject.other"),
                ProcessingFailureCode.SUBJECT_BINDING_MISMATCH,
            ),
            (
                "environment_id",
                Identifier("env.other"),
                ProcessingFailureCode.INVALID_IDENTIFIER,
            ),
            (
                "release_id",
                Identifier("release.other"),
                ProcessingFailureCode.INVALID_IDENTIFIER,
            ),
        )
        for field_name, value, expected_code in cases:
            with self.subTest(field_name=field_name):
                with self.assertRaises(ContractValidationError) as ctx:
                    run_finding(**{field_name: value})
                self.assertEqual(ctx.exception.failure.code, expected_code)

    def test_t18_no_external_side_effects_and_vector_replay(self) -> None:
        source_path = Path(fd.__file__).resolve()
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
            {"__future__", "dataclasses", "datetime", "enum", "afr"},
        )
        self.assertTrue(
            {"open", "exec", "eval", "print"}.isdisjoint(direct_calls)
        )
        self.assertEqual(len(vector_cases()), 5)

        for case in vector_cases():
            state = str(case["expected_state"])
            with self.subTest(state=state):
                finding = run_finding(state)
                self.assertEqual(finding.finding_state.value, state)


if __name__ == "__main__":
    unittest.main()
