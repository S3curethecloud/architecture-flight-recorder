"""Phase 4 normalized-evidence byte admission unit tests."""

from __future__ import annotations

from dataclasses import fields
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import afr.eligibility.normalized_evidence_bytes as _neb
from afr.eligibility.normalized_evidence_bytes import (
    NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
    NormalizedEvidenceBytesContractError,
    NormalizedEvidenceBytesLimitFailure,
    NormalizedEvidenceBytesLimitResult,
    NormalizedEvidenceBytesRequest,
    evaluate_normalized_evidence_bytes_limit,
)


VECTOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "vectors"
    / "eligibility"
    / "normalized-evidence-bytes-v1.json"
)


def make_request(**overrides):
    values = {
        "observation_id": "obs-1",
        "observation_envelope_version": "1.0.0",
        "source_id": "source-1",
        "source_class": "cloud",
        "tenant_id": "tenant-a",
        "subject_id": "subject-a",
        "subject_type": "service",
        "environment_id": "prod",
        "scope_id": "scope-a",
        "release_binding": None,
        "observed_at": datetime(
            2026, 1, 2, 10, 4, 5, 123456, tzinfo=timezone.utc
        ),
        "received_at": datetime(
            2026, 1, 2, 10, 4, 6, tzinfo=timezone.utc
        ),
        "applicable_time": None,
        "valid_from": None,
        "valid_until": None,
        "representation": "json",
        "representation_version": "1.0.0",
        "integrity_reference": "sha256:integrity",
        "integrity_mechanism_version": "1.0.0",
        "provenance_chain_reference": "provenance:chain-1",
        "provenance_version": "1.0.0",
        "content_reference": "content:1",
        "normalized_content": {
            "b": 2,
            "a": "e\u0301",
            "sequence": [1, True, None],
        },
        "normalized_content_identity": "sha256:normalized",
        "trusted_evaluation_time": None,
        "freshness_policy": {
            "mode": "strict",
            "window_seconds": 300,
        },
        "freshness_policy_version": "1.0.0",
        "eligibility_policy_version": "1.0.0",
        "evidence_model_version": "1.0.0",
        "release_binding_present": False,
        "applicable_time_present": False,
        "validity_interval_present": False,
        "trusted_evaluation_time_present": False,
        "freshness_policy_present": True,
        "maximum_normalized_evidence_bytes": 1_000_000,
        "resource_policy_version": "1.0.0",
    }
    values.update(overrides)
    return NormalizedEvidenceBytesRequest(**values)


def projection_document(request):
    return json.loads(_neb._emit_projection_bytes(request).decode("utf-8"))


