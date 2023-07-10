#!/usr/bin/python3
"""A function that checks if an object is an instance of class"""


def is_same_class(obj, a_class):
    """check to see if inherited instance of a class"""
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
