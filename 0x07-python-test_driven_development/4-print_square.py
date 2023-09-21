#!/usr/bin/python3
"""program to print #.
"""


def print_square(size):
    """Function to print.
    Args:
        size: the length of the square.
    raises:
        TypeError: size must be an integer.
                   size must be an integer.
        ValueError: size must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and not isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
