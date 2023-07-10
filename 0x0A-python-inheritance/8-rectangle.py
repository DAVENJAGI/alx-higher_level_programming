#!/usr/bin/python3
"""Create an empty class"""


class BaseGeometry:
    """Raises empty area"""

    def area(self):
        """raises area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the parameter"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
