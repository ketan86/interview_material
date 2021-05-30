"""
Given an array of numbers sorted in ascending order, find the element
in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""
# pylint: skip-file


def search_min_diff_element(arr, key):
    start_index = 0
    end_index = len(arr) - 1
    if end_index < 1:
        return - 1

    if key < arr[start_index]:
        return arr[start_index]

    if key > arr[end_index]:
        return arr[end_index]

    # binary search
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if key < arr[mid]:
            end_index = mid - 1
        elif key > arr[mid]:
            start_index = mid + 1
        else:
            return arr[mid]

    # NOTE: WE most prob don't need this condition. Any usecase ?
    # at the end of the while loop, 'start == end+1'
    # once element is not found, end index (lower value) is always less than
    # start_index (start_index <= end_index),
    # so 7 10 and key == 8
    # 8 - 7 less than 10 - 8,  7 is the answer arr(end_index)
    # else, 10 is the answer arr(start_index)

    # if key - arr[end_index] < arr[start_index] - key:
    #    return arr[end_index]

    return arr[start_index]


def main():
    print(search_min_diff_element([3, 6, 10], 4))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 4))
    print(search_min_diff_element([4, 6, 10], 17))
    print(search_min_diff_element([7, 10], 8))


main()
