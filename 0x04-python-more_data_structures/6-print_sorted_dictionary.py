#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
