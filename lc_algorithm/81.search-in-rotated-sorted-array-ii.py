#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
"""
81. Search in Rotated Sorted Array II Medium

2354

601

Add to List

Share There is an integer array nums sorted in non-decreasing order (not
necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index
k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1],
..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example,
[0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
[4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if
target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 0
Output: true
Example 2:

Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

"""
# @lc code=start


class Solution:

    def search(self, nums, target: int) -> bool:
        """
        Time -> O(log n)
        """
        start = 0
        end = len(nums) - 1

        if target == nums[start]:
            return True

        if target == nums[end]:
            return True

        while start <= end:
            """
            If we had not deleted duplicates from both sides, mid would
            have been 1 and both sides seem sorted when compared with
            start element.

            [1, 4, 5, 6, 1, 1, 1, 1, 1]
                         ^

            so delete duplicates from both sides and then calculate the mid

            [1, 4, 5, 6, 1] 1, 1, 1, 1
                   ^

            wohhoo it works as prob 33 target in sorted rotated array (distinct). 
            """
            # remove duplicates
            while start < end and nums[start] == nums[start + 1]:
                start += 1

            while start < end and nums[end] == nums[end - 1]:
                end -= 1
            # end of remove duplicate

            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True

            # left sorted array
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # right sorted array
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False
# @lc code=end
