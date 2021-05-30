
"""
@lc app=leetcode id=190 lang=python3
[190] Reverse Bits

https://leetcode.com/problems/reverse-bits/description/

algorithms
Easy (32.51%)
Likes:    847
Dislikes: 318
Total Accepted:    230.7K
Total Submissions: 648.2K
Testcase Example:  '00000010100101000001111010011100'

Reverse bits of a given 32 bits unsigned integer.



Example 1:


Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100
represents the unsigned integer 43261596, so return 964176192 which its
binary representation is 00111001011110000010100101000000.


Example 2:


Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101
represents the unsigned integer 4294967293, so return 3221225471 which its
binary representation is 10111111111111111111111111111111.



Note:


Note that in some languages such as Java, there is no unsigned integer type.
In this case, both input and output will be given as signed integer type and
should not affect your implementation, as the internal binary representation
of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement
notation. Therefore, in Example 2 above the input represents the signed
integer -3 and the output represents the signed integer -1073741825.




Follow up:

If this function is called many times, how would you optimize it?
"""

# @lc code=start


class Solution:
    def reverseBits(self, n):
        """
        Runtime: 32 ms, faster than 69.32%

        To reverse bits or a 32 bit unsigned integer, find the right most
        bit of the number and right shift the number.

        (b) 0
        (a) 011 -> 1 & 1     -> 1  -> (b) (0 >> 1) | 1 = 1
                  011 >> 1   -> 01
            01  -> 1 & 1     -> 1  -> (b) (1 >> 1) | 1 = 11
                  01 >> 1    -> 0
            0   -> 0 & 1     -> 0  -> (b) (11 >> 1) | 0 = 110


        for ex,
            00000000000000000000000000001000 (4)
            00010000000000000000000000000000 (268435456)

        a = 4
        b = 0
        (a) 00000000000000000000000000001000 & 1 = 0
        (a) 00000000000000000000000000001000 >> 1 = 0000000000000000000000000000100

        b << 1 = 0
        b | 0 = 0

        (a) 0000000000000000000000000000100 & 1 = 0
        (a) 0000000000000000000000000000100 >> 1 = 000000000000000000000000000010

        b << 1 = 0
        b | 0 = 0


        (a) 000000000000000000000000000010 & 1 = 0
        (a) 000000000000000000000000000010 >> 1 = 00000000000000000000000000001

        b << 1 = 0
        b | 0 = 0

        (a) 00000000000000000000000000001 & 1 = 1
        (a) 00000000000000000000000000001 >> 1 = 0000000000000000000000000000

        b << 1 = 0
        b | 1 = 1


        **We can't stop at a == 0 because reversed number needs to append all
        remaining 0's of the a.**

        (a) 00000000000000000000000000001 & 1 = 1
        (a) 00000000000000000000000000001 >> 1 = 0000000000000000000000000000

        b << 1 = 0
        b | 1 = 1

        (a) 0000000000000000000000000000 & 1 = 0
        (a) 0000000000000000000000000000 >> 1 = 000000000000000000000000000

        b << 1 = 2
        2 | 0 = 2 

        (a) 000000000000000000000000000 & 1 = 0
        (a) 000000000000000000000000000 >> 1 = 00000000000000000000000000

        b << 1 = 4
        4 | 0 = 4

        ....

        (b) 10000000000000000000000000000 (268435456) <-- answer

        """
        INT_MAX_SIZE = 32
        reversed_number = 0
        for _ in range(INT_MAX_SIZE):
            reversed_number <<= 1
            reversed_number |= n & 1
            n >>= 1
        return reversed_number

# print(Solution().reverseBits(43261596))
# print(Solution().reverseBits(4294967293))
# @lc code=end
