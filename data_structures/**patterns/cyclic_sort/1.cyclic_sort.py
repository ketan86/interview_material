"""
We are given an array containing ‘n’ objects. Each object, when created,
was assigned a unique number from 1 to ‘n’ based on their creation sequence.
 This means that the object with sequence number ‘3’ was created just before
 the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence
number in O(n) and without any extra space. For simplicity, let’s assume
we are passed an integer array containing only the sequence numbers, though
each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""

# keep swapping until number comes to the right place.
# first soultion, goes through the array and moves to different.

"""
3 1 5 4 2
None 1 3 4 2 -> 5 in temp 
None 1 3 4 5 -> 2 in temp 
None 2 3 4 5 -> 1 in temp 
1 2 3 4 5 -> None in temp -> break since it's None.
"""


def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        if arr[i] - 1 == i:
            i += 1
            continue
        curr = arr[i]
        arr[i] = None
        while curr is not None:
            temp = arr[curr - 1]
            arr[curr - 1] = curr
            curr = temp
        i += 1
    return arr


"""
Another solution would be the swap until number at the current index is the 
right number.
3 1 5 4 2
^
5 1 3 4 2 -> swap(3,5)
2 1 3 4 5 -> swap(5,2)
1 2 3 4 5 -> swap(2,1)
  ^
    ^
      ^
        ^ -> done
"""


def cyclic_sort(arr):
    for i in range(len(arr)):
        while arr[i] - 1 != i:
            # one liner swap would not
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
    return arr


print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))
