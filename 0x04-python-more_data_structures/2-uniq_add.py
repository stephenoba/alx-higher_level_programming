#!/usr/bin/python3
# 3-uniq_add.py

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    total = sum(set(my_list))
    return total
