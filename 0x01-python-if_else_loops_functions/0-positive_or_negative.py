#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print(number, 'is zero')
elif number > 0:
    print(number, 'positif')
else:
    print(number, 'is negatif')
