"""Deterministic Phase 12 S5A conformance-summary projection.

This module projects one accepted, scope-compatible Phase 12 finding set into an
immutable deterministic Architecture Conformance Score representation. The v1
formula keeps every accepted finding in the denominator, excludes nothing, and
fails closed by making the score unavailable whenever an eligible finding is
STALE, INCONCLUSIVE, or EVIDENCE_UNAVAILABLE.

The score is derived presentation state only. It performs no persistence,
provider/network I/O, Command Center shell mutation, architecture approval,
remediation, certificate signing/issuance/publication, NEXUS mutation, runtime
action, or authority grant.
"""

from __future__ import annotations

from dataclasses import dataclass

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


SCORE_CONTRACT_VERSION = SemanticVersion("1.0.0")
SCORE_FORMULA_ID = Identifier("afr.score.all-findings-supported-basis-points")
SCORE_FORMULA_VERSION = SemanticVersion("1.0.0")
ACCEPTED_FINDING_SET_STATUS = Identifier("ACCEPTED")
SCORE_SCALE_BASIS_POINTS = 10_000
_UNRESOLVED_SCORE_STATES = frozenset(
    {
        FindingState.STALE,
        FindingState.INCONCLUSIVE,
        FindingState.EVIDENCE_UNAVAILABLE,
    }
)


@dataclass(frozen=True, slots=True)
class ConformanceScoreSummary:
    """Exact immutable 14-field Phase 12 Architecture Conformance Score."""

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
    limitations: tuple[Identifier, ...]


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
) -> tuple[Identifier, ...]:
    combined = tuple(inherited) + tuple(additional)
    for index, item in enumerate(combined):
        if not isinstance(item, Identifier):
            _fail(
                ProcessingFailureCode.INVALID_TYPE,
                f"limitations[{index}]",
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


def _summary_payload(summary: ConformanceScoreSummary) -> dict[str, object]:
    return {
        "contradicted_count": summary.contradicted_count,
        "eligible_finding_count": summary.eligible_finding_count,
        "evidence_unavailable_count": summary.evidence_unavailable_count,
        "excluded_count": summary.excluded_count,
        "finding_set_id": summary.finding_set_id.value,
        "inconclusive_count": summary.inconclusive_count,
        "limitations": [item.value for item in summary.limitations],
        "score_contract_version": summary.score_contract_version.value,
        "score_formula_id": summary.score_formula_id.value,
        "score_formula_version": summary.score_formula_version.value,
        "score_value_or_unavailable": {
            "present": summary.score_value_or_unavailable.present,
            "value": summary.score_value_or_unavailable.value,
        },
        "stale_count": summary.stale_count,
        "supported_count": summary.supported_count,
    }


def canonical_score_summary_bytes(
    summary: ConformanceScoreSummary,
    resource_limits: ResourceLimits,
    *,
    input_byte_length: int,
) -> bytes:
    """Reproduce canonical bytes bound by ``score_fingerprint``."""

    _require_instance(summary, ConformanceScoreSummary, "summary")
    _require_instance(resource_limits, ResourceLimits, "resource_limits")
    return canonicalize(
        _summary_payload(summary),
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
    if finding_set_status != ACCEPTED_FINDING_SET_STATUS:
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
    finding_ids: set[str] = set()
    claim_ids: set[str] = set()

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
        if finding.finding_id.value in finding_ids:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "findings",
                "duplicate finding_id values are prohibited",
            )
        finding_ids.add(finding.finding_id.value)
        if finding.claim_id.value in claim_ids:
            _fail(
                ProcessingFailureCode.INVALID_IDENTIFIER,
                "findings",
                "duplicate claim_id values are prohibited in one score set",
            )
        claim_ids.add(finding.claim_id.value)

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
        "finding_derivation_policy_id",
        "finding_derivation_policy_version",
        "evaluator_id",
        "evaluator_version",
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
                    "all findings must share one compatible score scope",
                )
    return ordered


