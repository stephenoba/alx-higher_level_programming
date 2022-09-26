#!/usr/bin/python3
# 2-is_same_class.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provdes function to check belonging of an instance
"""


def is_same_class(obj, a_class):
    """Function checks if the object is exactly an instance of the
    specified class

    Args:
        obj (Any): Object
        a_class (object): Class

    Return:
        True if same class or False if not
    """
    return obj.__class__ == a_class
