#!/usr/bin/python3
# 3-to_json_string.py
# Stephen Oba <obastepheno@gmail.com>
"""Module defines function to convert object to JSON string
"""
import json


def to_json_string(my_obj):
    """Convert object to JSO string

    Args;
        my_obj (Any): Object

    Return:
        Json representation of my_obj
    """
    return json.dumps(my_obj)
