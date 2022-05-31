#!/usr/bin/python3
"""Function declaration"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = []
try:
    arguments = load_from_json_file("add_item.json")
except:
    pass
for i in range(1, len(sys.argv)):
    arguments += [sys.argv[i]]
save_to_json_file(arguments, "add_item.json")
