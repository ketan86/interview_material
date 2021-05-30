"""
Problem Statement #
Given an infinite sorted array (or an array with unknown size),
find if a given number ‘key’ is present in the array. Write a
function to return the index of the ‘key’ if it is present in
the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown)
size, you will be provided with an interface ArrayReader to read
elements of the array. ArrayReader.get(index) will return the number
at index; if the array’s size is smaller than the index, it will return
Integer.MAX_VALUE.

Example 1:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.
Example 2:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
Example 3:

Input: [1, 3, 8, 10, 15], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.
Example 4:

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.
"""
# pylint: skip-file

import math


class ArrayReader:

    def __init__(self, arr):
        self._arr = arr

    def get(self, index):
        if index >= len(self._arr):
            return math.inf
        return self._arr[index]

# Not too optimal since we are spending time searching the exact end boundary.
# and also starting to search the key from the start when end boundary is
# found.


def search_in_infinite_array(reader, key):
    # find end of the array. This will follow the same approach of binary
    # search but instead of diving by 2, we multiply by 2.
    start_index = 0
    end_index = 2
    while start_index < end_index:
        value = reader.get(end_index)
        if value == math.inf:
            end_index = start_index + (end_index - start_index) // 2
        else:
            start_index = end_index
            end_index *= 2

    start_index = 0
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if key < reader.get(mid):
            end_index = mid - 1
        elif key > reader.get(mid):
            start_index = mid + 1
        else:
            return mid
    return -1


# NOTE: We can optimize the algorithm only finding the boundary where
# end index is not greater than key ( it can with infinite value)
# for ex,
# 1 2 3 4 5 6 7 -> target 7
# -- (start 1, end 2)
#   ------ (start 3, end 6)
#             -------- (start 7, end 14)
# since we found end (value infinite in this case) greater than key,
# we can use start 7 and end 14 to binary search.

# NOTE: also instead doing the search from 0 to end, we can only search in
# last start and end while searching the boundary.

def search_in_infinite_array_optimized(reader, key):
    # find end of the array. This will follow the same approach of binary
    # search but instead of diving by 2, we multiply by 2.
    start_index = 0
    end_index = 2
    while reader.get(end_index) < key:
        new_start = end_index + 1
        end_index += (end_index - start_index + 1) * 2
        # increase to double the bounds size
        start_index = new_start

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if key < reader.get(mid):
            end_index = mid - 1
        elif key > reader.get(mid):
            start_index = mid + 1
        else:
            return mid
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))

    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array_optimized(reader, 16))
    print(search_in_infinite_array_optimized(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array_optimized(reader, 15))
    print(search_in_infinite_array_optimized(reader, 200))


main()
