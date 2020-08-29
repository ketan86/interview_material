#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (32.01%)
# Likes:    665
# Dislikes: 1941
# Total Accepted:    392.4K
# Total Submissions: 1.2M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#

# @lc code=start
# pylint: skip-file

from string import ascii_lowercase, digits
from collections import deque


class Solution:
    def isPalindrome(self, s):
        output = ''
        for char in s:
            if char.lower() in ascii_lowercase + digits:
                output += char.lower()

        i = 0
        j = len(output) - 1

        while i <= j:
            if output[i] != output[j]:
                return False
            i += 1
            j -= 1

        return True


print(Solution().isPalindrome(";  "))
# @lc code=end
