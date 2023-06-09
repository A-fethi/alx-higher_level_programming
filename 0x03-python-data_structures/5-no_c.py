#!/usr/bin/python3
def no_c(my_string):
    removed = ''
    for i in my_string:
        if i not in 'Cc':
            removed += i
    return (removed)
