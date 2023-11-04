#!/usr/bin/env python3
"""
Module: digits_1000
Description: finding the greatest product of n-digit adjacent
numbers in the 1000 number scheme.
"""


# READ THE DATA SEPARATETLY
f = open("1000_digits.txt", "r", encoding="utf-8", errors="ignore")
data = f.read()
data = data[:-1]
f.close()


def str_multiplication(digits: str) -> int:
    """Multiplies the chars in digits"""
    if type(digits) is not str:
        raise TypeError("digits must be a string")
    store = 1
    for index in range(0, len(digits), 1):
        store = store * int(digits[index])
    return store


def nMultiDigits(string: str, digit: int) -> [int, str]:
    """Main comuptation for max product"""
    if type(string) is not str:
        raise TypeError("string must be of type str")
    if type(digit) is not int:
        raise TypeError("digit must be an integer")
    maxprod = 0
    str_return = 0
    for i in range(0, len(string) - digit + 1, 1):
        str_num = string[i:i + digit]
        num = str_multiplication(str_num)
        if num > maxprod:
            maxprod = num
            str_return = str_num
    return maxprod, str_return


if __name__ == "__main__":
    n = int(input("Number of digits required: "))
    prod, s = nMultiDigits(data, n)
    print(prod, s)
