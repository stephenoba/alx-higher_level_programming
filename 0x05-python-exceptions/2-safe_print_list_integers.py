#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Stephen Oba <obastepheno@gmail.com>

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