class PublicContractTests(unittest.TestCase):
    def test_public_surface_is_exactly_six_symbols(self):
        self.assertEqual(
            _neb.__all__,
            (
                "NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED",
                "NormalizedEvidenceBytesRequest",
                "NormalizedEvidenceBytesLimitResult",
                "NormalizedEvidenceBytesLimitFailure",
                "NormalizedEvidenceBytesContractError",
                "evaluate_normalized_evidence_bytes_limit",
            ),
        )

    def test_stable_code_is_exact_string_not_enum(self):
        self.assertIs(type(NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED), str)
        self.assertEqual(
            NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
            "NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED",
        )

    def test_request_has_exact_36_fields_and_is_frozen_slotted(self):
        self.assertEqual(
            tuple(field.name for field in fields(NormalizedEvidenceBytesRequest)),
            (
                "observation_id",
                "observation_envelope_version",
                "source_id",
                "source_class",
                "tenant_id",
                "subject_id",
                "subject_type",
                "environment_id",
                "scope_id",
                "release_binding",
                "observed_at",
                "received_at",
                "applicable_time",
                "valid_from",
                "valid_until",
                "representation",
                "representation_version",
                "integrity_reference",
                "integrity_mechanism_version",
                "provenance_chain_reference",
                "provenance_version",
                "content_reference",
                "normalized_content",
                "normalized_content_identity",
                "trusted_evaluation_time",
                "freshness_policy",
                "freshness_policy_version",
                "eligibility_policy_version",
                "evidence_model_version",
                "release_binding_present",
                "applicable_time_present",
                "validity_interval_present",
                "trusted_evaluation_time_present",
                "freshness_policy_present",
                "maximum_normalized_evidence_bytes",
                "resource_policy_version",
            ),
        )
        self.assertTrue(NormalizedEvidenceBytesRequest.__dataclass_params__.frozen)
        self.assertTrue(hasattr(NormalizedEvidenceBytesRequest, "__slots__"))

    def test_failure_has_exact_7_fields_and_is_frozen_slotted(self):
        self.assertEqual(
            tuple(
                field.name
                for field in fields(NormalizedEvidenceBytesLimitFailure)
            ),
            (
                "code",
                "classification",
                "resource_reference",
                "semantic_location",
                "resource_policy_version",
                "safe_context_maximum_normalized_evidence_bytes",
                "construction_state",
            ),
        )
        self.assertTrue(
            NormalizedEvidenceBytesLimitFailure.__dataclass_params__.frozen
        )
        self.assertTrue(
            hasattr(NormalizedEvidenceBytesLimitFailure, "__slots__")
        )

    def test_result_has_exact_3_fields_and_is_frozen_slotted(self):
        self.assertEqual(
            tuple(field.name for field in fields(NormalizedEvidenceBytesLimitResult)),
            (
                "within_limit",
                "normalized_evidence_bytes",
                "failure",
            ),
        )
        self.assertTrue(NormalizedEvidenceBytesLimitResult.__dataclass_params__.frozen)
        self.assertTrue(hasattr(NormalizedEvidenceBytesLimitResult, "__slots__"))

    def test_contract_error_carries_only_safe_field_path_and_reason(self):
        error = NormalizedEvidenceBytesContractError(
            "normalized_content.value",
            "unsupported projection-value type",
        )
        self.assertEqual(error.field_path, "normalized_content.value")
        self.assertEqual(error.reason, "unsupported projection-value type")
        self.assertNotIn("secret", str(error).lower())


class RequestValidationTests(unittest.TestCase):
    def test_string_subclass_is_rejected(self):
        class DerivedString(str):
            pass

        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(observation_id=DerivedString("obs-1"))

    def test_bool_maximum_is_rejected(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(maximum_normalized_evidence_bytes=True)

    def test_negative_maximum_is_contract_error_not_limit_failure(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(maximum_normalized_evidence_bytes=-1)

    def test_zero_maximum_is_constructible(self):
        request = make_request(maximum_normalized_evidence_bytes=0)
        self.assertEqual(request.maximum_normalized_evidence_bytes, 0)

    def test_naive_timestamp_is_rejected(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(observed_at=datetime(2026, 1, 2, 3, 4, 5))

    def test_float_in_normalized_content_is_rejected(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content={"value": 1.5})

    def test_raw_bytes_are_rejected(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content={"value": b"raw"})

    def test_unordered_collection_is_rejected(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content={"value": {"a", "b"}})

    def test_custom_object_is_rejected(self):
        class Unsupported:
            pass

        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content={"value": Unsupported()})

    def test_direct_self_referential_list_is_rejected(self):
        value = []
        value.append(value)
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content=value)

    def test_direct_self_referential_dict_is_rejected(self):
        value = {}
        value["self"] = value
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content=value)

    def test_indirect_list_dict_cycle_is_rejected(self):
        value = []
        mapping = {"value": value}
        value.append(mapping)
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(normalized_content=value)

    def test_shared_acyclic_subobject_is_accepted_by_value(self):
        shared = {"value": [1, 2]}
        request = make_request(
            normalized_content={"left": shared, "right": shared}
        )
        before = _neb._emit_projection_bytes(request)
        shared["value"].append(3)
        after = _neb._emit_projection_bytes(request)
        self.assertEqual(before, after)

    def test_snapshot_is_independent_of_ambient_recursion_limit(self):
        value = "leaf"
        for _ in range(250):
            value = [value]

        previous = sys.getrecursionlimit()
        try:
            sys.setrecursionlimit(80)
            request = make_request(normalized_content=value)
            result = evaluate_normalized_evidence_bytes_limit(request)
        finally:
            sys.setrecursionlimit(previous)

        self.assertTrue(result.within_limit)

    def test_mutation_during_mapping_capture_fails_closed(self):
        with patch.object(
            _neb,
            "_materialize_mapping_items",
            side_effect=RuntimeError("mapping changed size during iteration"),
        ):
            with self.assertRaises(
                NormalizedEvidenceBytesContractError
            ) as captured:
                make_request(normalized_content={"value": 1})

        self.assertNotIn(
            NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
            str(captured.exception),
        )


