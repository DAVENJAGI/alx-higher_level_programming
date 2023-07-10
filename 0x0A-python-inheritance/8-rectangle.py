#!/usr/bin/python3
"""Import module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Create  a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Instantatin"""
    def __init__(self, width, height):
        """integer width validation"""
        self.integer_validator("width", width)
        self.__width = width
        """Integer height validation"""
        self.integer_validator("height", height)
        self.__height = height
