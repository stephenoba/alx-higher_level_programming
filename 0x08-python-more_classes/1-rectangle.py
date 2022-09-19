#!/usr/bin/python3
# 0-rectangle.py
# Stephen Oba <obastepheno@gmail.com>
"""
Module defines a Rectangle Class
"""


class Rectangle:
    """
    Class used to represent a rectangle

    Attributes
    ----------
    width : int
        Integer >= 0 to represent width of rectangle
    height : int
        integer >= 0 to represent height of rectangle

    Methods
    -------
    None
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Returns:
            None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
