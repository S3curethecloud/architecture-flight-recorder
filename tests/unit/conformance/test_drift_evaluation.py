from __future__ import annotations

import ast
from datetime import datetime, timezone
import json
from pathlib import Path
import unittest

import afr.conformance.drift_evaluation as de
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
        maximum_input_bytes=16384,
        maximum_collection_items=512,
        maximum_nesting_depth=24,
        maximum_canonical_bytes=16384,
        maximum_work_units=65536,
    )


def evaluation() -> EvaluationBinding:
    return EvaluationBinding(
        invocation_id=Identifier("invocation.synthetic.s2.001"),
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
        input_byte_length=512,
    )


def run_case(**overrides: object) -> de.DriftEvaluationResult:
    args: dict[str, object] = {
        "drift_contract_version":
            de.DRIFT_EVALUATION_CONTRACT_VERSION,
        "foundation": foundation(),
        "expected_value": "expected.synthetic.v1",
        "evidence_available": True,
        "evidence_conclusive": True,
        "evidence_value": "expected.synthetic.v1",
        "evidence_observed_at":
            aware("2026-10-28T19:59:00Z"),
        "trusted_evaluation_time":
            aware("2026-10-28T20:00:00Z"),
        "freshness_bound_seconds": 3600,
        "evidence_references": (
            Identifier("evidence.ref.synthetic.b"),
            Identifier("evidence.ref.synthetic.a"),
        ),
        "resource_limits": limits(),
        "input_byte_length": 1024,
    }
    args.update(overrides)
    return de.evaluate_drift(**args)


