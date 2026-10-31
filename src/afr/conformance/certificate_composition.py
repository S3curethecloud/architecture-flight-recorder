"""Deterministic Phase 12 S4 conformance-certificate composition.

This module composes immutable certificate content from an accepted Phase 12
S3 finding set under an exact bounded scope and validity policy. Composition is
pure deterministic construction. It performs no signing, issuance, publication,
delivery, revocation, persistence, provider/network I/O, Command Center work,
NEXUS mutation, runtime action, or authority grant.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from afr.conformance.finding_derivation import (
    FINDING_CONTRACT_VERSION,
    ConformanceFinding,
    FindingState,
    canonical_finding_bytes,
)
from afr.kernel.canonicalization import CANONICALIZATION_VERSION, canonicalize
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


CERTIFICATE_CONTRACT_VERSION = SemanticVersion("1.0.0")
ACCEPTED_S3_FINDING_SET_STATUS = Identifier("ACCEPTED")
ISSUANCE_AUTHORITY_NOT_AUTHORIZED = Identifier("NOT_AUTHORIZED")


@dataclass(frozen=True, slots=True)
class ConformanceCertificateContent:
    """Exact immutable 19-field Phase 12 certificate-content contract."""

    certificate_contract_version: SemanticVersion
    certificate_content_id: Identifier
    tenant_id: Identifier
    subject_id: Identifier
    scope_id: Identifier
    architecture_truth_reference_id: Identifier
    finding_set_id: Identifier
    source_evaluation_set_id: Identifier
    evidence_set_id: Identifier
    conformance_policy_id: Identifier
    conformance_policy_version: SemanticVersion
    canonicalization_version: SemanticVersion
    fingerprint_version: SemanticVersion
    valid_from: datetime
    valid_until: datetime
    limitations: tuple[Identifier, ...]
    unresolved_conditions: tuple[Identifier, ...]
    certificate_content_fingerprint: Fingerprint
    issuance_authority_state: Identifier


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


def _require_aware_datetime(value: object, field_path: str) -> datetime:
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
        return rendered.isoformat(timespec="microseconds").replace(
            "+00:00", "Z"
        )
    return rendered.isoformat(timespec="seconds").replace("+00:00", "Z")


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


def _merge_identifier_tuples(
    inherited: tuple[Identifier, ...],
    additional: tuple[Identifier, ...],
    field_path: str,
) -> tuple[Identifier, ...]:
    combined = tuple(inherited) + tuple(additional)
    for index, item in enumerate(combined):
        if not isinstance(item, Identifier):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                f"{field_path}[{index}]",
                "must be Identifier",
            )
    return tuple(
        Identifier(value)
        for value in sorted({item.value for item in combined})
    )


def _derive_identifier(
    namespace: str,
    payload: object,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> Identifier:
    canonical_bytes = canonicalize(
        payload,
        resource_limits,
        input_byte_length=input_byte_length,
    )
    fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )
    return Identifier(f"{namespace}.{fingerprint.digest_hex}")


def _certificate_payload(
    certificate: ConformanceCertificateContent,
) -> dict[str, object]:
    return {
        "architecture_truth_reference_id":
            certificate.architecture_truth_reference_id.value,
        "canonicalization_version": certificate.canonicalization_version.value,
        "certificate_content_id": certificate.certificate_content_id.value,
        "certificate_contract_version":
            certificate.certificate_contract_version.value,
        "conformance_policy_id": certificate.conformance_policy_id.value,
        "conformance_policy_version":
            certificate.conformance_policy_version.value,
        "evidence_set_id": certificate.evidence_set_id.value,
        "finding_set_id": certificate.finding_set_id.value,
        "fingerprint_version": certificate.fingerprint_version.value,
        "issuance_authority_state": certificate.issuance_authority_state.value,
        "limitations": [item.value for item in certificate.limitations],
        "scope_id": certificate.scope_id.value,
        "source_evaluation_set_id": certificate.source_evaluation_set_id.value,
        "subject_id": certificate.subject_id.value,
        "tenant_id": certificate.tenant_id.value,
        "unresolved_conditions": [
            item.value for item in certificate.unresolved_conditions
        ],
        "valid_from": _utc_text(certificate.valid_from),
        "valid_until": _utc_text(certificate.valid_until),
    }


def canonical_certificate_bytes(
    certificate: ConformanceCertificateContent,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> bytes:
    """Reproduce the canonical bytes bound by certificate content fingerprint."""

    _require_instance(
        certificate,
        ConformanceCertificateContent,
        "certificate",
    )
    _require_instance(resource_limits, ResourceLimits, "resource_limits")
    return canonicalize(
        _certificate_payload(certificate),
        resource_limits,
        input_byte_length=input_byte_length,
    )


def _validate_findings(
    findings: object,
    finding_set_status: Identifier,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> tuple[ConformanceFinding, ...]:
    if not isinstance(findings, tuple):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "findings",
            "must be a tuple of ConformanceFinding values",
        )
    if not findings:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "findings",
            "accepted finding set cannot be empty",
        )
    _require_instance(finding_set_status, Identifier, "finding_set_status")
    if finding_set_status != ACCEPTED_S3_FINDING_SET_STATUS:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "finding_set_status",
            "must equal ACCEPTED",
        )

    ordered = tuple(
        sorted(
            findings,
            key=lambda finding: (
                finding.finding_id.value
                if isinstance(finding, ConformanceFinding)
                else ""
            ),
        )
    )
    observed_ids: set[str] = set()

    for index, finding in enumerate(ordered):
        if not isinstance(finding, ConformanceFinding):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                f"findings[{index}]",
                "must be ConformanceFinding",
            )
        if finding.finding_contract_version != FINDING_CONTRACT_VERSION:
            _fail(
                ProcessingFailureCode.INVALID_VERSION,
                f"findings[{index}].finding_contract_version",
                "must equal FINDING_CONTRACT_VERSION",
            )
        if finding.canonicalization_version != CANONICALIZATION_VERSION:
            _fail(
                ProcessingFailureCode.INVALID_VERSION,
                f"findings[{index}].canonicalization_version",
                "must equal CANONICALIZATION_VERSION",
            )
        if finding.fingerprint_version != FINGERPRINT_VERSION:
            _fail(
                ProcessingFailureCode.INVALID_VERSION,
                f"findings[{index}].fingerprint_version",
                "must equal FINGERPRINT_VERSION",
            )
        if finding.finding_id.value in observed_ids:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "findings",
                "duplicate finding_id values are prohibited",
            )
        observed_ids.add(finding.finding_id.value)

        canonical_bytes = canonical_finding_bytes(
            finding,
            resource_limits,
            input_byte_length=input_byte_length,
        )
        expected_fingerprint = compute_fingerprint(
            canonical_bytes,
            resource_limits,
            canonicalization_version=CANONICALIZATION_VERSION,
            fingerprint_version=FINGERPRINT_VERSION,
        )
        if expected_fingerprint != finding.finding_fingerprint:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                f"findings[{index}].finding_fingerprint",
                "must match deterministic canonical finding content",
            )

    first = ordered[0]
    common_fields = (
        "tenant_id",
        "subject_id",
        "environment_id",
        "release_id",
        "architecture_truth_reference_id",
        "trusted_time_context_id",
    )
    for field_name in common_fields:
        expected = getattr(first, field_name)
        for index, finding in enumerate(ordered[1:], start=1):
            if getattr(finding, field_name) != expected:
                code = ProcessingFailureCode.INVALID_IDENTIFIER
                if field_name == "tenant_id":
                    code = ProcessingFailureCode.TENANT_BINDING_MISMATCH
                elif field_name == "subject_id":
                    code = ProcessingFailureCode.SUBJECT_BINDING_MISMATCH
                _fail(
                    code,
                    f"findings[{index}].{field_name}",
                    "all findings must share one compatible certificate scope",
                )
    return ordered


def compose_certificate(
    *,
    certificate_contract_version: SemanticVersion,
    finding_set_status: Identifier,
    findings: tuple[ConformanceFinding, ...],
    scope_id: Identifier,
    accepted_scope_id: Identifier,
    conformance_policy_id: Identifier,
    conformance_policy_version: SemanticVersion,
    valid_from: datetime,
    valid_until: datetime,
    trusted_evaluation_time: datetime,
    additional_limitations: tuple[Identifier, ...],
    additional_unresolved_conditions: tuple[Identifier, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> ConformanceCertificateContent:
    """Compose one immutable deterministic Phase 12 certificate representation."""

    required = (
        ("certificate_contract_version", certificate_contract_version, SemanticVersion),
        ("scope_id", scope_id, Identifier),
        ("accepted_scope_id", accepted_scope_id, Identifier),
        ("conformance_policy_id", conformance_policy_id, Identifier),
        (
            "conformance_policy_version",
            conformance_policy_version,
            SemanticVersion,
        ),
        ("resource_limits", resource_limits, ResourceLimits),
    )
    for field_path, value, expected_type in required:
        _require_instance(value, expected_type, field_path)

    if certificate_contract_version != CERTIFICATE_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "certificate_contract_version",
            "must equal CERTIFICATE_CONTRACT_VERSION",
        )
    if resource_limits.version != CANONICALIZATION_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "resource_limits.version",
            "must equal CANONICALIZATION_VERSION",
        )
    if scope_id != accepted_scope_id:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "scope_id",
            "certificate scope cannot exceed the accepted finding scope",
        )

    ordered_findings = _validate_findings(
        findings,
        finding_set_status,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    requested_from = _require_aware_datetime(valid_from, "valid_from")
    requested_until = _require_aware_datetime(valid_until, "valid_until")
    trusted_time = _require_aware_datetime(
        trusted_evaluation_time,
        "trusted_evaluation_time",
    )
    if requested_until < requested_from:
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "valid_until",
            "must not precede valid_from",
        )

    intersection_from = max(
        finding.finding_valid_from for finding in ordered_findings
    )
    intersection_until = min(
        finding.finding_valid_until for finding in ordered_findings
    )
    if requested_from < intersection_from or requested_until > intersection_until:
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "valid_from",
            "certificate validity must remain inside accepted finding validity intersection",
        )
    if requested_until <= trusted_time:
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "valid_until",
            "expired certificate content cannot support a current assertion",
        )
    if any(finding.finding_state == FindingState.STALE for finding in ordered_findings):
        _fail(
            ProcessingFailureCode.INVALID_TIME_RANGE,
            "findings",
            "STALE required finding state fails closed for current certificate composition",
        )

    normalized_additional_limitations = _normalized_identifier_tuple(
        additional_limitations,
        "additional_limitations",
    )
    normalized_additional_unresolved = _normalized_identifier_tuple(
        additional_unresolved_conditions,
        "additional_unresolved_conditions",
    )
    inherited_limitations = tuple(
        item
        for finding in ordered_findings
        for item in finding.limitations
    )
    inherited_unresolved = tuple(
        item
        for finding in ordered_findings
        for item in finding.unresolved_conditions
    )
    limitations = _merge_identifier_tuples(
        inherited_limitations,
        normalized_additional_limitations,
        "limitations",
    )
    unresolved_conditions = _merge_identifier_tuples(
        inherited_unresolved,
        normalized_additional_unresolved,
        "unresolved_conditions",
    )

    first = ordered_findings[0]
    finding_set_id = _derive_identifier(
        "finding-set",
        {
            "members": [
                {
                    "finding_fingerprint": finding.finding_fingerprint.digest_hex,
                    "finding_id": finding.finding_id.value,
                }
                for finding in ordered_findings
            ]
        },
        resource_limits,
        input_byte_length=input_byte_length,
    )
    source_evaluation_set_id = _derive_identifier(
        "source-evaluation-set",
        {
            "members": sorted(
                {
                    finding.source_evaluation_result_id.value
                    for finding in ordered_findings
                }
            )
        },
        resource_limits,
        input_byte_length=input_byte_length,
    )
    evidence_set_id = _derive_identifier(
        "evidence-set",
        {
            "members": sorted(
                {
                    finding.evidence_binding_or_set_id.value
                    for finding in ordered_findings
                }
            )
        },
        resource_limits,
        input_byte_length=input_byte_length,
    )

    pre_id_payload: dict[str, object] = {
        "architecture_truth_reference_id":
            first.architecture_truth_reference_id.value,
        "canonicalization_version": CANONICALIZATION_VERSION.value,
        "certificate_contract_version": certificate_contract_version.value,
        "conformance_policy_id": conformance_policy_id.value,
        "conformance_policy_version": conformance_policy_version.value,
        "evidence_set_id": evidence_set_id.value,
        "finding_set_id": finding_set_id.value,
        "fingerprint_version": FINGERPRINT_VERSION.value,
        "issuance_authority_state": ISSUANCE_AUTHORITY_NOT_AUTHORIZED.value,
        "limitations": [item.value for item in limitations],
        "scope_id": scope_id.value,
        "source_evaluation_set_id": source_evaluation_set_id.value,
        "subject_id": first.subject_id.value,
        "tenant_id": first.tenant_id.value,
        "unresolved_conditions": [
            item.value for item in unresolved_conditions
        ],
        "valid_from": _utc_text(requested_from),
        "valid_until": _utc_text(requested_until),
    }
    certificate_content_id = _derive_identifier(
        "certificate-content",
        pre_id_payload,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    provisional = ConformanceCertificateContent(
        certificate_contract_version=certificate_contract_version,
        certificate_content_id=certificate_content_id,
        tenant_id=first.tenant_id,
        subject_id=first.subject_id,
        scope_id=scope_id,
        architecture_truth_reference_id=first.architecture_truth_reference_id,
        finding_set_id=finding_set_id,
        source_evaluation_set_id=source_evaluation_set_id,
        evidence_set_id=evidence_set_id,
        conformance_policy_id=conformance_policy_id,
        conformance_policy_version=conformance_policy_version,
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
        valid_from=requested_from,
        valid_until=requested_until,
        limitations=limitations,
        unresolved_conditions=unresolved_conditions,
        certificate_content_fingerprint=Fingerprint(
            algorithm="sha256",
            fingerprint_version=FINGERPRINT_VERSION,
            canonicalization_version=CANONICALIZATION_VERSION,
            digest_hex="0" * 64,
        ),
        issuance_authority_state=ISSUANCE_AUTHORITY_NOT_AUTHORIZED,
    )
    canonical_bytes = canonical_certificate_bytes(
        provisional,
        resource_limits,
        input_byte_length=input_byte_length,
    )
    content_fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )
    return ConformanceCertificateContent(
        certificate_contract_version=certificate_contract_version,
        certificate_content_id=certificate_content_id,
        tenant_id=first.tenant_id,
        subject_id=first.subject_id,
        scope_id=scope_id,
        architecture_truth_reference_id=first.architecture_truth_reference_id,
        finding_set_id=finding_set_id,
        source_evaluation_set_id=source_evaluation_set_id,
        evidence_set_id=evidence_set_id,
        conformance_policy_id=conformance_policy_id,
        conformance_policy_version=conformance_policy_version,
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
        valid_from=requested_from,
        valid_until=requested_until,
        limitations=limitations,
        unresolved_conditions=unresolved_conditions,
        certificate_content_fingerprint=content_fingerprint,
        issuance_authority_state=ISSUANCE_AUTHORITY_NOT_AUTHORIZED,
    )
