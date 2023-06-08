#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv)
    if args == 1:
        print("{}".format(args - 1), "arguments.")
    elif args == 2:
        print("{}".format(args - 1), "argument:")
        for i in range(1, args):
            print("{}".format(i) + ":", argv[i])
    elif args > 2:
        print("{}".format(args - 1), "arguments:")
        for i in range(1, args):
            print("{}".format(i) + ":", argv[i])
