"""Deterministic Phase 12 S3 finding derivation over accepted S1/S2 state.

This module is pure construction logic. It consumes an accepted S1 evidence
foundation and one accepted S2 drift-evaluation result, validates their exact
identity/scope/version relationship, and emits one immutable deterministic
Phase 12 finding representation.

It performs no finding persistence or lifecycle mutation, certificate work,
Command Center work, provider/network I/O, NEXUS mutation, runtime action, or
authority grant.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum

from afr.conformance.drift_evaluation import (
    DRIFT_EVALUATION_CONTRACT_VERSION,
    DriftEvaluationResult,
    DriftState,
)
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
    OptionalValue,
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


FINDING_CONTRACT_VERSION = SemanticVersion("1.0.0")
ACCEPTED_S2_RESULT_STATUS = Identifier("ACCEPTED")


class FindingState(str, Enum):
    """Canonical Phase 12 finding-state vocabulary."""

    SUPPORTED = "SUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    STALE = "STALE"
    INCONCLUSIVE = "INCONCLUSIVE"
    EVIDENCE_UNAVAILABLE = "EVIDENCE_UNAVAILABLE"


@dataclass(frozen=True, slots=True)
class ConformanceFinding:
    """Exact immutable 25-field Phase 12 finding contract."""

    finding_contract_version: SemanticVersion
    finding_id: Identifier
    finding_state: FindingState
    tenant_id: Identifier
    subject_id: Identifier
    environment_id: Identifier
    release_id: Identifier
    architecture_truth_reference_id: Identifier
    claim_id: Identifier
    source_evaluation_cycle_id: Identifier
    source_evaluation_result_id: Identifier
    evidence_binding_or_set_id: Identifier
    finding_derivation_policy_id: Identifier
    finding_derivation_policy_version: SemanticVersion
    evaluator_id: Identifier
    evaluator_version: SemanticVersion
    canonicalization_version: SemanticVersion
    fingerprint_version: SemanticVersion
    trusted_time_context_id: Identifier
    finding_valid_from: datetime
    finding_valid_until: datetime
    limitations: tuple[Identifier, ...]
    unresolved_conditions: tuple[Identifier, ...]
    finding_fingerprint: Fingerprint
    supersedes_finding_id: OptionalValue[Identifier]


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


def _require_optional_identifier(
    value: object,
    field_path: str,
) -> OptionalValue[Identifier]:
    if not isinstance(value, OptionalValue):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be OptionalValue",
        )

    if (
        value.present
        and value.value is not None
        and not isinstance(value.value, Identifier)
    ):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            f"{field_path}.value",
            "must be Identifier when present and non-null",
        )

    return value


def _require_source_value(
    field_path: str,
    expected: object,
    actual: object,
    code: ProcessingFailureCode = ProcessingFailureCode.INVALID_IDENTIFIER,
) -> None:
    if actual != expected:
        _fail(
            code,
            field_path,
            "must equal the accepted S1/S2 source binding",
        )


def _validate_source_pair(
    foundation: EvidenceFoundationBinding,
    drift_result: DriftEvaluationResult,
    s2_result_status: Identifier,
) -> None:
    _require_instance(
        foundation,
        EvidenceFoundationBinding,
        "foundation",
    )
    _require_instance(
        drift_result,
        DriftEvaluationResult,
        "drift_result",
    )
    _require_instance(
        s2_result_status,
        Identifier,
        "s2_result_status",
    )

    if s2_result_status != ACCEPTED_S2_RESULT_STATUS:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "s2_result_status",
            "must equal ACCEPTED",
        )

    if foundation.foundation_contract_version != FOUNDATION_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "foundation.foundation_contract_version",
            "must equal FOUNDATION_CONTRACT_VERSION",
        )

    if drift_result.drift_contract_version != DRIFT_EVALUATION_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "drift_result.drift_contract_version",
            "must equal DRIFT_EVALUATION_CONTRACT_VERSION",
        )

    if foundation.source_evaluation_status != ACCEPTED_SOURCE_EVALUATION_STATUS:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "foundation.source_evaluation_status",
            "must equal ACCEPTED",
        )

    if not isinstance(drift_result.state, DriftState):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "drift_result.state",
            "must be DriftState",
        )

    _require_source_value(
        "drift_result.foundation_contract_version",
        foundation.foundation_contract_version,
        drift_result.foundation_contract_version,
        ProcessingFailureCode.INVALID_VERSION,
    )
    _require_source_value(
        "drift_result.foundation_fingerprint",
        foundation.fingerprint,
        drift_result.foundation_fingerprint,
    )
    _require_source_value(
        "drift_result.source_evaluation_cycle_id",
        foundation.source_evaluation_cycle_id,
        drift_result.source_evaluation_cycle_id,
    )
    _require_source_value(
        "drift_result.source_evaluation_result_id",
        foundation.source_evaluation_result_id,
        drift_result.source_evaluation_result_id,
    )
    _require_source_value(
        "drift_result.source_evaluation_status",
        foundation.source_evaluation_status,
        drift_result.source_evaluation_status,
    )
    _require_source_value(
        "drift_result.tenant_id",
        foundation.tenant_id,
        drift_result.tenant_id,
        ProcessingFailureCode.TENANT_BINDING_MISMATCH,
    )
    _require_source_value(
        "drift_result.subject_id",
        foundation.subject_id,
        drift_result.subject_id,
        ProcessingFailureCode.SUBJECT_BINDING_MISMATCH,
    )
    _require_source_value(
        "drift_result.architecture_truth_reference_id",
        foundation.architecture_truth_reference_id,
        drift_result.architecture_truth_reference_id,
    )
    _require_source_value(
        "drift_result.evidence_binding_or_set_id",
        foundation.evidence_binding_or_set_id,
        drift_result.evidence_binding_or_set_id,
    )
    _require_source_value(
        "drift_result.trusted_time_context_id",
        foundation.trusted_time_context_id,
        drift_result.trusted_time_context_id,
    )
    _require_source_value(
        "drift_result.canonicalization_version",
        foundation.canonicalization_version,
        drift_result.canonicalization_version,
        ProcessingFailureCode.INVALID_VERSION,
    )
    _require_source_value(
        "drift_result.fingerprint_version",
        foundation.fingerprint_version,
        drift_result.fingerprint_version,
        ProcessingFailureCode.INVALID_VERSION,
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


def _payload_from_finding(
    finding: ConformanceFinding,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "architecture_truth_reference_id":
            finding.architecture_truth_reference_id.value,
        "canonicalization_version":
            finding.canonicalization_version.value,
        "claim_id": finding.claim_id.value,
        "environment_id": finding.environment_id.value,
        "evaluator_id": finding.evaluator_id.value,
        "evaluator_version": finding.evaluator_version.value,
        "evidence_binding_or_set_id":
            finding.evidence_binding_or_set_id.value,
        "finding_contract_version":
            finding.finding_contract_version.value,
        "finding_derivation_policy_id":
            finding.finding_derivation_policy_id.value,
        "finding_derivation_policy_version":
            finding.finding_derivation_policy_version.value,
        "finding_id": finding.finding_id.value,
        "finding_state": finding.finding_state.value,
        "finding_valid_from": _utc_text(finding.finding_valid_from),
        "finding_valid_until": _utc_text(finding.finding_valid_until),
        "fingerprint_version": finding.fingerprint_version.value,
        "limitations": [item.value for item in finding.limitations],
        "release_id": finding.release_id.value,
        "source_evaluation_cycle_id":
            finding.source_evaluation_cycle_id.value,
        "source_evaluation_result_id":
            finding.source_evaluation_result_id.value,
        "subject_id": finding.subject_id.value,
        "tenant_id": finding.tenant_id.value,
        "trusted_time_context_id":
            finding.trusted_time_context_id.value,
        "unresolved_conditions": [
            item.value for item in finding.unresolved_conditions
        ],
    }

    supersedes = finding.supersedes_finding_id
    if supersedes.present:
        payload["supersedes_finding_id"] = (
            None
            if supersedes.value is None
            else supersedes.value.value
        )

    return payload


def canonical_finding_bytes(
    finding: ConformanceFinding,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> bytes:
    """Reproduce the canonical bytes bound by ``finding_fingerprint``."""

    _require_instance(finding, ConformanceFinding, "finding")
    _require_instance(resource_limits, ResourceLimits, "resource_limits")

    return canonicalize(
        _payload_from_finding(finding),
        resource_limits,
        input_byte_length=input_byte_length,
    )


def derive_finding(
    *,
    finding_contract_version: SemanticVersion,
    s2_result_status: Identifier,
    foundation: EvidenceFoundationBinding,
    drift_result: DriftEvaluationResult,
    finding_id: Identifier,
    tenant_id: Identifier,
    subject_id: Identifier,
    environment_id: Identifier,
    release_id: Identifier,
    claim_id: Identifier,
    finding_derivation_policy_id: Identifier,
    finding_derivation_policy_version: SemanticVersion,
    evaluator_id: Identifier,
    evaluator_version: SemanticVersion,
    finding_valid_from: datetime,
    finding_valid_until: datetime,
    limitations: tuple[Identifier, ...],
    unresolved_conditions: tuple[Identifier, ...],
    supersedes_finding_id: OptionalValue[Identifier],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> ConformanceFinding:
    """Derive one immutable deterministic Phase 12 finding."""

    required = (
        ("finding_contract_version", finding_contract_version, SemanticVersion),
        ("finding_id", finding_id, Identifier),
        ("tenant_id", tenant_id, Identifier),
        ("subject_id", subject_id, Identifier),
        ("environment_id", environment_id, Identifier),
        ("release_id", release_id, Identifier),
        ("claim_id", claim_id, Identifier),
        (
            "finding_derivation_policy_id",
            finding_derivation_policy_id,
            Identifier,
        ),
        (
            "finding_derivation_policy_version",
            finding_derivation_policy_version,
            SemanticVersion,
        ),
        ("evaluator_id", evaluator_id, Identifier),
        ("evaluator_version", evaluator_version, SemanticVersion),
        ("resource_limits", resource_limits, ResourceLimits),
    )

    for field_path, value, expected_type in required:
        _require_instance(value, expected_type, field_path)

    if finding_contract_version != FINDING_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "finding_contract_version",
            "must equal FINDING_CONTRACT_VERSION",
        )

    _validate_source_pair(
        foundation,
        drift_result,
        s2_result_status,
    )

    _require_source_value(
        "tenant_id",
        foundation.tenant_id,
        tenant_id,
        ProcessingFailureCode.TENANT_BINDING_MISMATCH,
    )
    _require_source_value(
        "subject_id",
        foundation.subject_id,
        subject_id,
        ProcessingFailureCode.SUBJECT_BINDING_MISMATCH,
    )
    _require_source_value(
        "environment_id",
        foundation.environment_id,
        environment_id,
    )
    _require_source_value(
        "release_id",
        foundation.release_id,
        release_id,
    )

    valid_from = _require_aware_datetime(
        finding_valid_from,
        "finding_valid_from",
    )
    valid_until = _require_aware_datetime(
        finding_valid_until,
        "finding_valid_until",
    )

    if valid_until < valid_from:
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "finding_valid_until",
            "must not precede finding_valid_from",
        )

    if valid_from < foundation.valid_from:
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "finding_valid_from",
            "must not precede the accepted foundation validity interval",
        )

    if valid_until > foundation.valid_until:
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "finding_valid_until",
            "must not exceed the accepted foundation validity interval",
        )

    normalized_limitations = _normalized_identifier_tuple(
        limitations,
        "limitations",
    )
    normalized_unresolved = _normalized_identifier_tuple(
        unresolved_conditions,
        "unresolved_conditions",
    )

    if not set(foundation.limitations).issubset(normalized_limitations):
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "limitations",
            "must preserve all accepted foundation limitations",
        )

    if not set(foundation.unresolved_conditions).issubset(
        normalized_unresolved
    ):
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "unresolved_conditions",
            "must preserve all accepted foundation unresolved conditions",
        )

    supersedes = _require_optional_identifier(
        supersedes_finding_id,
        "supersedes_finding_id",
    )

    if supersedes.present and supersedes.value == finding_id:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "supersedes_finding_id",
            "cannot equal finding_id",
        )

    finding_state = FindingState(drift_result.state.value)

    payload: dict[str, object] = {
        "architecture_truth_reference_id":
            foundation.architecture_truth_reference_id.value,
        "canonicalization_version":
            foundation.canonicalization_version.value,
        "claim_id": claim_id.value,
        "environment_id": environment_id.value,
        "evaluator_id": evaluator_id.value,
        "evaluator_version": evaluator_version.value,
        "evidence_binding_or_set_id":
            foundation.evidence_binding_or_set_id.value,
        "finding_contract_version": finding_contract_version.value,
        "finding_derivation_policy_id":
            finding_derivation_policy_id.value,
        "finding_derivation_policy_version":
            finding_derivation_policy_version.value,
        "finding_id": finding_id.value,
        "finding_state": finding_state.value,
        "finding_valid_from": _utc_text(valid_from),
        "finding_valid_until": _utc_text(valid_until),
        "fingerprint_version": foundation.fingerprint_version.value,
        "limitations": [item.value for item in normalized_limitations],
        "release_id": release_id.value,
        "source_evaluation_cycle_id":
            foundation.source_evaluation_cycle_id.value,
        "source_evaluation_result_id":
            foundation.source_evaluation_result_id.value,
        "subject_id": subject_id.value,
        "tenant_id": tenant_id.value,
        "trusted_time_context_id":
            foundation.trusted_time_context_id.value,
        "unresolved_conditions": [
            item.value for item in normalized_unresolved
        ],
    }

    if supersedes.present:
        payload["supersedes_finding_id"] = (
            None
            if supersedes.value is None
            else supersedes.value.value
        )

    canonical_bytes = canonicalize(
        payload,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=foundation.canonicalization_version,
        fingerprint_version=foundation.fingerprint_version,
    )

    return ConformanceFinding(
        finding_contract_version=finding_contract_version,
        finding_id=finding_id,
        finding_state=finding_state,
        tenant_id=tenant_id,
        subject_id=subject_id,
        environment_id=environment_id,
        release_id=release_id,
        architecture_truth_reference_id=
            foundation.architecture_truth_reference_id,
        claim_id=claim_id,
        source_evaluation_cycle_id=
            foundation.source_evaluation_cycle_id,
        source_evaluation_result_id=
            foundation.source_evaluation_result_id,
        evidence_binding_or_set_id=
            foundation.evidence_binding_or_set_id,
        finding_derivation_policy_id=
            finding_derivation_policy_id,
        finding_derivation_policy_version=
            finding_derivation_policy_version,
        evaluator_id=evaluator_id,
        evaluator_version=evaluator_version,
        canonicalization_version=foundation.canonicalization_version,
        fingerprint_version=foundation.fingerprint_version,
        trusted_time_context_id=foundation.trusted_time_context_id,
        finding_valid_from=valid_from,
        finding_valid_until=valid_until,
        limitations=normalized_limitations,
        unresolved_conditions=normalized_unresolved,
        finding_fingerprint=fingerprint,
        supersedes_finding_id=supersedes,
    )
