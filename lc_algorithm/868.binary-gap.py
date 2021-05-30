#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#
# https://leetcode.com/problems/binary-gap/description/
#
# algorithms
# Easy (59.76%)
# Likes:    172
# Dislikes: 417
# Total Accepted:    31.2K
# Total Submissions: 51.9K
# Testcase Example:  '22'
# #
# Given a positive integer n, find and return the longest distance between any
# two adjacent 1's in the binary representation of n. If there are no two
# adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them(possibly no 0's).
# The distance between two 1's is the absolute difference between their bit
# positions. For example, the two 1's in "1001" have a distance of 3.


#
#
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating
# the two 1's underlined.
#
#
#
# Example 2:
#
#
# Input: 5
# Output: 2
# Explanation:
# 5 in binary is 0b101.
#
#
#
# Example 3:
#
#
# Input: 6
# Output: 1
# Explanation:
# 6 in binary is 0b110.
#
#
#
# Example 4:
#
#
# Input: 8
# Output: 0
# Explanation:
# 8 in binary is 0b1000.
# There aren't any adjacent pairs of 1's in the binary representation of 8,
# so we return 0.
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= N <= 10^9
#
#
#
#
#
#
#
#
#
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Runtime: 24 ms, faster than 94.77%
        """

        found = False
        max_distance = 0
        curr_distance = 0

        while n > 0:
            # find if right most bit is 1 or 0
            bit = n & 1
            # if bit is 1, and we have found 1 before, calculate the max
            # distance and set current distance to 0. if not found 1 before.
            # set found to True.
            if bit == 1:
                if found:
                    max_distance = max(max_distance, curr_distance)
                    curr_distance = 0
                else:
                    found = True
            # if 0 or 1, if we have found the 1 before, increment the curr
            # distance.
            if found:
                curr_distance += 1

            # right shift 1 bit
            n >>= 1
        return max_distance


print(Solution().binaryGap(22))
print(Solution().binaryGap(5))
print(Solution().binaryGap(6))
print(Solution().binaryGap(8))
print(Solution().binaryGap(0))
print(Solution().binaryGap(3))
print(Solution().binaryGap(4))
# @lc code=end
