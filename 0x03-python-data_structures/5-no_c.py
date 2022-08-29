#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """remove 'c' and 'C' from a string"""
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return new_string
