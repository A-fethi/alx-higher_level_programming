#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv)
    if args == 0:
        print("{}".format(args - 1), "arguments.")
    elif args == 1:
        print("{}".format(args - 1), "argument:")
    elif args > 1:
        print("{}".format(args - 1), "arguments:")
        for i in range(1, args):
            print("{}".format(i) + ":", argv[i])
