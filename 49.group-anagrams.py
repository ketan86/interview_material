#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (55.30%)
# Likes:    3929
# Dislikes: 196
# Total Accepted:    734.2K
# Total Submissions: 1.3M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    # O(n *k * log(k))
    def groupAnagrams(self, strs):
        # we can use map to store the sorted string and values
        # would be anagram of the sorted string.
        # for ex, eat, ate, tea -> {'aet': ['eat', 'ate', 'tea']}
        # return the values of the dict would give them sorted
        # based on the anagram property
        d = defaultdict(list)
        # O(n)
        for s in strs:
            # find the sorted version of the string and store it
            # in the map.
            # O(k*log(k))
            sorted_str = ''.join(sorted(s))
            d[sorted_str].append(s)

        # d.values() return the list of all the values of the map.
        return d.values()

    # O(n*k)
    def groupAnagramsOptimized(self, strs):
        d = defaultdict(list)
        for s in strs:
            # define a char array with 26 indexes
            # [0, 0, 0, 0, ...]
            # for ex, 'abc' -> [1, 1, 1, 0, ...] -> (1,1,1,0,...)
            char_array = [0] * 26
            for char in s:
                char_array[ord(char) - ord('a')] += 1
            d[tuple(char_array)].append(s)

        # d.values() return the list of all the values of the map.
        return d.values()


# @lc code=end
