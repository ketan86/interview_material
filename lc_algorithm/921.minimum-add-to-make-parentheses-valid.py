#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
"""
921. Minimum Add to Make Parentheses Valid
Medium

1307

88

Add to List

Share
Given a string s of '(' and ')' parentheses, we add the minimum number of 
parentheses ( '(' or ')', and in any positions ) so that the resulting 
parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid 
strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must 
add to make the resulting string valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
Example 3:

Input: s = "()"
Output: 0
Example 4:

Input: s = "()))(("
Output: 4
 

Note:

s.length <= 1000
s only consists of '(' and ')' characters.
"""

# @lc code=start


class Solution:
    def minAddToMakeValid(self, s):
        """Runtime: 32 ms, faster than 57.66%"""
        # stack to maintain the parentheses
        stack = []

        for char in s:
            if stack and char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


print(Solution().minAddToMakeValid('())'))
print(Solution().minAddToMakeValid('((('))
print(Solution().minAddToMakeValid('()'))
print(Solution().minAddToMakeValid('))(()()'))
print(Solution().minAddToMakeValid('))))'))
# @lc code=end
