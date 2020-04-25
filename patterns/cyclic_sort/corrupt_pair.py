"""
We are given an unsorted array containing ‘n’ numbers taken from the
range 1 to ‘n’. The array originally contained all the numbers from
1 to ‘n’, but due to a data error, one of the numbers got duplicated
which also resulted in one number going missing. Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""


def find_corrupt_pair(arr):
    i = 0
    n = len(arr)
    while i < n:
        index = arr[i] - 1
        if i != index and arr[i] != arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
        else:
            i += 1

    for i in range(n):
        if i != arr[i] - 1:
            return [arr[i], i + 1]


print(find_corrupt_pair([3, 1, 2, 5, 2]))
print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))
