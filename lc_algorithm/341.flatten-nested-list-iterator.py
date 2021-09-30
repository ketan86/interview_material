#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import Any, List


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> List[Any]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.iterator = self.dfs(nestedList)
        self.next_value = None

    def dfs(self, nl):
        # perfrom DFS to return the values in the order (DFS processes values
        # in the level order which is not expected in this problem)
        for i in nl:
            if i.isInteger():
                yield i.getInteger()
            yield from self.dfs(i.getList())

    def next(self) -> int:
        if self.next_value is not None:
            temp = self.next_value
            self.next_value = None
            return temp

        return next(self.iterator)

    def hasNext(self) -> bool:
        try:
            self.next_value = next(self.iterator)
        except StopIteration:
            return False
        return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
