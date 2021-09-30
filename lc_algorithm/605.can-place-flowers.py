#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            # if flower is not placed at current index
            # if first index or previous index was empty
            # if last index or next index is empty.
            if flowerbed[i] == 0 and \
                    (i == 0 or flowerbed[i-1] == 0) and \
                    (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                n -= 1
                if n == 0:
                    return True
                flowerbed[i] = 1

        return False

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Runtime: 164 ms, faster than 71.24%"""
        if n == 0:
            return True

        # append extra pots to flowerbed
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
# @lc code=end
