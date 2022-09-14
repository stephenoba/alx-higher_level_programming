#!/usr/bin/python3
# 103-magic_class.py
# Stephen Oba <obastepheno@gmail.com>
"""
Magic Class
"""
import math


class MagicClass:
    """
    Magic class
    """
    def __init__(self, radius=0):
        """initialize object"""
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """compute the area"""
        return self.__radius ** 2 * math.pi

    def circumfrence(self):
        """compute the circumference"""
        return (2 * math.pi) * self.__radius
