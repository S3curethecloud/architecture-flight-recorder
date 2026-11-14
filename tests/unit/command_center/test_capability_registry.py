from __future__ import annotations

import ast
import json
import unittest
from dataclasses import FrozenInstanceError, replace
from pathlib import Path

import afr.command_center.capability_registry as cr
from afr.kernel.contracts import (
    ContractValidationError,
    Identifier,
)


VECTOR = (
    Path(__file__).resolve().parents[2]
    / "vectors"
    / "command_center"
    / "command-center-foundation-v1.json"
)


class CapabilityRegistryTests(unittest.TestCase):
    def test_t01_all_ten_stable_surface_ids_are_declared(self) -> None:
        data = json.loads(
            VECTOR.read_text(encoding="utf-8")
        )

        self.assertEqual(
            [item.value for item in cr.STABLE_SURFACE_IDS],
            data["stable_surface_ids"],
        )
        self.assertEqual(len(cr.STABLE_SURFACE_IDS), 10)

    def test_t02_foundation_registers_executive_status_only(self) -> None:
        registry = cr.build_foundation_registry()

        self.assertEqual(len(registry.registrations), 1)

        registration = registry.registrations[0]

        self.assertEqual(
            registration.supported_surface_ids,
            cr.FOUNDATION_IMPLEMENTED_SURFACE_IDS,
        )
        self.assertEqual(
            tuple(
                item.value
                for item
                in registration.supported_surface_ids
            ),
            ("executive_status",),
        )

    def test_t03_capability_contract_fields_are_exact(self) -> None:
        registration = (
            cr.build_foundation_registry()
            .registrations[0]
        )

        self.assertEqual(
            registration.capability_id,
            cr.EXECUTIVE_STATUS_CAPABILITY_ID,
        )
        self.assertEqual(
            registration.read_write_posture,
            cr.READ_ONLY_POSTURE,
        )
        self.assertEqual(
            registration.adapter_class,
            cr.ADAPTER_CLASS_DECLARATIVE_ONLY,
        )
        self.assertEqual(
            registration.lifecycle_state,
            cr.FOUNDATION_LIFECYCLE_STATE,
        )

    def test_t04_registration_does_not_grant_authority(self) -> None:
        self.assertFalse(
            hasattr(cr, "grant_authority")
        )
        self.assertFalse(
            hasattr(cr, "invoke_adapter")
        )
        self.assertFalse(
            hasattr(cr, "mutate_provider")
        )

    def test_t05_duplicate_capability_id_fails_closed(self) -> None:
        registration = (
            cr.build_foundation_registry()
            .registrations[0]
        )

        with self.assertRaises(ContractValidationError):
            cr.build_registry(
                (
                    registration,
                    registration,
                )
            )

    def test_t06_unimplemented_surface_registration_fails_closed(self) -> None:
        registration = (
            cr.build_foundation_registry()
            .registrations[0]
        )

        modified = replace(
            registration,
            supported_surface_ids=(
                Identifier("live_findings"),
            ),
        )

        with self.assertRaises(ContractValidationError):
            cr.build_registry((modified,))

    def test_t07_write_posture_fails_closed(self) -> None:
        registration = (
            cr.build_foundation_registry()
            .registrations[0]
        )

        modified = replace(
            registration,
            read_write_posture=Identifier("READ_WRITE"),
        )

        with self.assertRaises(ContractValidationError):
            cr.build_registry((modified,))

    def test_t08_capability_resolution_is_declarative(self) -> None:
        registry = cr.build_foundation_registry()

        resolved = cr.capability_for_surface(
            registry,
            Identifier("executive_status"),
        )

        self.assertEqual(
            resolved.capability_id,
            cr.EXECUTIVE_STATUS_CAPABILITY_ID,
        )

        with self.assertRaises(ContractValidationError):
            cr.capability_for_surface(
                registry,
                Identifier("live_findings"),
            )

    def test_t09_registry_is_immutable(self) -> None:
        registry = cr.build_foundation_registry()

        with self.assertRaises(FrozenInstanceError):
            registry.registrations = ()

    def test_t10_no_external_side_effect_primitives(self) -> None:
        source = Path(cr.__file__).read_text(
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
