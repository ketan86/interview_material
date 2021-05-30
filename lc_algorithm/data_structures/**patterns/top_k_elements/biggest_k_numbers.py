"""
Problem Statement #
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this
problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""
# pylint: skip-file
import heapq


def find_k_largest_numbers(nums, k):
    min_heap = []
    for num in nums:
        # add first k elements into the heap.
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        # for, k + 1 to n, if element is greater than current min heap
        # element, pop the min element and insert the current element.
        else:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

    # at the end, you have the biggest k elements.
    return min_heap


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
