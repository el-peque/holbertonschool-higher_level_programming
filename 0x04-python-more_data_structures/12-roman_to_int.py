#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    res = 0
    i = -1
    s = roman_string
    roman_num = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for c in roman_string:
        if roman_num[(roman_string[i])] < roman_num[c] and i >= 0:
            res -= roman_num[(roman_string[i])] * 2
        res += roman_num[c]
        i += 1
    return int(res)
