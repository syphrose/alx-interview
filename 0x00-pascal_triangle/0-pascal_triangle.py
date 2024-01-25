#!/usr/bin/python3
"""Pascal's triangle representation using a function"""


def pascal_triangle(n):
    """
    Returns a list representing pascal's triangle of n.

    Args:
    n (integer): The num of rows in the triangle.

    Returns:
    An empty list if n <= 0
    """

    if n <= 0:
        return []

    else:
        triangle = [[1]]
        for i in range(1, n):
            triangle.append([1])
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle[i].append(1)
        return triangle
