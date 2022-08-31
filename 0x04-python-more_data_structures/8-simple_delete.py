#!/usr/bin/python3
# 8-simple_delete.py

def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary"""
    if key and (key in a_dictionary.keys()):
        del a_dictionary[key]
    return a_dictionary
