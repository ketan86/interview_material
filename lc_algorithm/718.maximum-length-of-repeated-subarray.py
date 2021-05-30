#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.


# Example 1:

# Input: nums1 = [1, 2, 3, 2, 1], nums2 = [3, 2, 1, 4, 7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3, 2, 1].
# Example 2:

# Input: nums1 = [0, 0, 0, 0, 0], nums2 = [0, 0, 0, 0, 0]
# Output: 5


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
# Accepted
# 92, 846
# Submissions
# 183, 274

# @lc code=start
class Solution:
    def findLength(self, nums1, nums2):
        """
        Runtime: 2544 ms, faster than 91.64%

        Start calculating the matched length by checking the length saved at
        previous index diagonally.

        [        3  2  1  4  7
             [0, 0, 0, 0, 0, 0]
          1  [0, 0, 0, 1, 0, 0],
          2  [0, 0, 1, 0, 0, 0],
          3  [0, 1, 0, 0, 0, 0],
          2  [0, 0, 2, 0, 0, 0],
          1  [0, 0, 0, 3, 0, 0]
        ]

        Steps:
            1. set 2d matrix with len + 1
            2. for i in 1..len(array1) + 1:
                - for j in 1..len(array2) + 1:
                    - when both elements are same, calculate the the max length
                      of subarray by checking the prev max value. It will
                      one addition to next value.
                for ex,
                        [3,2,1] [4,3,2,1]
                                 0 1 2 3

            3. calculate the max of rows and cols to find the answer.

        """
        # N^2 solution by looping one array and checking in other array.

        # using DP,
        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n+1) for _ in range(m + 1)]

        mx = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    mx = max(mx, dp[i][j])
        return mx


# print(Solution().findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
# print(Solution().findLength(nums1=[0, 0, 0], nums2=[0, 0, 0]))

# @lc code=end
