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
            palindromes = 0
            # if string is empty or left > right, return the
            # total_palindrome_substrings
            if not s or left > right:
                return

            # for every match, increment the total_palindrome_substrings count.
            # because, every smallest substring can be a palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1

            return palindromes

        # expand from the middle and keep counting the palindrome string.
        # for ex, "aba" -> 1. "a" total_palindrome_substrings = 1
            #                  2. "ab" total_palindrome_substrings = 1
            #               -> 1. "b" total_palindrome_substrings = 2
            #                     "aba" total_palindrome_substrings = 3
            #                  2."ba" total_palindrome_substrings = 3
            #               -> 1."a" total_palindrome_substrings = 4
            #                  2. "a " total_palindrome_substrings = 4
        for i in range(len(s)):
            total_palindrome_substrings += expand_from_middle(s, i, i)
            total_palindrome_substrings += expand_from_middle(s, i, i + 1)

        return total_palindrome_substrings

    def countSubstringsDP(self, s):
        """
        Runtime: 556 ms, faster than 12.50%

        # "abc"
            [0,1,2,3]
            i -> 1
                j -> 0..0
            i -> 2
                j -> 0..1
                "ab" -> 0
            i -> 3
                j -> 0..2
                "abc" -> 0
                    "bc" -> 0

        # "aaa"
            [0,1,3,6]
            i ->1
                j-> 0..0
            i-> 2
                j -> 0..1
                    "aa" -> 1

            i -> 3
                j -> 0..2
                    "aaa" -> 1
                    "aa" -> 1
        # "aba"
            [0,1,2,4]
            i ->1
                j-> 0..0
            i-> 2
                j -> 0..1
                    "ab" -> 0
            i -> 3
                j -> 0..2
                    "aba" -> 1 
                    "ba" -> 0
        """
        # Initiate the DP
        dp = [0] * (len(s) + 1)
        # Start from 1'st index till end. [i is a dp index]
        for i in range(1, len(s)+1):
            # increment previous count by 1 to include current curr because
            # it is a palindrome by itself.
            dp[i] = dp[i-1] + 1
            # j start from 0 till curr char(excluding current char)
            # [j from to i-1 to find substring]
            for j in range(0, i-1):
                # find if substring is palindrome or not from j to curr char.
                dp[i] += self._is_palindrome(s[j:i])
        # return last count
        return dp[-1]

    def _is_palindrome(self, s):
        return 1 if s == s[::-1] else 0


print(Solution().countSubstrings('abaddedsed'))
# @lc code=end
