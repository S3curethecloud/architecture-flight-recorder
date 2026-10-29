"""Deterministic Phase 12 S2 drift evaluation over qualified S1 evidence.

This module is pure evaluation logic. It consumes an accepted S1
EvidenceFoundationBinding plus caller-supplied comparison inputs, trusted
evaluation time, and freshness policy. It emits one immutable deterministic
evaluation result using only the canonical Phase 12 state vocabulary:

SUPPORTED / CONTRADICTED / STALE / INCONCLUSIVE / EVIDENCE_UNAVAILABLE.

It creates no findings, certificates, Command Center writes, provider effects,
runtime authority, architecture acceptance, or execution authority.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum

from afr.conformance.evidence_foundation import (
    ACCEPTED_SOURCE_EVALUATION_STATUS,
    FOUNDATION_CONTRACT_VERSION,
    EvidenceFoundationBinding,
)
from afr.kernel.canonicalization import (
    CANONICALIZATION_VERSION,
    canonicalize,
)
from afr.kernel.contracts import (
    ContractValidationError,
    Identifier,
    ProcessingFailure,
    ProcessingFailureCode,
    ResourceLimits,
    SemanticVersion,
)
from afr.kernel.fingerprints import (
    FINGERPRINT_VERSION,
    Fingerprint,
    compute_fingerprint,
)


DRIFT_EVALUATION_CONTRACT_VERSION = SemanticVersion("1.0.0")


class DriftState(str, Enum):
    """Canonical Phase 12 S2 drift-evaluation state vocabulary."""

    SUPPORTED = "SUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    STALE = "STALE"
    INCONCLUSIVE = "INCONCLUSIVE"
    EVIDENCE_UNAVAILABLE = "EVIDENCE_UNAVAILABLE"


_STATE_REASON = {
    DriftState.SUPPORTED: Identifier("reason.s2.supported"),
    DriftState.CONTRADICTED: Identifier("reason.s2.contradicted"),
    DriftState.STALE: Identifier("reason.s2.stale"),
    DriftState.INCONCLUSIVE: Identifier("reason.s2.inconclusive"),
    DriftState.EVIDENCE_UNAVAILABLE:
        Identifier("reason.s2.evidence-unavailable"),
}


@dataclass(frozen=True, slots=True)
class DriftEvaluationResult:
    """Immutable deterministic S2 evaluation result."""

    drift_contract_version: SemanticVersion
    state: DriftState
    reason_codes: tuple[Identifier, ...]
    evidence_references: tuple[Identifier, ...]

    foundation_contract_version: SemanticVersion
    foundation_fingerprint: Fingerprint
    source_evaluation_cycle_id: Identifier
    source_evaluation_result_id: Identifier
    source_evaluation_status: Identifier
    tenant_id: Identifier
    subject_id: Identifier
    architecture_truth_reference_id: Identifier
    evidence_binding_or_set_id: Identifier
    trusted_time_context_id: Identifier

    expected_value: str
    evidence_available: bool
    evidence_conclusive: bool
    evidence_value: str | None
    evidence_observed_at: datetime | None
    trusted_evaluation_time: datetime
    freshness_bound_seconds: int

    canonicalization_version: SemanticVersion
    fingerprint_version: SemanticVersion
    canonical_bytes: bytes
    fingerprint: Fingerprint


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


def _require_instance(
    value: object,
    expected_type: type,
    field_path: str,
) -> None:
    if not isinstance(value, expected_type):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            f"must be {expected_type.__name__}",
        )


def _require_nonempty_text(
    value: object,
    field_path: str,
) -> str:
    if not isinstance(value, str):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be str",
        )

    if not value:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            field_path,
            "must not be empty",
        )

    return value


def _require_aware_datetime(
    value: object,
    field_path: str,
) -> datetime:
    if not isinstance(value, datetime):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be datetime",
        )

    if value.tzinfo is None or value.utcoffset() is None:
        _fail(
            ProcessingFailureCode.INVALID_TIMESTAMP,
            field_path,
            "must be timezone-aware",
        )

    return value


def _utc_text(value: datetime) -> str:
    rendered = value.astimezone(timezone.utc)

    if rendered.microsecond:
        return rendered.isoformat(
            timespec="microseconds"
        ).replace("+00:00", "Z")

    return rendered.isoformat(
        timespec="seconds"
    ).replace("+00:00", "Z")


def _normalized_identifier_tuple(
    value: object,
    field_path: str,
) -> tuple[Identifier, ...]:
    if not isinstance(value, tuple):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be a tuple of Identifier values",
        )

    if not value:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            field_path,
            "must contain at least one Identifier",
        )

    for index, item in enumerate(value):
        if not isinstance(item, Identifier):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                f"{field_path}[{index}]",
                "must be Identifier",
            )

    ordered = tuple(sorted(value, key=lambda item: item.value))

    if len({item.value for item in ordered}) != len(ordered):
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            field_path,
            "duplicate identifiers are prohibited",
        )

    return ordered


def _foundation_payload(
    foundation: EvidenceFoundationBinding,
) -> dict[str, object]:
    provenance = foundation.provenance
    integrity = provenance.integrity_reference

    return {
        "architecture_truth_reference_id":
            foundation.architecture_truth_reference_id.value,
        "evidence_binding_or_set_id":
            foundation.evidence_binding_or_set_id.value,
        "foundation_contract_version":
            foundation.foundation_contract_version.value,
        "foundation_fingerprint_digest_hex":
            foundation.fingerprint.digest_hex,
        "foundation_fingerprint_algorithm":
            foundation.fingerprint.algorithm,
        "provenance": {
            "collector_id": provenance.collector_id.value,
            "integrity_reference":
                None
                if not integrity.present or integrity.value is None
                else integrity.value.value,
            "observed_at": _utc_text(provenance.observed_at),
            "source_id": provenance.source_id.value,
        },
        "source_evaluation_cycle_id":
            foundation.source_evaluation_cycle_id.value,
        "source_evaluation_result_id":
            foundation.source_evaluation_result_id.value,
        "source_evaluation_status":
            foundation.source_evaluation_status.value,
        "subject_id": foundation.subject_id.value,
        "tenant_id": foundation.tenant_id.value,
        "trusted_time_context_id":
            foundation.trusted_time_context_id.value,
    }


def _classify(
    *,
    expected_value: str,
    evidence_available: bool,
    evidence_conclusive: bool,
    evidence_value: str | None,
    evidence_observed_at: datetime | None,
    trusted_evaluation_time: datetime,
    freshness_bound_seconds: int,
) -> DriftState:
    if not evidence_available:
        if (
            evidence_conclusive
            or evidence_value is not None
            or evidence_observed_at is not None
        ):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "evidence_available",
                "unavailable evidence must not carry value, timestamp, "
                "or conclusive state",
            )

        return DriftState.EVIDENCE_UNAVAILABLE

    if evidence_observed_at is None:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "evidence_observed_at",
            "available evidence requires an observation timestamp",
        )

    observed = _require_aware_datetime(
        evidence_observed_at,
        "evidence_observed_at",
    )

    actual_value = _require_nonempty_text(
        evidence_value,
        "evidence_value",
    )

    if observed > trusted_evaluation_time:
        _fail(
            ProcessingFailureCode.INVALID_TIMESTAMP,
            "evidence_observed_at",
            "must not be later than trusted_evaluation_time",
        )

    age_seconds = (
        trusted_evaluation_time - observed
    ).total_seconds()

    if age_seconds > freshness_bound_seconds:
        return DriftState.STALE

    if not evidence_conclusive:
        return DriftState.INCONCLUSIVE

    if actual_value == expected_value:
        return DriftState.SUPPORTED

    return DriftState.CONTRADICTED


def evaluate_drift(
    *,
    drift_contract_version: SemanticVersion,
    foundation: EvidenceFoundationBinding,
    expected_value: str,
    evidence_available: bool,
    evidence_conclusive: bool,
    evidence_value: str | None,
    evidence_observed_at: datetime | None,
    trusted_evaluation_time: datetime,
    freshness_bound_seconds: int,
    evidence_references: tuple[Identifier, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> DriftEvaluationResult:
    """Evaluate one deterministic S2 drift result."""

    _require_instance(
        drift_contract_version,
        SemanticVersion,
        "drift_contract_version",
    )
    _require_instance(
        foundation,
        EvidenceFoundationBinding,
        "foundation",
    )
    _require_instance(
        resource_limits,
        ResourceLimits,
        "resource_limits",
    )

    if drift_contract_version != DRIFT_EVALUATION_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "drift_contract_version",
            "must equal DRIFT_EVALUATION_CONTRACT_VERSION",
        )

    if foundation.foundation_contract_version != FOUNDATION_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "foundation.foundation_contract_version",
            "must equal FOUNDATION_CONTRACT_VERSION",
        )

    if (
        foundation.source_evaluation_status
        != ACCEPTED_SOURCE_EVALUATION_STATUS
    ):
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "foundation.source_evaluation_status",
            "must equal ACCEPTED",
        )

    if foundation.canonicalization_version != CANONICALIZATION_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "foundation.canonicalization_version",
            "must equal CANONICALIZATION_VERSION",
        )

    if foundation.fingerprint_version != FINGERPRINT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "foundation.fingerprint_version",
            "must equal FINGERPRINT_VERSION",
        )

    expected = _require_nonempty_text(
        expected_value,
        "expected_value",
    )

    if not isinstance(evidence_available, bool):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "evidence_available",
            "must be bool",
        )

    if not isinstance(evidence_conclusive, bool):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "evidence_conclusive",
            "must be bool",
        )

    trusted_time = _require_aware_datetime(
        trusted_evaluation_time,
        "trusted_evaluation_time",
    )

    if (
        isinstance(freshness_bound_seconds, bool)
        or not isinstance(freshness_bound_seconds, int)
        or freshness_bound_seconds < 0
    ):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "freshness_bound_seconds",
            "must be a non-negative integer",
        )

    references = _normalized_identifier_tuple(
        evidence_references,
        "evidence_references",
    )

    state = _classify(
        expected_value=expected,
        evidence_available=evidence_available,
        evidence_conclusive=evidence_conclusive,
        evidence_value=evidence_value,
        evidence_observed_at=evidence_observed_at,
        trusted_evaluation_time=trusted_time,
        freshness_bound_seconds=freshness_bound_seconds,
    )

    reasons = (_STATE_REASON[state],)

    payload: dict[str, object] = {
        "canonicalization_version":
            foundation.canonicalization_version.value,
        "comparison": {
            "evidence_available": evidence_available,
            "evidence_conclusive": evidence_conclusive,
            "evidence_value": evidence_value,
            "expected_value": expected,
        },
        "drift_contract_version":
            drift_contract_version.value,
        "evidence_references":
            [item.value for item in references],
        "foundation": _foundation_payload(foundation),
        "freshness": {
            "evidence_observed_at":
                None
                if evidence_observed_at is None
                else _utc_text(evidence_observed_at),
            "freshness_bound_seconds": freshness_bound_seconds,
            "trusted_evaluation_time":
                _utc_text(trusted_time),
        },
        "fingerprint_version":
            foundation.fingerprint_version.value,
        "reason_codes":
            [item.value for item in reasons],
        "state": state.value,
    }

    canonical_bytes = canonicalize(
        payload,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=
            foundation.canonicalization_version,
        fingerprint_version=
            foundation.fingerprint_version,
    )

    return DriftEvaluationResult(
        drift_contract_version=drift_contract_version,
        state=state,
        reason_codes=reasons,
        evidence_references=references,
        foundation_contract_version=
            foundation.foundation_contract_version,
        foundation_fingerprint=foundation.fingerprint,
        source_evaluation_cycle_id=
            foundation.source_evaluation_cycle_id,
        source_evaluation_result_id=
            foundation.source_evaluation_result_id,
        source_evaluation_status=
            foundation.source_evaluation_status,
        tenant_id=foundation.tenant_id,
        subject_id=foundation.subject_id,
        architecture_truth_reference_id=
            foundation.architecture_truth_reference_id,
        evidence_binding_or_set_id=
            foundation.evidence_binding_or_set_id,
        trusted_time_context_id=
            foundation.trusted_time_context_id,
        expected_value=expected,
        evidence_available=evidence_available,
        evidence_conclusive=evidence_conclusive,
        evidence_value=evidence_value,
        evidence_observed_at=evidence_observed_at,
        trusted_evaluation_time=trusted_time,
        freshness_bound_seconds=freshness_bound_seconds,
        canonicalization_version=
            foundation.canonicalization_version,
        fingerprint_version=
            foundation.fingerprint_version,
        canonical_bytes=canonical_bytes,
        fingerprint=fingerprint,
    )
