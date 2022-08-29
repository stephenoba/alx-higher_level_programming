#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """updates value in copy of a list"""
    list_len = len(my_list)
    if idx > 0 and idx < list_len:
        new_list = [x for x in my_list]
        new_list[idx] = element
        return new_list
    return my_list
