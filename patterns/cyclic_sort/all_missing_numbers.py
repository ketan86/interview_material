"""
We are given an unsorted array containing numbers taken from the range
1 to ‘n’. The array can have duplicates, which means some numbers will
be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4
"""

# pylint: skip-file


def find_all_missing_numbers(arr):
    n = len(arr)
    # i = 0

    # cyclic sort
    # while i < n:
    #     j = arr[i] - 1
    #     if arr[j] != arr[i] and j != i:
    #         arr[j], arr[i] = arr[i], arr[j]
    #     else:
    #         i += 1

    for i in range(len(arr)):
        while arr[i] - 1 != i and arr[i] != arr[arr[i] - 1]:
            # one liner swap would not work
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
    # capture where indexes do not match the value - 1
    missing = []
    for i in range(n):
        if i != arr[i] - 1:
            missing.append(i + 1)

    return missing


print(find_all_missing_numbers([2, 4, 1, 2]))
print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
