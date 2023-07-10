#!/usr/bin/python3
"""Checks if object is instance of the specified class"""


def is_kind_of_class(obj, a_class):
    """Check if object is inherited"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
