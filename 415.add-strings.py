#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (44.31%)
# Likes:    790
# Dislikes: 236
# Total Accepted:    160.7K
# Total Submissions: 345.5K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#

# @lc code=start
class Solution:
    def addStrings(self, num1, num2):
        """
        In this problem we are using the characters ascii code to find the
        integer value. Following steps are taken.

        1. find the max length of the both string.
        2. prepend '0's before the shortest string among both.
        3. set carry value to 0.
        4. iterate over the bits one step at a time.
        5. find the sum of the first bits including carry and if sum is
           larger than 9, calculate the carry and sum (add to result)
           if not, carry is 0, and add sum to result.
        6. until we are done with all the indexes, repeat the loop.
        7. if carry is not 0 at the end, prepend the carry to result
           and return.
        """
        num1_length = len(num1)
        num2_length = len(num2)

        # find the max length of the both integer strings
        max_length = max(num1_length, num2_length)

        # prepend '0' to both strings to make them same length
        num1 = '0' * (max_length - num1_length) + num1
        num2 = '0' * (max_length - num2_length) + num2

        index = max_length - 1

        # define carry to 0
        carry = 0
        result = ''

        # reverse loop
        while index >= 0:
            # find the sum of the right most digit of both numbers with carry.
            sum_ = (ord(num1[index]) - ord('0')) \
                + (ord(num2[index]) - ord('0')) + carry

            # if sum is greater than 9, we have to add the number in the
            # result and generate the carry
            # for ex,
            #     129
            #   + 003
            #     ---
            #       12 <-   2 go to result and 1 to carry
            #       12 // 10 -> 1
            #       12 % 10  -> 2
            if sum_ > 9:
                carry = sum_ // 10
                result = str(sum_ % 10) + result
            else:
                # if sum is not greater than 9, add sum to result and
                # reset carry to 0.
                result = str(sum_) + result
                carry = 0
            # go to left digit
            index -= 1

        # if carry is left at the end, prepend that to result.
        if carry:
            result = str(carry) + result

        return result


# print(Solution().addStrings('999', '1231'))
# @lc code=end

1231
0999
0
