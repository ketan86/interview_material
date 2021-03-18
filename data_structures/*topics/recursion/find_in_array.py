"""
Given an array of ints, compute recursively if the array contains a 6.
We'll use the convention of considering only the part of the array
that begins at the given index. In this way, a recursive call can
pass index+1 to move down the array. The initial call will pass in index as 0.


array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
"""


def find_in_array(a, n):
    if len(a) == 1:
        if a[0] == n:
            return 1
        return 0

    return find_in_array(a[:1], n) + find_in_array(a[1:], n)


found = find_in_array([1, 8, 5, 6, 8], 8)
print(found)
