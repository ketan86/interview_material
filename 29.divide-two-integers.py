#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.23%)
# Likes:    1050
# Dislikes: 4875
# Total Accepted:    261.5K
# Total Submissions: 1.6M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) =
# -2.
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
#
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
#
#
# Note:
#
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
#
#
#

# @lc code=start
# pylint: skip-file


class Solution:
    """
    2^32 is about 4.2 billion. This is a the maximum number of VALUES that a
    binary number with 32 digits (a 32-bit number) can represent.

    Those values can be any values in any range.

    In an UNSIGNED 32-bit number, the valid values are from 0 to 2^32-1
        (instead of 1 to 2^32, but the same number of VALUES, about 4.2
        billion).

    In a SIGNED 32-bit number, one of the 32 bits is used to indicate whether
        the number is negative or not. This reduces the number of values by
        2^1, or by half. This leaves 2^31, which is about 2.1 billion.
        This means the range is now about -2.1 billion to 2.1 billion.
        Same number of values, different range.

    Summary:
        = 2^32 possible values
        = 2^32 values used for negative integers
            1 bit for sign = -2^31
        = 2^32 values available for positive integers
            1..2^32 or 1-1..2^32-1 = 0..2^31
    """
    INT_MAX = (2 ** 31) - 1   # 0..2^32
    INT_MIN = -(2 ** 31)
    INT_MAX_BITS = 31

    def divide(self, dividend, divisor):
        # division is a substracting divisor n time till dividend becomes 0.
        # for ex, dividend = 10, divisor = 3  (10-3 =7-3 =4-3 =1-3 =-2)
        #                                            1     2     3   ->3 answer
        sign = 1
        if (dividend < 0 and divisor > 0) \
                or (dividend > 0 and divisor < 0):
            sign = -1

        if dividend == 0:
            return 0

        if dividend == Solution.INT_MIN and divisor == -1:
            return Solution.INT_MAX

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # # remove divisor until dividend is greater than 0
        # VERY SLOW - Time limit exceeds
        # while dividend <= divisor:
        #     dividend -= divisor
        #     quotient += 1

        # using 32 bits to find the first number where dividend is greater
        # or equal to number.
        #
        # for ex, 257 , 3
        # 3 << 31 = 6442450944 >= 257
        # 3 << 30 ..
        # 3 << 6 = 192 < 257
        #        dividend = 257 - 192 = 65
        #        quotient = 1 << 6 = 64 (64*3=192)
        # 3 << 5 = 96 > 65
        # 3 << 4 = 48 < 65
        #        dividend = 65 - 48 = 17
        #        quotient = 1 << 4 =  64 + 16 (16*3=48) = 80
        # 3 << 3 = 24 > 17
        # 3 << 2 = 12 < 17
        #        dividend = 17 - 12 = 5
        #        quotient = 1 << 2 =  80 + 4 (4*3=12) = 84
        # 3 << 1 = 6 > 5
        # 3 << 0 = 1 < 5
        #        dividend = 5 - 3 = 2
        #        quotient = 1 << 0 =  80 + 1 (1*3=3) = 85
        #
        # answer = 257/3 = 85.66666666666667 = 85
        for i in range(31, -1, -1):  # start, stop and steps
            number = divisor << i
            if dividend >= number:
                dividend -= number
                quotient += 1 << i

        return sign * quotient


# print(Solution().divide(2147483648, 1))
# @lc code=end
