"""
Given an unsorted array of numbers, find k smallest numbers in it.


Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: [5, 1, 2]

Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: [5, 2, 5, 1]

Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: [11, 5, -1]
"""
# pylint: skip-file
import heapq


def find_K_smallest_number(nums, k):
    # use max heap to store top max elements
    max_heap = []
    for num in nums:
        # push k elements to max heap using the negative sign
        if len(max_heap) < k:
            heapq.heappush(max_heap, -num)
        else:
            # if top element value is greater than current element value,
            # swap top element with current element
            if max_heap[0] < -num:
                heapq.heapreplace(max_heap, -num)

    # return the top k elements by changing the sign to recreate the prev list
    return [-num for num in max_heap]


def main():

    print("K smallest number is: " +
          str(find_K_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest
    # numbers should be a '5'
    print("K smallest number is: " +
          str(find_K_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("K smallest number is: " +
          str(find_K_smallest_number([5, 12, 11, -1, 12], 3)))


main()
