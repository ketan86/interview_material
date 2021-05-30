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
        """
        Runtime: 484 ms, faster than 5.30% 

        We could use recursion to find if by removing one character or more
        we can still have the valid palindrome or not ?

        We only remove char when we find left and right char is not same.

        We is two pointer approach.
        1. if both char are same at start and end index, keep reducing the
           string by moving start and index by 1.
        2. if both char are not same, you could either remove left char or
           right char and make sure the remaining string is valid palindrome.
           - if either side of the string is valid palindrome, return True
        3. else return False

        Here the base condition is, if the length of the substring is 1 or 0,
        it's valid palindrome so return True.

        Since we can remove 1 char only, we have to maitain the flag that
        ensures that only one char can be removed.

        If more than one char can be remove, we can use the deleted count
        and reduce everytime we remove either left or right char.
        """
        return self.dfs(s, 0, len(s) - 1)

    def dfs(self, s, start, end, deleted=False):
        # if length of the string is 1 or empty, return True
        if start >= end:
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
