#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# 849. Maximize Distance to Closest Person
# Medium
# You are given an array representing a row of seats where seats[i] = 1
# represents a person sitting in the ith seat, and seats[i] = 0 represents that
# the ith seat is empty(0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized.

# Return that maximum distance to the closest person.


# Example 1:


# Input: seats = [1, 0, 0, 0, 1, 0, 1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat(i.e. seats[2]), then the closest
# person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: seats = [1, 0, 0, 0]
# Output: 3
# Explanation:
# If Alex sits in the last seat(i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Example 3:

# Input: seats = [0, 1]
# Output: 1


# Constraints:

# 2 <= seats.length <= 2 * 104
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.
# Accepted
# 109, 444
# Submissions
# 244, 889
# @lc code=start
class Solution:
    def maxDistToClosest(self, seats) -> int:
        """Runtime: 272 ms, faster than 5.29%"""
        # user prev and nxt occupied index list to find the
        # min distance.
        prev = None
        nxt_occupied_index_list = self._find_nx_occupied(seats)

        # find the max distance overall
        max_distance = 0

        for index, seat in enumerate(seats):
            # if seat is occupied, set prev occupied index
            if seat == 1:
                prev = index
            else:
                # if no prev, set to float('inf')
                if prev is not None:
                    left = index - prev
                else:
                    left = float('inf')

                # find the right index using the current index and
                # looking for right index in the list
                right = nxt_occupied_index_list[index] - index

                # find max distance using min of left and right distance
                max_distance = max(
                    max_distance, min(left, right))

        return max_distance

    def _find_nx_occupied(self, seats):
        """
                                         0  1  2  3  4  5  6
        seats ->                        [1, 0, 0, 0, 1, 0, 1]
        nxt_occupied_index_list ->      [0, 4, 4, 4, 4, 6, 6]
        """
        nxt_occupied_index_list = [-1] * len(seats)

        # if no right boundary, set occupied to float('inf')
        occupied_index = float('inf')

        for index in range(len(seats) - 1, -1, -1):
            if seats[index] == 0:
                nxt_occupied_index_list[index] = occupied_index
            else:
                nxt_occupied_index_list[index] = index
                occupied_index = index

        return nxt_occupied_index_list

# @lc code=end
