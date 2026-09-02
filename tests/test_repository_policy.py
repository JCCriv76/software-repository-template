from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "repository_policy", ROOT / "scripts/check_repository_policy.py"
)
POLICY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(POLICY)


class RepositoryPolicyTests(unittest.TestCase):
    def test_accepts_full_sha_action_reference(self) -> None:
        text = "uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd\n"
        self.assertEqual(POLICY.action_reference_failures(text, "ci.yml"), [])

    def test_rejects_floating_action_reference(self) -> None:
        text = "uses: actions/checkout@v6\n"
        failures = POLICY.action_reference_failures(text, "ci.yml")
        self.assertEqual(len(failures), 1)
        self.assertIn("not pinned to a full SHA", failures[0])

    def test_accepts_local_action_reference(self) -> None:
        text = "uses: ./.github/actions/build\n"
        self.assertEqual(POLICY.action_reference_failures(text, "ci.yml"), [])

    def test_environment_file_detection_allows_examples_only(self) -> None:
        self.assertTrue(POLICY.is_environment_file(".env"))
        self.assertTrue(POLICY.is_environment_file("app/.env.production"))
        self.assertFalse(POLICY.is_environment_file(".env.example"))
        self.assertFalse(POLICY.is_environment_file(".env.production.example"))

    def test_template_copy_must_be_bootstrapped(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "repository-profile.json").write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "template": {
                            "isTemplate": True,
                            "repositoryName": "software-repository-template",
                        },
                        "project": {"lifecycle": "template"},
                    }
                ),
                encoding="utf-8",
            )
            failures: list[str] = []
            warnings: list[str] = []
            profile = POLICY.load_profile(root, failures)
            POLICY.validate_profile(root, profile, "new-project", failures, warnings)
            self.assertTrue(any("was not bootstrapped" in item for item in failures))


if __name__ == "__main__":
    unittest.main()
