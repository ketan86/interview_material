#
# @lc app=leetcode id=1213 lang=python3
#
# [1213] Intersection of Three Sorted Arrays
#
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/
#
# algorithms
# Easy (78.53%)
# Likes:    179
# Dislikes: 16
# Total Accepted:    29.2K
# Total Submissions: 37K
# Testcase Example:  '[1,2,3,4,5]\n[1,2,5,7,9]\n[1,3,4,5,8]'
#
# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing
# order, return a sorted array of only the integers that appeared in all three
# arrays.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
# 
# 
#

# @lc code=start
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
# @lc code=end

