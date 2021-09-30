#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
"""
744. Find Smallest Letter Greater Than Target
Easy

750

828

Add to List

Share
Given a characters array letters that is sorted in non-decreasing order and a
character target, return the smallest character in the array that is larger
than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"
"""

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        start_index = 0
        end_index = len(letters) - 1

        if target < letters[start_index] or target >= letters[end_index]:
            return letters[start_index]

        index = -1
        while start_index <= end_index:
            mid = start_index + (end_index - start_index) // 2
            if target < letters[mid]:
                # save mid as it could be one of the possible answer
                index = mid
                end_index = mid - 1
            else:
                start_index = mid + 1

        return letters[index]


# @lc code=end
