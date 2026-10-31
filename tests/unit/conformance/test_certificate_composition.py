from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
from datetime import datetime, timezone
import json
from pathlib import Path
import unittest

import afr.conformance.certificate_composition as cc
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
    / "vectors/conformance/certificate-composition-v1.json"
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
    policy_version: str = "1.0.0",
    supersedes: Identifier | None = None,
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
        claim_id=Identifier(f"claim.synthetic.{ordinal:03d}"),
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
        supersedes_finding_id=(
            OptionalValue.missing()
            if supersedes is None
            else OptionalValue.of(supersedes)
        ),
        resource_limits=limits(),
        input_byte_length=4096,
    )


def compose_args(
    findings: tuple[fd.ConformanceFinding, ...],
) -> dict[str, object]:
    return {
        "certificate_contract_version": cc.CERTIFICATE_CONTRACT_VERSION,
        "finding_set_status": cc.ACCEPTED_S3_FINDING_SET_STATUS,
        "findings": findings,
        "scope_id": Identifier("scope.synthetic.001"),
        "accepted_scope_id": Identifier("scope.synthetic.001"),
        "conformance_policy_id": Identifier("policy.certificate.synthetic"),
        "conformance_policy_version": SemanticVersion("1.0.0"),
        "valid_from": aware("2026-10-28T20:00:00Z"),
        "valid_until": aware("2026-10-29T18:00:00Z"),
        "trusted_evaluation_time": aware("2026-10-28T20:00:00Z"),
        "additional_limitations": (
            Identifier("limitation.certificate.synthetic"),
        ),
        "additional_unresolved_conditions": (
            Identifier("condition.certificate.synthetic"),
        ),
        "resource_limits": limits(),
        "input_byte_length": 8192,
    }


def compose(
    findings: tuple[fd.ConformanceFinding, ...] | None = None,
    **overrides: object,
) -> cc.ConformanceCertificateContent:
    actual_findings = findings or (make_finding(),)
    args = compose_args(actual_findings)
    args.update(overrides)
    return cc.compose_certificate(**args)


def vector_cases() -> list[dict[str, object]]:
    data = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
    return list(data["cases"])


