#!/usr/bin/python3
"""Function declaration"""


import json


def from_json_string(my_str):
    """returns an object (Python data strcture) represented by a JSON string"""
    return json.loads(my_str)
