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


def remove_duplicates(arr):
    if not arr:
        return 0
    # non-duplicate end index
    non_duplicate_end = 0
    for index, item in enumerate(arr):
        # if non_duplicate_end item and current item is not same,
        # swap next item with current item.

        # NOTE: if non_duplicate_end's next item same as current, swap does not
        # do any harm.
        if arr[non_duplicate_end] != item:
            non_duplicate_end += 1
            arr[non_duplicate_end], arr[index] = \
                arr[index], arr[non_duplicate_end]

    # if all items are done, length should be non_duplicate_end + 1
    return non_duplicate_end + 1


print(remove_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 4, 5]))
