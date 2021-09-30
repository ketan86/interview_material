#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        # divide the number in half and iterate from -ve to +ve
        half = n // 2
        for i in range(-half, half+1):
            # for even numbers, do no include 0.
            if i == 0 and n % 2 == 0:
                continue
            result.append(i)

        return result
# @lc code=end
