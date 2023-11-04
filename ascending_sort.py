#!/usr/bin/env python3
"""
Module: ascending_sort
Description: sorting a list in ascending order.
"""

my_list = [4, 12, 0, -3, -5, 1000, 28]


def sort_array(my_list: list) -> None:
    """Sorts an array of integers"""
    if my_list is None:
        return None
    if type(my_list) is not list:
        raise TypeError("Please use list type")
    if type(my_list[0]) not in [int, float]:
        raise TypeError("Items must be of type int or float")
    while True:
        for index in range(0, len(my_list) - 1, 1):
            if my_list[index] > my_list[index + 1]:
                """Switching values"""
                my_list.insert(index, my_list.pop(index + 1))
        check = True
        for index in range(0, len(my_list) - 1, 1):
            if my_list[index] <= min(my_list[index + 1:]):
                pass
            else:
                check = False
        if check:
            break
    return None


if __name__ == "__main__":
    print("Before sorting:\n", my_list)
    sort_array(my_list)
    print("After sorting:\n", my_list)
