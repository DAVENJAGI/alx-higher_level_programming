#!/usr/bin/python3
"""Function that returns a list of lists of integes"""


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        last = triangle[-1]
        temp = [1]
        for x in range(len(last) - 1):
            temp.append(last[x] + last[x + 1])
        temp.append(1)
        triangle.append(temp)
    return (triangle)
