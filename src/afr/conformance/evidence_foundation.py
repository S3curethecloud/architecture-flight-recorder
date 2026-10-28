"""Deterministic Phase 12 S1 trust, provenance, and shared-evidence binding.

This module is pure construction logic. It accepts already-qualified Phase 11
identity and binding objects supplied by the caller, validates exact scope and
version relationships, produces canonical bytes with the accepted AFR kernel,
and binds those bytes to the accepted AFR fingerprint algorithm.

It grants no finding, drift, certificate, presentation, persistence, provider,
network, runtime, or authority effect.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from afr.kernel.canonicalization import (
    CANONICALIZATION_VERSION,
    canonicalize,
)
from afr.kernel.contracts import (
    ContractValidationError,
    EvaluationBinding,
    Identifier,
    OptionalValue,
    ProcessingFailure,
    ProcessingFailureCode,
    ProvenanceBinding,
    ResourceLimits,
    SemanticVersion,
)
from afr.kernel.fingerprints import (
    FINGERPRINT_VERSION,
    Fingerprint,
    compute_fingerprint,
)


FOUNDATION_CONTRACT_VERSION = SemanticVersion("1.0.0")
ACCEPTED_SOURCE_EVALUATION_STATUS = Identifier("ACCEPTED")


@dataclass(frozen=True, slots=True)
class EvidenceFoundationBinding:
    """Immutable shared source binding for later Phase 12 slices."""

    foundation_contract_version: SemanticVersion
    source_evaluation_cycle_id: Identifier
    source_evaluation_result_id: Identifier
    source_evaluation_status: Identifier
    tenant_id: Identifier
    subject_id: Identifier
    subject_type: Identifier
    environment_id: Identifier
    release_id: Identifier
    architecture_truth_reference_id: Identifier
    evidence_binding_or_set_id: Identifier
    trusted_time_context_id: Identifier
    evaluation_contract_version: SemanticVersion
    provenance: ProvenanceBinding
    evaluated_at: datetime
    valid_from: datetime
    valid_until: datetime
    limitations: tuple[Identifier, ...]
    unresolved_conditions: tuple[Identifier, ...]
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


def _normalized_identifier_tuple(
    value: tuple[Identifier, ...],
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


def _utc_text(value: datetime) -> str:
    rendered = value.astimezone(timezone.utc)

    if rendered.microsecond:
        return rendered.isoformat(
            timespec="microseconds"
        ).replace("+00:00", "Z")

    return rendered.isoformat(
        timespec="seconds"
    ).replace("+00:00", "Z")


def _provenance_payload(
    provenance: ProvenanceBinding,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "collector_id": provenance.collector_id.value,
        "observed_at": _utc_text(provenance.observed_at),
        "source_id": provenance.source_id.value,
    }

    integrity = provenance.integrity_reference

    if integrity.present:
        payload["integrity_reference"] = (
            None
            if integrity.value is None
            else integrity.value.value
        )

    return payload


def build_evidence_foundation(
    *,
    foundation_contract_version: SemanticVersion,
    source_evaluation_cycle_id: Identifier,
    source_evaluation_result_id: Identifier,
    source_evaluation_status: Identifier,
    tenant_id: Identifier,
    subject_id: Identifier,
    architecture_truth_reference_id: Identifier,
    evidence_binding_or_set_id: Identifier,
    trusted_time_context_id: Identifier,
    evaluation_binding: EvaluationBinding,
    provenance: ProvenanceBinding,
    limitations: tuple[Identifier, ...],
    unresolved_conditions: tuple[Identifier, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> EvidenceFoundationBinding:
    """Build one immutable S1 shared-evidence foundation binding."""

    required = (
        ("foundation_contract_version", foundation_contract_version, SemanticVersion),
        ("source_evaluation_cycle_id", source_evaluation_cycle_id, Identifier),
        ("source_evaluation_result_id", source_evaluation_result_id, Identifier),
        ("source_evaluation_status", source_evaluation_status, Identifier),
        ("tenant_id", tenant_id, Identifier),
        ("subject_id", subject_id, Identifier),
        (
            "architecture_truth_reference_id",
            architecture_truth_reference_id,
            Identifier,
        ),
        (
            "evidence_binding_or_set_id",
            evidence_binding_or_set_id,
            Identifier,
        ),
        (
            "trusted_time_context_id",
            trusted_time_context_id,
            Identifier,
        ),
        ("evaluation_binding", evaluation_binding, EvaluationBinding),
        ("provenance", provenance, ProvenanceBinding),
        ("resource_limits", resource_limits, ResourceLimits),
    )

    for field_path, value, expected_type in required:
        _require_instance(value, expected_type, field_path)

    if foundation_contract_version != FOUNDATION_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "foundation_contract_version",
            "must equal FOUNDATION_CONTRACT_VERSION",
        )

    if source_evaluation_status != ACCEPTED_SOURCE_EVALUATION_STATUS:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "source_evaluation_status",
            "must equal ACCEPTED",
        )

    if tenant_id != evaluation_binding.tenant.tenant_id:
        _fail(
            ProcessingFailureCode.TENANT_BINDING_MISMATCH,
            "tenant_id",
            "must equal evaluation_binding.tenant.tenant_id",
        )

    if subject_id != evaluation_binding.subject.subject_id:
        _fail(
            ProcessingFailureCode.SUBJECT_BINDING_MISMATCH,
            "subject_id",
            "must equal evaluation_binding.subject.subject_id",
        )

    if (
        evaluation_binding.canonicalization_version
        != CANONICALIZATION_VERSION
    ):
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "evaluation_binding.canonicalization_version",
            "must equal CANONICALIZATION_VERSION",
        )

    if evaluation_binding.fingerprint_version != FINGERPRINT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "evaluation_binding.fingerprint_version",
            "must equal FINGERPRINT_VERSION",
        )

    normalized_limitations = _normalized_identifier_tuple(
        limitations,
        "limitations",
    )
    normalized_unresolved = _normalized_identifier_tuple(
        unresolved_conditions,
        "unresolved_conditions",
    )

    time = evaluation_binding.time
    subject = evaluation_binding.subject

    payload: dict[str, object] = {
        "architecture_truth_reference_id":
            architecture_truth_reference_id.value,
        "canonicalization_version":
            evaluation_binding.canonicalization_version.value,
        "environment_id":
            evaluation_binding.environment.environment_id.value,
        "evaluated_at": _utc_text(time.evaluated_at),
        "evaluation_contract_version":
            evaluation_binding.contract_version.value,
        "evidence_binding_or_set_id":
            evidence_binding_or_set_id.value,
        "fingerprint_version":
            evaluation_binding.fingerprint_version.value,
        "foundation_contract_version":
            foundation_contract_version.value,
        "limitations":
            [item.value for item in normalized_limitations],
        "provenance": _provenance_payload(provenance),
        "release_id":
            evaluation_binding.release.release_id.value,
        "source_evaluation_cycle_id":
            source_evaluation_cycle_id.value,
        "source_evaluation_result_id":
            source_evaluation_result_id.value,
        "source_evaluation_status":
            source_evaluation_status.value,
        "subject_id": subject_id.value,
        "subject_type": subject.subject_type.value,
        "tenant_id": tenant_id.value,
        "trusted_time_context_id":
            trusted_time_context_id.value,
        "unresolved_conditions":
            [item.value for item in normalized_unresolved],
        "valid_from": _utc_text(time.valid_from),
        "valid_until": _utc_text(time.valid_until),
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
            evaluation_binding.canonicalization_version,
        fingerprint_version=
            evaluation_binding.fingerprint_version,
    )

    return EvidenceFoundationBinding(
        foundation_contract_version=foundation_contract_version,
        source_evaluation_cycle_id=source_evaluation_cycle_id,
        source_evaluation_result_id=source_evaluation_result_id,
        source_evaluation_status=source_evaluation_status,
        tenant_id=tenant_id,
        subject_id=subject_id,
        subject_type=subject.subject_type,
        environment_id=
            evaluation_binding.environment.environment_id,
        release_id=evaluation_binding.release.release_id,
        architecture_truth_reference_id=
            architecture_truth_reference_id,
        evidence_binding_or_set_id=evidence_binding_or_set_id,
        trusted_time_context_id=trusted_time_context_id,
        evaluation_contract_version=
            evaluation_binding.contract_version,
        provenance=provenance,
        evaluated_at=time.evaluated_at,
        valid_from=time.valid_from,
        valid_until=time.valid_until,
        limitations=normalized_limitations,
        unresolved_conditions=normalized_unresolved,
        canonicalization_version=
            evaluation_binding.canonicalization_version,
        fingerprint_version=
            evaluation_binding.fingerprint_version,
        canonical_bytes=canonical_bytes,
        fingerprint=fingerprint,
    )
