#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples"""
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = [0, 0]
        else:
            tuple_a = list(tuple_a)
            tuple_a.append(0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = [0, 0]
        else:
            tuple_b = list(tuple_b)
            tuple_b.append(0)
    return tuple([sum(x) for x in zip(tuple_a, tuple_b)])
