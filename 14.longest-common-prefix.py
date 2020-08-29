#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.95%)
# Likes:    2321
# Dislikes: 1775
# Total Accepted:    707.9K
# Total Submissions: 2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

# @lc code=start
# pylint: skip-file


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # mark shortest string a longest common prefix.
        longest_prefix = min(strs, key=len)
        # we cant find a longest command prefix greater
        # than the shorted string so iterate over the
        # shortest string and if any string that is even
        # shorter compare to shortest, that is final
        # answer.
        for i in range(len(longest_prefix)):
            # compare first char of longest prefix with
            # all string's first char and so on.
            # when we hit the point where char of a string
            # does not match the prefix char, the longest
            # prefix is the prefix till now.
            for other in strs:
                if other[i] != longest_prefix[i]:
                    return longest_prefix[:i]
        return longest_prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["a", "aa"]))
# @lc code=end
