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
        """Runtime: 4088 ms, faster than 15.24%"""
        if len(nums) < 1:
            return 0
        # max LIS for each number is 1
        dp = [1] * len(nums)

        # to maintain the max so far.
        # NOTE: max wont be at the end of the dp because in below example,
        # when we are at last index (1), the LIS will be 1 instead of 4.
        # for ex,# [10, 9, 2, 5, 3, 7, 101, 1]
        #           1   1  1  2  2  3   4   1
        max_so_far = dp[0]

        for i in range(1, len(nums)):
            # start from 0 till i to find the max LIS if current value is
            # greater than jth value.
            for j in range(0, i):
                # if ith value is greater than jth value.
                if nums[i] > nums[j]:
                    # if increment is greater than the current max.
                    dp[i] = max(dp[i], dp[j] + 1)

            # calculate max so far
            max_so_far = max(max_so_far, dp[i])

        # return max_so_far
        return max_so_far


class Solution2:
    """
    In order to find all elements with max longest increasing subsequence,
    we can store the previous index at the ith index to find all elements.
    """

    def allElementsOfLIS(self, nums):
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
        # max LIS for each number is 1
        dp = [1] * len(nums)

        # NOTE: max wont be at the end of the dp because in below example,
        # when we are at last index (1), the LIS will be 1 instead of 4.
        # for ex,# [10, 9, 2, 5, 3, 7, 101, 1]
        #           1   1  1  2  2  3   4   1

        # maintain the prev index at each number from where this number can
        # be reached while increasing. -1 represents that the starting of the
        # LIS and there is no smaller number before that number. if that number
        # is not -1, use that index to reach the previous number in the chain.
        indexes = [-1] * (len(nums) + 1)

        for i in range(1, len(nums)):
            # start from 0 till i to find what should be the max ith value
            # based on the jth value.
            for j in range(0, i):
                # if ith value is greater than jth value.
                if nums[i] > nums[j]:
                    # if increment is greater than the current max.
                    dp[i] = max(dp[i], dp[j] + 1)
                    # put the last index of j from where we reached i for LIS
                    indexes[i + 1] = j
        # results represent the index from where we reached current number
        # while maintaining the increasing order.
        # [10, 15, 12, 5, 3, 7, 101, 18] -> [-1, -1, 0, 0, -1, -1, 4, 5, 5]

        # NOTE: in order to find the LIS array,
        # 1. find max number in the indexes,
        # 2. iterate from max number in reverse order
        #   1. use current index of indexes to find the number in nums array
        #   2. use value of the current index to find the previous index of
        #       and extract the value and continue

        return indexes


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution2().allElementsOfLIS([10, 15, 12, 5, 3, 7, 101, 18]))
# @lc code=end
