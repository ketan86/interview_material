#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
import sys


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        shortest_str = strs[0]
        for i, ch in enumerate(shortest_str):
            for item in strs:
                if item[i] != ch:
                    return shortest_str[:i]
            i += 1
        return shortest_str[:i]


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
