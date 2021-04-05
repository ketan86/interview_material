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
# pylint:skip-file


class Solution:
    def trap(self, elevation_map):
        """
        Runtime: 1748 ms
        The idea here is to find the total water we could trap over the
        current bar. It will be min of two highest bar - current height.
        """
        unit_of_water = 0
        # iterate over the elevation map
        for i in range(len(elevation_map)):
            # find the highest on left side of the current element
            left_highest = max(elevation_map[:i], default=0)
            # find the highest on the right side of the current element
            right_highest = max(elevation_map[i + 1:], default=0)
            # if both left and right highest are found, the amount of water
            # we can trap over the current bat will be min of highest - current.
            if left_highest > elevation_map[i] and \
                    right_highest > elevation_map[i]:
                unit_of_water += min(
                    left_highest, right_highest) - elevation_map[i]
        return unit_of_water

    def trap_improved(self, elevation_map):
        """
        Runtime: 60 ms, faster than 44.71%
        """
        total_water = 0
        left_max_so_far = 0
        right_max_array = [0] * len(elevation_map)

        self._fill_right_max_array(elevation_map, right_max_array)

        for i in range(len(elevation_map)):
            left_max_so_far = max(left_max_so_far, elevation_map[i])

            min_height = min(left_max_so_far, right_max_array[i])

            if min_height > elevation_map[i]:
                total_water += min_height - elevation_map[i]

        return total_water

    def _fill_right_max_array(self, arr, right_max_array):
        max_ = 0
        for i in range(len(arr)):
            j = len(arr) - 1 - i
            max_ = max(max_, arr[j])
            right_max_array[j] = max_


# print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# @lc code=end
