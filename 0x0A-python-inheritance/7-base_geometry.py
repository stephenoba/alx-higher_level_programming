#!/usr/bin/python3
# 5-base_geometry.py
# Stephen Oba <obastepheno@gmail.com>
"""Module contains defintion of class BaseGeometry
"""


class BaseGeometry:
    """Base class for geometry operations

    Methods
    --------
        area
        integer_validator
    """
    def area(self):
        """Cumpute area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an attributes value

        Args:
            name (str): Attribute name
            value (int): Attribute value

        Raises:
            TypeError: If value is not an integer
            ValueError: if value is less than or equal 0

        Return:
            None
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
