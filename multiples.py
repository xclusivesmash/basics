#!/usr/bin/env python3
"""
Module: multiples
Description: find all multiples of 3 or 5
below a certain input number.
"""


number = int(input("Please enter positive number: "))
summation = 0
for index in range(1, number, 1):
    if (index % 3) == 0 or (index % 5) == 0:
        summation += index


if __name__ == "__main__":
    print("Total: ", summation)
