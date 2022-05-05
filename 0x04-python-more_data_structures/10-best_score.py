#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.items()) == 0:
        return None
    else:
        max = 0
        for k, v in a_dictionary.items():
            if v > max:
                max = v
                s = k
        return s
    return None
