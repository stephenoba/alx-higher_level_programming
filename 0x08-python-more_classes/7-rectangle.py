#!/usr/bin/python3
# 7-rectangle.py
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
    area
        compute the area of rectangle
    perimeter
        compute the perimeter of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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

    def area(self):
        """
        computes the area of rectangle

        Args:
            None

        Returns:
            int: product of width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        computes the perimeter of rectangle

        Args:
            None

        Return:
            int: total sum of all sides or zero if width or heght equal 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """str representation of rectangle"""
        _str = ""
        if self.__width == 0 or self.__height == 0:
            return _str
        for i in range(self.__height):
            for j in range(self.__width):
                _str += str(self.print_symbol)
            if i != self.__height - 1:
                _str += "\n"
        return _str

    def __repr__(self):
        """representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """action before del is called on a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
