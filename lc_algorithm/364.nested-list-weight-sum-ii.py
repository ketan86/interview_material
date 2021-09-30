# You are given a nested list of integers nestedList. Each element is either an
# integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For
# example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to
# its depth. Let maxDepth be the maximum depth of any integer.

# The weight of an integer is maxDepth - (the depth of the integer) + 1.

# Return the sum of each integer in nestedList multiplied by its weight.


# Example 1:


# Input: nestedList = [[1,1],2,[1,1]] Output: 8 Explanation: Four 1's with a
# weight of 1, one 2 with a weight of 2. 1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8 Example
# 2:


# Input: nestedList = [1,[4,[6]]] Output: 17 Explanation: One 1 at depth 3, one
# 4 at depth 2, and one 6 at depth 1. 1*3 + 4*2 + 6*1 = 17


# Constraints:

# 1 <= nestedList.length <= 50 The values of the integers in the nested list is
# in the range [-100, 100]. The maximum depth of any integer is less than or
# equal to 50.

from typing import List
from collections import deque

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


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
    def depthSumInverse(self, nested_list: List[NestedInteger]) -> int:
        """
        Runtime: 28 ms, faster than 89.26%

        For each integer in the list, the final result is 
        integer * (maxDepth - (the depth of the integer) + 1) 
            => integer * maxDepth + integer * (1 - depth)

        The second part (1 - depth) * integer can be calculated as we traverse.
        And the first part is integer * maxDepth for each integer, which is
        actually sum(every integer * maxDepth) => sum(all integers) * maxDepth
        So we need to accumulate every integer to get the sum of all integers
        while we traverse. Once we completes traversal, we will know have both
        sum(all integers) and maxDepth in hand.


        weight = max_depth - depth of the integer + 1


        weighted_sum = sum(weight * interger)
                           /     \
                sum((max_depth  +   (1 - depth_of_integer))  * interger value)
                    |
                sum(max_depth   * integer_value + (1 - depth_of_integer) * integer_value)
                    |               |                            |
                sum(max_depth   * integer_value + integer_value - (depth_of_integer * integer_value))
                    |               |                             |
                sum(max_depth   * integer_value) + sum(integer_value) - sum(depth_of_integer * integer_value)
                    |
                sum(interger_value) * ( max_depth + 1) - sum(depth_of_integer * integer_value)

        """
        max_depth = 0
        integer_sum = 0
        integer_weighted_sum = 0

        # unpack nested integers object into queue
        queue = deque((i, 1) for i in nested_list)

        while queue:
            ni, depth = queue.popleft()
            # keep calculating the max depth
            max_depth = max(max_depth, depth)
            if ni.isInteger():
                # find the weighted sum by adding each depth.
                integer_weighted_sum += ni.getInteger() * depth
                # calculate the integer sum
                integer_sum += ni.getInteger()
            else:
                for item in ni.getList():
                    queue.append((item, depth+1))

        return integer_sum * (max_depth + 1) - integer_weighted_sum

        # max_depth = 0
        # integer_sum = 0
        # partial_weighted_sum = 0

        # # unpack nested integers object into queue
        # queue = deque((i, 1) for i in nested_list)

        # while queue:
        #     ni, depth = queue.popleft()
        #     # keep calculating the max depth
        #     max_depth = max(max_depth, depth)
        #     if ni.isInteger():
        #         # find the weighted sum by adding each depth.
        #         partial_weighted_sum += ni.getInteger() * (1-depth)
        #         # calculate the integer sum
        #         integer_sum += ni.getInteger()
        #     else:
        #         for item in ni.getList():
        #             queue.append((item, depth+1))
        # return partial_weighted_sum + integer_sum * max_depth
