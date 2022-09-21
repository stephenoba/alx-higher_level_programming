#!/usr/bin/python3
# 3-say_my_name.py
# Stephen Oba <obastepheno@gmail.com>
"""module provides a function to return a person's full name"""


def say_my_name(first_name, last_name=""):
    """
    Print full name

    Args:
        first_name (str): first name
        last_name (str): last name. Default ""

    Return:
        None

    Raises:
        TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    msg = "My name is {} {}"
    print(msg.format(first_name, last_name))
