#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if val in row:
                for val in row:
                    print(f"{val:d}", end="")
                    if (val + 1 in row):
                        print(" ", end="")
        print()
