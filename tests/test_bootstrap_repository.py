from __future__ import annotations

import argparse
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "bootstrap_repository", ROOT / "scripts/bootstrap_repository.py"
)
BOOTSTRAP = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BOOTSTRAP)


class BootstrapRepositoryTests(unittest.TestCase):
    def args(self, profile: str = "node-web") -> argparse.Namespace:
        return argparse.Namespace(
            name="example-app",
            description="Example application.",
            org="example-org",
            team="engineering",
            backup_team="operations",
            security_email="security@example.com",
            support_url="https://example.com/support",
            profile=profile,
            license="proprietary",
            license_holder="Example Organization",
            visibility="private",
            risk_tier="moderate",
            data_classification="confidential",
            allow_dirty=True,
        )

    def base_profile(self) -> dict:
        return json.loads((ROOT / "repository-profile.json").read_text(encoding="utf-8"))

    def test_build_profile_resolves_ownership_and_state(self) -> None:
        result = BOOTSTRAP.build_profile(self.base_profile(), self.args())
        self.assertFalse(result["template"]["isTemplate"])
        self.assertEqual(result["project"]["lifecycle"], "bootstrapping")
        self.assertEqual(result["ownership"]["primaryTeam"], "example-org/engineering")
        self.assertEqual(result["stack"]["profile"], "node-web")

    def test_profiles_do_not_force_node(self) -> None:
        result = BOOTSTRAP.build_profile(self.base_profile(), self.args("python-service"))
        self.assertEqual(result["stack"]["languages"], ["Python"])
        self.assertNotIn("npm", result["stack"]["packageManagers"])

    def test_render_rejects_unresolved_values(self) -> None:
        with self.assertRaises(ValueError):
            BOOTSTRAP.render("{{MISSING}}", {})

    def test_identifier_validation(self) -> None:
        BOOTSTRAP.validate_identifier("valid-name_1", "name")
        with self.assertRaises(ValueError):
            BOOTSTRAP.validate_identifier("invalid/name", "name")


if __name__ == "__main__":
    unittest.main()
