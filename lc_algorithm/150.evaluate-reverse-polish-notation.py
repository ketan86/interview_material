#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# Medium

# Evaluate the value of an arithmetic expression in Reverse Polish
# Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer
# or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.


# Example 1:

# Input: tokens = ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10", "6", "9", "3", "+",
#                  "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range[-200, 200].
# Accepted
# 304, 837
# Submissions
# 771, 628

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            # in reverse polish do not use floor to find the division
            # instead of divide and find the int.
            # >>> 6 // -132
            # -1
            # >>> 6 / -132
            # -0.045454545454545456
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        stack = []
        for t in tokens:
            if t in operations:
                right = stack.pop()
                left = stack.pop()
                stack.append(operations[t](left, right))
            else:
                stack.append(int(t))

        return stack.pop()

# @lc code=end
