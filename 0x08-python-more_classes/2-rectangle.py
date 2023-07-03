#!/usr/bin/python3
"""Create a class Rectangle"""


class Rectangle:

    """initializing the Rectangle
        Arguments:
            width (int):width of rectangle
            height (int): Height of rectangle
        """
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """return the value of wight"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the rectangle given height or width is not 0"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
