#!/usr/bin/python3
# 4-from_json_string.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines function to convert to object from JSON string
"""
import json


def from_json_string(my_str):
    """Convert to object from JSon string

    Args;
        my_str (str): String

    Return:
        object
    """
    return json.loads(my_str)
