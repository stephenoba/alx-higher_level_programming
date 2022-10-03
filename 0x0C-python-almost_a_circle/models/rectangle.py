#!/usr/bin/python3
# rectangle.py
# Stephen Oba <obastepheno@gmail.com>
"""Models defines a rectangle class
"""
from models.base import Base

__all__ = ['Rectangle']


class Rectangle(Base):
    """Class to create rectangle objects

    Methods
    -------
        area(self)
        display(self)
        update(self, *args)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle object

        Args:
            width (int): Width
            height (int): Height
            x (int): X postion
            y (int): Y postion
            id (int): Unique ID

        Return;
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for heiight"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x position"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x position"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y position"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y position"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """display a rectangle with '#' character
        """
        if self.__height == 0 and self.__height == 0:
            print("")
            return
        [print("") for i in range(self.__y)]
        for x in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            [print("#", end="") for i in range(self.__width)]
            print("")

    def __str__(self):
        """string representation of rectangle
        """
        _str = "[{}] ({}) {}/{} - {}/{}"
        return _str.format(
                self.__class__.__name__,
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
        )

    def update(self, *args, **kwargs):
        """Update the values of rectangle

        Args:
            *args (list):
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs (dict): key/value pair
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        else:
            for k, v in kwargs.items():
                if k not in attrs:
                    continue
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
