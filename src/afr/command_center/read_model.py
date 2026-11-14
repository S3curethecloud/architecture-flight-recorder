"""Deterministic AFR Phase 12 Command Center foundation read model.

COMMAND_CENTER_FOUNDATION_R1 implements only the accepted ``executive_status``
semantic surface. It is provider-neutral, read-only construction logic.

This module performs no persistence, provider/network I/O, remediation,
certificate issuance, NEXUS mutation, runtime action, deployment, or authority
grant. Unknown or incompatible mandatory state fails closed.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Generic, TypeVar

from afr.conformance.conformance_summary import (
    ACCEPTED_FINDING_SET_STATUS,
    SCORE_CONTRACT_VERSION,
    ConformanceScoreSummary,
    canonical_score_summary_bytes,
    project_conformance_summary,
)
from afr.conformance.finding_derivation import ConformanceFinding
from afr.kernel.canonicalization import CANONICALIZATION_VERSION, canonicalize
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


READ_MODEL_CONTRACT_VERSION = SemanticVersion("1.0.0")
SOURCE_SCOPE_BINDING_CONTRACT_VERSION = SemanticVersion("1.0.0")

EXECUTIVE_STATUS_SURFACE_ID = Identifier("executive_status")

FRESHNESS_CURRENT = Identifier("CURRENT")
FRESHNESS_STALE = Identifier("STALE")
FRESHNESS_UNKNOWN = Identifier("UNKNOWN")
FRESHNESS_UNAVAILABLE = Identifier("UNAVAILABLE")

FRESHNESS_STATES = (
    FRESHNESS_CURRENT,
    FRESHNESS_STALE,
    FRESHNESS_UNKNOWN,
    FRESHNESS_UNAVAILABLE,
)

AVAILABILITY_AVAILABLE = Identifier("AVAILABLE")
AVAILABILITY_PARTIAL = Identifier("PARTIAL")
AVAILABILITY_STALE = Identifier("STALE")
AVAILABILITY_UNAVAILABLE = Identifier("UNAVAILABLE")
AVAILABILITY_UNCONFIGURED = Identifier("UNCONFIGURED")
AVAILABILITY_UNAUTHORIZED = Identifier("UNAUTHORIZED")
AVAILABILITY_INCONCLUSIVE = Identifier("INCONCLUSIVE")
AVAILABILITY_BLOCKED = Identifier("BLOCKED")

AVAILABILITY_STATES = (
    AVAILABILITY_AVAILABLE,
    AVAILABILITY_PARTIAL,
    AVAILABILITY_STALE,
    AVAILABILITY_UNAVAILABLE,
    AVAILABILITY_UNCONFIGURED,
    AVAILABILITY_UNAUTHORIZED,
    AVAILABILITY_INCONCLUSIVE,
    AVAILABILITY_BLOCKED,
)

EXECUTIVE_STATUS_AUTHORITY_STATE = (
    Identifier("PRESENTATION_ACCEPTED"),
    Identifier("IMPLEMENTATION_NOT_AUTHORIZED"),
    Identifier("RUNTIME_NOT_QUALIFIED"),
    Identifier("PROVIDER_ACCESS_NOT_AUTHORIZED"),
    Identifier("CERTIFICATE_ISSUANCE_NOT_AUTHORIZED"),
    Identifier("REMEDIATION_NOT_AUTHORIZED"),
)

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class ExecutiveStatusData:
    """Immutable executive-status projection over accepted S5A summary state."""

    score_contract_version: SemanticVersion
    score_formula_id: Identifier
    score_formula_version: SemanticVersion
    finding_set_id: Identifier
    eligible_finding_count: int
    supported_count: int
    contradicted_count: int
    stale_count: int
    inconclusive_count: int
    evidence_unavailable_count: int
    excluded_count: int
    score_value_or_unavailable: OptionalValue[int]
    score_fingerprint: Fingerprint


@dataclass(frozen=True, slots=True)
class SourceScopeBinding:
    """Immutable scope proof derived from the accepted S5A finding set."""

    binding_contract_version: SemanticVersion
    tenant_id: Identifier
    subject_id_or_scope: Identifier
    workspace_or_system_scope: Identifier
    finding_set_id: Identifier
    score_fingerprint: Fingerprint
    source_findings: tuple[ConformanceFinding, ...]
    binding_fingerprint: Fingerprint


@dataclass(frozen=True, slots=True)
class CommandCenterReadModel(Generic[T]):
    """Versioned provider-neutral Command Center read-model envelope."""

    read_model_contract_version: SemanticVersion
    surface_id: Identifier
    tenant_id: Identifier
    subject_id_or_scope: Identifier
    workspace_or_system_scope: Identifier
    as_of_trusted_time: datetime
    freshness_state: Identifier
    source_identity_set: tuple[Identifier, ...]
    source_fingerprint: Fingerprint
    authority_state: tuple[Identifier, ...]
    availability_state: Identifier
    limitations: tuple[Identifier, ...]
    warnings: tuple[Identifier, ...]
    data: T


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
            "must be tuple of Identifier values",
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


def _validate_summary(
    summary: object,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> ConformanceScoreSummary:
    _require_instance(summary, ConformanceScoreSummary, "summary")

    if summary.score_contract_version != SCORE_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "summary.score_contract_version",
            "must equal accepted SCORE_CONTRACT_VERSION",
        )

    counts = (
        summary.supported_count,
        summary.contradicted_count,
        summary.stale_count,
        summary.inconclusive_count,
        summary.evidence_unavailable_count,
    )

    for index, value in enumerate(counts):
        if type(value) is not int or value < 0:
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                f"summary.counts[{index}]",
                "must be non-negative int",
            )

    if type(summary.eligible_finding_count) is not int:
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "summary.eligible_finding_count",
            "must be int",
        )

    if summary.eligible_finding_count <= 0:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "summary.eligible_finding_count",
            "must be greater than zero",
        )

    if sum(counts) != summary.eligible_finding_count:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "summary",
            "finding-state counts must equal eligible_finding_count",
        )

    if summary.excluded_count != 0:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "summary.excluded_count",
            "foundation v1 accepts the S5A zero-exclusion model only",
        )

    unresolved = (
        summary.stale_count
        + summary.inconclusive_count
        + summary.evidence_unavailable_count
    ) > 0

    score = summary.score_value_or_unavailable

    if not isinstance(score, OptionalValue):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "summary.score_value_or_unavailable",
            "must be OptionalValue",
        )

    if unresolved:
        if score.present:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "summary.score_value_or_unavailable",
                "unresolved mandatory state requires unavailable score",
            )
    else:
        if (
            not score.present
            or score.value is None
            or type(score.value) is not int
        ):
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "summary.score_value_or_unavailable",
                "resolved summary requires integer score",
            )

        expected_score = (
            summary.supported_count
            * 10_000
            // summary.eligible_finding_count
        )

        if score.value != expected_score:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "summary.score_value_or_unavailable",
                "must preserve accepted S5A score formula",
            )

    normalized_limitations = _normalized_identifier_tuple(
        summary.limitations,
        "summary.limitations",
    )

    if normalized_limitations != summary.limitations:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "summary.limitations",
            "must already be canonical sorted unique identifiers",
        )

    canonical_bytes = canonical_score_summary_bytes(
        summary,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    expected_fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )

    if expected_fingerprint != summary.score_fingerprint:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "summary.score_fingerprint",
            "must match deterministic accepted summary content",
        )

    return summary


def _reproject_source_summary(
    summary: ConformanceScoreSummary,
    source_findings: tuple[ConformanceFinding, ...],
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> ConformanceScoreSummary:
    """Rebind S5A presentation state to its accepted finding-set lineage."""

    return project_conformance_summary(
        score_contract_version=
            summary.score_contract_version,
        finding_set_status=
            ACCEPTED_FINDING_SET_STATUS,
        findings=source_findings,
        score_formula_id=
            summary.score_formula_id,
        score_formula_version=
            summary.score_formula_version,
        additional_limitations=
            summary.limitations,
        resource_limits=resource_limits,
        input_byte_length=input_byte_length,
    )


def _derive_workspace_or_system_scope(
    summary: ConformanceScoreSummary,
    source_findings: tuple[ConformanceFinding, ...],
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> Identifier:
    """Derive an immutable system scope from accepted finding-set scope."""

    ordered = tuple(
        sorted(
            source_findings,
            key=lambda finding: finding.finding_id.value,
        )
    )

    first = ordered[0]

    canonical_bytes = canonicalize(
        {
            "architecture_truth_reference_id":
                first.architecture_truth_reference_id.value,
            "environment_id":
                first.environment_id.value,
            "finding_set_id":
                summary.finding_set_id.value,
            "release_id":
                first.release_id.value,
            "subject_id":
                first.subject_id.value,
            "tenant_id":
                first.tenant_id.value,
        },
        resource_limits,
        input_byte_length=input_byte_length,
    )

    fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=
            CANONICALIZATION_VERSION,
        fingerprint_version=
            FINGERPRINT_VERSION,
    )

    return Identifier(
        "system-scope:" + fingerprint.digest_hex
    )


def _scope_binding_fingerprint(
    *,
    tenant_id: Identifier,
    subject_id_or_scope: Identifier,
    workspace_or_system_scope: Identifier,
    finding_set_id: Identifier,
    score_fingerprint: Fingerprint,
    source_findings: tuple[ConformanceFinding, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> Fingerprint:
    ordered = tuple(
        sorted(
            source_findings,
            key=lambda finding: finding.finding_id.value,
        )
    )

    canonical_bytes = canonicalize(
        {
            "binding_contract_version":
                SOURCE_SCOPE_BINDING_CONTRACT_VERSION.value,
            "finding_set_id":
                finding_set_id.value,
            "score_fingerprint": {
                "algorithm":
                    score_fingerprint.algorithm,
                "canonicalization_version":
                    score_fingerprint.canonicalization_version.value,
                "digest_hex":
                    score_fingerprint.digest_hex,
                "fingerprint_version":
                    score_fingerprint.fingerprint_version.value,
            },
            "source_findings": [
                {
                    "finding_fingerprint":
                        finding.finding_fingerprint.digest_hex,
                    "finding_id":
                        finding.finding_id.value,
                }
                for finding in ordered
            ],
            "subject_id_or_scope":
                subject_id_or_scope.value,
            "tenant_id":
                tenant_id.value,
            "workspace_or_system_scope":
                workspace_or_system_scope.value,
        },
        resource_limits,
        input_byte_length=input_byte_length,
    )

    return compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=
            CANONICALIZATION_VERSION,
        fingerprint_version=
            FINGERPRINT_VERSION,
    )


def build_source_scope_binding(
    *,
    summary: ConformanceScoreSummary,
    source_findings: tuple[ConformanceFinding, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> SourceScopeBinding:
    """Build scope proof only from findings that exactly reproduce S5A."""

    _require_instance(
        resource_limits,
        ResourceLimits,
        "resource_limits",
    )

    if resource_limits.version != CANONICALIZATION_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "resource_limits.version",
            "must equal CANONICALIZATION_VERSION",
        )

    accepted_summary = _validate_summary(
        summary,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    reproduced_summary = _reproject_source_summary(
        accepted_summary,
        source_findings,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    if reproduced_summary != accepted_summary:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "source_findings",
            "must exactly reproduce the accepted S5A summary",
        )

    ordered = tuple(
        sorted(
            source_findings,
            key=lambda finding: finding.finding_id.value,
        )
    )

    first = ordered[0]

    workspace_or_system_scope = (
        _derive_workspace_or_system_scope(
            accepted_summary,
            ordered,
            resource_limits,
            input_byte_length=input_byte_length,
        )
    )

    binding_fingerprint = _scope_binding_fingerprint(
        tenant_id=first.tenant_id,
        subject_id_or_scope=first.subject_id,
        workspace_or_system_scope=
            workspace_or_system_scope,
        finding_set_id=
            accepted_summary.finding_set_id,
        score_fingerprint=
            accepted_summary.score_fingerprint,
        source_findings=ordered,
        resource_limits=resource_limits,
        input_byte_length=input_byte_length,
    )

    return SourceScopeBinding(
        binding_contract_version=
            SOURCE_SCOPE_BINDING_CONTRACT_VERSION,
        tenant_id=
            first.tenant_id,
        subject_id_or_scope=
            first.subject_id,
        workspace_or_system_scope=
            workspace_or_system_scope,
        finding_set_id=
            accepted_summary.finding_set_id,
        score_fingerprint=
            accepted_summary.score_fingerprint,
        source_findings=ordered,
        binding_fingerprint=
            binding_fingerprint,
    )


def _validate_source_scope_binding(
    summary: ConformanceScoreSummary,
    source_scope_binding: object,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> SourceScopeBinding:
    _require_instance(
        source_scope_binding,
        SourceScopeBinding,
        "source_scope_binding",
    )

    expected = build_source_scope_binding(
        summary=summary,
        source_findings=
            source_scope_binding.source_findings,
        resource_limits=resource_limits,
        input_byte_length=input_byte_length,
    )

    if source_scope_binding != expected:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "source_scope_binding",
            "must exactly match accepted finding-set scope lineage",
        )

    return source_scope_binding


def project_executive_status(
    *,
    summary: ConformanceScoreSummary,
    source_scope_binding: SourceScopeBinding,
    as_of_trusted_time: datetime,
    freshness_state: Identifier,
    availability_state: Identifier,
    warnings: tuple[Identifier, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> CommandCenterReadModel[ExecutiveStatusData]:
    """Project the bounded ``executive_status`` foundation surface."""

    _require_instance(resource_limits, ResourceLimits, "resource_limits")

    if resource_limits.version != CANONICALIZATION_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "resource_limits.version",
            "must equal CANONICALIZATION_VERSION",
        )

    for field_path, value in (
        ("freshness_state", freshness_state),
        ("availability_state", availability_state),
    ):
        _require_instance(value, Identifier, field_path)

    _require_aware_datetime(
        as_of_trusted_time,
        "as_of_trusted_time",
    )

    if freshness_state not in FRESHNESS_STATES:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "freshness_state",
            "must use the frozen foundation freshness domain",
        )

    if availability_state not in AVAILABILITY_STATES:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "availability_state",
            "must use the Command Center availability domain",
        )

    if (
        freshness_state != FRESHNESS_CURRENT
        and availability_state == AVAILABILITY_AVAILABLE
    ):
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "availability_state",
            "non-current freshness cannot present as AVAILABLE",
        )

    accepted_summary = _validate_summary(
        summary,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    binding = _validate_source_scope_binding(
        accepted_summary,
        source_scope_binding,
        resource_limits,
        input_byte_length=input_byte_length,
    )

    normalized_warnings = _normalized_identifier_tuple(
        warnings,
        "warnings",
    )

    source_identity_set = tuple(
        sorted(
            (
                accepted_summary.finding_set_id,
                Identifier(
                    "score-fingerprint:"
                    + accepted_summary.score_fingerprint.digest_hex
                ),
                Identifier(
                    "scope-binding:"
                    + binding.binding_fingerprint.digest_hex
                ),
            ),
            key=lambda item: item.value,
        )
    )

    data = ExecutiveStatusData(
        score_contract_version=
            accepted_summary.score_contract_version,
        score_formula_id=
            accepted_summary.score_formula_id,
        score_formula_version=
            accepted_summary.score_formula_version,
        finding_set_id=
            accepted_summary.finding_set_id,
        eligible_finding_count=
            accepted_summary.eligible_finding_count,
        supported_count=
            accepted_summary.supported_count,
        contradicted_count=
            accepted_summary.contradicted_count,
        stale_count=
            accepted_summary.stale_count,
        inconclusive_count=
            accepted_summary.inconclusive_count,
        evidence_unavailable_count=
            accepted_summary.evidence_unavailable_count,
        excluded_count=
            accepted_summary.excluded_count,
        score_value_or_unavailable=
            accepted_summary.score_value_or_unavailable,
        score_fingerprint=
            accepted_summary.score_fingerprint,
    )

    return CommandCenterReadModel(
        read_model_contract_version=
            READ_MODEL_CONTRACT_VERSION,
        surface_id=
            EXECUTIVE_STATUS_SURFACE_ID,
        tenant_id=
            binding.tenant_id,
        subject_id_or_scope=
            binding.subject_id_or_scope,
        workspace_or_system_scope=
            binding.workspace_or_system_scope,
        as_of_trusted_time=as_of_trusted_time,
        freshness_state=freshness_state,
        source_identity_set=source_identity_set,
        source_fingerprint=
            accepted_summary.score_fingerprint,
        authority_state=
            EXECUTIVE_STATUS_AUTHORITY_STATE,
        availability_state=availability_state,
        limitations=
            accepted_summary.limitations,
        warnings=normalized_warnings,
        data=data,
    )


def _fingerprint_payload(
    fingerprint: Fingerprint,
) -> dict[str, object]:
    return {
        "algorithm": fingerprint.algorithm,
        "canonicalization_version":
            fingerprint.canonicalization_version.value,
        "digest_hex": fingerprint.digest_hex,
        "fingerprint_version":
            fingerprint.fingerprint_version.value,
    }


def canonical_read_model_bytes(
    model: CommandCenterReadModel[ExecutiveStatusData],
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> bytes:
    """Return deterministic canonical bytes for the foundation read model."""

    _require_instance(model, CommandCenterReadModel, "model")
    _require_instance(resource_limits, ResourceLimits, "resource_limits")

    if model.read_model_contract_version != READ_MODEL_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "model.read_model_contract_version",
            "must equal READ_MODEL_CONTRACT_VERSION",
        )

    if model.surface_id != EXECUTIVE_STATUS_SURFACE_ID:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "model.surface_id",
            "foundation R1 implements executive_status only",
        )

    if not isinstance(model.data, ExecutiveStatusData):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "model.data",
            "must be ExecutiveStatusData",
        )

    score = model.data.score_value_or_unavailable

    payload = {
        "as_of_trusted_time":
            _utc_text(model.as_of_trusted_time),
        "authority_state":
            [item.value for item in model.authority_state],
        "availability_state":
            model.availability_state.value,
        "data": {
            "contradicted_count":
                model.data.contradicted_count,
            "eligible_finding_count":
                model.data.eligible_finding_count,
            "evidence_unavailable_count":
                model.data.evidence_unavailable_count,
            "excluded_count":
                model.data.excluded_count,
            "finding_set_id":
                model.data.finding_set_id.value,
            "inconclusive_count":
                model.data.inconclusive_count,
            "score_contract_version":
                model.data.score_contract_version.value,
            "score_fingerprint":
                _fingerprint_payload(
                    model.data.score_fingerprint
                ),
            "score_formula_id":
                model.data.score_formula_id.value,
            "score_formula_version":
                model.data.score_formula_version.value,
            "score_value_or_unavailable": {
                "present": score.present,
                "value": score.value,
            },
            "stale_count":
                model.data.stale_count,
            "supported_count":
                model.data.supported_count,
        },
        "freshness_state":
            model.freshness_state.value,
        "limitations":
            [item.value for item in model.limitations],
        "read_model_contract_version":
            model.read_model_contract_version.value,
        "source_fingerprint":
            _fingerprint_payload(
                model.source_fingerprint
            ),
        "source_identity_set":
            [item.value for item in model.source_identity_set],
        "subject_id_or_scope":
            model.subject_id_or_scope.value,
        "surface_id":
            model.surface_id.value,
        "tenant_id":
            model.tenant_id.value,
        "warnings":
            [item.value for item in model.warnings],
        "workspace_or_system_scope":
            model.workspace_or_system_scope.value,
    }

    return canonicalize(
        payload,
        resource_limits,
        input_byte_length=input_byte_length,
    )
