#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (34.65%)
# Likes:    1303
# Dislikes: 93
# Total Accepted:    140.1K
# Total Submissions: 388.8K
# Testcase Example:  '"aba"'
#
#
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
#
#
# Example 1:
#
# Input: "aba"
# Output: True
#
#
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
# Note:
#
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#
#
#

# @lc code=start


class Solution:
    def validPalindrome(self, s):
        return self.dfs(s, 0, len(s) - 1)

    def dfs(self, s, start, end, deleted=False):
        # if length of the string is 1 or empty, return True
        if len(s[start:end + 1]) <= 1:
            return True

        # if start and end index values are not same, we could
        # skip one character from left or right and make sure
        # either one is palindrome.
        if s[start] != s[end]:
            # if we have not deleted a char, we can remove left
            # or right char. else, it's not palindrome.
            if not deleted:
                deleted = True
                # 'abccd' -> 'bccd' or 'abcc' is True, return True
                if self.dfs(s, start + 1, end, deleted) \
                        or self.dfs(s, start, end - 1, deleted):
                    return True
        else:
            # if start and end index values are same, check if
            # rest of the string is palindrome or nor ?
            # 'abba' -> 'bb' True
            return self.dfs(s, start + 1, end - 1, deleted)

        return False

# print(Solution().validPalindrome('eeccccbebaeeabebccceea'))
# @lc code=end
