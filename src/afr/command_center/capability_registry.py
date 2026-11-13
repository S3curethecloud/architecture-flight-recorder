"""Declarative Phase 12 Command Center capability registry foundation.

Registration is metadata only. It grants no execution, provider, remediation,
issuance, deployment, or runtime authority.
"""

from __future__ import annotations

from dataclasses import dataclass

from afr.command_center.read_model import (
    EXECUTIVE_STATUS_SURFACE_ID,
    READ_MODEL_CONTRACT_VERSION,
)
from afr.kernel.contracts import (
    ContractValidationError,
    Identifier,
    ProcessingFailure,
    ProcessingFailureCode,
    SemanticVersion,
)


REGISTRY_CONTRACT_VERSION = SemanticVersion("1.0.0")
CAPABILITY_CONTRACT_VERSION = SemanticVersion("1.0.0")

STABLE_SURFACE_IDS = (
    Identifier("executive_status"),
    Identifier("live_findings"),
    Identifier("architecture_drift"),
    Identifier("evidence_health"),
    Identifier("evaluation_runs"),
    Identifier("conformance_certificates"),
    Identifier("system_scope"),
    Identifier("critical_alerts"),
    Identifier("flight_recorder_timeline"),
    Identifier("governance_audit"),
)

FOUNDATION_IMPLEMENTED_SURFACE_IDS = (
    EXECUTIVE_STATUS_SURFACE_ID,
)

EXECUTIVE_STATUS_CAPABILITY_ID = Identifier(
    "afr.command-center.executive-status"
)

SOURCE_CLASS_ACCEPTED_CONFORMANCE_SUMMARY = Identifier(
    "AFR_ACCEPTED_CONFORMANCE_SUMMARY"
)

ADAPTER_CLASS_DECLARATIVE_ONLY = Identifier(
    "DECLARATIVE_ONLY"
)

READ_ONLY_POSTURE = Identifier("READ_ONLY")

REQUIRED_AUTHORITY_CLASSES = (
    Identifier("AFR_ACCEPTED_STATE_READ"),
)

FRESHNESS_CONTRACT = Identifier(
    "AFR_COMMAND_CENTER_FRESHNESS_V1"
)

FAILURE_CONTRACT = Identifier(
    "AFR_COMMAND_CENTER_FAIL_CLOSED_V1"
)

PROVENANCE_CONTRACT = Identifier(
    "AFR_COMMAND_CENTER_PROVENANCE_V1"
)

FOUNDATION_LIFECYCLE_STATE = Identifier(
    "FOUNDATION_R1_CANDIDATE"
)


@dataclass(frozen=True, slots=True)
class CapabilityRegistration:
    capability_id: Identifier
    capability_contract_version: SemanticVersion
    supported_surface_ids: tuple[Identifier, ...]
    source_class: Identifier
    adapter_class: Identifier
    read_write_posture: Identifier
    required_authority_classes: tuple[Identifier, ...]
    freshness_contract: Identifier
    failure_contract: Identifier
    provenance_contract: Identifier
    compatibility_min_version: SemanticVersion
    compatibility_max_version: SemanticVersion
    lifecycle_state: Identifier


@dataclass(frozen=True, slots=True)
class CapabilityRegistry:
    registry_contract_version: SemanticVersion
    registrations: tuple[CapabilityRegistration, ...]


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


def _normalized_ids(
    value: object,
    field_path: str,
) -> tuple[Identifier, ...]:
    if not isinstance(value, tuple):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be tuple of Identifier values",
        )

    if not value:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            field_path,
            "cannot be empty",
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
            "duplicates are prohibited",
        )

    return ordered


