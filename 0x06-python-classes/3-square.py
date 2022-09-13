#!/usr/bin/python3
# 3-square.py
# Stephen Oba <obastepheno@gmail.com>
"""
Module provides a class for cresting Square objects
"""


class Square:
    """
    Square class that defines a square with a size
    """
    def __init__(self, size=0):
        """Initialize object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2
