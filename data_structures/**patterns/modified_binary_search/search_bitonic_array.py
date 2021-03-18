"""
Given a Bitonic array, find if a given ‘key’ is present in it.
An array is considered bitonic if it is monotonically increasing
and then monotonically decreasing. Monotonically increasing or
decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3
Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1
Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3
Example 4:

Input: [10, 9, 8], key=10
Output: 0
"""
# pylint: skip-file


def search_bitonic_array(arr, key):
    # here we can have a key in either asscending and descending array.
    # we can find the peak and if peak and run two binary searches on
    # left and right of the peak.
    start_index = 0
    end_index = len(arr) - 1
    peak_index = _find_peak_index(arr)
    left = _binary_search(arr, start_index, peak_index, key, True)
    right = _binary_search(arr, peak_index + 1, end_index, key, False)
    if left != -1:
        return left
    if right != -1:
        return right


def _binary_search(arr, start_index, end_index, key, asscending=True):

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if key < arr[mid]:
            if asscending:
                end_index = mid - 1
            else:
                start_index = mid + 1
        elif key > arr[mid]:
            if asscending:
                start_index = mid + 1
            else:
                end_index = mid - 1
        else:
            return mid
    return -1


def _find_peak_index(arr):
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if arr[mid] < arr[mid - 1]:
            end_index = mid - 1
        else:
            start_index = mid + 1

    return end_index


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
