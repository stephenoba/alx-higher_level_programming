#!/usr/bin/python3
# 2-append_write.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines a function to append text to a file
"""


def write_file(filename="", text=""):
    """Append to a file

    Args:
        filename (str): Path to file
        text (str): text to write to file

    Return:
        None
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
