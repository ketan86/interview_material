#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.29%)
# Likes:    6508
# Dislikes: 288
# Total Accepted:    799.1K
# Total Submissions: 1.7M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#

# @lc code=start
# pylint: skip-file

# O(n^2)


class Solution:
    def maxSubArray(self, nums):
        """
        [-2,1,-3,4,-1,2,1,-5,4]
          i j = -2 + 1 = -1 max(-2, -1) = -1
               j = -1 + -3 = -4 max(-1, -4) = -1
                 j = -4 + 4 = 0 max(-1, 0) = 0
                 ...
            i j = 1 + -3 = -2 ...

        """
        n = len(nums)
        if n < 1:
            return 0
        # initialize the max_sum to first element.
        max_sum = nums[0]
        for i in range(n):
            # initialize running_sum to current ith index and find running sum.
            running_sum = nums[i]
            for j in range(i + 1, n):
                running_sum += nums[j]
                # keep calculating the max_sum.
                max_sum = max(max_sum, running_sum)
        return max_sum

# O(n)


class Solution:
    def maxSubArray(self, nums):
        """
        [-5, -1, -4, -3]
         -5  -1  -4  -3

        max_sum | i | nums[i-1] | nums[i]
        -5        0
        -5        1        -5        -1 = -5 < 0 = max(-5, -1) = -1
                  2        -1        -4 = -1 < 0 = max(-1, -4) = -1
                  3        -4        -3 = -4 < 0 = max(-1, -3) = -1
                  ...

        [-2, 1, 4, -3, 2]
         -2  1  5  2   4

        max_sum | i | nums[i-1] | nums[i]
        -2        0
                  1      -2          1 = -2 < 0 = max(-2, 1) = 1
                  2       1          4 = 1 < 0 = max(1, 5) = 4
                  ...
        """

        n = len(nums)
        if n < 1:
            return 0
        # initialize max sum to first element.
        max_sum = nums[0]
        # loop over the elements and if previous element is non-negative,
        # add previous number to current and keep calculating the sum.

        # if previous number is negative, current number is considered the
        # subarray.
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            # keep calculating the max_sum between previous sum and current
            # number.
            max_sum = max(nums[i], max_sum)
        return max_sum


# @lc code=end
