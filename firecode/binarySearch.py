"""
Oracle

Binary Search
Time-Complexity - O(log n)
Space-Complexity - O(1)

Write a function that searches a list of ints for a given integer using the Binary Search Algorithm. If the input integer is found in the list, return True. Otherwise, return False.
You can assume that the given list of integers is already sorted in ascending order.

Examples:
binary_search([2, 5, 7, 8, 9],9) -> True

binary_search([2, 8, 9, 12],6) -> False

binary_search([2],4) -> False

binary_search([],9) -> False

[] -> [Empty] Array
"""

def binary_search(a_list, item):
    if len(a_list) == 0:
        return False

    left = 0
    right = len(a_list) - 1

    while (left <= right):
        mid = (left + right) / 2
        if a_list[mid] > item:
            right = mid - 1
        elif a_list[mid] < item:
            left = mid + 1
        else:
            return True
    return False
