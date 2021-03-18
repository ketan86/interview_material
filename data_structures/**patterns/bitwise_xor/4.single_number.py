"""
Problem Statement #
In a non-empty array of integers, every number appears twice except
for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9
"""

# pylint: skip-file

# 1. sort and go thorought the array and find one occurrence. (nlogn)
# 2. use set, put when found and remove when found again. when done, last
# element will be singe number.


def find_single_number(arr):
    result = 0
    # all duplicate numbers will be removed when XORed.
    for i in arr:
        result ^= i
    if result == 0:
        return -1
    return result


def main():
    arr = [1, 4, 4, 2, 1, 3, 2, 5, 5]
    print(find_single_number(arr))


main()
