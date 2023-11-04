#!/usr/bin/env python3
"""
Module: palindrome
Description: find a maximum palindrome derived
from the product of n-digit 2 numbers.
"""


def is_palindromic(number: int) -> bool:
    """Checks if number is a palindrome.
    Optimized verison 1.0
    """
    if number is None:
        raise ValueError("Null input!")
    if type(number) is not int:
        raise TypeError("number must be an int")
    number_or = str(number)
    check = False
    if number_or == number_or[::-1]:
        check = True
    return check


def palindrome_product(nOfDigits: int) -> int:
    """Returns maximum palindrome.
    Optimized version 1.0
    """
    if nOfDigits is None:
        return -1
    if type(nOfDigits) is not int:
        raise TypeError("nOfDigits must be an int")
    maxprod = 0
    num_one = 0
    num_two = 0
    start = 10**(nOfDigits - 1)
    ending = 10**nOfDigits
    outer_list = list(range(start, ending, 1))
    inner_list = list(range(start, ending, 1))
    for i in outer_list:
        for ii in inner_list:
            product = i * ii
            if is_palindromic(product) and product >= maxprod:
                maxprod = product
                num_one = i
                num_two = ii
        if len(inner_list) != 0:
            inner_list.pop(0)
    return maxprod, num_one, num_two


if __name__ == "__main__":
    p, f1, f2 = palindrome_product(3)
    print(p, f1, f2)
