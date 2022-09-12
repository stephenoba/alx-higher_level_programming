#!/usr/bin/python3
# 3-safe_print_division.py
# Stephen Oba <obastepheno@gmail.com>

def safe_print_division(a, b):
    """Divide two integers"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
