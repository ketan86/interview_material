#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.89%)
# Likes:    10455
# Dislikes: 606
# Total Accepted:    1.7M
# Total Submissions: 5.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        # if string is empty, return 0
        if not s:
            return 0
        # define running max length to 0
        max_length = 0
        # set first and second pointers to 0
        i = 0
        j = 0
        # char set to store all the unique chars visited so far
        char_set = set()
        # when j reches the end, the window does not have to shrink, since
        # shrinking window might give some lengths but won't be greater than
        # the last window.
        # for ex.
        #                 abbcdegdvs
        #                      ^   ^  <- max_length = 5
        # we can shirk window but since j can't move, window length never
        # going to be greater than the current max_length.
        while j < len(s):
            # if char is not in set. sub-string is still unique.
            if s[j] not in char_set:
                # add to set
                char_set.add(s[j])
                # find the max length
                max_length = max(max_length, j - i + 1)
                # expand the window
                j += 1
            else:
                # shrink window until we find the ith element value that is
                # equal to jth value to make the char in the window unique.
                while s[j] != s[i]:
                    char_set.remove(s[i])
                    i += 1
                # ith == jth, remove this and shrink the window by 1
                char_set.remove(s[i])
                i += 1

        return max_length

    # CAN NOT optimize by keeping the index value with the char in map
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_length = 1
        i = 0
        j = 1
        char_map = {s[i]: i}
        while j < len(s):
            if s[j] not in char_map:
                char_map[s[j]] = j
                max_length = max(max_length, j - i + 1)
                j += 1
            else:
                i = char_map[s[j]] + 1
                # NOTE: Only deleting the jth char is not enough.
                # all the chars until the first occurrence must be
                # removed which can not be done without shrinking
                # the window size one by one.

                del char_map[s[j]]

        return max_length


print(Solution().lengthOfLongestSubstring(' '))
# print(Solution().lengthOfLongestSubstring('abcabcbb'))
# print(Solution().lengthOfLongestSubstring('bbbbbbb'))
# print(Solution().lengthOfLongestSubstring('pwwkew'))

# @lc code=end
