#!/usr/bin/python3
# 3-is_kind_of_class.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provides a function to check if an object is an
instance of a class by inheritance
"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj (Any): Instance of a class
        a-class (object): Class

    Return:
        True or False
    """
    return isinstance(obj, a_class)
