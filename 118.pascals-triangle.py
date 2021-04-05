#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (47.42%)
# Likes:    989
# Dislikes: 87
# Total Accepted:    318.6K
# Total Submissions: 645.2K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#

# @lc code=start


class Solution:
    def generate(self, numRows):
        """Runtime: 12 ms, faster than 100.00%"""
        arr = []
        for i in range(numRows):
            arr.append([])
            for j in range(i + 1):
                # when i ==0 (one time only for first row), j will be 0 too and
                # loop will exit so dont need i==0.
                if j == 0 or j == i:
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
        return arr


# print(Solution().generate(10))
# @lc code=end
