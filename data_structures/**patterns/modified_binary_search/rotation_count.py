"""
Given an array of numbers which is sorted in ascending order and is
rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
Example 2:

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.

Example 3:

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
"""
# pylint: skip-file


def count_rotations(arr):
    # find peak element
    start_index = 0
    end_index = len(arr) - 1
    peak_index = _find_peak_index(arr, start_index, end_index)
    if peak_index == end_index:
        return 0
    return peak_index - start_index + 1


def _find_peak_index(arr, start_index, end_index):
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if arr[mid] < end_index:
            end_index = mid - 1
        else:
            start_index = mid + 1
    return end_index


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
    print(count_rotations([10, 1, 3, 8]))


main()
