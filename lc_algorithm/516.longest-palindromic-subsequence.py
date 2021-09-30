#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:

    def longestPalindromeSubseqDP(self, s: str) -> int:
        """
        Runtime: 1744 ms, faster than 63.53%

        same:
        b c b
        ^   ^ <- 2 + "c" palindrome length

        not same: exclude b and exclude a and max of both answers

        b c a
        ^   ^ <- 

        if both char are same, they will have length of 2 + helper(i+1, j -1)
        if both char are not same, max(helper(i+1, j), helper(i, j-1))


        longest palindromic subsequence for 1 char length string would be 1.
        for length = 1,
            "bbbab"
             -      1
              -     1
               -    1
                -   1
                 -  1

                 b  b  b  a  b
                 0  1  2  3  4
            b 0 [1, 0, 0, 0, 0],
            b 1 [0, 1, 0, 0, 0],
            b 2 [0, 0, 1, 0, 0],
            a 3 [0, 0, 0, 1, 0],
            b 4 [0, 0, 0, 0, 1]

        for length = 2,
             01234
            "bbbab"
             --       <- 0 and 1
              --
               --
                --

                 b  b  b  a  b
                 0  1  2  3  4
            b 0 [1, 2, 0, 0, 0],
            b 1 [0, 1, 2, 0, 0],
            b 2 [0, 0, 1, 1, 0],
            a 3 [0, 0, 0, 1, 1],
            b 4 [0, 0, 0, 0, 1]

        for length = 3,
             01234
            "bbbab"
             ---      <- 0 and 2 (2 + index 1 and 1 = 1) = 3
             *---     <- 1 and 3 max(1,2 or 2,3)
               ---


                 b  b  b  a  b
                 0  1  2  3  4
            b 0 [1, 2, 3, 0, 0],
            b 1 [0, 1, 2, *, 0],
            b 2 [0, 0, 1, 1, 0],
            a 3 [0, 0, 0, 1, 1],
            b 4 [0, 0, 0, 0, 1]


        [
            [1, 2, 3, 3, 4],
            [0, 1, 2, 2, 3],
            [0, 0, 1, 1, 3],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1]
        ]

        """
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # capture window of length 0, 1, 2 and so on..
        # iterate over the length
        for l in range(n):
            # move i from 0 till n-l
            for i in range(n-l):
                j = i + l
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][-1]

    def longestPalindromeSubseq(self, s):
        """
        NOTE: Time limit exceeds.
            "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
        same:
        b c b
        ^   ^ <- 2 + "c" palindrome length

        not same: exclude b and exclude a and max of both answers

        b c a
        ^   ^ <- 

        if both char are same, they will have length of 2 + helper(i+1, j -1)
        if both char are not same, max(helper(i+1, j), helper(i, j-1))
        """
        return self.helper(s, 0, len(s) - 1)

    def helper(self, s, left, right):
        if left > right:
            return 0
        if left == right:
            return 1

        if s[left] == s[right]:
            return 2 + self.helper(s, left + 1, right - 1)
        else:
            return max(self.helper(s, left+1, right), self.helper(s, left, right-1))

# print(Solution().longestPalindromeSubseq("bbbab"))
# print(Solution().longestPalindromeSubseqDP("bbbab"))
# print(Solution().longestPalindromeSubseq("cbbd"))
print(Solution().longestPalindromeSubseqDP("a"))
# print(Solution().longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
# @lc code=end
