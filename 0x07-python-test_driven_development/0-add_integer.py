#!/usr/bin/python3
# 0-add_integer.py
# Stephen Oba <obastepheno@gmail.com>
"""module provides a function for addition"""

def add_integer(a, b=98):
    """
    Add to numbers

    Args:
        a ([int, float]): first number
        b ([int, float]): second number. Default 98

    Return:
        sum of both numbers

    Raises:
        TypeError
    """
    if type(a) not in [int,  float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return round(a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