def _validate_registration(
    registration: CapabilityRegistration,
    index: int,
) -> CapabilityRegistration:
    _require_instance(
        registration,
        CapabilityRegistration,
        f"registrations[{index}]",
    )

    if (
        registration.capability_contract_version
        != CAPABILITY_CONTRACT_VERSION
    ):
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            f"registrations[{index}].capability_contract_version",
            "must equal CAPABILITY_CONTRACT_VERSION",
        )

    surfaces = _normalized_ids(
        registration.supported_surface_ids,
        f"registrations[{index}].supported_surface_ids",
    )

    if surfaces != registration.supported_surface_ids:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            f"registrations[{index}].supported_surface_ids",
            "must already be canonical sorted unique identifiers",
        )

    for surface in surfaces:
        if surface not in FOUNDATION_IMPLEMENTED_SURFACE_IDS:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                f"registrations[{index}].supported_surface_ids",
                "foundation R1 implements executive_status only",
            )

    _normalized_ids(
        registration.required_authority_classes,
        f"registrations[{index}].required_authority_classes",
    )

    if registration.read_write_posture != READ_ONLY_POSTURE:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            f"registrations[{index}].read_write_posture",
            "foundation R1 is strictly READ_ONLY",
        )

    if registration.adapter_class != ADAPTER_CLASS_DECLARATIVE_ONLY:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            f"registrations[{index}].adapter_class",
            "foundation R1 permits declarative adapter seam only",
        )

    if (
        registration.compatibility_min_version
        != READ_MODEL_CONTRACT_VERSION
        or registration.compatibility_max_version
        != READ_MODEL_CONTRACT_VERSION
    ):
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            f"registrations[{index}].compatibility",
            "foundation R1 supports read-model contract 1.0.0 only",
        )

    if registration.lifecycle_state != FOUNDATION_LIFECYCLE_STATE:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            f"registrations[{index}].lifecycle_state",
            "must remain FOUNDATION_R1_CANDIDATE",
        )

    return registration


def build_registry(
    registrations: tuple[CapabilityRegistration, ...],
) -> CapabilityRegistry:
    """Build an immutable declarative registry without granting authority."""

    if not isinstance(registrations, tuple):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "registrations",
            "must be tuple",
        )

    if not registrations:
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            "registrations",
            "cannot be empty",
        )

    validated = tuple(
        _validate_registration(registration, index)
        for index, registration in enumerate(registrations)
    )

    capability_ids = [
        item.capability_id.value
        for item in validated
    ]

    if len(set(capability_ids)) != len(capability_ids):
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "registrations",
            "duplicate capability_id values are prohibited",
        )

    ordered = tuple(
        sorted(
            validated,
            key=lambda item: item.capability_id.value,
        )
    )

    return CapabilityRegistry(
        registry_contract_version=
            REGISTRY_CONTRACT_VERSION,
        registrations=ordered,
    )


def build_foundation_registry() -> CapabilityRegistry:
    """Return the exact one-capability Foundation R1 registry."""

    registration = CapabilityRegistration(
        capability_id=
            EXECUTIVE_STATUS_CAPABILITY_ID,
        capability_contract_version=
            CAPABILITY_CONTRACT_VERSION,
        supported_surface_ids=
            FOUNDATION_IMPLEMENTED_SURFACE_IDS,
        source_class=
            SOURCE_CLASS_ACCEPTED_CONFORMANCE_SUMMARY,
        adapter_class=
            ADAPTER_CLASS_DECLARATIVE_ONLY,
        read_write_posture=
            READ_ONLY_POSTURE,
        required_authority_classes=
            REQUIRED_AUTHORITY_CLASSES,
        freshness_contract=
            FRESHNESS_CONTRACT,
        failure_contract=
            FAILURE_CONTRACT,
        provenance_contract=
            PROVENANCE_CONTRACT,
        compatibility_min_version=
            READ_MODEL_CONTRACT_VERSION,
        compatibility_max_version=
            READ_MODEL_CONTRACT_VERSION,
        lifecycle_state=
            FOUNDATION_LIFECYCLE_STATE,
    )

    return build_registry((registration,))


def capability_for_surface(
    registry: CapabilityRegistry,
    surface_id: Identifier,
) -> CapabilityRegistration:
    """Resolve one registered surface without invoking any adapter."""

    _require_instance(
        registry,
        CapabilityRegistry,
        "registry",
    )
    _require_instance(
        surface_id,
        Identifier,
        "surface_id",
    )

    matches = tuple(
        registration
        for registration in registry.registrations
        if surface_id in registration.supported_surface_ids
    )

    if len(matches) != 1:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "surface_id",
            "surface must resolve to exactly one capability",
        )

    return matches[0]