class DriftEvaluationTests(unittest.TestCase):
    def test_t01_matching_fresh_conclusive_returns_supported(self) -> None:
        result = run_case()
        self.assertEqual(result.state, de.DriftState.SUPPORTED)

    def test_t02_contradictory_fresh_conclusive_returns_contradicted(self) -> None:
        result = run_case(
            evidence_value="observed.synthetic.other"
        )
        self.assertEqual(
            result.state,
            de.DriftState.CONTRADICTED,
        )

    def test_t03_stale_evidence_returns_stale(self) -> None:
        result = run_case(
            evidence_conclusive=False,
            evidence_value="ambiguous.synthetic.value",
            evidence_observed_at=
                aware("2026-10-28T17:00:00Z"),
        )
        self.assertEqual(result.state, de.DriftState.STALE)

    def test_t04_fresh_ambiguous_evidence_returns_inconclusive(self) -> None:
        result = run_case(evidence_conclusive=False)
        self.assertEqual(
            result.state,
            de.DriftState.INCONCLUSIVE,
        )

    def test_t05_unavailable_evidence_returns_evidence_unavailable(self) -> None:
        result = run_case(
            evidence_available=False,
            evidence_conclusive=False,
            evidence_value=None,
            evidence_observed_at=None,
        )
        self.assertEqual(
            result.state,
            de.DriftState.EVIDENCE_UNAVAILABLE,
        )

    def test_t06_result_vocabulary_exactly_five_states(self) -> None:
        self.assertEqual(
            tuple(item.value for item in de.DriftState),
            (
                "SUPPORTED",
                "CONTRADICTED",
                "STALE",
                "INCONCLUSIVE",
                "EVIDENCE_UNAVAILABLE",
            ),
        )

    def test_t07_s1_foundation_bindings_are_preserved(self) -> None:
        source = foundation()
        result = run_case(foundation=source)
        payload = json.loads(result.canonical_bytes)

        self.assertEqual(
            result.foundation_contract_version,
            source.foundation_contract_version,
        )
        self.assertEqual(
            result.foundation_fingerprint.digest_hex,
            source.fingerprint.digest_hex,
        )
        self.assertEqual(
            result.source_evaluation_cycle_id,
            source.source_evaluation_cycle_id,
        )
        self.assertEqual(result.tenant_id, source.tenant_id)
        self.assertEqual(result.subject_id, source.subject_id)

        bound = payload["foundation"]
        self.assertEqual(
            bound["foundation_fingerprint_digest_hex"],
            source.fingerprint.digest_hex,
        )
        self.assertEqual(
            bound["architecture_truth_reference_id"],
            source.architecture_truth_reference_id.value,
        )
        self.assertEqual(
            bound["provenance"]["source_id"],
            source.provenance.source_id.value,
        )

    def test_t08_reason_and_evidence_references_stable_sorted(self) -> None:
        first = run_case()
        second = run_case()

        self.assertEqual(
            tuple(item.value for item in first.evidence_references),
            (
                "evidence.ref.synthetic.a",
                "evidence.ref.synthetic.b",
            ),
        )
        self.assertEqual(
            tuple(item.value for item in first.reason_codes),
            ("reason.s2.supported",),
        )
        self.assertEqual(
            first.evidence_references,
            second.evidence_references,
        )
        self.assertEqual(first.reason_codes, second.reason_codes)

    def test_t09_same_inputs_are_deterministic(self) -> None:
        first = run_case()
        second = run_case()

        self.assertEqual(first.state, second.state)
        self.assertEqual(
            first.canonical_bytes,
            second.canonical_bytes,
        )
        self.assertEqual(
            first.fingerprint.digest_hex,
            second.fingerprint.digest_hex,
        )

    def test_t10_invalid_input_fails_closed_as_processing_failure(self) -> None:
        with self.assertRaises(ContractValidationError) as type_ctx:
            run_case(foundation=None)
        self.assertEqual(
            type_ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_TYPE,
        )

        with self.assertRaises(ContractValidationError) as version_ctx:
            run_case(
                drift_contract_version=
                    SemanticVersion("9.9.9")
            )
        self.assertEqual(
            version_ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_VERSION,
        )

        with self.assertRaises(ContractValidationError) as missing_ctx:
            run_case(expected_value="")
        self.assertEqual(
            missing_ctx.exception.failure.code,
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
        )

    def test_t11_trusted_time_is_caller_supplied_no_wall_clock(self) -> None:
        with self.assertRaises(ContractValidationError) as ctx:
            run_case(
                trusted_evaluation_time=
                    datetime(2026, 10, 28, 20, 0, 0)
            )
        self.assertEqual(
            ctx.exception.failure.code,
            ProcessingFailureCode.INVALID_TIMESTAMP,
        )

        source_path = Path(de.__file__).resolve()
        source_text = source_path.read_text()
        for forbidden in (
            "datetime.now(",
            "datetime.utcnow(",
            "time.time(",
        ):
            self.assertNotIn(forbidden, source_text)

    def test_t12_no_finding_creation_persistence_or_lifecycle_promotion(self) -> None:
        payload = json.loads(run_case().canonical_bytes)
        forbidden = (
            "finding_id",
            "finding_state",
            "finding_lifecycle",
            "finding_persistence",
            "finding_authority",
        )
        for key in forbidden:
            self.assertNotIn(key, payload)

    def test_t13_no_certificate_command_center_nexus_or_execution_promotion(self) -> None:
        payload = json.loads(run_case().canonical_bytes)
        forbidden = (
            "certificate_content_id",
            "certificate_issuance",
            "command_center_write",
            "nexus_architecture_acceptance",
            "execution_authority",
            "provider_mutation_authority",
        )
        for key in forbidden:
            self.assertNotIn(key, payload)

    def test_t14_no_external_side_effects_or_hidden_mutation(self) -> None:
        source_path = Path(de.__file__).resolve()
        source_text = source_path.read_text()
        tree = ast.parse(source_text, filename=str(source_path))

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

        for forbidden in (
            "open(",
            "subprocess.",
            "socket.",
            "requests.",
            "urllib.",
        ):
            self.assertNotIn(forbidden, source_text)

    def test_t15_vector_replay_covers_five_states_and_failures(self) -> None:
        vector_path = (
            Path(__file__).resolve().parents[2]
            / "vectors"
            / "conformance"
            / "drift-evaluation-v1.json"
        )
        vector = json.loads(vector_path.read_text())

        observed_states: set[str] = set()

        for case in vector["cases"]:
            observed = (
                None
                if case["evidence_observed_at"] is None
                else aware(case["evidence_observed_at"])
            )
            result = run_case(
                expected_value=case["expected_value"],
                evidence_available=case["evidence_available"],
                evidence_conclusive=case["evidence_conclusive"],
                evidence_value=case["evidence_value"],
                evidence_observed_at=observed,
                trusted_evaluation_time=
                    aware(case["trusted_evaluation_time"]),
                freshness_bound_seconds=
                    case["freshness_bound_seconds"],
            )
            self.assertEqual(
                result.state.value,
                case["expected_state"],
            )
            observed_states.add(result.state.value)

        self.assertEqual(
            observed_states,
            {
                "SUPPORTED",
                "CONTRADICTED",
                "STALE",
                "INCONCLUSIVE",
                "EVIDENCE_UNAVAILABLE",
            },
        )

        failures = {
            item["name"]: item
            for item in vector["failure_cases"]
        }

        with self.assertRaises(ContractValidationError) as version_ctx:
            run_case(
                drift_contract_version=
                    SemanticVersion("9.9.9")
            )
        self.assertEqual(
            version_ctx.exception.failure.code.value,
            failures["invalid-contract-version"][
                "expected_failure_code"
            ],
        )

        with self.assertRaises(ContractValidationError) as time_ctx:
            run_case(
                trusted_evaluation_time=
                    datetime(2026, 10, 28, 20, 0, 0)
            )
        self.assertEqual(
            time_ctx.exception.failure.code.value,
            failures["naive-trusted-evaluation-time"][
                "expected_failure_code"
            ],
        )


if __name__ == "__main__":
    unittest.main()
