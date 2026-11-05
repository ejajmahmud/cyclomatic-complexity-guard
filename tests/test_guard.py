"""Tests for cyclomatic-complexity-guard."""
import unittest
from cyclomatic_complexity_guard.guard import ComplexityGuard


class TestComplexityGuard(unittest.TestCase):
    def test_simple_vs_complex(self):
        guard = ComplexityGuard()
        code = "def simple(): return 1\n\ndef branches(a, b):\n    if a: return 1\n    if b: return 2\n    return 0\n"
        report = guard.analyze_source(code, max_allowed=2)
        self.assertEqual(report["functions_scanned"], 2)
        self.assertEqual(len(report["violations"]), 1)
        self.assertEqual(report["violations"][0]["name"], "branches")


if __name__ == "__main__":
    unittest.main()
