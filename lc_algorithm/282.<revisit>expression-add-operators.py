#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (35.06%)
# Likes:    1110
# Dislikes: 178
# Total Accepted:    96.3K
# Total Submissions: 274K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
#
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
#
# Example 3:
#
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
#
# Example 4:
#
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#
#
# Example 5:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
#
#
#


#                       123
#                + /     \-      \* 
#             1 + "23"  1 - "23"  1 * 23 = target
#          + /  \-    \*   
#    1+2+3     1+2-3  1+2*3


#         for i in range(len(123)):
#             # 1, 23 : 12, 3 : 123
#             for i in range("+-*"):
#                 # 1+23, 1-23, 1*23
#                 ...


# @lc code=start


class Solution:
    def addOperators(self, num, target):
        pass
# @lc code=end
