#!/usr/bin/python3
"""Create an empty class"""


class BaseGeometry:
    """Raises empty area"""
    def area(self):
        """raises area not implemented"""
        raise Exception("area() is not implemented")
