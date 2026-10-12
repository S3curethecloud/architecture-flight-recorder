"""Pure-local Phase 8 read-only Consumer Gateway projection."""

from __future__ import annotations

import math
from collections.abc import Mapping
from typing import Any

READ_ONLY_PROJECTION_ALLOWED = "READ_ONLY_PROJECTION_ALLOWED"
READ_ONLY_PROJECTION_DENIED = "READ_ONLY_PROJECTION_DENIED"
READ_ONLY_PROJECTION_FAIL_CLOSED = "READ_ONLY_PROJECTION_FAIL_CLOSED"

_REQUIRED_FIELDS = (
    "subject_tenant_id",
    "resource_tenant_id",
    "authorization_tenant_id",
    "authorized",
    "resource",
)


def _fail_closed(reason: str) -> dict[str, Any]:
    return {
        "result": READ_ONLY_PROJECTION_FAIL_CLOSED,
        "tenant_id": None,
        "projection": None,
        "reason": reason,
    }


def _denied(tenant_id: str, reason: str) -> dict[str, Any]:
    return {
        "result": READ_ONLY_PROJECTION_DENIED,
        "tenant_id": tenant_id,
        "projection": None,
        "reason": reason,
    }


def _clone_json_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("non-finite float")
        return value
    if isinstance(value, list):
        return [_clone_json_value(item) for item in value]
    if isinstance(value, Mapping):
        cloned: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError("resource keys must be strings")
            cloned[key] = _clone_json_value(item)
        return cloned
    raise ValueError("resource is not JSON-compatible")


def project_read_only(request: Mapping[str, Any]) -> dict[str, Any]:
    """Return one deterministic tenant-bound read-only projection decision."""

    if not isinstance(request, Mapping):
        return _fail_closed("INVALID_REQUEST_TYPE")
    if any(field not in request for field in _REQUIRED_FIELDS):
        return _fail_closed("MISSING_REQUIRED_FIELD")

    subject_tenant_id = request["subject_tenant_id"]
    resource_tenant_id = request["resource_tenant_id"]
    authorization_tenant_id = request["authorization_tenant_id"]
    authorized = request["authorized"]
    resource = request["resource"]

    tenant_values = (
        subject_tenant_id,
        resource_tenant_id,
        authorization_tenant_id,
    )
    if any(not isinstance(value, str) or not value for value in tenant_values):
        return _fail_closed("INVALID_TENANT_BINDING")
    if not isinstance(authorized, bool):
        return _fail_closed("INVALID_AUTHORIZATION_DECISION")
    if not isinstance(resource, Mapping):
        return _fail_closed("INVALID_RESOURCE")

    try:
        projection = _clone_json_value(resource)
    except ValueError:
        return _fail_closed("INVALID_RESOURCE")

    if not (
        subject_tenant_id
        == resource_tenant_id
        == authorization_tenant_id
    ):
        return _denied(resource_tenant_id, "TENANT_BINDING_MISMATCH")
    if not authorized:
        return _denied(resource_tenant_id, "AUTHORIZATION_DENIED")

    return {
        "result": READ_ONLY_PROJECTION_ALLOWED,
        "tenant_id": resource_tenant_id,
        "projection": projection,
        "reason": None,
    }
