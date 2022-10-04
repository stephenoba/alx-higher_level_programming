#!/usr/bin/python3
# base.py
# Stephen Oba <obastepheno@gmail.com>
"""Module containing Base class
"""
import json
import csv
import turtle


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

    @classmethod
    def create(cls, **dictionary):
        """Create an object from dictionary

        Args:
            dictionary (dict): key word arguments to create object

        Return:
            instance
        """
        if not dictionary:
            return None
        if cls.__name__ == "Rectangle":
            _obj = cls(1, 1)
        else:
            _obj = cls(1)
        _obj.update(**dictionary)
        return _obj

    @classmethod
    def load_from_file(cls):
        """Create objects from file
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                _list = cls.from_json_string(f.read())
                return list(map(lambda x: cls.create(**x), _list))
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#000000")
        tur.pensize(3)
        tur.shape("turtle")

        tur.color("#ffffff")
        for rect in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rect.x, rect.y)
            tur.down()
            for i in range(2):
                tur.forward(rect.width)
                tur.left(90)
                tur.forward(rect.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#b4d3d1")
        for sq in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sq.x, sq.y)
            tur.down()
            for i in range(2):
                tur.forward(sq.width)
                tur.left(90)
                tur.forward(sq.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