def project_conformance_summary(
    *,
    score_contract_version: SemanticVersion,
    finding_set_status: Identifier,
    findings: tuple[ConformanceFinding, ...],
    score_formula_id: Identifier,
    score_formula_version: SemanticVersion,
    additional_limitations: tuple[Identifier, ...],
    resource_limits: ResourceLimits,
    input_byte_length: int,
) -> ConformanceScoreSummary:
    """Project one immutable deterministic Phase 12 conformance summary."""

    required = (
        ("score_contract_version", score_contract_version, SemanticVersion),
        ("score_formula_id", score_formula_id, Identifier),
        ("score_formula_version", score_formula_version, SemanticVersion),
        ("resource_limits", resource_limits, ResourceLimits),
    )
    for field_path, value, expected_type in required:
        _require_instance(value, expected_type, field_path)

    if score_contract_version != SCORE_CONTRACT_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "score_contract_version",
            "must equal SCORE_CONTRACT_VERSION",
        )
    if score_formula_id != SCORE_FORMULA_ID:
        _fail(
            ProcessingFailureCode.INVALID_IDENTIFIER,
            "score_formula_id",
            "must equal the accepted v1 score formula identity",
        )
    if score_formula_version != SCORE_FORMULA_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "score_formula_version",
            "must equal SCORE_FORMULA_VERSION",
        )
    if resource_limits.version != CANONICALIZATION_VERSION:
        _fail(
            ProcessingFailureCode.INVALID_VERSION,
            "resource_limits.version",
            "must equal CANONICALIZATION_VERSION",
        )

    ordered_findings = _validate_findings(
        findings,
        finding_set_status,
        resource_limits,
        input_byte_length=input_byte_length,
    )
    normalized_additional_limitations = _normalized_identifier_tuple(
        additional_limitations,
        "additional_limitations",
    )
    inherited_limitations = tuple(
        item
        for finding in ordered_findings
        for item in finding.limitations
    )
    limitations = _merge_identifier_tuples(
        inherited_limitations,
        normalized_additional_limitations,
    )

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

    state_counts = {
        state: sum(
            1 for finding in ordered_findings if finding.finding_state == state
        )
        for state in FindingState
    }
    eligible_finding_count = len(ordered_findings)
    excluded_count = 0
    unresolved_present = any(
        state_counts[state] > 0 for state in _UNRESOLVED_SCORE_STATES
    )
    if unresolved_present:
        score_value = OptionalValue.missing()
    else:
        score_value = OptionalValue.of(
            state_counts[FindingState.SUPPORTED]
            * SCORE_SCALE_BASIS_POINTS
            // eligible_finding_count
        )

    provisional = ConformanceScoreSummary(
        score_contract_version=score_contract_version,
        score_formula_id=score_formula_id,
        score_formula_version=score_formula_version,
        finding_set_id=finding_set_id,
        eligible_finding_count=eligible_finding_count,
        supported_count=state_counts[FindingState.SUPPORTED],
        contradicted_count=state_counts[FindingState.CONTRADICTED],
        stale_count=state_counts[FindingState.STALE],
        inconclusive_count=state_counts[FindingState.INCONCLUSIVE],
        evidence_unavailable_count=state_counts[
            FindingState.EVIDENCE_UNAVAILABLE
        ],
        excluded_count=excluded_count,
        score_value_or_unavailable=score_value,
        score_fingerprint=Fingerprint(
            algorithm="sha256",
            fingerprint_version=FINGERPRINT_VERSION,
            canonicalization_version=CANONICALIZATION_VERSION,
            digest_hex="0" * 64,
        ),
        limitations=limitations,
    )
    canonical_bytes = canonical_score_summary_bytes(
        provisional,
        resource_limits,
        input_byte_length=input_byte_length,
    )
    score_fingerprint = compute_fingerprint(
        canonical_bytes,
        resource_limits,
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )
    return ConformanceScoreSummary(
        score_contract_version=score_contract_version,
        score_formula_id=score_formula_id,
        score_formula_version=score_formula_version,
        finding_set_id=finding_set_id,
        eligible_finding_count=eligible_finding_count,
        supported_count=state_counts[FindingState.SUPPORTED],
        contradicted_count=state_counts[FindingState.CONTRADICTED],
        stale_count=state_counts[FindingState.STALE],
        inconclusive_count=state_counts[FindingState.INCONCLUSIVE],
        evidence_unavailable_count=state_counts[
            FindingState.EVIDENCE_UNAVAILABLE
        ],
        excluded_count=excluded_count,
        score_value_or_unavailable=score_value,
        score_fingerprint=score_fingerprint,
        limitations=limitations,
    )
