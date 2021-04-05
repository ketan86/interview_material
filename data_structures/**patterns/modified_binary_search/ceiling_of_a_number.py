"""
Problem Statement # 
Given an array of numbers sorted in an ascending order, find
the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the
smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t
any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6 Output: 1
Explanation: The smallest number greater
than or equal to '6' is '6' having index '1'. Example 2:

Input: [1, 3, 8, 10, 15], key = 12 Output: 4
Explanation: The smallest number
greater than or equal to '12' is '15' having index '4'. Example 3:

Input: [4, 6, 10], key = 17 Output: -1
Explanation: There is no number greater
than or equal to '17' in the given array. Example 4:

Input: [4, 6, 10], key = -1 Output: 0
Explanation: The smallest number greater
than or equal to '-1' is '4' having index '0'.


# find a target
    - if target is found, return target index
    - if present/absent, return the right element of the target
    - if not right element, return -1

until start_index <= end_index:
    mid = find_mid()
    if mid == target:
        return mid
    if target > mid:
        start_index = mid + 1
    if target < mid:
        end_index = mid - 1

if end_index < 0:
    return 0
if start_index > len(arr) - 1:
    return -1
return end_index

 [1, 3, 8, 10, 15]
                              
"""
# pylint: skip-file


def search_ceiling_of_a_number(arr, key):
    start = 0
    end = len(arr) - 1
    if key < arr[start]:
        return start
    if key > arr[end]:
        return - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()