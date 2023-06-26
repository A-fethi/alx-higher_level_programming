#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        div = int(a) / int(b)
        result += div
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
