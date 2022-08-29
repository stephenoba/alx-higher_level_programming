#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """print a list reversed"""
    if isinstance(my_list, list):
        list_len = len(my_list)
        while list_len != 0:
            list_len -= 1
            print("{:d}".format(my_list[list_len]))
