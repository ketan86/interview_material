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
        AND with 1 (1 -> 1 and 0 -> 0) and add that number
        with right shift number that we have already calculated in past.

        For ex,

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
        """
        results = [0] * (num + 1)
        for i in range(1, num + 1):
            right_shifted_number = i >> 1
            results[i] = results[right_shifted_number] + (i & 1)
        return results

# print(Solution().countBits(15))
# @lc code=end

