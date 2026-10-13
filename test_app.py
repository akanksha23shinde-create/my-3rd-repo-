"""Unit tests for app.py."""
import unittest
from app import greet


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(
            greet(),
            "Hello, DevOps! Python CI/CD pipeline is working."
        )

    def test_custom_name(self):
        self.assertEqual(
            greet("Aakanksha"),
            "Hello, Aakanksha! Python CI/CD pipeline is working."
        )

    def test_blank_name_uses_default(self):
        self.assertEqual(
            greet("   "),
            "Hello, DevOps! Python CI/CD pipeline is working."
        )


if __name__ == "__main__":
    unittest.main()
