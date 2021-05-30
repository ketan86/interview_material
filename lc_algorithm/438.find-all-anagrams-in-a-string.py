#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.


# Example 1:

# Input: s = "cbaebabacd", p = "abc"
#                    ---
# Output: [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.


# @lc code=start

from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        Runtime: 164 ms, faster than 39.96%


        KEY : Keep windown size fixed to len(p) and move window 1 step at 
        a time.

        # Input: s = "cbaebabacd", p = "abc"
                      -
                      --
                      ---  <- check if anagram
                      ----
                       --- <- check if anagram after reducing/deleting start char
                       ----
                        ---
        """
        result = []
        if not s:
            return result

        p_counter = Counter(p)
        s_counter = Counter()

        start = 0
        for end in range(len(s)):
            s_counter[s[end]] += 1

            if end - start >= len(p):
                s_counter[s[start]] -= 1
                if s_counter[s[start]] == 0:
                    del s_counter[s[start]]
                start += 1

            if s_counter == p_counter:
                result.append(start)

        return result


print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
# @lc code=end
