#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Stephen Oba <obastepheno@gmail.com>
import sys


def safe_print_integer_err(value):
    flag = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        flag = False
        sys.stderr.write("Exception: {}\n".format(err))
    return flag
