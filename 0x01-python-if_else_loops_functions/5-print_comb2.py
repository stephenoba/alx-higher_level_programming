#!/usr/bin/python3

"""
prints numbers from 0 - 99 seperated by ', '
with padding
"""
for num in range(100):
    if num is 99:
        print(num)
    else:
        print("{}".format(str(num).zfill(2)), end=", ")
