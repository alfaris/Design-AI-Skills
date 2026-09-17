"""Focused regression tests for validate-skills.py."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate-skills.py")
SPEC = importlib.util.spec_from_file_location("validate_skills", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidateSkillsTests(unittest.TestCase):
    def test_repository_passes(self) -> None:
        self.assertEqual(VALIDATOR.validate(SCRIPT.parent.parent), 0)

    def test_installer_contains_installation_contract(self) -> None:
        installer = SCRIPT.parent.parent / "INSTALL.md"
        text = installer.read_text(encoding="utf-8")
        for requirement in VALIDATOR.INSTALLER_REQUIREMENTS:
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text)

    def test_missing_description_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "example"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: example\n---\n", encoding="utf-8")
            (skill / "agents" / "openai.yaml").write_text(
                "interface:\n  display_name: Example\n  short_description: Example\n  default_prompt: Example\n",
                encoding="utf-8",
            )
            self.assertEqual(VALIDATOR.validate(root), 1)


if __name__ == "__main__":
    unittest.main()