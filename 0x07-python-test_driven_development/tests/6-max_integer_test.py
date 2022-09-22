#!/usr/bin/python3
# 6-max_integer_test.py
# Stephen Oba <obastepheno@gmail.com>
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest class with test cases for max_integer function

    Method
    ------
        test
    """
    def test_max_number_at_start(self):
        """Test max integer with max number at start
        """
        li = [23, 9, 1, 34, 13]
        self.assertEqual(max_integer(li), 34)

    def test_max_number_at_end(self):
        """Test max integer with max number at end
        """
        li = [23, 9, 1, 34, 113]
        self.assertEqual(max_integer(li), 113)

    def test_max_integer_at_middle(self):
        """Test max integer with max at middle
        """
        li = [33, 44, 99, 77, 66]
        self.assertEqual(max_integer(li), 99)

    def test_max_integer_empty_list(self):
        """Test max integer with an empty list
        """
        li = []
        self.assertEqual(max_integer(li), None)

    def test_max_integer_positive_negetive_integers(self):
        """Test max integer with a list of positive and negative
        integers
        """
        li = [43, 74, 8, -4, 99, -102, 73, 2]
        self.assertEqual(max_integer(li), 99)

    def test_max_integer_negetive_integers(self):
        """Test max integer with list of negetive integers
        """
        li = [-2, -63, -4663, -8, -87]
        self.assertEqual(max_integer(li), -2)

    def test_max_integer_list_with_non_integers(self):
        """Test max integer with a list of integers and non-integers
        """
        li = [23, 84, "12", 42]
        with self.assertRaises(TypeError):
            max_integer(li)
