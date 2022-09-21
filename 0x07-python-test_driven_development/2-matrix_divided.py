#!/usr/bin/python3
# 2-matrix_divided.py
# Stephen Oba <obastepheno@gmail.com>
"""module provides a function to divide elements in a matrix"""


def isvalid_matrix_type(matrix):
    """
    Check if Matrix is valid

    Args:
        matix (list): matrix

    Return:
        True or False
    """
    if isinstance(matrix, list):
        if all(isinstance(x, list) for x in matrix):
            for row in matrix:
                if not all(type(col) in [int, float] for col in row):
                    return False
            return True
    return False


def isvalid_matrix_size(matrix):
    """
    check if all rows are of equal size

    Args:
        matrix (list): Matrix

    Return:
        True or False
    """
    if not matrix or not all(x == len(
            matrix[0]) for x in list(map(lambda x: len(x), matrix))):
        return False
    return True


def matrix_divided(matrix, div):
    """
    Divide elements in a matrix

    Args:
        matrix (list): Matrix
        div ([int, float]): Divisor

    Return:
        matrix eith quotient of element and divisor

    Raises:
        TypeError
        ZeroDivisionError
    """
    if not isvalid_matrix_type(matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not isvalid_matrix_size(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
