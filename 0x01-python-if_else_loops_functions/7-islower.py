#!/usr/bin/python3
def islower(c):
    unicode_char = ord(c)
    if unicode_char >= 97 and unicode_char <= 122:
        return True
    else:
        return False
