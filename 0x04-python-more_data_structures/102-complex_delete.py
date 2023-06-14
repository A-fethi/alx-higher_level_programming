#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_remove = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_remove.append(key)
    for i in keys_to_remove:
        a_dictionary.pop(i)
    return a_dictionary
