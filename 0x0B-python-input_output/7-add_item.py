#!/usr/bin/python3
"""Function declaration"""


import json, sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = []
for i in range(1, len(sys.argv)):
    arguments.append(sys.argv[i])
save_to_json_file(arguments, "add_item.json")
