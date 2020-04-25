"""
Given an array of sorted numbers and a target sum, find a pair in the array
whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair)
such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

# pylint: skip-file

# brute-force - O(n^2)


def pair_with_targetsum_bf(arr, target_sum):
    for i, item in enumerate(arr):
        diff = target_sum - item
        for j in range(i + 1, len(arr)):
            if arr[j] == diff:
                return [i, j]
    return [-1, -1]


# brute-force with binary search to find diff - O(n log n)
def pair_with_targetsum_bs(arr, target_sum):
    for i, item in enumerate(arr):
        diff = target_sum - item
        found, j = _binary_search(arr, i + 1, diff)
        if found:
            return [i, j]
    return [-1, -1]


def _binary_search(arr, start_index, diff):
    left = start_index
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < diff:
            left = mid + 1
        elif arr[mid] > diff:
            right = mid - 1
        else:
            return True, mid
    return False, 0


# hash table - space O(n) - time - O(n)
def pair_with_targetsum_ht(arr, target_sum):
    d = {}
    for index, item in enumerate(arr):
        d[item] = index
    for index, item in enumerate(arr):
        diff = target_sum - item
        if diff in d:
            return [index, d[diff]]
    return [-1, -1]

# two pointers - O(n)


def pair_with_targetsum_tp(arr, target_sum):
    start = 0
    end = len(arr) - 1
    while start < end:
        s = arr[start] + arr[end]
        if s < target_sum:
            start += 1
        elif s > target_sum:
            end -= 1
        else:
            return [start, end]
    return [-1, -1]


print(pair_with_targetsum_ht([1, 4, 0, 4, 6, 6, 0], 7))