class OptionalPresenceTests(unittest.TestCase):
    def test_optional_presence_map_is_exactly_five_booleans(self):
        document = projection_document(make_request())
        self.assertEqual(
            document["optional_field_presence"],
            {
                "release_binding": False,
                "applicable_time": False,
                "validity_interval": False,
                "trusted_evaluation_time": False,
                "freshness_policy": True,
            },
        )
        self.assertTrue(
            all(
                type(value) is bool
                for value in document["optional_field_presence"].values()
            )
        )

    def test_release_binding_absence_omits_root_member(self):
        document = projection_document(make_request())
        self.assertNotIn("release_binding", document)

    def test_release_binding_present_null_is_distinct_from_absence(self):
        document = projection_document(
            make_request(
                release_binding_present=True,
                release_binding=None,
            )
        )
        self.assertIn("release_binding", document)
        self.assertIsNone(document["release_binding"])

    def test_release_binding_false_with_value_is_rejected(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(
                release_binding_present=False,
                release_binding="release-a",
            )

    def test_applicable_time_present_null_is_distinct_from_absence(self):
        absent = projection_document(make_request())
        present_null = projection_document(
            make_request(
                applicable_time_present=True,
                applicable_time=None,
            )
        )
        self.assertNotIn("applicable_time", absent)
        self.assertIn("applicable_time", present_null)
        self.assertIsNone(present_null["applicable_time"])

    def test_validity_interval_both_members_are_present_together(self):
        document = projection_document(
            make_request(
                validity_interval_present=True,
                valid_from=None,
                valid_until=None,
            )
        )
        self.assertIn("valid_from", document)
        self.assertIn("valid_until", document)

    def test_validity_interval_false_rejects_member_value(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(
                validity_interval_present=False,
                valid_from=datetime(2026, 1, 2, tzinfo=timezone.utc),
            )

    def test_trusted_evaluation_time_present_null(self):
        document = projection_document(
            make_request(
                trusted_evaluation_time_present=True,
                trusted_evaluation_time=None,
            )
        )
        self.assertIn("trusted_evaluation_time", document)
        self.assertIsNone(document["trusted_evaluation_time"])

    def test_freshness_policy_absence_omits_value_and_version(self):
        document = projection_document(
            make_request(
                freshness_policy_present=False,
                freshness_policy=None,
                freshness_policy_version=None,
            )
        )
        self.assertNotIn("freshness_policy", document)
        self.assertNotIn("freshness_policy_version", document)

    def test_freshness_policy_present_null_preserves_nulls(self):
        document = projection_document(
            make_request(
                freshness_policy_present=True,
                freshness_policy=None,
                freshness_policy_version=None,
            )
        )
        self.assertIn("freshness_policy", document)
        self.assertIn("freshness_policy_version", document)
        self.assertIsNone(document["freshness_policy"])
        self.assertIsNone(document["freshness_policy_version"])

    def test_freshness_policy_false_rejects_value(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(
                freshness_policy_present=False,
                freshness_policy={"window": 10},
                freshness_policy_version=None,
            )


class SnapshotAndSerializationTests(unittest.TestCase):
    def test_normalized_content_is_deep_snapshot(self):
        content = {"items": [1, {"name": "before"}]}
        request = make_request(normalized_content=content)
        before = _neb._emit_projection_bytes(request)
        content["items"][1]["name"] = "after"
        content["items"].append(2)
        after = _neb._emit_projection_bytes(request)
        self.assertEqual(before, after)

    def test_freshness_policy_is_deep_snapshot(self):
        policy = {"windows": [60, 300]}
        request = make_request(freshness_policy=policy)
        before = _neb._emit_projection_bytes(request)
        policy["windows"].append(900)
        after = _neb._emit_projection_bytes(request)
        self.assertEqual(before, after)

    def test_list_mutation_after_request_construction_is_irrelevant(self):
        values = [1, 2]
        request = make_request(normalized_content=values)
        before = _neb._emit_projection_bytes(request)
        values.reverse()
        values.append(3)
        self.assertEqual(before, _neb._emit_projection_bytes(request))

    def test_dict_mutation_after_request_construction_is_irrelevant(self):
        values = {"a": 1}
        request = make_request(normalized_content=values)
        before = _neb._emit_projection_bytes(request)
        values["b"] = 2
        self.assertEqual(before, _neb._emit_projection_bytes(request))

    def test_nfc_string_equivalence(self):
        decomposed = _neb._emit_projection_bytes(
            make_request(normalized_content={"text": "e\u0301"})
        )
        composed = _neb._emit_projection_bytes(
            make_request(normalized_content={"text": "\u00e9"})
        )
        self.assertEqual(decomposed, composed)

    def test_mapping_order_is_by_canonical_key_bytes(self):
        first = _neb._emit_projection_bytes(
            make_request(normalized_content={"b": 2, "a": 1})
        )
        second = _neb._emit_projection_bytes(
            make_request(normalized_content={"a": 1, "b": 2})
        )
        self.assertEqual(first, second)
        self.assertIn(
            b'"normalized_content":{"a":1,"b":2}',
            first,
        )

    def test_nfc_key_collision_is_rejected_without_repair(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            make_request(
                normalized_content={"e\u0301": 1, "\u00e9": 2}
            )

    def test_sequence_order_is_preserved(self):
        first = _neb._emit_projection_bytes(
            make_request(normalized_content={"values": [1, 2, 3]})
        )
        second = _neb._emit_projection_bytes(
            make_request(normalized_content={"values": [3, 2, 1]})
        )
        self.assertNotEqual(first, second)
        self.assertIn(b'"values":[1,2,3]', first)

    def test_timestamp_normalizes_to_utc_z(self):
        instant = datetime(
            2026, 1, 2, 10, 4, 5, 123456, tzinfo=timezone.utc
        )
        offset = instant.astimezone(timezone(timedelta(hours=-7)))
        first = _neb._emit_projection_bytes(
            make_request(observed_at=instant)
        )
        second = _neb._emit_projection_bytes(
            make_request(observed_at=offset)
        )
        self.assertEqual(first, second)
        self.assertIn(b'"2026-01-02T10:04:05.123456Z"', first)

    def test_closed_root_schema_has_exact_32_members_when_all_present(self):
        instant = datetime(2026, 1, 2, tzinfo=timezone.utc)
        document = projection_document(
            make_request(
                release_binding_present=True,
                release_binding="release-a",
                applicable_time_present=True,
                applicable_time=instant,
                validity_interval_present=True,
                valid_from=instant,
                valid_until=instant,
                trusted_evaluation_time_present=True,
                trusted_evaluation_time=instant,
            )
        )
        self.assertEqual(
            set(document),
            {
                "projection_schema_version",
                "projection_serialization_version",
                "observation_id",
                "observation_envelope_version",
                "source_id",
                "source_class",
                "tenant_id",
                "subject_id",
                "subject_type",
                "environment_id",
                "scope_id",
                "release_binding",
                "observed_at",
                "received_at",
                "applicable_time",
                "valid_from",
                "valid_until",
                "representation",
                "representation_version",
                "integrity_reference",
                "integrity_mechanism_version",
                "provenance_chain_reference",
                "provenance_version",
                "content_reference",
                "normalized_content",
                "normalized_content_identity",
                "trusted_evaluation_time",
                "freshness_policy",
                "freshness_policy_version",
                "eligibility_policy_version",
                "evidence_model_version",
                "optional_field_presence",
            },
        )
        self.assertEqual(len(document), 32)

    def test_admission_inputs_are_excluded_from_projection(self):
        document = projection_document(make_request())
        self.assertNotIn("maximum_normalized_evidence_bytes", document)
        self.assertNotIn("resource_policy_version", document)

    def test_final_decision_identity_and_accounting_are_excluded(self):
        raw = _neb._emit_projection_bytes(make_request())
        self.assertNotIn(b"final_eligibility_decision", raw)
        self.assertNotIn(b"final_evidence_identity", raw)
        self.assertNotIn(b"resource_accounting", raw)


class LimitAdmissionTests(unittest.TestCase):
    def test_count_equal_to_maximum_passes(self):
        baseline = make_request()
        expected = len(_neb._emit_projection_bytes(baseline))
        request = make_request(
            maximum_normalized_evidence_bytes=expected
        )
        result = evaluate_normalized_evidence_bytes_limit(request)
        self.assertTrue(result.within_limit)
        self.assertEqual(result.normalized_evidence_bytes, expected)
        self.assertIsNone(result.failure)

    def test_count_greater_than_maximum_returns_exact_failure(self):
        baseline = make_request()
        expected = len(_neb._emit_projection_bytes(baseline))
        request = make_request(
            maximum_normalized_evidence_bytes=expected - 1
        )
        result = evaluate_normalized_evidence_bytes_limit(request)
        self.assertFalse(result.within_limit)
        self.assertIsNone(result.normalized_evidence_bytes)
        self.assertEqual(
            result.failure,
            NormalizedEvidenceBytesLimitFailure(
                code=NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
                classification="PROCESSING_FAILURE",
                resource_reference="normalized_evidence_bytes",
                semantic_location="normalized_evidence_bytes",
                resource_policy_version="1.0.0",
                safe_context_maximum_normalized_evidence_bytes=(
                    expected - 1
                ),
                construction_state=(
                    "STOPPED_BEFORE_EVIDENCE_CONSTRUCTION"
                ),
            ),
        )

    def test_zero_maximum_fails_as_limit_not_policy_error(self):
        result = evaluate_normalized_evidence_bytes_limit(
            make_request(maximum_normalized_evidence_bytes=0)
        )
        self.assertFalse(result.within_limit)
        self.assertEqual(
            result.failure.code,
            NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
        )

    def test_failure_policy_version_is_copied_unchanged(self):
        result = evaluate_normalized_evidence_bytes_limit(
            make_request(
                maximum_normalized_evidence_bytes=0,
                resource_policy_version="resource-policy-v7",
            )
        )
        self.assertEqual(
            result.failure.resource_policy_version,
            "resource-policy-v7",
        )

    def test_failure_safe_context_contains_only_applicable_maximum(self):
        failure = evaluate_normalized_evidence_bytes_limit(
            make_request(maximum_normalized_evidence_bytes=7)
        ).failure
        self.assertEqual(
            tuple(field.name for field in fields(failure)),
            (
                "code",
                "classification",
                "resource_reference",
                "semantic_location",
                "resource_policy_version",
                "safe_context_maximum_normalized_evidence_bytes",
                "construction_state",
            ),
        )
        self.assertEqual(
            failure.safe_context_maximum_normalized_evidence_bytes,
            7,
        )
        self.assertFalse(hasattr(failure, "partial_count"))
        self.assertFalse(hasattr(failure, "projection_bytes"))
        self.assertFalse(hasattr(failure, "normalized_content"))

    def test_public_result_exposes_no_projection_or_decision_payload(self):
        result = evaluate_normalized_evidence_bytes_limit(make_request())
        self.assertFalse(hasattr(result, "projection_bytes"))
        self.assertFalse(hasattr(result, "normalized_content"))
        self.assertFalse(hasattr(result, "eligibility_decision"))
        self.assertFalse(hasattr(result, "evidence_identity"))
        self.assertFalse(hasattr(result, "resource_accounting_record"))

    def test_non_request_direct_call_is_contract_error(self):
        with self.assertRaises(NormalizedEvidenceBytesContractError):
            evaluate_normalized_evidence_bytes_limit(object())


class CorrectionRegressionTests(unittest.TestCase):
    def test_measurement_consumes_no_phase4_work_units(self):
        request_field_names = {
            field.name for field in fields(NormalizedEvidenceBytesRequest)
        }
        result_field_names = {
            field.name for field in fields(NormalizedEvidenceBytesLimitResult)
        }
        failure_field_names = {
            field.name for field in fields(NormalizedEvidenceBytesLimitFailure)
        }
        governed_names = (
            request_field_names | result_field_names | failure_field_names
        )
        self.assertFalse(
            any("work_unit" in name for name in governed_names)
        )
        result = evaluate_normalized_evidence_bytes_limit(make_request())
        self.assertFalse(hasattr(result, "work_units"))
        self.assertFalse(hasattr(result, "work_unit_count"))

    def test_phase3_maximum_canonical_bytes_remains_independent(self):
        request_field_names = {
            field.name for field in fields(NormalizedEvidenceBytesRequest)
        }
        self.assertNotIn("maximum_canonical_bytes", request_field_names)
        self.assertFalse(
            hasattr(make_request(), "maximum_canonical_bytes")
        )
        result = evaluate_normalized_evidence_bytes_limit(
            make_request(maximum_normalized_evidence_bytes=0)
        )
        self.assertEqual(
            result.failure.code,
            NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
        )
        self.assertNotEqual(
            result.failure.code,
            "RESOURCE_LIMIT_EXCEEDED",
        )

    def test_invalid_result_state_construction_raises_contract_error(self):
        failure = NormalizedEvidenceBytesLimitFailure(
            code=NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
            classification="PROCESSING_FAILURE",
            resource_reference="normalized_evidence_bytes",
            semantic_location="normalized_evidence_bytes",
            resource_policy_version="1.0.0",
            safe_context_maximum_normalized_evidence_bytes=7,
            construction_state="STOPPED_BEFORE_EVIDENCE_CONSTRUCTION",
        )
        invalid_states = (
            {
                "within_limit": True,
                "normalized_evidence_bytes": None,
                "failure": None,
            },
            {
                "within_limit": True,
                "normalized_evidence_bytes": 7,
                "failure": failure,
            },
            {
                "within_limit": False,
                "normalized_evidence_bytes": 7,
                "failure": failure,
            },
            {
                "within_limit": False,
                "normalized_evidence_bytes": None,
                "failure": None,
            },
        )
        for state in invalid_states:
            with self.subTest(state=state):
                with self.assertRaises(NormalizedEvidenceBytesContractError):
                    NormalizedEvidenceBytesLimitResult(**state)

    def test_large_exact_int_canonicalization_and_limit_semantics_ignore_interpreter_digit_limit(self):
        if not hasattr(sys, "set_int_max_str_digits"):
            self.skipTest("interpreter has no integer-string digit limit")

        previous_limit = sys.get_int_max_str_digits()
        try:
            sys.set_int_max_str_digits(640)
            large_integer = 10 ** 699 + 12345
            baseline = make_request(
                normalized_content={"large_integer": large_integer},
                maximum_normalized_evidence_bytes=1_000_000,
            )
            expected = len(_neb._emit_projection_bytes(baseline))

            exact = evaluate_normalized_evidence_bytes_limit(
                make_request(
                    normalized_content={"large_integer": large_integer},
                    maximum_normalized_evidence_bytes=expected,
                )
            )
            self.assertTrue(exact.within_limit)
            self.assertEqual(exact.normalized_evidence_bytes, expected)

            below = evaluate_normalized_evidence_bytes_limit(
                make_request(
                    normalized_content={"large_integer": large_integer},
                    maximum_normalized_evidence_bytes=expected - 1,
                )
            )
            self.assertFalse(below.within_limit)
            self.assertEqual(
                below.failure.code,
                NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
            )
        finally:
            sys.set_int_max_str_digits(previous_limit)

    def test_large_mapping_key_small_limit_is_governed_limit_failure(self):
        common = "x" * 10_000
        normalized_content = {
            common + "b": 2,
            common + "a": 1,
        }
        empty_projection = _neb._emit_projection_bytes(
            make_request(normalized_content={})
        )
        marker = b'"normalized_content":{}'
        marker_offset = empty_projection.index(marker)
        small_limit = marker_offset + len(b'"normalized_content":{') + 8

        result = evaluate_normalized_evidence_bytes_limit(
            make_request(
                normalized_content=normalized_content,
                maximum_normalized_evidence_bytes=small_limit,
            )
        )
        self.assertFalse(result.within_limit)
        self.assertIsNone(result.normalized_evidence_bytes)
        self.assertEqual(
            result.failure.code,
            NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
        )


    # AFR_D1_CORRECTION_TEST_BEGIN
    def test_evaluator_has_no_ambient_runtime_dependencies(self):
        forbidden_by_category = {
            "clock": {
                "time",
                "time_ns",
                "monotonic",
                "monotonic_ns",
                "perf_counter",
                "perf_counter_ns",
                "process_time",
                "process_time_ns",
                "now",
                "utcnow",
                "today",
            },
            "randomness": {
                "random",
                "randint",
                "randrange",
                "choice",
                "choices",
                "shuffle",
                "sample",
                "uniform",
                "getrandbits",
                "secrets",
                "token_bytes",
                "token_hex",
                "token_urlsafe",
                "uuid4",
            },
            "environment": {
                "environ",
                "getenv",
                "putenv",
                "unsetenv",
            },
            "filesystem": {
                "open",
                "pathlib",
                "Path",
                "read_text",
                "write_text",
                "read_bytes",
                "write_bytes",
                "listdir",
                "scandir",
                "walk",
                "stat",
                "lstat",
                "unlink",
                "mkdir",
                "makedirs",
                "rmdir",
            },
            "network": {
                "socket",
                "create_connection",
                "urlopen",
                "requests",
                "urllib",
                "http",
                "connect",
                "sendall",
                "recv",
            },
            "provider": {
                "boto3",
                "botocore",
                "aws",
                "azure",
                "google",
                "provider",
                "sdk",
            },
            "secret": {
                "secrets",
                "secret",
                "credential",
                "credentials",
                "password",
                "api_key",
                "token_bytes",
                "token_hex",
                "token_urlsafe",
            },
            "persistence": {
                "sqlite3",
                "sqlalchemy",
                "redis",
                "psycopg",
                "database",
                "db",
                "cache",
                "queue",
                "kafka",
                "persistence",
                "persist",
            },
        }

        executable_surfaces = {}
        for name, value in vars(_neb).items():
            if getattr(value, "__module__", None) != _neb.__name__:
                continue

            code = getattr(value, "__code__", None)
            if code is not None:
                executable_surfaces[name] = code

            if isinstance(value, type):
                for member_name, member in vars(value).items():
                    target = getattr(member, "__func__", member)
                    member_code = getattr(target, "__code__", None)
                    if member_code is not None:
                        executable_surfaces[
                            f"{name}.{member_name}"
                        ] = member_code

        violations = {}
        for category, forbidden_symbols in forbidden_by_category.items():
            category_hits = []
            for surface_name, code in executable_surfaces.items():
                hits = sorted(
                    set(code.co_names) & forbidden_symbols
                )
                if hits:
                    category_hits.append((surface_name, hits))
            if category_hits:
                violations[category] = category_hits

        self.assertTrue(executable_surfaces)
        self.assertEqual(violations, {})
    # AFR_D1_CORRECTION_TEST_END


class VectorTests(unittest.TestCase):
    def test_static_vector_exact_projection_hex_and_octet_count(self):
        document = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
        vector = document["normalized_evidence_bytes_vectors"][0]
        request_data = dict(vector["request"])

        for name in (
            "observed_at",
            "received_at",
            "applicable_time",
            "valid_from",
            "valid_until",
            "trusted_evaluation_time",
        ):
            value = request_data[name]
            if value is not None:
                request_data[name] = datetime.fromisoformat(
                    value.replace("Z", "+00:00")
                )

        request = NormalizedEvidenceBytesRequest(**request_data)
        actual = _neb._emit_projection_bytes(request)

        self.assertEqual(
            actual.hex(),
            vector["expected_canonical_projection_utf8_hex"],
        )
        self.assertEqual(
            len(actual),
            vector["expected_normalized_evidence_byte_count"],
        )

    def test_vector_limit_boundary_reproduces_pass_and_fail(self):
        document = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
        vector = document["normalized_evidence_bytes_vectors"][0]
        request_data = dict(vector["request"])

        for name in (
            "observed_at",
            "received_at",
            "applicable_time",
            "valid_from",
            "valid_until",
            "trusted_evaluation_time",
        ):
            value = request_data[name]
            if value is not None:
                request_data[name] = datetime.fromisoformat(
                    value.replace("Z", "+00:00")
                )

        count = vector["expected_normalized_evidence_byte_count"]

        exact = dict(request_data)
        exact["maximum_normalized_evidence_bytes"] = count
        exact_result = evaluate_normalized_evidence_bytes_limit(
            NormalizedEvidenceBytesRequest(**exact)
        )
        self.assertTrue(exact_result.within_limit)
        self.assertEqual(exact_result.normalized_evidence_bytes, count)

        below = dict(request_data)
        below["maximum_normalized_evidence_bytes"] = count - 1
        below_result = evaluate_normalized_evidence_bytes_limit(
            NormalizedEvidenceBytesRequest(**below)
        )
        self.assertFalse(below_result.within_limit)
        self.assertEqual(
            below_result.failure.code,
            NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
        )


if __name__ == "__main__":
    unittest.main()
