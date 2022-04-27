#!/usr/bin/python3
for i in range(0, 10):
    for n in range(0, 10):
        if i >= n:
            continue
        if i < 8:
            print(f"{i}{n}", end=", ")
        else:
            print(f"{i}{n}")
