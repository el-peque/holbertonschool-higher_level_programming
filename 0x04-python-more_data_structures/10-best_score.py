#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = list(a_dictionary.values())[0]
        s = None
        for k, v in a_dictionary.items():
            if v > max:
                max = v
                s = k
        if s is not None:
            return s
    return None
