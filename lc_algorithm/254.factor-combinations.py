# Medium

# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4. Given an integer n, return all possible
# combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range[2, n - 1].


# Example 1:

# Input: n = 1
# Output: []
# Example 2:

# Input: n = 12
# Output: [[2, 6], [3, 4], [2, 2, 3]]
# Example 3:

# Input: n = 37
# Output: []
# Example 4:

# Input: n = 32
# Output: [[2, 16], [4, 8], [2, 2, 8], [2, 4, 4], [2, 2, 2, 4], [2, 2, 2, 2, 2]]

import math


class Solution:

    def getFactors(self, n):
        """
        Runtime: 56 ms, faster than 63.08%

        Expand last element of the current factors.

        N = 32,
        []
        [2, 16]
        [2, 2, 8]
        [2, 2, 2, 4]
        [2, 2, 2, 2, 2]
        [2, 4, 4]
        [4, 8]


        R = [[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [2, 4, 4], [4, 8]]

        Start with 32
            go from 2...sqrt(32) + 1:
                2 and 32/2 -> 16 -> save 2 and 16
                    go from 2..sqrt(16) + 1:
                        2 and 16/2 -> 8
                            go from 2..sqrt(8) + 1:
                                ...

        when array length becomes more than 0, append array + [n] to result.

        """
        result = []
        if n == 1:
            return result

        def dfs(index, n, ans):
            if len(ans) > 0:
                result.append(ans+[n])
            for i in range(index, int(math.sqrt(n))+1):
                if n % i == 0:
                    ans.append(i)
                    dfs(i, n // i, ans)
                    ans.pop()

        dfs(2, n, [])
        return result


print(Solution().getFactors(32))
print(Solution().getFactors(42))
