#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10
print("Last digit of", number, "is", last_digit, "and is", end=" ")
if last_digit == 0:
    print(0)
elif last_digit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
