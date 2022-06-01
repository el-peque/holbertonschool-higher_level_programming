#!/usr/bin/python3
"""Function declaration"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialzation of an object"""
    return obj.__doc__
