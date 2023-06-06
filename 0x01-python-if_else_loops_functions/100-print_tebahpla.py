#!/usr/bin/python3
for i, j in zip(reversed(range(97, 123, 2)), reversed(range(98, 123, 2))):
    print("{:c}{:c}".format(j, i - 32), end="")
