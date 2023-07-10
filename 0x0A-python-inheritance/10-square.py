#!/usr/bin/python3
"""import module"""
Rectangle = __import__('9-rectangle').Rectangle


"""Create a class Square inheriting from Rectangle"""


class Square(Rectangle):
    """instantiation"""
    def __init__(self, size):
        """initializing"""
        self.integer_validator("self", size)
        """invoking"""
        super().__init__(size, size)
        self.__size = size
