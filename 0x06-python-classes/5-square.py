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
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print a square
        """
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")
