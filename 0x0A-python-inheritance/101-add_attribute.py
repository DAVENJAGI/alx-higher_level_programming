#!/usr/bin/python3
"""Function to add attributes to objects"""


def add_attribute(obj, att, value):
    """use hasattr() function to check for attrite"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
