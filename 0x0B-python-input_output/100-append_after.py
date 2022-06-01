#!/usr/bin/python3
"""Function Declaration"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing
    a specific string"""
    text = ""
    with open(filename, "r+", encoding="utf-8") as f:
        data = f.read()
        f.write(data.replace(search_string, search_string + new_string))
