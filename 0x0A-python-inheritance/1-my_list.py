#!/usr/bin/python3
"""Class called MyList"""


class MyList(list):

    """Defines public attribute sorted"""
    def print_sorted(self):
        """prints sorted"""
        print(sorted(self))
