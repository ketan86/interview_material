#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up
# to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example 3:

# Input: nums = [3, 3], target = 6
# Output: [0, 1]


# Constraints:

# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# @lc code=start
class Solution:
    def twoSum(self, nums, target_sum):
        d = {}

        for index, n in enumerate(nums):
            d[n] = index

        for index, n in enumerate(nums):
            target = target_sum - n
            if target in d and index != d[target]:
                return [index, d[target]]

    def twoSum(self, nums, target_sum):
        """Runtime: 44 ms, faster than 81.78%"""
        d = {}

        for index, n in enumerate(nums):
            target = target_sum - n
            if target in d:
                return [d[target], index]
            d[n] = index


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([2, 7, 11, 15], 9))

# @lc code=end
