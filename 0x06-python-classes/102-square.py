#!/usr/bin/python3
# 102-square.py
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
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __gt__(self, other):
        """compare area self > other"""
        return self.area() > other.area()

    def __lt__(self, other):
        """compare area less than other"""
        return self.area() < other.area()

    def __ge__(self, other):
        """compare area greater than or equal other"""
        return self.area() >= other.area()

    def __le__(self, other):
        """compare area less than or equal other"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """compare area equal other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """compare area not equal other"""
        return self.area() != other.area()
