"""
We are given an unsorted array containing ‘n+1’ numbers taken from the
range 1 to ‘n’. The array has only one duplicate but it can be repeated
multiple times. Find that duplicate number without using any extra space.
You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
"""

# pylint: skip-file


def duplicate_number(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] - 1 != i:
            index = arr[i] - 1
            if arr[i] == arr[index]:
                return arr[i]
            arr[i], arr[index] = arr[index], arr[i]
        else:
            i += 1


def all_duplicate_numbers(arr):
    n = len(arr)
    i = 0
    results = set()
    while i < n:
        if arr[i] - 1 != i:
            index = arr[i] - 1
            if arr[i] == arr[index]:
                results.add(arr[i])
                i += 1
            else:
                arr[i], arr[index] = arr[index], arr[i]
        else:
            i += 1
    return results


print(duplicate_number([1, 4, 4, 3, 2]))
print(duplicate_number([2, 1, 3, 3, 5, 4]))
print(duplicate_number([2, 4, 1, 4, 4]))


print(all_duplicate_numbers([1, 4, 4, 3, 3, 2]))
print(all_duplicate_numbers([5, 4, 7, 2, 3, 5, 3]))
print(all_duplicate_numbers([1, 2, 2, 4, 1, 4, 4]))
print(all_duplicate_numbers([3, 4, 4, 5, 5]))
