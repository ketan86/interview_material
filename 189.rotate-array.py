#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (31.11%)
# Likes:    1975
# Dislikes: 715
# Total Accepted:    388.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
# Example 1:
#
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Note:
#
#
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#

# @lc code=start


# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.

#         """
#         # n = len(nums)
#         # i = 0
#         # temp = nums[i]
#         # for _ in range(n):
#         #     i += k
#         #     if i > n - 1:
#         #         i = i - n
#         #     temp2 = nums[i]
#         #     nums[i] = temp
#         #     temp = temp2

#         # return nums

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.

        Let n=7n=7 and k=3k=3.

        Original List                   : 1 2 3 4 5 6 7
        After reversing all numbers     : 7 6 5 4 3 2 1
        After reversing first k numbers : 5 6 7 4 3 2 1
        After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
        """
        n = len(nums)
        if n < 1:
            return nums
        k = k % n
        # reverse the array
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# print(Solution().rotate([1], 3))
# @lc code=end
