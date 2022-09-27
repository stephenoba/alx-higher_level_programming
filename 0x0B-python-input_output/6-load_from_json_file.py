#!/usr/bin/python3
# 6-load_from_json_file.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines function to loads object to JSON file
"""
import json


def load_from_json_file(filename):
    """Loads an object to a text file using JSON representation

    Args:
        filename (str): File to load from

    Return:
        Object
    """
    with open(filename, "w") as f:
        return json.load(f)
