#!/usr/bin/python3
# 4-print_square.py
# Stephen Oba <obastepheno@gmail.com>
"""module provides a function that prints squares"""


def print_square(size):
    """
    Add to numbers

    Args:
        size (int): size of sides

    Return:
        None

    Raises:
        TypeError
        ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i != (size - 1):
            print("")
