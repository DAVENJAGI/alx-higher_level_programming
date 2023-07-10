#!/usr/bin/python3
"""A function  that checks whether it is an inherited class"""


def inherits_from(obj, a_class):
    """Checks whether an object is an inherited instance"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
