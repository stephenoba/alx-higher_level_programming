#!/usr/bin/python3
# rectangle.py
# Stephen Oba <obastepheno@gmail.com>
"""Models defines a rectangle class
"""
from models.rectangle import Rectangle

__all__ = ['Square']


class Square(Rectangle):
    """Class to create square objects

    Methods
    -------
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a rectangle object

        Args:
            size (int): hieght and width of square
            x (int): X postion
            y (int): Y postion
            id (int): Unique ID

        Return;
            None
        """
        super().__init__(size, size, x=x, y=y, id=id)

    @property
    def size(self):
        """size property"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """string representation of rectangle
        """
        _str = "[{}] ({}) {}/{} - {}"
        return _str.format(
                self.__class__.__name__,
                self.id,
                self.x,
                self.y,
                self.size,
        )

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
