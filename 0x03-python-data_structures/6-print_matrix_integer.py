#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            print(val, end="")
            if (val + 1 in row):
                print(" ", end="")
        print("$")
