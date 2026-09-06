"""Deterministic fingerprints over accepted canonical bytes.

This module implements only bounded fingerprint construction. It performs no
evaluation, filesystem access, networking, persistence, integration,
deployment, certificate issuance, or runtime action.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re

from .canonicalization import CANONICALIZATION_VERSION
from .contracts import (
    ContractValidationError,
    ProcessingFailure,
    ProcessingFailureCode,
    ResourceLimits,
    SemanticVersion,
)


FINGERPRINT_VERSION = SemanticVersion("1.0.0")
FINGERPRINT_ALGORITHM = "sha256"
_FINGERPRINT_DOMAIN = b"AFR-DETERMINISTIC-KERNEL-FINGERPRINT"
_HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _fail(
    code: ProcessingFailureCode,
    field_path: str,
    detail: str,
) -> None:
    raise ContractValidationError(
        ProcessingFailure(
            code=code,
            field_path=field_path,
            detail=detail,
        )
    )


def _require_version(
    value: SemanticVersion,
    expected: SemanticVersion,
    field_path: str,
) -> None:
    if not isinstance(value, SemanticVersion):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "version must be SemanticVersion",
        )

    if value != expected:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            field_path,
            f"version must equal {expected.value}",
        )


def _update_frame_header(
    digest: object,
    label: bytes,
    value_length: int,
) -> None:
    """Stream a frame header while preserving its byte label exactly."""

    digest.update(len(label).to_bytes(4, "big"))
    digest.update(label)
    digest.update(value_length.to_bytes(8, "big"))


def _update_frame(
    digest: object,
    label: bytes,
    value: bytes,
) -> None:
    """Stream one bounded non-payload frame."""

    _update_frame_header(digest, label, len(value))
    digest.update(value)


@dataclass(frozen=True, slots=True)
class Fingerprint:
    """Immutable identity of one exact canonical byte sequence."""

    algorithm: str
    fingerprint_version: SemanticVersion
    canonicalization_version: SemanticVersion
    digest_hex: str

    def __post_init__(self) -> None:
        if not isinstance(self.algorithm, str):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "fingerprint.algorithm",
                "algorithm must be str",
            )

        if self.algorithm != FINGERPRINT_ALGORITHM:
            _fail(
                ProcessingFailureCode.INVALID_VERSION,
                "fingerprint.algorithm",
                f"algorithm must equal {FINGERPRINT_ALGORITHM}",
            )

        _require_version(
            self.fingerprint_version,
            FINGERPRINT_VERSION,
            "fingerprint.fingerprint_version",
        )

        _require_version(
            self.canonicalization_version,
            CANONICALIZATION_VERSION,
            "fingerprint.canonicalization_version",
        )

        if not isinstance(self.digest_hex, str):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "fingerprint.digest_hex",
                "digest must be str",
            )

        if _HEX_SHA256.fullmatch(self.digest_hex) is None:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "fingerprint.digest_hex",
                "digest must be exactly 64 lowercase hexadecimal characters",
            )


def compute_fingerprint(
    canonical_bytes: bytes,
    limits: ResourceLimits,
    *,
    canonicalization_version: SemanticVersion,
    fingerprint_version: SemanticVersion,
) -> Fingerprint:
    """Compute a domain-separated SHA-256 fingerprint.

    The caller must supply bytes produced by the independently accepted
    canonicalization contract. The fingerprint binds the algorithm domain,
    fingerprint version, canonicalization version, and exact canonical bytes.

    This function does not authorize or perform canonicalization, evaluation,
    persistence, integration, or any external side effect.
    """

    if not isinstance(canonical_bytes, bytes):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "canonical_bytes",
            "canonical input must be bytes",
        )

    if not canonical_bytes:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "canonical_bytes",
            "canonical input cannot be empty",
        )

    if not isinstance(limits, ResourceLimits):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "limits",
            "limits must be ResourceLimits",
        )

    _require_version(
        canonicalization_version,
        CANONICALIZATION_VERSION,
        "canonicalization_version",
    )

    _require_version(
        fingerprint_version,
        FINGERPRINT_VERSION,
        "fingerprint_version",
    )

    if limits.version != canonicalization_version:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "limits.version",
            "resource-limit version must equal canonicalization version",
        )

    if len(canonical_bytes) > limits.maximum_canonical_bytes:
        _fail(
            ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
            "canonical_bytes",
            "canonical input exceeds maximum canonical byte size",
        )

    if len(canonical_bytes) > limits.maximum_work_units:
        _fail(
            ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
            "canonical_bytes",
            "fingerprint work exceeds deterministic work-unit bound",
        )

    digest = hashlib.sha256()
    _update_frame(digest, b"domain", _FINGERPRINT_DOMAIN)
    _update_frame(digest, b"algorithm", FINGERPRINT_ALGORITHM.encode("ascii"))
    _update_frame(digest, b"fingerprint-version", fingerprint_version.value.encode("ascii"))
    _update_frame(digest, b"canonicalization-version", canonicalization_version.value.encode("ascii"))
    _update_frame_header(
        digest,
        b"canonical-bytes",
        len(canonical_bytes),
    )
    digest.update(canonical_bytes)
    digest_hex = digest.hexdigest()

    return Fingerprint(
        algorithm=FINGERPRINT_ALGORITHM,
        fingerprint_version=fingerprint_version,
        canonicalization_version=canonicalization_version,
        digest_hex=digest_hex,
    )
