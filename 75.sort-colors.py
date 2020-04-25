#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (42.97%)
# Likes:    2291
# Dislikes: 184
# Total Accepted:    391.6K
# Total Submissions: 886.8K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this
# problem.
#
# Example:
#
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
#
#
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
#
#
#

# @lc code=start


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        m = 0
        while m <= j:
            if nums[m] == 0:
                temp = nums[m]
                nums[m] = nums[i]
                nums[i] = temp
                i += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                temp = nums[m]
                nums[m] = nums[j]
                nums[j] = temp
                j -= 1

        return nums


# print(Solution().sortColors([2, 0, 1]))


# @lc code=end
