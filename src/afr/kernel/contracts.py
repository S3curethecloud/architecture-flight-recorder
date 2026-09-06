"""Immutable contracts for the AFR deterministic-kernel first slice.

This module defines value representations and local validation only. It does
not canonicalize, fingerprint, evaluate conformance, access external state, or
perform side effects.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import re
from typing import Generic, TypeVar


__all__ = [
    "ContractValidationError",
    "EnvironmentBinding",
    "EvaluationBinding",
    "Identifier",
    "OptionalValue",
    "ProcessingFailure",
    "ProcessingFailureCode",
    "ProvenanceBinding",
    "ReleaseBinding",
    "ResourceLimits",
    "SemanticVersion",
    "SubjectBinding",
    "TenantBinding",
    "TimeBinding",
]


_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]*$")
_VERSION_PATTERN = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$"
)

MAX_IDENTIFIER_CHARACTERS = 256
MAX_VERSION_CHARACTERS = 32
MAX_FAILURE_PATH_CHARACTERS = 512
MAX_FAILURE_DETAIL_CHARACTERS = 1024

T = TypeVar("T")


class ProcessingFailureCode(str, Enum):
    """Failures in contract construction, never conformance outcomes."""

    INVALID_TYPE = "INVALID_TYPE"
    MISSING_REQUIRED_FIELD = "MISSING_REQUIRED_FIELD"
    INVALID_IDENTIFIER = "INVALID_IDENTIFIER"
    INVALID_VERSION = "INVALID_VERSION"
    INVALID_TIMESTAMP = "INVALID_TIMESTAMP"
    INVALID_TIME_RANGE = "INVALID_TIME_RANGE"
    INVALID_RESOURCE_LIMIT = "INVALID_RESOURCE_LIMIT"
    RESOURCE_LIMIT_EXCEEDED = "RESOURCE_LIMIT_EXCEEDED"
    TENANT_BINDING_MISMATCH = "TENANT_BINDING_MISMATCH"
    SUBJECT_BINDING_MISMATCH = "SUBJECT_BINDING_MISMATCH"


@dataclass(frozen=True, slots=True)
class ProcessingFailure:
    """Immutable processing-failure data.

    A processing failure is not CONFORMANT, NON_CONFORMANT, INCONCLUSIVE, or
    STALE and must never be converted into one of those outcomes implicitly.
    """

    code: ProcessingFailureCode
    field_path: str
    detail: str

    def __post_init__(self) -> None:
        if not isinstance(self.code, ProcessingFailureCode):
            raise TypeError("code must be a ProcessingFailureCode")

        _require_nonempty_text(
            self.field_path,
            field_path="field_path",
            maximum=MAX_FAILURE_PATH_CHARACTERS,
        )
        _require_nonempty_text(
            self.detail,
            field_path="detail",
            maximum=MAX_FAILURE_DETAIL_CHARACTERS,
        )


class ContractValidationError(ValueError):
    """Raised when immutable contract construction fails."""

    def __init__(self, failure: ProcessingFailure) -> None:
        if not isinstance(failure, ProcessingFailure):
            raise TypeError("failure must be a ProcessingFailure")

        self.failure = failure
        super().__init__(
            f"{failure.code.value}:{failure.field_path}:{failure.detail}"
        )


@dataclass(frozen=True, slots=True)
class OptionalValue(Generic[T]):
    """Represents missing separately from explicit null.

    ``present=False`` means the field is absent.
    ``present=True, value=None`` means the field is explicitly null.
    """

    present: bool
    value: T | None = None

    def __post_init__(self) -> None:
        if type(self.present) is not bool:
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "present",
                "must be a bool",
            )

        if not self.present and self.value is not None:
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "value",
                "must be None when present is False",
            )

        if (
            self.present
            and self.value is not None
            and not _is_approved_immutable_value(self.value)
        ):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "value",
                "must be an approved immutable scalar or value object",
            )

    @classmethod
    def missing(cls) -> OptionalValue[T]:
        return cls(present=False)

    @classmethod
    def of(cls, value: T | None) -> OptionalValue[T]:
        return cls(present=True, value=value)


@dataclass(frozen=True, slots=True, order=True)
class Identifier:
    """Validated opaque identifier with no inferred authority."""

    value: str

    def __post_init__(self) -> None:
        value = _require_nonempty_text(
            self.value,
            field_path="value",
            maximum=MAX_IDENTIFIER_CHARACTERS,
        )

        if value != value.strip():
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "value",
                "leading or trailing whitespace is prohibited",
            )

        if not value.isascii() or _IDENTIFIER_PATTERN.fullmatch(value) is None:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "value",
                "must use the approved ASCII identifier grammar",
            )


@dataclass(frozen=True, slots=True, order=True)
class SemanticVersion:
    """Explicit major.minor.patch semantic version."""

    value: str

    def __post_init__(self) -> None:
        value = _require_nonempty_text(
            self.value,
            field_path="value",
            maximum=MAX_VERSION_CHARACTERS,
        )

        if _VERSION_PATTERN.fullmatch(value) is None:
            _fail(
                ProcessingFailureCode.INVALID_VERSION,
                "value",
                "must be an unprefixed major.minor.patch version",
            )


@dataclass(frozen=True, slots=True)
class TenantBinding:
    tenant_id: Identifier

    def __post_init__(self) -> None:
        _require_instance(self.tenant_id, Identifier, "tenant_id")


@dataclass(frozen=True, slots=True)
class SubjectBinding:
    subject_id: Identifier
    subject_type: Identifier

    def __post_init__(self) -> None:
        _require_instance(self.subject_id, Identifier, "subject_id")
        _require_instance(self.subject_type, Identifier, "subject_type")


@dataclass(frozen=True, slots=True)
class EnvironmentBinding:
    environment_id: Identifier

    def __post_init__(self) -> None:
        _require_instance(
            self.environment_id,
            Identifier,
            "environment_id",
        )


@dataclass(frozen=True, slots=True)
class ReleaseBinding:
    release_id: Identifier

    def __post_init__(self) -> None:
        _require_instance(self.release_id, Identifier, "release_id")


@dataclass(frozen=True, slots=True)
class TimeBinding:
    """Caller-supplied trusted-time boundaries.

    No current time is read by this module.
    """

    evaluated_at: datetime
    valid_from: datetime
    valid_until: datetime

    def __post_init__(self) -> None:
        _require_aware_datetime(self.evaluated_at, "evaluated_at")
        _require_aware_datetime(self.valid_from, "valid_from")
        _require_aware_datetime(self.valid_until, "valid_until")

        if self.valid_until < self.valid_from:
            _fail(
                ProcessingFailureCode.INVALID_TIME_RANGE,
                "valid_until",
                "must not precede valid_from",
            )


@dataclass(frozen=True, slots=True)
class ProvenanceBinding:
    """Explicit source, collector, observation-time, and integrity bindings."""

    source_id: Identifier
    collector_id: Identifier
    observed_at: datetime
    integrity_reference: OptionalValue[Identifier]

    def __post_init__(self) -> None:
        _require_instance(self.source_id, Identifier, "source_id")
        _require_instance(self.collector_id, Identifier, "collector_id")
        _require_aware_datetime(self.observed_at, "observed_at")
        _require_instance(
            self.integrity_reference,
            OptionalValue,
            "integrity_reference",
        )

        integrity_value = self.integrity_reference.value

        if (
            self.integrity_reference.present
            and integrity_value is not None
            and not isinstance(integrity_value, Identifier)
        ):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "integrity_reference.value",
                "must be an Identifier when present and non-null",
            )


@dataclass(frozen=True, slots=True)
class EvaluationBinding:
    """Scope and semantic-version bindings for one future invocation."""

    invocation_id: Identifier
    tenant: TenantBinding
    subject: SubjectBinding
    environment: EnvironmentBinding
    release: ReleaseBinding
    time: TimeBinding
    contract_version: SemanticVersion
    canonicalization_version: SemanticVersion
    fingerprint_version: SemanticVersion

    def __post_init__(self) -> None:
        _require_instance(
            self.invocation_id,
            Identifier,
            "invocation_id",
        )

        expected = (
            ("tenant", self.tenant, TenantBinding),
            ("subject", self.subject, SubjectBinding),
            ("environment", self.environment, EnvironmentBinding),
            ("release", self.release, ReleaseBinding),
            ("time", self.time, TimeBinding),
            ("contract_version", self.contract_version, SemanticVersion),
            (
                "canonicalization_version",
                self.canonicalization_version,
                SemanticVersion,
            ),
            (
                "fingerprint_version",
                self.fingerprint_version,
                SemanticVersion,
            ),
        )

        for field_path, value, expected_type in expected:
            if not isinstance(value, expected_type):
                _fail(
                    ProcessingFailureCode.INVALID_TYPE,
                    field_path,
                    f"must be {expected_type.__name__}",
                )


@dataclass(frozen=True, slots=True)
class ResourceLimits:
    """Explicit versioned deterministic limits for a future invocation."""

    version: SemanticVersion
    maximum_input_bytes: int
    maximum_collection_items: int
    maximum_nesting_depth: int
    maximum_canonical_bytes: int
    maximum_work_units: int

    def __post_init__(self) -> None:
        if not isinstance(self.version, SemanticVersion):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "version",
                "must be a SemanticVersion",
            )

        values = (
            ("maximum_input_bytes", self.maximum_input_bytes),
            ("maximum_collection_items", self.maximum_collection_items),
            ("maximum_nesting_depth", self.maximum_nesting_depth),
            ("maximum_canonical_bytes", self.maximum_canonical_bytes),
            ("maximum_work_units", self.maximum_work_units),
        )

        for field_path, value in values:
            if type(value) is not int:
                _fail(
                    ProcessingFailureCode.INVALID_TYPE,
                    field_path,
                    "must be an int",
                )

            if value <= 0:
                _fail(
                    ProcessingFailureCode.INVALID_RESOURCE_LIMIT,
                    field_path,
                    "must be greater than zero",
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


def _is_approved_immutable_value(value: object) -> bool:
    """Return whether a value is permitted inside OptionalValue.

    Mutable containers, floating-point values, and arbitrary caller-defined
    objects are intentionally excluded.
    """

    if value is None:
        return True

    if isinstance(
        value,
        (
            bool,
            int,
            str,
            bytes,
            datetime,
            Enum,
            Identifier,
            SemanticVersion,
        ),
    ):
        return True

    if isinstance(value, tuple):
        return all(
            _is_approved_immutable_value(item)
            for item in value
        )

    return False


def _require_nonempty_text(
    value: object,
    *,
    field_path: str,
    maximum: int,
) -> str:
    if not isinstance(value, str):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be a string",
        )

    if value == "":
        _fail(
            ProcessingFailureCode.MISSING_REQUIRED_FIELD,
            field_path,
            "must not be empty",
        )

    if len(value) > maximum:
        _fail(
            ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
            field_path,
            f"must not exceed {maximum} characters",
        )

    return value


def _require_aware_datetime(value: object, field_path: str) -> datetime:
    if not isinstance(value, datetime):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "must be a datetime",
        )

    if value.tzinfo is None or value.utcoffset() is None:
        _fail(
            ProcessingFailureCode.INVALID_TIMESTAMP,
            field_path,
            "must include an explicit UTC offset",
        )

    return value


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
