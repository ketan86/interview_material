#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.72%)
# Likes:    2323
# Dislikes: 2559
# Total Accepted:    366.9K
# Total Submissions: 1.5M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z can be encoded into numbers using the
# following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back
# into letters using the reverse of the mapping above(there may be multiple ways).
# For example, "11106" can be mapped into:

# "AAJF" with the grouping(1 1 10 6)
# "KJF" with the grouping(11 10 6)
# Note that the grouping(1 11 06) is invalid because "06" cannot be mapped into
# 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.


# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF"
# (2 2 6).
# Example 3:

# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of
# which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be
# mapped.
# Example 4:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero
# ("6" is different from "06").


# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# @lc code=start
from collections import defaultdict
from string import ascii_uppercase


class Solution:
    def numDecodingsWithoutDict(self, s):

        # map to store the already computed results.
        memo = {}

        def dfs(s):
            """
            try all possible combinations

                                226 
                        /                     \
                    "2" & "26"                ...
                          / \
                "2" & "6"    "26" & ""
                    / 
            "6" and ""     

            """
            # if string results are already stored, return the results
            if s in memo:
                return memo[s]

            # if string is empty, return 1
            if s == '':
                return 1

            total_ways = 0
            for i in range(len(s)):
                # split string in two sections
                first, second = s[: i + 1], s[i + 1:]
                # if first string does not start with 0 and value of
                # first string is less than or equal to 26, combinations
                # are possible with second string.
                if not first.startswith("0") and int(first) <= 26:
                    # add all values into total ways
                    total_ways += dfs(second)
            # store results
            memo[s] = total_ways
            # return total ways
            return total_ways

        return dfs(s)

    def numDecodings(self, s):

        # define a map that stores int keys as string and upper case char.
        # {'1': 'A', '2': 'B', ... '26': 'Z'}
        char_dict = defaultdict(int)
        for index, num in enumerate(range(len(ascii_uppercase))):
            # NOTE:: here we store num as string.
            # if we use int and later string "01" has to convert to int,
            # it will return "1" and hence the wrong char.
            char_dict[str(num + 1)] = ascii_uppercase[index]

        # map to store the already computed results.
        memo = {}

        def dfs(s):
            """
            try all possible combinations

                                226 
                        /                     \
                    "2" & "26"                ...
                          / \
                "2" & "6"    "26" & ""
                    / 
            "6" and ""     

            """
            # if string results are already stored, return the results
            if s in memo:
                return memo[s]

            # if string is empty, return 1
            if s == '':
                return 1

            total_ways = 0
            for i in range(len(s)):
                # split string in two sections
                first, second = s[: i + 1], s[i + 1:]
                # if first string is there in map, save the return value of
                # second dfs call.
                if first in char_dict:
                    # add all values into total ways
                    total_ways += dfs(second)
            # store results
            memo[s] = total_ways
            # return total ways
            return total_ways

        return dfs(s)

    def numDecodings(self, s):
        """
        Runtime: 32 ms, faster than 65.01%

        To find the equation,
            DW()        = 1
            DW(1)       = 1
            DW(12)      =   DW(1) [n-1] + DW(2) [n]
                            DW() [n-2] + DW(12) [n-1:n]

                        = (1 + 1) = 2

            DW(123)     =   DW(12) [n-1] + DW(3) [n]   if 3 >= 1
                                - if 3 >= 1, we can use all n-1 results to form
                                a combination with digit 3
                            DW(1) [n-2] + DW(23) [n-1:n] if 12 >= 10 <= 26
                                - if 12 >=10 <= 26, we can use all n-2 combinations
                                with digit 23
                        = (2 + 1) = 3

            DW(1239)    =   DW(123) [n-1] + DW(9) [n]   if 3 >= 1
                            DW(12) [n-1] + DW(39) [n-1:n]
                                - this combination is not possible due to the fact
                                that, 39 is not a valid number.
                        = (3 + (not possible)) = 3

            ...

        For ex,

            "245"
                index ->  0  1  2  3
                dp    -> [0, 0, 0, 0]
                          1  1  2  3

                1. dp[0] -> 1
                2. dp[1] = 2 can be decoded as B so set to 1 and if leading 0, 
                    then 0.
                3. we start from second char because we have to check current
                   and combination with prev.
                   - check single char that is greater than 0. we don't have
                     to check boundaries because single char can always be
                     decoded if greater than 0.
                        dp[2] += dp[1]
                   - check combination with prev that is >= 10 and <= 26
                        - combination may contain 0 for ex, 10
                            dp[2] += dp[0]
                4. return last index values
        """

        dp = [0] * (len(s) + 1)
        # assume no way of decoding is one way
        dp[0] = 1
        # if string is one char and it is not 0, it could be decoded one way
        dp[1] = 0 if s[0] == '0' else 1

        # from 2..n+1
        for i in range(2, len(s) + 1):
            # NOTE:: one thing to note here is that, we use string to compare
            # the values and it works because it is compared lexicographically.
            # In[13]: '9' > '1'
            # Out[13]: True

            # we only use n-1 combinations, if current digit is >= 1
            if s[i - 1:i] >= '1':
                dp[i] += dp[i - 1]
            # we only use n-2 combinations, if current digit is >=10 & <=26
            if s[i - 2:i] >= '10' and s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[-1]


# print(Solution().numDecodings("22642"))
# @lc code=end
