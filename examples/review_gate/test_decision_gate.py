"""Tests of the standalone example only; not tests of T-Bot."""
import unittest
from decision_gate import review_gate


class ReviewGateTests(unittest.TestCase):
    def test_deny(self):
        self.assertEqual(review_gate("DENY", True), {"decision": "REJECT", "dummy_action_count": 0})

    def test_unknown(self):
        self.assertEqual(review_gate("UNKNOWN", True), {"decision": "REJECT", "dummy_action_count": 0})

    def test_no_approval(self):
        self.assertEqual(review_gate("ALLOW", False), {"decision": "REJECT", "dummy_action_count": 0})

    def test_allowed(self):
        self.assertEqual(review_gate("ALLOW", True), {"decision": "ALLOW", "dummy_action_count": 1})

    def test_repeated_input(self):
        self.assertEqual(review_gate("DENY", True), review_gate("DENY", True))

    def test_invalid_verdict(self):
        self.assertEqual(review_gate("INVALID", True), {"decision": "REJECT", "dummy_action_count": 0})

    def test_non_boolean_approval(self):
        self.assertEqual(review_gate("ALLOW", 1), {"decision": "REJECT", "dummy_action_count": 0})


if __name__ == "__main__":
    unittest.main()
