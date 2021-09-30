#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.82%)
# Likes:    3310
# Dislikes: 138
# Total Accepted:    293.8K
# Total Submissions: 949.5K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#

# @lc code=start


class Solution:
    def maxProduct(self, nums):
        """Runtime: 56 ms, faster than 62.51%"""
        n = len(nums)
        if n < 1:
            return 0

        # maintain min and max so far and max product total
        min_so_far = nums[0]
        max_so_far = nums[0]
        max_product = nums[0]

        # start from 1.. till end
        for i in range(1, len(nums)):

            # if current number is negative, multiplying with current min and
            # max so far would change the product so min and max should be
            # swapped to keep the max product always max.
            if nums[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            # either current element is max or current * max so far is max.
            max_so_far = max(nums[i], max_so_far * nums[i])
            # same as above
            min_so_far = min(nums[i], min_so_far * nums[i])

            # find total max
            max_product = max(max_product, max_so_far)

        return max_product


print(Solution().maxProduct([2, 3, -2, 4]))
# @lc code=end
