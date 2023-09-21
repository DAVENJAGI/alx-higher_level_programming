#!/usr/bin/python3
"""
    a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Function to print name
    Args: first_name, last_name
    raise TypeError: first_name and last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "":
        raise ValueError("first name required")
    print("My name is {} {}".format(first_name, last_name))
