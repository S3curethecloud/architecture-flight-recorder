from __future__ import annotations

from dataclasses import replace as _shell_replace

from afr.conformance.conformance_summary import (
    ACCEPTED_FINDING_SET_STATUS as _SHELL_ACCEPTED_FINDING_SET_STATUS,
    project_conformance_summary as _shell_project_conformance_summary,
)
from afr.conformance.finding_derivation import (
    FINDING_CONTRACT_VERSION as _SHELL_FINDING_CONTRACT_VERSION,
    ConformanceFinding as _ShellConformanceFinding,
    FindingState as _ShellFindingState,
    canonical_finding_bytes as _shell_canonical_finding_bytes,
)
from afr.kernel.contracts import SemanticVersion as _ShellSemanticVersion


import ast
import json
import unittest
from dataclasses import FrozenInstanceError, replace
from datetime import datetime, timezone
from pathlib import Path

import afr.command_center.capability_registry as cr
import afr.command_center.read_model as rm
import afr.command_center.shell as sh
from afr.conformance.conformance_summary import (
    SCORE_CONTRACT_VERSION,
    SCORE_FORMULA_ID,
    SCORE_FORMULA_VERSION,
    ConformanceScoreSummary,
    canonical_score_summary_bytes,
)
from afr.kernel.canonicalization import CANONICALIZATION_VERSION
from afr.kernel.contracts import (
    ContractValidationError,
    Identifier,
    OptionalValue,
    ResourceLimits,
)
from afr.kernel.fingerprints import (
    FINGERPRINT_VERSION,
    Fingerprint,
    compute_fingerprint,
)


VECTOR = (
    Path(__file__).resolve().parents[2]
    / "vectors"
    / "command_center"
    / "command-center-foundation-v1.json"
)


def limits() -> ResourceLimits:
    return ResourceLimits(
        version=CANONICALIZATION_VERSION,
        maximum_input_bytes=1_000_000,
        maximum_collection_items=10_000,
        maximum_nesting_depth=64,
        maximum_canonical_bytes=1_000_000,
        maximum_work_units=1_000_000,
    )


def summary() -> ConformanceScoreSummary:
    provisional = ConformanceScoreSummary(
        score_contract_version=SCORE_CONTRACT_VERSION,
        score_formula_id=SCORE_FORMULA_ID,
        score_formula_version=SCORE_FORMULA_VERSION,
        finding_set_id=Identifier("finding-set.shell"),
        eligible_finding_count=2,
        supported_count=2,
        contradicted_count=0,
        stale_count=0,
        inconclusive_count=0,
        evidence_unavailable_count=0,
        excluded_count=0,
        score_value_or_unavailable=
            OptionalValue.of(10_000),
        score_fingerprint=Fingerprint(
            algorithm="sha256",
            fingerprint_version=FINGERPRINT_VERSION,
            canonicalization_version=CANONICALIZATION_VERSION,
            digest_hex="0" * 64,
        ),
        limitations=(),
    )

    fingerprint = compute_fingerprint(
        canonical_score_summary_bytes(
            provisional,
            limits(),
            input_byte_length=8192,
        ),
        limits(),
        canonicalization_version=CANONICALIZATION_VERSION,
        fingerprint_version=FINGERPRINT_VERSION,
    )

    return replace(
        provisional,
        score_fingerprint=fingerprint,
    )


def _shell_source_fixture():
    provisional = _ShellConformanceFinding(
        finding_contract_version=
            _SHELL_FINDING_CONTRACT_VERSION,
        finding_id=
            Identifier("finding.shell.synthetic.0001"),
        finding_state=
            _ShellFindingState.SUPPORTED,
        tenant_id=
            Identifier("tenant.synthetic"),
        subject_id=
            Identifier("subject.synthetic"),
        environment_id=
            Identifier("environment.synthetic"),
        release_id=
            Identifier("release.synthetic"),
        architecture_truth_reference_id=
            Identifier("architecture.synthetic"),
        claim_id=
            Identifier("claim.shell.synthetic.0001"),
        source_evaluation_cycle_id=
            Identifier("cycle.synthetic"),
        source_evaluation_result_id=
            Identifier("result.synthetic"),
        evidence_binding_or_set_id=
            Identifier("evidence.synthetic"),
        finding_derivation_policy_id=
            Identifier("policy.synthetic"),
        finding_derivation_policy_version=
            _ShellSemanticVersion("1.0.0"),
        evaluator_id=
            Identifier("evaluator.synthetic"),
        evaluator_version=
            _ShellSemanticVersion("1.0.0"),
        canonicalization_version=
            CANONICALIZATION_VERSION,
        fingerprint_version=
            FINGERPRINT_VERSION,
        trusted_time_context_id=
            Identifier("trusted-time.synthetic"),
        finding_valid_from=datetime(
            2026,
            11,
            10,
            19,
            0,
            tzinfo=timezone.utc,
        ),
        finding_valid_until=datetime(
            2026,
            11,
            10,
            21,
            0,
            tzinfo=timezone.utc,
        ),
        limitations=(
            Identifier("limitation.synthetic"),
        ),
        unresolved_conditions=(),
        finding_fingerprint=Fingerprint(
            algorithm="sha256",
            fingerprint_version=
                FINGERPRINT_VERSION,
            canonicalization_version=
                CANONICALIZATION_VERSION,
            digest_hex="0" * 64,
        ),
        supersedes_finding_id=
            OptionalValue.missing(),
    )

    finding_fingerprint = compute_fingerprint(
        _shell_canonical_finding_bytes(
            provisional,
            limits(),
            input_byte_length=8192,
        ),
        limits(),
        canonicalization_version=
            CANONICALIZATION_VERSION,
        fingerprint_version=
            FINGERPRINT_VERSION,
    )

    finding = _shell_replace(
        provisional,
        finding_fingerprint=
            finding_fingerprint,
    )

    findings = (finding,)

    summary = _shell_project_conformance_summary(
        score_contract_version=
            SCORE_CONTRACT_VERSION,
        finding_set_status=
            _SHELL_ACCEPTED_FINDING_SET_STATUS,
        findings=findings,
        score_formula_id=
            SCORE_FORMULA_ID,
        score_formula_version=
            SCORE_FORMULA_VERSION,
        additional_limitations=(),
        resource_limits=limits(),
        input_byte_length=8192,
    )

    binding = rm.build_source_scope_binding(
        summary=summary,
        source_findings=findings,
        resource_limits=limits(),
        input_byte_length=8192,
    )

    return summary, binding


