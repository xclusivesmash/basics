#!/usr/bin/env python3
"""
Module: diviibility
Description: find the smallest number that can be divided
by numbers from  1 - 20 without any remainder.
"""


num = 1
start = int(input("Enter starting point: "))
ending = int(input("Enter ending point: "))
while True:
    check = True
    for index in range(start, ending + 1, 1):
        if (num % index) == 0:
            continue
        else:
            check = False
            break
    if check:
        print("The number is: ", num)
        break
    num = num + 1
