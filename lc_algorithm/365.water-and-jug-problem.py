#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # if capacity of the jugs are enough, we cant find the target capacity
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        # target capacity % gcd(1,2) is divisible, we can find the target
        return targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0

    def gcd(self, a, b):
        """
        Greatest common divisor is 

        3 5 -> 4
        a%b 3
        5 3
        a%b 2
        3 2
        a%b 1
        2 1
        a%b 0
        1 0

        4 % 1 = 0

        2 6  -> 5
        a%b 2
        6 2
        a%b 0
        2 0

        5 % 2 = 1

        """
        print(a, b)
        if b == 0:
            return a

        print('a%b', a % b)
        return self.gcd(b, a % b)  # @lc code=end
