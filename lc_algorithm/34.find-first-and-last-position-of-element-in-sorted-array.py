#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        if not nums:
            return result

        if nums[0] == target and nums[-1] == target:
            return [0, len(nums) - 1]

        left = self.bs(nums, target, True)

        # if target not found.
        if left == -1:
            return result

        right = self.bs(nums, target, False)

        return [left, right]

    def bs(self, nums, target, left):
        start = 0
        end = len(nums) - 1

        # maintain last found match
        index = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                index = mid
                if left:
                    end = mid - 1
                else:
                    start = mid + 1
        return index


print(Solution().searchRange(
    [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 9, 9], 9))
# @lc code=end
