"""
Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence, we can’t
count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue;
and since our input array also consists of three different numbers that is
why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""
# pylint: skip-file


def dutch_flag_sort(arr):
    """
    Use three pointers low, high and i.
    1. low and high pointers define the ending and starting of the 0's and 2's windows.
    2. i moves from 0 to high and swaps with low and high numbers if 0 and 2 are found
    respectively.
    3. * if 0 is found, i and low increments
       * if 2 is found high decrements and
       * if 1 is found, i increments.
    """
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            # increment 'i' and 'low'
            i += 1
            low += 1

        elif arr[i] == 1:
            i += 1
        else:  # the case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1

    return arr


print(dutch_flag_sort([1, 0, 2, 1, 0]))
print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
