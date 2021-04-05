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
        Runtime: 60 ms, faster than 91.95% of Python3

        At each index, either the current element is max sum or prev sum +
        current element is max.

        Based on this max, we calculate the overall max.

        [-5, -1, -4, -3]

        i

        0 -> curr_sum, max_sum = -5
        1 -> curr_sum = max(-1, -5-1) = -1
             curr_sum > max_sum so max_sum = -1
        2 -> curr_sum = max(-4, -4-1) = -4
             curr_sum < max_sum so max_sum = -1
        3 -> curr_sum = max(-3, -4-3) = -7
             curr_sum < max_sum so max_sum = -1

        max_sum = -1

        [-2,1,-3,4,-1]

        i

        0 -> curr_sum, max_sum = -2
        1 -> curr_sum = max(1, -2+1) = 1
             curr_sum > max_sum so max_sum = 1
        -3 -> curr_sum = max(-3, -3+1) = -2
             curr_sum < max_sum so max_sum = 1
        4 -> curr_sum = max(4, -2+4) = 4
             curr_sum > max_sum so max_sum = 4
        -1 -> curr_sum = max(-1, -1+4) = 3
             curr_sum < max_sum so max_sum = 4
        """
        # curr_sum = max(curr_sum + nums[i], curr_sum)
        # max_sum = max(curr_sum, max_sum)

        n = len(nums)
        if n < 1:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


# @lc code=end
print(Solution().maxSubArray([1, -2, 4, 6, -7, -3]))
