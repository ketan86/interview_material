"""
1229. Meeting Scheduler Medium

452

21

Add to List

Share Given the availability time slots arrays slots1 and slots2 of two people
and a meeting duration duration, return the earliest time slot that works for
both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty
array.

The format of a time slot is an array of two elements [start, end] representing
an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect
with each other. That is, for any two time slots [start1, end1] and [start2,
end2] of the same person, either start1 > end2 or start2 > end1.



Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]],
duration = 8 Output: [60,68] Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]],
duration = 12 Output: []


Constraints:

1 <= slots1.length, slots2.length <= 104 slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1] slots2[i][0] < slots2[i][1] 0 <= slots1[i][j],
slots2[i][j] <= 109 1 <= duration <= 106 Accepted 35,003 Submissions 64,046

"""


class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):

        # merge all the intervals and sort
        slots1.extend(slots2)
        slots1.sort()

        merged_intervals = []
        for interval in slots1:
            # if interval can be merged, check if duration of the meeting
            # can be accommodated else merge and continue
            if merged_intervals and merged_intervals[-1][1] > interval[0]:
                start = max(merged_intervals[-1][0], interval[0])
                end = min(merged_intervals[-1][1], interval[1])
                if end - start >= duration:
                    return [start, start + duration]
                else:
                    merged_intervals[-1][1] = max(
                        merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)
        return []

#         0   10                      50      60           120   140         210
#             --------------------------      ----------------    --------------
#         ----------                          --------
#         0        15                         60    70

        # 10                     60
        # ------------------------
        #     12----17
        #         14----------50
        # [10,50],[60,120],[140,210]
