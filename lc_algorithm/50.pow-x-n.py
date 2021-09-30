#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Runtime: 28 ms, faster than 81.91%

        Time => O(log n) + 1
        Space => O(1)

        This solution divides iteration into half.

        for ex, 2 ** 8 -> 2*2 power 4
                          4*4 power 2
                          16*16 power 1
                          256

                2 * 10 -> n % 2 == 0:
                            res -> 1
                            temp = 4
                          10//2 -> 5 (odd)
                            res -> 4
                            temp = 4*4 = 16
                          5//2  -> 2
                            temp = 256
                          2//2  -> 1
                            res -> 256 * 4

                    pow(2,8)
                    /      \
                pow(2,4) *  pow(2,4)
                /       \
            pow(2,2) *  pow(2*2)
            /      \
           pow(2, 1) * pow(2*1)
            |              |
            x              x
        x=2, n =4

        [2 * 2 * 2 * 2]n -> 4 iteration

        ans -> 1
        temp -> 2

            temp*temp (2*2) = 4
            n//2 -> 2
            temp*temp (4*4) = 16
            n//2 -> 1
                result *= temp

        x=2, n=16     =   x 2 |     2^4 + 1


                              temp(2)      ans(1)
        #         10/2 -> 5   2*2            4*1    
        #         5/2  -> 2   4*4            
        #         2/2  -> 1   16*16          256*4
        #         1/2  -> 0   256*256        
        #                                    --------
        #                                     1024

                              temp(2)      ans(1)
        #         16/2 -> 8   2*2               
        #         8/2  -> 4   4*4            
        #         4/2  -> 2   16*16          
        #         2/2  -> 1   256*256        65536*1
        #         1/2  -> 0   65536*65536
        #                                    --------
        #                                     65536


        x=3
        n= 5   1           0        1
               1x2^2       0 x 2^1  1 x 2^0  <- multiple by x

        """
        # if n is negative
        if n < 0:
            x = 1/x
            n = -1 * n

        ans = 1
        product = x

        # # while n > 0, if n
        # while n > 0:
        #     if n % 2 != 0:
        #         ans *= product
        #     n = n//2
        #     product *= product

        while n > 0:
            if n & 1 == 1:
                ans *= product
            n >>= 1
            product *= product

        return ans


print(Solution().myPow(2.00, 16))
# @lc code=end
