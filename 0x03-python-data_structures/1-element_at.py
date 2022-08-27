#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """
    get element at index
    """
    list_len = len(my_list)
    
    if idx > 0 or idx < list_len:
        for i in range(len(my_list)):
            if i == idx:
                return my_list[i]
    return None
