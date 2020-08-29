#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (56.16%)
# Likes:    3314
# Dislikes: 281
# Total Accepted:    360.9K
# Total Submissions: 622.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
#
#

# @lc code=start
# pylint:skip-file

# class Solution:
#     def productExceptSelf(self, nums):
#         new_nums = []
#         n = len(nums)
#         if n < 2:
#             return nums
#         for i in range(n):
#             new_nums.append(self.sum_elements(nums, i))
#         return new_nums

#     def sum_elements(self, nums, skip_index):
#         n = len(nums)
#         s = 1
#         for i in range(n):
#             if i == skip_index:
#                 continue
#             s = s * nums[i]
#         return s


class Solution:
    def productExceptSelf(self, nums):
        new_nums = []

        n = len(nums)
        if n < 2:
            return nums

        # calculate left products
        product = 1
        new_nums.append(1)
        for i in range(1, n):
            product = product * nums[i - 1]
            new_nums.append(product)

        # caculate right products
        product = 1
        for i in range(1, n):
            i = n - 1 - i
            product = product * nums[i + 1]
            new_nums[i] = new_nums[i] * product
        return new_nums

# print(Solution().productExceptSelf([1,2,4,5,6,7]))
# @lc code=end
