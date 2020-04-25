"""
Given a sorted array, create a new array containing squares of all the
number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

steps :
1. find a center where left side <= 0 and right side is >= 0
   - if left < right, sq(left) and decrement left
   - if left > right, sq(right) and increment right
   loop until left > 0 or right < len(arr)

3. if left > 0, put all the left elements square into array
4. if right < len(arr), pull the right elements square into array
"""


def _find_center(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= 0 and arr[mid - 1] <= 0:
            return mid - 1, mid
        elif arr[mid] <= 0 and arr[mid + 1] >= 0:
            return mid, mid + 1

        if arr[mid] >= 0:
            end = mid - 1
        else:
            start = mid + 1

    if start == len(arr) - 1:
        return end, end + 1
    else:
        return start - 1, start


def square_sorted(arr):
    result_array = []
    left, right = _find_center(arr)
    while left >= 0 and right < len(arr):
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square < right_square:
            result_array.append(left_square)
            left -= 1
        else:
            result_array.append(right_square)
            right += 1

    while left >= 0:
        result_array.append(arr[left] * arr[left])
        left -= 1
    while right < len(arr):
        result_array.append(arr[right] * arr[right])
        right += 1
    return result_array


# Approach - 2
# if you have to populate result array from left to right, you need to find
# the middle element which is lowest and go left and right. (hard to find)
# instead, you if you populate array from end, you can go from both ends.
def square_sorted_tp(arr):
    new_array = [None] * len(arr)
    start = 0
    end = len(arr) - 1
    index = len(arr) - 1
    while start <= end:
        s_square = arr[start] * arr[start]
        e_square = arr[end] * arr[end]
        if s_square > e_square:
            new_array[index] = s_square
            start += 1
        else:
            new_array[index] = e_square
            end -= 1
        index -= 1
    return new_array


print(square_sorted_tp([-3, -2, -1, 0, 0, 1, 2, 3, 4, 5]))
