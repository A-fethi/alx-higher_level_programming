#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10 if number > 0 else number % -10
if number > 0 and ld > 5:
    print("Last digit of", number, "is", ld, "and is greater than 5")
if ld == 0:
    print("Last digit of", number, "is", ld, "and is 0")
elif ld < 6 and ld != 0 and number < 0:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
