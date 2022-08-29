#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """prints a matrix"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
                break
            print("{:d}".format(matrix[i][j]), end=" ")
