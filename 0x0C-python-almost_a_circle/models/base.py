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
        """Json representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Return:
            Json representation
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Object from json representation

        Args:
            json_string (str): json string

        Return:
            Object
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string representation to a file

        Args:
            list_objs (list): list of objects

        Return:
            creates a json file
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            _list = []
        else:
            _list = list(map(lambda x: x.to_dictionary(), list_objs))
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(_list))
