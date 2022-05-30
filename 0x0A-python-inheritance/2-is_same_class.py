#!/usr/bin/python3
"""function declaration"""


def is_same_class(obj, a_class):
    """checks if its the same class"""
    if type(obj) == a_class:
        return True
    else:
        return False
