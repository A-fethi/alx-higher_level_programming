#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        error_message = "Exception: Unknown format code 'd' for object of "
        error_message2 = "type 'str'" + "\n"
        sys.stderr.write(error_message + error_message2)
        return False
