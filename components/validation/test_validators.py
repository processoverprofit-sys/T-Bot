"""Portable fictional-input tests for the validation toolkit."""

import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "validators",
    Path(__file__).with_name("validators.py")
)

validators = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validators)

CASES = [

    # Digest formatting
    ("digest_zero", "digest", ("0" * 64,), True),
    ("digest_hex", "digest", ("0123456789abcdef" * 4,), True),
    ("digest_short", "digest", ("a" * 63,), False),
    ("digest_long", "digest", ("a" * 65,), False),
    ("digest_uppercase", "digest", ("A" * 64,), False),
    ("digest_nonhex", "digest", ("g" * 64,), False),
    ("digest_empty", "digest", ("",), False),
    ("digest_newline", "digest", ("a" * 64 + "\n",), False),
    ("digest_bytes", "digest", (b"a" * 64,), False),
    ("digest_none", "digest", (None,), False),
    ("digest_integer", "digest", (123,), False),

    # Alias formatting and literal-prefix correction
    ("alias_valid", "alias", ("PREFIX_ABC", "PREFIX_"), True),
    ("alias_minimum", "alias", ("P_A", "P_"), True),
    ("alias_maximum", "alias", ("P_" + "A" * 40, "P_"), True),
    ("alias_overlong", "alias", ("P_" + "A" * 41, "P_"), False),
    ("alias_no_suffix", "alias", ("P_", "P_"), False),
    ("alias_lowercase", "alias", ("P_abc", "P_"), False),
    ("alias_invalid_char", "alias", ("P_A!", "P_"), False),
    ("alias_literal_dot", "alias", ("A.B_X", "A.B_"), True),
    ("alias_regex_wildcard", "alias", ("ACB_X", "A.B_"), False),
    ("alias_literal_brackets", "alias", ("[X]A", "[X]"), True),
    ("alias_literal_backslash", "alias", ("P\\A", "P\\"), True),
    ("alias_integer_prefix", "alias", ("ABC", 123), False),
    ("alias_none_prefix", "alias", ("ABC", None), False),
    ("alias_bytes_prefix", "alias", ("ABC", b"P_"), False),
    ("alias_bytes_value", "alias", (b"P_A", "P_"), False),
    ("alias_empty_prefix", "alias", ("ABC", ""), True),
    ("alias_newline", "alias", ("P_A\n", "P_"), False),

    # Structured reason-code formatting
    ("reason_minimum", "reason_code", ("A",), True),
    ("reason_maximum", "reason_code", ("A" * 100,), True),
    ("reason_overlong", "reason_code", ("A" * 101,), False),
    ("reason_empty", "reason_code", ("",), False),
    ("reason_valid", "reason_code", ("CHECK_123",), True),
    ("reason_lowercase", "reason_code", ("check",), False),
    ("reason_hyphen", "reason_code", ("CHECK-1",), False),
    ("reason_space", "reason_code", ("CHECK 1",), False),
    ("reason_newline", "reason_code", ("CHECK\n",), False),
    ("reason_bytes", "reason_code", (b"CHECK",), False),
    ("reason_none", "reason_code", (None,), False),

    # Ordered integers and decision-type correction
    ("available_zero", "_available", (0, 0, 0), True),
    ("available_equal", "_available", (5, 5, 5), True),
    ("available_ordered", "_available", (1, 2, 3), True),
    ("available_negative_observed", "_available", (-1, 2, 3), False),
    ("available_negative_available", "_available", (0, -1, 3), False),
    ("available_negative_decision", "_available", (0, 1, -1), False),
    ("available_observed_too_high", "_available", (3, 2, 4), False),
    ("available_available_too_high", "_available", (1, 4, 3), False),
    ("available_float_decision", "_available", (0, 1, 2.0), False),
    ("available_bool_decision", "_available", (0, 1, True), False),
    ("available_string_decision", "_available", (0, 1, "2"), False),
    ("available_none_decision", "_available", (0, 1, None), False),
    ("available_bool_observed", "_available", (True, 2, 3), False),
    ("available_bool_available", "_available", (0, True, 3), False),
    ("available_float_observed", "_available", (0.0, 1, 2), False),
    ("available_float_available", "_available", (0, 1.0, 2), False),
    ("available_string_observed", "_available", ("0", 1, 2), False),
    ("available_string_available", "_available", (0, "1", 2), False),
]

class ValidatorTests(unittest.TestCase):
    pass

def build_test(function, arguments, expected):
    def test(self):
        self.assertIs(
            getattr(validators, function)(*arguments),
            expected
        )
    return test

for name, function, arguments, expected in CASES:
    setattr(
        ValidatorTests,
        "test_" + name,
        build_test(function, arguments, expected)
    )

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        ValidatorTests
    )

    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print("TESTS_RUN=" + str(result.testsRun))
    print("TEST_FAILURES=" + str(len(result.failures)))
    print("TEST_ERRORS=" + str(len(result.errors)))
    print("TEST_SKIPPED=" + str(len(result.skipped)))

    success = (
        result.wasSuccessful()
        and result.testsRun == len(CASES)
        and not result.skipped
    )

    raise SystemExit(0 if success else 1)
