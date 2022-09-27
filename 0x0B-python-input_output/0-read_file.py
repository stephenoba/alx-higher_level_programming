#!/usr/bin/python3
# 0-read_file.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines a function that reads a file
"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename (str): relative path to file

    Return:
        None
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line.strip())
