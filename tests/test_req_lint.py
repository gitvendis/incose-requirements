"""Bounded wording regressions; these do not establish INCOSE conformance."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "req_lint.py"
SPEC = importlib.util.spec_from_file_location("req_lint", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


def rules(statement):
    return {finding.rule for finding in checker.check(statement)[1]}


class WordingRegressions(unittest.TestCase):
    def test_incomplete_obligation_is_not_clean(self):
        self.assertIn("R1", rules("The service shall."))
        self.assertNotIn("R1", rules("The service shall record the request."))

    def test_number_does_not_hide_performance_word_review(self):
        for statement in (
            "The service shall process inputs quickly for 3 operators.",
            "The service shall process inputs quickly under ICD 3.",
            "The service shall process inputs quickly within 2 seconds.",
        ):
            with self.subTest(statement=statement):
                self.assertIn("R34", rules(statement))

    def test_explicit_measurable_wording(self):
        self.assertNotIn("R34", rules(
            "The service shall process each input within 2 seconds for 3 operators."
        ))

    def test_defined_performance_term(self):
        with patch.object(checker, "EXTRA_TERMS", ["high fidelity"]):
            self.assertNotIn("R34", rules("The service shall produce high fidelity output."))

    def test_strict_json_reports_both_false_negatives(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--strict", "--json"],
            input="DIR-X-001: The service shall.\n"
                  "DIR-X-002: The service shall process inputs quickly for 3 operators.\n",
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 1)
        entries = json.loads(result.stdout)
        self.assertEqual([entry["id"] for entry in entries], ["DIR-X-001", "DIR-X-002"])
        self.assertIn("R1", {f["rule"] for f in entries[0]["findings"]})
        self.assertIn("R34", {f["rule"] for f in entries[1]["findings"]})

    def test_terms_cli_preserves_custom_mask(self):
        with tempfile.TemporaryDirectory() as directory:
            terms = Path(directory) / "terms.txt"
            terms.write_text("high fidelity\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--strict", "--json", "--terms", str(terms)],
                input="The service shall produce high fidelity output.\n",
                text=True, capture_output=True, check=False,
            )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)[0]["findings"], [])


if __name__ == "__main__":
    unittest.main()
