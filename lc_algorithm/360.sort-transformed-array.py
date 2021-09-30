"""
360. Sort Transformed Array
Medium

427

124

Add to List

Share
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.

 

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
 

Constraints:

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order.
 

Follow up: Could you solve it in O(n) time?

Accepted
42,118
Submissions
83,182
"""


class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        """
        If we plot the transformed array, it would form a parabola. 
        If a > 0, the two ends will be higher than the center. 
            So do a merge sort - move from both ends of the transformed 
            array towards the center.
        if a > 0, choose the bigger element and put it at the end of the 
            resulting array,
            i.e. fill the array from right to left. 
        If a < 0, merge the elements from left to right.
        """
        result = []
        if not nums:
            return result

        # first create unsorted version
        nums = [a*num*num + b*num + c for num in nums]

        left = 0
        right = len(nums) - 1
        """
        [9, 3, 15, 33]      -> [33,15,9,3] -> [3,9,15,33]
         ^         ^
        """
        while left <= right:
            if (a > 0 and nums[left] > nums[right]) or\
                    (a <= 0 and nums[left] < nums[right]):
                result.append(nums[left])
                left += 1
            else:
                result.append(nums[right])
                right -= 1

        return result if a <= 0 else result[::-1]


print(Solution().sortTransformedArray([-4, -2, 2, 4], a=1, b=3, c=5))
print(Solution().sortTransformedArray([-4, -2, 2, 4], a=0, b=3, c=5))
