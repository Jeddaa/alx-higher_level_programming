#!/usr/bin/python3
"""divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """function to divide all elements of a matrix"""
    new_matrix, new_row = [], []
    prev_len = 0
    msg = ('matrix must be a matrix (list of lists) of integers/floats',\
            'each row of the matrix must have the same size',\
            'div must be a number', 'division by zero')
    if type(matrix) is not list:
        raise TypeError(msg[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg[0])
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(msg[0])
        current_len = len(row)
        if current_len != prev_len and prev_len != 0:
            raise TypeError(msg[1])
        prev_len = current_len
    if type(div) not in [int, float]:
        raise TypeError(msg[2])
    if div == 0:
        raise ZeroDivisionError(msg[3])
    for row in matrix:
        new_row = list(map(lambda x: round(x / div, 2), row))
        new_matrix.append(new_row)
    return new_matrix
