"""
We are given an array containing ‘n’ ** distinct ** numbers taken from the
range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total
‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""
# pylint: skip-file


def find_missing_number(arr):
    n = len(arr)
    i = 0
    # largest number will be at the wrong place.
    while i < n:
        j = arr[i]
        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    for i in range(n):
        if i != arr[i]:
            print(arr[i])
            return
    return n


print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number([8, 3, 5, 1, 2, 4, 6, 0, 1]))
