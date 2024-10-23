import unittest

from src.password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()

    def test_generate_password_length(self):
        password = self.generator.generate_password(8)
        self.assertEqual(len(password), 8)

    def test_generate_password_with_uppercase(self):
        password = self.generator.generate_password(10, include_uppercase=True)
        self.assertTrue(any(c.isupper() for c in password))

    def test_generate_password_with_numbers(self):
        password = self.generator.generate_password(12, include_numbers=True)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_generate_password_with_special(self):
        password = self.generator.generate_password(15, include_special=True)
        special_characters = "!@#$%^&*()"
        self.assertTrue(any(c in special_characters for c in password))

    def test_generate_password_invalid_length(self):
        with self.assertRaises(ValueError):
            self.generator.generate_password(0)


if __name__ == "__main__":
    unittest.main()
