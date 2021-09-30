#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start

# O(log N)
class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left = 2
        # max sqrt wil be in the half of the actual number
        right = x // 2

        # [1,2,3,4,5,6,7,8] -> 15
        #      ^ ^
        #   when 3 * 3 < 15, left moves to 4 and hence break
        #   answer is at right.
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid

        # choose smallest number when sqrt is not exact number.
        return right


print(Solution().mySqrt(10))
# @lc code=end
