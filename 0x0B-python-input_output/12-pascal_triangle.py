#!/usr/bin/python3
"""a function that returns a list of lists
of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """a pascal triangle function"""
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for rows in range(n - 1):
            line = [1]
            for i in range(rows):
                line.append(triangle[rows][i] + triangle[rows][i + 1])
            line.append(1)
            triangle.append(line)

        return triangle
