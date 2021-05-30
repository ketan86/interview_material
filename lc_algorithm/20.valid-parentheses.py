#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.40%)
# Likes:    5510
# Dislikes: 233
# Total Accepted:    1.1M
# Total Submissions: 2.8M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: s = "{[]}"
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s):
        # stack to store the left parentheses
        stack = []
        # parenthese map
        d = {'{': '}', '(': ')', '[': ']'}
        for char in s:
            # if char in map, add it to stack
            if char in d:
                stack.append(char)
            else:
                # if stack is not empty and last entry matches
                # the current right parentheses value, pop the
                # left parentheses.
                if stack and d[stack[-1]] == char:
                    stack.pop()
                else:
                    # if stack is empty and found the right
                    # parenthese, its invalid
                    return False
        # if stack is not empty, it's not balanced.
        if stack:
            return False

        # if stack is empty, it's balanced
        return True

# @lc code=end
