#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        odd = 0
        even = 0
        for index, char in enumerate(s):
            even += index % 2 == int(char)
            odd += (index + 1) % 2 == int(char)
            print(char, even, odd)

        return min(odd, even)


print(Solution().minOperations('0100'))
# @lc code=end
