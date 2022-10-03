#!/usr/bin/python3
# test_base.py
# Stephen Oba <obastepheno@gmail.com>
"""Unit Test for Base module
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Suite for Rectangle model
    """
    def test_rectangle_id(self):
        """Test object has id of 1"""
        r = Rectangle(5, 8)
        self.assertEqual(r.id, 1)

    def test_set_rectangle_width_height(self):
        """Test setting rectangle width and height"""
        r = Rectangle(8, 12)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.width, 8)

    def test_set_position_x_y(self):
        """Test setting x and y position"""
        r = Rectangle(12, 8, x=5, y=3)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 3)

    def test_missing_positional_argument(self):
        """Test missing argument"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_rectangle_with_specified_id(self):
        """Test creating a rectangle with a specified id"""
        r = Rectangle(2, 6, id=12)
        self.assertEqual(r.id, 12)
