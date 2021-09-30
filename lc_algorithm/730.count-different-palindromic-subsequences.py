#
# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#
"""
730. Count Different Palindromic Subsequences Hard

841

51

Add to List

Share Given a string s, return the number of different non-empty palindromic
subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from
the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for
which ai != bi.

Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 
    'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:

Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, 
    which is 104860361 modulo 10**9 + 7.


Constraints:

1 <= s.length <= 1000
s[i] is either 'a', 'b', 'c', or 'd'.
"""

# @lc code=start


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """
                              abca  <- 7 palindrome
                              i  j  -> i == j 
                         /     |            \
    1 palindrome   <-  (aa)1  + abc (3)          + bca -> 3 palindrome
                             i j -> i != j     i j -> i != j  
                         /     |               /     | 
       3 palindrome   <- ab +  bc - b        bc +  ca - c  -> 3 palindrome
                        /\    /\            /\    /\ 
                       a  b  b  c          b  c  c  a  

        1. if i and j are same: "aba"
            pointing to the left most and right most char of the string
           1 palindrome combining i+j together
           + find_palindrome(i+1, j) + find_palindrom(i, j-1)
                   "ab"                       "ba"
                    b repeated but "aba" also is a palindrome and one b will substitute it's answer.  

        2. if i and j are not same: "abc"

        find_palindrome(i+1, j) + find_palindrom(i, j-1) - find_palindrom(i-1, j-1) 
              "ab"                       "ba"                         "b"
                     b repeated so remove b by subtracting it

        """
        memo = {}

        def helper(s, left, right):
            if left > right:
                return 0

            if left == right:
                return 1

            if s[left:right+1] in memo:
                return 0

            if s[left] == s[right]:
                palindromes = 1 + helper(s, left + 1, right) + \
                    helper(s, left, right - 1)
            else:
                palindromes = helper(s, left + 1, right) + \
                    helper(s, left, right - 1) - \
                    helper(s, left + 1, right - 1)

            memo[s[left:right+1]] = palindromes

            return palindromes

        return helper(s, 0, len(s) - 1)


print(Solution().countPalindromicSubsequences("bccb"))
# @lc code=end
