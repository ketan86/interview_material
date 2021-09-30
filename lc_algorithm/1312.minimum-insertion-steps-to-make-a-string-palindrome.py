#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Runtime: 632 ms, faster than 89.57%

        dp[i,j] stands for the minimum insertion steps to make s[i:j+1] palindrome.


        If s[i] == s[j] then dp[i,j] should be equal to dp[i+1,j-1] as no extra cost 
        needed for a palidrome string to include s[i] on the left and s[j] on the right.
        
        else, dp[i,j] take an extra 1 cost from the smaller cost between dp[i+1,j] and dp[i,j-1].
        Then the recurrence equation would be:

        dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1]) + 1

        To build a bottom-up iteration, we need to iterate all the combination of (i, j) where i < j.
        There is no need to check dp[i,i] which is 0.
        Another base case is dp[i,i-1]. This happens only when we are checking a dp[i,i+1] and s[i] == s[i+1]. This can also be set as 0 so dp[i,i+1] will be 0 correctly.
        So we can safely initialized the entire dp array to be filled with 0.

        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # left pointer starting from 0
        for j in range(n):
            # right pointer reversed j to 0.
            for i in range(j-1,-1,-1):
                # if both end char are same, we don't have to insert
                # so no extra cost
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    # min cost of the "mbad" -> +1 for last m or first "d" to make it palindromic
                    # min("bad", "mba")
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

        return dp[0][-1]
# @lc code=end

