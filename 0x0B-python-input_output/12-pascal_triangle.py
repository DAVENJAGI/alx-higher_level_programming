#!/usr/bin/python3
"""Function that returns a list of lists of integes"""


def pascal_triangle(n):
    """if n is less than 0 return empty list"""
    if n <= 0:
        return []
    """initializes a single list triangle with 1 as the element in list"""
    triangle = [[1]]
    """a while loop provided length of triangle is not equals to n"""
    while len(triangle) != n:
        last = triangle[-1]
        temp = [1]
        """it iterates over adding the las element to list"""
        for x in range(len(last) - 1):
            temp.append(last[x] + last[x + 1])
            """it appends the last item to the list"""
        temp.append(1)
        triangle.append(temp)
        """returns the triangle"""
    return (triangle)
