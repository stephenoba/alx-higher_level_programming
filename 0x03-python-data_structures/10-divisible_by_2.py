#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """
    highlights numbers in a list that are
    divisible by 2
    """
    new_list = [x % 2 == 0 for x in my_list]
    return new_list
