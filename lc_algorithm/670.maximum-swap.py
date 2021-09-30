#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = [int(x) for x in str(num)]
        max_i = len(num) - 1
        res = (len(num) - 1, len(num) - 1)
        
        for i in range(len(num)-1, -1, -1):
            if num[i] < num[max_i]:
                res = (i, max_i)
            if num[i] > num[max_i]:
                max_i = i
        
        prev, post = res
        num[prev], num[post] = num[post], num[prev]
        
        return int(''.join([str(x) for x in num]))

    def maximumSwap(self, num: int) -> int:
        """Runtime: 32 ms, faster than 57.26%
        O(n^2)
        """
        maximum_num = 0

        digits = list(str(num))

        for i in range(len(digits)):
            for j in range(len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                maximum_num = max(maximum_num, int(''.join(digits)))
                digits[j], digits[i] = digits[i], digits[j]

        return maximum_num

print(Solution().maximumSwap("2736"))
print(Solution().maximumSwap("9973"))
# @lc code=end

