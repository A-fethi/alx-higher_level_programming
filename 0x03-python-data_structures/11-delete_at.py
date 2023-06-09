#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = 0
    while i < len(my_list):
        if i == idx + 1:
            i = my_list.remove(i)
            return my_list
        i += 1
