"""Deterministic canonicalization unit tests."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import unittest

from afr.kernel.canonicalization import (
    CANONICALIZATION_VERSION,
    canonicalize,
)
from afr.kernel.contracts import (
    ContractValidationError,
    EnvironmentBinding,
    EvaluationBinding,
    Identifier,
    OptionalValue,
    ProcessingFailureCode,
    ReleaseBinding,
    ResourceLimits,
    SemanticVersion,
    SubjectBinding,
    TenantBinding,
    TimeBinding,
)


VECTOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "vectors"
    / "kernel"
    / "canonicalization-v1.json"
)


def limits(**overrides):
    values = {
        "version": CANONICALIZATION_VERSION,
        "maximum_input_bytes": 1_000_000,
        "maximum_collection_items": 1_000,
        "maximum_nesting_depth": 32,
        "maximum_canonical_bytes": 1_000_000,
        "maximum_work_units": 100_000,
    }
    values.update(overrides)
    return ResourceLimits(**values)


def canonical(value, *, governed_limits=None, input_byte_length=None):
    if input_byte_length is None:
        input_byte_length = len(repr(value).encode("utf-8"))

    return canonicalize(
        value,
        governed_limits or limits(),
        input_byte_length=input_byte_length,
    )


class CanonicalizationSemanticTests(unittest.TestCase):
    def test_mapping_order_is_deterministic(self):
        first = canonical({"b": 2, "a": 1})
        second = canonical({"a": 1, "b": 2})

        self.assertEqual(first, b'{"a":1,"b":2}')
        self.assertEqual(first, second)

    def test_unicode_is_nfc_normalized(self):
        decomposed = canonical({"text": "e\u0301"})
        composed = canonical({"text": "\u00e9"})

        self.assertEqual(decomposed, composed)

    def test_normalized_key_collision_fails(self):
        with self.assertRaises(ContractValidationError):
            canonical({"e\u0301": 1, "\u00e9": 2})

    def test_timestamp_normalizes_to_utc(self):
        utc_value = datetime(
            2026, 1, 2, 3, 4, 5, 123456, tzinfo=timezone.utc
        )
        offset_value = utc_value.astimezone(
            timezone(timedelta(hours=-7))
        )

        self.assertEqual(
            canonical({"time": utc_value}),
            canonical({"time": offset_value}),
        )

    def test_naive_timestamp_fails(self):
        with self.assertRaises(ContractValidationError):
            canonical({"time": datetime(2026, 1, 2, 3, 4, 5)})

    def test_missing_and_explicit_null_are_distinct(self):
        absent = canonical({})
        explicit_null = canonical({"value": None})

        self.assertEqual(absent, b"{}")
        self.assertEqual(explicit_null, b'{"value":null}')
        self.assertNotEqual(absent, explicit_null)

    def test_standalone_missing_fails(self):
        with self.assertRaises(ContractValidationError):
            canonical(OptionalValue.missing())

    def test_unsupported_float_fails(self):
        with self.assertRaises(ContractValidationError):
            canonical({"value": 1.5})

    def test_non_string_mapping_key_fails(self):
        with self.assertRaises(ContractValidationError):
            canonical({1: "value"})

    def test_input_byte_limit_fails_closed(self):
        with self.assertRaises(ContractValidationError):
            canonical(
                {"value": "small"},
                governed_limits=limits(maximum_input_bytes=4),
                input_byte_length=5,
            )

    def test_canonical_byte_limit_fails_closed(self):
        with self.assertRaises(ContractValidationError):
            canonical(
                {"value": "too-large"},
                governed_limits=limits(maximum_canonical_bytes=4),
            )

    def test_collection_limit_fails_closed(self):
        with self.assertRaises(ContractValidationError):
            canonical(
                [1, 2],
                governed_limits=limits(maximum_collection_items=1),
            )

    def test_nesting_limit_fails_closed(self):
        with self.assertRaises(ContractValidationError):
            canonical(
                {"outer": {"inner": {"value": 1}}},
                governed_limits=limits(maximum_nesting_depth=1),
            )

    def test_work_limit_fails_closed(self):
        with self.assertRaises(ContractValidationError):
            canonical(
                {"a": 1, "b": 2},
                governed_limits=limits(maximum_work_units=1),
            )


    def test_structured_processing_failure_is_preserved(self):
        with self.assertRaises(ContractValidationError) as captured:
            canonical({"value": 1.5})

        failure = captured.exception.failure

        self.assertEqual(
            failure.code,
            ProcessingFailureCode.INVALID_TYPE,
        )
        self.assertEqual(failure.field_path, "$.value")
        self.assertTrue(failure.detail)

    def test_canonicalization_version_mismatch_fails(self):
        mismatched_limits = limits(
            version=SemanticVersion("999.0.0")
        )

        with self.assertRaises(ContractValidationError) as captured:
            canonical(
                {"value": 1},
                governed_limits=mismatched_limits,
            )

        failure = captured.exception.failure

        self.assertEqual(
            failure.code,
            ProcessingFailureCode.INVALID_VERSION,
        )
        self.assertTrue(failure.field_path)
        self.assertTrue(failure.detail)

    def test_tenant_and_subject_wrapper_substitution_fails(self):
        tenant = TenantBinding(
            tenant_id=Identifier("tenant-a")
        )
        subject = SubjectBinding(
            subject_id=Identifier("subject-a"),
            subject_type=Identifier("service"),
        )
        environment = EnvironmentBinding(
            environment_id=Identifier("environment-a")
        )
        release = ReleaseBinding(
            release_id=Identifier("release-a")
        )
        instant = datetime(
            2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc
        )
        time_binding = TimeBinding(
            evaluated_at=instant,
            valid_from=instant,
            valid_until=instant,
        )

        common = {
            "invocation_id": Identifier("invocation-a"),
            "environment": environment,
            "release": release,
            "time": time_binding,
            "contract_version": SemanticVersion("1.0.0"),
            "canonicalization_version":
                CANONICALIZATION_VERSION,
            "fingerprint_version": SemanticVersion("1.0.0"),
        }

        with self.assertRaises(ContractValidationError) as tenant_error:
            EvaluationBinding(
                tenant=subject,
                subject=subject,
                **common,
            )

        self.assertEqual(
            tenant_error.exception.failure.code,
            ProcessingFailureCode.INVALID_TYPE,
        )
        self.assertTrue(
            tenant_error.exception.failure.field_path
        )

        with self.assertRaises(ContractValidationError) as subject_error:
            EvaluationBinding(
                tenant=tenant,
                subject=tenant,
                **common,
            )

        self.assertEqual(
            subject_error.exception.failure.code,
            ProcessingFailureCode.INVALID_TYPE,
        )
        self.assertTrue(
            subject_error.exception.failure.field_path
        )


class CanonicalizationVectorTests(unittest.TestCase):
    def test_static_vectors(self):
        document = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))

        self.assertEqual(
            document["canonicalization_version"],
            CANONICALIZATION_VERSION.value,
        )

        for vector in document["canonicalization_vectors"]:
            with self.subTest(vector=vector["name"]):
                actual = canonical(
                    vector["input"],
                    input_byte_length=vector["input_byte_length"],
                )
                self.assertEqual(
                    actual,
                    vector["canonical_utf8"].encode("utf-8"),
                )


    def test_negative_vectors(self):
        document = json.loads(
            VECTOR_PATH.read_text(encoding="utf-8")
        )

        handlers = {
            "unsupported-float": lambda vector: canonical(
                {"value": vector["value"]}
            ),
            "unsupported-version": lambda vector: canonical(
                {"value": 1},
                governed_limits=limits(
                    version=SemanticVersion(vector["version"])
                ),
            ),
        }

        for vector in document["negative_vectors"]:
            with self.subTest(vector=vector["name"]):
                with self.assertRaises(
                    ContractValidationError
                ) as captured:
                    handlers[vector["kind"]](vector)

                failure = captured.exception.failure

                self.assertEqual(
                    failure.code.value,
                    vector["failure_code"],
                )
                self.assertTrue(failure.field_path)
                self.assertTrue(failure.detail)

    def test_malformed_vector_fails_closed(self):
        document = json.loads(
            VECTOR_PATH.read_text(encoding="utf-8")
        )

        with self.assertRaises(json.JSONDecodeError):
            json.loads(document["malformed_vector"])


if __name__ == "__main__":
    unittest.main()
