#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
"""
46. Permutations
Medium

6444

139

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 pem

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
# @lc code=start


class Solution:
    def permute(self, nums):
        """Runtime: 68 ms, faster than 6.01%

                                  1,2,3,4
                                /      
                            1 & [2,3,4]
                                2 & [3,4] -> [3,4][4,3]
                                    |
                                    3 & [4]
                                    return [1,2,3][2,1,3][2,3,1] [1,3,2][3,1,2][3,2,1]


                                [1,2,3], index=0
                                   |
                                 i=index=0..2
                                    [1,2,3], index=1
                                        |
                                        i=index=1..2
                                            [1,2,3], index=2
                                            [1,3,2], index=3 -> save
                                    [2,1,3], index=2
                                        |
                                        i=index=2..2
                                            [2,1,3], index=3 -> save

                                    [3,2,1], index=3 -> save
                                        |
                                        i=index=3
        """
        output = []

        def backtrack(index=0):
            # if all integers are used up
            if index == len(nums):
                # [:] creates a copy of the existing list
                output.append(nums[:])

            for i in range(index, len(nums)):
                # place i-th integer index
                # in the current permutation
                nums[index], nums[i] = nums[i], nums[index]
                # use next integers to complete the permutations
                backtrack(index + 1)
                # backtrack
                nums[index], nums[i] = nums[i], nums[index]

        backtrack()
        return output


print(Solution().permute([1, 2, 3]))
# @lc code=end
