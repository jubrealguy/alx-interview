#!/usr/bin/python3
"""
A Pascal Triangle
"""


def pascal_triangle(n):
    """
    A function that returns  a list of lists of integers
    representing the Pascal’s triangle n
    """
    if n <= 0:
        return []
    """Initializing first row"""
    result = [[1]]
    """Looping through the other rows"""
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result
