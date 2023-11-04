#!/usr/bin/env python3
"""
Module: factorial
Description: finding the factorial of a given number.
"""


def factorial(num: int) -> int:
    """Computing the factorial of a number
    Recursion version 1.0
    """
    if (num == 0 or num == 1):
        return 1
    return num * factorial(num - 1)


if __name__ == "__main__":
    number = int(input("Please enter positive number: "))
    print("{}! = {}".format(number, factorial(number)))
