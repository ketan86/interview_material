#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#
"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

1039

95

Add to List

Share
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.

"""
# @lc code=start


class Solution(object):
    def maxLength(self, arr):

        self.max_length = 0

        def backtrack(s, index):
            # Check if current string has all unique chars
            # if not, then stop backtracking further and return
            if len(s) != len(set(s)):
                return

            # Current string is valid, update maxLen value
            self.max_length = max(self.max_length, len(s))

            # Start concatenating from the next index value
            for i in range(index, len(arr)):
                backtrack(s + arr[i], i)

        backtrack("", 0)

        return self.max_length


print(Solution().maxLength(["un", "iq", "ue"]))
# @lc code=end
