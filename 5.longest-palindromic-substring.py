#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.04%)
# Likes:    7819
# Dislikes: 567
# Total Accepted:    1M
# Total Submissions: 3.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s):
        # if string is empty, return empty string
        if not s:
            return ''

        def expand_from_middle(s, left, right):
            # if string is empty or left index is bigger than the right.
            # return empty string.
            if not s or left > right:
                return ''

            # check if left and right indexes are in bound and char at
            # left and right indexes are matching. if it does, move
            # left to the left and right to the right.
            # when char at left and right indexes do not match, break
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # we are at the left and right indexes where chars are different.
            # return substring that is a palindrome string.
            # [left + 1 :right] -> left and right exclusive
            return s[left + 1:right]

        # set max substring to empty string
        max_substring = ''
        # iterate through the string
        for i in range(len(s)):
            # expand from the middle to find the longest substring
            # instead of finding the ith and i+j/2th index, we can
            # use (i,i) and (i, i+1) which will take care of the both
            # cases.
            # for ex, bab
            #         ^ <- ith
            #         ^ <- ith
            #         ^^ < ith and i+1th index
            # by expanding from above indexes, we will cover both
            # "b" and "ba" cases that should be covered to find the
            # longest palindrome.
            ss1 = expand_from_middle(s, i, i)
            ss2 = expand_from_middle(s, i, i + 1)

            # find the max of the ss1, ss2 and current max_substring
            max_substring = max(max_substring, ss1, ss2, key=len)

        return max_substring


# @lc code=end
