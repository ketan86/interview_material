#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.59%)
# Likes:    1592
# Dislikes: 151
# Total Accepted:    294.1K
# Total Submissions: 411.7K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 2^31.
#
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠       ↑   ↑
#
# The above arrows point to positions where the corresponding bits are
# different.
#
#
#
# @lc code=start
class Solution:
    def hammingDistance(self, x, y):
        """
        Hamming distance of two integers is a number of bits that are
        different.

        for ex, 101 & 110 (2 bits are different)
                111 & 110 (1 bit is different)

        we could solve this by two ways,

            1. iterate over the largest number and keep right shifting both
               numbers and when right most bit of both numbers are not same,
               increase the bits_diff.

            2. xor both numbers. after xoring, only different numbers are left
               in the result. count number of one's in the result to find the
               bits_diff.


        """

        # larger = max(x,y)
        # smaller = min(x,y)
        # bits_diff = 0
        # while larger:
        #     larger_rmb = larger & 1
        #     smaller_rmb = smaller & 1
        #     if larger_rmb != smaller_rmb:
        #         bits_diff += 1
        #     larger >>= 1
        #     smaller >>= 1

        # return bits_diff

        # XOR tow numbers and count 1's
        bits_diff = 0
        xor = x ^ y
        while xor:
            if xor & 1 == 1:
                bits_diff += 1
            xor >>= 1

        return bits_diff


# print(Solution().hammingDistance(73,93))
# @lc code=end
