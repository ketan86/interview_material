#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (36.22%)
# Likes:    3645
# Dislikes: 197
# Total Accepted:    490.1K
# Total Submissions: 1.3M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#

# @lc code=start


class Solution:
    def failedWordBreak(self, s, wordDict):
        """
        This solution breaks with following example.
        ex: "aaaaaaa", ["aaaa", "aaa"]

        root@sjc-mptvf: ~/.practice $ python3 139.word-break.py
        0 1 a
        0 2 aa
        0 3 aaa
        3 3
        3 4 a
        3 5 aa
        3 6 aaa
        6 6
        6 7 a
        False

        Instead of selecting 4 a's, it selects 3 a's and hence last a can not
        be found.

        """
        n = len(s)
        word_set = set(wordDict)
        i = 0
        j = 1
        while i < n and j < n + 1:
            # print(i, j, s[i:j])
            if s[i:j] in word_set:
                if j == n:
                    return True
                i = j
            else:
                j += 1
        return False

    # *** pythonic way : nested scope ***
    # def wordBreak(self, s, wordDict):
    #     memo = {}
    #     def dfs(s):
    #         if s in memo:
    #             return memo[s]
    #         if s == "":
    #             return True
    #         for i in wordDict:
    #             if s.startswith(i):
    #                 if dfs(s[len(i):]):
    #                     memo[s] = True
    #                     return True
    #         memo[s] = False
    #         return False
    #     return dfs(s)

    def topDownWordBreak(self, s, wordDict):
        """
        Top down recursive approach with memoization.
        """
        memo = {}
        return self._dfs(s, memo, wordDict)

    def _dfs(self, s, memo, wordDict):
        """
        # one approach
        if s in memo:
            return memo[s]

        if s == '':
            return True

        for i in wordDict:
            if s.startswith(i):
                if self._dfs(s[len(i):], memo, wordDict):
                    memo[s] = True
                    return True

        memo[s] = False
        return False
        """
        # second approach

        # if word is already in memo dict, (already present in word dict)
        # return the result of that word.
        # if word is not found in word dict, it is marked not found and
        # we do not have to search that word either.

        # for ex, "dog" ["d", "g"]
        # if "og" is not found in word, we can save results and consider
        # "og" absent in the word dict for other searches in dfs.

        if s in memo:
            return memo[s]

        # if word is empty, it is considered present in the dict.
        if s == '':
            return True

        # loop over the length of the word
        # for ex,
        #            dfs(dog)
        #      /         \        \
        #   d&dfs(og)  do&dfs(g)  dog&dfs('')  <-- if "dog" is found,
        #                                       '' must return True to
        #                                       satisfy the and condition.
        #
        # loop over 1, 2, ..len(s) characters and send the 1..n, 2..n, .. n..n
        # characters for dfs search. if both conditions satisfy, we return True.
        # for ex, "d" is found and "og" is found, we found the word.
        for i in range(len(s)):
            if s[: i + 1] in wordDict and self._dfs(s[i + 1:], memo, wordDict):
                memo[s] = True
                return True
        # if word is not found, we save the results so same word is not searched
        # again.
        memo[s] = False

        return False

    def wordBreak(self, s, wordDict):
        """
        Runtime: 32 ms, faster than 93.10%

        Mark each char with True or False based on whether a string from 0
        till that char is present in the word dict or not.

        """
        word_set = set(wordDict)
        # create a dp array to hold the results of the string.
        dp = [False] * (len(s) + 1)
        # empty string would be present  in the word dict so set to True.
        dp[0] = True
        # if first char is present, mark the dp index 1 to True else False
        dp[1] = s[0] in word_set

        # "abc", ["a", "b", "c"] -> b to c
        for j in range(2, len(s) + 1):
            # j(2) at "b", 0..2
            for i in range(j + 1):
                # 0th inter: d[""] -> True and "ab" in wordset -> False
                # 1st iter: d["a"] -> True and "b" in wordset -> d[2] -> True
                # break
                # We can find the word starting from 0 to till "b".
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
                    break
        return dp[len(s)]


print(Solution().wordBreak("abc", ["a", "bc"]))
print(Solution().topDownWordBreak("abc", ["a", "b", "c"]))
# @lc code=end
