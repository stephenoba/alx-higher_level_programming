#!/usr/bin/python3

"""
prints numbers from 0 - 99 seperated by ', '
with padding
"""
for num in range(100):
    if num is 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
