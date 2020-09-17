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


class Solution:
    def isPalindrome(self, s):
        # create alpha numeric char list
        alpha_numeric = ascii_lowercase + digits

        i = 0
        j = len(s) - 1

        # single char is considered palindrome so i < j and not i <= j
        while i < j:
            # if char not alphanumeric, skip it
            if s[i].lower() not in alpha_numeric:
                i += 1
            # if char not alphanumeric, skip it
            elif s[j].lower() not in alpha_numeric:
                j -= 1
            # if chars are alphanumeric, and not same, it's not palindrome
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1

        # if it's empty or one char or if palindrome, return true
        return True

        # output = ''
        # for char in s:
        #     if char.lower() in ascii_lowercase + digits:
        #         output += char.lower()

        # i = 0
        # j = len(output) - 1

        # while i <= j:
        #     if output[i] != output[j]:
        #         return False
        #     i += 1
        #     j -= 1

        # return True


# print(Solution().isPalindrome(";  "))
# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# print(Solution().isPalindrome("race a car"))
# @lc code=end
