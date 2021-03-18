"""
Problem Statement #
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""
# pylint: skip-file

from collections import deque


def find_subsets(nums):
    queue = deque()
    queue.append([])
    index = 0
    while queue:
        n = len(queue)
        for i in range(n):
            num = queue.popleft()
            num_copy = list(num)
            num_copy.append(nums[index])
            queue.append(num)
            queue.append(num_copy)
        index += 1

        if index == len(nums):
            break
    return list(queue)


# without removing elements

def find_subsets_without_removal(nums):
    subsets = []
    subsets.append([])

    for num in nums:
        n = len(subsets)
        for i in range(n):
            set_ = list(subsets[i])
            set_.append(num)
            subsets.append(set_)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

    print("Here is the list of subsets without removal: " +
          str(find_subsets_without_removal([1, 3])))
    print("Here is the list of subsets without removal: " +
          str(find_subsets_without_removal([1, 5, 3])))


main()
