#!/usr/bin/python3
# 101-square.py
# Stephen Oba <obastepheno@gmail.com>
"""
Module provides a class for cresting Square objects
"""


class Square:
    """
    Square class that defines a square with a size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize object

        :param size: int, size of square;
          default: 0
        :param position: position;
          default: 0
        """
        self.size = size
        self.position = position

    def area(self):
        """
        computes the area of square

        :return: int, size ^ 2
        """
        return self.__size ** 2

    @property
    def size(self):
        """get square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if len(value) != 2 or not all(
                isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print a square
        """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for x in range(self.__size):
            [print(" ", end="") for i in range(self.__position[0])]
            [print("#", end="") for i in range(self.__size)]
            print("")

    def __str__(self):
        """print a string representation of Square"""
        _str = ""
        if self.__size == 0:
            return _str
        _str = _str.join("\n" for i in range(self.__position[1]))
        for x in range(self.__size):
            for i in range(self.__position[0]):
                _str += " "
            for i in range(self.__size):
                _str += "#"
            if x != self.__size - 1:
                _str += "\n"
        return _str
