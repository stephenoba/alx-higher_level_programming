#!/usr/bin/python3
"""Module provides a function to find a pick in a list
"""


def find_peak(list_of_integers):
    """ Finds the peak number in a list of integers"""
    if list_of_integers and type(list_of_integers) is list:
        return max(list_of_integers)
    return None
