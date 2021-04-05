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
        """Runtime: 40 ms, faster than 98.09%"""

        """
        NOTE: By setting j to 0, we can eliminate the need of first
        while loop.

        i = 0
        j = 1

        while i < len(nums) and nums[i] != 0:
            i += 1
            j += 1

        while j < len(nums):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1

        two pointers where one pointer stays at 0 and other moves
        j pointers moves ahead and swaps non zero value with zero
        value at ith pointer.
        """
        n = len(nums)
        i = 0
        for j in range(n):
            # if current value is not zero, swap with ith value that is at
            # zero. move i and j
            # if current value is not zero, move j
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


print(Solution().moveZeroes([1, 0, 0, 1, 0, 2, 1]))

# @lc code=end
