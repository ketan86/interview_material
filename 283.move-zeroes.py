#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (54.93%)
# Likes:    2749
# Dislikes: 97
# Total Accepted:    588.2K
# Total Submissions: 1.1M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
#

# @lc code=start


class Solution:
    def moveZeroes(self, nums):
        # i = 0
        # j = 1
        # while j < len(nums):
        #     if nums[j] != 0 and nums[i] == 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #     elif nums[i] == 0 and nums[j] == 0:
        #         j += 1
        #     else:
        #         i += 1
        #         j += 1

        # return nums

        # n = len(nums)
        # l = 0
        # for i in range(n):
        #     if(nums[i] != 0):
        #         k = nums[i]
        #         nums[i] = nums[l]
        #         nums[l] = k
        #         l += 1
        # return nums


print(Solution().moveZeroes([1, 0, 0, 1, 0, 2, 1]))
# @lc code=end
