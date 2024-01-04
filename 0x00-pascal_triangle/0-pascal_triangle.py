#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """returns the pascal triangle"""
    triangle = []

    if n < 1:
        return triangle

    triangle = [[1]]

    for i in range(1, n):
        temp = [1]
        for j in range(1, i):
            total = triangle[i-1][j-1] + triangle[i-1][j]
            temp.append(total)
        temp.append(1)
        triangle.append(temp)
    return triangle
