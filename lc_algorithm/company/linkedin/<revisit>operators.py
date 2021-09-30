"""
Given a string of digits and a goal target, using operators +, -, *, / evaluate
if it is possible to reach a target

Example:
1. 2451 -> 2 * 4 + 5 / 1
2. 2011051945 -> 2 + 0 - 1/1-0+5*1-9+45

Question:
1. divide by zero
2. numb starting with sign + or - 
3. start with zero not valid
4. overflow
5. num can not start with * or /

follow up:
1. ** or bitwise
2. out of order num

"""


class Solution:

    def find_goal_target(self, num, target):
        result = []
        if not num:
            return result
        self.dfs(num, 0, '', target, result)
        return result

    def dfs(self, num, index, eval_string, target, result):
        if index == len(num):
            if eval(eval_string) == target:
                result.append(eval_string)
        else:
            for i in range(index, len(num)):
                pass
