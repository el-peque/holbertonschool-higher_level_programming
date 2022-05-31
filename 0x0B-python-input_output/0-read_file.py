#!/usr/bin/python3
"""Function declaration"""


def read_file(filename=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
