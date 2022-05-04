#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        n_matrix += [[x ** 2 for x in row]]
    return n_matrix
