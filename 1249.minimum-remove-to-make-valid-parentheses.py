#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (61.18%)
# Likes:    574
# Dislikes: 20
# Total Accepted:    48.1K
# Total Submissions: 78.6K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters. 
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
#
# Formally, a parentheses string is valid if and only if:
#
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
#
#
#
# Example 1:
#
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
#
# Example 2:
#
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#
#
# Example 3:
#
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Example 4:
#
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.
#
#

# @lc code=start
# pylint: skip-file

from string import ascii_lowercase


class Solution:
    def minRemoveToMakeValid(self, s):
        output = ''
        if not s:
            return output

        # stack to store the parentheses and index where it occured
        stack = []

        # loop over the input string
        for index, char in enumerate(s):
            # if char is ')' and we find '(' on top of the
            # stack, pop the stack value.
            if char == ')' and stack and stack[-1][0] == '(':
                stack.pop()
            # else if it is not an lowercase ascii value, push
            # into stack.
            else:
                if char not in ascii_lowercase:
                    stack.append((char, index))

        # traverse reverse the string and build the output string
        n = len(s) - 1
        while n >= 0:
            # it stack is not empty and index matches the index
            # of the top stack value, do not append the char
            if stack and n == stack[-1][1]:
                stack.pop()
            # else, append the char in front of the output string.
            else:
                output = s[n] + output
            n -= 1

        # return the result.
        return output


# print(Solution().minRemoveToMakeValid('(a(b(c)d)'))
# @lc code=end
