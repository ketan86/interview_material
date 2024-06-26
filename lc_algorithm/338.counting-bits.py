#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (65.42%)
# Likes:    2107
# Dislikes: 139
# Total Accepted:    228.9K
# Total Submissions: 341K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
#
#

# @lc code=start
class Solution:
    def countBits(self, num):
        """
        Runtime: 84 ms, faster than 60.46%

        NOTE: A number can be formed by left shifting it's right shifted
        number and adding 0 or 1 if current number is even or odd.

        for ex,
              12 -> 1100
                - this number is left shifted number of 6 -> 110 and
                  0 to it's right most bit because it's event
              13 -> 1101
                - this number is left shifted number of 6 -> 110 and
                1 to it's right most bit because it's odd


        AND with 1 (1 -> 1 and 0 -> 0) and add that number
        with right shift number that we have already calculated in past.

        For ex,

        num last_bit + num_of_1's
        0   0
        1   1 & 1    + (right shift 1 >> 1 = 0) 0's 1  = 1
        2   0 & 1    + (right shift 2 >> 1 = 1) 1's 1  = 1
        3   1 & 1    + (right shift 3 >> 1 = 1) 1's 1  = 2
        4   0 & 1    + (right shift 4 >> 1 = 2) 2's 1  = 1
        so on..


        1 1 0 1 -> 13
              1 AND -> 1
        1 1 0 1 >> 1
          1 1 0 -> 6 (we know the 1's in 6 from previous results)

        one's in 13 = 1(13 AND with 1) + 2(13 >> 1 = 6) = 3

        0 -> 0 & 1 + 0 >> 1 = 0 + 0 = 0
        1 -> 1 & 1 + 1 >> 1 = 1 + (0) = 1 + 0 = 1
        2 -> 10 & 1 + 10 >> 1 = 0 + (1) = 0 + 1 = 1
        3 -> 11 & 1 + 11 >> 1 = 1 + (1) = 1 + 1 = 2
        4 -> 100 & 1 + 100 >> 1 = 0 + (10) = 0 + 1 = 1
        ...

        # 0 --> 0   -> 0
        # 1 --> 1   -> 1      => (1 >> 1) + (1 & 1) -> 0 + 1 -> 1
        # 2 --> 10  -> 1      => (2 >> 1) + (2 & 1) -> 1 + 0 -> 1
        # 3 --> 11  -> 2      => (3 >> 1) + (3 & 1) -> 1 + 1 -> 2
        # 4 --> 100 -> 1      => (4 >> 1) + (4 & 1) -> 1 + 0 -> 1
        # 5 --> 101 -> 2      => (5 >> 1) + (5 & 1) -> 1 + 1 -> 2
        # 6 --> 110 -> 2      => (6 >> 1) + (6 & 1) -> 1 + 1 -> 2
        # 7 --> 111 -> 3      => (7 >> 1) + (7 & 1) -> 2 + 1 -> 3
        # 8 --> 1000 -> 1     => (8 >> 1) + (8 & 1) -> 1 + 0 -> 1
        # 9 -> 1001 -> 2      => (9 >> 1) + (9 & 1) -> 1 + 1 -> 2
        # 10 -> 1010 -> 2     => (10 >> 1) + (10 & 1) -> 1 + 1 -> 2
        # 11 -> 1011 -> 3     => (11 >> 1) + (11 & 1) -> 2 + 1 -> 3
        # 12 -> 1100 -> 2     => (12 >> 1) + (12 & 1) -> 1 + 1 -> 2


        """
        # dp to store the nums of 1's for each number
        dp = [0] * (num + 1)
        # starting from 1, right shift 1 and find the result from dp
        # + add AND of last bit to it.
        # for ex, 4 -> 1000, since it' even, last bit it 0 + 4 >> 1 = 2
        # and 2 had one 1. so total 1's = 1
        for i in range(1, num + 1):
            right_shifted_number = i >> 1
            last_digit = (i & 1)
            dp[i] = dp[right_shifted_number] + last_digit

        # return all values till n
        return dp


print(Solution().countBits(5))
# @lc code=end
