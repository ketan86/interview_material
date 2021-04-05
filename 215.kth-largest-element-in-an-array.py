#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (53.49%)
# Likes:    3327
# Dislikes: 232
# Total Accepted:    580.7K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#

# @lc code=start
# pylint:skip-file
import heapq


class Solution:
    # O(nlogn) solution
    def findKthLargest(self, nums, k):
        # sort and return the kth element from end
        nums.sort()
        return nums[len(nums)-k]

    # O(nlogk) solution  ---> Better than above
    def findKthLargest(self, nums, k):
        """Runtime: 68 ms, faster than 50.12%"""
        # min heap to store the max k largest elements
        min_heap = []

        for i in nums:
            # store first k elements
            if len(min_heap) < k:
                heapq.heappush(min_heap, i)
            else:
                # if top element is less than the current element,
                # replace it with current element
                top = min_heap[0]
                if i > top:
                    heapq.heapreplace(min_heap, i)

        # top element is the kth largest. peek or pop
        return min_heap[0]
        # or return heapq.heappop(min_heap)

# @lc code=end
