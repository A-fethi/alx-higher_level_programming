#!/usr/bin/python3
from sys import argv

tot = 0
if __name__ == "__main__":
    args = len(argv)
    for i in range(1, args):
        tot = tot + int(argv[i])
    if args > 1:
        print(tot)
    else:
        print(0)
