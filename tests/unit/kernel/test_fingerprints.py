"""Deterministic fingerprint unit tests."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, fields
import json
from pathlib import Path
import re
import unittest

from afr.kernel.canonicalization import CANONICALIZATION_VERSION
from afr.kernel.contracts import (
    ContractValidationError,
    ProcessingFailureCode,
    ResourceLimits,
    SemanticVersion,
)
from afr.kernel.fingerprints import (
    FINGERPRINT_VERSION,
    compute_fingerprint,
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


def fingerprint(
    canonical_bytes,
    *,
    governed_limits=None,
    canonicalization_version=CANONICALIZATION_VERSION,
    fingerprint_version=FINGERPRINT_VERSION,
):
    return compute_fingerprint(
        canonical_bytes,
        governed_limits or limits(),
        canonicalization_version=canonicalization_version,
        fingerprint_version=fingerprint_version,
    )


def digest_text(value):
    for field in fields(value):
        candidate = getattr(value, field.name)
        if (
            isinstance(candidate, str)
            and re.fullmatch(r"[0-9a-f]{64}", candidate)
        ):
            return candidate

    raise AssertionError("Fingerprint has no lowercase SHA-256 field")


class FingerprintSemanticTests(unittest.TestCase):
    def test_identical_input_reproduces_exactly(self):
        canonical_bytes = b'{"a":1,"b":"stable"}'

        self.assertEqual(
            fingerprint(canonical_bytes),
            fingerprint(canonical_bytes),
        )

    def test_material_change_changes_digest(self):
        first = digest_text(fingerprint(b'{"a":1}'))
        second = digest_text(fingerprint(b'{"a":2}'))

        self.assertNotEqual(first, second)

    def test_digest_is_lowercase_sha256_hex(self):
        digest = digest_text(fingerprint(b'{"a":1}'))

        self.assertRegex(digest, r"^[0-9a-f]{64}$")

    def test_result_is_immutable(self):
        result = fingerprint(b'{"a":1}')
        field = fields(result)[0]

        with self.assertRaises(FrozenInstanceError):
            setattr(result, field.name, getattr(result, field.name))

    def test_non_bytes_input_fails(self):
        with self.assertRaises(ContractValidationError):
            fingerprint('{"a":1}')

    def test_empty_input_fails(self):
        with self.assertRaises(ContractValidationError):
            fingerprint(b"")

    def test_fingerprint_version_mismatch_fails(self):
        with self.assertRaises(ContractValidationError):
            fingerprint(
                b'{"a":1}',
                fingerprint_version=SemanticVersion("999.0.0"),
            )

    def test_canonicalization_version_mismatch_fails(self):
        with self.assertRaises(ContractValidationError):
            fingerprint(
                b'{"a":1}',
                canonicalization_version=SemanticVersion("999.0.0"),
            )

    def test_canonical_byte_limit_fails_closed(self):
        payload = b'{"value":"too-large"}'

        with self.assertRaises(ContractValidationError):
            fingerprint(
                payload,
                governed_limits=limits(
                    maximum_canonical_bytes=len(payload) - 1
                ),
            )

    def test_work_limit_fails_closed(self):
        with self.assertRaises(ContractValidationError):
            fingerprint(
                b'{"a":1}',
                governed_limits=limits(maximum_work_units=1),
            )


    def test_structured_failure_record_is_preserved(self):
        with self.assertRaises(ContractValidationError) as captured:
            fingerprint("not-bytes")

        failure = captured.exception.failure

        self.assertEqual(
            failure.code,
            ProcessingFailureCode.INVALID_TYPE,
        )
        self.assertTrue(failure.field_path)
        self.assertTrue(failure.detail)


class FingerprintVectorTests(unittest.TestCase):
    def test_frozen_protocol_vector(self):
        document = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
        vector = document["fingerprint_vector"]

        self.assertEqual(
            vector["canonicalization_version"],
            CANONICALIZATION_VERSION.value,
        )
        self.assertEqual(
            vector["fingerprint_version"],
            FINGERPRINT_VERSION.value,
        )

        actual = digest_text(
            fingerprint(vector["canonical_utf8"].encode("utf-8"))
        )

        self.assertEqual(actual, vector["sha256"])


if __name__ == "__main__":
    unittest.main()
