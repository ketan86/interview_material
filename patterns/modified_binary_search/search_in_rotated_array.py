"""
Search in Rotated Array (medium) #
Given an array of numbers which is sorted in ascending order and also
rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array.
If the ‘key’ is not present, return -1. You can assume that the given array
does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
"""
# pylint: skip-file


def search_rotated_array(arr, key):
    start_index = 0
    end_index = len(arr) - 1
    peak_index = _find_peak_index(arr, start_index, end_index)
    # now if key is greater than end index, search in left side of the peak
    # else right.
    if key > arr[end_index]:
        return _binary_search(arr, start_index, peak_index, key)
    return _binary_search(arr, peak_index + 1, end_index, key)


def _binary_search(arr, start_index, end_index, key):
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if key < arr[mid]:
            end_index = mid - 1
        elif key > arr[mid]:
            start_index = mid + 1
        else:
            return mid
    return - 1


def _find_peak_index(arr, start_index, end_index):
    # since there is a tick (6 7 10 1 2 3 5) ( 7 -> hight -> low)
    # we can not compare with immediate member, instead when we
    # find mid element, if that element is less than end element, we go
    # right else we go left. at some point, end will settle on highest peak.
    # we return end index.
    # for ex,
    #   9 10 11 12 15 1 2 3 4 5 6 7 8
    #           ^                     -> 12 > 8, right
    #                 ^               -> 1 < 8, left
    #     ^                           -> 10 > 8, right
    #                              ^  -> 7 < 8, right
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if arr[mid] < end_index:
            end_index = mid - 1
        else:
            start_index = mid + 1
    return end_index


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_array([4, 5, 7, 9, -1, 2], 5))
    print(search_rotated_array([9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 9, 9, 9], 5))
    print(search_rotated_array([3, 7, 3, 3, 3], 7))


main()
