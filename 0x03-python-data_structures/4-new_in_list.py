#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """updates value in copy of a list"""
    new_list = my_list.copy()
    list_len = len(new_list)
    if idx > 0 and idx < list_len:
        for i in range(list_len):
            if i == idx:
                new_list[i] = element
                break
    return new_list
