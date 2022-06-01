#!/usr/bin/python3
"""Function Declaration"""


import fileinput
import shlex


i = 0
for line in fileinput.input():
    a = shlex.split(line)
    print(f"{a[5]}: {a[3]}")
    if i == 10:
        print(f"File size: {total_size}")
    i += 1
