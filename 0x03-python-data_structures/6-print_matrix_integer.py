#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in range(len(row)):
            if val != len(row) - 1:
                print(f"{row[val]:d}", end=" ")
            else:
                print(f"{row[val]:d}")
