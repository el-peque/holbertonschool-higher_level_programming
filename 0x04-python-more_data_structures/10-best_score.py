#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        if len(a_dictionary.values()) == 0:
            return None
        max = list(a_dictionary.values())[0]
        for k, v in a_dictionary.items():
            if v > max:
                max = v
                s = k
        return s
    return None
