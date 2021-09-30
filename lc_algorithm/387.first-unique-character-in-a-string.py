#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# Given a string s, return the first non-repeating character
# in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1


# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


# @lc code=start
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s):
        """124ms beats 54.67 %"""
        char_set = defaultdict(int)

        for char in s:
            char_set[char] += 1

        for index, char in enumerate(s):
            if char_set[char] == 1:
                return index

        return -1


print(Solution().firstUniqChar('leetcode'))
print(Solution().firstUniqChar('loveleetcode'))
# print(Solution().firstUniqChar('aabb'))
# @lc code=end
