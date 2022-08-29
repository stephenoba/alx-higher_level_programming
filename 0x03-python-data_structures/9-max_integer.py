#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """get the max integer in list"""
    if not my_list:
        return None
    my_list.sort()
    return my_list[-1]
