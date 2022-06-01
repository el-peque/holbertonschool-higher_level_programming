#!/usr/bin/python3
"""Function Declaration"""


import fileinput
import shlex


i = 0
b = []
total_size = 0
for line in fileinput.input():
    if i == 10:
        b.sort()
        for n in b:
            total_size += n
            print(f"b: {b}")
        print(f"File size: {total_size}")
        total_size = 0
        b = []
        i = 0
        continue
    a = shlex.split(line)
    b += [a[5]]
#    total_size += inta[6])
    i += 1
#    for i in b:
#        print(f"{i}: {a[6]}")
    
