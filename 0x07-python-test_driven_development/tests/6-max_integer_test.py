#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max int."""
    def test_positive(self):
        """Positive numbers test"""
        list = [1, 6, 8, 56, 100, 16]
        self.assertEqual(max_integer(list), 100)

    def test_negative(self):
        """Negative numbers test"""
        list = [-15, -56, -2, -157, -1, -9]
        self.assertEqual(max_integer(list), -1)

    def test_mixed(self):
        """Both positive/negative numbers test"""
        list = [-15, 56, -2, -157, -1, 9, 157]
        self.assertEqual(max_integer(list), 157)

    def test_empty(self):
        """Empty list test"""
        list = []
        self.assertIsNone(max_integer(list), None)

    def test_once(self):
        """One element in list test"""
        list = [2]
        self.assertEqual(max_integer(list), 2)

    def test_identical(self):
        """Identical numbers test"""
        list = [49, 49]
        self.assertEqual(max_integer(list), 49)

    def test_positive_float(self):
        """Positive floats test"""
        list = [10.4, 11.6, 4.8, 79.5]
        self.assertEqual(max_integer(list), 79.5)

    def test_negative_float(self):
        """Negative floats test"""
        list = [-10.4, -11.6, -4.8, -79.5]
        self.assertEqual(max_integer(list), -4.8)

    def test_intfloat(self):
        """Both ints/floats test"""
        list = [10, 11.6, 49, 7.9]
        self.assertEqual(max_integer(list), 49)

    def test_string(self):
        """One string test"""
        list = "Abderrahmane"
        self.assertEqual(max_integer(list), "r")

    def test_strings(self):
        """Multiple strings test"""
        list = ["Abderrahmane", "fethi", "z"]
        self.assertEqual(max_integer(list), "z")

    def test_max_at_beginning(self):
        """Max at beginning."""
        list = [100, 50, 16, 45]
        self.assertEqual(max_integer(list), 100)

if __name__ == "__main__":
    unittest.main()
