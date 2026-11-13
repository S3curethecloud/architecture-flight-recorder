"""Stable read-only Command Center shell foundation.

The shell composes accepted read models. It performs no routing, persistence,
provider access, adapter invocation, remediation, mutation, certificate issuance,
deployment, or runtime authority transition.
"""

from __future__ import annotations

from dataclasses import dataclass

from afr.command_center.capability_registry import (
    EXECUTIVE_STATUS_CAPABILITY_ID,
    READ_ONLY_POSTURE,
    REGISTRY_CONTRACT_VERSION,
    CapabilityRegistry,
    capability_for_surface,
)
from afr.command_center.read_model import (
    EXECUTIVE_STATUS_AUTHORITY_STATE,
    EXECUTIVE_STATUS_SURFACE_ID,
    READ_MODEL_CONTRACT_VERSION,
    CommandCenterReadModel,
    ExecutiveStatusData,
)
from afr.kernel.contracts import (
    ContractValidationError,
    Identifier,
    ProcessingFailure,
    ProcessingFailureCode,
    SemanticVersion,
)


SHELL_CONTRACT_VERSION = SemanticVersion("1.0.0")


@dataclass(frozen=True, slots=True)
class CommandCenterShellSnapshot:
    shell_contract_version: SemanticVersion
    registry: CapabilityRegistry
    surfaces: tuple[
        CommandCenterReadModel[ExecutiveStatusData],
        ...,
    ]


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


def build_shell_snapshot(
    *,
    registry: CapabilityRegistry,
    read_models: tuple[
        CommandCenterReadModel[ExecutiveStatusData],
        ...,
    ],
) -> CommandCenterShellSnapshot:
    """Compose the exact Foundation R1 read-only shell snapshot."""

    _require_instance(
        registry,
        CapabilityRegistry,
        "registry",
    )

    if registry.registry_contract_version != REGISTRY_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "registry.registry_contract_version",
            "must equal REGISTRY_CONTRACT_VERSION",
        )

    if len(registry.registrations) != 1:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "registry.registrations",
            "Foundation R1 requires exactly one capability",
        )

    if not isinstance(read_models, tuple):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "read_models",
            "must be tuple",
        )

    if len(read_models) != 1:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "read_models",
            "Foundation R1 requires exactly one executive_status model",
        )

    model = read_models[0]

    _require_instance(
        model,
        CommandCenterReadModel,
        "read_models[0]",
    )

    if model.read_model_contract_version != READ_MODEL_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "read_models[0].read_model_contract_version",
            "must equal READ_MODEL_CONTRACT_VERSION",
        )

    if model.surface_id != EXECUTIVE_STATUS_SURFACE_ID:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "read_models[0].surface_id",
            "Foundation R1 implements executive_status only",
        )

    if not isinstance(model.data, ExecutiveStatusData):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "read_models[0].data",
            "must be ExecutiveStatusData",
        )

    if model.authority_state != EXECUTIVE_STATUS_AUTHORITY_STATE:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "read_models[0].authority_state",
            "shell cannot inherit or invent execution authority",
        )

    capability = capability_for_surface(
        registry,
        model.surface_id,
    )

    if capability.capability_id != EXECUTIVE_STATUS_CAPABILITY_ID:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "capability.capability_id",
            "unexpected Foundation R1 capability",
        )

    if capability.read_write_posture != READ_ONLY_POSTURE:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "capability.read_write_posture",
            "shell is strictly read-only",
        )

    return CommandCenterShellSnapshot(
        shell_contract_version=
            SHELL_CONTRACT_VERSION,
        registry=registry,
        surfaces=(model,),
    )


def get_surface(
    shell: CommandCenterShellSnapshot,
    surface_id: Identifier,
) -> CommandCenterReadModel[ExecutiveStatusData]:
    """Return a materialized read model without executing a capability."""

    _require_instance(
        shell,
        CommandCenterShellSnapshot,
        "shell",
    )
    _require_instance(
        surface_id,
        Identifier,
        "surface_id",
    )

    matches = tuple(
        model
        for model in shell.surfaces
        if model.surface_id == surface_id
    )

    if len(matches) != 1:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "surface_id",
            "surface is unavailable in this shell snapshot",
        )

    return matches[0]
