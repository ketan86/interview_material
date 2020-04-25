"""
Given an unsorted array containing numbers, find the smallest missing
positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
"""
# pylint: skip-file


def find_smallest_missing_positive_number(arr):
    i = 0
    n = len(arr)
    while i < n:
        index = arr[i] - 1
        # if number is 0 or less than 0, we skip the number,
        # if number is positive and not at the currect index and index is not
        # out of bound, we swap
        if arr[i] > 0 and index != i and index < n:
            arr[i], arr[index] = arr[index], arr[i]
        else:
            i += 1

    for i in range(n):
        if i != arr[i] - 1:
            return i + 1


print(find_smallest_missing_positive_number([-3, 1, 5, 4, 2]))
print(find_smallest_missing_positive_number([3, -2, 0, 1, 2]))
print(find_smallest_missing_positive_number([3, 2, 5, 1]))
