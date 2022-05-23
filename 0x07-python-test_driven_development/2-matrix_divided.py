#!/usr/bin/python3
def matrix_divided(matrix, div):
    """adds two integers or floats, casting floats into integers"""
    if type(matrix) != list or all(isinstance(x, (int, float)) for x in matrix) == True:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    items = len(matrix[0])
    for row in matrix:
        if len(row) != items:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row: list(map(lambda i: round(i / div, 2), row)), matrix))
