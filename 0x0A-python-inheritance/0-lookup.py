#!/usr/bin/pyhton3
# 0-lookup.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provides a function to list available attributes
and methods in a class
"""


def lookup(obj):
    """List available attributes and methods in an object

    Args:
        obj (object): object to lookup

    Return:
        List of attributes and methods
    """
    res = []
    if isinstance(obj, object):
        res = dir(obj)
    return res
