#!/usr/bin/python3
# 8-rectangle.py
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
    bigger_or_equal
        static method that compares two rectangles
    square
        create a rectangle with equal sides
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares two rectangles

        Args:
            rect_1 (Rectanglie): first rectangle
            rect_2 (Rectangle): secont rectangle

        Return:
            the rectangle with a larger area. If equal returns rect_1

        Raises:
            TypeError if rect_1 or rect_2 are not Rectangle instances
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()
        if rect_1_area >= rect_2_area:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a square

        Args:
            size (int): size of a single side

        Return:
            Instance of a Rectangle
        """
        new_square = cls(width=size, height=size)
        return new_square

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
