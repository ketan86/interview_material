"""
Problem Statement #
Find the maximum value in a given Bitonic array. An array is considered
bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the
array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:

Input: [3, 8, 3, 1]
Output: 8
Example 3:

Input: [1, 3, 8, 12]
Output: 12
Example 4:

Input: [10, 9, 8]
Output: 10
"""
# pylint: skip-file


def find_max_in_bitonic_array(arr):
    start_index = 0
    end_index = len(arr) - 1
    if end_index < 1:
        return arr[end_index]

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if mid == len(arr) - 1 or mid == 0:
            return arr[mid]
        if arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            start_index = mid + 1
        elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
            end_index = mid - 1
        else:
            return arr[mid]

# do not have to check both sides, just check if left value is less than
# mid value and if it is, go right else go left,
# when start > end, you will find peak at the end index.
# for ex,  1 10 9 8 7 6 5 4 3 2 1
#                     ^           -> 6 < 7, go left, end index = mid - 1
#               ^                 -> 9 < 10, go left, end index = mid - 1
#            ^                    -> 10 > 1, go right, start index = mid + 1
#                                    break since start index is greater than
#                                    end index.
# at time moment, we found the peak at end index (10)


def find_max_in_bitonic_array_alternative(arr):
    start_index = 0
    end_index = len(arr) - 1
    if end_index < 1:
        return arr[end_index]

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if arr[mid] > arr[mid - 1]:
            start_index = mid + 1
        else:
            end_index = mid - 1

    return arr[end_index]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))

    print(find_max_in_bitonic_array_alternative([1, 3, 8, 9, 12, 4, 2]))
    print(find_max_in_bitonic_array_alternative([3, 8, 3, 1]))
    print(find_max_in_bitonic_array_alternative([1, 3, 8, 12]))
    print(find_max_in_bitonic_array_alternative([10, 9, 8]))


main()
