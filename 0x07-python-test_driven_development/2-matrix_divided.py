#!/usr/bin/python3
"""Function that divides a matrix
"""


def matrix_divided(matrix, div):
    """Takes two arguments and returns the result
    Args: matrix, div
    """
    result = []
    for i in matrix:
        result.append([round(x / div, 2) for x in i])
    return result
