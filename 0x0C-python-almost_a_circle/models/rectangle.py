#!/usr/bin/python3
# rectangle.py
# Stephen Oba <obastepheno@gmail.com>
"""Models defines a rectangle class
"""
from models.base import Base

__all__ = ['Rectangle']


class Rectangle(Base):
    """Class to create rectangle objects

    Attributes
    ----------

    Methods
    -------
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
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for heiight"""
        self.__height = value

    @property
    def x(self):
        """getter for x position"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x position"""
        self.__x = value

    @property
    def y(self):
        """getter for y position"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y position"""
        self.__y = value
