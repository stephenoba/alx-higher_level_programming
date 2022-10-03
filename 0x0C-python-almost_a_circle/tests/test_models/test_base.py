#!/usr/bin/python3
# test_base.py
# Stephen Oba <obastepheno@gmail.com>
"""Unit Test for Base module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Suite for BAse model
    """
    def test_base_id(self):
        """Test first object has id of 1"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_increment(self):
        """test id increaments"""
        b = Base()
        self.assertEqual(b.id, 2)

    def test_object_initialized_with_id(self):
        """Test id when passed to class"""
        b = Base(12)
        self.assertEqual(b.id, 12)


if __name__ == "__main__":
    unittest.main()
