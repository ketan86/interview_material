
# Easy

# Add to List

# Share
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.


# Example 1:

# Input: intervals = [[0, 30], [5, 10], [15, 20]]
# Output: false
# Example 2:

# Input: intervals = [[7, 10], [2, 4]]
# Output: true


# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti < endi <= 106
# Accepted
# 188, 804
# Submissions
# 339, 520

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        # sort interval by start and end time
        intervals.sort()

        # check for overlapping interval
        i = 1
        while i < len(intervals):
            # if overlap, return false
            if intervals[i][0] < intervals[i-1][1]:
                return False
            i += 1

        return True
