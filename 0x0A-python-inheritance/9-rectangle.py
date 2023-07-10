#!/usr/bin/python3
"""import 8-rectangle.py"""
BaseGeometry = __import__('8-rectangle').Rectangle


"""write a class Rectangle"""


class Rectangle(BaseGeometry):
    """Return area"""
    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        """Return string representation"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
