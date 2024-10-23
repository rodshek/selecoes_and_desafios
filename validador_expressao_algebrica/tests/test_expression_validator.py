import unittest

from src.expression_validator import ExpressionValidator


class TestExpressionValidator(unittest.TestCase):

    def setUp(self):
        self.validator = ExpressionValidator()

    def test_valid_expression(self):
        self.assertTrue(self.validator.validate("(a + b) * {c + [d - e]}"))

    def test_invalid_expression_unmatched_parentheses(self):
        self.assertFalse(self.validator.validate("(a + b * {c + [d - e]}"))

    def test_invalid_expression_wrong_order(self):
        self.assertFalse(self.validator.validate("(a + b) * {c + [d - e]}]"))

    def test_empty_expression(self):
        self.assertTrue(self.validator.validate(""))


if __name__ == '__main__':
    unittest.main()
