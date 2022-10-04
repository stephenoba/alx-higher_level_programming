#!/usr/bin/python3
# base.py
# Stephen Oba <obastepheno@gmail.com>
"""Module containing Base class
"""
import json


class Base:
    """Base class

    Attributes
    ----------
        None

    Methods
    -------
        None
    """
    __no_objects = 0

    def __init__(self, id=None):
        """Initializes an objject

        Args:
            id (int): id of object

        Raises:
            None

        Return:
            None
        """
        if not id:
            Base.__no_objects += 1
            self.id = Base.__no_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
