#!/usr/bin/python3
"""test for console"""
import unittest
import console


class TestConsole(unittest.TestCase):
    """TESTING CONSOLE"""

    def test_doc(self):
        """test docstrings"""
        self.assertIsNotNone(console.__doc__)


if __name__ == "__main__":
    unittest.main()
