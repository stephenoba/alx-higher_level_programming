#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """prints a matrix"""
    for row in matrix:
        row_len = len(row)
        for i in range(row_len):
            if i == row_len - 1:
                print("{:d}".format(row[i]))
                break
            print("{:d}".format(row[i]), end=" ")
