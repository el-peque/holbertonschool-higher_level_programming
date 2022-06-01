#!/usr/bin/python3
"""Function Declaration"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing
    a specific string"""
    text = ""
    with open(filename, "r+", encoding="utf-8") as f:
        for line in f:
            if line.find("python"):
                text += line + new_string
                continue
            text += line
        data = f.read()
        f.write(text)
