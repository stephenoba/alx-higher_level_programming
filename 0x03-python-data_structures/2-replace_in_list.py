#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """replace element at index"""
    list_len = len(my_list)
    if list_len > 0 or idx < list_len:
        for i in range(list_len):
            if i == idx:
                my_list[i] = element
                break
    return my_list
