#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix

# Given an n x n matrix where each of the rows and columns are sorted in
# ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.


# Example 1:

# Input: matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8 Output: 13
# Explanation: The elements in the matrix are[1, 5, 9, 10, 11, 12, 13, 13, 15],
# and the 8th smallest number is 13 Example 2:

# Input: matrix = [[-5]], k = 1 Output: -5


# Constraints:

# n == matrix.length n == matrix[i].length 1 <= n <= 300 -109 <= matrix[i][j] <=
# 109 All the rows and columns of matrix are guaranteed to be sorted in
# non-degreasing order. 1 <= k <= n2

# @lc code=start
import heapq


class Solution:
    """
    NOTE: This solution uses 3 value tuple because heapq can not sort
    elements when first element of the tuple is same and second value is not
    comparable. Unless row/list defines compartor method (__lt__, __eq__,
    __gt__ etc..), heapq does not know how to sort values when first
    elements are same.
    """

    def kthSmallest(self, matrix, k):
        """Runtime: 216 ms, faster than 30.88%"""
        # use min_heap tp store the value, index of that element in the row
        # and a pointer to the row.
        min_heap = []
        # insert 0th element value, index and a row to min heap.
        for row in matrix:
            heapq.heappush(min_heap, (row[0], 0, row))

        # keep going until k -1 and min_heap.
        while k > 1 and min_heap:
            value, index, row = heapq.heappop(min_heap)
            # if next index of the list is less than the length, push the
            # element into the heap for processing.
            if index + 1 < len(row):
                heapq.heappush(min_heap, (row[index + 1], index + 1, row))
            k -= 1

        # if min heap is empty, return -1
        if not min_heap:
            return -1

        # return the value of the kth smallest element.
        return heapq.heappop(min_heap)[0]

    def kthSmallestUsingBinarySearch(matrix, k):
        raise NotImplemented()

# @lc code=end
