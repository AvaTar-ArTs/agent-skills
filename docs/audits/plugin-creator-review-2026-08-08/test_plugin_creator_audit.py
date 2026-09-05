#!/usr/bin/env python3
"""Executable regression probes for the 2026-08-08 plugin-creator audit."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path("/Users/steven/.codex/skills/.system/plugin-creator")
CREATE = SKILL_ROOT / "scripts/create_basic_plugin.py"
VALIDATE = SKILL_ROOT / "scripts/validate_plugin.py"
CACHEBUSTER = SKILL_ROOT / "scripts/update_plugin_cachebuster.py"


def run(*args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", *(str(arg) for arg in args)],
        capture_output=True,
        text=True,
        check=False,
    )


class PluginCreatorAuditTests(unittest.TestCase):
    def test_basic_scaffold_validates_while_declared_skills_dir_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            created = run(CREATE, "basic-sample", "--path", root)
            self.assertEqual(created.returncode, 0, created.stderr)
            plugin = root / "basic-sample"
            self.assertFalse((plugin / "skills").exists())
            manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
            self.assertEqual(manifest["skills"], "./skills/")
            validated = run(VALIDATE, plugin)
            self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)

    def test_full_optional_scaffold_validates(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            plugin = root / "full-sample"
            created = run(
                CREATE,
                "full-sample",
                "--path",
                root,
                "--with-skills",
                "--with-hooks",
                "--with-scripts",
                "--with-assets",
                "--with-mcp",
                "--with-apps",
            )
            self.assertEqual(created.returncode, 0, created.stderr)
            validated = run(VALIDATE, plugin)
            self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)

    def test_folder_and_manifest_name_mismatch_passes_validation(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            created = run(CREATE, "manifest-name", "--path", root)
            self.assertEqual(created.returncode, 0, created.stderr)
            renamed = root / "different-folder-name"
            (root / "manifest-name").rename(renamed)
            validated = run(VALIDATE, renamed)
            self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)

    def test_marketplace_duplicate_failure_leaves_second_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            marketplace = root / "marketplace.json"
            first = run(
                CREATE,
                "duplicate-sample",
                "--path",
                root / "first/plugins",
                "--marketplace-path",
                marketplace,
                "--with-marketplace",
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            second = run(
                CREATE,
                "duplicate-sample",
                "--path",
                root / "second/plugins",
                "--marketplace-path",
                marketplace,
                "--with-marketplace",
            )
            self.assertNotEqual(second.returncode, 0)
            self.assertTrue(
                (root / "second/plugins/duplicate-sample/.codex-plugin/plugin.json").is_file()
            )

    def test_existing_marketplace_without_name_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            marketplace = root / "marketplace.json"
            marketplace.write_text('{"plugins": []}\n', encoding="utf-8")
            created = run(
                CREATE,
                "nameless-marketplace",
                "--path",
                root / "plugins",
                "--marketplace-path",
                marketplace,
                "--with-marketplace",
            )
            self.assertEqual(created.returncode, 0, created.stderr)
            self.assertNotIn("name", json.loads(marketplace.read_text()))

    def test_invalid_semver_base_is_accepted_by_cachebuster_then_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            plugin = root / "cachebuster-sample"
            created = run(CREATE, "cachebuster-sample", "--path", root)
            self.assertEqual(created.returncode, 0, created.stderr)
            manifest_path = plugin / ".codex-plugin/plugin.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["version"] = "dev-build+other-tag"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            updated = run(CACHEBUSTER, plugin, "--cachebuster", "audit")
            self.assertEqual(updated.returncode, 0, updated.stderr)
            validated = run(VALIDATE, plugin)
            self.assertNotEqual(validated.returncode, 0)
            self.assertIn("strict semver", validated.stdout)

    def test_name_normalization_and_limits(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            normalized = run(CREATE, "My__Plugin!!", "--path", root)
            self.assertEqual(normalized.returncode, 0, normalized.stderr)
            self.assertTrue((root / "my-plugin/.codex-plugin/plugin.json").is_file())
            empty = run(CREATE, "!!!", "--path", root)
            self.assertNotEqual(empty.returncode, 0)
            too_long = run(CREATE, "a" * 65, "--path", root)
            self.assertNotEqual(too_long.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
