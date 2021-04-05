#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (31.21%)
# Likes:    4110
# Dislikes: 853
# Total Accepted:    370K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Follow up:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        """
        Instead of using cyclic sort n^2, this algorithm marks
        numbers negative if they are at the right position.

        for ex, [2,1,0] (-2,-1,0) becomes (-2+4, -1+4, 0+4)
                     *
                [2,1,4]

            abs(2) = 2 & 2 > 3, false so 2 should be placed at 1st position
            so mark 1st position where 1 is located to -1
            [2,-1,4]

            abs(-1) = 1 & 1 > 3, false so 1 should be placed at the 0th
            position. mark 0th position where 2 is located to -2

            abs(4) = 4 & 4 > 3 so exit

            now check the first non-negative number and the index of that
            number is the missing number.

        """
        n = len(nums)
        # mark all -inf, 0 & len(nums) to inf number to n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # find the position of the current number and mark that negative
        # if inbound.
        for i in range(n):
            curr_position = abs(nums[i])
            if curr_position > n:
                continue

            actual_position = curr_position - 1
            if nums[actual_position] > 0:
                nums[actual_position] = -1 * nums[actual_position]

        # a first non negative number's index is the missing number.
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

# @lc code=end
