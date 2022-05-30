#!/usr/bin/python3
def inherits_from(obj, a_class):
    if issubclass(a_class, type(obj)) is True:
        return False
    else:
        return True
