#!/usr/bin/env python3
"""
Module: prime_factorization
Description: finding prime factors of a given number.
"""


number = int(input("Please enter a positive number: "))
maxprod = 0
index = 2
while number > 1:
    if (number % index) == 0:
        number = number / index
        if index > maxprod:
            maxprod = index
        else:
            pass
    else:
        pass
    index = index + 1


if __name__ == "__main__":
    print("Max. prod: ", maxprod)
