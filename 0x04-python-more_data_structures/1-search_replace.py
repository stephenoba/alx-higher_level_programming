#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """Replaces all occurence of an element"""
    new_list = []
    for i in my_list:
        if i is search:
            new_list.append(replace)
            continue
        new_list.append(i)
    return new_list
