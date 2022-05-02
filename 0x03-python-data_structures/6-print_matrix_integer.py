#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in range(0, len(row)):
            if val == len(row) - 1:
                print(f"{row[val]}")
            else:
                print(f"{row[val]}", end=" ")
