#!/usr/bin/python3
# 4-square.py
# Stephen Oba <obastepheno@gmail.com>
"""
Module provides a class for cresting Square objects
"""


class Square:
    """
    Square class that defines a square with a size
    """
    def __init__(self, size=0):
        """
        Initialize object

        :param size: int, size of square;
          default: 0
        """
        self.size = size

    def area(self):
        """
        computes the area of square

        :return: int, size ^ 2
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get square size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
