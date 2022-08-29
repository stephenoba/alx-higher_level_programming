#!/usr/bin/python3
# 7-add_tuple.py


def pad_tuple(tuple_x):
    """adds zeros to tuple with length less than 2"""
    tup_to_list = list(tuple_x)
    i = 2  # max length
    while i != len(tuple_x):
        i -= 1
        tup_to_list.append(0)
    return tup_to_list


def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples"""
    tuple_a = pad_tuple(tuple_a)
    tuple_b = pad_tuple(tuple_b)
    total = [sum(x) for x in zip(tuple_a, tuple_b)]
    return tuple(total)
