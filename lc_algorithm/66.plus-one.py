#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.58%)
# Likes:    1146
# Dislikes: 1938
# Total Accepted:    490.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#

# @lc code=start


class Solution:
    def plusOne(self, digits):
        """32 ms, faster than 71.11%"""
        n = len(digits) - 1
        # use carry flag
        carry = False
        # reversed loop
        for i in range(n, -1, -1):
            # increment the digit by 1. We break when
            # carry is False, so increment by 1 also serves
            # the carry addition.
            digits[i] += 1

            # if digit is greater than 9, set it's value to
            # 0 and carry to True
            if digits[i] > 9:
                digits[i] = 0
                carry = True
            # if digit is less than 9, we wont need to check
            # left digits since they will remain same. so break
            else:
                carry = False
                break
        # if carry is set, insert additional digit to left of the
        # array
        if carry:
            digits.insert(0, 1)

        return digits


print(Solution().plusOne([1, 9, 9]))
# @lc code=end
