#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.99%)
# Likes:    1781
# Dislikes: 557
# Total Accepted:    337.1K
# Total Submissions: 1.1M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
#

# @lc code=start
# pylint: skip-file

import math


class Solution:
    """
    What are Prime Numbers?

    In math, prime numbers are whole numbers greater than 1, that have only two
    factors – 1 and the number itself. Prime numbers are divisible only by the
    number 1 or itself.

    For example, 2, 3, 5, 7 and 11 are the first few prime numbers.

    0 is not prime, because you can not create any new number by having it as a
    factor. 1 was considered prime at some time, but was dropped because many
    rules for primes would need to make a special case exemption for 1 - which
    was impractical.


    """

    def countPrimes(self, n):
        count = 0
        # 0 and 1 are not prime so start with 2.
        for i in range(2, n):
            if self.is_prime(i):
                count += 1

        return count

    def is_prime(self, n):
        # to ensure the number is prime or not, divide the number from 2..n-1
        # and if divisible, return False.

        # optimized version is that if number is not divisible by sqrt(n) + 1,
        # it's not a prime number.
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # Optimized using space.
    def countPrimes(self, n):
        """
        0   1   2   3   4
        5   6   7   8   9
        10  11  12  13  14

        2 is prime, so all the multiple of 2 are marked not prime
        3 is prime, so all the multiple of 3 are marked not prime
        5 is prime, so all the multiple of 5 are marked not prime
        """
        # an array that marks all the numbers prime and later
        # non-prime based on the multiple of the prime number.
        primes = [1] * n
        count = 0
        # start from 2 to n
        for i in range(2, n):
            # if number is prime, increase the count and mark all the
            # multiple numbers a non-prime.
            if primes[i] == 1:
                count += 1
                # mark all numbers from i to n in the ith increment
                # to non prime.
                for j in range(i, n, i):
                    primes[j] = 0
        # return the count
        return count


print(Solution().countPrimes(45))
# @lc code=end
