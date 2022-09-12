#!/usr/bin/python3
# 1-safe_print_integer.py
# Stephen Oba <obastepheno@gmail.com>

def safe_print_integer(value):
    flag = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        flag = False
    return flag
