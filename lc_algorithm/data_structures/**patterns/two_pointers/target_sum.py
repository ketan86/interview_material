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
    # iterate over the array
    for i, item in enumerate(arr):
        # find the diff that need to be found in the
        # binary search
        target = target_sum - item
        # binary search the number and return index
        # and the flag to indicate the search result
        found, j = _binary_search(arr, i + 1, target)
        # if found, return i and j
        if found:
            return [i, j]
    return [-1, -1]


def _binary_search(arr, start_index, target):
    # use two pointers
    start = start_index
    end = len(arr) - 1
    # while start is less than equal to end
    while start <= end:
        # find mid (make sure we don't overflow)
        mid = start + (end - start) // 2
        # if mid < target, move start
        if arr[mid] < target:
            start = mid + 1
        # if mid > target, move end
        elif arr[mid] > target:
            end = mid - 1
        # else found the number and the index, return
        else:
            return True, mid
    return False, -1


# hash table - space O(n) - time - O(n)
def pair_with_targetsum_ht(arr, target_sum):
    # use hashtable to find if target number is
    # present or not.
    d = {}
    # iterate over the arr and form the hash table
    # to store the item and it's index
    for index, item in enumerate(arr):
        d[item] = index
    # iterate over the arr and find the target number
    # in the map, if found, return the current and target
    # number indexes.
    for index, item in enumerate(arr):
        target = target_sum - item
        if target in d:
            return [index, d[target]]
    return [-1, -1]

# two pointers - O(n)


def pair_with_targetsum_tp(arr, target_sum):
    # use two pointers pointing to start and end
    start = 0
    end = len(arr) - 1
    # loop until start is less than end
    while start < end:
        # find sum
        sum_ = arr[start] + arr[end]
        # if sum is less than target, increment start
        if sum_ < target_sum:
            start += 1
        # if sum is greater than target, decrement end
        elif sum_ > target_sum:
            end -= 1
        # if sum is target, return the indexes
        else:
            return [start, end]
    return [-1, -1]


print(pair_with_targetsum_ht([1, 4, 0, 4, 6, 6, 0], 7))
