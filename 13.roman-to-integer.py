#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev_char = None
        prev_value = 1001
        num = 0
        for i in s:
            if map[i] <= prev_value:
                num += map[i]
            else:
                num += map[i] - map[prev_char] - prev_value
            prev_char = i
            prev_value = map[i]
        return num


print(Solution().romanToInt('M'))
