#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0; i = 0; s = roman_string
    roman_num = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for c in roman_string:
        res += roman_num[c]
    i = s.count("IV") + s.count("IX") + s.count("IL") + s.count("IC")
    i += s.count("ID") + s.count("IM")
    res += i * (-2)
    return int(res)
