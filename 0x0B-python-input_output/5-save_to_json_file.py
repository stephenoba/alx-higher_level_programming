#!/usr/bin/python3
# 5-save_to_json_file.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines function to write object to JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation

    Args:
        my_obj (Any): Object
        filename (str): Filename

    Return:
        None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
