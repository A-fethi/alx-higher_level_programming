#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            unicode_str = str[i]
            unicode_str = ord(unicode_str)
            unicode_str -= 32
        else:
            unicode_str = str[i]
            unicode_str = ord(unicode_str)
        print("{:c}".format(unicode_str), end='')
    print()
