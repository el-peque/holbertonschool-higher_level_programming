#!/usr/bin/python3
"""Class declaration"""


def add_attribute(ob, key, value):
    """adds a new attribute to an object if it’s possible"""
    if "__dict__" not in dir(ob):
        raise TypeError("can't add new attribute")

    setattr(ob, key, value)
