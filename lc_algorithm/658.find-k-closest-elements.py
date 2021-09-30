#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        """
        Instead of finding target and then explanding the search on both side,
        we can find the start.
        """
        # start index boundaries would be between 0 and n - k considering
        # that start could be at n - k till n.
        start = 0
        end = len(arr) - k

        while start < end:
            mid = start + (end - start) // 2

            # [1,2,3,4,5,6,7,8,9] -> k = 3, x = 2
            #  ^           ^
            #        ^(mid) 
            # 
            # if diff between x to mid > mid + k and x, start in in right
            if x - arr[mid] > arr[mid + k] - x:
                start = mid + 1
            else:
                end = mid 

            return arr[start:start + k]

        
# @lc code=end

