#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (49.06%)
# Likes:    1451
# Dislikes: 1839
# Total Accepted:    400.1K
# Total Submissions: 791.1K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
# pylint: skip-file
class Solution:
    def missingNumber(self, nums):
        """
        **Solution 1**: Store all nums to set and loop over all numbers
                and the one that is not in the set, is missing else no missing.

                set_ = set(nums)
                for i in range(len(nums)):
                    if i not in set_:
                        return i
                return -1

        **Solution 2**: Sum all number. Because we have one missing number
                we have one extra number so the sum of those numbers - total sum
                should give us the missing number.

                for ex, [3,0,1] means the total sum is 4 but actual sum would
                be 0+1+2+3 = 6. because we have 2 missing, total sum is 4 and so
                the missing number is 6-4 = 2

                sum of 0 to n : n(n-1)/2
                sum of 1 to n : n(n+1)/2

                sum_ = sum(nums)
                n = len(nums)

                actual_sum = (n*(n+1)) // 2

                return actual_sum - sum_

        Solution 3: place numbers to it's correct position using cyclic
                sort (patters/cyclic_sort folder) and the number at the wrong
                position is missing.

                O(n2)

                for ex, [3,0,1]. 3 should move to index 3 but length is 2 so go to
                0, move 0 to 0th position and move 3 to 1st position. again 3 can not
                be moved so go to 1. move 1 to 1st position and 3 to 2nd position.
                3 again can not be move and we are done.

                Now, go over the list and if number is not it's position, return the 
                index value where number is wrong.

                n = len(nums)
                i = 0

                while i < n:
                    if nums[i] < n and nums[i] != i:
                        nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
                    else:
                        i += 1

                for i in range(nums):
                    if i != nums[i]:
                        return i
                return -1

        Solution 4: XOR property of the number. When two same numbers are XORed
                result is 0. Using this property, we can XOR all the numbers
                o to len(nums) and all give numbers. XOR the two XOR results
                and we find the missing number.

                for ex, [3,0,1]
                    0 ^ 1     ^ 3  = R1
                    ^   ^       ^
                    0 ^ 1 ^ 2 ^ 3  = R2
                    -------------
                    0 ^ 0 = 0
                    1 ^ 1 = 0
                    3 ^ 3 = 0

                    so we are left with 2.

                R1 = A1 ^ A2 ^ A4
                R2 = A1 ^ A2 ^ A3 ^ A4

                R1 ^ R2 = (A1 ^ A2 ^ A4) ^ A1 ^ A2 ^ A3 ^ A4
                        = (A1 ^ A1) ^ (A2 ^ A2) ^ A3 ^ (A4 ^ A4)
                        = 0 ^ 0 ^ A3 ^ 0 # because {A ^ A = 0}
                        = A3

        """
        # total_sum = sum(nums)
        # n = len(nums) + 1
        # return ((n * (n-1))// 2) - total_sum

        # n = len(nums)
        # i = 0
        # while i < n:
        #     j = nums[i]
        #     if j < n and nums[i] != i:
        #         nums[i], nums[j] = nums[j], nums[i]
        #     else:
        #         i += 1

        # for i in range(n):
        #     if i != nums[i]:
        #         return i
        # return -1

        n = len(nums)
        r1 = 0
        r2 = 0

        for i in nums:
            r1 ^= i

        # XOR all the elements from 0 to n+1 to include the one
        # extra number that is a replacement for the missing number.

        for i in range(n + 1):
            r2 ^= i

        return r1 ^ r2


print(Solution().missingNumber([2, 0, 1, 4]))
# @lc code=end
