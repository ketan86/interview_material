"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates
in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be
[2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be
[2, 11].
"""
# two pointer, one finds the unique number and other waits at the place
# where that unique number should be replaced to remove duplicates

# pylint: skip-file


def remove_duplicates(nums):
    if not nums:
        return 0

    # prev pointer
    i = 0
    # running pointer
    j = 1

    # use two pointers and if forward pointers find a number that is not
    # equal to current pointer value (unique), increment the ith index
    # and swap the number with j index.
    while j < len(nums):
        if nums[i] != nums[j]:
            # increment first because till ith index, elements
            # are unique already.
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
        j += 1

    return i + 1


print(remove_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 4, 5]))
