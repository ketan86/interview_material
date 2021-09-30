#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
"""
65. Valid Number
Hard

156

315

Add to List

Share
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: [
    "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", 
    "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", 
    "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
Accepted
219,295
Submissions
1,313,199
"""

# @lc code=start


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
            "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
        Invalid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3",
            "95a54e53"].
        """
        seen_digit = False
        # can only occur once
        seen_exponent = False
        seen_dot = False

        for index, char in enumerate(s):
            # we can have any number of digits
            if char.isdigit():
                seen_digit = True
            # if we find + or -, it can be in first position or after 'e' or 'E'
            # "-.9", "3e+7"
            elif char in ('+', '-'):
                if index > 0 and s[index-1] != 'e' and s[index-1] != 'E':
                    return False
            # if we find 'e' or 'E', we should have not seen those first,
            # and digit must be seen before that.
            # only onces after digits, "3e+7"
            elif char in ('e', 'E'):
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # digits must be seen after 'e' or 'E'
                seen_digit = False
            # if '.', dot and exponent must not be seen again
            # before exponent and only once. "53.5e93", "4."
            elif char == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            # anything other than that, should return false
            else:
                return False

        # NOTE: if digit are not seen after exponent, then fail.
        # digit must not be the last one. ("4.") -> valid
        return seen_digit


print(Solution().isNumber("+53.5e93+"))
# @lc code=end
