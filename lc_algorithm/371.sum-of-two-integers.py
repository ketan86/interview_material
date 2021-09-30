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
    def getSumTimeLimitExceeds(self, a, b):
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
            b = carry << 1

        return a

    def getSum(self, a: int, b: int) -> int:
        """
        Runtime: 28 ms, faster than 76.38%

        However, in python, integers can exceed 32 bits. This causes a problem
        for us! So to mitigate this, we have to:

        Make sure our integers are strictly 32 bits Juggle between 32 bit, two's
        complements.
        # 1 of making sure our intergers are strictly 32 bits.
        First, lets talk about the mask variable. Notice that it is equal to
        0b11111111111111111111111111111111. This is simply 32 bits of one's.
        This means any time the integer overflows to more than 32 bits, we do a
        & mask to set any bit greater than 32 to zero. This satisfies our
        constraint

        Second, let's deal with the MAX variable. To understand the MAX
        variable, you must understand what is two's complement. Ultimately, MAX
        = 0b01111111111111111111111111111111 is the largest 32 bit integer that
        is "positive" under the "two's complement" scheme. Thus, when we do if a
        <= MAX we are checking if a is positive. If a is greater than MAX, we
        have a "negative" number. However, since python can deal with integers
        greater than 32 bits, python assumes this negative integer is positive.
        Thus, ~(a ^ mask) allows us to juggle from the positive number to the
        negative complement, ensuring we return the correct answer.

        """
        mask = 0b11111111111111111111111111111111
        MAX = 0b01111111111111111111111111111111  # 1 sign bit

        carry = 0
        while b != 0:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)


# print(Solution().getSumTimeLimitExceeds(-1, 1))
print(Solution().getSum(-1, 2))
# print(Solution().getSum(2, 5))
# @lc code=end
