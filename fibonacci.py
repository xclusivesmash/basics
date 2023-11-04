#!/usr/bin/env python3
"""
Module: fibonacci
Description: manipulation of the Fibonacci sequence
starting with 1 and 2.
"""


a = 1
b = 2
summation = 0
while True:
    n_term = a + b
    if (n_term <= 4000000):
        if (n_term % 2) == 0:
            summation += n_term
        else:
            pass
    else:
        break
    a = b
    b = n_term


if __name__ == "__main__":
    print("Total: ", summation)
