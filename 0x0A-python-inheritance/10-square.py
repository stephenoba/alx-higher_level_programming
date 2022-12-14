#!/usr/bin/python3
# 10-square.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provides definition of a Square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class representation of a Square
    """
    def __init__(self, size):
        """Initialize a Square object

        Args:
            size (int): width and height of square

        Return:
            None
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
