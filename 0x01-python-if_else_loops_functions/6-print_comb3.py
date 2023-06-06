#!/usr/bin/python3
for i in range(0, 90):
    if int(i / 10) < (i % 10) and i <= 79:
        print("{:02}".format(i), end=', ')
    if i == 89:
        print("{:02}".format(i))
