#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        new_list = []
        for n in my_list:
            if n % 2 == 0:
                new_list += [True]
            else:
                new_list += [False]
        return new_list
