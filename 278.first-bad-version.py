#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (30.90%)
# Likes:    1079
# Dislikes: 585
# Total Accepted:    319.1K
# Total Submissions: 947.3K
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# Example:
# 
# 
# Given n = 5, and version = 4 is the first bad version.
# 
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# 
# Then 4 is the first bad version. 
# 
# 
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start_index = 1
        end_index = n

        # Note: here we stop when start_index is greater than end_index
        # instead of greater or equal.
        while start_index < end_index:
            mid = start_index + ((end_index - start_index) // 2)
            # if version is bad, we have to find if any earlier version is
            # also bad but if we move end_index to mid - 1, we loose the last
            # found index where version was bad. also in the case when mid
            # was the first bad version, storing that in end_index and
            # returning later would work beacause, we would always move
            # start index to right to reach the end_index where the version
            # is bad.
            # for ex, [F F T T T], mid = 3 and end_index = 3
            #          1 2 3 4 5
            # after we find mid as 3, we are going to search in 1..3 to see if
            # any prior version was bad too but since there are none, start
            # index ends up reaching the end_index and loop breaks where
            # end_index(mid) is the start of the bad version.
            # if we had a bad version prior to index 3, end_index would have
            # moved to left anyway.
            if isBadVersion(mid):
                end_index = mid
            else:
                start_index = mid + 1

        return end_index
        
# @lc code=end

