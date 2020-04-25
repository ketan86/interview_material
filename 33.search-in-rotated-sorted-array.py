#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.10%)
# Likes:    3465
# Dislikes: 388
# Total Accepted:    543.1K
# Total Submissions: 1.6M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
#

# @lc code=start


class Solution:
    def search(self, nums, target):
        n = len(nums)
        if n < 1:
            return - 1
        # find pivot
        pivot_index = self._find_pivot_index(nums)

        if target > nums[n - 1]:
            return self._binary_search(0, pivot_index, nums, target)
        return self._binary_search(pivot_index + 1, n, nums, target)

    def _find_pivot_index(self, nums):
        start_index = 0
        end_index = len(nums) - 1
        while start_index <= end_index:
            mid = start_index + ((end_index - start_index) // 2)
            if nums[mid] > nums[len(nums) - 1]:
                start_index = mid + 1
            else:
                end_index = mid - 1

        return end_index

    def _binary_search(self, start_index, end_index, nums, target):
        while start_index <= end_index:
            mid = start_index + ((end_index - start_index) // 2)
            if nums[mid] < target:
                start_index = mid + 1
            elif nums[mid] > target:
                end_index = mid - 1
            else:
                return mid

        return -1


# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
# @lc code=end
