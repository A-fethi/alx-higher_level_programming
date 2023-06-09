#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = 0
    while i < len(my_list):
        if my_list[i] == idx + 1:
            my_list[i] = element
            return my_list
        i += 1
