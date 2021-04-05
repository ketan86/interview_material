#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (55.88%)
# Likes:    1738
# Dislikes: 148
# Total Accepted:    613.6K
# Total Submissions: 1.1M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    """Runtime: 48 ms, faster than 60.95%"""

    def isAnagram(self, s, t):
        # if both strings are not the same size, they are not
        # anagram.
        if len(s) != len(t):
            return False

        # freq map to store the freq of each char
        # set won't work when same letters are there in t.
        freq_map = defaultdict(int)
        for char in t:
            freq_map[char] += 1

        # iterate over the chars
        for char in s:
            # if char in freq map and freq is > 0, they are
            # still anagrams of each other.
            if char in freq_map and freq_map[char] > 0:
                freq_map[char] -= 1
            else:
                # if char not in freq map or freq is 0. they are
                # not anagram of each other.
                return False
        # if we iterate over all the char in s, and length of both
        # s and t is same, (considering we have the condition to ensure
        # length is same) they are considered anagram. No need to check
        # if freq of each char is 0.
        return True


# @lc code=end
