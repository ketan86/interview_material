#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (33.87%)
# Likes:    4938
# Dislikes: 339
# Total Accepted:    423.8K
# Total Submissions: 1.2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ''

        # variable that represents the number of unique characters in the map.
        # for ex,
        # pattern -> "abc" -> {a->2, b->1, c->1 }, match = 0
        # if a is found, a ->1 and match -> 0 since freq is still not 0.
        # if a is found, a ->0 and match -> 1 since freq of the char *a* is 0.
        # if b is found, b ->0 and match -> 2 and so on.
        match = 0
        freq_map = defaultdict(int)

        # initialize the map with freq of the chr from pattern string.
        for char in t:
            freq_map[char] += 1

        i = 0
        j = 0
        # initialize the variable to store the min substring use existing
        # string and add one extra character. any substring of the string would
        # be less than m.
        min_string = s + '-'

        # NOTE: can't use min_string as float('inf') because it's not a string
        # and can't be compared with new string using min function.

        # expand the window size until reaches the end.
        while j < len(s):
            # if chr found in map, reduce the freq of the char
            if s[j] in freq_map:
                freq_map[s[j]] -= 1
                # when freq goes to 0, increase the match count
                if freq_map[s[j]] == 0:
                    match += 1

            # when match count equal to length of the map. in other words, window
            # contains all the characters from the pattern.
            # 1. we found the substring so calculate min by comparing with previous
            #    string.
            # 2. reduce the widow size.

            # while loop to make sure we eliminate all the chr that are not
            # paresent in pattern and stop at the first match.
            while match == len(freq_map):
                min_string = min(min_string, s[i: j + 1], key=len)
                # keep reducing the window size, until the first char of the
                # pattern is found
                if s[i] in freq_map:
                    if freq_map[s[i]] == 0:
                        match -= 1
                    # increment the freq of the char
                    freq_map[s[i]] += 1
                i += 1
            # increment the end index
            j += 1

        # if min
        if len(min_string) > len(s):
            return ''
        return min_string


# @lc code=end
