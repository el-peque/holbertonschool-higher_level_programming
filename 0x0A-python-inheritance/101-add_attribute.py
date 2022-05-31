#!/usr/bin/python3
"""Class declaration"""


def add_attribute(ob, key, value):
    """adds a new attribute to an object if it’s possible"""
    if key in dir(ob):
        setattr(ob, key, value)
    else:
        raise TypeError("can't add new attribute")
