#!/usr/bin/python3
def add_integer(a, b=98):
    """adds two integers or floats, casting floats into integers"""
    if type(a) == float:
        a = int(a)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
