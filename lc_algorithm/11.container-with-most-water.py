#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (46.13%)
# Likes:    3741
# Dislikes: 464
# Total Accepted:    425.2K
# Total Submissions: 921.7K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49.
#
#
#
# Example:
#
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#
#

# @lc code=start
# O(n2)


class Solution:
    def maxArea(self, heights):
        n = len(heights)
        max_hight = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                area = (j - i) * min(heights[i], heights[j])
                max_hight = max(max_hight, area)
        return max_hight


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


# O(n)
class Solution:
    def maxArea(self, heights):
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, area)
            # why we move smaller line ?
            # for ex, [1, 8, 6, 2, 5, 4, 8, 3, 7]
            #          i                       j
            # for 1 and 7, we can hold 8 unit of water (8-0) * min(1,7)
            # now since we moving the pointers inward, reducing j(7) would
            # result in even smaller area in both cases where j is bigger
            # than i or less than i.

            # with this logic, you can safely skip all the combinations
            # of i + 1 to j - 1 with i where area is guaranty to be less than
            # the current.

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# @lc code=end
