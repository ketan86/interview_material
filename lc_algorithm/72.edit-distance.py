#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        To find the min distance we can use following approach.

        1. if last char of the word1 is same as word2. we can reduce the problem
           size to n-1.
           ro
           ho
           - 'o' is same so we only have to take care of the r -> h
            transformation


        2. If last char of the word1 is not same as word2. we can do three
           operations.
            1. insert
            2. delete
            3. substitute

            we have to choose the min of those three operations to find the min
            distance
            e.g. s="horse", t="ros"
            min(
                delete(s[:-2], t[:])
                substitute(s[:-2], t[:-2])
                insert(s[:], t[:-2])
            )

                '' r   o   s    (target)
            ''  0  1   2   3
            h   1  x
            o   2
            r   3
            s   4
            e   5

            word1 -> '', word2 -> ''   = 0 operation to match target
            word1 -> '', word2 -> 'r'  = 1 insert operation to match target
            word1 -> '', word2 -> 'ro' = 1 insert operation on top of previous
                to match target
            word1 -> '', word2 -> 'ros' = 1 insert operation on top of previous
                to match target
                ...
            word1 -> 'h', word2 -> '' = 1 delete operation
            word1 -> 'ho', word2 -> '' = 2 delete operation
            word1 -> 'hor', word2 -> '' = 3 delete operation
                ...

            word1 -> 'h', word2 -> 'r' = 1 + min('' -> 'r', '' -> '', 'h' -> '') 
        """
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(
                            dp[i][j-1],
                            dp[i-1][j],
                            dp[i-1][j-1])

        return dp[-1][-1]


print(Solution().minDistance('horse', 'ros'))
# @lc code=end
