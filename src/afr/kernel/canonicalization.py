"""Deterministic, resource-bounded canonical byte production.

This module performs canonical representation only. It performs no hashing,
fingerprinting, evaluation, filesystem access, networking, persistence,
integration, deployment, or runtime action.

The caller must supply the byte length measured at the governed ingress
boundary. This module validates that measurement against the bound resource
contract; it does not misrepresent canonical output length as input length.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import fields, is_dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any
import unicodedata

from .contracts import (
    ContractValidationError,
    Identifier,
    OptionalValue,
    ProcessingFailure,
    ProcessingFailureCode,
    ResourceLimits,
    SemanticVersion,
)


CANONICALIZATION_VERSION = SemanticVersion("1.0.0")


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


class _Budget:
    __slots__ = (
        "limits",
        "collection_items",
        "work_units",
    )

    def __init__(self, limits: ResourceLimits) -> None:
        if not isinstance(limits, ResourceLimits):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                "limits",
                "limits must be ResourceLimits",
            )

        if limits.version != CANONICALIZATION_VERSION:
            _fail(
                ProcessingFailureCode.INVALID_VERSION,
                "limits.version",
                "resource-limit version must equal "
                "CANONICALIZATION_VERSION",
            )

        self.limits = limits
        self.collection_items = 0
        self.work_units = 0

    def work(self, field_path: str, amount: int = 1) -> None:
        self.work_units += amount

        if self.work_units > self.limits.maximum_work_units:
            _fail(
                ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
                field_path,
                "maximum deterministic work units exceeded",
            )

    def collection(
        self,
        field_path: str,
        amount: int,
    ) -> None:
        self.collection_items += amount

        if (
            self.collection_items
            > self.limits.maximum_collection_items
        ):
            _fail(
                ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
                field_path,
                "maximum collection cardinality exceeded",
            )

    def depth(self, field_path: str, depth: int) -> None:
        if depth > self.limits.maximum_nesting_depth:
            _fail(
                ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
                field_path,
                "maximum nesting depth exceeded",
            )


class _Emitter:
    __slots__ = ("_buffer", "_maximum_bytes")

    def __init__(self, maximum_bytes: int) -> None:
        self._buffer = bytearray()
        self._maximum_bytes = maximum_bytes

    def emit(self, value: bytes, field_path: str) -> None:
        if not isinstance(value, bytes):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                field_path,
                "canonical emission must be bytes",
            )

        remaining = self._maximum_bytes - len(self._buffer)

        if len(value) > remaining:
            _fail(
                ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
                field_path,
                "maximum canonical byte size exceeded",
            )

        self._buffer.extend(value)

    def finish(self) -> bytes:
        return bytes(self._buffer)


def _validate_input_byte_length(
    input_byte_length: int,
    limits: ResourceLimits,
) -> None:
    if (
        not isinstance(input_byte_length, int)
        or isinstance(input_byte_length, bool)
    ):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            "input_byte_length",
            "input byte length must be an integer",
        )

    if input_byte_length < 0:
        _fail(
            ProcessingFailureCode.INVALID_RESOURCE_LIMIT,
            "input_byte_length",
            "input byte length cannot be negative",
        )

    if input_byte_length > limits.maximum_input_bytes:
        _fail(
            ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
            "input_byte_length",
            "maximum governed ingress byte size exceeded",
        )


def _normalized_string(value: str, field_path: str) -> str:
    if not isinstance(value, str):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "canonical string value must be str",
        )

    normalized = unicodedata.normalize("NFC", value)

    for character in normalized:
        code_point = ord(character)

        if 0xD800 <= code_point <= 0xDFFF:
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                field_path,
                "unpaired Unicode surrogate is not canonicalizable",
            )

    return normalized


def _emit_json_string(
    value: str,
    budget: _Budget,
    emitter: _Emitter,
    field_path: str,
) -> None:
    normalized = _normalized_string(value, field_path)
    emitter.emit(b'"', field_path)

    for character in normalized:
        budget.work(field_path)
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

        emitter.emit(encoded, field_path)

    emitter.emit(b'"', field_path)


def _canonical_key_bytes(
    value: str,
    budget: _Budget,
    field_path: str,
) -> bytes:
    key_emitter = _Emitter(
        budget.limits.maximum_canonical_bytes
    )

    _emit_json_string(
        value,
        budget,
        key_emitter,
        field_path,
    )

    return key_emitter.finish()


def _emit_integer(
    value: int,
    emitter: _Emitter,
    field_path: str,
) -> None:
    maximum_bytes = emitter._maximum_bytes

    if value.bit_length() > max(1, maximum_bytes * 4):
        _fail(
            ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
            field_path,
            "integer representation exceeds the canonical byte bound",
        )

    try:
        encoded = str(value).encode("ascii")
    except ValueError:
        _fail(
            ProcessingFailureCode.RESOURCE_LIMIT_EXCEEDED,
            field_path,
            "integer representation exceeds interpreter safety bounds",
        )

    emitter.emit(encoded, field_path)


def _mapping_entries(
    value: Mapping[Any, Any],
    budget: _Budget,
    field_path: str,
) -> list[tuple[bytes, str, Any]]:
    budget.collection(field_path, len(value))

    entries: list[tuple[bytes, str, Any]] = []
    observed_keys: set[bytes] = set()

    for key, item in value.items():
        budget.work(field_path)

        if not isinstance(key, str):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                field_path,
                "canonical mapping keys must be strings",
            )

        key_bytes = _canonical_key_bytes(
            key,
            budget,
            f"{field_path}.<key>",
        )

        if key_bytes in observed_keys:
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                field_path,
                "mapping keys collide after NFC normalization",
            )

        observed_keys.add(key_bytes)
        entries.append((key_bytes, key, item))

    entries.sort(key=lambda entry: entry[0])
    return entries


def _emit_mapping(
    value: Mapping[Any, Any],
    budget: _Budget,
    emitter: _Emitter,
    field_path: str,
    depth: int,
) -> None:
    entries = _mapping_entries(
        value,
        budget,
        field_path,
    )

    emitter.emit(b"{", field_path)

    for index, (key_bytes, key, item) in enumerate(entries):
        if index:
            emitter.emit(b",", field_path)

        emitter.emit(key_bytes, f"{field_path}.<key>")
        emitter.emit(b":", field_path)

        item_path = (
            f"{field_path}.{key}"
            if field_path
            else key
        )

        _encode(
            item,
            budget,
            emitter,
            item_path,
            depth + 1,
        )

    emitter.emit(b"}", field_path)


def _emit_dataclass(
    value: Any,
    budget: _Budget,
    emitter: _Emitter,
    field_path: str,
    depth: int,
) -> None:
    entries: list[tuple[bytes, str, Any]] = []

    dataclass_fields = fields(value)
    budget.collection(field_path, len(dataclass_fields))

    for field in dataclass_fields:
        budget.work(field_path)
        item = getattr(value, field.name)

        if isinstance(item, OptionalValue):
            if not item.present:
                continue

            item = item.value

        key_bytes = _canonical_key_bytes(
            field.name,
            budget,
            f"{field_path}.{field.name}.<key>",
        )

        entries.append((key_bytes, field.name, item))

    entries.sort(key=lambda entry: entry[0])

    emitter.emit(b"{", field_path)

    for index, (key_bytes, name, item) in enumerate(entries):
        if index:
            emitter.emit(b",", field_path)

        emitter.emit(
            key_bytes,
            f"{field_path}.{name}.<key>",
        )
        emitter.emit(b":", field_path)

        _encode(
            item,
            budget,
            emitter,
            f"{field_path}.{name}",
            depth + 1,
        )

    emitter.emit(b"}", field_path)


def _emit_sequence(
    value: Sequence[Any],
    budget: _Budget,
    emitter: _Emitter,
    field_path: str,
    depth: int,
) -> None:
    budget.collection(field_path, len(value))
    emitter.emit(b"[", field_path)

    for index, item in enumerate(value):
        if index:
            emitter.emit(b",", field_path)

        _encode(
            item,
            budget,
            emitter,
            f"{field_path}[{index}]",
            depth + 1,
        )

    emitter.emit(b"]", field_path)


def _encode(
    value: Any,
    budget: _Budget,
    emitter: _Emitter,
    field_path: str,
    depth: int,
) -> None:
    budget.depth(field_path, depth)
    budget.work(field_path)

    if value is None:
        emitter.emit(b"null", field_path)
        return

    if isinstance(value, bool):
        emitter.emit(
            b"true" if value else b"false",
            field_path,
        )
        return

    if isinstance(value, int):
        _emit_integer(value, emitter, field_path)
        return

    if isinstance(value, float):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "floating-point values are not canonicalizable",
        )

    if isinstance(value, str):
        _emit_json_string(
            value,
            budget,
            emitter,
            field_path,
        )
        return

    if isinstance(value, bytes):
        _fail(
            ProcessingFailureCode.INVALID_TYPE,
            field_path,
            "raw bytes require an explicitly typed representation",
        )

    if isinstance(value, Identifier):
        _emit_json_string(
            value.value,
            budget,
            emitter,
            field_path,
        )
        return

    if isinstance(value, SemanticVersion):
        _emit_json_string(
            value.value,
            budget,
            emitter,
            field_path,
        )
        return

    if isinstance(value, datetime):
        if value.tzinfo is None or value.utcoffset() is None:
            _fail(
                ProcessingFailureCode.INVALID_TIMESTAMP,
                field_path,
                "canonical timestamp must be timezone-aware",
            )

        utc_value = value.astimezone(timezone.utc)

        if utc_value.microsecond:
            rendered = utc_value.isoformat(
                timespec="microseconds"
            ).replace("+00:00", "Z")
        else:
            rendered = utc_value.isoformat(
                timespec="seconds"
            ).replace("+00:00", "Z")

        _emit_json_string(
            rendered,
            budget,
            emitter,
            field_path,
        )
        return

    if isinstance(value, Enum):
        _encode(
            value.value,
            budget,
            emitter,
            field_path,
            depth + 1,
        )
        return

    if isinstance(value, OptionalValue):
        if not value.present:
            _fail(
                ProcessingFailureCode.MISSING_REQUIRED_FIELD,
                field_path,
                "standalone missing value has no canonical representation",
            )

        _encode(
            value.value,
            budget,
            emitter,
            field_path,
            depth + 1,
        )
        return

    if is_dataclass(value) and not isinstance(value, type):
        _emit_dataclass(
            value,
            budget,
            emitter,
            field_path,
            depth,
        )
        return

    if isinstance(value, Mapping):
        _emit_mapping(
            value,
            budget,
            emitter,
            field_path,
            depth,
        )
        return

    if (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes, bytearray))
    ):
        _emit_sequence(
            value,
            budget,
            emitter,
            field_path,
            depth,
        )
        return

    _fail(
        ProcessingFailureCode.INVALID_TYPE,
        field_path,
        f"unsupported canonical value type: {type(value).__name__}",
    )


def canonicalize(
    value: Any,
    limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> bytes:
    """Produce bounded deterministic canonical UTF-8 bytes.

    ``input_byte_length`` must be measured by the governed ingress boundary
    before parsing or typed-contract construction. Supplying that measurement
    does not grant this module authority to read an input source.

    Missing dataclass fields represented by ``OptionalValue.missing()`` are
    omitted. Explicit null fields represented by ``OptionalValue.of(None)``
    are emitted as JSON null.
    """

    budget = _Budget(limits)

    _validate_input_byte_length(
        input_byte_length,
        limits,
    )

    emitter = _Emitter(limits.maximum_canonical_bytes)

    _encode(
        value,
        budget,
        emitter,
        "$",
        1,
    )

    return emitter.finish()
