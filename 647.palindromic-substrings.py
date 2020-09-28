#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (59.74%)
# Likes:    2940
# Dislikes: 121
# Total Accepted:    203K
# Total Submissions: 333.5K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
#
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
#
# Example 2:
#
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
#
# Note:
#
#
# The input string length won't exceed 1000.
#
#
#
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # if string is empty, return 0 palindrome
        total_palindrome_substrings = 0
        if not s:
            return total_palindrome_substrings

        # expand from the middle
        def expand_from_middle(s, left, right):
            nonlocal total_palindrome_substrings

            # if string is empty or left > right, return the
            # total_palindrome_substrings
            if not s or left > right:
                return total_palindrome_substrings

            # for every match, increment the total_palindrome_substrings count.
            # because, every smallest substring can be a palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total_palindrome_substrings += 1
                left -= 1
                right += 1

        # expand from the middle and keep counting the palindrome string.
        # for ex, "aba" -> 1. "a" total_palindrome_substrings = 1
            #                  2. "ab" total_palindrome_substrings = 1
            #               -> 1. "b" total_palindrome_substrings = 2
            #                     "aba" total_palindrome_substrings = 3
            #                  2."ba" total_palindrome_substrings = 3
            #               -> 1."a" total_palindrome_substrings = 4
            #                  2. "a " total_palindrome_substrings = 4
        for i in range(len(s)):
            expand_from_middle(s, i, i)
            expand_from_middle(s, i, i + 1)

        return total_palindrome_substrings


print(Solution().countSubstrings('aba'))
# @lc code=end
