#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

a = abs(number % 10)
print(a)

if a > 5:
    print(f"Last digit of {number} is {a} and it is greater than 5")
elif a == 0:
    print(f"Last digit of {number} is {a} and it is 0")
elif a < 6 and a != 0:
    print(f"Last digit of {number} is {a} and it is less than 6 and not 0")
