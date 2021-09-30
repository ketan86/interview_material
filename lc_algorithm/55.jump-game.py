#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (34.20%)
# Likes:    4922
# Dislikes: 364
# Total Accepted:    528K
# Total Submissions: 1.5M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i][j] <= 10^5
#
#
#

# @lc code=start
class Solution:

    def canJump(self, nums):
        """Runtime: 80 ms, faster than 94.02%

        [2, 3, 1, 1, 4]

        n = 4
        target = 4
        ti = 4

        i -> 3
        1 + 3 == 4 -> true 
            ti -> 3

        i -> 2
        1 + 2 = 3 -> true 
            ti -> 2

        i -> 1
        3 + 1 = 4 -> false 

        i -> 0
        2 + 0 = 2 -> true 
        ti -> 0

        return True
        """
        target_index = len(nums) - 1

        # target index remains on the index from where we can reach the end index
        # i moves from second last index to 0 and updates target index when
        # there is a path form i to target index.

        # start from second last index till 0
        for i in range(len(nums) - 2, -1, -1):
            # if current index value and index is greater than the target index,
            # we can reach target index from the current index, so set the
            # target index to i.
            if nums[i] + i >= target_index:
                target_index = i

        return target_index == 0

    def canJumpBitComplicated(self, nums) -> bool:
        """Runtime: 80 ms, faster than 94.02%"""
        # Greedy approach to find the path.

        # start with the last index
        last_index = len(nums) - 1

        #   <len(nums) - 1>, <-1>,                                    <-1>
        #   <last index>,    <0 (inclusive) (till -1 to include 0)>  ,<reversed>
        for i in range(len(nums) - 1, -1, -1):
            # if current index value is greater or equal to the
            # diff of the last index and current index, we could
            # reach the last index so last index is moved to
            # current index.
            if nums[i] >= last_index - i:
                last_index = i

        # by taking the above approach, if we landed on the first position,
        # we know there is path from first to last index.
        return last_index == 0

    def canJumpDfsTimeLimitExceeded(self, nums: List[int]) -> bool:
        memo = {}
        return self.dfs(nums, index=0, memo=memo)

    def dfs(self, nums, index, memo):
        """
                        [2,3,1,1,4]

                    loop(2) & [2,3,1,1,4]
                                 ^
                loop(3) [2,3,1,1,4]   loop(1) [2,3,1,1,4]
                             ^                       ^
                        ....
                find last index, return True else False
        """
        # if we reach the last index, we found path
        if index == len(nums) - 1:
            return True

        # if out of bound, return False
        if index >= len(nums):
            return False

        # if index is found in memo, return the result stored at
        # that index. result indicates wether there is a path to
        # last index or not.
        if index in memo:
            return memo[index]

        # traverse 1..index steps from the current index because
        # we could take minimum 1 and max of index value steps.

        # min(nums[index] + 1, len(nums)) ensures that if the value
        # at the index is greater than the length, we don't want to
        # continue.
        for i in range(1, min(nums[index] + 1, len(nums))):
            # if in either direction, we find the path to last index,
            # return immediately.
            if self.dfs(nums, index + i, memo):
                return True

        # if path was not found, (did not return), we can save the results
        # and use it.
        # we use index as key instead of the nums[index] because nums[index]
        # can be duplicate.
        memo[index] = False

        # return False if no path was found from current index.
        return False


# @lc code=end