class CertificateCompositionTests(unittest.TestCase):
    def test_t01_accepted_finding_set_required(self) -> None:
        args = compose_args((make_finding(),))
        args["finding_set_status"] = Identifier("REJECTED")
        with self.assertRaises(ContractValidationError):
            cc.compose_certificate(**args)
        args = compose_args((make_finding(),))
        args["findings"] = ()
        with self.assertRaises(ContractValidationError):
            cc.compose_certificate(**args)

    def test_t02_exact_certificate_field_set(self) -> None:
        certificate = compose()
        self.assertEqual(
            [item.name for item in fields(cc.ConformanceCertificateContent)],
            [
                "certificate_contract_version",
                "certificate_content_id",
                "tenant_id",
                "subject_id",
                "scope_id",
                "architecture_truth_reference_id",
                "finding_set_id",
                "source_evaluation_set_id",
                "evidence_set_id",
                "conformance_policy_id",
                "conformance_policy_version",
                "canonicalization_version",
                "fingerprint_version",
                "valid_from",
                "valid_until",
                "limitations",
                "unresolved_conditions",
                "certificate_content_fingerprint",
                "issuance_authority_state",
            ],
        )
        self.assertEqual(
            certificate.certificate_contract_version,
            cc.CERTIFICATE_CONTRACT_VERSION,
        )

    def test_t03_deterministic_content_id_and_fingerprint(self) -> None:
        first = compose()
        second = compose()
        self.assertEqual(first, second)
        self.assertEqual(first.certificate_content_id, second.certificate_content_id)
        first_bytes = cc.canonical_certificate_bytes(
            first,
            limits(),
            input_byte_length=8192,
        )
        self.assertEqual(
            compute_fingerprint(
                first_bytes,
                limits(),
                canonicalization_version=CANONICALIZATION_VERSION,
                fingerprint_version=FINGERPRINT_VERSION,
            ),
            first.certificate_content_fingerprint,
        )

    def test_t04_tenant_and_subject_scope_bound(self) -> None:
        finding = make_finding()
        certificate = compose((finding,))
        self.assertEqual(certificate.tenant_id, finding.tenant_id)
        self.assertEqual(certificate.subject_id, finding.subject_id)
        self.assertEqual(certificate.scope_id, Identifier("scope.synthetic.001"))

    def test_t05_certificate_scope_cannot_exceed_accepted_scope(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            compose(scope_id=Identifier("scope.synthetic.other"))
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_IDENTIFIER,
        )

    def test_t06_truth_evaluation_and_evidence_identities_bound(self) -> None:
        finding = make_finding()
        certificate = compose((finding,))
        self.assertEqual(
            certificate.architecture_truth_reference_id,
            finding.architecture_truth_reference_id,
        )
        self.assertTrue(certificate.finding_set_id.value.startswith("finding-set."))
        self.assertTrue(
            certificate.source_evaluation_set_id.value.startswith(
                "source-evaluation-set."
            )
        )
        self.assertTrue(certificate.evidence_set_id.value.startswith("evidence-set."))
        self.assertEqual(certificate, compose((finding,)))

    def test_t07_policy_canonicalization_and_fingerprint_versions_bound(self) -> None:
        certificate = compose()
        self.assertEqual(
            certificate.conformance_policy_id,
            Identifier("policy.certificate.synthetic"),
        )
        self.assertEqual(
            certificate.conformance_policy_version,
            SemanticVersion("1.0.0"),
        )
        self.assertEqual(
            certificate.canonicalization_version,
            CANONICALIZATION_VERSION,
        )
        self.assertEqual(certificate.fingerprint_version, FINGERPRINT_VERSION)

    def test_t08_explicit_validity_interval_required(self) -> None:
        with self.assertRaises(ContractValidationError):
            compose(valid_from=datetime(2026, 10, 28, 20, 0, 0))
        with self.assertRaises(ContractValidationError):
            compose(valid_until=aware("2026-10-30T00:00:00Z"))

    def test_t09_stale_or_expired_required_state_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError):
            compose((make_finding(state="STALE"),))
        with self.assertRaises(ContractValidationError):
            compose(valid_until=aware("2026-10-28T20:00:00Z"))

    def test_t10_limitations_preserved(self) -> None:
        finding = make_finding()
        certificate = compose((finding,))
        for item in finding.limitations:
            self.assertIn(item, certificate.limitations)
        self.assertIn(
            Identifier("limitation.certificate.synthetic"),
            certificate.limitations,
        )

    def test_t11_unresolved_conditions_preserved(self) -> None:
        finding = make_finding()
        certificate = compose((finding,))
        for item in finding.unresolved_conditions:
            self.assertIn(item, certificate.unresolved_conditions)
        self.assertIn(
            Identifier("condition.certificate.synthetic"),
            certificate.unresolved_conditions,
        )

    def test_t12_issuance_authority_state_visible(self) -> None:
        certificate = compose()
        self.assertEqual(
            certificate.issuance_authority_state,
            cc.ISSUANCE_AUTHORITY_NOT_AUTHORIZED,
        )

    def test_t13_composition_distinct_from_signing_and_issuance(self) -> None:
        source_path = Path(cc.__file__).resolve()
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
            {"__future__", "dataclasses", "datetime", "afr"},
        )
        self.assertTrue(
            {"open", "exec", "eval", "print"}.isdisjoint(direct_calls)
        )
        self.assertFalse(hasattr(cc, "sign_certificate"))
        self.assertFalse(hasattr(cc, "issue_certificate"))

    def test_t14_accepted_certificate_representation_immutable(self) -> None:
        certificate = compose()
        with self.assertRaises(FrozenInstanceError):
            certificate.scope_id = Identifier("scope.mutated")

    def test_t15_later_state_does_not_rewrite_historical_content(self) -> None:
        prior_finding = make_finding(ordinal=1)
        prior_certificate = compose((prior_finding,))
        later_finding = make_finding(
            state="CONTRADICTED",
            ordinal=2,
            policy_version="1.0.1",
            supersedes=prior_finding.finding_id,
        )
        later_certificate = compose((later_finding,))
        self.assertNotEqual(
            later_certificate.certificate_content_id,
            prior_certificate.certificate_content_id,
        )
        self.assertNotEqual(
            later_certificate.certificate_content_fingerprint,
            prior_certificate.certificate_content_fingerprint,
        )
        self.assertEqual(
            prior_certificate,
            compose((prior_finding,)),
        )

    def test_t16_cross_scope_mismatch_fails_closed(self) -> None:
        base = make_finding(ordinal=1)
        cases = (
            make_finding(ordinal=2, tenant="tenant.other"),
            make_finding(ordinal=2, subject="subject.other"),
            make_finding(ordinal=2, environment="env.other"),
            make_finding(ordinal=2, release="release.other"),
            make_finding(ordinal=2, truth="truth.other"),
        )
        for other in cases:
            with self.subTest(other=other.finding_id.value):
                with self.assertRaises(ContractValidationError):
                    compose((base, other))

    def test_t17_equivalent_input_reproduces_identical_content(self) -> None:
        first_finding = make_finding(ordinal=1)
        second_finding = make_finding(
            state="CONTRADICTED",
            ordinal=2,
        )
        forward = compose((first_finding, second_finding))
        reverse = compose((second_finding, first_finding))
        self.assertEqual(forward, reverse)
        self.assertEqual(
            cc.canonical_certificate_bytes(
                forward,
                limits(),
                input_byte_length=8192,
            ),
            cc.canonical_certificate_bytes(
                reverse,
                limits(),
                input_byte_length=8192,
            ),
        )

    def test_t18_no_external_side_effects_and_vector_replay(self) -> None:
        self.assertEqual(len(vector_cases()), 4)
        for case in vector_cases():
            findings = tuple(
                make_finding(state=str(state), ordinal=index + 1)
                for index, state in enumerate(case["finding_states"])
            )
            args = compose_args(findings)
            args["valid_from"] = aware(str(case["valid_from"]))
            args["valid_until"] = aware(str(case["valid_until"]))
            outcome = str(case["expected_outcome"])
            with self.subTest(case=case["id"]):
                if outcome == "PASS":
                    certificate = cc.compose_certificate(**args)
                    self.assertEqual(
                        certificate.issuance_authority_state,
                        cc.ISSUANCE_AUTHORITY_NOT_AUTHORIZED,
                    )
                else:
                    with self.assertRaises(ContractValidationError):
                        cc.compose_certificate(**args)


if __name__ == "__main__":
    unittest.main()
