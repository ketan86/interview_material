#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# Hard

# Given a string s representing an expression, implement a basic calculator to 
# evaluate it.

# Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval().
# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23


# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# Accepted
# 211,901
# Submissions
# 551,977

# @lc code=start
class Solution:

    def calculateUsingEval(self, s: str) -> int:
        """
        Runtime: 132 ms, faster than 23.24%

        This solution requires reversing of the sub-expressions in order
        to evaluate the sub-expression in order.

        for ex, (7-8+9), stack -> [9,+,8,-,7,')']
        - in order to process this sub expression, we can not do it
        without reversing the order or using another stack.

        This soultion builds the expression as string in reverse order
        and uses `eval` to evaluate the expression.

        This solution also takes care of the usecases where s = "1234"
        because `eval('1234')` would calculate the result correctly.
        """

        # result expression
        result_exp = ''
        # stack to store items
        stack = []
        for i in s:
            # if string is not empty then only process the element
            if i != ' ':
                # if char is digit, +, - or (, push it to stack
                if i.isdigit() or i in ('+', '-') or i == '(':
                    stack.append(i)
                else:
                    # else, we found closing bracket ')', create
                    # an expression in reverse order from the stack
                    # until we find the opening bracket '('
                    temp_result_exp = ''
                    while stack[-1] != '(':
                        temp_result_exp = stack.pop() + temp_result_exp

                    # pop the opening bracket and push evaluated
                    # string to stack after converting it to string.
                    stack.pop()
                    stack.append(str(eval(temp_result_exp)))

        # one we complete the iteration, we only have digits and operators
        # create result expression in reverse order.
        while stack:
            result_exp = stack.pop() + result_exp

        # return evaluated expression.
        return eval(result_exp)

    def calculate(self, s: str) -> int:
        """
        Runtime: 104 ms, faster than 45.51%

        This soultion reverses the string before processing to avoid
        sub-expression reverse processing issue.


        Also it covers following major areas,

        1. how to form an integer that is reversed and followed by another
           integer.

           for ex,     (78+8)-25 -> 52-)8+87(

               process 5 and then 2 and make "25" (reversed)

        2. once non empty char found, push formed digit into stack
        3. when char is '(', evaluate the expression and remove '(' and 
           push result in stack.
        4. when char is operator, push to stack
        5. eval_expression function makes sure if expression starts
           with operator, append 0 to stack before processing the expression
           to avoid, failure.

           for ex, when eval_expression is called, it starts with digit and ends
            with digit unless there is an operator. if there is, append 0 to
            stack before processing it.




        for ex, (1+(4+5+2)-3)+(6+8) -> )8+6(+)3-)2+5+4(+1(

            23  -> ans
            ---
            9
            +
            14
            ---
            ( -> pop until found ')' and sum values between
            1
            +
            11
            -
            3
            )
            +
            14
            ---
            (  -> pop until found ')' and sum values between
            4
            +
            5
            +
            2
            )
            -
            3
            )
            +
            14
            ---
            ( -> pop until found ')' and sum values between
            6
            +
            8
            )
        """

        # stack to store items
        stack = []
        # save operands
        operand = 0
        n = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            # if char is digit and continuing, we need to form the
            # actual number in reverse.
            if char.isdigit():
                # 5 ->  10^0 * 5  + 0 -> 5
                # 2 ->  (10^1 * 2) + 5 -> 25
                # 3 ->  (10^2 * 3) + 25 -> 325
                # ...
                operand = ((10 ** n) * int(char)) + operand
                n += 1
            elif char != ' ':
                if n:
                    stack.append(operand)
                    operand = 0
                    n = 0
                if char == '(':
                    result = self.eval_expression(stack)
                    # pop ')' -> can't move inside eval_expression func
                    # because same func is used to process the last
                    # "1+/-3" kind of expression.
                    stack.pop()
                    stack.append(result)
                else:
                    stack.append(char)

        # once we complete the iteration, we only have digits and operators
        # create result expression in reverse order.
        if n:
            stack.append(operand)

        # return evaluated expression.
        return self.eval_expression(stack)

    def eval_expression(self, stack):
        if stack and stack[-1] in ('+', '-'):
            stack.append(0)
        result = stack.pop() if stack else 0
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                result += stack.pop()
            else:
                result -= stack.pop()
        return result

print(Solution().calculate('(78+8)-25'))
# @lc code=end
