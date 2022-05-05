#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    vaux = []
    for k, v in a_dictionary.items():
        if v == value:
            vaux += [k]
    for i in vaux:
        del a_dictionary[i]
    return a_dictionary
