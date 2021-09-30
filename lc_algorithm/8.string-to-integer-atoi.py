#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # there are 5 cases, 
        # 1. first character can be whitespace,'-','+', any digit, any other character than digit.
        # for whitespace , first remove all whitespace through split. the new string will have 4 cases above
        # for -,+ will tell about the sign of output and don't consider them for digit formation, remove them
        # if the character is digit then form a number , repeat till you don't encounter any other character than digit
        # check the boundary condition and return accordingly

        ls = list(s.strip())

        if len(ls) == 0:
            return 0
        # see whether sign positive or negative and
        # remove it as will not consider in digit formation.
        if ls[0] == '-':
            sign = -1
        else:
            sign = 1

        if ls[0] in ['-', '+']:
            del ls[0]

        # ret stores our final number if exists.
        ret, i = 0, 0
        # check if the character is digit, if yes then convert to int and form number else leave
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1

        # boundary check
        return max(-2**31, min(sign * ret, 2**31-1))


print(Solution().myAtoi("0"))
# @lc code=end
