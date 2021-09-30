#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
"""
205. Isomorphic Strings Easy

2134

486

Add to List

Share Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get
t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add" Output: true Example 2:

Input: s = "foo", t = "bar" Output: false Example 3:

Input: s = "paper", t = "title" Output: true


Constraints:

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
# @lc code=start


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        st = set()

        i = 0
        j = 0

        while i < len(s):
            # if char of s in dict
            if s[i] in d:
                # if s != t, return False
                if d[s[i]] != t[j]:
                    return False
            else:
                # if t in set, return False
                if t[j] in st:
                    return False
                else:
                    # update d and set
                    d[s[i]] = t[j]
                    st.add(t[j])
            i += 1
            j += 1

        return True
# @lc code=end
