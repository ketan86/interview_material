#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30

        minutes_angle = one_min_angle * minutes

        # Hour angle will be affected by minutes too so need to add
        # additional forward movement of minute hand.

        # hour % 12 to only handle 12 hour. other will remain same
        hours_angle = (one_hour_angle * (hour % 12)) + \
            (minutes * (one_hour_angle/60))

        diff = abs(hours_angle - minutes_angle)

        return min(diff, 360 - diff)
# @lc code=end
