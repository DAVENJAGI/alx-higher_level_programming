#!/usr/bin/python3
"""defines a function
   Function takes two integers and adds them
"""


def add_integer(a, b=98):
    """
    adds two integers.
    Args: a, b
    raise TypeError: arguments must be integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

#    a = int(a)
#    b = int(b)

    return int(a) + int(b)
