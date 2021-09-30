#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#

"""
1611. Minimum One Bit Operations to Make Integers Zero
Hard

184

131

Add to List

Share
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

 

Example 1:

Input: n = 0
Output: 0
Example 2:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 3:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
Example 4:

Input: n = 9
Output: 14
Example 5:

Input: n = 333
Output: 393
 

Constraints:

0 <= n <= 109
Accepted
5,109
Submissions
8,590


"""

# @lc code=start
import math


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """Runtime: 56 ms, faster than 13.60%

        1     0     0       1       0       1
        i     i-1   i-2.....................i-5

        two operations possible: 
            1. Change the rightmost (0th) bit in the binary representation of n.
                - i-5th bit to 0 if 1
            or
            2. Change the ith bit in the binary representation of n if the 
                  (i-1)th bit is set to 1 and the 
                  (i-2)th through 0th bits are set to 0.
                e.b    1     1     0       0       0       0
                       i    i-1   i-2.....................i-5
                - ith bit can be set to 0 because 
                    it's 1 and 
                    i-1 is 1 and 
                    i-2.. 0 is all 0.

        NOTE: that the number of operations for n to become 0 is the 
            same as the number of operations for 0 to become n...

        Let's see how it can be done for numbers that are powers of 2.
        1 -> 0 => 1 = 2 ^ 1 - 1 = 1
        10 -> 11 -> 01 -> ... => 2 + 1 = 2 ^ 2 - 1 = 3
        100 -> 101 -> 111 -> 110 -> 010 -> ... => 4 + 2 + 1 = 2^3 - 1 = 7
        1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> ... => 8 + 4 + 2 + 1 = 2 ^ 4 - 1 = 15
        We can find that for 2^n, it needs 2^(n+1) - 1 operations to become 0.

        Now suppose we want to know the number of operations for 1110 to
        become 0. We know it takes 15 operations for 0 to become 1000, and
        it takes 4 operations for 1000 to become 1110. We get the solution
        by 15 - 4.

        Note that 4 here is the number of operations from 1000 to become 1110,
        which is the same as the number of operations from 000 to 110
        (ignoring the most significant bit), and it can be computed recursively.
        The observation gives us: 

        minimumOneBitOperations(1110) + minimumOneBitOperations(0110) = minimumOneBitOperations(1000).

        From the above intuition, we can reduce n bit by bit, starting from the most significant bit.

        e.g. 14 (1111)

              total  diff
        14    15      min(6)
        6     7       min(2)
        2     3       min(0) 
        0     <- return 0

        ans = 11
        """
        print(n)
        # 1 to become 0, requires 1 operation
        if n <= 1:
            return n

        # count total bits to find the power of 2 number that have same bits
        # 14 -> 1000(16)
        bit = 0
        while (1 << bit) <= n:
            bit += 1

        # total operation needed for power of 2 bits to become zero is 2 ^ bits - 1
        # 16 -> 2 ^ 4 - 1 = 15
        total_operation_power_of_2 = (1 << bit) - 1

        # for 14, 14 - 8 = 6 diff
        diff = n - (1 << (bit - 1))


        return total_operation_power_of_2 - self.minimumOneBitOperations(diff)


print(Solution().minimumOneBitOperations(n=14))
# @lc code=end
