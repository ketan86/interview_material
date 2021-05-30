#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s):
        """Runtime: 32 ms, faster than 57.66%"""
        # stack to maintain the parentheses
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)

        return len(stack)


print(Solution().minAddToMakeValid('())'))
print(Solution().minAddToMakeValid('((('))
print(Solution().minAddToMakeValid('()'))
print(Solution().minAddToMakeValid('))(()()'))
print(Solution().minAddToMakeValid('))))'))
# @lc code=end
