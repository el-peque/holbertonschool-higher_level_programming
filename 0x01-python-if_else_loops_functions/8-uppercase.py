#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str[i]) < 123 and ord(str[i]) > 96:
            print(chr(ord(str[i])-32))
