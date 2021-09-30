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
#                                       [4,6,7,0,1,2,3]
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

from multiprocessing import Lock


class Solution:

    def search(self, nums, target):
        """
        Divide array and every division is sorted array than further be 
        divided and search.

        nums = [4,5,6,7,0,1,2], target = 0
                i           j
                      m
                4 > 7  --> 0 > 4 and 0 > 7
                      |
                       --> go right 
                [0,1,2]
                 i   j
                   m
        """
        start = 0
        end = len(nums) - 1
        if not nums:
            return -1

        if target == nums[0]:
            return 0

        if target == nums[-1]:
            return len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            # check in left sorted
            elif nums[mid] >= nums[start]:
                # if target in left sorted
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # check in right sorted
            else:
                # target in right sorted
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

    def search(self, nums, target):
        n = len(nums)
        if n < 1:
            return - 1

        # find the minimum number index.
        min_index = self._find_min_index(nums)

        # if target value is greater than last value, search
        # in left subarray from 0 to min_index - 1
        # else, search in right subarray from min_index to n.
        if target > nums[n - 1]:
            return self._binary_search(0, min_index - 1, nums, target)
        return self._binary_search(min_index, n, nums, target)

    def _find_min_index(self, nums):
        start_index = 0
        end_index = len(nums) - 1

        # if array is sorted already. (may contain duplicates so >=)
        if nums[end_index] >= nums[start_index]:
            return nums[start_index]

        while start_index <= end_index:
            mid = start_index + ((end_index - start_index) // 2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[len(nums) - 1]:
                start_index = mid + 1
            else:
                end_index = mid

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


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([4, 6, 7, 0, 1, 2, 3], 3))
print(Solution().search([4, 1, 2, 3], 3))
print(Solution().search([], 3))
# @lc code=end
