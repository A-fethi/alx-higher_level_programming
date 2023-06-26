#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for counter in range(x):
        try:
            print(my_list[counter], end="")
        except IndexError:
            print()
            return x - 2
    print()
    return x
