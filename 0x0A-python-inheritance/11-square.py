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

    def area(self):
        """Computes the Area of Square

        Return:
            None
        """
        return self.__size ** 2

    def __str__(self):
        """String representation of square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
