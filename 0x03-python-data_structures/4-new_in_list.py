#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = 0
    new = my_list.copy()
    while i < len(my_list):
        if new[i] == idx + 1:
            new[i] = element
            return new
        i += 1
