#!/usr/bin/python3
# 1-write_file.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines a function to write to a file
"""


def write_file(filename="", text=""):
    """Write to a file

    Args:
        filename (str): Path to file
        text (str): text to write to file

    Return:
        None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
