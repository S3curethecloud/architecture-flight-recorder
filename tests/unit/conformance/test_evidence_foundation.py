from __future__ import annotations

import ast
from datetime import datetime, timezone
import json
from pathlib import Path
import unittest

import afr.conformance.evidence_foundation as ef
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
from afr.kernel.fingerprints import FINGERPRINT_VERSION


UTC = timezone.utc


def aware(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def limits() -> ResourceLimits:
    return ResourceLimits(
        version=CANONICALIZATION_VERSION,
        maximum_input_bytes=8192,
        maximum_collection_items=256,
        maximum_nesting_depth=16,
        maximum_canonical_bytes=8192,
        maximum_work_units=32768,
    )


def evaluation(
    *,
    tenant: str = "tenant.synthetic",
    subject: str = "subject.synthetic.001",
    fingerprint_version: SemanticVersion = FINGERPRINT_VERSION,
) -> EvaluationBinding:
    return EvaluationBinding(
        invocation_id=Identifier("invocation.synthetic.001"),
        tenant=TenantBinding(Identifier(tenant)),
        subject=SubjectBinding(
            Identifier(subject),
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
            valid_until=aware("2026-10-28T20:00:00Z"),
        ),
        contract_version=SemanticVersion("1.0.0"),
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=fingerprint_version,
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


def build(**overrides: object) -> ef.EvidenceFoundationBinding:
    args: dict[str, object] = {
        "foundation_contract_version":
            ef.FOUNDATION_CONTRACT_VERSION,
        "source_evaluation_cycle_id":
            Identifier("cycle.synthetic.001"),
        "source_evaluation_result_id":
            Identifier("result.synthetic.001"),
        "source_evaluation_status":
            ef.ACCEPTED_SOURCE_EVALUATION_STATUS,
        "tenant_id": Identifier("tenant.synthetic"),
        "subject_id": Identifier("subject.synthetic.001"),
        "architecture_truth_reference_id":
            Identifier("truth.phase12.synthetic.001"),
        "evidence_binding_or_set_id":
            Identifier("evidence.synthetic.set.001"),
        "trusted_time_context_id":
            Identifier("time.synthetic.001"),
        "evaluation_binding": evaluation(),
        "provenance": provenance(),
        "limitations":
            (Identifier("limitation.synthetic-only"),),
        "unresolved_conditions":
            (
                Identifier(
                    "condition.external-issuance-not-authorized"
                ),
            ),
        "resource_limits": limits(),
        "input_byte_length": 512,
    }
    args.update(overrides)
    return ef.build_evidence_foundation(**args)


class EvidenceFoundationTests(unittest.TestCase):
    def test_t01_valid_binding_construction(self) -> None:
        result = build()
        self.assertEqual(
            result.foundation_contract_version,
            ef.FOUNDATION_CONTRACT_VERSION,
        )
        self.assertEqual(
            result.source_evaluation_status.value,
            "ACCEPTED",
        )
        self.assertTrue(result.canonical_bytes)
        self.assertEqual(result.fingerprint.algorithm, "sha256")

    def test_t02_missing_required_identity_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            Identifier("")
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
        )

    def test_t03_invalid_tenant_subject_scope_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError) as tenant_ctx:
            build(tenant_id=Identifier("tenant.other"))
        self.assertEqual(
            tenant_ctx.exception.failure.code,
            ProcessingFailureCode.TENANT_BINDING_MISMATCH,
        )

        with self.assertRaises(ContractValidationError) as subject_ctx:
            build(subject_id=Identifier("subject.other"))
        self.assertEqual(
            subject_ctx.exception.failure.code,
            ProcessingFailureCode.SUBJECT_BINDING_MISMATCH,
        )

    def test_t04_invalid_or_missing_provenance_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            build(provenance=None)
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_TYPE,
        )

        with self.assertRaises(ContractValidationError) as empty_ctx:
            ProvenanceBinding(
                source_id=Identifier(""),
                collector_id=Identifier("collector.synthetic"),
                observed_at=aware("2026-10-27T19:59:00Z"),
                integrity_reference=OptionalValue.missing(),
            )
        self.assertEqual(
            empty_ctx.exception.failure.code,
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
        )

    def test_t05_untrusted_or_naive_time_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            TimeBinding(
                evaluated_at=datetime(2026, 10, 27, 20, 0, 0),
                valid_from=datetime(2026, 10, 27, 20, 0, 0),
                valid_until=datetime(2026, 10, 28, 20, 0, 0),
            )
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_TIMESTAMP,
        )

    def test_t06_version_binding_is_explicit_and_validated(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            build(
                foundation_contract_version=SemanticVersion("9.9.9")
            )
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_VERSION,
        )

    def test_t07_canonical_bytes_are_deterministic(self) -> None:
        first = build()
        second = build()
        self.assertEqual(first.canonical_bytes, second.canonical_bytes)

    def test_t08_fingerprint_is_deterministic_and_version_bound(self) -> None:
        first = build()
        second = build()
        self.assertEqual(
            first.fingerprint.digest_hex,
            second.fingerprint.digest_hex,
        )

        with self.assertRaises(ContractValidationError) as ctx:
            build(
                evaluation_binding=evaluation(
                    fingerprint_version=SemanticVersion("9.9.9")
                )
            )
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_VERSION,
        )

    def test_t09_limitations_and_unresolved_conditions_preserved(self) -> None:
        result = build(
            limitations=(
                Identifier("limitation.z"),
                Identifier("limitation.a"),
            ),
            unresolved_conditions=(
                Identifier("condition.z"),
                Identifier("condition.a"),
            ),
        )
        self.assertEqual(
            tuple(item.value for item in result.limitations),
            ("limitation.a", "limitation.z"),
        )
        self.assertEqual(
            tuple(
                item.value
                for item in result.unresolved_conditions
            ),
            ("condition.a", "condition.z"),
        )

    def test_t10_no_finding_drift_certificate_or_authority_promotion(self) -> None:
        result = build()
        payload = json.loads(result.canonical_bytes)
        forbidden = (
            "finding_state",
            "drift_class",
            "certificate_content_id",
            "issuance_authority_state",
            "provider_mutation_authority",
        )
        for key in forbidden:
            self.assertNotIn(key, payload)

    def test_t11_no_external_side_effects_or_wall_clock_read(self) -> None:
        source_path = Path(ef.__file__).resolve()
        tree = ast.parse(source_path.read_text(), filename=str(source_path))

        forbidden_import_roots = {
            "os",
            "pathlib",
            "socket",
            "subprocess",
            "requests",
            "urllib",
            "http",
        }
        imported_roots: set[str] = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(
                    alias.name.split(".", 1)[0]
                    for alias in node.names
                )
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".", 1)[0])

        self.assertTrue(
            imported_roots.isdisjoint(forbidden_import_roots)
        )

        source_text = source_path.read_text()
        for forbidden_call in (
            "datetime.now(",
            "datetime.utcnow(",
            "time.time(",
            "open(",
            "subprocess.",
            "socket.",
            "requests.",
        ):
            self.assertNotIn(forbidden_call, source_text)

    def test_t12_vector_replay_matches_expected_pass_or_failure_code(self) -> None:
        vector_path = (
            Path(__file__).resolve().parents[2]
            / "vectors"
            / "conformance"
            / "evidence-foundation-v1.json"
        )
        vector = json.loads(vector_path.read_text())
        case = vector["case"]

        result = build()
        self.assertEqual(
            result.fingerprint.digest_hex,
            case["expected_fingerprint_digest_hex"],
        )
        self.assertEqual(
            result.canonical_bytes.decode("utf-8"),
            case["expected_canonical_utf8"],
        )

        negative = {
            item["name"]: item
            for item in vector["negative_cases"]
        }

        with self.assertRaises(ContractValidationError) as tenant_ctx:
            build(tenant_id=Identifier("tenant.other"))
        self.assertEqual(
            tenant_ctx.exception.failure.code.value,
            negative["tenant-mismatch"]["expected_failure_code"],
        )

        with self.assertRaises(ContractValidationError) as subject_ctx:
            build(subject_id=Identifier("subject.other"))
        self.assertEqual(
            subject_ctx.exception.failure.code.value,
            negative["subject-mismatch"]["expected_failure_code"],
        )

        with self.assertRaises(ContractValidationError) as status_ctx:
            build(source_evaluation_status=Identifier("REJECTED"))
        self.assertEqual(
            status_ctx.exception.failure.code.value,
            negative["source-not-accepted"]["expected_failure_code"],
        )


if __name__ == "__main__":
    unittest.main()
