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
        n = len(nums)
        if n < 1:
            return 0
        minVal = nums[0]
        maxVal = nums[0]
        maxProduct = nums[0]

        for i in range(1, len(nums)): 

            # When multiplied by -ve number, 
            # maxVal becomes minVal 
            # and minVal becomes maxVal. 
            if (nums[i] < 0): 
                maxVal, minVal = minVal, maxVal

            # maxVal and minVal stores the 
            # product of subarray ending at nums[i]. 
            maxVal = max(nums[i], maxVal * nums[i]) 
            minVal = min(nums[i], minVal * nums[i]) 

            # Max Product of array. 
            maxProduct = max(maxProduct, maxVal) 


print(Solution().maxProduct([6, -2, 3, -4, 5]))
# @lc code=end
