#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    """calculate the weighted average of all integers"""
    if not my_list:
        return 0
    if all([len(x) == 2 for x in my_list]):
        total = 0
        n = 0
        for i, j in dict(my_list).items():
            total += i * j
            n += j
        return total / n
    return 0
