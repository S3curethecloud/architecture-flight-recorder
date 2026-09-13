"""Phase 4 normalized-evidence byte admission primitive."""

from __future__ import annotations

from dataclasses import dataclass as _dataclass
from datetime import datetime as _datetime, timezone as _timezone
import unicodedata as _unicodedata
from typing import Any as _Any


NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED = (
    "NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED"
)

__all__ = (
    "NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED",
    "NormalizedEvidenceBytesRequest",
    "NormalizedEvidenceBytesLimitResult",
    "NormalizedEvidenceBytesLimitFailure",
    "NormalizedEvidenceBytesContractError",
    "evaluate_normalized_evidence_bytes_limit",
)

_PROJECTION_SCHEMA_VERSION = "1.0.0"
_PROJECTION_SERIALIZATION_VERSION = "1.0.0"
_PROCESSING_FAILURE = "PROCESSING_FAILURE"
_RESOURCE_REFERENCE = "normalized_evidence_bytes"
_SEMANTIC_LOCATION = "normalized_evidence_bytes"
_STOPPED_BEFORE_EVIDENCE_CONSTRUCTION = (
    "STOPPED_BEFORE_EVIDENCE_CONSTRUCTION"
)


class NormalizedEvidenceBytesContractError(ValueError):
    """Noncanonical direct-call programming-contract error."""

    __slots__ = ("field_path", "reason")

    def __init__(self, field_path: str, reason: str) -> None:
        self.field_path = field_path
        self.reason = reason
        super().__init__(f"{field_path}: {reason}")


@_dataclass(frozen=True, slots=True)
class _FrozenMapping:
    entries: tuple[tuple[str, _Any], ...]


def _contract_error(field_path: str, reason: str) -> None:
    raise NormalizedEvidenceBytesContractError(field_path, reason)


def _validate_unicode_string(value: str, field_path: str) -> None:
    for character in value:
        code_point = ord(character)
        if 0xD800 <= code_point <= 0xDFFF:
            _contract_error(
                field_path,
                "unpaired Unicode surrogate is not canonicalizable",
            )


def _require_exact_str(
    value: _Any,
    field_path: str,
    *,
    allow_none: bool = False,
) -> None:
    if allow_none and value is None:
        return
    if type(value) is not str:
        _contract_error(field_path, "must be an exact str")
    _validate_unicode_string(value, field_path)


def _require_exact_bool(value: _Any, field_path: str) -> None:
    if type(value) is not bool:
        _contract_error(field_path, "must be an exact bool")


def _require_exact_nonnegative_int(value: _Any, field_path: str) -> None:
    if type(value) is not int:
        _contract_error(
            field_path,
            "must be an exact int excluding bool",
        )
    if value < 0:
        _contract_error(field_path, "must be greater than or equal to zero")


