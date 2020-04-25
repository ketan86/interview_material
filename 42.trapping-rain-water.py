#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (44.26%)
# Likes:    5191
# Dislikes: 97
# Total Accepted:    400.7K
# Total Submissions: 868.9K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
#

# @lc code=start


class Solution:
    def trap(self, elevation_map) -> int:
        unit_of_water = 0
        for index, i in enumerate(elevation_map):
            left_highest = max(elevation_map[:index], default=0)
            right_highest = max(elevation_map[index + 1:], default=0)
            current_hight = elevation_map[index]
            # print(left_highest, current_hight, right_highest)
            if left_highest > current_hight and right_highest > current_hight:
                unit_of_water += min(
                    left_highest, right_highest) - current_hight
            # print(unit_of_water)
        return unit_of_water


# if __name__ == '__main__':
#     s = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
#     print(s)

# @lc code=end
