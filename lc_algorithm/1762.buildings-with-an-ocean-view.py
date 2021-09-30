"""
1762. Buildings With an Ocean View
Medium

154

26

Add to List

Share
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
Example 4:

Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109
"""


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []

        # find right max height
        right_max_array = self.find_right_maximum(heights)

        # if current height at current index is greater than max height,
        # ocean view is possible.
        for i in range(len(heights) - 1):
            if heights[i] > right_max_array[i]:
                result.append(i)

        # right most building will always have ocean view
        result.append(len(heights) - 1)

        return result

    def find_right_maximum(self, heights):
        right_maximum_array = [0] * len(heights)
        prev_max = 0

        for i in range(len(heights) - 2, -1, -1):
            prev_max = max(prev_max, heights[i+1])
            right_maximum_array[i] = prev_max

        return right_maximum_array
