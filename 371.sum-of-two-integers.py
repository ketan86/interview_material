#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.84%)
# Likes:    1069
# Dislikes: 1968
# Total Accepted:    171.9K
# Total Submissions: 339.4K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def getSum(self, a, b):
        """
        For ex (5 + 3)
        
        1 0 1 (a)
        0 1 1 (b)
        -----
              0 0 1 AND (carry)
              1 1 0 XOR (sum)
              0 1 0 (carry << 1)
        
        a = 1 1 0 (sum)
        b = 0 1 0 (carry << 1)

        b != 0 yet

        1 1 0 (a)
        0 1 0 (b)
        -----
              0 1 0 AND (carry)
              1 0 0 XOR (sum)
              1 0 0 (carry << 1)
        
        a = 1 0 0 XOR (sum)
        b = 1 0 0 (carry << 1)

        b != 0 yet

        1 0 0 (a)
        1 0 0 (b)
        -----
              1 0 0 AND (carry)
              0 0 0 XOR (sum)
            1 0 0 0 (carry << 1)

        a =   0 0 0 XOR (sum)
        b = 1 0 0 0 (carry << 1)

        b != 0 yet

        0 0 0 0 (a)
        1 0 0 0 (b)
        ------
            0 0 0 0 AND (carry)
            1 0 0 0 XOR (sum)
            0 0 0 0 0 (carry << 1)

        a = 1 0 0 0 XOR (sum)
        b = 0 0 0 0 0 (carry << 1)

        b == 0 **break**

        return a (8)

        """
        carry = 0
        # until b == carry is not 0, keep adding carry to sum(a)
        while (b != 0):
            # AND of a & b with left shift gives carry.
            carry = a & b
            # XOR of a & b gives sum. add carry to sum in the next
            # iteration.
            a = a ^ b
            # assign left shifted carry value to b for next sum.
            print('carry', bin(carry))
            b = carry << 1
            print('b', bin(b))
        return a

print(Solution().getSum(2, 5))
# @lc code=end

