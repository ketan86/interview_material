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
    # using equation
    n = len(arr)
    total_sum = 0
    for i in arr:
        total_sum += i

    # sum of 1..n -> (n * n+1)//2
    # sum of 0..n -> (n * n-1)//2
    return ((n * (n + 1)) // 2) - total_sum


def find_missing_number_2(arr):
    # using set
    num_set = set(arr)

    for num in range(0, len(arr) + 1):
        if num not in num_set:
            return num


def find_missing_number_3(arr):
    # using bit-manipulation
    num = 0
    for i in range(0, len(arr) + 1):
        num ^= i

    for i in arr:
        num ^= i

    return num


def find_missing_number_4(arr):
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
            return i
    return n


print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number([8, 3, 5, 1, 2, 4, 6, 0, 1]))

print(find_missing_number_2([4, 0, 3, 1]))
print(find_missing_number_2([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number_2([8, 3, 5, 1, 2, 4, 6, 0]))

print(find_missing_number_3([4, 0, 3, 1]))
print(find_missing_number_3([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number_3([8, 3, 5, 1, 2, 4, 6, 0]))

print(find_missing_number_4([4, 0, 3, 1]))
print(find_missing_number_4([8, 3, 5, 2, 4, 6, 0, 1]))
print(find_missing_number_4([8, 3, 5, 1, 2, 4, 6, 0]))
