#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.24%)
# Likes:    3925
# Dislikes: 89
# Total Accepted:    333.6K
# Total Submissions: 792.4K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
# pylint: skip-file
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return 0
        dp = [1] * len(nums)
        # run two pointers i and j. i starts from 1 since at 0'th index,
        # the max length is already one.
        # j runs from 0 to i and increments ith value by 1 (
        # length is incremented by 1) if ith value is
        # greater than the jth value.
        for i in range(1, len(nums)):
            # start from 0 till i to find what should be the max ith value
            # based on the jth value.
            for j in range(0, i):
                # if ith value is greater than jth value.
                if nums[i] > nums[j]:
                    # if increament is greater than the current max.
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


"""
In order to find all elements with max longest increasing subsequence,
we can store the previous index at the ith index to find all elements.
"""
class Solution2:
    def elementsOfLIS(self, nums):
        """
        At every index, calculate max(all increating numbers length) you could
        build.

        2 pointer problem.

        for ex,
            10, 9, 2, 5, 3
            10    1
            9     1(10<9)
            2     1(2<10 and 2<9)
            5     1+1(from 2) = 2(5>2 but 5<10 and 5<9)
            3     1+1(from 2) = 2(3>2 but 3<10 and 3<9)
        """
        if len(nums) < 1:
            return 0
        indexes = [0] * (len(nums) + 1)
        dp = [1] * len(nums)
        # run two pointers i and j. i starts from 1 since at 0'th index,
        # the max length is already one.
        # j runs from 0 to i and increments ith value by 1 (
        # length is incremented by 1) if ith value is
        # greater than the jth value.
        for i in range(1, len(nums)):
            # start from 0 till i to find what should be the max ith value
            # based on the jth value.
            for j in range(0, i):
                # if ith value is greater than jth value.
                if nums[i] > nums[j]:
                    # if increament is greater than the current max.
                    dp[i] = max(dp[i], dp[j] + 1)
                    indexes[i+1] = j
        import pdb;pdb.set_trace()
        return max(dp)


print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution2().elementsOfLIS([10,9,2,5,3,7,101,18]))
# @lc code=end

