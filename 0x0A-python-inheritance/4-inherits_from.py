#!/usr/bin/python3
# 4-inherits_from.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provides function to check only classes an object
inherits from
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (Any): An instance of a class
        a_class (object): Class

    Return:
        True or False
    """
    if isinstance(obj, a_class) and obj.__class__ is not a_class:
        return True
    return False
