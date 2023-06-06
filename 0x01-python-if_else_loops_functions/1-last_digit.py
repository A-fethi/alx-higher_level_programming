#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number > 0 and ld > 5:
    print("last digit of", number, "is", ld, "and is greater than 5")
elif ld == 0:
    print("last digit of", number, "is", ld, "and is 0")
elif ld < 6 and ld != 0 and number < 0:
    print(f"last digit of {number} is {ld * -1} and is less than 6 and not 0")
