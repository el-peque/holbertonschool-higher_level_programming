#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) < 123 and ord(c) > 96:
            print(f"{chr(ord(c)-32)}", end="")
        else:
            print(c, end="")
    print("")
