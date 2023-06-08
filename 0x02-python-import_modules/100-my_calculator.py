#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(argv)
    for i in range(args):
        if args != 4:
            print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        if argv[2] not in '*+-/':
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    if argv[2] == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    if argv[2] == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    if argv[2] == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
