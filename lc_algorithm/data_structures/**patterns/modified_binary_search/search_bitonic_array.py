"""
Given a Bitonic array, find if a given ‘key’ is present in it.
An array is considered bitonic if it is monotonically increasing
and then monotonically decreasing. Monotonically increasing or
decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, 
return -1.

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


"""
Problem Statement #
Find the value in a given Bitonic array. An array is considered
bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the
array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2], 12
Output: 3
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:

Input: [3, 8, 3, 1]
Output: 1
Example 3:

Input: [1, 3, 8, 12]
Output: 3
Example 4:

Input: [10, 9, 8]
Output: 0
"""


def search_bitonic_array(arr, target, overlap=True):
    """
    NOTE: In botanic array (left increasing, right decreasing) arrays
    overlap, for ex. {-3, 9, 18, 20, 17, 5, 1}, after finding max, we have to
    search both in left and right to determine if target is present or not.

    if two arrays are not overlapping [NOT CONSIDERED BOTANIC]
    (such condition is present), we can rely on one side search.
    """
    # find the max element in the botanic array to divide two arrays
    # in one sorted in right and other in left direction.
    max_index = find_max_in_bitonic_array(arr)

    # if target is the max element, return the index
    if target == arr[max_index]:
        return max_index
    # if target is greater than max element, return -1
    if target > arr[max_index]:
        return -1

    if overlap:
        # ** OVERLAPPING CONDITION **
        left = _find(arr, 0, max_index - 1, target, reversed=False)
        if left != -1:
            return left

        right = _find(arr, max_index + 1, len(arr)-1, target, reversed=True)
        if right != -1:
            return right
    else:
        # ** NON OVERLAPPING CONDITION : NOT CONSIDERED BOTANIC**
        # if target less than the max element and greater than the 0th element,
        # search in left array
        if target < arr[max_index] and target >= arr[0]:
            return _find(arr, 0, max_index - 1, target, reversed=False)
        # else search in right array that is revered.
        else:
            return _find(arr, max_index + 1, len(arr)-1, target, reversed=True)


def find_max_in_bitonic_array(arr):
    # start_index = 0
    # end_index = len(arr) - 1

    # # until start index is less than the end index.
    # while start_index < end_index:
    #     mid = start_index + (end_index - start_index) // 2
    #     # if left element is less than equal to and right element
    #     # is less than the mid, we found the max.
    #     if arr[mid - 1] <= arr[mid] and arr[mid+1] < arr[mid]:
    #         return mid
    #     # if left >= mid, move to left
    #     if arr[mid-1] >= arr[mid]:
    #         end_index = mid - 1
    #     # if right >= mid, move to right
    #     if arr[mid+1] >= arr[mid]:
    #         start_index = mid + 1

    # # when both elements meet, that is the max
    # return end_index

    start_index = 0
    end_index = len(arr) - 1

    # until start index is less than the end index.
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        # check with previous element, if less move end index else start
        if arr[mid] < arr[mid - 1]:
            end_index = mid - 1
        else:
            start_index = mid + 1
    # return end index.
    return end_index


def _find(arr, start_index, end_index, target, reversed):
    # loop over the array
    while start_index <= end_index:
        # find mid element
        mid = start_index + (end_index - start_index) // 2
        # if target is grater than mid and reversed, move left or right
        if target > arr[mid]:
            if reversed:
                end_index = mid - 1
            else:
                start_index = mid + 1
        # if target is less than the mid and reversed, move right or left
        elif target < arr[mid]:
            if reversed:
                start_index = mid + 1
            else:
                end_index = mid - 1
        # if target is equal to mid, return mid
        else:
            return mid

    # if target is not present, return -1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([1, 3, 8, 3], 3))
    print(search_bitonic_array([10, 9, 8], 10))


main()
