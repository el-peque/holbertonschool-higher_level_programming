#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        res = fct(*args)
        return res

    except (TypeError, ValueError, ZeroDivisionError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
