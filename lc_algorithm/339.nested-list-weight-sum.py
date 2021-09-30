# You are given a nested list of integers nestedList. Each element is either an
# integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For
# example, the nested list[1, [2, 2], [[3], 2], 1] has each integer's value set
# to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.


# Example 1:


# Input: nestedList = [[1, 1], 2, [1, 1]] Output: 10 Explanation: Four 1's at
# depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10. Example 2:


# Input: nestedList = [1, [4, [6]]] Output: 27 Explanation: One 1 at depth 1,
# one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27. Example 3:

# Input: nestedList = [0] Output: 0


# Constraints:

# 1 <= nestedList.length <= 50 The values of the integers in the nested list is
# in the range[-100, 100]. The maximum depth of any integer is less than or
# equal to 50.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List
from collections import deque


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    """Runtime: 32 ms, faster than 60.74% """

    def depthSumDFS(self, nested_list: List[NestedInteger]) -> int:
        weighted_sum = 0
        if not nested_list:
            return weighted_sum

        queue = deque()

        # Put items into the queue with depth 1
        for item in nested_list:
            queue.append((item, 1))

        while queue:
            ni, depth = queue.popleft()
            # if ni is an integer, update weighted sum
            if ni.isInteger():
                weighted_sum += ni.getInteger() * depth
            else:
                # go over the list and put it in queue
                for l in ni.getList():
                    queue.append((l, depth+1))

        return weighted_sum

    def depthSumBFS(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
