#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (40.16%)
# Likes:    1535
# Dislikes: 258
# Total Accepted:    412.7K
# Total Submissions: 960.7K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a, b):
        """
        # NOTE: Solution without using binary opeations. (using operators)
        result = ''
        carry = 0
        length = max(len(a), len(b))
        if len(a) < length:
            a = '0' * (length - len(a)) + a
        if len(b) < length:
            b = '0' * (length - len(b)) + b
        index = length - 1
        while index >= 0:
            if int(b[index]) + int(a[index]) + carry == 2:
                carry = 1
                result = '0' + result
            elif int(b[index]) + int(a[index]) + carry == 0:
                carry = 0
                result = '0' + result
            elif int(b[index]) + int(a[index]) + carry == 1:
                carry = 0
                result = '1' + result
            elif int(b[index]) + int(a[index]) + carry == 3:
                carry = 1
                result = '1' + result
            index -= 1
        if carry == 1:
            result = '1' + result
        return result
        """
        # NOTE: solution using binary operators.
        carry = 0
        # covert string values to binary
        a = int(a, 2)
        b = int(b, 2)
        # when carry becomes zero, stop
        while b !=0:
            # find the carry
            carry = a & b
            # xor a and b to find the sum
            a = a ^ b
            # set carry value left shifted so carry can be added to the sum
            # (stored in a)
            b = carry << 1
            
        return format(a, 'b')

# @lc code=end

