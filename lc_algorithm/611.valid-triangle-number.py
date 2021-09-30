#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        The condition for the triplets (a, b, c) representing the lengths
        of the sides of a triangle, to form a valid triangle, is that the sum of
        any two sides should always be greater than the third side alone. i.e. 
        a + b > c and b + c > a and a + c > b.

        # O(n^3)
        if nums[i] + nums[j] > nums[k] and
                nums[i] + nums[k] > nums[j] and 
                nums[j] + nums[k] > nums[i]
            count += 1


        # O(n^2)

        1. Sort the numbers, use i, j, k pointers and move k until
            i + j > k satisfies. count all the numbers and add to total.

        Time complexity : O(n^2) 
        Space complexity : O(log n). Sorting takes O(log n) space.
        """
        nums.sort()  # n log n
        count = 0
        # start from 0 till third last element
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            # set k two steps away
            k = i+2
            # move j from i+ 1 till end
            for j in range(i+1, len(nums) - 1):
                # until k is out of bound or i + j > k, move k
                # NOTE: Because numbers are sorted, k can move right until
                # the equation of i + j > k satisfies and once, k - j - 1
                # count can be added into the list.
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                # if j < k, update count
                if j < k:
                    count += k-j-1
        return count
# @lc code=end
