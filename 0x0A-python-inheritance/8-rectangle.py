#!/usr/bin/python3
# 8-rectangle.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provides definition of a Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class representation of a Rectangle
    """
    def __init__(self, width, height):
        """Initialize a Rectanglle object

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Return:
            None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
