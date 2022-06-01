#!/usr/bin/python3
"""Function Declaration"""


def pascal_triangle(n):
    list1 = []
    list2 = []
    if n == 1:
        return [[1]]
    for r in range(1, n):
        if l in r:
            l = [1]
