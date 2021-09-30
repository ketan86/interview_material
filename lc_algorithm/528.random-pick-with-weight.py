#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
"""
528. Random Pick with Weight Medium

1355

2961

Add to List

Share You are given an array of positive integers w where w[i] describes the
weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in
the range [0, w.length - 1]. pickIndex() should return the integer proportional
to its weight in the w array. For example, for w = [1, 3], the probability of
picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
"""

# @lc code=start
import random


class Solution:
    """ Maintain total sum and prefix sum (i and 0..i-1) for each
    index in list.

    - find a random target using total sum * random.random() and return the 
        index where target sum is less than prefix sum.
    """

    def __init__(self, w):  # T and S -> O(n)
        """
        :type w: List[int]
        """
        self.weight_by_index = []
        self.total_weight = 0
        for weight in w:
            self.total_weight += weight
            self.weight_by_index.append(self.total_weight)

    def pickIndex(self) -> int:  # T -> O(n), S->O(1)
        """
        :rtype: int
        """
        # calculate target using total sum and random number
        target = self.total_weight * random.random()
        # run a linear search to find the target zone
        # for index, prefix_sum in enumerate(self.prefix_sums):
        #     if target < prefix_sum:
        #         return index

        low, high = 0, len(self.weight_by_index)

        print(self.weight_by_index, target)

        while low < high:
            mid = low + (high - low) // 2
            if target > self.weight_by_index[mid]:
                low = mid + 1
            else:
                high = mid

        return low


# Your Solution object will be instantiated and called as such:
obj = Solution([1,3,5,2,1,4,5])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
# @lc code=end