def _require_exact_datetime(
    value: _Any,
    field_path: str,
    *,
    allow_none: bool = False,
) -> None:
    if allow_none and value is None:
        return
    if type(value) is not _datetime:
        _contract_error(field_path, "must be an exact datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        _contract_error(field_path, "must be timezone-aware")


def _canonical_key_identity(value: str, field_path: str) -> str:
    """Return the NFC key identity used for collision detection.

    Deterministic JSON string encoding is injective over validated NFC strings,
    so equality of these identities is equivalent to equality of canonical key
    bytes without materializing the complete encoded key.
    """

    _require_exact_str(value, field_path)
    return _unicodedata.normalize("NFC", value)


def _iter_json_string_octets(value: str, field_path: str):
    """Yield canonical JSON-string UTF-8 octets without a whole-value buffer."""

    _require_exact_str(value, field_path)
    normalized = _unicodedata.normalize("NFC", value)
    yield 0x22
    for character in normalized:
        code_point = ord(character)
        if character == '"':
            encoded = b'\\"'
        elif character == "\\":
            encoded = b"\\\\"
        elif character == "\b":
            encoded = b"\\b"
        elif character == "\f":
            encoded = b"\\f"
        elif character == "\n":
            encoded = b"\\n"
        elif character == "\r":
            encoded = b"\\r"
        elif character == "\t":
            encoded = b"\\t"
        elif code_point < 0x20:
            encoded = f"\\u{code_point:04x}".encode("ascii")
        else:
            encoded = character.encode("utf-8")
        yield from encoded
    yield 0x22


def _compare_canonical_key_bytes(
    left: str,
    right: str,
    field_path: str,
) -> int:
    """Compare canonical key bytes lazily, without full key-byte buffers."""

    left_octets = _iter_json_string_octets(left, field_path)
    right_octets = _iter_json_string_octets(right, field_path)
    sentinel = object()

    while True:
        left_octet = next(left_octets, sentinel)
        right_octet = next(right_octets, sentinel)
        if left_octet is sentinel:
            return 0 if right_octet is sentinel else -1
        if right_octet is sentinel:
            return 1
        if left_octet < right_octet:
            return -1
        if left_octet > right_octet:
            return 1


class _CanonicalKeyOrder:
    __slots__ = ("value", "field_path")

    def __init__(self, value: str, field_path: str) -> None:
        self.value = value
        self.field_path = field_path

    def __lt__(self, other: object) -> bool:
        if type(other) is not _CanonicalKeyOrder:
            return NotImplemented
        return (
            _compare_canonical_key_bytes(
                self.value,
                other.value,
                self.field_path,
            )
            < 0
        )


def _materialize_sequence_items(value: _Any) -> tuple[_Any, ...]:
    return tuple(value)


def _materialize_mapping_items(
    value: dict[str, _Any],
) -> tuple[tuple[str, _Any], ...]:
    return tuple(value.items())


def _capture_sequence_items(value: _Any, field_path: str) -> tuple[_Any, ...]:
    try:
        return _materialize_sequence_items(value)
    except RuntimeError:
        _contract_error(
            field_path,
            "container mutated during deep-snapshot capture",
        )


def _capture_mapping_items(
    value: dict[str, _Any],
    field_path: str,
) -> tuple[tuple[str, _Any], ...]:
    try:
        items = _materialize_mapping_items(value)
    except RuntimeError:
        _contract_error(
            field_path,
            "mapping mutated during deep-snapshot capture",
        )

    observed: set[str] = set()
    for key, _ in items:
        if type(key) is not str:
            _contract_error(
                f"{field_path}.<key>",
                "mapping key must be an exact str",
            )
        key_identity = _canonical_key_identity(
            key,
            f"{field_path}.<key>",
        )
        if key_identity in observed:
            _contract_error(
                field_path,
                "mapping keys collide after NFC normalization",
            )
        observed.add(key_identity)
    return items


def _snapshot_scalar(value: _Any, field_path: str) -> _Any:
    if value is None:
        return None
    if type(value) is bool:
        return value
    if type(value) is int:
        return value
    if type(value) is str:
        _validate_unicode_string(value, field_path)
        return value
    if type(value) is _datetime:
        _require_exact_datetime(value, field_path)
        return value
    _contract_error(
        field_path,
        "unsupported projection-value type",
    )


def _deep_snapshot(value: _Any, field_path: str) -> _Any:
    """Snapshot the approved nested domain without recursive Python calls."""

    stack: list[tuple[_Any, ...]] = [("visit", value, field_path)]
    outputs: list[_Any] = []
    active: set[int] = set()

    while stack:
        action = stack.pop()
        kind = action[0]

        if kind == "visit":
            _, current, current_path = action
            current_type = type(current)

            if current is None or current_type in (
                bool,
                int,
                str,
                _datetime,
            ):
                outputs.append(_snapshot_scalar(current, current_path))
                continue

            if current_type is list or current_type is tuple:
                identity = id(current)
                if identity in active:
                    _contract_error(
                        current_path,
                        "cyclic container graph is not permitted",
                    )
                items = _capture_sequence_items(current, current_path)
                active.add(identity)
                stack.append(
                    ("assemble_sequence", identity, len(items), current_path)
                )
                for index in range(len(items) - 1, -1, -1):
                    stack.append(
                        (
                            "visit",
                            items[index],
                            f"{current_path}[{index}]",
                        )
                    )
                continue

            if current_type is dict:
                identity = id(current)
                if identity in active:
                    _contract_error(
                        current_path,
                        "cyclic container graph is not permitted",
                    )
                items = _capture_mapping_items(current, current_path)
                active.add(identity)
                keys = tuple(key for key, _ in items)
                stack.append(
                    (
                        "assemble_mapping",
                        identity,
                        keys,
                        len(items),
                        current_path,
                    )
                )
                for index in range(len(items) - 1, -1, -1):
                    key, item = items[index]
                    stack.append(
                        (
                            "visit",
                            item,
                            f"{current_path}.{key}",
                        )
                    )
                continue

            _contract_error(
                current_path,
                "unsupported projection-value type",
            )

        if kind == "assemble_sequence":
            _, identity, count, _ = action
            if count:
                values = tuple(outputs[-count:])
                del outputs[-count:]
            else:
                values = ()
            active.remove(identity)
            outputs.append(values)
            continue

        if kind == "assemble_mapping":
            _, identity, keys, count, _ = action
            if count:
                values = tuple(outputs[-count:])
                del outputs[-count:]
            else:
                values = ()
            active.remove(identity)
            outputs.append(
                _FrozenMapping(tuple(zip(keys, values, strict=True)))
            )
            continue

    if len(outputs) != 1:
        _contract_error(field_path, "snapshot assembly failed")
    return outputs[0]


@_dataclass(frozen=True, slots=True)
class NormalizedEvidenceBytesRequest:
    observation_id: str
    observation_envelope_version: str
    source_id: str
    source_class: str
    tenant_id: str
    subject_id: str
    subject_type: str
    environment_id: str
    scope_id: str
    release_binding: str | None
    observed_at: _datetime
    received_at: _datetime
    applicable_time: _datetime | None
    valid_from: _datetime | None
    valid_until: _datetime | None
    representation: str
    representation_version: str
    integrity_reference: str
    integrity_mechanism_version: str
    provenance_chain_reference: str
    provenance_version: str
    content_reference: str
    normalized_content: object
    normalized_content_identity: str
    trusted_evaluation_time: _datetime | None
    freshness_policy: object | None
    freshness_policy_version: str | None
    eligibility_policy_version: str
    evidence_model_version: str
    release_binding_present: bool
    applicable_time_present: bool
    validity_interval_present: bool
    trusted_evaluation_time_present: bool
    freshness_policy_present: bool
    maximum_normalized_evidence_bytes: int
    resource_policy_version: str

    def __post_init__(self) -> None:
        string_fields = (
            "observation_id",
            "observation_envelope_version",
            "source_id",
            "source_class",
            "tenant_id",
            "subject_id",
            "subject_type",
            "environment_id",
            "scope_id",
            "representation",
            "representation_version",
            "integrity_reference",
            "integrity_mechanism_version",
            "provenance_chain_reference",
            "provenance_version",
            "content_reference",
            "normalized_content_identity",
            "eligibility_policy_version",
            "evidence_model_version",
            "resource_policy_version",
        )
        for name in string_fields:
            _require_exact_str(getattr(self, name), name)

        _require_exact_str(
            self.release_binding,
            "release_binding",
            allow_none=True,
        )
        _require_exact_str(
            self.freshness_policy_version,
            "freshness_policy_version",
            allow_none=True,
        )

        _require_exact_datetime(self.observed_at, "observed_at")
        _require_exact_datetime(self.received_at, "received_at")
        _require_exact_datetime(
            self.applicable_time,
            "applicable_time",
            allow_none=True,
        )
        _require_exact_datetime(
            self.valid_from,
            "valid_from",
            allow_none=True,
        )
        _require_exact_datetime(
            self.valid_until,
            "valid_until",
            allow_none=True,
        )
        _require_exact_datetime(
            self.trusted_evaluation_time,
            "trusted_evaluation_time",
            allow_none=True,
        )

        presence_fields = (
            "release_binding_present",
            "applicable_time_present",
            "validity_interval_present",
            "trusted_evaluation_time_present",
            "freshness_policy_present",
        )
        for name in presence_fields:
            _require_exact_bool(getattr(self, name), name)

        _require_exact_nonnegative_int(
            self.maximum_normalized_evidence_bytes,
            "maximum_normalized_evidence_bytes",
        )

        if not self.release_binding_present and self.release_binding is not None:
            _contract_error(
                "release_binding",
                "must be None when release_binding_present is false",
            )

        if not self.applicable_time_present and self.applicable_time is not None:
            _contract_error(
                "applicable_time",
                "must be None when applicable_time_present is false",
            )

        if not self.validity_interval_present:
            if self.valid_from is not None or self.valid_until is not None:
                _contract_error(
                    "validity_interval",
                    "valid_from and valid_until must both be None when "
                    "validity_interval_present is false",
                )

        if (
            not self.trusted_evaluation_time_present
            and self.trusted_evaluation_time is not None
        ):
            _contract_error(
                "trusted_evaluation_time",
                "must be None when trusted_evaluation_time_present is false",
            )

        if not self.freshness_policy_present:
            if (
                self.freshness_policy is not None
                or self.freshness_policy_version is not None
            ):
                _contract_error(
                    "freshness_policy",
                    "freshness_policy and freshness_policy_version must both "
                    "be None when freshness_policy_present is false",
                )

        normalized_snapshot = _deep_snapshot(
            self.normalized_content,
            "normalized_content",
        )
        object.__setattr__(
            self,
            "normalized_content",
            normalized_snapshot,
        )

        if self.freshness_policy_present:
            freshness_snapshot = _deep_snapshot(
                self.freshness_policy,
                "freshness_policy",
            )
            object.__setattr__(
                self,
                "freshness_policy",
                freshness_snapshot,
            )


@_dataclass(frozen=True, slots=True)
class NormalizedEvidenceBytesLimitFailure:
    code: str
    classification: str
    resource_reference: str
    semantic_location: str
    resource_policy_version: str
    safe_context_maximum_normalized_evidence_bytes: int
    construction_state: str

    def __post_init__(self) -> None:
        _require_exact_str(self.code, "failure.code")
        _require_exact_str(
            self.classification,
            "failure.classification",
        )
        _require_exact_str(
            self.resource_reference,
            "failure.resource_reference",
        )
        _require_exact_str(
            self.semantic_location,
            "failure.semantic_location",
        )
        _require_exact_str(
            self.resource_policy_version,
            "failure.resource_policy_version",
        )
        _require_exact_nonnegative_int(
            self.safe_context_maximum_normalized_evidence_bytes,
            "failure.safe_context_maximum_normalized_evidence_bytes",
        )
        _require_exact_str(
            self.construction_state,
            "failure.construction_state",
        )

        if self.code != NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED:
            _contract_error(
                "failure.code",
                "must equal NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED",
            )
        if self.classification != _PROCESSING_FAILURE:
            _contract_error(
                "failure.classification",
                "must equal PROCESSING_FAILURE",
            )
        if self.resource_reference != _RESOURCE_REFERENCE:
            _contract_error(
                "failure.resource_reference",
                "must equal normalized_evidence_bytes",
            )
        if self.semantic_location != _SEMANTIC_LOCATION:
            _contract_error(
                "failure.semantic_location",
                "must equal normalized_evidence_bytes",
            )
        if self.construction_state != _STOPPED_BEFORE_EVIDENCE_CONSTRUCTION:
            _contract_error(
                "failure.construction_state",
                "must equal STOPPED_BEFORE_EVIDENCE_CONSTRUCTION",
            )


@_dataclass(frozen=True, slots=True)
class NormalizedEvidenceBytesLimitResult:
    within_limit: bool
    normalized_evidence_bytes: int | None
    failure: NormalizedEvidenceBytesLimitFailure | None

    def __post_init__(self) -> None:
        _require_exact_bool(self.within_limit, "result.within_limit")

        if self.within_limit:
            _require_exact_nonnegative_int(
                self.normalized_evidence_bytes,
                "result.normalized_evidence_bytes",
            )
            if self.failure is not None:
                _contract_error(
                    "result.failure",
                    "must be None when within_limit is true",
                )
            return

        if self.normalized_evidence_bytes is not None:
            _contract_error(
                "result.normalized_evidence_bytes",
                "must be None when within_limit is false",
            )
        if type(self.failure) is not NormalizedEvidenceBytesLimitFailure:
            _contract_error(
                "result.failure",
                "must be NormalizedEvidenceBytesLimitFailure when "
                "within_limit is false",
            )


def _projection(request: NormalizedEvidenceBytesRequest) -> _FrozenMapping:
    entries: list[tuple[str, _Any]] = [
        ("projection_schema_version", _PROJECTION_SCHEMA_VERSION),
        (
            "projection_serialization_version",
            _PROJECTION_SERIALIZATION_VERSION,
        ),
        ("observation_id", request.observation_id),
        (
            "observation_envelope_version",
            request.observation_envelope_version,
        ),
        ("source_id", request.source_id),
        ("source_class", request.source_class),
        ("tenant_id", request.tenant_id),
        ("subject_id", request.subject_id),
        ("subject_type", request.subject_type),
        ("environment_id", request.environment_id),
        ("scope_id", request.scope_id),
    ]

    if request.release_binding_present:
        entries.append(("release_binding", request.release_binding))

    entries.extend(
        (
            ("observed_at", request.observed_at),
            ("received_at", request.received_at),
        )
    )

    if request.applicable_time_present:
        entries.append(("applicable_time", request.applicable_time))

    if request.validity_interval_present:
        entries.extend(
            (
                ("valid_from", request.valid_from),
                ("valid_until", request.valid_until),
            )
        )

    entries.extend(
        (
            ("representation", request.representation),
            ("representation_version", request.representation_version),
            ("integrity_reference", request.integrity_reference),
            (
                "integrity_mechanism_version",
                request.integrity_mechanism_version,
            ),
            (
                "provenance_chain_reference",
                request.provenance_chain_reference,
            ),
            ("provenance_version", request.provenance_version),
            ("content_reference", request.content_reference),
            ("normalized_content", request.normalized_content),
            (
                "normalized_content_identity",
                request.normalized_content_identity,
            ),
        )
    )

    if request.trusted_evaluation_time_present:
        entries.append(
            (
                "trusted_evaluation_time",
                request.trusted_evaluation_time,
            )
        )

    if request.freshness_policy_present:
        entries.extend(
            (
                ("freshness_policy", request.freshness_policy),
                (
                    "freshness_policy_version",
                    request.freshness_policy_version,
                ),
            )
        )

    entries.extend(
        (
            (
                "eligibility_policy_version",
                request.eligibility_policy_version,
            ),
            ("evidence_model_version", request.evidence_model_version),
            (
                "optional_field_presence",
                _FrozenMapping(
                    (
                        (
                            "release_binding",
                            request.release_binding_present,
                        ),
                        (
                            "applicable_time",
                            request.applicable_time_present,
                        ),
                        (
                            "validity_interval",
                            request.validity_interval_present,
                        ),
                        (
                            "trusted_evaluation_time",
                            request.trusted_evaluation_time_present,
                        ),
                        (
                            "freshness_policy",
                            request.freshness_policy_present,
                        ),
                    )
                ),
            ),
        )
    )

    return _FrozenMapping(tuple(entries))


def _validate_projection_formability(value: _Any) -> None:
    stack: list[tuple[_Any, str]] = [(value, "$")]

    while stack:
        current, path = stack.pop()
        current_type = type(current)

        if current is None or current_type in (bool, int):
            continue

        if current_type is str:
            _validate_unicode_string(current, path)
            continue

        if current_type is _datetime:
            _require_exact_datetime(current, path)
            continue

        if current_type is tuple:
            for index in range(len(current) - 1, -1, -1):
                stack.append((current[index], f"{path}[{index}]"))
            continue

        if current_type is _FrozenMapping:
            observed: set[str] = set()
            for key, item in current.entries:
                if type(key) is not str:
                    _contract_error(
                        f"{path}.<key>",
                        "mapping key must be an exact str",
                    )
                key_identity = _canonical_key_identity(
                    key,
                    f"{path}.<key>",
                )
                if key_identity in observed:
                    _contract_error(
                        path,
                        "mapping keys collide after NFC normalization",
                    )
                observed.add(key_identity)
                stack.append((item, f"{path}.{key}"))
            continue

        _contract_error(path, "unsupported snapshotted value type")


def _render_datetime(value: _datetime, field_path: str) -> str:
    _require_exact_datetime(value, field_path)
    utc_value = value.astimezone(_timezone.utc)
    if utc_value.microsecond:
        return utc_value.isoformat(
            timespec="microseconds"
        ).replace("+00:00", "Z")
    return utc_value.isoformat(timespec="seconds").replace("+00:00", "Z")


class _LimitExceededSignal(Exception):
    __slots__ = ()


class _CountingSink:
    __slots__ = ("maximum", "count")

    def __init__(self, maximum: int) -> None:
        self.maximum = maximum
        self.count = 0

    def remaining_capacity(self) -> int:
        return self.maximum - self.count

    def emit(self, value: bytes) -> None:
        next_count = self.count + len(value)
        if next_count > self.maximum:
            raise _LimitExceededSignal
        self.count = next_count


class _BufferSink:
    __slots__ = ("buffer",)

    def __init__(self) -> None:
        self.buffer = bytearray()

    def remaining_capacity(self) -> None:
        return None

    def emit(self, value: bytes) -> None:
        self.buffer.extend(value)

    def finish(self) -> bytes:
        return bytes(self.buffer)


def _emit_json_string(
    value: str,
    sink: _Any,
    field_path: str,
) -> None:
    for octet in _iter_json_string_octets(value, field_path):
        sink.emit(bytes((octet,)))


def _emit_integer(value: int, sink: _Any) -> None:
    """Emit exact base-10 ASCII without Python int-to-string conversion."""

    if type(value) is not int:
        _contract_error("$", "integer serializer requires exact int")

    magnitude = -value if value < 0 else value
    if value < 0:
        sink.emit(b"-")

    if magnitude == 0:
        sink.emit(b"0")
        return

    remaining = sink.remaining_capacity()
    if remaining is not None and remaining <= 0:
        raise _LimitExceededSignal

    divisor = 1
    digit_count = 1
    while magnitude >= divisor * 10:
        if remaining is not None and digit_count >= remaining:
            raise _LimitExceededSignal
        divisor *= 10
        digit_count += 1

    remainder = magnitude
    while divisor:
        digit, remainder = divmod(remainder, divisor)
        sink.emit(bytes((0x30 + digit,)))
        divisor //= 10


def _sorted_mapping_entries(
    value: _FrozenMapping,
    field_path: str,
) -> tuple[tuple[str, _Any], ...]:
    return tuple(
        sorted(
            value.entries,
            key=lambda entry: _CanonicalKeyOrder(
                entry[0],
                f"{field_path}.<key>",
            ),
        )
    )


def _serialize_value(value: _Any, sink: _Any) -> None:
    stack: list[tuple[str, _Any, str]] = [("value", value, "$")]

    while stack:
        action, current, path = stack.pop()

        if action == "bytes":
            sink.emit(current)
            continue

        if action == "json_string":
            _emit_json_string(current, sink, path)
            continue

        current_type = type(current)

        if current is None:
            sink.emit(b"null")
            continue
        if current_type is bool:
            sink.emit(b"true" if current else b"false")
            continue
        if current_type is int:
            _emit_integer(current, sink)
            continue
        if current_type is str:
            _emit_json_string(current, sink, path)
            continue
        if current_type is _datetime:
            _emit_json_string(
                _render_datetime(current, path),
                sink,
                path,
            )
            continue
        if current_type is tuple:
            stack.append(("bytes", b"]", path))
            for index in range(len(current) - 1, -1, -1):
                if index < len(current) - 1:
                    stack.append(("bytes", b",", path))
                stack.append(
                    (
                        "value",
                        current[index],
                        f"{path}[{index}]",
                    )
                )
            stack.append(("bytes", b"[", path))
            continue
        if current_type is _FrozenMapping:
            entries = _sorted_mapping_entries(current, path)
            stack.append(("bytes", b"}", path))
            for index in range(len(entries) - 1, -1, -1):
                key, item = entries[index]
                if index < len(entries) - 1:
                    stack.append(("bytes", b",", path))
                stack.append(
                    (
                        "value",
                        item,
                        f"{path}.{key}",
                    )
                )
                stack.append(("bytes", b":", path))
                stack.append(("json_string", key, f"{path}.<key>"))
            stack.append(("bytes", b"{", path))
            continue

        _contract_error(path, "unsupported snapshotted value type")


def _emit_projection_bytes(
    request: NormalizedEvidenceBytesRequest,
) -> bytes:
    """Module-private deterministic emitter for authorized unit/vector tests."""

    if type(request) is not NormalizedEvidenceBytesRequest:
        _contract_error(
            "request",
            "must be NormalizedEvidenceBytesRequest",
        )
    projection = _projection(request)
    _validate_projection_formability(projection)
    sink = _BufferSink()
    _serialize_value(projection, sink)
    return sink.finish()


def _limit_failure(
    request: NormalizedEvidenceBytesRequest,
) -> NormalizedEvidenceBytesLimitFailure:
    return NormalizedEvidenceBytesLimitFailure(
        code=NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED,
        classification=_PROCESSING_FAILURE,
        resource_reference=_RESOURCE_REFERENCE,
        semantic_location=_SEMANTIC_LOCATION,
        resource_policy_version=request.resource_policy_version,
        safe_context_maximum_normalized_evidence_bytes=(
            request.maximum_normalized_evidence_bytes
        ),
        construction_state=_STOPPED_BEFORE_EVIDENCE_CONSTRUCTION,
    )


def evaluate_normalized_evidence_bytes_limit(
    request: NormalizedEvidenceBytesRequest,
) -> NormalizedEvidenceBytesLimitResult:
    """Evaluate the final pre-construction normalized-evidence byte limit."""

    if type(request) is not NormalizedEvidenceBytesRequest:
        _contract_error(
            "request",
            "must be NormalizedEvidenceBytesRequest",
        )

    projection = _projection(request)
    _validate_projection_formability(projection)

    sink = _CountingSink(request.maximum_normalized_evidence_bytes)
    try:
        _serialize_value(projection, sink)
    except _LimitExceededSignal:
        return NormalizedEvidenceBytesLimitResult(
            within_limit=False,
            normalized_evidence_bytes=None,
            failure=_limit_failure(request),
        )

    return NormalizedEvidenceBytesLimitResult(
        within_limit=True,
        normalized_evidence_bytes=sink.count,
        failure=None,
    )
