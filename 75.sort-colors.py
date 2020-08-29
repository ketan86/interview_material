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
# pylint: skip-file


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.

        KEY: m pointer advances and swaps numbers with i and j pointers
        based on the fact that the all 0's must be on left and all 2's
        must be on right.
        """
        # here i represent the far left (0) and j far right(2)
        # m moves ahead and if it is 0, swap with i and if 2,
        # swap with j.
        i = 0
        j = len(nums) - 1
        m = 0
        # move m till it crosses j. m and j must meet :)
        # NOTE: usecase fails if m < j ([2,0,1])
        while m <= j:
            # if m is 0, swap with i and increment i and m
            if nums[m] == 0:
                nums[m], nums[i] = nums[i], nums[m]
                i += 1
                m += 1

            # if m is 1, move m
            elif nums[m] == 1:
                m += 1
            # if m is 2, swap with j and decrement j
            elif nums[m] == 2:
                nums[m], nums[j] = nums[j], nums[m]
                j -= 1

        return nums


print(Solution().sortColors([2, 0, 1]))


# @lc code=end
