#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """Inverts two operators"""
    def __eq__(self, value):
        return (self.real != value)

    def __ne__(self, value):
        return (self.real == value)
