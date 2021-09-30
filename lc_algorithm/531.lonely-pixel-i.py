"""
531. Lonely Pixel I Medium

252

33

Add to List

Share Given an m x n picture consisting of black 'B' and white 'W' pixels,
return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position
where the same row and same column don't have any other black pixels.

Example 1:


Input: picture = [
    ["W","W","B"],
    ["W","B","W"],
    ["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
Example 2:


Input: picture = [
    ["B","B","B"],
    ["B","B","B"],
    ["B","B","B"]]
Output: 0
 

Constraints:

m == picture.length
n == picture[i].length
1 <= m, n <= 500
picture[i][j] is 'W' or 'B'.
"""

from collections import defaultdict


class Solution:
    def findLonelyPixel(self, picture) -> int:
        """Runtime: 484 ms, faster than 36.92%"""

        row_dict = defaultdict(int)
        col_dict = defaultdict(int)

        # row_dict( < class 'int' > , {0: 1, 1: 1, 2: 1})
        # col_dict( < class 'int' > , {2: 1, 1: 1, 0: 1})
        # store number of instances of B in each row and col
        for row in range(len(picture)):
            for col in range(len(picture[row])):
                if picture[row][col] == 'B':
                    row_dict[row] += 1
                    col_dict[col] += 1

        count = 0
        for row in range(len(picture)):
            for col in range(len(picture[row])):
                if picture[row][col] == 'B':
                    # only this instance of the B should be present so
                    # checking of both dict had value to 1 should make
                    # sure there are no instances of B anywhere else
                    # in that row and col.
                    if row_dict[row] == 1 and col_dict[col] == 1:
                        count += 1

        return count


print(Solution().findLonelyPixel(
    [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]))
print(Solution().findLonelyPixel(
    [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]]))