def model():
    summary, binding = _shell_source_fixture()

    return rm.project_executive_status(
        summary=summary,
        source_scope_binding=binding,
        as_of_trusted_time=datetime(
            2026,
            11,
            10,
            20,
            0,
            tzinfo=timezone.utc,
        ),
        freshness_state=
            rm.FRESHNESS_CURRENT,
        availability_state=
            rm.AVAILABILITY_AVAILABLE,
        warnings=(
            Identifier("warning.synthetic"),
        ),
        resource_limits=limits(),
        input_byte_length=8192,
    )


class ShellTests(unittest.TestCase):
    def test_t01_foundation_shell_contains_exactly_one_surface(self) -> None:
        shell = sh.build_shell_snapshot(
            registry=cr.build_foundation_registry(),
            read_models=(model(),),
        )

        self.assertEqual(
            shell.shell_contract_version,
            sh.SHELL_CONTRACT_VERSION,
        )
        self.assertEqual(len(shell.surfaces), 1)
        self.assertEqual(
            shell.surfaces[0].surface_id,
            rm.EXECUTIVE_STATUS_SURFACE_ID,
        )

    def test_t02_get_surface_returns_exact_model(self) -> None:
        expected = model()

        shell = sh.build_shell_snapshot(
            registry=cr.build_foundation_registry(),
            read_models=(expected,),
        )

        actual = sh.get_surface(
            shell,
            rm.EXECUTIVE_STATUS_SURFACE_ID,
        )

        self.assertEqual(actual, expected)

    def test_t03_empty_shell_fails_closed(self) -> None:
        with self.assertRaises(ContractValidationError):
            sh.build_shell_snapshot(
                registry=cr.build_foundation_registry(),
                read_models=(),
            )

    def test_t04_multiple_models_fail_closed(self) -> None:
        first = model()
        second = model()

        with self.assertRaises(ContractValidationError):
            sh.build_shell_snapshot(
                registry=cr.build_foundation_registry(),
                read_models=(first, second),
            )

    def test_t05_execution_authority_cannot_be_injected(self) -> None:
        modified = replace(
            model(),
            authority_state=(
                Identifier("EXECUTION_AUTHORIZED"),
            ),
        )

        with self.assertRaises(ContractValidationError):
            sh.build_shell_snapshot(
                registry=cr.build_foundation_registry(),
                read_models=(modified,),
            )

    def test_t06_unregistered_surface_is_unavailable(self) -> None:
        shell = sh.build_shell_snapshot(
            registry=cr.build_foundation_registry(),
            read_models=(model(),),
        )

        with self.assertRaises(ContractValidationError):
            sh.get_surface(
                shell,
                Identifier("live_findings"),
            )

    def test_t07_tampered_registry_fails_closed(self) -> None:
        registry = replace(
            cr.build_foundation_registry(),
            registrations=(),
        )

        with self.assertRaises(ContractValidationError):
            sh.build_shell_snapshot(
                registry=registry,
                read_models=(model(),),
            )

    def test_t08_shell_is_immutable(self) -> None:
        shell = sh.build_shell_snapshot(
            registry=cr.build_foundation_registry(),
            read_models=(model(),),
        )

        with self.assertRaises(FrozenInstanceError):
            shell.surfaces = ()

    def test_t09_shell_has_no_execution_or_provider_actions(self) -> None:
        self.assertFalse(hasattr(sh, "execute"))
        self.assertFalse(hasattr(sh, "remediate"))
        self.assertFalse(hasattr(sh, "mutate_provider"))
        self.assertFalse(hasattr(sh, "issue_certificate"))
        self.assertFalse(hasattr(sh, "deploy"))

    def test_t10_vector_confirms_foundation_surface_only(self) -> None:
        data = json.loads(
            VECTOR.read_text(encoding="utf-8")
        )

        self.assertEqual(
            data["foundation_surface_id"],
            "executive_status",
        )
        self.assertEqual(
            [
                item.value
                for item
                in cr.FOUNDATION_IMPLEMENTED_SURFACE_IDS
            ],
            ["executive_status"],
        )
        self.assertEqual(
            len(data["stable_surface_ids"]),
            10,
        )

    def test_t11_no_external_side_effect_primitives(self) -> None:
        source = Path(sh.__file__).read_text(
            encoding="utf-8"
        )
        tree = ast.parse(source)

        imported_roots: set[str] = set()
        direct_calls: set[str] = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(
                    alias.name.split(".", 1)[0]
                    for alias in node.names
                )
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(
                    node.module.split(".", 1)[0]
                )
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
            ):
                direct_calls.add(node.func.id)

        self.assertLessEqual(
            imported_roots,
            {
                "__future__",
                "dataclasses",
                "afr",
            },
        )

        self.assertTrue(
            {
                "open",
                "exec",
                "eval",
                "print",
                "system",
            }.isdisjoint(direct_calls)
        )


if __name__ == "__main__":
    unittest.main()
