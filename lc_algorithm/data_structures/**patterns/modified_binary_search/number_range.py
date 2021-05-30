"""
Given an array of numbers sorted in ascending order, find the range of a
given number ‘key’. The range of the ‘key’ will be the first and last
position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not
present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
"""
# pylint: skip-file


def find_range(arr, key):
    result = [-1, -1]
    start = 0
    end = len(arr) - 1
    if arr[start] == key and arr[end] == key:
        return [start, end]

    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return _find_boundary(arr, mid, key)

    return result

# O(n)


def _find_boundary(arr, mid, key):
    start = mid
    end = mid

    while arr[start - 1] == key:
        start -= 1

    while arr[end + 1] == key:
        end += 1

    return [start, end]


def find_range_efficient(arr, key):

    start = 0
    end = len(arr) - 1
    # search far left element
    far_left = _binary_search(arr, start, end, key, search_left=True)
    if far_left == -1:
        return [-1, -1]
    else:
        # serach far right element
        far_right = _binary_search(arr, far_left, end, key, search_left=False)
        # we do not have to check far_right since far_left is found and
        # in worse, case far_right will be the far_left.
        return [far_left, far_right]


def _binary_search(arr, start, end, key, search_left):
    """Technique to find the far left or far right number matching the key.

    1. use index to store the matched number and move left or right when key
       is less/right or equal to mid.
    2. return index that hold the far left or right matched element.
    """
    index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            index = mid
            if search_left:
                end = mid - 1
            else:
                start = mid + 1
    return index


def main():
    # print(find_range([4, 6, 6, 6, 9], 6))
    # print(find_range([1, 3, 8, 10, 15], 10))
    # print(find_range([1, 3, 8, 10, 15], 12))
    # print(find_range([8, 8, 8, 8, 8], 8))

    print(find_range_efficient([4, 6, 6, 6, 9], 6))
    print(find_range_efficient([1, 3, 8, 10, 15], 10))
    print(find_range_efficient([1, 3, 8, 10, 15], 12))
    print(find_range_efficient([8, 8, 8, 8, 8], 8))


main()
