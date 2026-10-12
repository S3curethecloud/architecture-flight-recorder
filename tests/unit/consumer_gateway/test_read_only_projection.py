from __future__ import annotations

import json
import unittest
from pathlib import Path

from afr.consumer_gateway.read_only_projection import (
    READ_ONLY_PROJECTION_ALLOWED,
    READ_ONLY_PROJECTION_DENIED,
    READ_ONLY_PROJECTION_FAIL_CLOSED,
    project_read_only,
)

VECTOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "vectors"
    / "consumer_gateway"
    / "read_only_projection-v1.json"
)


class ReadOnlyProjectionTests(unittest.TestCase):
    def test_vectors(self) -> None:
        payload = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))
        for case in payload["cases"]:
            with self.subTest(case=case["name"]):
                self.assertEqual(
                    project_read_only(case["request"]),
                    case["expected"],
                )

    def test_result_vocabulary_is_exact(self) -> None:
        self.assertEqual(
            {
                READ_ONLY_PROJECTION_ALLOWED,
                READ_ONLY_PROJECTION_DENIED,
                READ_ONLY_PROJECTION_FAIL_CLOSED,
            },
            {
                "READ_ONLY_PROJECTION_ALLOWED",
                "READ_ONLY_PROJECTION_DENIED",
                "READ_ONLY_PROJECTION_FAIL_CLOSED",
            },
        )

    def test_projection_is_detached_from_input(self) -> None:
        request = {
            "subject_tenant_id": "tenant-a",
            "resource_tenant_id": "tenant-a",
            "authorization_tenant_id": "tenant-a",
            "authorized": True,
            "resource": {"nested": {"values": [1, 2]}},
        }
        result = project_read_only(request)
        result["projection"]["nested"]["values"].append(3)
        self.assertEqual(
            request["resource"],
            {"nested": {"values": [1, 2]}},
        )

    def test_non_json_resource_fails_closed(self) -> None:
        request = {
            "subject_tenant_id": "tenant-a",
            "resource_tenant_id": "tenant-a",
            "authorization_tenant_id": "tenant-a",
            "authorized": True,
            "resource": {"unsupported": {1, 2}},
        }
        self.assertEqual(
            project_read_only(request),
            {
                "result": READ_ONLY_PROJECTION_FAIL_CLOSED,
                "tenant_id": None,
                "projection": None,
                "reason": "INVALID_RESOURCE",
            },
        )


if __name__ == "__main__":
    unittest.main()
